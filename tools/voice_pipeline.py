#!/usr/bin/env python3
"""Build English Ren'Py voice assets from canonical original game source.

English dialogue text and speaker syntax come only from original-source/game.
Translation exports are used only as ID metadata so generated audio filenames match
Ren'Py's config.auto_voice dialogue identifiers.
"""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "voice" / "config.json"
VALIDATOR_PATH = ROOT / "tools" / "dutch_translation_validate.py"

SPEC = importlib.util.spec_from_file_location("voice_id_validator", VALIDATOR_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)

VARIABLE_RE = re.compile(r"\[([A-Za-z_][\w.]*)\]")
PERCENT_VAR_RE = re.compile(r"%\([^)]+\)[#0 +\-]?(?:\d+|\*)?(?:\.\d+)?[diouxXeEfFgGcrs]")
WAIT_TAG_RE = re.compile(r"\{(?:w(?:=[^}]*)?|p)\}", re.IGNORECASE)
BRACE_TAG_RE = re.compile(r"\{[^{}]*\}")
CHARACTER_DEFINE_RE = re.compile(
    r"^\s*define\s+([A-Za-z_][\w]*)\s*=\s*Character\s*\(",
    re.MULTILINE,
)
TOKEN_DIALOGUE_SHAPE_RE = re.compile(r'^([A-Za-z_][\w.]*)\s+""(?:\s+.*)?$')
LITERAL_SPEAKER_SHAPE_RE = re.compile(r'^""\s+""(?:\s+.*)?$')
NARRATOR_SHAPE_RE = re.compile(r'^""(?:\s+.*)?$')


def read_json(path: Path, default: dict | None = None) -> dict:
    if not path.exists():
        return {} if default is None else default
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def load_config() -> dict:
    return read_json(CONFIG_PATH)


def root_path(value: str) -> Path:
    return ROOT / value


def load_variables(config: dict) -> dict[str, str]:
    path = root_path(config["variables_file"])
    data = read_json(path, {})
    return {str(key): str(value) for key, value in data.items()}


def original_source_root(config: dict) -> Path:
    return root_path(config.get("original_source_root", "original-source/game"))


def id_manifest_path(config: dict) -> Path:
    value = config.get("id_manifest") or config.get("source_manifest")
    if not value:
        raise RuntimeError("voice/config.json must define id_manifest")
    return root_path(value)


def id_language_priority(config: dict) -> list[str]:
    return list(
        config.get("id_reference_language_priority")
        or config.get("reference_language_priority")
        or []
    )


def load_character_tokens(config: dict) -> set[str]:
    source_root = original_source_root(config)
    if not source_root.exists():
        raise RuntimeError(
            f"canonical original source is missing: {source_root.relative_to(ROOT)}"
        )

    tokens = {"narrator", "extend"}
    for path in sorted(source_root.rglob("*.rpy")):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            continue
        tokens.update(CHARACTER_DEFINE_RE.findall(text))
    return tokens


def prepare_tts_text(text: str, variables: dict[str, str]) -> tuple[str, list[str]]:
    unresolved: list[str] = []

    def replace_variable(match: re.Match[str]) -> str:
        name = match.group(1)
        if name in variables:
            return variables[name]
        unresolved.append(name)
        return match.group(0)

    value = VARIABLE_RE.sub(replace_variable, text)
    if PERCENT_VAR_RE.search(value):
        unresolved.append("percent-format-variable")

    value = WAIT_TAG_RE.sub(" <short pause> ", value)
    value = BRACE_TAG_RE.sub("", value)
    value = value.replace("\n", " ")
    value = re.sub(r"\s+", " ", value).strip()
    return value, sorted(set(unresolved))


def dialogue_from_statement(
    literals: tuple[str, ...] | list[str],
    shape: str,
    character_tokens: set[str],
) -> dict | None:
    values = tuple(literals)

    if NARRATOR_SHAPE_RE.fullmatch(shape) and not LITERAL_SPEAKER_SHAPE_RE.fullmatch(shape):
        if len(values) != 1:
            return None
        return {
            "speaker": "narrator",
            "speaker_label": "",
            "speaker_kind": "narrator",
            "english_text": values[0],
        }

    if LITERAL_SPEAKER_SHAPE_RE.fullmatch(shape):
        if len(values) != 2:
            return None
        return {
            "speaker": "",
            "speaker_label": values[0],
            "speaker_kind": "literal",
            "english_text": values[1],
        }

    match = TOKEN_DIALOGUE_SHAPE_RE.fullmatch(shape)
    if not match:
        return None

    speaker = match.group(1).split(".", 1)[0]
    if speaker not in character_tokens:
        return None
    if len(values) != 1:
        return None
    return {
        "speaker": speaker,
        "speaker_label": "",
        "speaker_kind": "token",
        "english_text": values[0],
    }


