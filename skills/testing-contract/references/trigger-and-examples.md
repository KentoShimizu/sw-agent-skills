# Testing Contract Trigger And Examples

## Positive Trigger Signals
- Provider-consumer compatibility is a release risk.
- API or event schema changes need executable compatibility checks.
- CI must block merges on contract violations.

## Non-Matching Signals
- UI visual behavior validation only (`testing-e2e`/`playwright`).
- Isolated logic verification only (`testing-unit`).

## Example Requests That Should Trigger This Skill
- `Validate that this API change stays backward compatible.`
- `Add CI checks for provider and consumer contract verification.`
- `Prove event schema changes are safe for downstream consumers.`

## Minimal Deliverable Example
1. Compatibility policy and scope
2. Alternatives and migration trade-offs
3. Selected contract strategy
4. Provider/consumer execution evidence
5. Residual compatibility risks and owners
