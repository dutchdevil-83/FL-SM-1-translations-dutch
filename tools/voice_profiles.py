#!/usr/bin/env python3
"""Validate/export researched voice profiles and Gemini request files, offline only."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MODELS = {"gemini-3.8-flash-tts", "gemini-3.8-flash-lite-tts"}
TOKEN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8-sig") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected an object: {path}")
    return value


def resolve_identity(characters: dict[str, Any], speaker: str) -> str:
    seen: set[str] = set()
    while True:
        if speaker in seen:
            raise ValueError("Cyclic voice_ref: " + speaker)
        if speaker not in characters:
            raise ValueError("Missing voice_ref target: " + speaker)
        seen.add(speaker)
        entry = characters[speaker]
        reference = entry.get("voice_ref", "")
        if not reference:
            return speaker
        speaker = reference


def validate_registry(registry: dict[str, Any], sources: dict[str, Any]) -> None:
    if registry.get("schema_version") != 1 or registry.get("profile_schema_version") != 1:
        raise ValueError("Unsupported character/profile schema")
    characters = registry.get("characters")
    if not isinstance(characters, dict) or not characters:
        raise ValueError("Missing characters")
    ids: dict[str, str] = {}
    for speaker, entry in characters.items():
        if not TOKEN.fullmatch(speaker):
            raise ValueError("Unsafe speaker token: " + speaker)
        if entry.get("gender") not in {"male", "female", "neutral"}:
            raise ValueError("Invalid proposed voice gender: " + speaker)
        if not isinstance(entry.get("enabled"), bool):
            raise ValueError("enabled must be boolean: " + speaker)
        if not str(entry.get("language_code", "")).startswith("en-"):
            raise ValueError("Only English vocal locales are allowed: " + speaker)
        profile = entry.get("profile", {})
        age = profile.get("canonical_age_years")
        if age is not None and (type(age) is not int or age < 0):
            raise ValueError("Invalid canonical age: " + speaker)
        if not profile.get("evidence_ids"):
            raise ValueError("Missing dialogue provenance: " + speaker)
        for source_id in profile.get("official_source_ids", []):
            if source_id not in sources.get("sources", {}):
                raise ValueError("Unknown source ID: " + source_id)
        target = resolve_identity(characters, speaker)
        if entry.get("voice_ref") and entry.get("voice_id"):
            raise ValueError("Alias has its own voice_id: " + speaker)
        if entry.get("enabled") and not characters[target].get("enabled"):
            raise ValueError("Enabled alias refers to disabled identity: " + speaker)
        if entry.get("enabled") and not entry.get("voice_ref") and not entry.get("design_prompt", "").strip():
            raise ValueError("Missing design prompt: " + speaker)
        if profile.get("identity_status") in {"dynamic_performer", "unresolved_binding"} and entry.get("enabled"):
            raise ValueError("Unresolved identity must remain disabled: " + speaker)
        voice_id = entry.get("voice_id", "")
        if voice_id:
            if not voice_id.startswith("voice_"):
                raise ValueError("Expected a persistent designed voice ID: " + speaker)
            if voice_id in ids and ids[voice_id] != target:
                raise ValueError("Distinct identities share one voice_id; use an explicit alias")
            ids[voice_id] = target


def voice_metadata(entry: dict[str, Any]) -> dict[str, str]:
    """Map casting facets to documented Voice discovery metadata, not acoustic knobs."""
    profile = entry["profile"]
    accent_text = profile["accent"]
    if "Dutch" in accent_text:
        accent, region = "Dutch", "NL"
    elif "Korean" in accent_text:
        accent, region = "South Korean", "KR"
    elif accent_text == "General American English":
        # These are proposed accent labels, never inferred citizenship.
        accent, region = "American", "US"
    else:
        raise ValueError("Unmapped proposed accent: " + accent_text)
    pitch = profile["pitch"]
    return {
        "accent": accent,
        "region_code": region,
        "context": "Conversational",
        "description": entry["design_prompt"],
        "persona": profile["cadence"],
        "pitch": pitch if pitch in {"low", "medium", "high"} else "medium",
    }


def design_request(registry: dict[str, Any], speaker: str, model: str) -> dict[str, Any]:
    if model not in MODELS:
        raise ValueError("Unverified Voice Design model: " + model)
    entry = registry["characters"][speaker]
    if entry.get("voice_ref") or not entry.get("enabled"):
        raise ValueError("Aliases and unresolved speakers have no creation request: " + speaker)
    # Deliberate allowlist from CreateVoiceRequest/Voice. No output-only fields.
    return {"store": True, "voice": {
        "model": model, "type": "prompted", "display_name": entry["display_name"],
        "gender": entry["gender"], "language_code": entry["language_code"],
        "prompted": {"input": entry["design_prompt"]},
        **voice_metadata(entry),
    }}


def audit_manifest(registry: dict[str, Any], manifest: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    rows: dict[str, Any] = {}
    counts: Counter[str] = Counter()
    unresolved: list[dict[str, Any]] = []
    with manifest.open(encoding="utf-8") as handle:
        for raw in handle:
            if not raw.strip():
                continue
            row = json.loads(raw)
            if row["id"] in rows:
                raise ValueError("Duplicate manifest ID: " + row["id"])
            rows[row["id"]] = row
            if row["speaker"]:
                counts[row["speaker"]] += 1
            else:
                # Report IDs/locations, not copied narrative content.
                unresolved.append({k: row[k] for k in ("id", "reference_file", "source_line", "review_reasons")})
    characters = registry["characters"]
    missing = set(counts) - set(characters)
    unexpected = set(characters) - set(counts)
    if missing or unexpected:
        raise ValueError(f"Speaker coverage differs: missing={sorted(missing)}, unexpected={sorted(unexpected)}")
    evidence: dict[str, Any] = {}
    commit = registry["research"]["source_commit"]
    repo = registry["research"]["source_repository"]
    for speaker, entry in characters.items():
        if entry.get("line_count") != counts[speaker]:
            raise ValueError("Stale dialogue count: " + speaker)
        evidence[speaker] = []
        for identifier in entry["profile"]["evidence_ids"]:
            if identifier not in rows:
                raise ValueError("Missing evidence ID: " + identifier)
            row = rows[identifier]
            path = row["reference_file"]
            line = row["source_line"]
            evidence[speaker].append({"id": identifier, "speaker": row["speaker"],
                "url": f"https://github.com/{repo}/blob/{commit}/{path}#L{line}",
                "reference_file": path, "source_line": line})
    return {"speaker_tokens": len(counts), "dialogue_rows": len(rows),
        "untokenized_rows": len(unresolved), "unresolved_dialogue": unresolved}, evidence


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def export_profiles(registry: dict[str, Any], sources: dict[str, Any], audit: dict[str, Any],
                    evidence: dict[str, Any], destination: Path, model: str) -> dict[str, Any]:
    # Use a fresh generation directory; never leave stale requests for newly blocked identities.
    destination.mkdir(parents=True, exist_ok=True)
    for name in ("profiles", "requests"):
        folder = destination / name
        folder.mkdir(exist_ok=True)
        if folder.is_symlink():
            raise ValueError("Generated folder must not be a symlink: " + str(folder))
        for previous in folder.glob("*.json"):
            previous.unlink()
    requests = 0
    aliases: dict[str, str] = {}
    blocked: list[str] = []
    for speaker, entry in registry["characters"].items():
        target = resolve_identity(registry["characters"], speaker)
        write_json(destination / "profiles" / f"{speaker}.json", {
            "speaker": speaker, "voice_identity": target, "character": entry,
            "voice_metadata": voice_metadata(registry["characters"][target]) if entry["enabled"] else None,
            "evidence": evidence[speaker],
            "official_sources": {k: sources["sources"][k] for k in entry["profile"]["official_source_ids"]},
        })
        if entry.get("voice_ref"):
            aliases[speaker] = target
        elif not entry["enabled"]:
            blocked.append(speaker)
        else:
            write_json(destination / "requests" / f"{speaker}.json", design_request(registry, speaker, model))
            requests += 1
    write_json(destination / "unresolved_dialogue.json", audit["unresolved_dialogue"])
    digest = hashlib.sha256(json.dumps(registry, sort_keys=True, ensure_ascii=True).encode()).hexdigest()
    summary = {k: v for k, v in audit.items() if k != "unresolved_dialogue"}
    summary.update({"design_request_files": requests, "aliases": aliases, "blocked_speakers": blocked,
                    "registry_sha256": digest, "api_calls": 0,
                    "status": "research_and_casting_proposals_not_auditioned_voices"})
    write_json(destination / "summary.json", summary)
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "export"))
    parser.add_argument("--registry", type=Path, default=ROOT / "voice/characters.json")
    parser.add_argument("--sources", type=Path, default=ROOT / "voice/character_sources.json")
    parser.add_argument("--manifest", type=Path, default=ROOT / "voice/build/dialogue_manifest.jsonl")
    parser.add_argument("--output", type=Path, default=ROOT / "voice/build/casting")
    parser.add_argument("--model", choices=sorted(MODELS), default="gemini-3.8-flash-tts")
    args = parser.parse_args(argv)
    try:
        registry, sources = load_json(args.registry), load_json(args.sources)
        validate_registry(registry, sources)
        audit, evidence = audit_manifest(registry, args.manifest)
        if args.command == "export":
            # Prevent accidental deletion/writes outside the ignored voice/build tree.
            build_root = (ROOT / "voice/build").resolve()
            destination = args.output.resolve()
            if destination == build_root or build_root not in destination.parents:
                raise ValueError("Export output must be a subdirectory of voice/build")
            summary = export_profiles(registry, sources, audit, evidence, destination, args.model)
            print(json.dumps(summary, indent=2))
        else:
            print(f"Validated {audit['speaker_tokens']} tokens against {audit['dialogue_rows']} dialogue rows. API calls: 0.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
