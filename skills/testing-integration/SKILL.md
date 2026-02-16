---
name: testing-integration
description: "Integration-boundary testing for component/service collaboration correctness. Use when modules interact through APIs, queues, databases, or adapters and boundary behavior must be verified before release; do not use for UX flow validation or pure unit isolation work."
---

# Testing Integration

## Trigger Boundary
- Use when the core need is integration boundary correctness.
- Typical requests:
  - `Repository層とDBの結合部を検証したい`
  - `service間API連携の失敗系を明示的にテストしたい`
  - `adapter差し替え時の境界契約を確認したい`
- Do not use when:
  - ブラウザ導線のE2E検証をしたい（`testing-e2e` / `playwright` を使う）
  - 単体関数だけを高速検証したい（`testing-unit` を使う）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for integration boundary correctness
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- integration boundary matrix with dependency strategy
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for integration boundary correctness.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using boundary-focused integration runs including timeout/error paths.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when critical seams are unverified for failure and timeout behavior.
- Escalate when shared dependency ownership prevents reliable integration fixtures.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
