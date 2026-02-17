---
name: testing-mutation
description: "Mutation-testing workflow for exposing weak assertions and missing behavioral checks. Use when tests pass but confidence is low and objective robustness evidence is needed; do not use before baseline tests exist."
---

# Testing Mutation

## Overview
Use this skill to quantify test effectiveness and prioritize strengthening weak assertions.

## Scope Boundaries
- Use when pass-only test status is insufficient for confidence.
- Typical requests:
  - `Find weak tests that do not fail when behavior is changed.`
  - `Use surviving mutants to guide assertion hardening.`
  - `Quantify test robustness for critical modules.`
- Do not use when:
  - Baseline unit/integration coverage is missing.
  - The primary goal is load or capacity benchmarking (`performance-*`).

## Inputs
- Existing tests and module criticality
- Mutation tooling constraints and runtime budget
- Release risk tolerance

## Outputs
- Mutation report with surviving mutant triage
- Decision record for target score and remediation strategy
- Verification checklist for strengthened assertions

## Workflow
1. Select mutation scope by business risk and runtime budget.
2. Define acceptable mutation score and exception policy.
3. Run mutation analysis and triage surviving mutants.
4. Strengthen tests or implementation assertions based on triage.
5. Re-run and publish deltas, residual risk, and follow-up plan.

## Quality Gates
- Surviving mutants are triaged with explicit rationale.
- Critical-path mutants have remediation plan.
- Runtime cost is balanced with risk coverage.
- Evidence is reproducible and comparable over time.

## Failure Handling
- Stop when critical survivors remain without remediation owner.
- Escalate when mutation runtime cost blocks practical adoption.

## Bundled Resources
- `references/trigger-and-examples.md`: trigger patterns, anti-patterns, and deliverable expectations.
