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

The registry currently contains 59 researched speaker profiles; the canonical imported build exposes 49 active speaker tokens.
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

The export under `voice/build/casting/` contains 59 profiles and 51 eligible Voice Design
request files. Two protagonist aliases reuse `mc`; six uncertain or dynamic speaker
bindings remain disabled. The current canonical source audit reports 201 untokenized
rows for manual review. These counts are tied to the imported game build and may differ
from historical research snapshots.

GitHub Actions publishes the resulting `english-character-casting-pack` artifact.
The files describe proposed voices: provider IDs remain empty until real voices are
created and auditioned. Prefer `create-voice --speaker <token>` to create a provider
voice directly from the exported request object, retaining all verified casting metadata.
The older `design-voice` command remains available for explicit ad-hoc prompt creation.

## Import the original English game source from Windows

The canonical English Ren'Py source can live on another developer machine. The importer defaults to the primary clone at `X:\\dev\\repos\\personal\\FL-SM-1-translations-dutch`, then automatically resolves the Git worktree that has `voice/english-gemini-tts` checked out. Tooling work stays on that canonical voice branch.

```powershell
& {
    pwsh -NoProfile -File "X:\dev\repos\personal\FL-SM-1-translations-dutch\tools\Import-OriginalGameVoiceSource.ps1"
}
```

The importer defaults to the installed game at `E:\\Games\\Fetish Locator SM Studio`. If that folder is unavailable, it falls back to a Windows folder picker where either the installation folder or its `game` folder can be selected.

Released Ren'Py games often contain most creator scripts as compiled `.rpyc` / `.rpymc` files and inside `.rpa` archives rather than as loose `.rpy` files. The importer therefore reconstructs the effective English source in a temporary workspace when packaged scripts are detected. It uses a temporary Python virtual environment with pinned `rpycdec 0.2.0`, verifies the published wheel SHA-256, extracts only source/data candidates, decompiles compiled scripts, and never modifies the installed game.

It then:

- scans loose source files plus `.rpa`, `.rpyc` and `.rpymc` packaging;
- reconstructs source from archives/compiled scripts in a temporary workspace when needed;
- prefers direct loose source when the same path is also present in packaged content;
- excludes `game/tl`, saves, cache, audio/media, binary archives, compiled files and executables from the PR;
- scans reconstructed text files for common credential patterns before committing anything;
- compares reconstructed `.rpy` paths against the 444-path project translation/source inventory as a review diagnostic; version skew between the installed game and that inventory does not block a valid import;
- copies the reviewed source snapshot to `original-source/game/`;
- creates `original-source/SOURCE_MANIFEST.json` with SHA-256 hashes, archive/decompile provenance and source coverage;
- creates `original-source/SOURCE_COVERAGE.json` listing inventory paths that are absent from this installed build;
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

