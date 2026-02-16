---
name: testing-e2e
description: "End-to-end test planning for critical user journeys across integrated systems. Use when release confidence depends on browser/API/dependency behavior as one flow; do not use for isolated unit behavior or pure contract compatibility checks."
---

# Testing E2e

## Trigger Boundary
- Use when the core need is full-stack user journey integrity.
- Typical requests:
  - `購入フロー全体を本番相当で検証したい`
  - `UIから外部連携まで通した回帰を最小セットで定義したい`
  - `リリース前に致命的導線だけE2Eで担保したい`
- Do not use when:
  - 単体関数の正しさを確認したい（`testing-unit` を使う）
  - 契約互換性だけ見たい（`testing-contract` を使う）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for full-stack user journey integrity
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- critical journey e2e pack with environment assumptions
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for full-stack user journey integrity.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using production-like journey runs with reproducible artifacts.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.
- Release gating criteria and rollback signals are explicit for production-impacting changes.

## Failure Handling
- Stop when critical journeys fail or remain untested in integrated conditions.
- Escalate when environment instability prevents deterministic replay.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
