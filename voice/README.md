# English voice pipeline

This branch is intentionally separate from the Dutch subtitle work.

## Scope

- Spoken dialogue stays English.
- Dutch translation files are only used as project metadata; the spoken source text comes from the embedded English source comments already present in the upstream translation files.
- The existing `docs/dutch/PHASE0_FILE_MANIFEST.csv` supplies the scene inventory. For each scene the voice extractor inspects all available translation-language copies and chooses the cleanest, most complete embedded-English source. This avoids inheriting duplicate/corrupt translation IDs from one language while remaining independent of Dutch translation progress.
- Generated audio is not committed by default. Raw/generated files are ignored to avoid turning the repository into a multi-gigabyte audio dump.

## Models

- Preview: `gemini-3.8-flash-lite-tts`
- Final: `gemini-3.8-flash-tts`
- Voice design: `gemini-3.8-flash-tts`

On a Gemini Developer API **Free Tier** project, Standard input and audio output for these two TTS models are currently listed by Google as free of charge. Requests still consume the project's applicable Free Tier quota and rate limits. Enabling billing changes the project's usage tier and paid pricing can then apply.

Each real character should receive one persistent `voice_...` ID. The `mct` speaker is configured to reuse the main character voice by default, with a different delivery style.

For the project-specific Google AI Studio setup, Voice Design workflow, API-key setup and Free Tier notes, see [AI_STUDIO_SETUP.md](AI_STUDIO_SETUP.md).

For a ready-to-paste Google AI Studio Build-mode prompt that creates a full-stack casting/review dashboard for this exact project, see [AI_STUDIO_BUILD_PROMPT.md](AI_STUDIO_BUILD_PROMPT.md).

## Researched character casting pack

The registry now covers the 58 nonempty speaker tokens in the English manifest.
[CHARACTER_RESEARCH.md](CHARACTER_RESEARCH.md) records confirmed facts, proposed casting
directions, cross-game matches and unresolved identities. Unknown canonical ages are
not replaced by invented facts. [MODEL_INPUTS.md](MODEL_INPUTS.md) documents the supported
Gemini creation fields and the distinction between discovery metadata and voice direction.

After extraction, validate and export the individual profile/request files without
making any Gemini calls:

```powershell
python tools/voice_profiles.py validate
python tools/voice_profiles.py export
```

The export under `voice/build/casting/` contains 58 profiles and 50 eligible Voice Design
request files. Two protagonist aliases reuse `mc`; six uncertain or dynamic speaker
bindings remain disabled. Another 474 manifest rows lack a resolved speaker token and
are listed separately for review. These counts are a source snapshot, not a claim that
all distinct characters or every game line have already been cast.

GitHub Actions publishes the resulting `english-character-casting-pack` artifact.
The files describe proposed voices: provider IDs remain empty until real voices are
created and auditioned. The existing `design-voice` CLI still takes an explicit prompt;
use the exported request object when all optional casting metadata must be retained.

## Import the original English game source from Windows

The canonical English Ren'Py source can live on another developer machine. The importer defaults to the primary clone at `X:\\dev\\repos\\personal\\FL-SM-1-translations-dutch`, then automatically resolves the Git worktree that has `voice/english-gemini-tts` checked out. Tooling work stays on that canonical voice branch.

```powershell
& {
    pwsh -NoProfile -File "X:\dev\repos\personal\FL-SM-1-translations-dutch\tools\Import-OriginalGameVoiceSource.ps1"
}
```

The importer now defaults to the installed game at `E:\\Games\\Fetish Locator SM Studio`. If that folder is unavailable, it falls back to a Windows folder picker where either the installation folder or its `game` folder can be selected.

It then:

- finds original source-like files such as `.rpy`, `.rpym`, `.py`, JSON and configuration files;
- excludes `game/tl`, compiled files, saves, cache, media, archives and executables;
- scans selected text files for common credential patterns before committing anything;
- copies the snapshot to `original-source/game/`;
- creates `original-source/SOURCE_MANIFEST.json` with SHA-256 hashes and sizes;
- keeps the canonical voice worktree on `voice/english-gemini-tts`;
- creates a temporary Git worktree and timestamped branch from that voice branch only for the imported source snapshot;
- commits and pushes the snapshot;
- opens a **draft pull request** against `voice/english-gemini-tts` for review;
- removes the temporary import worktree after a successful push/PR, while leaving the canonical voice worktree untouched.

