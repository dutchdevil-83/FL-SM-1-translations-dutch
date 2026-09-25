# Google AI Studio setup for the Ren'Py English voice project

This project uses Google AI Studio and the Gemini Developer API as a character-voice production backend for the English dialogue in the game. Dutch remains the subtitle/localization layer.

## Recommended architecture

Use one dedicated Google AI Studio project for all game voices.

```text
Google AI Studio project
  |
  +-- one Gemini API key
  |
  +-- Voice Design
  |     +-- mc  -> voice_...
  |     +-- arj -> voice_...
  |     +-- ...
  |
  +-- Gemini 3.8 Flash-Lite TTS -> development previews
  |
  +-- Gemini 3.8 Flash TTS      -> approved/final renders
        |
        v
Ren'Py voice/en/{dialogue-id}.ogg

Subtitle language is independent and can be Dutch.
```

Do not create a separate Google AI Studio project for every character. Stored custom voices are project-scoped, and the same project/API key should be used by the local generator.

## 1. Create or select a dedicated Free Tier project

Open Google AI Studio:

https://aistudio.google.com/

Create or select a project dedicated to this game, for example:

```text
FL-SM-English-Voices
```

Keep the project on the **Free Tier** unless you deliberately decide to enable billing later.

Current Google pricing lists Standard input and audio output for both of the TTS models used here as **Free of charge on the Free Tier**:

- `gemini-3.8-flash-tts`
- `gemini-3.8-flash-lite-tts`

The calls still consume the project's Free Tier quota.

This project intentionally uses Standard interactive requests. Google's pricing page currently lists Batch and Flex as unavailable on the Free Tier for these TTS models.

## 2. Create the API key

In Google AI Studio, open the API Keys page and create a key for the same project.

New AI Studio users normally receive a project and API key automatically, but using a dedicated project makes it much easier to keep voice IDs, usage and quota together.

On Windows PowerShell, expose the key only to the current process:

```powershell
$env:GEMINI_API_KEY = "<your-api-key>"
```

Do not add the key to `voice/config.json`, `characters.json`, source control, screenshots or issue reports.

Gemini API rate limits are applied per project, not per API key. Creating extra keys for the same project does not create extra quota.

## 3. Open the AI Studio Voice Design studio

Google's Voice Design documentation links directly to:

https://aistudio.google.com/generate-speech

Use **Voice Design** to create and audition each main character.

For the final identity, use:

```text
Model: gemini-3.8-flash-tts
Type: prompted / designed voice
Language: en-US (unless a specific character needs another English locale)
Storage: persistent / stored voice
```

A stored designed voice returns a reusable identifier:

```text
voice_...
```

Copy that ID into the matching entry in `voice/characters.json`.

## 4. Design voices for identity, not scene emotion

Put stable character properties in Voice Design:

```text
age range
gender presentation
regional accent
pitch/timbre
vocal texture
baseline energy
baseline speaking cadence
personality impression
```

Keep the prompt concise. Google's current guidance recommends a clear one- or two-sentence description rather than a giant contradictory character biography.

Example:

```text
A woman in her mid twenties with a warm but guarded American voice,
intelligent and emotionally expressive, with a natural conversational cadence.
```

Do not bake temporary scene emotion into the permanent voice. Per-line emotion belongs in `speech_metadata.style`, which this pipeline exposes through `line_overrides.json`.

## 5. Audition before locking a voice

For every important character, audition several lines that cover different situations:

```text
neutral conversation
quiet/intimate speech
anger or confrontation
sadness
humour
fast/excited delivery
whispering or restrained delivery
```

Once a character voice is accepted, keep the same `voice_...` ID throughout the game.

The current repository discovers 58 speaker IDs, which fits inside Google's current project limit of 200 stored stateful voices.

Google currently gives stored stateful custom voices a one-year TTL. Keep the Voice Design prompt and voice ID in the repository so a voice can be recreated deliberately if it eventually expires.

## 6. Connect the repository pipeline

Set up the Python environment:

```powershell
& {
    Set-Location "<repo-root>"
    py -m venv .venv-voice
    .\.venv-voice\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements-voice.txt
}
```

Extract the English dialogue and populate the speaker registry:

```powershell
python tools/voice_pipeline.py extract
python tools/voice_pipeline.py init-characters
```

Then either:

