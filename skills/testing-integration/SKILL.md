---
name: testing-integration
description: "Integration-boundary testing for component and service collaboration correctness. Use when modules interact via APIs, queues, databases, or adapters and boundary behavior must be verified; do not use for full UI journey validation or pure unit isolation work."
---

# Testing Integration

## Overview
Use this skill to verify boundary behavior where independently correct units may still fail in combination.

## Scope Boundaries
- Use when correctness depends on integration seams.
- Typical requests:
  - `Validate repository-to-database behavior including failure paths.`
  - `Test timeout and retry handling between services.`
  - `Verify adapter replacement does not break boundary contracts.`
- Do not use when:
  - The goal is full browser journey validation (`testing-e2e`/`playwright`).
  - The goal is pure isolated unit checks (`testing-unit`).

## Inputs
- Integration seams and dependency topology
- Failure-mode expectations (timeout, retry, partial failure)
- Fixture/environment constraints

## Outputs
- Boundary test matrix with dependency strategy
- Decision record for integration depth and tooling choices
- Verification checklist for success and failure semantics

## Workflow
1. Enumerate high-risk seams and boundary contracts.
2. Define required behaviors for success, timeout, and error cases.
3. Compare fixture strategies and choose one with rationale.
4. Execute focused integration tests with reproducible setup.
5. Publish coverage gaps, residual risks, and ownership.

## Quality Gates
- Critical seams include failure-path coverage.
- Boundary expectations are explicit and deterministic.
- Evidence can be replayed in CI.
- Dependency assumptions are documented.

## Failure Handling
- Stop when critical boundaries lack failure-path tests.
- Escalate when dependency ownership blocks reliable fixtures.

## Bundled Resources
- `references/trigger-and-examples.md`: trigger patterns, anti-patterns, and deliverable expectations.
