# Phase 2 batch 02 - System labels and lightweight UI

## Scope

This batch continues Phase 2 with low-level system strings, Ren'Py labels and a bounded set of lightweight navigation/UI screens. Large translation surfaces such as `common.rpy`, `code/hints.rpy` and `code/renpy/screens/screens.rpy` remain separate review batches.

- **Files:** 21
- **Source string/dialogue units:** 70
- **Source words (inventory estimate):** 241
- **Phase 2 total:** 58 files / 976 units / 3,850 words
- **Target locale:** Netherlands Dutch (`nl-NL`)
- **Ren'Py key/root used by this fork:** `dutch`

## Files

- `code/debug/storyline_config.rpy`
- `code/functions/functions.rpy`
- `code/functions/init.rpy`
- `code/functions/release_1.rpy`
- `code/renpy/config/options.rpy`
- `code/renpy/labels/actions.rpy`
- `code/renpy/labels/labels.rpy`
- `code/renpy/labels/vn_mode.rpy`
- `code/renpy/screens/interaction.rpy`
- `code/renpy/screens/language.rpy`
- `code/renpy/screens/map.rpy`
- `code/renpy/screens/money_statement.rpy`
- `code/renpy/screens/music_player.rpy`
- `code/renpy/screens/neutral_characters.rpy`
- `code/renpy/screens/sandbox.rpy`
- `code/renpy/screens/scifi_movie.rpy`
- `code/renpy/screens/studio_laptop.rpy`
- `code/renpy/screens/topics.rpy`
- `code/renpy/screens/ui.rpy`
- `code/renpy/screens/vn_mode.rpy`
- `code/renpy/screens/wait.rpy`

## Translation decisions

- Preserve `Mike`, `Young`, `Brown`, `Chase`, `SM` and `Fetish Locator: S&M Studio` as proper names/title values.
- Preserve `Bzzzzz` as a non-lexical sound effect while translating `*knock knock*` as `*klop klop*`.
- Use `Missie` / `Missies` for visible quest UI in this batch.
- Use `Tijdvak` for visible `Timeslot` labels.
- Use concise Dutch UI labels such as `Terug`, `Taal kiezen`, `Kaart openen` and `Laptop openen`.
- Keep the sexually suggestive shower reaction lines direct and idiomatic rather than sanitizing them.
- Preserve every Ren'Py token, interpolation and formatting tag exactly.

## Cumulative Phase 2 position after this batch

After generated tracking is refreshed, Phase 2 should contain:

- **39 files in `review`**
- **19 files still `not started`**
- **183 source units represented by Dutch files**
- **793 source units remaining**

The larger remaining files are intentionally isolated into later batches so language review remains practical instead of turning into an archaeological expedition through one enormous diff.

## Acceptance status

- Translation files complete for the batch: **implemented**
- Token/block/source parity: **CI required**
- Manifest status: **generated as `review` after successful implementation-branch validation**
- Dutch human language review: **pending**
- Compatible-build smoke test: **pending**
- Upstream submission: **not part of this batch**
