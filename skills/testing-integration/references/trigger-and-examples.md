# Testing Integration Trigger And Examples

## Positive Trigger Signals
- Boundary behavior between modules/services is uncertain.
- Timeout/retry/failure semantics across dependencies must be verified.
- Adapter or infrastructure changes may break seams.

## Non-Matching Signals
- Full browser journey validation (`testing-e2e`/`playwright`).
- Pure isolated unit logic checks (`testing-unit`).

## Example Requests That Should Trigger This Skill
- `Test repository and DB boundary behavior including failures.`
- `Verify service timeout and retry handling across integration seams.`
- `Validate adapter replacement with boundary tests.`

## Minimal Deliverable Example
1. Boundary matrix and constraints
2. Fixture alternatives and trade-offs
3. Selected integration strategy
4. Reproducible seam-level evidence
5. Residual boundary risks and owners
