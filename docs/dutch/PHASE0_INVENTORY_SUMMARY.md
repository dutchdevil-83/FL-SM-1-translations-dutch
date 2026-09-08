# Phase 0 Dutch translation inventory summary

- **Upstream baseline:** `cbb9016479fa95aca7c6ad58593fdf63093d7659`
- **Candidate `.rpy` files:** 444
- **Structural-variance files:** 126
- **Unassigned files:** 0
- **Production language roots used for union:** `chinese`, `deutsch`, `french`, `italian`, `magyar`, `portuguese`, `spanish`, `turkish`, `ukrainian`

## Inventory by implementation phase

| Phase | Files | Translation blocks | String/dialogue units | Source words (estimate) |
| --- | ---: | ---: | ---: | ---: |
| Phase 2 | 58 | 82 | 976 | 3850 |
| Phase 3 | 76 | 1582 | 2926 | 16480 |
| Phase 4 | 60 | 6989 | 7095 | 52317 |
| Phase 5 | 92 | 11281 | 11439 | 84864 |
| Phase 6 | 158 | 18775 | 19215 | 141003 |

## Language-contract status

| Decision | Proposed value | Status |
| --- | --- | --- |
| Ren'Py key | `dutch` | `confirmed` |
| Display name | `Nederlands` | `confirmed` |
| Locale variant | `nl-NL` | project target |
| Storefront metadata | `storepage_896318_dutch.json` | `pending_maintainer_confirmation` |

## Interpretation

The candidate set is the union of editable `.rpy` paths across the configured production language roots. Generated `.rpyc` files are not candidates.

Counts come from the available language copy that exposes the most embedded English source units for that path. `structure_variance=yes` means existing language trees disagree on block/unit counts and should receive extra attention during implementation; it does not remove the file from Dutch scope.

A newly committed Dutch target whose manifest status is still `not started` is automatically promoted to `review`. The validator must still pass, and human Dutch review/runtime smoke testing remain required before `done`.

Any `Unassigned` path is a Phase 0 failure and must be classified before Phase 0 can be closed.
