---
name: testing-bdd
description: "Behavior-driven scenario design for shared business language and executable acceptance evidence. Use when teams must align requirements as Given-When-Then scenarios before implementation sign-off or release; do not use for performance/load benchmarking or deployment policy design."
---

# Testing Bdd

## Trigger Boundary
- Use when the core need is behavior scenarios in ubiquitous language.
- Typical requests:
  - `仕様レビュー前にGiven-When-Thenを整理したい`
  - `要件の解釈差分をテスト可能なシナリオに落としたい`
  - `PO/QA/開発で同じ受け入れ条件を共有したい`
- Do not use when:
  - 純粋な負荷試験設計のみをしたい（`performance-*` を使う）
  - 本番監視やアラート運用の設計をしたい（`observability-*` を使う）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for behavior scenarios in ubiquitous language
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- Given-When-Then scenario suite with requirement mapping
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for behavior scenarios in ubiquitous language.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using scenario execution evidence tied to acceptance decisions.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when critical business behavior cannot be expressed as executable scenarios.
- Escalate when stakeholders disagree on scenario semantics and release criteria.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
