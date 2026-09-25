#!/usr/bin/env python3
"""Recover original speaker syntax without changing dialogue or translation files."""
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


def collect(root: Path = ROOT) -> list[dict]:
    manifest = root / "voice/build/dialogue_manifest.jsonl"
    rows = [json.loads(line) for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip()]
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


def main() -> None:
    result = collect()
    output = ROOT / "voice/build/speaker_syntax.jsonl"
    temporary = output.with_suffix(".tmp")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in result), encoding="utf-8")
    temporary.replace(output)
    print(f"Preserved speaker syntax for {len(result)} dialogue rows. API calls: 0.")


if __name__ == "__main__":
    main()
