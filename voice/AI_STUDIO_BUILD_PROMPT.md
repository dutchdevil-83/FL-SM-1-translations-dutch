# AI Studio Build Prompt: Ren'Py Voice Casting Studio

Paste the prompt below into **Google AI Studio > Build > Web app** after importing or connecting this repository/branch.

```text
Build a full-stack web application called "Ren'Py Voice Casting Studio".

PROJECT CONTEXT
This application manages English character voice production for a Ren'Py visual novel.
The repository also contains an unfinished Dutch translation, but Dutch is subtitle-only.
Never use Dutch translated text as TTS input.

SOURCE OF TRUTH
Use these existing repository files and preserve their schemas:
- voice/config.json
- voice/characters.json
- voice/line_overrides.json
- voice/build/dialogue_manifest.jsonl when supplied/generated
- voice/build/speaker_stats.json when supplied/generated
- tools/voice_pipeline.py

The spoken source text is the original embedded English dialogue extracted by the
repository pipeline. Do not independently translate, rewrite, or substitute the dialogue.

GEMINI MODELS
- Voice Design / persistent character personas: gemini-3.8-flash-tts
- Final-quality TTS: gemini-3.8-flash-tts
- Fast development previews: gemini-3.8-flash-lite-tts

FREE TIER
Assume Gemini Developer API Free Tier by default.
Use Standard requests only.
Do not require Billing, Batch API, Flex inference, Priority inference, Cloud Run,
or any other paid service.
Show quota/rate-limit errors clearly and allow safe retry/resume.
Never automatically synthesize the full game.

SECURITY
Use the GEMINI_API_KEY provided automatically by Google AI Studio as a server-side
secret. All Gemini and Voices API calls must execute server-side.
Never expose GEMINI_API_KEY in the browser, logs, generated JSON, download files,
localStorage, URL parameters, or source displayed to the user.

VOICE DESIGN
Use the Gemini Voices API to create persistent prompted Voice Design personas.
Each real game character should have one stable voice_... ID.
Permanent vocal identity belongs in Voice Design:
- age range
- gender presentation
- accent / English locale
- pitch and timbre
- vocal texture
- baseline cadence and energy
- stable personality impression

Temporary scene emotion must NOT be baked into the voice persona.
Use speech_metadata.style for line-specific acting such as:
- nervous
- angry but controlled
- whispered
- playful
- sad
- excited
- out of breath

When creating a designed voice:
- show the generated sample_audio
- show the resulting voice_... ID
- require explicit approval before assigning the ID to a character
- preserve the full design prompt with the character
- never replace an already-approved voice ID without explicit user action

CHARACTER REGISTRY
Read voice/characters.json.
Provide a Characters view containing:
- speaker token
- display name
- dialogue line count
- voice ID
- voice_ref
- language code
- design prompt
- baseline/default style
- enabled state
- casting status: unassigned / auditioning / approved

Respect voice_ref. For example, mct can reuse the mc voice identity while applying
a different baseline delivery style.

DIALOGUE
Import and parse voice/build/dialogue_manifest.jsonl.
Provide a Dialogue view with:
- Ren'Py voice ID
- speaker
- original English text
- cleaned TTS text
- scene/source file
- status
- review reasons
- source occurrences

Allow filtering by:
- speaker
- character
- scene/source file
- ready / needs_review
- voice assigned / unassigned
- generated / not generated
- approved / rejected

Never synthesize needs_review lines automatically.

AUDITION WORKFLOW
For each important character provide a Casting/Audition screen.

Allow the user to:
1. enter/edit a concise Voice Design prompt
2. generate a persistent prompted voice
3. listen to the returned voice sample
4. audition that voice on selected game dialogue
5. compare multiple candidate voices before approval
6. approve exactly one voice identity
7. save the chosen voice_... ID into the in-app character state

Include a useful audition set covering:
- neutral conversation
- intimate/quiet delivery
- anger/confrontation
- sadness
- humour
- excited/fast delivery

PREVIEW COMPARISON
For individual dialogue rows provide:
- Flash-Lite preview
- Flash final-quality preview
- playback controls
- regenerate button
- optional line-specific style field
- approve/reject take

Do not generate both versions automatically for thousands of lines.
Only generate when explicitly requested.

LINE OVERRIDES
Edit voice/line_overrides.json without changing its schema.
Allow per-line:
- tts_text override
- style
- skip=true

Clearly indicate whenever an override changes the spoken text from the extracted
original English dialogue.

FREE-TIER QUOTA SAFETY
Implement a request queue with:
- configurable concurrency, default 1
- rate limiting
- exponential backoff with jitter for HTTP 429
- retry-after support when supplied by the API
- pause/resume
- cancel queued requests
- persistent completed-state in the current app session
- no regeneration of an already completed asset unless Force is selected

Show counts:
- queued
- running
- successful
- skipped
- needs review
- failed due to quota/rate limit

Do not label Free Tier TTS generation as paid.

EXPORT
Provide validated downloads for:
- characters.json
- line_overrides.json

Keep both files schema-compatible with the existing repository pipeline.
Do not export GEMINI_API_KEY or temporary browser state.

REN'PY
Show the expected output naming convention:
voice/en/{renpy-id}.ogg

The application does not need to package the final Ren'Py game. It is a casting,
review, preview and configuration application. The existing Python repository pipeline
remains responsible for reproducible extraction, final bulk generation, encoding and
game integration.

UI
Create a clean desktop-oriented React UI with:
- Dashboard
- Characters
- Casting
- Dialogue
- Review Queue
- Generation Queue
- Settings

Dashboard should immediately show:
- total extracted dialogue lines
- ready lines
- needs-review lines
- number of speakers
- characters with approved voices
- characters still needing casting
- generation queue status

Use compact tables and side panels rather than huge cards.
Make audio auditioning fast: one click to play and obvious A/B comparison controls.

IMPLEMENTATION
Use the current Google GenAI JavaScript SDK.
Use a Node.js server-side runtime for Gemini calls.
Keep client-side code free of API credentials.
Validate imported JSON/JSONL before use.
Do not silently rewrite repository files.
Make the app functional in AI Studio preview before declaring the task complete.
```