No Gemini/TTS request is made by the importer. The installed game is read-only throughout the process. Import completeness is gated on reconstructing every effective `.rpyc`/`.rpymc` script discovered in the installed package, not on matching the translation inventory, because those two sources can represent different game versions. The inventory coverage report remains useful for spotting version drift. The imported PR should remain unmerged until the reconstructed English source and coverage report have been reviewed and the voice extractor has been switched from translation-export recovery to direct original-source ingestion.

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
    # Optional Windows GUI:
    python -m pip install -r requirements-voice-gui.txt
}
```

Set the Gemini API key only in your local environment or GitHub secret storage. Do not commit it.

```powershell
$env:GEMINI_API_KEY = "<your-key>"
```

## PySide6 Windows Voice Studio

For normal Windows use, the PySide6 desktop app is the recommended frontend. It uses
the same backend, registry, rate limiter, retry logic, token ledger and approval files as
the terminal studio.

Install the GUI dependencies once:

```powershell
python -m pip install -r requirements-voice-gui.txt
```

Launch directly:

```powershell
python tools/voice_pipeline.py gui
```

Or use the Windows launcher, which checks PySide6 and securely asks for the Gemini key
when the current PowerShell process does not already contain one:

```powershell
pwsh -NoProfile -File tools/Start-VoiceStudio.ps1
```

The desktop app provides:

- searchable character list with Needs voice / Audition / Approved / Disabled / Alias filters;
- character profile, line counts, provider voice ID and editable Voice Design prompt;
- one-click Voice Design creation, provider-sample refresh, approval and rejection/retry;
- built-in Qt WAV playback for design samples and generated dialogue demos;
- representative dialogue demo generation in a background worker;
- shared persistent RPM/TPM limiting and TTS retry/backoff;
- exact provider token usage when returned by Gemini plus clearly marked estimates otherwise;
- local usage dashboard and recent-request table;
- rate/retry settings dialog persisted in ignored `voice/runtime.local.json`;
- resumable final generation for an approved voice;
- activity log and busy protection so overlapping API jobs cannot accidentally fight over quota.

The UI never stores the Gemini API key itself. It inherits `GEMINI_API_KEY` from the
launching process.
## Interactive Voice Studio

For normal casting and production work, prefer the interactive studio instead of calling
Voice Design and TTS commands manually:

\`\`\`powershell
python tools/voice_studio.py
\`\`\`

Open one character directly:

\`\`\`powershell
python tools/voice_studio.py --speaker mc
\`\`\`

The studio keeps the human approval step explicit and provides:

- character search/selection with line counts and current casting status;
- Voice Design creation from the exported request JSON;
- direct WAV playback of the provider design sample on Windows;
- representative, first-N, or explicit-ID dialogue demo generation;
- approve/reject/retry flows, including provider-side \`voices.delete\` before replacing a rejected voice;
- local archiving of rejected samples under \`voice/build/runtime/rejected/\`;
- persistent client-side rolling-window RPM limiting across script restarts;
- exponential retry/backoff for idempotent TTS/read operations;
- delayed retries for transient \`403 permission_denied\` TTS failures;
- provider token accounting from Interactions API usage metadata;
- a local JSONL usage ledger at \`voice/build/runtime/usage.jsonl\`;
- resumable final WAV generation for one approved voice identity or all approved voices;
- Ogg/Opus encoding through the existing pipeline encoder;
- custom-voice inventory so untracked/orphan provider voices are visible.

The default local runtime settings are deliberately conservative:

\`\`\`text
preview TTS RPM: 3
preview input TPM: 0 (disabled until you enter the real project limit)
final TTS RPM:   3
final input TPM: 0 (disabled until you enter the real project limit)
Voices API RPM:  3
max retries:     4
403 retry delay: 65 seconds
\`\`\`

Google's project/model limits remain authoritative and can change by usage tier. Gemini
limits are commonly expressed as RPM, input TPM and RPD. Check the active limits in Google
AI Studio, then adjust option **4. Client-side rate / retry settings** in the studio.
The optional TPM guard uses a conservative pre-request text-token estimate so it can throttle
before sending the request; exact provider token usage is recorded after successful responses. Local overrides are stored in ignored
\`voice/runtime.local.json\`; they are not committed.

The rate limiter writes recent request timestamps to
\`voice/build/runtime/rate_state.json\`. This prevents a script restart from immediately
forgetting the local rolling request window. Do not run multiple independent TTS
processes against the same project if you expect this single-process limiter to protect
the combined project quota.

For each successful Interactions TTS response the studio records, when supplied by the
provider:

- total input tokens;
- total output tokens;
- total tokens;
- text input tokens by modality;
- audio output tokens by modality;
- request latency, model, speaker and dialogue ID.

If provider usage metadata is absent, the studio records a clearly labeled local input
estimate rather than pretending it is exact.

Voice Design creation is intentionally not retried after ambiguous transient failures,
because repeating a non-idempotent create request could leave duplicate stored voices.
A rejected candidate can be retried explicitly through the character menu; the current
stored voice is deleted first, local samples are archived, approval is revoked if needed,
and a new candidate can then be created.

Approvals are written to \`voice/approvals.json\` and the character's
\`casting_status\` becomes \`approved\`. Final audio generation is blocked until the
canonical voice identity is approved.

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

## 3. Create and audition a character voice from the exported casting request

Recommended:

```powershell
python tools/voice_pipeline.py create-voice --speaker mc
```

This reads `voice/build/casting/requests/<speaker>.json`, refuses stale request data,
never overwrites an existing `voice_id`, stores the returned persistent provider ID in
`voice/characters.json`, and saves any returned audition sample under
`voice/previews/<speaker>.wav`. Local creation metadata is written beside the preview
and remains ignored by Git.

Before creating voices, regenerate the offline casting requests after any profile edit:

```powershell
python tools/voice_profiles.py validate
python tools/voice_profiles.py export
```

## 3b. Design and lock a character voice manually


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