def parse_original_dialogue_file(path: Path, character_tokens: set[str]) -> list[dict]:
    units: list[dict] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        stripped = line.strip()
        if '"' not in stripped:
            continue
        try:
            parsed = VALIDATOR.extract_statement(stripped)
        except ValueError:
            continue
        if parsed is None:
            continue

        literals, shape = parsed
        dialogue = dialogue_from_statement(literals, shape, character_tokens)
        if dialogue is None:
            continue
        units.append(
            {
                **dialogue,
                "source_line": line_no,
                "source_shape": shape,
                "source_literals": tuple(literals),
                "statement": stripped,
            }
        )
    return units


def source_signature(block) -> tuple:
    return tuple((unit.source_shape, unit.source) for unit in block.units)


def analyze_id_file(path: Path) -> dict:
    blocks, problems = VALIDATOR.parse_translation_file(path, strict_missing_targets=False)
    unique_blocks: dict[str, object] = {}
    identical_duplicates: list[str] = []
    conflicts: list[str] = []

    for block in blocks:
        if block.block_id == "strings":
            continue
        existing = unique_blocks.get(block.block_id)
        if existing is None:
            unique_blocks[block.block_id] = block
            continue
        if source_signature(existing) == source_signature(block):
            identical_duplicates.append(block.block_id)
        else:
            conflicts.append(block.block_id)

    return {
        "path": path,
        "blocks": list(unique_blocks.values()),
        "problems": problems,
        "identical_duplicates": sorted(set(identical_duplicates)),
        "conflicts": sorted(set(conflicts)),
        "unique_block_count": len(unique_blocks),
        "unit_count": sum(len(block.units) for block in unique_blocks.values()),
    }


def candidate_id_languages(manifest_row: dict, config: dict) -> list[str]:
    declared = [
        value.strip()
        for value in (manifest_row.get("present_in_languages") or "").split(";")
        if value.strip()
    ]
    reference = (manifest_row.get("count_reference_language") or "").strip()
    if reference and reference not in declared:
        declared.append(reference)

    priority = id_language_priority(config)
    rank = {language: index for index, language in enumerate(priority)}
    return sorted(set(declared), key=lambda language: (rank.get(language, 999), language))


def select_id_metadata_file(
    relative_path: str,
    manifest_row: dict,
    config: dict,
) -> tuple[dict | None, list[str]]:
    warnings: list[str] = []
    candidates: list[tuple[str, dict]] = []

    for language in candidate_id_languages(manifest_row, config):
        path = ROOT / language / relative_path
        if not path.exists():
            continue
        candidates.append((language, analyze_id_file(path)))

    if not candidates:
        return None, [f"missing all translation ID metadata candidates for: {relative_path}"]

    priority = id_language_priority(config)
    rank = {language: index for index, language in enumerate(priority)}

    def score(item: tuple[str, dict]) -> tuple:
        language, analysis = item
        return (
            1 if not analysis["conflicts"] else 0,
            1 if not analysis["problems"] else 0,
            analysis["unique_block_count"],
            analysis["unit_count"],
            -rank.get(language, 999),
        )

    language, best = max(candidates, key=score)
    if best["conflicts"]:
        details = ", ".join(best["conflicts"][:10])
        raise RuntimeError(
            f"no conflict-free ID metadata file for {relative_path}; "
            f"best candidate {language!r} has conflicting translation IDs: {details}"
        )

    preferred = (manifest_row.get("count_reference_language") or "").strip()
    if preferred and language != preferred:
        warnings.append(
            f"ID resolver selected {language}/{relative_path} instead of "
            f"manifest count reference {preferred}/{relative_path}"
        )
    if best["identical_duplicates"]:
        warnings.append(
            f"deduplicated {len(best['identical_duplicates'])} identical translation ID(s) "
            f"in {language}/{relative_path}"
        )
    for problem in best["problems"]:
        warnings.append(problem.render())

    best["language"] = language
    return best, warnings


