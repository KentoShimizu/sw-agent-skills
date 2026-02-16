---
name: pytest-workflow
description: "Pytest verification workflow for Python code changes. Use when Python modules need executable pytest evidence (fixtures, parametrization, unit/integration behavior, regression checks) before merge; do not use for browser-level E2E or non-Python test tooling decisions."
---

# Pytest Workflow

## Trigger Boundary
- Use when the core need is pytest-based verification in Python.
- Typical requests:
  - `fixture設計を整理してpytestを安定化したい`
  - `parametrizeで境界ケースを重複なく増やしたい`
  - `遅いpytest群の実行戦略を見直したい`
- Do not use when:
  - JS/TSのJest運用（`jest-testing-workflow`）
  - ブラウザE2E導線の検証（`playwright`）

## Goal
Create fast, reliable, and debuggable pytest suites aligned with change risk.

## Inputs
- Change scope and affected Python modules
- Fixture graph and environment/data setup constraints
- CI/runtime constraints and marker policy

## Outputs
- pytest plan with fixture/marker/parametrization strategy
- Case matrix for happy/edge/failure paths
- Command set for local-fast and CI-full runs

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for pytest-based verification in Python.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using reproducible pytest commands for local and CI environments.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when fixtures produce non-deterministic or hidden shared state behavior.
- Escalate when runtime cost blocks practical feedback loops.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
