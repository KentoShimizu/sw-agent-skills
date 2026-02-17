---
name: testing-property-based
description: "Property-based testing workflow for invariant validation over broad input spaces. Use when correctness depends on rules that must hold across many generated inputs; do not use for narrow deterministic examples only."
---

# Testing Property-Based

## Overview
Use this skill to validate invariants beyond hand-picked test cases by combining generators, shrinking, and reproducible seeds.

## Scope Boundaries
- Use when input space is large and example-based tests are insufficient.
- Typical requests:
  - `Verify encode/decode roundtrip invariants for arbitrary inputs.`
  - `Stress aggregate invariants with generated data.`
  - `Catch edge cases that fixed examples miss.`
- Do not use when:
  - A small deterministic unit test set is sufficient (`testing-unit`).
  - The primary scope is UI journey validation (`testing-e2e`).

## Inputs
- Invariants and domain constraints
- Generator strategy and seed reproducibility requirements
- Runtime budget and flaky-risk tolerance

## Outputs
- Property definitions and generator coverage strategy
- Decision record for shrinking and seed policy
- Verification checklist with failing-case reproduction guidance

## Workflow
1. Formalize invariants and invalid-state assumptions.
2. Design generators that reflect realistic and adversarial inputs.
3. Compare generation/shrinking strategies and choose one.
4. Run property tests with reproducible seeds.
5. Triages failures with shrunk counterexamples and publish fixes.

## Quality Gates
- Core invariants are explicit and testable.
- Generators cover edge and adversarial shapes.
- Failures are reproducible via seed and shrunk case.
- Residual unknowns are documented.

## Failure Handling
- Stop when invariants are undefined or contradictory.
- Escalate when generator quality is too weak for meaningful coverage.

## Bundled Resources
- `references/trigger-and-examples.md`: trigger patterns, anti-patterns, and deliverable expectations.