def block_dialogue_units(block, character_tokens: set[str]) -> list[object]:
    result = []
    for unit in block.units:
        if dialogue_from_statement(unit.source, unit.source_shape, character_tokens) is not None:
            result.append(unit)
    return result


def match_ids_to_original(
    blocks: list[object],
    direct_units: list[dict],
    character_tokens: set[str],
    relative_path: str,
) -> tuple[list[tuple[object, object, dict]], set[int], list[str]]:
    matches: list[tuple[object, object, dict]] = []
    used: set[int] = set()
    warnings: list[str] = []
    cursor = 0

    for block in blocks:
        dialogue_units = block_dialogue_units(block, character_tokens)
        if not dialogue_units:
            continue
        if len(dialogue_units) > 1:
            warnings.append(
                f"{relative_path}: ID block {block.block_id} contains "
                f"{len(dialogue_units)} dialogue units; skipped as ambiguous"
            )
            continue

        metadata_unit = dialogue_units[0]
        key = (metadata_unit.source_shape, tuple(metadata_unit.source))

        found = None
        for index in range(cursor, len(direct_units)):
            direct = direct_units[index]
            if index not in used and (
                direct["source_shape"],
                tuple(direct["source_literals"]),
            ) == key:
                found = index
                break

        if found is None:
            candidates = [
                index
                for index, direct in enumerate(direct_units)
                if index not in used
                and (
                    direct["source_shape"],
                    tuple(direct["source_literals"]),
                ) == key
            ]
            if len(candidates) == 1:
                found = candidates[0]
                warnings.append(
                    f"{relative_path}: ID {block.block_id} matched original source "
                    "outside expected statement order"
                )

        if found is None:
            warnings.append(
                f"{relative_path}: ID {block.block_id} source comment does not match "
                "the canonical original source"
            )
            continue

        used.add(found)
        if found >= cursor:
            cursor = found + 1
        matches.append((block, metadata_unit, direct_units[found]))

    return matches, used, warnings