Requirements on the developer machine:

```text
PowerShell 7.2+
Git
GitHub CLI (gh), authenticated with gh auth login
A local clone at `X:\dev\repos\personal\FL-SM-1-translations-dutch` and a clean worktree with `voice/english-gemini-tts` checked out
```

No Gemini/TTS request is made by the importer. The imported PR should remain unmerged until the English source has been reviewed and the voice extractor has been switched from translation-export recovery to direct original-source ingestion.

For a local-only dry run without pushing:

```powershell
pwsh -NoProfile -File "X:\dev\repos\personal\FL-SM-1-translations-dutch\tools\Import-OriginalGameVoiceSource.ps1" -SkipPush
```

## Setup

```powershell
& {
    Set-Location "<repo-root>"
    py -m venv .venv-voice
    .\.venv-voice\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements-voice.txt
}
```

Set the Gemini API key only in your local environment or GitHub secret storage. Do not commit it.

```powershell
$env:GEMINI_API_KEY = "<your-key>"
```

## 1. Extract the English dialogue

```powershell
python tools/voice_pipeline.py extract
```

This creates:

- `voice/build/dialogue_manifest.jsonl`
- `voice/build/speaker_stats.json`

Each manifest row contains the Ren'Py translation ID, speaker token, original English text, cleaned TTS text, source file and review status.

Lines with unresolved Ren'Py variables such as `[mcname]` are marked `needs_review` instead of being synthesized blindly.

## 2. Create the speaker registry

```powershell
python tools/voice_pipeline.py init-characters
```

This merges discovered speaker IDs into `voice/characters.json` without overwriting voice IDs or prompts you already approved.

## 3. Design and lock a character voice

Example:

```powershell
python tools/voice_pipeline.py design-voice --speaker arj --display-name "AmRose" --gender female --language-code en-US --prompt "A woman in her mid twenties with a warm but guarded American voice, intelligent, emotionally expressive, natural conversational cadence."
```

The command stores the returned persistent `voice_...` ID in `voice/characters.json` and saves the API preview to `voice/previews/<speaker>.wav`.

Design the core vocal identity once. Use line styles only for temporary emotion or delivery.

## 4. Preview a small batch

```powershell
python tools/voice_pipeline.py synthesize --mode preview --speaker arj --limit 20
```

Nothing is regenerated unless `--force` is supplied.

## 5. Generate final WAV files

```powershell
python tools/voice_pipeline.py synthesize --mode final
```

Output:

```text
voice/generated/wav/<renpy-id>.wav
```

## 6. Encode for Ren'Py

Install FFmpeg, then run:

```powershell
python tools/voice_pipeline.py encode
```

Output:

```text
voice/generated/ogg/<renpy-id>.ogg
```

The encoder uses Opus in an Ogg container by default.

## 7. Integrate into the game

Copy:

```text
voice/renpy/english_voice_config.rpy
```

into the game's `game/` directory and place final audio under:

```text
game/voice/en/
```

The provided Ren'Py config uses:

```renpy
define config.auto_voice = "voice/en/{id}.ogg"
```

This keeps the English voice layer independent from the selected subtitle language, so Dutch subtitles can continue changing without invalidating the voice work.

## Variables and exceptional lines

Create `voice/variables.local.json` locally when a spoken replacement is stable, for example a fixed protagonist name. The file is intentionally ignored by Git.

Use `voice/line_overrides.json` for reviewed one-off changes:

```json
{
  "schema_version": 1,
  "overrides": {
    "sm1cs_arj001_5d6702d2": {
      "style": "worried and cautious",
      "tts_text": "Man... I hope AmRose is a little less... spicy this time."
    }
  }
}
```

An override can also contain `"skip": true`.

## Safety against accidental quota consumption

Extraction, tests, registry initialization, profile validation/export and encoding do not call Gemini. Only `design-voice` and `synthesize` consume Gemini API quota.

When the API key belongs to a Gemini Developer API Free Tier project, supported Standard requests to the configured Gemini 3.8 TTS models are free of charge within that project's active Free Tier limits. The pipeline does not require billing, Batch or Flex mode.

Generated files are skipped on reruns unless `--force` is supplied, which also prevents wasting quota after a rate-limit interruption.
