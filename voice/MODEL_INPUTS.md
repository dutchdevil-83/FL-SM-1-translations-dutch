# Character inputs and the Gemini API

Checked 2026-09-25 against Google's Voice Design guide, Voices API reference and
OpenAPI schemas, catalogued in `character_sources.json`. This contract covers the
prompted-voice, single-speaker workflow used here. It does not mix unrelated
replication, speech-recognition or generic agent options into character casting.

## Persistent identity: CreateVoice

`tools/voice_profiles.py export` writes one request JSON per eligible identity.
The object can be passed to Python `client.voices.create(**request)` when explicitly
creating a voice. Merely validating/exporting these files makes no API calls.

The request includes all documented writable Voice fields relevant to a prompted
voice, plus the required storage choice:

| Field | Source in this pack |
|---|---|
| `store` | `true`, required by Google for prompted voices |
| `voice.model` | `gemini-3.8-flash-tts`; export can select Flash-Lite |
| `voice.type` | `prompted`, not cloned/replicated audio |
| `voice.display_name` | Registry display name |
| `voice.gender` | Proposed perceived voice presentation: female, male, neutral |
| `voice.language_code` | English locale, currently `en-US` |
| `voice.prompted.input` | Concise permanent-persona description |
| `voice.accent` | American, Dutch or South Korean casting label |
| `voice.region_code` | US, NL or KR accent-discovery region, not citizenship |
| `voice.context` | Conversational |
| `voice.description` | The designed-persona summary |
| `voice.persona` | Proposed characteristic cadence/delivery |
| `voice.pitch` | Documented classification: low, medium or high |

`accent`, `region_code`, `context`, `description`, `persona` and `pitch` are supported
Voice discovery metadata. They are not independently calibrated acoustic controls.
The design prompt also describes the intended identity; do not rely on a metadata
label alone to produce it. A local medium-low or medium-high pitch maps to the
coarse medium classification while the detailed range stays in the prompt. The
exporter rejects an unmapped new accent rather than silently changing it to American.

Exact canonical age, approximate casting age, timbre, texture and cadence are
separate local profile fields. The appropriate casting descriptors go into
`prompted.input`, not invented numeric API properties. A casting age is not a claim
about the character's age in the story, and perceived vocal presentation is not
proof of gender identity. `profile.canonical_gender` remains separately recorded.

Do not send output-only `id`, `key`, `expire_time`, `usage` or `sample_audio` as creation
inputs. The provider returns the real identifier and sample. `replicated` is an
alternative input for a different voice type and is deliberately absent here.
Reference recordings and consent recordings are not required for original prompted
fictional personas. No celebrity/actor imitation is requested.

## Individual performance: Interactions TTS

The existing generator's separate synthesis path is structured as follows:

```json
{
  "model": "gemini-3.8-flash-tts",
  "input": [{
    "type": "user_input",
    "content": [{
      "type": "text",
      "text": "The original English dialogue goes here.",
      "annotations": [{
        "type": "speech_metadata",
        "style": "quiet and restrained"
      }]
    }]
  }],
  "generation_config": {
    "speech_config": [{"voice": "REPLACE_WITH_APPROVED_PROVIDER_ID"}]
  },
  "response_format": {
    "type": "audio",
    "mime_type": "audio/wav",
    "sample_rate": 24000
  }
}
```

This is a structural example, not a ready-to-send request: replace both transcript
and voice ID. `speech_metadata.style` controls temporary acting direction. The
optional `speaker` metadata field labels turns; it does not replace a stored voice
identity. For custom voices, synthesize each speaker turn separately. The documented
audio response controls are `type`, `mime_type` and `sample_rate`. WAV at 24 kHz is
this project's configured choice, not a claim of a live audio test in this change.

Do not add other providers' `stability`, `similarity_boost`, numeric age or numeric
pitch controls. Existing neutral/quiet/angry/sad/amused/urgent/internal delivery
presets are original direction text, not separate API fields. Transcript-level
vocal tags are performance choices, not permanent character biography.

## Listing and storage

ListVoices uses array-valued filters for accent, context, gender, language_code,
region_code, persona, pitch and type; it also accepts search, page_size and page_token.
Some SDK spellings differ, such as `contexts` or `type_`. These listing parameters
are not the scalar fields used inside a creation request.

Keep an approved provider ID unchanged. Save the returned sample and creation/expiry
information: current documentation gives stored custom voices a one-year lifetime.
Reusing a text prompt after expiration is not guaranteed to reconstruct an identical
voice. The local files document a casting proposal, not an archival voice model.

Dutch subtitles never become TTS input. Denise's Dutch accent still means English
speech. Nari's proposed light Korean English accent is supported by her stated origin,
but the precise strength is a casting decision rather than an explicit canon fact.
