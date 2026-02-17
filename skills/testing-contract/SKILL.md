---
name: testing-contract
description: "Provider-consumer compatibility testing for service interface changes. Use when APIs or event schemas evolve and executable contract checks must guard compatibility before release; do not use for UI-only validation or architecture topology decisions."
---

# Testing Contract

## Overview
Use this skill to prevent integration regressions by enforcing provider-consumer contracts in CI.

## Scope Boundaries
- Use when interface compatibility between producer and consumer is a release risk.
- Typical requests:
  - `Verify an API response change does not break existing consumers.`
  - `Enforce event schema compatibility in CI.`
  - `Add provider-consumer contract gates before merge.`
- Do not use when:
  - The scope is visual/UI behavior only (`testing-e2e` or `playwright`).
  - The scope is isolated unit logic (`testing-unit`).

## Inputs
- Contract definitions and compatibility policy
- Provider/consumer versioning constraints
- Release and rollback requirements

## Outputs
- Versioned contract suite and compatibility matrix
- Decision record for contract strategy and migration path
- Verification checklist for provider and consumer pipelines

## Workflow
1. Define compatibility policy (backward/forward/strict).
2. Identify contract surfaces and critical consumers.
3. Compare enforcement options and choose one with rationale.
4. Capture provider-consumer compatibility in `assets/contract-compatibility-matrix-template.md`.
5. Execute provider and consumer verification runs.
6. Publish failures, migration actions, and residual risk.

## Quality Gates
- Compatibility policy is explicit and test-enforced.
- Breaking changes include migration and communication plan.
- Contract evidence is reproducible in CI.
- Residual compatibility risk is owned and tracked.

## Failure Handling
- Stop when required compatibility policy is violated.
- Escalate when no feasible migration path exists.

## Bundled Resources
- `references/trigger-and-examples.md`: trigger patterns, anti-patterns, and deliverable expectations.
- `assets/contract-compatibility-matrix-template.md`: compatibility and migration tracking matrix.