1. design voices in AI Studio and paste their `voice_...` IDs into `voice/characters.json`, or
2. use the repository's `design-voice` command, which calls the same Gemini Voices API.

Example:

```powershell
python tools/voice_pipeline.py design-voice --speaker arj --display-name "AmRose" --gender female --language-code en-US --prompt "A woman in her mid twenties with a warm but guarded American voice, intelligent and emotionally expressive, with a natural conversational cadence."
```

## 7. Generate development previews

Use Flash-Lite for fast bulk experimentation:

```powershell
python tools/voice_pipeline.py synthesize --mode preview --speaker arj --limit 20
```

The command skips files that already exist, so rerunning after a quota/rate-limit interruption does not regenerate completed lines unless `--force` is supplied.

For a project with tens of thousands of lines, generate controlled batches by character or scene rather than firing the entire game at the API in one heroic act of optimism.

## 8. Generate approved final audio

After character voices are locked:

```powershell
python tools/voice_pipeline.py synthesize --mode final
python tools/voice_pipeline.py encode
```

The final model is:

```text
gemini-3.8-flash-tts
```

and the Ren'Py-ready files are written as:

```text
voice/generated/ogg/<renpy-id>.ogg
```

## Why this matches Ren'Py well

Google's current TTS guidance says custom designed voices should be synthesized per speaker turn rather than combined as custom multi-speaker voices in one request.

That maps directly to Ren'Py because each dialogue statement already has a stable translation/voice ID, and `config.auto_voice` resolves that ID to one audio asset.

## Free Tier notes

As of September 2026:

- Standard Gemini 3.8 Flash TTS input and audio output are free of charge on the Free Tier.
- Standard Gemini 3.8 Flash-Lite TTS input and audio output are free of charge on the Free Tier.
- Usage is still restricted by the project's active rate limits.
- Rate limits are per project.
- Free Tier request content may be used by Google to improve its products.
- Enabling billing moves the project to a paid usage tier, where paid pricing can apply.
- Batch/Flex TTS pricing is not available on the Free Tier, so this project does not depend on them.

View current usage and active limits in Google AI Studio under the project dashboard/usage and rate-limit views.

## Optional: AI Studio Build-mode management app

You do **not** need AI Studio Build mode to generate the game voices. The Voice Design studio plus this repository is the simpler and safer production path.

If you want a browser dashboard for casting/review, Build mode can create a separate full-stack app. Google AI Studio now keeps `GEMINI_API_KEY` as a server-side secret for Build-mode apps rather than exposing it to browser code.

Keep such a dashboard separate from the Ren'Py source tree. Its useful responsibilities would be:

```text
load dialogue_manifest.jsonl
load/save characters.json
filter by speaker/scene/review status
design and audition voices
store voice_... IDs
preview individual lines
compare Flash-Lite and Flash output
approve/reject takes
export the updated characters.json and line_overrides.json
show quota/rate-limit errors without losing progress
```

A suitable initial Build-mode prompt is:

```text
Build a full-stack web application called "Ren'Py Voice Casting Studio".

Purpose:
Manage English character voice production for a Ren'Py visual novel. Dutch is
subtitle-only and must not be used as TTS input.

Requirements:
- Use Gemini 3.8 Flash TTS for Voice Design and approved/final previews.
- Use Gemini 3.8 Flash-Lite TTS for fast development previews.
- Use the Gemini Voices API to create persistent prompted voice personas.
- Keep GEMINI_API_KEY server-side only.
- Never put the API key in client code or exported JSON.
- Import dialogue_manifest.jsonl, characters.json and line_overrides.json.
- Show characters, speaker IDs, line counts and assigned voice_... IDs.
- Allow designing, auditioning and approving one persistent voice per character.
- Keep permanent vocal identity separate from per-line speech_metadata.style.
- Allow filtering dialogue by speaker, scene and needs_review status.
- Preview one dialogue line at a time and allow Flash-Lite/Flash comparison.
- Export updated characters.json and line_overrides.json without changing their schema.
- Treat Gemini Developer API Free Tier as the default.
- Use Standard API requests only; do not require Batch, Flex or paid billing.
- Handle HTTP 429 rate limits gracefully and never lose already approved work.
- Do not automatically synthesize the entire game.
- Use a server-side Node.js backend and a clean React UI.
```

This optional app is a review/casting interface. The repository pipeline remains the source of truth for extraction, reproducible generation and Ren'Py integration.
