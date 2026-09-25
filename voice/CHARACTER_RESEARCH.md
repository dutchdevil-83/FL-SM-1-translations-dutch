# English voice character research and casting pack

Research checkpoint: 2026-09-25. Base branch: `voice/english-gemini-tts`.
English source snapshot: `4a396a365c89df4f5f543233d393ae2a2d55858c`.

## What is ready

`characters.json` contains all 58 nonempty speaker tokens in the current English
manifest. It preserves the version-1 fields consumed by `voice_pipeline.py`, and
adds explicitly labelled character/casting metadata. No voice has been created,
approved or assigned a fabricated provider ID.

The offline exporter produces **58 individual character profile files** and **50
Gemini Voice Design request files**. Two tokens reuse the protagonist's identity;
six remain disabled because their identity or performer binding needs confirmation.
The complete manifest also contains 474 rows without a resolved speaker token.
Those include literal-name speakers, narration and groups; they are not silently
assigned one generic character voice.

## Sources and certainty

The source catalog is `character_sources.json`. Research combines the original
English comments in this repository with the developer's stores/announcements and
official translation repositories for S&M Studio, Fetish Locator Week 1, and Taboo
University Book 1. It is not an exhaustive audit of every dialogue in all three games.
Public character pages do not establish an exact age for most of this cast.

`profile.canonical_age_years` is null unless supported explicitly. `casting_age`,
`pitch`, `timbre`, `cadence` and most accents are proposed direction for an audition,
not canonical biographical facts. Top-level `gender` means proposed vocal presentation;
`profile.canonical_gender` is separate and can remain unknown. A neutral proposal
must not be interpreted as a claim that a character is nonbinary.

Each entry has dialogue evidence IDs. Export resolves them to exact source file/line
URLs pinned to the recorded commit. Source-name lists help identify characters, but
initials, identical names or adjacency in a translation list are not enough to prove
a cross-game identity. Some secondary display-name expansions are working roster
labels and still merit checking against the game's Character definitions.

## Important results

- Nari identifies herself as 21 and from South Korea in `sm1cs_ns003_7a455ae2`.
  The suggested light Korean English accent is a casting proposal, not an explicit
  statement about how her voice sounds.
- Denise identifies her accent as Dutch in `sm1fs_t003_74958724`. Her transcript and
  TTS language remain English.
- `mct` uses the protagonist's voice with reflective delivery. `mo` is the opening,
  pre-name protagonist token and also refers to `mc`.
- `mhmes` is used for Commander Vel Spectre. The exact runtime performer selection
  must be confirmed in the full game. Lyssa/Min are candidate bindings, not a reason
  to blend both identities or to generate one actor for every branch.
- Melony uses Young and Chase in different paths. Her surname and relationship to
  the protagonist should not be forced to one route's version.
- `ms` is Maya; `my` is Melony. `bg` is Amore; `arj` is AmRose. `doc` is a police
  character, not a doctor. `sb` is Sam Bruce, who prefers Bruce.
- Hana identifies herself as Hana Rivera, Channel Six News. Carmel Blaise and Ethan
  Foxmorr are named in the confrontation scene; they are not interchangeable voices.

## Cross-game handling

Official developer material and the Week 1 name roster support returning identities
such as Stacy, Min, AmRose, Lyssa, Daisy and Hana. Their S&M performance can reflect
later experiences without inventing exact elapsed ages.

The official Taboo University roster includes Zemfira, Eliina, Ridley, Stacy, Daisy,
Lyssa and Nari. Zemfira is explicitly greeted as the Taboo University character in
S&M's post-credits scene. Named TU investigation notes confirm Winner's Club membership
and a past friendship with Brigitta. Adjacent anonymous leadership notes have not
been assigned to her. Her poised, alert delivery remains a casting proposal, not a
canonical voice or age.

Do not treat the promotional post-credits scene as ordinary story chronology. The
developer positions Taboo University before the Fetish Locator trilogy, while S&M
follows it. Shared `mc` tokens do not establish the same protagonist across games.
Ridley's name appears in both projects, but that alone does not prove identity.

## Identity review queue

| Token | Required check |
|---|---|
| `mhmes` | Resolve the selected movie performer using real game state/Character definitions. |
| `sbf` | Determine the actual speaker per post-credits line; Samiya is a candidate, not proof for every row. |
| `ef` | Verify whether this presenter is Eliina using full game definitions. |
| `ed` | Verify the interrupted-scene speaker; Elizabeth is only a candidate. |
| `ic` | Confirm that the shop speaker token binds to Inga. |
| `zh` | Confirm that the photography participant binds to Zuzana. |

Their records are present, but automatic creation-request export is blocked. This
prevents provisional names from becoming permanent mismatched voice identities.

## Use the files

After the existing extraction step has created `voice/build/dialogue_manifest.jsonl`:

```powershell
python tools/voice_profiles.py validate
python tools/voice_profiles.py export
```

Output:

```text
voice/build/casting/
  profiles/                 # One researched file per speaker token
  requests/                 # One API request per eligible voice identity
  summary.json
  unresolved_dialogue.json  # IDs and source locations, no copied dialogue
```

These commands are standard-library-only and offline. They do not need a key, change
translation files, create voices, or send any dialogue to a provider. Regeneration
replaces only generated JSON under this casting output directory.

Import `characters.json`, `character_sources.json` and the profile exports into the
casting UI. Start with the major cast, review the proposed age/accent/presentation,
then create and audition a candidate voice. Use `MODEL_INPUTS.md` for the exact API
field mapping. Request JSON is suitable for `client.voices.create(**request)`; this
is a separate explicit quota-consuming operation, not part of the exporter.

The existing `voice_pipeline.py design-voice` command still requires an explicit
`--prompt`; pass `--gender` explicitly to retain the proposed vocal presentation.
It does not automatically read all the new profile metadata. Use the exported
request to avoid omitting a casting field, or copy the registry values into those
explicit arguments. Never replace an approved voice without a deliberate audition.

Keep each approved `voice_...` ID on its real character only, and leave aliases using
`voice_ref`. Resolve identity-blocked and untokenized rows before claiming complete
game voice coverage. Do not begin a whole-game render before listening to the cast.
