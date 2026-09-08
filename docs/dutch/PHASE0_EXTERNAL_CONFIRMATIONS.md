# Phase 0 external confirmations

The upstream SM-1 maintainer confirmations requested in Phase 0 are still pending. The fork owner has now explicitly authorized Phase 2 implementation to proceed in this fork using the proposed Dutch runtime contract. This authorization is intentionally narrower than upstream maintainer confirmation.

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

**Status:** Pending maintainer confirmation  
**Proposed scope:** Include Dutch storefront metadata  
**Proposed filename if confirmed:** `storepage_896318_dutch.json`

### Repository evidence

Production language trees such as German and Italian contain language-specific `storepage_896318_<language>.json` files alongside `common.rpy` and the `code/` tree. This strongly suggests storefront metadata is maintained through the translation repository, but it does not prove that a Dutch store page is enabled or consumed by the release process.

### Phase 2 rule

Phase 2 does not create Dutch storefront metadata. That work remains blocked until the upstream/storefront contract is confirmed.

### Confirmation still required before upstream submission

An SM-1 maintainer should explicitly confirm:

> For the SM-1 Dutch localization, should the Ren'Py translation identifier/root directory be `dutch`, and should the language be displayed to players as `Nederlands`?

and:

> Should the Dutch localization include Steam/storefront metadata in this repository, using `storepage_896318_dutch.json` or another expected identifier?

## Completion rule

The fork may continue implementing and validating Dutch `.rpy` files under the fork-owner authorization above. Phase 0 external confirmation is still not considered complete for upstream-submission purposes until the maintainer response is recorded here.
