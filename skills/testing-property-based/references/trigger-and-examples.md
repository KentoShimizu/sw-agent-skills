# Testing Property-Based Trigger And Examples

## Positive Trigger Signals
- Input space is too broad for example-only testing.
- Invariants must hold across randomized/generated inputs.
- Edge-case discovery requires generator-driven exploration.

## Non-Matching Signals
- Small deterministic logic with fixed examples is sufficient.
- UI journey verification is the primary goal.

## Example Requests That Should Trigger This Skill
- `Test encode/decode roundtrip invariants over random inputs.`
- `Validate aggregate invariants using generated datasets.`
- `Find edge cases beyond handwritten examples.`

## Minimal Deliverable Example
1. Invariants and constraints
2. Generator strategy alternatives
3. Selected property-testing strategy
4. Seeded execution evidence with shrunk failures
5. Residual unknowns and follow-up actions
