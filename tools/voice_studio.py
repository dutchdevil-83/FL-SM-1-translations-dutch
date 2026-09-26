#!/usr/bin/env python3
"""Interactive terminal studio for casting, auditioning, approving, and generating game voices.

This tool deliberately keeps human approval in the loop. It reuses the canonical dialogue
manifest and character registry from voice_pipeline.py, adds persistent client-side rate
limiting, retry handling for idempotent TTS requests, provider usage/token accounting,
audio audition controls, and safe voice-design retry/delete workflows.

Local runtime state is written under voice/build/runtime/ and voice/previews/, which are
ignored by Git. Human approvals are written to voice/approvals.json so they can be reviewed
and committed deliberately.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import voice_pipeline as vp

ROOT = vp.ROOT
RUNTIME_SETTINGS_PATH = ROOT / "voice" / "runtime.local.json"
RUNTIME_DIR = ROOT / "voice" / "build" / "runtime"
RATE_STATE_PATH = RUNTIME_DIR / "rate_state.json"
USAGE_LEDGER_PATH = RUNTIME_DIR / "usage.jsonl"
VOICE_HISTORY_PATH = RUNTIME_DIR / "voice_history.jsonl"
APPROVALS_PATH = ROOT / "voice" / "approvals.json"
DESIGN_PREVIEW_DIR = ROOT / "voice" / "previews"
DIALOGUE_PREVIEW_DIR = DESIGN_PREVIEW_DIR / "dialogue"

DEFAULT_RUNTIME_SETTINGS = {
    "schema_version": 1,
    "preview_rpm": 3,
    "preview_tpm": 0,
    "final_rpm": 3,
    "final_tpm": 0,
    "voice_api_rpm": 3,
    "max_retries": 4,
    "retry_base_delay_seconds": 15.0,
    "permission_retry_delay_seconds": 65.0,
    "rate_safety_margin_seconds": 1.5,
    "demo_line_count": 5,
    "auto_play_after_generation": False,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    temp.replace(path)


def append_jsonl(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")


def load_runtime_settings() -> dict[str, Any]:
    settings = dict(DEFAULT_RUNTIME_SETTINGS)
    settings.update(read_json(RUNTIME_SETTINGS_PATH, {}))
    return settings


def save_runtime_settings(settings: dict[str, Any]) -> None:
    clean = dict(DEFAULT_RUNTIME_SETTINGS)
    for key in clean:
        if key in settings:
            clean[key] = settings[key]
    write_json_atomic(RUNTIME_SETTINGS_PATH, clean)


def prompt_yes_no(message: str, default: bool = False) -> bool:
    suffix = " [Y/n] " if default else " [y/N] "
    answer = input(message + suffix).strip().lower()
    if not answer:
        return default
    return answer in {"y", "yes", "j", "ja"}


def prompt_int(message: str, default: int, minimum: int = 1, maximum: int | None = None) -> int:
    while True:
        raw = input(f"{message} [{default}]: ").strip()
        if not raw:
            return default
        try:
            value = int(raw)
        except ValueError:
            print("Enter a whole number.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            bound = f"{minimum}..{maximum}" if maximum is not None else f">={minimum}"
            print(f"Enter a value in range {bound}.")
            continue
        return value


def prompt_float(
    message: str,
    default: float,
    minimum: float = 0.0,
    maximum: float | None = None,
) -> float:
    while True:
        raw = input(f"{message} [{default:g}]: ").strip()
        if not raw:
            return default
        try:
            value = float(raw)
        except ValueError:
            print("Enter a number.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            bound = f"{minimum:g}..{maximum:g}" if maximum is not None else f">={minimum:g}"
            print(f"Enter a value in range {bound}.")
            continue
        return value


def clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")
    elif sys.stdout.isatty():
        os.system("clear")


def short_voice_id(value: str) -> str:
    value = value or ""
    if len(value) <= 20:
        return value
    return value[:12] + "..." + value[-5:]


class PersistentRateLimiter:
    """Rolling-window RPM limiter persisted across script restarts."""

    def __init__(
        self,
        bucket: str,
        rpm: int,
        safety_margin_seconds: float,
        tpm: int = 0,
        state_path: Path = RATE_STATE_PATH,
        clock: Callable[[], float] = time.time,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        if rpm < 1:
            raise ValueError("rpm must be >= 1")
        self.bucket = bucket
        self.rpm = rpm
        self.tpm = max(0, int(tpm))
        self.safety_margin_seconds = max(0.0, safety_margin_seconds)
        self.state_path = state_path
        self.clock = clock
        self.sleeper = sleeper

    @staticmethod
    def compute_wait(
        timestamps: list[float],
        now: float,
        rpm: int,
        safety_margin_seconds: float,
    ) -> float:
        recent = sorted(ts for ts in timestamps if ts > now - 60.0)
        if not recent:
            return 0.0

        waits = [0.0]
        minimum_spacing = 60.0 / rpm + safety_margin_seconds
        waits.append(recent[-1] + minimum_spacing - now)

        if len(recent) >= rpm:
            waits.append(recent[-rpm] + 60.0 + safety_margin_seconds - now)

        return max(0.0, max(waits))

    @staticmethod
    def compute_tpm_wait(
        token_events: list[dict[str, float]],
        now: float,
        tpm: int,
        requested_tokens: int,
        safety_margin_seconds: float,
    ) -> float:
        if tpm <= 0 or requested_tokens <= 0:
            return 0.0
        recent = sorted(
            (
                {"ts": float(item["ts"]), "tokens": max(0, int(item["tokens"]))}
                for item in token_events
                if float(item.get("ts", 0)) > now - 60.0
            ),
            key=lambda item: item["ts"],
        )
        current = sum(item["tokens"] for item in recent)
        if current + requested_tokens <= tpm:
            return 0.0

        remaining = current
        for item in recent:
            remaining -= item["tokens"]
            if remaining + requested_tokens <= tpm:
                return max(
                    0.0,
                    item["ts"] + 60.0 + safety_margin_seconds - now,
                )
        return 60.0 + safety_margin_seconds

    def _load(self) -> dict[str, Any]:
        return read_json(self.state_path, {"schema_version": 1, "buckets": {}})

    def _save(self, state: dict[str, Any]) -> None:
        write_json_atomic(self.state_path, state)

    def wait(self, estimated_tokens: int = 0) -> float:
        total_wait = 0.0
        estimated_tokens = max(0, int(estimated_tokens))
        while True:
            state = self._load()
            buckets = state.setdefault("buckets", {})
            token_buckets = state.setdefault("token_buckets", {})
            raw = buckets.get(self.bucket, [])
            timestamps = [float(item) for item in raw if isinstance(item, (int, float))]
            now = self.clock()
            timestamps = [ts for ts in timestamps if ts > now - 60.0]

            raw_token_events = token_buckets.get(self.bucket, [])
            token_events = [
                item
                for item in raw_token_events
                if isinstance(item, dict)
                and isinstance(item.get("ts"), (int, float))
                and isinstance(item.get("tokens"), (int, float))
                and float(item["ts"]) > now - 60.0
            ]

            rpm_wait = self.compute_wait(
                timestamps,
                now,
                self.rpm,
                self.safety_margin_seconds,
            )
            tpm_wait = self.compute_tpm_wait(
                token_events,
                now,
                self.tpm,
                estimated_tokens,
                self.safety_margin_seconds,
            )
            wait_seconds = max(rpm_wait, tpm_wait)
            if wait_seconds <= 0.001:
                timestamps.append(now)
                buckets[self.bucket] = timestamps[-max(self.rpm * 3, 20):]
                if estimated_tokens > 0:
                    token_events.append({"ts": now, "tokens": estimated_tokens})
                token_buckets[self.bucket] = token_events[-200:]
                self._save(state)
                return total_wait

            dimensions = [f"{self.rpm} RPM"]
            if self.tpm > 0:
                dimensions.append(f"{self.tpm} TPM")
            print(
                f"[rate-limit] {self.bucket}: waiting {wait_seconds:.1f}s "
                f"to stay within {' / '.join(dimensions)}."
            )
            self.sleeper(wait_seconds)
            total_wait += wait_seconds


def parse_http_status(exc: BaseException) -> int | None:
    for name in ("status_code", "status"):
        value = getattr(exc, name, None)
        if isinstance(value, int):
            return value
    text = str(exc)
    for pattern in (
        r"Error code:\s*(\d{3})",
        r"Status\s+(\d{3})",
        r'"code"\s*:\s*(\d{3})',
        r"'code'\s*:\s*(\d{3})",
    ):
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def classify_api_error(exc: BaseException) -> str:
    status = parse_http_status(exc)
    message = str(exc).lower()
    if "api_key_invalid" in message or "api key not valid" in message:
        return "auth"
    if status == 429 or "resource_exhausted" in message:
        return "rate_limit"
    if status == 403 and (
        "permission_denied" in message or "does not have permission" in message
    ):
        return "permission"
    if status in {408, 500, 502, 503, 504}:
        return "transient"
    if isinstance(exc, (TimeoutError, ConnectionError)):
        return "transient"
    return "fatal"


def api_call_with_retry(
    action: Callable[[], Any],
    *,
    limiter: PersistentRateLimiter,
    settings: dict[str, Any],
    label: str,
    idempotent: bool,
    retry_permission: bool = False,
    estimated_tokens: int = 0,
) -> tuple[Any, int]:
    max_retries = int(settings["max_retries"]) if idempotent else 0
    base_delay = float(settings["retry_base_delay_seconds"])
    permission_delay = float(settings["permission_retry_delay_seconds"])
    attempt = 0

    while True:
        attempt += 1
        limiter.wait(estimated_tokens=estimated_tokens)
        started = time.perf_counter()
        try:
            result = action()
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            return result, elapsed_ms
        except Exception as exc:
            kind = classify_api_error(exc)
            retry = False
            delay = base_delay * (2 ** max(0, attempt - 1))

            if kind == "rate_limit":
                retry = attempt <= max(1, max_retries)
                delay = max(delay, 60.0 / limiter.rpm + limiter.safety_margin_seconds)
            elif idempotent and kind == "transient":
                retry = attempt <= max_retries
            elif idempotent and retry_permission and kind == "permission":
                retry = attempt <= max_retries
                delay = max(delay, permission_delay)

            if not retry:
                raise

            print(
                f"[retry] {label}: {kind} error on attempt {attempt}; "
                f"waiting {delay:.1f}s before retry."
            )
            time.sleep(delay)


def object_to_mapping(value: Any) -> dict[str, Any]:
    if value is None:
        return {}
    if isinstance(value, dict):
        return value
    for method_name in ("model_dump", "to_dict", "dict"):
        method = getattr(value, method_name, None)
        if callable(method):
            try:
                result = method()
            except TypeError:
                continue
            if isinstance(result, dict):
                return result
    return {}


def field_value(value: Any, name: str, default: Any = None) -> Any:
    if isinstance(value, dict):
        return value.get(name, default)
    return getattr(value, name, default)


def modality_token_count(usage: Any, field: str, modality: str) -> int:
    items = field_value(usage, field, []) or []
    total = 0
    for item in items:
        item_modality = str(field_value(item, "modality", "")).lower()
        if item_modality == modality.lower():
            total += int(field_value(item, "tokens", 0) or 0)
    return total


def extract_provider_usage(interaction: Any, text: str) -> dict[str, Any]:
    usage = field_value(interaction, "usage")
    estimated = max(1, math.ceil(len(text) / 4)) if text else 0
    if usage is None:
        return {
            "usage_source": "estimated",
            "estimated_input_tokens": estimated,
            "total_input_tokens": None,
            "total_output_tokens": None,
            "total_tokens": None,
            "input_text_tokens": None,
            "output_audio_tokens": None,
        }

    return {
        "usage_source": "provider",
        "estimated_input_tokens": estimated,
        "total_input_tokens": field_value(usage, "total_input_tokens"),
        "total_output_tokens": field_value(usage, "total_output_tokens"),
        "total_tokens": field_value(usage, "total_tokens"),
        "input_text_tokens": modality_token_count(
            usage, "input_tokens_by_modality", "text"
        ),
        "output_audio_tokens": modality_token_count(
            usage, "output_tokens_by_modality", "audio"
        ),
    }


def usage_suffix(usage: dict[str, Any]) -> str:
    if usage.get("usage_source") == "provider":
        return (
            f"tokens in={usage.get('total_input_tokens', '?')} "
            f"audio={usage.get('output_audio_tokens', '?')} "
            f"total={usage.get('total_tokens', '?')}"
        )
    return f"estimated input tokens~{usage.get('estimated_input_tokens', '?')}"


def log_usage(
    *,
    action: str,
    model: str,
    speaker: str = "",
    row_id: str = "",
    status: str,
    latency_ms: int | None = None,
    text: str = "",
    usage: dict[str, Any] | None = None,
    error: str = "",
) -> None:
    record: dict[str, Any] = {
        "timestamp": utc_now(),
        "action": action,
        "model": model,
        "speaker": speaker,
        "row_id": row_id,
        "status": status,
        "latency_ms": latency_ms,
        "text_chars": len(text),
        "text_words": len(text.split()) if text else 0,
    }
    if usage:
        record.update(usage)
    elif text:
        record["usage_source"] = "estimated"
        record["estimated_input_tokens"] = max(1, math.ceil(len(text) / 4))
    if error:
        record["error"] = error[:1000]
        record["http_status"] = parse_http_status(RuntimeError(error))
    append_jsonl(USAGE_LEDGER_PATH, record)


def play_wav(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)

    print(f"Playing: {path.relative_to(ROOT)}")
    if os.name == "nt":
        import winsound

        winsound.PlaySound(str(path), winsound.SND_FILENAME)
        return

    ffplay = shutil.which("ffplay")
    if ffplay:
        subprocess.run(
            [ffplay, "-nodisp", "-autoexit", "-loglevel", "error", str(path)],
            check=False,
        )
        return

    opener = shutil.which("open") or shutil.which("xdg-open")
    if opener:
        subprocess.run([opener, str(path)], check=False)
        return

    raise RuntimeError("No WAV playback method is available on this operating system.")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def registry_path(config: dict[str, Any]) -> Path:
    return vp.root_path(config["characters_file"])


def load_registry(config: dict[str, Any]) -> dict[str, Any]:
    return vp.read_json(registry_path(config), {"schema_version": 1, "characters": {}})


def save_registry(config: dict[str, Any], registry: dict[str, Any]) -> None:
    write_json_atomic(registry_path(config), registry)


def character_status(entry: dict[str, Any]) -> str:
    if not entry.get("enabled", True):
        return "DISABLED"
    if (entry.get("voice_ref") or "").strip():
        return f"ALIAS->{entry['voice_ref']}"
    status = (entry.get("casting_status") or "").strip().lower()
    if status == "approved":
        return "APPROVED"
    if (entry.get("voice_id") or "").strip():
        return "AUDITION"
    if status in {"rejected", "needs_identity_review"}:
        return status.upper()
    return "NEEDS VOICE"


def regenerate_casting_pack() -> None:
    commands = [
        [sys.executable, str(ROOT / "tools" / "voice_profiles.py"), "validate"],
        [sys.executable, str(ROOT / "tools" / "voice_profiles.py"), "export"],
    ]
    for command in commands:
        print("+ " + " ".join(command))
        subprocess.run(command, cwd=ROOT, check=True)


def ensure_casting_request(
    config: dict[str, Any],
    speaker: str,
    entry: dict[str, Any],
) -> tuple[Path, dict[str, Any]]:
    try:
        return vp.load_casting_request(config, speaker, entry)
    except SystemExit as first_error:
        print(f"Casting request needs refresh: {first_error}")
        regenerate_casting_pack()
        return vp.load_casting_request(config, speaker, entry)


def provider_voice_sample_path(speaker: str) -> Path:
    return DESIGN_PREVIEW_DIR / f"{speaker}.wav"


def provider_voice_metadata_path(speaker: str) -> Path:
    return DESIGN_PREVIEW_DIR / f"{speaker}.creation.json"


def save_created_voice(
    config: dict[str, Any],
    registry: dict[str, Any],
    speaker: str,
    request_path: Path,
    request: dict[str, Any],
    created: Any,
) -> str:
    voice_id = (field_value(created, "id", "") or "").strip()
    if not voice_id:
        raise RuntimeError("Gemini returned no persistent voice ID.")

    entry = registry["characters"][speaker]
    entry["voice_id"] = voice_id
    entry["casting_status"] = "audition_pending"
    save_registry(config, registry)

    DESIGN_PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    request_digest = hashlib.sha256(
        json.dumps(
            request,
            sort_keys=True,
            ensure_ascii=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()

    metadata = {
        "schema_version": 1,
        "speaker": speaker,
        "voice_id": voice_id,
        "model": request["voice"].get("model", ""),
        "display_name": request["voice"].get("display_name", ""),
        "create_time": vp.provider_time(field_value(created, "create_time")),
        "expire_time": vp.provider_time(field_value(created, "expire_time")),
        "request_file": request_path.relative_to(ROOT).as_posix(),
        "request_sha256": request_digest,
    }
    write_json_atomic(provider_voice_metadata_path(speaker), metadata)

    sample_audio = field_value(created, "sample_audio")
    sample_data = field_value(sample_audio, "data") if sample_audio is not None else None
    if sample_data:
        provider_voice_sample_path(speaker).write_bytes(vp.decode_audio_data(sample_data))

    return voice_id


def representative_rows(
    rows: list[dict[str, Any]],
    speaker: str,
    count: int,
) -> list[dict[str, Any]]:
    candidates = [
        row
        for row in rows
        if row.get("speaker") == speaker
        and row.get("status") == "ready"
        and row.get("renpy_id")
        and 18 <= len((row.get("tts_text") or "").strip()) <= 220
    ]
    if len(candidates) < count:
        candidates = [
            row
            for row in rows
            if row.get("speaker") == speaker
            and row.get("status") == "ready"
            and row.get("renpy_id")
            and (row.get("tts_text") or "").strip()
        ]
    if not candidates:
        return []

    count = min(count, len(candidates))
    chosen: list[dict[str, Any]] = []
    used_ids: set[str] = set()
    used_sources: set[str] = set()

    for index in range(count):
        target = (index + 0.5) * len(candidates) / count
        ranked = sorted(
            enumerate(candidates),
            key=lambda item: (
                item[1].get("game_source_file") in used_sources,
                abs(item[0] - target),
                abs(len(item[1].get("tts_text") or "") - 90),
            ),
        )
        for _, row in ranked:
            row_id = row["id"]
            if row_id in used_ids:
                continue
            chosen.append(row)
            used_ids.add(row_id)
            used_sources.add(row.get("game_source_file") or "")
            break

    return chosen


def create_tts_interaction(
    client: Any,
    *,
    model: str,
    voice_id: str,
    text: str,
    style: str,
    sample_rate: int,
) -> Any:
    content: dict[str, Any] = {"type": "text", "text": text}
    if style:
        content["annotations"] = [{"type": "speech_metadata", "style": style}]

    return client.interactions.create(
        model=model,
        input=[{"type": "user_input", "content": [content]}],
        response_format={
            "type": "audio",
            "mime_type": "audio/wav",
            "sample_rate": sample_rate,
        },
        generation_config={"speech_config": [{"voice": voice_id}]},
    )


def archive_local_candidate(speaker: str, voice_id: str, reason: str) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    target = RUNTIME_DIR / "rejected" / speaker / f"{stamp}-{voice_id}"
    target.mkdir(parents=True, exist_ok=True)

    for path in (
        provider_voice_sample_path(speaker),
        provider_voice_metadata_path(speaker),
    ):
        if path.exists():
            shutil.move(str(path), target / path.name)

    dialogue_dir = DIALOGUE_PREVIEW_DIR / speaker
    if dialogue_dir.exists():
        shutil.move(str(dialogue_dir), target / "dialogue")

    append_jsonl(
        VOICE_HISTORY_PATH,
        {
            "timestamp": utc_now(),
            "speaker": speaker,
            "voice_id": voice_id,
            "action": "rejected",
            "reason": reason,
            "archive": target.relative_to(ROOT).as_posix(),
        },
    )
    return target


class VoiceStudio:
    def __init__(self, config: dict[str, Any], settings: dict[str, Any]) -> None:
        self.config = config
        self.settings = settings
        self._manifest: list[dict[str, Any]] | None = None
        self._client: Any = None

    @property
    def manifest(self) -> list[dict[str, Any]]:
        if self._manifest is None:
            self._manifest = vp.load_manifest(self.config)
        return self._manifest

    @property
    def client(self) -> Any:
        if self._client is None:
            self._client = vp.create_genai_client()
        return self._client

    def limiter(self, bucket: str, rpm: int, tpm: int = 0) -> PersistentRateLimiter:
        return PersistentRateLimiter(
            bucket=bucket,
            rpm=rpm,
            tpm=tpm,
            safety_margin_seconds=float(self.settings["rate_safety_margin_seconds"]),
        )

    def choose_character(self, initial: str = "") -> str | None:
        registry = load_registry(self.config)
        characters = registry.get("characters", {})

        query = initial.strip()
        while True:
            if not query:
                query = input(
                    "Search character by token/name "
                    "(Enter = characters needing attention, q = back): "
                ).strip()
            if query.lower() in {"q", "quit", "back"}:
                return None

            if query and query in characters:
                return query

            lowered = query.lower()
            matches: list[tuple[str, dict[str, Any]]] = []
            for token, entry in characters.items():
                haystack = f"{token} {entry.get('display_name', '')}".lower()
                if lowered:
                    if lowered in haystack:
                        matches.append((token, entry))
                elif character_status(entry) in {"NEEDS VOICE", "AUDITION"}:
                    matches.append((token, entry))

            matches.sort(
                key=lambda item: (
                    character_status(item[1]) == "APPROVED",
                    character_status(item[1]).startswith("ALIAS"),
                    not item[1].get("enabled", True),
                    -(int(item[1].get("line_count") or 0)),
                    item[0],
                )
            )

            if not matches:
                print("No matching characters.")
                query = ""
                continue

            shown = matches[:30]
            print()
            for index, (token, entry) in enumerate(shown, start=1):
                print(
                    f"{index:2}. {token:<10} "
                    f"{entry.get('display_name', token)[:34]:<34} "
                    f"{int(entry.get('line_count') or 0):>6} lines  "
                    f"[{character_status(entry)}]"
                )
            if len(matches) > len(shown):
                print(f"... {len(matches) - len(shown)} more matches; narrow the search.")

            choice = input("Choose number/token, s = new search, q = back: ").strip()
            if choice.lower() == "q":
                return None
            if choice.lower() == "s":
                query = ""
                continue
            if choice in characters:
                return choice
            try:
                selected = int(choice)
            except ValueError:
                query = choice
                continue
            if 1 <= selected <= len(shown):
                return shown[selected - 1][0]
            print("Invalid selection.")

    def show_character_details(self, speaker: str) -> None:
        registry = load_registry(self.config)
        entry = registry["characters"][speaker]
        profile = entry.get("profile") or {}
        print()
        print("=" * 78)
        print(f"{speaker} - {entry.get('display_name', speaker)}")
        print("=" * 78)
        print(f"Status       : {character_status(entry)}")
        print(f"Line count   : {entry.get('line_count', 0)}")
        print(f"Enabled      : {entry.get('enabled', True)}")
        print(f"Voice ref    : {entry.get('voice_ref') or '-'}")
        print(f"Voice ID     : {entry.get('voice_id') or '-'}")
        print(f"Language     : {entry.get('language_code') or '-'}")
        print(f"Gender       : {entry.get('gender') or '-'}")
        print(f"Casting age  : {profile.get('casting_age') or '-'}")
        print(f"Accent       : {profile.get('accent') or '-'}")
        print(f"Pitch        : {profile.get('pitch') or '-'}")
        print(f"Timbre       : {profile.get('timbre') or '-'}")
        print(f"Cadence      : {profile.get('cadence') or '-'}")
        print(f"Design prompt: {entry.get('design_prompt') or '-'}")
        print()

    def create_voice(self, speaker: str) -> None:
        registry = load_registry(self.config)
        entry = registry["characters"][speaker]
        if not entry.get("enabled", True):
            print("This character is disabled.")
            return
        if entry.get("voice_ref"):
            print(f"This token reuses voice_ref={entry['voice_ref']}; create that voice instead.")
            return
        if entry.get("voice_id"):
            print("A provider voice already exists. Use Retry voice design to replace it.")
            return

        request_path, request = ensure_casting_request(self.config, speaker, entry)
        print()
        print(f"Creating voice for {speaker} - {entry.get('display_name', speaker)}")
        print(f"Prompt: {entry.get('design_prompt', '')}")
        if not prompt_yes_no("Send this Voice Design request to Gemini?", default=False):
            return

        limiter = self.limiter(
            "voices:create",
            int(self.settings["voice_api_rpm"]),
        )
        started = time.perf_counter()
        try:
            created, latency_ms = api_call_with_retry(
                lambda: self.client.voices.create(**request),
                limiter=limiter,
                settings=self.settings,
                label=f"create voice {speaker}",
                idempotent=False,
            )
            voice_id = save_created_voice(
                self.config,
                registry,
                speaker,
                request_path,
                request,
                created,
            )
            log_usage(
                action="voice_create",
                model=request["voice"].get("model", ""),
                speaker=speaker,
                status="ok",
                latency_ms=latency_ms,
                text=request["voice"].get("prompted", {}).get("input", ""),
            )
            print(f"Created voice: {voice_id}")
            sample = provider_voice_sample_path(speaker)
            if sample.exists():
                print(f"Saved sample: {sample.relative_to(ROOT)}")
                if prompt_yes_no("Play the design sample now?", default=True):
                    play_wav(sample)
        except Exception as exc:
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            log_usage(
                action="voice_create",
                model=request["voice"].get("model", ""),
                speaker=speaker,
                status="failed",
                latency_ms=elapsed_ms,
                text=request["voice"].get("prompted", {}).get("input", ""),
                error=str(exc),
            )
            print(f"Voice creation failed: {exc}")

    def refresh_design_sample(self, speaker: str) -> None:
        registry = load_registry(self.config)
        entry = registry["characters"][speaker]
        voice_id = (entry.get("voice_id") or "").strip()
        if not voice_id:
            print("No provider voice ID is stored for this character.")
            return

        limiter = self.limiter("voices:get", int(self.settings["voice_api_rpm"]))
        try:
            details, _ = api_call_with_retry(
                lambda: self.client.voices.get(id=voice_id),
                limiter=limiter,
                settings=self.settings,
                label=f"get voice {speaker}",
                idempotent=True,
            )
            sample_audio = field_value(details, "sample_audio")
            sample_data = field_value(sample_audio, "data") if sample_audio else None
            if not sample_data:
                print("Provider returned no sample_audio.")
                return
            path = provider_voice_sample_path(speaker)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(vp.decode_audio_data(sample_data))
            print(f"Refreshed: {path.relative_to(ROOT)}")
        except Exception as exc:
            print(f"Could not refresh provider sample: {exc}")

    def play_design_sample(self, speaker: str) -> None:
        path = provider_voice_sample_path(speaker)
        if not path.exists():
            print("Local design sample is missing.")
            if prompt_yes_no("Fetch it from the Voices API?", default=True):
                self.refresh_design_sample(speaker)
        if path.exists():
            try:
                play_wav(path)
            except Exception as exc:
                print(f"Playback failed: {exc}")

    def generate_dialogue_demo(self, speaker: str) -> None:
        registry = load_registry(self.config)
        characters = registry["characters"]
        try:
            voice_id, entry = vp.resolve_voice_id(characters, speaker)
        except KeyError as exc:
            print(exc)
            return

        default_count = int(self.settings["demo_line_count"])
        selection_mode = input(
            "Demo selection: [r]epresentative, [i]d(s), [f]irst ready lines [r]: "
        ).strip().lower() or "r"
        speaker_rows = [
            row
            for row in self.manifest
            if row.get("speaker") == speaker
            and row.get("status") == "ready"
            and row.get("renpy_id")
        ]

        if selection_mode == "i":
            requested_ids = {
                value.strip()
                for value in input("Dialogue ID(s), comma-separated: ").split(",")
                if value.strip()
            }
            rows = [row for row in speaker_rows if row["id"] in requested_ids]
            missing = requested_ids - {row["id"] for row in rows}
            if missing:
                print(f"Not found for speaker {speaker}: {sorted(missing)}")
        elif selection_mode == "f":
            count = prompt_int("Number of first ready dialogue lines", default_count, 1, 20)
            rows = speaker_rows[:count]
        else:
            count = prompt_int("Number of representative dialogue lines", default_count, 1, 20)
            rows = representative_rows(self.manifest, speaker, count)

        if not rows:
            print("No matching ready dialogue rows are available for this speaker.")
            return

        print()
        print("Selected dialogue lines:")
        for index, row in enumerate(rows, start=1):
            estimate = max(1, math.ceil(len(row["tts_text"]) / 4))
            print(
                f"{index:2}. {row['id']}  (~{estimate} input tokens)\n"
                f"    {row['tts_text']}"
            )
        if not prompt_yes_no("Generate these dialogue demos?", default=True):
            return

        model = self.config["preview_model"]
        limiter = self.limiter(
            f"tts:{model}",
            int(self.settings["preview_rpm"]),
            int(self.settings["preview_tpm"]),
        )
        output_dir = DIALOGUE_PREVIEW_DIR / speaker
        output_dir.mkdir(parents=True, exist_ok=True)
        sample_rate = int(self.config.get("sample_rate", 24000))
        style = (
            entry.get("default_style")
            or self.config.get("default_style")
            or ""
        ).strip()

        total_usage = Counter()
        generated = 0
        skipped = 0
        failed = 0

        for row in rows:
            output_path = output_dir / f"{row['id']}.wav"
            if output_path.exists():
                skipped += 1
                print(f"SKIP {row['id']}: demo already exists.")
                continue

            text = row["tts_text"].strip()
            try:
                interaction, latency_ms = api_call_with_retry(
                    lambda text=text: create_tts_interaction(
                        self.client,
                        model=model,
                        voice_id=voice_id,
                        text=text,
                        style=style,
                        sample_rate=sample_rate,
                    ),
                    limiter=limiter,
                    settings=self.settings,
                    label=row["id"],
                    idempotent=True,
                    retry_permission=True,
                    estimated_tokens=max(1, math.ceil(len(text) / 4)),
                )
                output_audio = field_value(interaction, "output_audio")
                audio_data = field_value(output_audio, "data") if output_audio else None
                output_path.write_bytes(vp.decode_audio_data(audio_data))

                usage = extract_provider_usage(interaction, text)
                log_usage(
                    action="tts_preview",
                    model=model,
                    speaker=speaker,
                    row_id=row["id"],
                    status="ok",
                    latency_ms=latency_ms,
                    text=text,
                    usage=usage,
                )
                for key in (
                    "total_input_tokens",
                    "total_output_tokens",
                    "total_tokens",
                    "output_audio_tokens",
                ):
                    value = usage.get(key)
                    if isinstance(value, int):
                        total_usage[key] += value
                generated += 1
                print(f"OK   {row['id']}  [{usage_suffix(usage)}]")
            except Exception as exc:
                failed += 1
                log_usage(
                    action="tts_preview",
                    model=model,
                    speaker=speaker,
                    row_id=row["id"],
                    status="failed",
                    text=text,
                    error=str(exc),
                )
                print(f"FAIL {row['id']}: {exc}")

        print()
        print(f"Generated: {generated}; skipped: {skipped}; failed: {failed}.")
        if total_usage:
            print(
                "Provider token totals this run: "
                f"input={total_usage['total_input_tokens']}, "
                f"audio={total_usage['output_audio_tokens']}, "
                f"total={total_usage['total_tokens']}."
            )

        if generated and bool(self.settings.get("auto_play_after_generation")):
            self.play_dialogue_demos(speaker)

    def canonical_voice_token(
        self,
        characters: dict[str, dict[str, Any]],
        speaker: str,
    ) -> str:
        seen: set[str] = set()
        current = speaker
        while True:
            if current in seen:
                raise RuntimeError(f"voice_ref cycle detected at {current!r}")
            seen.add(current)
            entry = characters.get(current)
            if not entry:
                raise KeyError(current)
            ref = (entry.get("voice_ref") or "").strip()
            if not ref:
                return current
            current = ref

    def _generate_rows(
        self,
        rows: list[dict[str, Any]],
        *,
        mode: str,
        output_dir: Path,
        force: bool = False,
    ) -> tuple[int, int, int, Counter]:
        registry = load_registry(self.config)
        characters = registry["characters"]
        overrides = vp.read_json(
            vp.root_path(self.config["line_overrides_file"]),
            {"overrides": {}},
        ).get("overrides", {})
        model = (
            self.config["preview_model"]
            if mode == "preview"
            else self.config["final_model"]
        )
        rpm = int(
            self.settings["preview_rpm"]
            if mode == "preview"
            else self.settings["final_rpm"]
        )
        tpm = int(
            self.settings["preview_tpm"]
            if mode == "preview"
            else self.settings["final_tpm"]
        )
        limiter = self.limiter(f"tts:{model}", rpm, tpm)
        sample_rate = int(self.config.get("sample_rate", 24000))
        output_dir.mkdir(parents=True, exist_ok=True)

        total_usage = Counter()
        generated = 0
        skipped = 0
        failed = 0

        for position, row in enumerate(rows, start=1):
            override = overrides.get(row["id"], {})
            if override.get("skip"):
                skipped += 1
                print(f"SKIP {row['id']}: line override says skip.")
                continue

            output_path = output_dir / f"{row['id']}.wav"
            if output_path.exists() and not force:
                skipped += 1
                print(f"SKIP {row['id']}: output already exists.")
                continue

            try:
                voice_id, entry = vp.resolve_voice_id(characters, row["speaker"])
            except KeyError as exc:
                failed += 1
                print(f"FAIL {row['id']}: {exc}")
                continue

            text = (override.get("tts_text") or row["tts_text"]).strip()
            style = (
                override.get("style")
                or entry.get("default_style")
                or self.config.get("default_style")
                or ""
            ).strip()
            if not text:
                failed += 1
                print(f"FAIL {row['id']}: empty TTS text.")
                continue

            print(
                f"[{position}/{len(rows)}] {row['id']} "
                f"speaker={row['speaker']} chars={len(text)}"
            )
            try:
                interaction, latency_ms = api_call_with_retry(
                    lambda text=text, style=style, voice_id=voice_id: create_tts_interaction(
                        self.client,
                        model=model,
                        voice_id=voice_id,
                        text=text,
                        style=style,
                        sample_rate=sample_rate,
                    ),
                    limiter=limiter,
                    settings=self.settings,
                    label=row["id"],
                    idempotent=True,
                    retry_permission=True,
                    estimated_tokens=max(1, math.ceil(len(text) / 4)),
                )
                output_audio = field_value(interaction, "output_audio")
                audio_data = field_value(output_audio, "data") if output_audio else None
                output_path.write_bytes(vp.decode_audio_data(audio_data))

                usage = extract_provider_usage(interaction, text)
                log_usage(
                    action=f"tts_{mode}",
                    model=model,
                    speaker=row["speaker"],
                    row_id=row["id"],
                    status="ok",
                    latency_ms=latency_ms,
                    text=text,
                    usage=usage,
                )
                for key in (
                    "total_input_tokens",
                    "total_output_tokens",
                    "total_tokens",
                    "output_audio_tokens",
                ):
                    value = usage.get(key)
                    if isinstance(value, int):
                        total_usage[key] += value
                generated += 1
                print(f"OK   {row['id']}  [{usage_suffix(usage)}]")
            except Exception as exc:
                failed += 1
                log_usage(
                    action=f"tts_{mode}",
                    model=model,
                    speaker=row["speaker"],
                    row_id=row["id"],
                    status="failed",
                    text=text,
                    error=str(exc),
                )
                print(f"FAIL {row['id']}: {exc}")

        return generated, skipped, failed, total_usage

    def final_generation_plan(self, speaker: str) -> dict[str, Any]:
        registry = load_registry(self.config)
        characters = registry["characters"]
        canonical = self.canonical_voice_token(characters, speaker)
        canonical_entry = characters[canonical]
        related_tokens = {
            token
            for token in characters
            if self.canonical_voice_token(characters, token) == canonical
        }

        all_rows = [
            row
            for row in self.manifest
            if row.get("speaker") in related_tokens
        ]
        eligible_rows = [
            row
            for row in all_rows
            if row.get("status") == "ready" and row.get("renpy_id")
        ]
        output_dir = vp.root_path(self.config["wav_output_dir"])
        pending_rows = [
            row
            for row in eligible_rows
            if not (output_dir / f"{row['id']}.wav").exists()
        ]

        status_counts = Counter((row.get("status") or "unknown") for row in all_rows)
        review_reasons = Counter()
        for row in all_rows:
            for reason in row.get("review_reasons") or []:
                review_reasons[str(reason)] += 1

        stored_line_count = int(canonical_entry.get("line_count") or 0)
        return {
            "speaker": speaker,
            "canonical": canonical,
            "canonical_entry": canonical_entry,
            "related_tokens": related_tokens,
            "all_rows": all_rows,
            "eligible_rows": eligible_rows,
            "pending_rows": pending_rows,
            "status_counts": status_counts,
            "review_reasons": review_reasons,
            "missing_renpy_id_count": sum(not row.get("renpy_id") for row in all_rows),
            "stored_line_count": stored_line_count,
            "source_missing_hints": self.source_missing_hints(canonical),
        }

    def source_missing_hints(self, speaker: str) -> list[str]:
        registry = load_registry(self.config)
        entry = registry.get("characters", {}).get(speaker) or {}
        evidence_ids = [
            str(value).lower()
            for value in ((entry.get("profile") or {}).get("evidence_ids") or [])
            if value
        ]
        if not evidence_ids:
            return []

        coverage_path = ROOT / "original-source" / "SOURCE_COVERAGE.json"
        coverage = read_json(coverage_path, {"missing_paths": []})
        matches: list[str] = []
        for raw_path in coverage.get("missing_paths") or []:
            path = str(raw_path)
            stem = Path(path).stem.lower().replace("-", "_")
            stems = {stem}
            # Ren'Py projects commonly use a trailing "i" for the interaction/
            # intro companion of a numbered scene (for example dc009i beside
            # dc009). Character evidence usually points at the base scene ID.
            if stem.endswith("i"):
                stems.add(stem[:-1])
            if any(
                evidence == candidate
                or evidence.startswith(candidate + "_")
                or candidate in evidence
                for candidate in stems
                for evidence in evidence_ids
            ):
                matches.append(path)
        return sorted(set(matches))

    @staticmethod
    def describe_final_plan(plan: dict[str, Any]) -> str:
        total = len(plan["all_rows"])
        eligible = len(plan["eligible_rows"])
        pending = len(plan["pending_rows"])
        stored = int(plan.get("stored_line_count") or 0)
        lines = [
            f"Current canonical source rows: {total}",
            f"Final-ready rows: {eligible}",
            f"Pending WAV files: {pending}",
        ]
        if stored != total:
            lines.append(
                f"Registry line_count: {stored} (stale/historical versus current source)"
            )
        if plan.get("missing_renpy_id_count"):
            lines.append(
                f"Rows without Ren'Py ID: {plan['missing_renpy_id_count']}"
            )
        if plan.get("review_reasons"):
            top = ", ".join(
                f"{reason}={count}"
                for reason, count in plan["review_reasons"].most_common(5)
            )
            lines.append(f"Review reasons: {top}")
        if plan.get("source_missing_hints"):
            lines.append("Matching missing source files:")
            lines.extend(f"  - {path}" for path in plan["source_missing_hints"])
        return "\n".join(lines)

    def generate_final_character(self, speaker: str) -> None:
        plan = self.final_generation_plan(speaker)
        canonical = plan["canonical"]
        canonical_entry = plan["canonical_entry"]

        if canonical_entry.get("casting_status") != "approved":
            print(
                f"Canonical voice {canonical!r} is not approved. "
                "Approve the audition before final generation."
            )
            return

        print()
        print(self.describe_final_plan(plan))

        if not plan["eligible_rows"]:
            if not plan["all_rows"]:
                print(
                    "No dialogue rows for this voice identity exist in the current "
                    "canonical source manifest. No TTS request was made."
                )
            else:
                print(
                    "Dialogue rows exist, but none are final-ready. Resolve the review "
                    "reasons/Ren'Py ID mapping before final generation."
                )
            return

        if not plan["pending_rows"]:
            print("All final-ready dialogue lines already have WAV output.")
            return

        rpm = int(self.settings["final_rpm"])
        estimated_minutes = len(plan["pending_rows"]) / rpm
        print(f"Rate limit : {rpm} RPM")
        print(
            f"Best-case request time at configured RPM: "
            f"{estimated_minutes:.1f} minutes ({estimated_minutes / 60:.1f} hours)."
        )
        if not prompt_yes_no("Start resumable final generation now?", default=False):
            return

        generated, skipped, failed, totals = self._generate_rows(
            plan["eligible_rows"],
            mode="final",
            output_dir=vp.root_path(self.config["wav_output_dir"]),
            force=False,
        )
        print(
            f"Final generation complete: generated={generated}, "
            f"skipped={skipped}, failed={failed}."
        )
        if totals:
            print(
                f"Provider tokens: input={totals['total_input_tokens']}, "
                f"audio={totals['output_audio_tokens']}, "
                f"total={totals['total_tokens']}."
            )

    def generate_all_approved_final(self) -> None:
        registry = load_registry(self.config)
        characters = registry["characters"]
        approved = {
            token
            for token, entry in characters.items()
            if entry.get("casting_status") == "approved"
            and (entry.get("voice_id") or "").strip()
        }
        if not approved:
            print("No approved provider voices are available.")
            return

        eligible = []
        for row in self.manifest:
            speaker = row.get("speaker")
            if not speaker or row.get("status") != "ready" or not row.get("renpy_id"):
                continue
            try:
                canonical = self.canonical_voice_token(characters, speaker)
            except (KeyError, RuntimeError):
                continue
            if canonical in approved:
                eligible.append(row)

        output_dir = vp.root_path(self.config["wav_output_dir"])
        pending = [
            row
            for row in eligible
            if not (output_dir / f"{row['id']}.wav").exists()
        ]
        if not pending:
            print("All currently approved ready lines already have final WAV output.")
            return

        rpm = int(self.settings["final_rpm"])
        estimated_minutes = len(pending) / rpm
        print()
        print(f"Approved voice identities : {len(approved)}")
        print(f"Eligible ready rows       : {len(eligible)}")
        print(f"Pending WAV files         : {len(pending)}")
        print(f"Configured final rate     : {rpm} RPM")
        print(
            f"Best-case request time    : "
            f"{estimated_minutes:.1f} minutes ({estimated_minutes / 60:.1f} hours)"
        )
        confirmation = input("Type GENERATE to start this resumable batch: ").strip()
        if confirmation != "GENERATE":
            print("Cancelled.")
            return

        generated, skipped, failed, totals = self._generate_rows(
            eligible,
            mode="final",
            output_dir=output_dir,
            force=False,
        )
        print(
            f"Batch complete: generated={generated}, skipped={skipped}, failed={failed}."
        )
        if totals:
            print(
                f"Provider tokens: input={totals['total_input_tokens']}, "
                f"audio={totals['output_audio_tokens']}, "
                f"total={totals['total_tokens']}."
            )

    def encode_generated_audio(self) -> None:
        command = [sys.executable, str(ROOT / "tools" / "voice_pipeline.py"), "encode"]
        print("+ " + " ".join(command))
        try:
            subprocess.run(command, cwd=ROOT, check=True)
        except subprocess.CalledProcessError as exc:
            print(f"Encoding failed: {exc}")

    def _dialogue_demo_files(self, speaker: str) -> list[tuple[Path, dict[str, Any] | None]]:
        by_id = {
            row["id"]: row
            for row in self.manifest
            if row.get("speaker") == speaker
        }
        found: dict[str, Path] = {}

        studio_dir = DIALOGUE_PREVIEW_DIR / speaker
        if studio_dir.exists():
            for path in studio_dir.glob("*.wav"):
                found[path.stem] = path

        generated_dir = vp.root_path(self.config["wav_output_dir"])
        if generated_dir.exists():
            for row_id in by_id:
                path = generated_dir / f"{row_id}.wav"
                if path.exists() and row_id not in found:
                    found[row_id] = path

        return [
            (path, by_id.get(row_id))
            for row_id, path in sorted(found.items())
        ]

    def play_dialogue_demos(self, speaker: str) -> None:
        files = self._dialogue_demo_files(speaker)
        if not files:
            print("No dialogue demo WAV files found for this speaker.")
            return

        shown = files[:40]
        print()
        for index, (path, row) in enumerate(shown, start=1):
            text = (row or {}).get("tts_text", "")
            print(f"{index:2}. {path.name}")
            if text:
                print(f"    {text}")

        choice = input("Play number, a = all shown, q = cancel: ").strip().lower()
        if choice == "q":
            return
        try:
            if choice == "a":
                selected = shown
            else:
                index = int(choice)
                if not 1 <= index <= len(shown):
                    raise ValueError
                selected = [shown[index - 1]]
        except ValueError:
            print("Invalid selection.")
            return

        for path, _ in selected:
            try:
                play_wav(path)
            except KeyboardInterrupt:
                break
            except Exception as exc:
                print(f"Playback failed for {path.name}: {exc}")

    def approve_voice(self, speaker: str) -> None:
        registry = load_registry(self.config)
        entry = registry["characters"][speaker]
        voice_id = (entry.get("voice_id") or "").strip()
        if not voice_id:
            print("No provider voice exists to approve.")
            return

        sample = provider_voice_sample_path(speaker)
        if sample.exists() and prompt_yes_no("Play design sample before approval?", default=True):
            play_wav(sample)

        demos = self._dialogue_demo_files(speaker)
        if demos and prompt_yes_no("Play dialogue demos before approval?", default=True):
            self.play_dialogue_demos(speaker)

        if not prompt_yes_no(
            f"Approve {entry.get('display_name', speaker)} with {voice_id}?",
            default=False,
        ):
            return

        approvals = read_json(
            APPROVALS_PATH,
            {"schema_version": 1, "approvals": {}, "history": []},
        )
        approval = {
            "speaker": speaker,
            "display_name": entry.get("display_name", speaker),
            "voice_id": voice_id,
            "approved_at": utc_now(),
            "design_prompt_sha256": hashlib.sha256(
                (entry.get("design_prompt") or "").encode("utf-8")
            ).hexdigest(),
            "sample_sha256": file_sha256(sample) if sample.exists() else "",
        }
        approvals.setdefault("approvals", {})[speaker] = approval
        write_json_atomic(APPROVALS_PATH, approvals)

        entry["casting_status"] = "approved"
        save_registry(self.config, registry)
        print("Voice approved and recorded in voice/approvals.json.")

    def revoke_approval(self, speaker: str, reason: str) -> None:
        approvals = read_json(
            APPROVALS_PATH,
            {"schema_version": 1, "approvals": {}, "history": []},
        )
        current = approvals.setdefault("approvals", {}).pop(speaker, None)
        if current:
            current = dict(current)
            current["revoked_at"] = utc_now()
            current["revoke_reason"] = reason
            approvals.setdefault("history", []).append(current)
            write_json_atomic(APPROVALS_PATH, approvals)

    def edit_prompt(self, speaker: str) -> None:
        registry = load_registry(self.config)
        entry = registry["characters"][speaker]
        print(f"Current prompt:\n{entry.get('design_prompt') or '-'}")
        new_prompt = input("New Voice Design prompt (blank = cancel): ").strip()
        if not new_prompt:
            return
        entry["design_prompt"] = new_prompt
        if entry.get("voice_id"):
            print("Note: the existing provider voice is unchanged until you retry Voice Design.")
        save_registry(self.config, registry)
        regenerate_casting_pack()
        print("Prompt updated and casting request regenerated.")

    def retry_voice(self, speaker: str) -> None:
        registry = load_registry(self.config)
        entry = registry["characters"][speaker]
        old_voice_id = (entry.get("voice_id") or "").strip()
        if not old_voice_id:
            print("No current provider voice. Use Create voice instead.")
            return

        if entry.get("casting_status") == "approved":
            print("This voice is currently APPROVED.")
            if not prompt_yes_no("Revoke approval and retry anyway?", default=False):
                return

        reason = input("Reason for retry/rejection (optional): ").strip()
        if prompt_yes_no("Edit the Voice Design prompt before retry?", default=False):
            self.edit_prompt(speaker)
            registry = load_registry(self.config)
            entry = registry["characters"][speaker]

        print(
            "Retry will delete the current stored Gemini voice, archive local samples, "
            "clear the local voice ID, and create a new candidate."
        )
        if not prompt_yes_no(
            f"Delete provider voice {old_voice_id} and continue?",
            default=False,
        ):
            return

        limiter = self.limiter("voices:delete", int(self.settings["voice_api_rpm"]))
        try:
            api_call_with_retry(
                lambda: self.client.voices.delete(id=old_voice_id),
                limiter=limiter,
                settings=self.settings,
                label=f"delete voice {speaker}",
                idempotent=True,
            )
        except Exception as exc:
            print(f"Provider delete failed. Local state was not changed: {exc}")
            return

        archive = archive_local_candidate(speaker, old_voice_id, reason)
        self.revoke_approval(speaker, reason or "voice design retry")

        registry = load_registry(self.config)
        entry = registry["characters"][speaker]
        entry["voice_id"] = ""
        entry["casting_status"] = "proposed"
        save_registry(self.config, registry)
        print(f"Archived rejected local candidate under {archive.relative_to(ROOT)}.")

        if prompt_yes_no("Create the replacement voice now?", default=True):
            self.create_voice(speaker)

    def show_usage(self) -> None:
        if not USAGE_LEDGER_PATH.exists():
            print("No local usage ledger exists yet.")
            return

        records = []
        with USAGE_LEDGER_PATH.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

        if not records:
            print("Usage ledger is empty.")
            return

        status_counts = Counter(record.get("status", "?") for record in records)
        action_counts = Counter(record.get("action", "?") for record in records)
        model_counts = Counter(record.get("model", "?") for record in records)
        totals = Counter()
        estimated = 0
        for record in records:
            for key in (
                "total_input_tokens",
                "total_output_tokens",
                "total_tokens",
                "output_audio_tokens",
            ):
                value = record.get(key)
                if isinstance(value, int):
                    totals[key] += value
            if record.get("usage_source") == "estimated":
                estimated += int(record.get("estimated_input_tokens") or 0)

        print()
        print("Local API usage ledger")
        print("=" * 78)
        print(f"Requests logged : {len(records)}")
        print(f"Status          : {dict(status_counts)}")
        print(f"Actions         : {dict(action_counts)}")
        print(f"Models          : {dict(model_counts)}")
        print(f"Exact input     : {totals['total_input_tokens']} tokens")
        print(f"Exact audio out : {totals['output_audio_tokens']} tokens")
        print(f"Exact total     : {totals['total_tokens']} tokens")
        if estimated:
            print(f"Estimated input : {estimated} tokens where provider usage was unavailable")
        print(f"Ledger          : {USAGE_LEDGER_PATH.relative_to(ROOT)}")

    def configure_runtime(self) -> None:
        print()
        print("Client-side runtime settings")
        print("Google's active project limits remain authoritative; check AI Studio for them.")
        self.settings["preview_rpm"] = prompt_int(
            "Preview TTS RPM",
            int(self.settings["preview_rpm"]),
            1,
            1000,
        )
        self.settings["preview_tpm"] = prompt_int(
            "Preview input TPM (0 = do not enforce)",
            int(self.settings["preview_tpm"]),
            0,
            1000000000,
        )
        self.settings["final_rpm"] = prompt_int(
            "Final TTS RPM",
            int(self.settings["final_rpm"]),
            1,
            1000,
        )
        self.settings["final_tpm"] = prompt_int(
            "Final input TPM (0 = do not enforce)",
            int(self.settings["final_tpm"]),
            0,
            1000000000,
        )
        self.settings["voice_api_rpm"] = prompt_int(
            "Voices API RPM",
            int(self.settings["voice_api_rpm"]),
            1,
            1000,
        )
        self.settings["max_retries"] = prompt_int(
            "Maximum retries for idempotent TTS/read calls",
            int(self.settings["max_retries"]),
            0,
            20,
        )
        self.settings["retry_base_delay_seconds"] = prompt_float(
            "Base retry delay seconds",
            float(self.settings["retry_base_delay_seconds"]),
            0.0,
            600.0,
        )
        self.settings["permission_retry_delay_seconds"] = prompt_float(
            "403 permission retry delay seconds",
            float(self.settings["permission_retry_delay_seconds"]),
            0.0,
            600.0,
        )
        self.settings["rate_safety_margin_seconds"] = prompt_float(
            "RPM safety margin seconds",
            float(self.settings["rate_safety_margin_seconds"]),
            0.0,
            30.0,
        )
        self.settings["demo_line_count"] = prompt_int(
            "Default dialogue demo line count",
            int(self.settings["demo_line_count"]),
            1,
            20,
        )
        save_runtime_settings(self.settings)
        print(f"Saved local settings to {RUNTIME_SETTINGS_PATH.relative_to(ROOT)}.")

    def list_provider_voices(self) -> None:
        limiter = self.limiter("voices:list", int(self.settings["voice_api_rpm"]))
        try:
            response, _ = api_call_with_retry(
                lambda: self.client.voices.list(type_=["prompted"]),
                limiter=limiter,
                settings=self.settings,
                label="list voices",
                idempotent=True,
            )
        except Exception as exc:
            print(f"Could not list provider voices: {exc}")
            return

        voices = field_value(response, "voices", []) or []
        registry = load_registry(self.config)
        local_ids = {
            (entry.get("voice_id") or ""): token
            for token, entry in registry.get("characters", {}).items()
            if entry.get("voice_id")
        }
        print()
        print(f"Stored prompted voices in project: {len(voices)}")
        for voice in voices:
            voice_id = field_value(voice, "id", "")
            display_name = field_value(voice, "display_name", "")
            local = local_ids.get(voice_id, "")
            suffix = f"  local={local}" if local else "  [ORPHAN/UNTRACKED]"
            print(f"{voice_id:<28} {display_name:<34}{suffix}")

    def character_menu(self, speaker: str) -> None:
        while True:
            registry = load_registry(self.config)
            entry = registry["characters"][speaker]
            clear_screen()
            print(
                f"VOICE STUDIO | {speaker} - {entry.get('display_name', speaker)} | "
                f"{character_status(entry)} | {entry.get('line_count', 0)} lines"
            )
            print("-" * 90)
            print("1. Show character / voice profile")
            print("2. Create character voice")
            print("3. Listen Voice Design sample")
            print("4. Generate representative dialogue demo")
            print("5. Listen dialogue demos")
            print("6. Approve voice")
            print("7. Retry / reject Voice Design")
            print("8. Edit Voice Design prompt")
            print("9. Refresh design sample from provider")
            print("10. Generate final audio for this approved voice")
            print("0. Back")
            choice = input("\nChoose: ").strip().lower()

            if choice == "0":
                return
            if choice == "1":
                self.show_character_details(speaker)
            elif choice == "2":
                self.create_voice(speaker)
            elif choice == "3":
                self.play_design_sample(speaker)
            elif choice == "4":
                self.generate_dialogue_demo(speaker)
            elif choice == "5":
                self.play_dialogue_demos(speaker)
            elif choice == "6":
                self.approve_voice(speaker)
            elif choice == "7":
                self.retry_voice(speaker)
            elif choice == "8":
                self.edit_prompt(speaker)
            elif choice == "9":
                self.refresh_design_sample(speaker)
            elif choice == "10":
                self.generate_final_character(speaker)
            else:
                continue
            input("\nPress Enter to continue...")

    def next_attention_character(self) -> str | None:
        registry = load_registry(self.config)
        candidates = []
        for token, entry in registry.get("characters", {}).items():
            if not entry.get("enabled", True) or entry.get("voice_ref"):
                continue
            status = character_status(entry)
            priority = 0 if status == "AUDITION" else 1 if status == "NEEDS VOICE" else 2
            if priority < 2:
                candidates.append(
                    (priority, -int(entry.get("line_count") or 0), token)
                )
        if not candidates:
            return None
        candidates.sort()
        return candidates[0][2]

    def main_menu(self) -> None:
        while True:
            clear_screen()
            registry = load_registry(self.config)
            statuses = Counter(
                character_status(entry)
                for entry in registry.get("characters", {}).values()
            )
            print("GEMINI GAME VOICE STUDIO")
            print("=" * 90)
            print(
                "Characters: "
                f"approved={statuses['APPROVED']}  "
                f"audition={statuses['AUDITION']}  "
                f"needs_voice={statuses['NEEDS VOICE']}  "
                f"disabled={statuses['DISABLED']}"
            )
            print(
                "Rate limits: "
                f"preview={self.settings['preview_rpm']} RPM/"
                f"{self.settings['preview_tpm'] or 'unlimited'} TPM  "
                f"final={self.settings['final_rpm']} RPM/"
                f"{self.settings['final_tpm'] or 'unlimited'} TPM  "
                f"voices={self.settings['voice_api_rpm']} RPM"
            )
            print("-" * 90)
            print("1. Choose character")
            print("2. Open next character needing attention")
            print("3. Usage / token dashboard")
            print("4. Client-side rate / retry settings")
            print("5. Refresh character validation + casting requests")
            print("6. List stored Gemini custom voices")
            print("7. Generate final WAVs for all approved voices")
            print("8. Encode generated WAVs to Ogg/Opus")
            print("q. Quit")
            choice = input("\nChoose: ").strip().lower()

            if choice == "q":
                return
            if choice == "1":
                speaker = self.choose_character()
                if speaker:
                    self.character_menu(speaker)
            elif choice == "2":
                speaker = self.next_attention_character()
                if speaker:
                    self.character_menu(speaker)
                else:
                    print("No pending characters.")
                    input("\nPress Enter to continue...")
            elif choice == "3":
                self.show_usage()
                input("\nPress Enter to continue...")
            elif choice == "4":
                self.configure_runtime()
                input("\nPress Enter to continue...")
            elif choice == "5":
                try:
                    regenerate_casting_pack()
                    self._manifest = None
                    print("Casting pack refreshed.")
                except subprocess.CalledProcessError as exc:
                    print(f"Casting pack refresh failed: {exc}")
                input("\nPress Enter to continue...")
            elif choice == "6":
                self.list_provider_voices()
                input("\nPress Enter to continue...")
            elif choice == "7":
                self.generate_all_approved_final()
                input("\nPress Enter to continue...")
            elif choice == "8":
                self.encode_generated_audio()
                input("\nPress Enter to continue...")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Interactive casting, audition, approval, and safe TTS studio."
    )
    parser.add_argument(
        "--speaker",
        help="Open one speaker token directly instead of starting at the main menu.",
    )
    parser.add_argument(
        "--usage",
        action="store_true",
        help="Print the local token/usage dashboard and exit.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config = vp.load_config()
    settings = load_runtime_settings()
    studio = VoiceStudio(config, settings)

    try:
        if args.usage:
            studio.show_usage()
            return 0
        if args.speaker:
            registry = load_registry(config)
            if args.speaker not in registry.get("characters", {}):
                raise SystemExit(f"Unknown speaker {args.speaker!r}.")
            studio.character_menu(args.speaker)
            return 0
        studio.main_menu()
        return 0
    except KeyboardInterrupt:
        print("\nCancelled.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
