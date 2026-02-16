---
name: testing-regression-strategy
description: "Risk-based regression suite curation for release gating under limited time and budget. Use when you must decide which tests run always/conditionally based on impact and risk; do not use for writing a single test type in isolation."
---

# Testing Regression Strategy

## Trigger Boundary
- Use when the core need is regression suite selection by risk and impact.
- Typical requests:
  - `CI時間制約の中で回帰セットを最適化したい`
  - `毎回全部回せないので高リスク優先で選びたい`
  - `変更影響とテスト優先度を紐付けたい`
- Do not use when:
  - 単一テストケース実装のみ（`testing-unit` など個別skillを使う）
  - 監視設計そのもの（`observability-*` を使う）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for regression suite selection by risk and impact
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- regression policy with tiered test selection rules
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for regression suite selection by risk and impact.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using change-impact traceability between risks and selected suites.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.
- Release gating criteria and rollback signals are explicit for production-impacting changes.

## Failure Handling
- Stop when high-risk areas are missing from mandatory regression gates.
- Escalate when suite budget and required risk coverage are irreconcilable.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