def make_unmapped_id(relative_path: str, unit: dict) -> str:
    payload = json.dumps(
        [
            relative_path,
            unit["source_line"],
            unit["source_shape"],
            list(unit["source_literals"]),
        ],
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return "unmapped_" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def build_row(
    *,
    row_id: str,
    renpy_id: str,
    relative_path: str,
    direct_path: Path,
    direct: dict,
    variables: dict[str, str],
    skip_speakers: set[str],
    reference_language: str = "",
    reference_file: str = "",
    id_source_line: int = 0,
    extra_reasons: list[str] | None = None,
) -> dict:
    tts_text, unresolved = prepare_tts_text(direct["english_text"], variables)
    reasons = list(extra_reasons or [])

    if direct["speaker_kind"] == "literal":
        reasons.append("literal-speaker:" + direct["speaker_label"])
    if direct["speaker"] in skip_speakers:
        reasons.append("speaker-skipped-by-config")
    if unresolved:
        reasons.append("unresolved-variable:" + ",".join(unresolved))

    source_file = direct_path.relative_to(ROOT).as_posix()
    return {
        "id": row_id,
        "renpy_id": renpy_id,
        "unit_index": 1,
        "speaker": direct["speaker"],
        "speaker_label": direct["speaker_label"],
        "speaker_kind": direct["speaker_kind"],
        "english_text": direct["english_text"],
        "tts_text": tts_text,
        "status": "ready" if not reasons else "needs_review",
        "review_reasons": reasons,
        "reference_language": reference_language,
        "reference_file": reference_file,
        "id_source_line": id_source_line,
        "game_source_file": relative_path,
        "source_file": source_file,
        "source_line": direct["source_line"],
        "source_shape": direct["source_shape"],
        "source_literals": list(direct["source_literals"]),
        "source_occurrences": [
            {
                "source_file": source_file,
                "source_line": direct["source_line"],
            }
        ],
    }


def iter_source_rows(config: dict) -> tuple[list[dict], list[str]]:
    manifest_path = id_manifest_path(config)
    source_root = original_source_root(config)
    variables = load_variables(config)
    skip_speakers = set(config.get("skip_speakers", []))
    character_tokens = load_character_tokens(config)
    rows_by_id: dict[str, dict] = {}
    warnings: list[str] = []
    conflicts: list[str] = []
    processed_paths: set[str] = set()

    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        id_manifest = list(csv.DictReader(handle))

    def add_row(row: dict) -> None:
        existing = rows_by_id.get(row["id"])
        if existing is None:
            rows_by_id[row["id"]] = row
            return

        same_voice_line = (
            existing["speaker"] == row["speaker"]
            and existing.get("speaker_label", "") == row.get("speaker_label", "")
            and existing["english_text"] == row["english_text"]
            and existing["tts_text"] == row["tts_text"]
        )
        if same_voice_line:
            existing["source_occurrences"].extend(row["source_occurrences"])
            warnings.append(
                f"deduplicated identical global voice ID {row['id']} from "
                f"{row['game_source_file']}"
            )
            return

        conflicts.append(
            f"{row['id']}: {existing['speaker']} {existing['english_text']!r} "
            f"vs {row['speaker']} {row['english_text']!r}"
        )

    for manifest_row in id_manifest:
        relative_path = (manifest_row.get("relative_path") or "").strip()
        if not relative_path:
            continue

        direct_path = source_root / relative_path
        if not direct_path.exists():
            warnings.append(
                f"not present in installed canonical original source: {relative_path}"
            )
            continue

        processed_paths.add(relative_path)
        direct_units = parse_original_dialogue_file(direct_path, character_tokens)
        selected, selection_warnings = select_id_metadata_file(
            relative_path, manifest_row, config
        )
        warnings.extend(selection_warnings)

        used: set[int] = set()
        if selected is not None:
            matches, used, mapping_warnings = match_ids_to_original(
                selected["blocks"], direct_units, character_tokens, relative_path
            )
            warnings.extend(mapping_warnings)

            reference_file = selected["path"].relative_to(ROOT).as_posix()
            reference_language = selected["language"]
            for block, metadata_unit, direct in matches:
                add_row(
                    build_row(
                        row_id=block.block_id,
                        renpy_id=block.block_id,
                        relative_path=relative_path,
                        direct_path=direct_path,
                        direct=direct,
                        variables=variables,
                        skip_speakers=skip_speakers,
                        reference_language=reference_language,
                        reference_file=reference_file,
                        id_source_line=metadata_unit.source_line,
                    )
                )

        for index, direct in enumerate(direct_units):
            if index in used:
                continue
            row_id = make_unmapped_id(relative_path, direct)
            add_row(
                build_row(
                    row_id=row_id,
                    renpy_id="",
                    relative_path=relative_path,
                    direct_path=direct_path,
                    direct=direct,
                    variables=variables,
                    skip_speakers=skip_speakers,
                    extra_reasons=["renpy-id-not-resolved"],
                )
            )

    for direct_path in sorted(source_root.rglob("*.rpy")):
        relative_path = direct_path.relative_to(source_root).as_posix()
        if relative_path in processed_paths:
            continue
        for direct in parse_original_dialogue_file(direct_path, character_tokens):
            row_id = make_unmapped_id(relative_path, direct)
            add_row(
                build_row(
                    row_id=row_id,
                    renpy_id="",
                    relative_path=relative_path,
                    direct_path=direct_path,
                    direct=direct,
                    variables=variables,
                    skip_speakers=skip_speakers,
                    extra_reasons=["renpy-id-not-resolved"],
                )
            )

    if conflicts:
        raise RuntimeError(
            "conflicting Ren'Py voice IDs cannot share one config.auto_voice filename: "
            + " | ".join(conflicts[:20])
        )

    return list(rows_by_id.values()), warnings


def write_manifest(config: dict, rows: list[dict], warnings: list[str]) -> None:
    manifest_path = root_path(config["manifest_output"])
    stats_path = root_path(config["speaker_stats_output"])
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    with manifest_path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    speaker_counts = Counter(row["speaker"] for row in rows if row["speaker"])
    id_language_counts = Counter(
        row["reference_language"] for row in rows if row.get("reference_language")
    )
    ready_count = sum(row["status"] == "ready" for row in rows)
    stats = {
        "source_kind": "canonical_original_english_game_source",
        "canonical_source_root": original_source_root(config).relative_to(ROOT).as_posix(),
        "id_metadata_manifest": id_manifest_path(config).relative_to(ROOT).as_posix(),
        "total_lines": len(rows),
        "ready_lines": ready_count,
        "needs_review_lines": len(rows) - ready_count,
        "unmapped_id_lines": sum(not row.get("renpy_id") for row in rows),
        "literal_speaker_lines": sum(row.get("speaker_kind") == "literal" for row in rows),
        "speaker_count": len(speaker_counts),
        "speakers": dict(sorted(speaker_counts.items(), key=lambda item: (-item[1], item[0]))),
        "id_metadata_languages": dict(sorted(id_language_counts.items())),
        "warnings": warnings,
    }
    write_json(stats_path, stats)


def load_manifest(config: dict, refresh_if_missing: bool = True) -> list[dict]:
    path = root_path(config["manifest_output"])
    if not path.exists() and refresh_if_missing:
        rows, warnings = iter_source_rows(config)
        write_manifest(config, rows, warnings)
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def merge_character_registry(config: dict, write: bool = True) -> dict:
    path = root_path(config["characters_file"])
    registry = read_json(path, {"schema_version": 1, "characters": {}})
    characters = registry.setdefault("characters", {})
    counts = Counter(row["speaker"] for row in load_manifest(config) if row["speaker"])

    # line_count describes the current canonical source manifest, not historical
    # research coverage. Reset existing entries first so speakers that disappeared
    # from the imported source do not retain stale non-zero counts.
    for speaker, entry in characters.items():
        entry["line_count"] = counts.get(speaker, 0)

    for speaker, count in sorted(counts.items()):
        if speaker in characters:
            continue
        characters[speaker] = {
            "display_name": speaker,
            "voice_id": "",
            "voice_ref": "",
            "language_code": config.get("spoken_language", "en-US"),
            "design_prompt": "",
            "default_style": config.get("default_style", ""),
            "enabled": True,
            "line_count": count,
        }

    if write:
        write_json(path, registry)
    return registry


def require_genai():
    try:
        from google import genai
    except ImportError as exc:
        raise SystemExit(
            "google-genai is not installed. Run: python -m pip install -r requirements-voice.txt"
        ) from exc
    return genai


def gemini_api_key() -> str:
    key = (os.environ.get("GEMINI_API_KEY") or "").strip()
    if not key:
        raise SystemExit("GEMINI_API_KEY is not set.")
    return key


def create_genai_client():
    genai = require_genai()
    key = gemini_api_key()
    if os.environ.get("GOOGLE_API_KEY"):
        print(
            "NOTE: GOOGLE_API_KEY is also set; this pipeline explicitly uses GEMINI_API_KEY.",
            file=sys.stderr,
        )
    return genai.Client(api_key=key)


def decode_audio_data(data) -> bytes:
    if data is None:
        raise RuntimeError("Gemini returned no audio data.")
    if isinstance(data, bytes):
        return data
    return base64.b64decode(data)


def resolve_voice_id(characters: dict, speaker: str) -> tuple[str, dict]:
    entry = characters.get(speaker)
    if not entry:
        raise KeyError(f"speaker {speaker!r} is missing from voice/characters.json")
    if not entry.get("enabled", True):
        raise KeyError(f"speaker {speaker!r} is disabled")

    voice_id = (entry.get("voice_id") or "").strip()
    ref = (entry.get("voice_ref") or "").strip()
    if not voice_id and ref:
        ref_entry = characters.get(ref)
        if not ref_entry:
            raise KeyError(f"speaker {speaker!r} refers to missing voice_ref {ref!r}")
        voice_id = (ref_entry.get("voice_id") or "").strip()

    if not voice_id:
        raise KeyError(f"speaker {speaker!r} has no approved voice_id")
    return voice_id, entry


def command_extract(args: argparse.Namespace, config: dict) -> int:
    rows, warnings = iter_source_rows(config)
    write_manifest(config, rows, warnings)
    ready = sum(row["status"] == "ready" for row in rows)
    print(f"Extracted {len(rows)} spoken English lines.")
    print(f"Ready: {ready}; needs review: {len(rows) - ready}.")
    print(f"Warnings: {len(warnings)}.")
    return 0


def command_init_characters(args: argparse.Namespace, config: dict) -> int:
    registry = merge_character_registry(config, write=not args.dry_run)
    print(f"Speaker registry contains {len(registry.get('characters', {}))} entries.")
    if args.dry_run:
        print("Dry run: voice/characters.json was not changed.")
    return 0


def load_casting_request(config: dict, speaker: str, entry: dict) -> tuple[Path, dict]:
    request_dir = root_path(config.get("casting_request_dir", "voice/build/casting/requests"))
    request_path = request_dir / f"{speaker}.json"
    if not request_path.is_file():
        raise SystemExit(
            f"Voice Design request is missing for {speaker!r}: {request_path.relative_to(ROOT)}. "
            "Run: python tools/voice_profiles.py export"
        )

    request = read_json(request_path)
    voice = request.get("voice")
    if request.get("store") is not True or not isinstance(voice, dict):
        raise SystemExit(f"Invalid Voice Design request for {speaker!r}: expected store=true and voice object.")

    expected = {
        "display_name": entry.get("display_name") or speaker,
        "language_code": entry.get("language_code") or config.get("spoken_language", "en-US"),
        "gender": entry.get("gender"),
        "prompt": entry.get("design_prompt") or "",
    }
    actual_prompt = ((voice.get("prompted") or {}).get("input") or "") if isinstance(voice.get("prompted"), dict) else ""
    actual = {
        "display_name": voice.get("display_name"),
        "language_code": voice.get("language_code"),
        "gender": voice.get("gender"),
        "prompt": actual_prompt,
    }
    mismatches = [name for name in expected if expected[name] != actual[name]]
    if mismatches:
        raise SystemExit(
            f"Voice Design request for {speaker!r} is stale ({', '.join(mismatches)}). "
            "Regenerate it with: python tools/voice_profiles.py export"
        )

    if voice.get("type") != "prompted" or not voice.get("model"):
        raise SystemExit(f"Invalid Voice Design request for {speaker!r}: prompted voice model is required.")

    return request_path, request


def provider_time(value) -> str:
    if value is None:
        return ""
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def command_create_voice(args: argparse.Namespace, config: dict) -> int:
    registry_path = root_path(config["characters_file"])
    registry = read_json(registry_path, {"schema_version": 1, "characters": {}})
    characters = registry.get("characters", {})
    entry = characters.get(args.speaker)
    if not entry:
        raise SystemExit(f"Unknown speaker {args.speaker!r}. Run init-characters first.")
    if not entry.get("enabled", True):
        raise SystemExit(f"Speaker {args.speaker!r} is disabled and cannot receive a provider voice.")
    if (entry.get("voice_ref") or "").strip():
        raise SystemExit(
            f"Speaker {args.speaker!r} uses voice_ref={entry['voice_ref']!r}; create the referenced voice instead."
        )
    existing_voice_id = (entry.get("voice_id") or "").strip()
    if existing_voice_id:
        raise SystemExit(
            f"Speaker {args.speaker!r} already has voice_id={existing_voice_id!r}. "
            "The create-voice command never replaces an existing provider voice."
        )

    request_path, request = load_casting_request(config, args.speaker, entry)
    client = create_genai_client()
    created = client.voices.create(**request)
    voice_id = (getattr(created, "id", None) or "").strip()
    if not voice_id:
        raise RuntimeError("Gemini created a voice but returned no persistent voice ID.")

    request_digest = hashlib.sha256(
        json.dumps(request, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    voice = request["voice"]
    preview_dir = ROOT / "voice" / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    metadata_path = preview_dir / f"{args.speaker}.creation.json"
    write_json(metadata_path, {
        "schema_version": 1,
        "speaker": args.speaker,
        "voice_id": voice_id,
        "model": voice.get("model", ""),
        "display_name": voice.get("display_name", ""),
        "create_time": provider_time(getattr(created, "create_time", None)),
        "expire_time": provider_time(getattr(created, "expire_time", None)),
        "request_file": request_path.relative_to(ROOT).as_posix(),
        "request_sha256": request_digest,
    })

    entry["voice_id"] = voice_id
    entry["casting_status"] = "audition_pending"
    write_json(registry_path, registry)

    sample_audio = getattr(created, "sample_audio", None)
    sample_data = getattr(sample_audio, "data", None) if sample_audio is not None else None
    if sample_data:
        preview_path = preview_dir / f"{args.speaker}.wav"
        preview_path.write_bytes(decode_audio_data(sample_data))
        print(f"Saved audition sample: {preview_path.relative_to(ROOT)}")
    else:
        print("Gemini returned no sample_audio; the persistent voice ID was still stored.")

    print(f"Stored persistent voice ID for {args.speaker}: {voice_id}")
    print(f"Creation metadata: {metadata_path.relative_to(ROOT)}")
    return 0


def command_design_voice(args: argparse.Namespace, config: dict) -> int:
    registry_path = root_path(config["characters_file"])
    registry = merge_character_registry(config)
    characters = registry["characters"]

    entry = characters.get(args.speaker)
    if not entry:
        raise SystemExit(f"Unknown speaker {args.speaker!r}. Run init-characters first.")
    if not entry.get("enabled", True):
        raise SystemExit(f"Speaker {args.speaker!r} is disabled and cannot receive a provider voice.")
    if (entry.get("voice_ref") or "").strip():
        raise SystemExit(
            f"Speaker {args.speaker!r} uses voice_ref={entry['voice_ref']!r}; design the referenced voice instead."
        )
    existing_voice_id = (entry.get("voice_id") or "").strip()
    if existing_voice_id:
        raise SystemExit(
            f"Speaker {args.speaker!r} already has voice_id={existing_voice_id!r}. "
            "The design-voice command never replaces an existing provider voice."
        )

    voice = {
        "model": config["voice_design_model"],
        "type": "prompted",
        "display_name": args.display_name or entry.get("display_name") or args.speaker,
        "language_code": args.language_code or entry.get("language_code") or config["spoken_language"],
        "prompted": {"input": args.prompt},
    }
    if args.gender:
        voice["gender"] = args.gender

    client = create_genai_client()
    created = client.voices.create(store=True, voice=voice)
    entry["display_name"] = voice["display_name"]
    entry["language_code"] = voice["language_code"]
    entry["design_prompt"] = args.prompt
    entry["voice_id"] = created.id
    write_json(registry_path, registry)

    if getattr(created, "sample_audio", None) and created.sample_audio.data:
        preview_path = ROOT / "voice" / "previews" / f"{args.speaker}.wav"
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        preview_path.write_bytes(decode_audio_data(created.sample_audio.data))
        print(f"Saved preview: {preview_path.relative_to(ROOT)}")

    print(f"Stored persistent voice ID for {args.speaker}: {created.id}")
    return 0


def command_synthesize(args: argparse.Namespace, config: dict) -> int:
    rows = load_manifest(config)
    registry = merge_character_registry(config)
    characters = registry["characters"]
    overrides = read_json(root_path(config["line_overrides_file"]), {"overrides": {}}).get("overrides", {})
    model = config["preview_model"] if args.mode == "preview" else config["final_model"]
    output_dir = root_path(config["wav_output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    selected: list[dict] = []
    for row in rows:
        if row["status"] != "ready" and not args.include_review:
            continue
        if args.speaker and row["speaker"] != args.speaker:
            continue
        if args.id and row["id"] != args.id:
            continue
        if args.scene and args.scene not in row["game_source_file"]:
            continue
        selected.append(row)
        if args.limit and len(selected) >= args.limit:
            break

    if not selected:
        print("No dialogue rows matched the requested filters.")
        return 0

    client = create_genai_client()
    generated = 0
    skipped = 0
    failures = 0

    for row in selected:
        override = overrides.get(row["id"], {})
        if override.get("skip"):
            skipped += 1
            continue

        output_path = output_dir / f"{row['id']}.wav"
        if output_path.exists() and not args.force:
            skipped += 1
            continue

        try:
            voice_id, entry = resolve_voice_id(characters, row["speaker"])
        except KeyError as exc:
            print(f"SKIP {row['id']}: {exc}", file=sys.stderr)
            failures += 1
            continue

        text = (override.get("tts_text") or row["tts_text"]).strip()
        style = (override.get("style") or entry.get("default_style") or config.get("default_style") or "").strip()
        if not text:
            print(f"SKIP {row['id']}: empty TTS text", file=sys.stderr)
            failures += 1
            continue

        content = {"type": "text", "text": text}
        if style:
            content["annotations"] = [{"type": "speech_metadata", "style": style}]

        try:
            interaction = client.interactions.create(
                model=model,
                input=[{"type": "user_input", "content": [content]}],
                response_format={
                    "type": "audio",
                    "mime_type": "audio/wav",
                    "sample_rate": int(config.get("sample_rate", 24000)),
                },
                generation_config={"speech_config": [{"voice": voice_id}]},
            )
            output_path.write_bytes(decode_audio_data(interaction.output_audio.data))
            generated += 1
            print(f"OK {row['id']} -> {output_path.relative_to(ROOT)}")
        except Exception as exc:
            failures += 1
            print(f"FAIL {row['id']}: {exc}", file=sys.stderr)

    print(f"Generated: {generated}; skipped: {skipped}; failed: {failures}.")
    return 1 if failures else 0


def command_encode(args: argparse.Namespace, config: dict) -> int:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("FFmpeg was not found in PATH.")

    source_dir = root_path(config["wav_output_dir"])
    target_dir = root_path(config["ogg_output_dir"])
    target_dir.mkdir(parents=True, exist_ok=True)
    bitrate = config.get("opus_bitrate", "64k")

    wav_files = sorted(source_dir.glob("*.wav")) if source_dir.exists() else []
    if not wav_files:
        print("No generated WAV files found.")
        return 0

    converted = 0
    skipped = 0
    for wav_path in wav_files:
        ogg_path = target_dir / f"{wav_path.stem}.ogg"
        if ogg_path.exists() and not args.force:
            skipped += 1
            continue
        subprocess.run(
            [
                ffmpeg,
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-i",
                str(wav_path),
                "-c:a",
                "libopus",
                "-b:a",
                str(bitrate),
                str(ogg_path),
            ],
            check=True,
        )
        converted += 1
        print(f"OK {ogg_path.relative_to(ROOT)}")

    print(f"Converted: {converted}; skipped: {skipped}.")
    return 0



def command_studio(args: argparse.Namespace, config: dict) -> int:
    command = [sys.executable, str(ROOT / "tools" / "voice_studio.py")]
    if args.speaker:
        command.extend(["--speaker", args.speaker])
    if args.usage:
        command.append("--usage")
    return subprocess.call(command, cwd=ROOT)


def command_gui(args: argparse.Namespace, config: dict) -> int:
    del args, config
    if sys.version_info >= (3, 15):
        print(
            "PySide6 currently requires Python < 3.15. "
            "Use tools/Start-VoiceStudio.ps1 so a compatible GUI venv is created.",
            file=sys.stderr,
        )
        return 2
    command = [sys.executable, str(ROOT / "tools" / "voice_studio_gui.py")]
    return subprocess.call(command, cwd=ROOT)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract = subparsers.add_parser("extract", help="Extract English spoken dialogue into a manifest.")
    extract.set_defaults(handler=command_extract)

    init_characters = subparsers.add_parser("init-characters", help="Merge discovered speaker IDs into the registry.")
    init_characters.add_argument("--dry-run", action="store_true")
    init_characters.set_defaults(handler=command_init_characters)

    studio = subparsers.add_parser(
        "studio",
        help="Open the interactive rate-limited casting and TTS studio.",
    )
    studio.add_argument("--speaker")
    studio.add_argument("--usage", action="store_true")
    studio.set_defaults(handler=command_studio)

    gui = subparsers.add_parser(
        "gui",
        help="Open the PySide6 Windows Voice Studio.",
    )
    gui.set_defaults(handler=command_gui)

    create = subparsers.add_parser(
        "create-voice",
        help="Create one persistent Gemini voice from an exported casting request.",
    )
    create.add_argument("--speaker", required=True)
    create.set_defaults(handler=command_create_voice)

    design = subparsers.add_parser("design-voice", help="Create one persistent Gemini Voice Design persona.")
    design.add_argument("--speaker", required=True)
    design.add_argument("--display-name")
    design.add_argument("--prompt", required=True)
    design.add_argument("--gender", choices=["male", "female", "neutral"])
    design.add_argument("--language-code")
    design.set_defaults(handler=command_design_voice)

    synthesize = subparsers.add_parser("synthesize", help="Generate WAV files for selected dialogue.")
    synthesize.add_argument("--mode", choices=["preview", "final"], default="preview")
    synthesize.add_argument("--speaker")
    synthesize.add_argument("--id")
    synthesize.add_argument("--scene")
    synthesize.add_argument("--limit", type=int)
    synthesize.add_argument("--force", action="store_true")
    synthesize.add_argument("--include-review", action="store_true")
    synthesize.set_defaults(handler=command_synthesize)

    encode = subparsers.add_parser("encode", help="Convert generated WAV files to Ogg/Opus.")
    encode.add_argument("--force", action="store_true")
    encode.set_defaults(handler=command_encode)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    config = load_config()
    return args.handler(args, config)


if __name__ == "__main__":
    raise SystemExit(main())
