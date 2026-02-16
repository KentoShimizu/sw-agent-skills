---
name: testing-unit
description: "Deterministic unit-test strategy for isolated logic and fast feedback. Use when core logic branches, error paths, and edge conditions need low-latency regression evidence with controlled dependencies; do not use for browser-flow or cross-service compatibility validation."
---

# Testing Unit

## Trigger Boundary
- Use when the core need is isolated deterministic unit behavior.
- Typical requests:
  - `ドメインロジックの境界条件を高速に固めたい`
  - `例外系や分岐網羅をユニットで担保したい`
  - `依存を分離して原因局所化したい`
- Do not use when:
  - サービス間互換性確認（`testing-contract` / `testing-integration`）
  - UI導線の実ブラウザ検証（`testing-e2e` / `playwright`）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for isolated deterministic unit behavior
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- unit suite with isolation and fixture strategy
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for isolated deterministic unit behavior.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using fast deterministic runs covering happy/edge/failure branches.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when critical units lack deterministic tests for edge and failure paths.
- Escalate when dependency isolation is impossible without design changes.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
