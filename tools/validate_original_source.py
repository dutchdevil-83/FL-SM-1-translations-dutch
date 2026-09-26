#!/usr/bin/env python3
"""Validate an imported original English Ren'Py source snapshot.

This validator is intentionally strict about snapshot integrity and credentials.
The translation/source inventory coverage is diagnostic only because it may refer
to a different game release than the installed package.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "original-source"
GAME_ROOT = SNAPSHOT / "game"
MANIFEST_PATH = SNAPSHOT / "SOURCE_MANIFEST.json"
COVERAGE_PATH = SNAPSHOT / "SOURCE_COVERAGE.json"
REPORT_PATH = SNAPSHOT / "IMPORT_REPORT.md"

FORBIDDEN_SUFFIXES = {
    ".rpyc", ".rpymc", ".pyc", ".rpa", ".exe", ".dll", ".so", ".dylib",
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp3", ".ogg", ".wav",
    ".mp4", ".webm", ".avi", ".mkv",
}
FORBIDDEN_PARTS = {"tl", "saves", "cache", "__pycache__", ".vscode", "audio"}
FORBIDDEN_EXACT = {"game/code/classes/analytics.rpy"}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "generic secret assignment": re.compile(
        r"""(?im)\b(?:secret|secret_key|client_secret|api_key|access_token|auth_token|password)\s*=\s*["'][^"'\r\n]{8,}["']"""
    ),
}
TRANSLATE_RE = re.compile(r"(?m)^\s*translate\s+(?!None\b)\S+")


def fail(message: str) -> None:
    raise SystemExit(f"[FAIL] {message}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not SNAPSHOT.exists():
        print("[INFO] original-source/ is absent; snapshot validation skipped.")
        return 0

    for required in (MANIFEST_PATH, COVERAGE_PATH, REPORT_PATH, GAME_ROOT):
        if not required.exists():
            fail(f"Required snapshot path is missing: {required.relative_to(ROOT)}")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    coverage = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))

    if manifest.get("source_kind") != "original_english_renpy_game_source":
        fail("Unexpected manifest source_kind.")

    reconstruction = manifest.get("reconstruction") or {}
    if reconstruction.get("used"):
        if float(reconstruction.get("decompile_coverage_ratio", 0.0)) != 1.0:
            fail("Compiled-script reconstruction coverage is not 100%.")
        if int(reconstruction.get("decompile_missing_count", -1)) != 0:
            fail("Manifest reports missing decompiled scripts.")
        effective = int(reconstruction.get("effective_compiled_count", -1))
        decompiled = int(reconstruction.get("decompiled_script_count", -2))
        if effective != decompiled:
            fail(
                f"Effective compiled count ({effective}) does not match "
                f"decompiled count ({decompiled})."
            )

    entries = manifest.get("files")
    if not isinstance(entries, list):
        fail("Manifest files must be an array.")

    actual_files = sorted(p for p in GAME_ROOT.rglob("*") if p.is_file())
    if len(entries) != int(manifest.get("file_count", -1)):
        fail("Manifest file_count does not match the number of manifest entries.")
    if len(actual_files) != len(entries):
        fail(
            f"Snapshot contains {len(actual_files)} files but manifest contains "
            f"{len(entries)} entries."
        )

    manifest_paths: set[str] = set()
    total_bytes = 0
    problems: list[str] = []

    for entry in entries:
        rel = str(entry.get("path", "")).replace("\\", "/")
        if not rel.startswith("game/") or rel.startswith("/") or ".." in Path(rel).parts:
            problems.append(f"unsafe manifest path: {rel!r}")
            continue

        if rel in manifest_paths:
            problems.append(f"duplicate manifest path: {rel}")
            continue
        manifest_paths.add(rel)

        target = SNAPSHOT / rel
        if not target.is_file():
            problems.append(f"missing file: {rel}")
            continue

        rel_parts = set(Path(rel).parts)
        if rel in FORBIDDEN_EXACT:
            problems.append(f"credential-bearing non-voice source must not be committed: {rel}")
        if rel_parts & FORBIDDEN_PARTS:
            problems.append(f"forbidden directory in snapshot: {rel}")
        if target.suffix.lower() in FORBIDDEN_SUFFIXES:
            problems.append(f"forbidden binary/media extension: {rel}")

        actual_size = target.stat().st_size
        total_bytes += actual_size
        if actual_size != int(entry.get("size_bytes", -1)):
            problems.append(f"size mismatch: {rel}")

        if sha256(target) != str(entry.get("source_sha256", "")).lower():
            problems.append(f"SHA-256 mismatch: {rel}")

        if target.suffix.lower() != str(entry.get("extension", "")).lower():
            problems.append(f"extension mismatch: {rel}")

        try:
            text = target.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"not UTF-8 text: {rel}")
            continue

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                problems.append(f"{label} detected: {rel}")

        if target.suffix.lower() in {".rpy", ".rpym"} and TRANSLATE_RE.search(text):
            problems.append(f"translation block detected in canonical English source: {rel}")

    actual_rel = {
        "game/" + p.relative_to(GAME_ROOT).as_posix()
        for p in actual_files
    }
    missing_manifest = sorted(actual_rel - manifest_paths)
    stale_manifest = sorted(manifest_paths - actual_rel)
    if missing_manifest:
        problems.append(f"{len(missing_manifest)} snapshot file(s) missing from manifest")
    if stale_manifest:
        problems.append(f"{len(stale_manifest)} manifest entry/entries missing from snapshot")

    if total_bytes != int(manifest.get("total_bytes", -1)):
        problems.append(
            f"total_bytes mismatch: manifest={manifest.get('total_bytes')} actual={total_bytes}"
        )

    expected = manifest.get("expected_source_coverage") or {}
    for key in ("expected_count", "covered_count", "missing_count"):
        manifest_key = {
            "expected_count": "expected_paths",
            "covered_count": "covered_paths",
            "missing_count": "missing_paths",
        }[key]
        if int(coverage.get(key, -1)) != int(expected.get(manifest_key, -2)):
            problems.append(f"coverage metadata mismatch for {key}")

    if problems:
        preview = "\n".join(f"  - {item}" for item in problems[:50])
        extra = "" if len(problems) <= 50 else f"\n  ... and {len(problems) - 50} more"
        fail(f"Original-source snapshot validation found {len(problems)} problem(s):\n{preview}{extra}")

    print(
        "[OK] Original-source snapshot validated: "
        f"{len(entries)} files, {total_bytes} bytes, "
        f"compiled reconstruction={float(reconstruction.get('decompile_coverage_ratio', 1.0)):.2%}, "
        f"inventory coverage={float(expected.get('coverage_ratio', 0.0)):.2%} (advisory)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
