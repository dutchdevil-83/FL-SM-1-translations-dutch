# Phase 0 external confirmations

The upstream SM-1 maintainer confirmations requested in Phase 0 are still pending. The fork owner has explicitly authorized Phase 2 implementation in this fork using the proposed Dutch runtime contract and has now also explicitly instructed the project to include Dutch storefront metadata using `storepage_896318_dutch.json`. These authorizations are intentionally narrower than upstream maintainer confirmation.

## Decision 1 - Dutch Ren'Py language identifier and display name

**Fork implementation status:** Authorized by fork owner on 2026-09-08  
**Upstream maintainer status:** Pending confirmation  
**Runtime key used by this fork:** `dutch`  
**Displayed name used by this fork:** `Nederlands`  
**Language variant:** `nl-NL`

### Repository evidence

Existing translations use a language-specific root directory and the same language identifier in Ren'Py translation declarations, for example the German tree uses `deutsch/` and `translate deutsch ...` declarations. There is still no pre-existing Dutch root or repository-owned runtime registration file that independently proves the identifier expected by an upstream SM-1 build.

### Fork-owner authorization

After Phase 1 was approved and merged, the fork owner instructed the project to continue with the next implementation phase. For this fork, that instruction authorizes use of the proposed `dutch` root/key and `Nederlands` display name so real Dutch translation files can be implemented and validated rather than blocking all translation work on the external confirmation.

`phase0-config.json` therefore records the runtime key and display name as `confirmed` with `confirmation_scope: fork_implementation_only`, `confirmed_by: fork_owner`, and `upstream_maintainer_status: pending`.

This is not represented as upstream acceptance. If the SM-1 maintainers later require a different key or display registration, the Dutch tree and configuration must be reconciled before an upstream submission.

## Decision 2 - Dutch store-page metadata

**Fork implementation status:** Authorized by fork owner on 2026-09-08  
**Upstream maintainer status:** Pending confirmation  
**Scope:** Include Dutch storefront metadata  
**Filename:** `storepage_896318_dutch.json`  
**Repository location:** `dutch/storepage_896318_dutch.json`

### Repository evidence

Production language trees such as German, Italian, French, Spanish, Portuguese, Turkish and Chinese contain language-specific `storepage_896318_<language>.json` files alongside `common.rpy` and the `code/` tree. This establishes the repository structure used for localized storefront metadata. The upstream baseline includes, for example, `deutsch/storepage_896318_german.json`.

### Fork-owner authorization

The fork owner explicitly instructed the project on 2026-09-08 to include Dutch storefront metadata and to use `storepage_896318_dutch.json` as the filename. For this fork, that instruction confirms the proposed storefront scope and filename.

`phase0-config.json` therefore records storefront metadata as `confirmed` with `confirmation_scope: fork_implementation_only`, `confirmed_by: fork_owner`, and `upstream_maintainer_status: pending`.

The Dutch storefront file is implemented under the Dutch language root and uses Steam language identifier `dutch`, matching the filename and the fork's established runtime language key.

This still does not claim that the upstream SM-1 maintainers or Steam release process have accepted or enabled the Dutch storefront entry. If upstream later requires another identifier, filename or ingestion path, the file must be reconciled before upstream submission.

## Upstream confirmation still required before upstream submission

An SM-1 maintainer should still explicitly confirm:

> For the SM-1 Dutch localization, should the Ren'Py translation identifier/root directory be `dutch`, and should the language be displayed to players as `Nederlands`?

and:

> Is `dutch/storepage_896318_dutch.json` the expected Dutch Steam/storefront metadata file and is the `dutch` Steam language identifier enabled for the SM-1 release process?

## Completion rule

The fork may continue implementing and validating Dutch `.rpy` files and Dutch storefront metadata under the fork-owner authorizations above. Phase 0 external confirmation is still not considered complete for upstream-submission purposes until the maintainer response is recorded here.
