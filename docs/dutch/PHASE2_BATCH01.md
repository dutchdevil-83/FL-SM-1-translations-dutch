# Phase 2 batch 01 - Core class and system strings

## Scope

This batch starts Phase 2 with the complete set of currently inventoried `code/classes/*.rpy` translation files.

- **Files:** 18
- **Source string/dialogue units:** 113
- **Source words (inventory estimate):** 438
- **Phase 2 total:** 58 files / 976 units / 3,850 words
- **Target locale:** Netherlands Dutch (`nl-NL`)
- **Ren'Py key/root used by this fork:** `dutch`

## Files

- `code/classes/character.rpy`
- `code/classes/chat_controller.rpy`
- `code/classes/gallery.rpy`
- `code/classes/gametime.rpy`
- `code/classes/interaction_character_option.rpy`
- `code/classes/interaction_location_option.rpy`
- `code/classes/interaction_object_option.rpy`
- `code/classes/it_controller.rpy`
- `code/classes/location_controller.rpy`
- `code/classes/lovense.rpy`
- `code/classes/map_location.rpy`
- `code/classes/movie_controllers.rpy`
- `code/classes/player.rpy`
- `code/classes/player_controller.rpy`
- `code/classes/quest_controller.rpy`
- `code/classes/renovation_controller.rpy`
- `code/classes/th_controller.rpy`
- `code/classes/vn_mode_controller.rpy`

## Translation rules used

- Preserve source `old` strings, block structure and Ren'Py tokens exactly.
- Use contemporary Netherlands Dutch rather than literal English syntax.
- Preserve character names and established proper names.
- Preserve token-only strings when there is no lexical content to translate.
- Use glossary-backed terminology for recurring gameplay/UI concepts.
- Do not create or commit `.rpyc` files.

## Tracking behavior

The inventory generator now promotes a newly committed Dutch target file from `not started` to `review` when no explicit manual status exists. It does not mark files `done` automatically.

This is intentional: a complete file can pass structural automation while still requiring Dutch-language review and an applicable in-game smoke test.

## Runtime-contract scope

The fork owner authorized Phase 2 implementation to continue using the proposed `dutch` root/key and `Nederlands` player-facing language name. The config records this as `fork_implementation_only`; upstream maintainer confirmation remains pending.

Storefront metadata is not included in this batch and remains blocked on the separate maintainer/storefront confirmation.

## Acceptance status

- Translation files complete for the batch: **implemented**
- Token/block/source parity: **CI required**
- Manifest status: **generated as `review` after successful implementation-branch validation**
- Dutch human language review: **pending**
- Compatible-build smoke test: **pending**
- Upstream submission: **not part of this batch**
