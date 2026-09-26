#!/usr/bin/env python3
"""Verify canonical original-source syntax and emit offline review evidence."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "syntax_validator", ROOT / "tools" / "dutch_translation_validate.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def read_manifest(root: Path) -> list[dict]:
    path = root / "voice" / "build" / "dialogue_manifest.jsonl"
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def collect(root: Path = ROOT) -> list[dict]:
    rows = read_manifest(root)
    cache: dict[str, list[str]] = {}
    result: list[dict] = []

    for row in rows:
        source_file = row.get("source_file")
        source_line = int(row.get("source_line") or 0)
        if not source_file or source_line <= 0:
            raise ValueError("Dialogue row has no canonical source location: " + row["id"])

        resolved = (root / source_file).resolve()
        if root.resolve() not in resolved.parents:
            raise ValueError("Source path escapes the repository")
        if source_file not in cache:
            cache[source_file] = resolved.read_text(encoding="utf-8-sig").splitlines()

        lines = cache[source_file]
        if source_line > len(lines):
            raise ValueError("Source line is outside the canonical file: " + row["id"])

        statement = lines[source_line - 1].strip()
        parsed = VALIDATOR.extract_statement(statement)
        if parsed is None:
            raise ValueError("Canonical source statement has no literals: " + row["id"])

        literals, shape = parsed
        expected_literals = tuple(row.get("source_literals") or ())
        expected_shape = row.get("source_shape") or ""
        if shape != expected_shape:
            raise ValueError("Canonical source shape changed: " + row["id"])
        if tuple(literals) != expected_literals:
            raise ValueError("Canonical source literals changed: " + row["id"])

        result.append(
            {
                "id": row["id"],
                "renpy_id": row.get("renpy_id") or "",
                "source_file": source_file,
                "source_line": source_line,
                "source_shape": shape,
                "source_literals": list(literals),
                "statement_sha256": hashlib.sha256(statement.encode("utf-8")).hexdigest(),
            }
        )

    return result


def review_evidence(root: Path = ROOT) -> dict:
    rows = read_manifest(root)
    unresolved = [
        {
            "id": row["id"],
            "renpy_id": row.get("renpy_id") or "",
            "source_file": row.get("source_file") or "",
            "source_line": row.get("source_line") or 0,
            "speaker": row.get("speaker") or "",
            "speaker_label": row.get("speaker_label") or "",
            "review_reasons": row.get("review_reasons") or [],
        }
        for row in rows
        if row.get("status") != "ready"
    ]
    reason_counts = Counter(
        reason
        for row in unresolved
        for reason in row.get("review_reasons", [])
    )
    return {
        "schema_version": 2,
        "source_kind": "canonical_original_english_game_source",
        "total_rows": len(rows),
        "needs_review_rows": len(unresolved),
        "review_reason_counts": dict(
            sorted(reason_counts.items(), key=lambda item: (-item[1], item[0]))
        ),
        "rows": unresolved,
    }


def main() -> None:
    result = collect()
    output = ROOT / "voice" / "build" / "speaker_syntax.jsonl"
    temporary = output.with_suffix(".tmp")
    temporary.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in result),
        encoding="utf-8",
    )
    temporary.replace(output)

    evidence = ROOT / "voice" / "build" / "source_candidates.json"
    evidence.write_text(
        json.dumps(review_evidence(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Verified canonical source syntax for {len(result)} dialogue rows and "
        "wrote unresolved-line review evidence. API calls: 0."
    )


if __name__ == "__main__":
    main()
