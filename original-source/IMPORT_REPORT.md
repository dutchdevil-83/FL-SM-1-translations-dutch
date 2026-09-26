# Original English game source import

Imported at UTC: 2026-09-26T00:22:48.5787922Z
Importer version: 202609.26
Source folder label: materialized
Repository: dutchdevil-83/FL-SM-1-translations-dutch
Base branch: voice/english-gemini-tts
Import branch: voice/import-original-source-20260926-022221

## Scope

This snapshot contains original English Ren'Py source-like text files needed to reconstruct dialogue, speaker bindings, variables, character definitions, labels, and related voice integration context.

The importer deliberately excludes translation folders, compiled Ren'Py/Python files, saves, caches, media, archives, and executables.

No AI/TTS requests are made by the importer.

Credential-bearing non-voice source excluded during review: `game/code/classes/analytics.rpy`.

## File counts

| Extension | Files |
| --- | ---: |
| .rpy | 499 |
| .txt | 1 |

Total imported files: 500
Total imported bytes: 6857353

## Reconstruction

RPA archives processed: 5
Loose compiled scripts found: 451
Effective compiled scripts discovered: 500
Compiled scripts decompiled: 500
Effective compiled-script reconstruction: 100.00%
Archive path conflicts resolved by archive priority: 0
Reconstruction tool: rpycdec 0.2.0

## Expected source coverage

Expected .rpy paths from project inventory: 444
Covered paths: 391
Missing paths: 53
Coverage: 88.06%

See SOURCE_COVERAGE.json for the exact missing-path review list.

## Review

Review this draft pull request before merging. SOURCE_MANIFEST.json records the original SHA-256 hash and size for every imported file.

After merge, the English voice extractor can be changed to treat original-source/game as the canonical dialogue and character source.


## Automated review checks

- Effective compiled Ren'Py reconstruction: 500/500 (100.00%).
- Imported source payload after review: 499 .rpy files plus script_version.txt.
- Translation root, compiled files, archives, media, saves and cache are excluded.
- Credential-bearing non-voice analytics source was removed during review.
- Project inventory coverage remains 391/444 (88.06%) and is advisory because the installed build reports game version 0.9.20.
- CI validates manifest hashes, sizes, file counts, source-only scope and credential patterns before merge.
