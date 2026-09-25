#!/usr/bin/env python3
"""Recover source syntax and alternate malformed-block evidence without source edits."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("syntax_validator", ROOT / "tools/dutch_translation_validate.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def read_manifest(root: Path) -> list[dict]:
    return [json.loads(line) for line in (root / "voice/build/dialogue_manifest.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]


def collect(root: Path = ROOT) -> list[dict]:
    rows = read_manifest(root)
    cache: dict[str, list[str]] = {}
    result = []
    for row in rows:
        path = row["reference_file"]
        resolved = (root / path).resolve()
        if root.resolve() not in resolved.parents:
            raise ValueError("Source path escapes the repository")
        if path not in cache:
            cache[path] = resolved.read_text(encoding="utf-8-sig").splitlines()
        source = cache[path][row["source_line"] - 1].lstrip()
        if not source.startswith("#"):
            raise ValueError("Source location is no longer an English comment: " + row["id"])
        statement = source[1:].lstrip()
        parsed = VALIDATOR.extract_statement(statement)
        if parsed is None:
            raise ValueError("Source statement has no literals: " + row["id"])
        literals, shape = parsed
        if " ".join(part for part in literals if part).strip() != row["english_text"]:
            raise ValueError("Source text changed: " + row["id"])
        result.append({"id": row["id"], "source_shape": shape, "source_literals": list(literals),
                       "statement_sha256": hashlib.sha256(statement.encode("utf-8")).hexdigest()})
    return result


def alternate_evidence(root: Path = ROOT) -> dict:
    rows = read_manifest(root)
    paths = {row["game_source_file"] for row in rows if "multi-unit-translation-block" in row["review_reasons"]}
    result = {}
    # Capture complete block metadata in the few affected scenes. It exposes the original
    # identifiers for orphan comments without assuming adjacent translation order is runtime order.
    for relative in sorted(paths):
        result[relative] = {}
        for language in ("deutsch", "italian", "french", "spanish", "portuguese", "turkish", "chinese"):
            path = (root / language / relative).resolve()
            if root.resolve() not in path.parents:
                raise ValueError("Candidate source escapes the repository")
            if not path.exists():
                continue
            blocks, problems = VALIDATOR.parse_translation_file(path, strict_missing_targets=False)
            result[relative][language] = {
                "path": path.relative_to(root).as_posix(),
                "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "parse_problem_count": len(problems),
                "blocks": [{"id": b.block_id, "line": b.line,
                            "units": [{"literals": list(u.source), "shape": u.source_shape,
                                       "source_line": u.source_line} for u in b.units]}
                           for b in blocks if b.block_id != "strings"]}
    return {"schema_version": 1, "scenes": result}


def main() -> None:
    result = collect()
    output = ROOT / "voice/build/speaker_syntax.jsonl"
    temporary = output.with_suffix(".tmp")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in result), encoding="utf-8")
    temporary.replace(output)
    evidence = ROOT / "voice/build/source_candidates.json"
    evidence.write_text(json.dumps(alternate_evidence(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Preserved speaker syntax for {len(result)} dialogue rows and alternate malformed-scene evidence. API calls: 0.")


if __name__ == "__main__":
    main()
