#!/usr/bin/env python3
"""Build English Ren'Py voice assets from embedded source dialogue.

Extraction is standard-library only. Gemini is imported only by commands that
actually call the TTS or Voices APIs.
"""

from __future__ import annotations

import argparse
import base64
import csv
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

SPEC = importlib.util.spec_from_file_location("voice_source_validator", VALIDATOR_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)

SPEAKER_RE = re.compile(r"^([A-Za-z_][\w.]*)\s+\"\"")
VARIABLE_RE = re.compile(r"\[([A-Za-z_][\w.]*)\]")
PERCENT_VAR_RE = re.compile(r"%\([^)]+\)[#0 +\-]?(?:\d+|\*)?(?:\.\d+)?[diouxXeEfFgGcrs]")
WAIT_TAG_RE = re.compile(r"\{(?:w(?:=[^}]*)?|p)\}", re.IGNORECASE)
BRACE_TAG_RE = re.compile(r"\{[^{}]*\}")


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


def speaker_from_shape(shape: str) -> str | None:
    match = SPEAKER_RE.match(shape)
    return match.group(1) if match else None


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


def source_signature(block) -> tuple:
    return tuple((unit.source_shape, unit.source) for unit in block.units)


def analyze_source_file(path: Path) -> dict:
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


def candidate_languages(manifest_row: dict, config: dict) -> list[str]:
    declared = [
        value.strip()
        for value in (manifest_row.get("present_in_languages") or "").split(";")
        if value.strip()
    ]
    reference = (manifest_row.get("count_reference_language") or "").strip()
    if reference and reference not in declared:
        declared.append(reference)

    priority = config.get("reference_language_priority", [])
    rank = {language: index for index, language in enumerate(priority)}
    return sorted(set(declared), key=lambda language: (rank.get(language, 999), language))


def select_source_file(relative_path: str, manifest_row: dict, config: dict) -> tuple[dict | None, list[str]]:
    warnings: list[str] = []
    candidates: list[tuple[str, dict]] = []

    for language in candidate_languages(manifest_row, config):
        path = ROOT / language / relative_path
        if not path.exists():
            continue
        analysis = analyze_source_file(path)
        candidates.append((language, analysis))

    if not candidates:
        return None, [f"missing all source-language candidates for: {relative_path}"]

    priority = config.get("reference_language_priority", [])
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
            f"no conflict-free source-language file for {relative_path}; "
            f"best candidate {language!r} still has conflicting translation IDs: {details}"
        )

    preferred = (manifest_row.get("count_reference_language") or "").strip()
    if preferred and language != preferred:
        warnings.append(
            f"voice source resolver selected {language}/{relative_path} instead of "
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


def iter_source_rows(config: dict) -> tuple[list[dict], list[str]]:
    manifest_path = root_path(config["source_manifest"])
    variables = load_variables(config)
    skip_speakers = set(config.get("skip_speakers", []))
    rows_by_id: dict[str, dict] = {}
    warnings: list[str] = []
    conflicts: list[str] = []

    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        source_manifest = list(csv.DictReader(handle))

    for manifest_row in source_manifest:
        relative_path = (manifest_row.get("relative_path") or "").strip()
        if not relative_path:
            continue

        selected, selection_warnings = select_source_file(relative_path, manifest_row, config)
        warnings.extend(selection_warnings)
        if selected is None:
            continue

        reference_path = selected["path"]
        reference_language = selected["language"]

        for block in selected["blocks"]:
            unit_count = len(block.units)
            for unit_index, unit in enumerate(block.units, start=1):
                speaker = speaker_from_shape(unit.source_shape)
                english_text = " ".join(part for part in unit.source if part).strip()
                if not english_text:
                    continue

                tts_text, unresolved = prepare_tts_text(english_text, variables)
                reasons: list[str] = []
                if not speaker:
                    reasons.append("speaker-not-resolved")
                if speaker in skip_speakers:
                    reasons.append("speaker-skipped-by-config")
                if unresolved:
                    reasons.append("unresolved-variable:" + ",".join(unresolved))
                if unit_count != 1:
                    reasons.append("multi-unit-translation-block")

                row_id = block.block_id if unit_count == 1 else f"{block.block_id}__u{unit_index}"
                occurrence = {
                    "reference_language": reference_language,
                    "reference_file": reference_path.relative_to(ROOT).as_posix(),
                    "source_line": unit.source_line,
                }
                row = {
                    "id": row_id,
                    "renpy_id": block.block_id,
                    "unit_index": unit_index,
                    "speaker": speaker or "",
                    "english_text": english_text,
                    "tts_text": tts_text,
                    "status": "ready" if not reasons else "needs_review",
                    "review_reasons": reasons,
                    "reference_language": reference_language,
                    "reference_file": reference_path.relative_to(ROOT).as_posix(),
                    "game_source_file": relative_path,
                    "source_line": unit.source_line,
                    "source_occurrences": [occurrence],
                }

                existing = rows_by_id.get(row_id)
                if existing is None:
                    rows_by_id[row_id] = row
                    continue

                same_voice_line = (
                    existing["speaker"] == row["speaker"]
                    and existing["english_text"] == row["english_text"]
                    and existing["tts_text"] == row["tts_text"]
                )
                if same_voice_line:
                    existing["source_occurrences"].extend(row["source_occurrences"])
                    warnings.append(
                        f"deduplicated identical global voice ID {row_id} from {relative_path}"
                    )
                    continue

                conflicts.append(
                    f"{row_id}: {existing['speaker']} {existing['english_text']!r} "
                    f"vs {row['speaker']} {row['english_text']!r}"
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
    source_language_counts = Counter(row["reference_language"] for row in rows)
    ready_count = sum(row["status"] == "ready" for row in rows)
    stats = {
        "total_lines": len(rows),
        "ready_lines": ready_count,
        "needs_review_lines": len(rows) - ready_count,
        "speaker_count": len(speaker_counts),
        "speakers": dict(sorted(speaker_counts.items(), key=lambda item: (-item[1], item[0]))),
        "source_languages": dict(sorted(source_language_counts.items())),
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

    for speaker, count in sorted(counts.items()):
        if speaker in characters:
            characters[speaker]["line_count"] = count
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

    if not os.environ.get("GEMINI_API_KEY"):
        raise SystemExit("GEMINI_API_KEY is not set.")
    return genai


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


def command_design_voice(args: argparse.Namespace, config: dict) -> int:
    genai = require_genai()
    registry_path = root_path(config["characters_file"])
    registry = merge_character_registry(config)
    characters = registry["characters"]

    entry = characters.get(args.speaker)
    if not entry:
        raise SystemExit(f"Unknown speaker {args.speaker!r}. Run init-characters first.")
    if (entry.get("voice_ref") or "").strip():
        raise SystemExit(
            f"Speaker {args.speaker!r} uses voice_ref={entry['voice_ref']!r}; design the referenced voice instead."
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

    client = genai.Client()
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
    genai = require_genai()
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

    client = genai.Client()
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract = subparsers.add_parser("extract", help="Extract English spoken dialogue into a manifest.")
    extract.set_defaults(handler=command_extract)

    init_characters = subparsers.add_parser("init-characters", help="Merge discovered speaker IDs into the registry.")
    init_characters.add_argument("--dry-run", action="store_true")
    init_characters.set_defaults(handler=command_init_characters)

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
