# Token Versioning Policy

## Goal
Define when token changes are safe, when they are breaking, and how rollout decisions should be made.

## Change Classification
- Non-breaking changes:
  - Additive token creation without changing existing semantics.
  - Value tuning within approved tolerance that does not alter interaction meaning.
  - Metadata/documentation-only updates.
- Breaking changes:
  - Removing or renaming existing tokens in active use.
  - Repointing semantic tokens to values that change behavior intent.
  - State model changes that remove previously available states.

## Decision Criteria
- User risk: can the change alter clarity, action confidence, or completion rate?
- Engineering risk: can the change break consuming code or render paths?
- Rollout complexity: can this be phased, or does it require coordinated releases?
- Reversibility: can this be rolled back quickly without compounding drift?

## Deprecation Lifecycle
1. Announce replacement token and migration window.
2. Soft deprecate old token (no new usage).
3. Enforce cutoff in lint/review policy.
4. Remove token after migration completion evidence.

## Required Evidence Before Breaking Release
- Usage inventory of affected token IDs.
- Migration plan with owners and timeline.
- Visual regression and accessibility checks.
- Rollback strategy and owner confirmation.
