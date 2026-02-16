---
name: testing-mutation
description: "Mutation-testing workflow for exposing weak assertions and missing behavioral checks. Use when existing tests pass but confidence is low and you need objective robustness signals; do not use for first-pass test creation before baseline tests exist."
---

# Testing Mutation

## Trigger Boundary
- Use when the core need is mutation score and weak assertion detection.
- Typical requests:
  - `テストは通るが壊しても落ちない不安がある`
  - `生存mutantを起点にアサーション強化したい`
  - `重要モジュールのテスト有効性を定量評価したい`
- Do not use when:
  - まだ基礎テストがない段階で初回設計したい（先に `testing-unit`/`testing-integration`）
  - パフォーマンス限界を測りたい（`performance-*` を使う）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for mutation score and weak assertion detection
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- mutation report with surviving mutant triage
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for mutation score and weak assertion detection.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using kill-rate evidence plus patch plan for surviving mutants.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when surviving mutants in critical logic remain without remediation plan.
- Escalate when mutation runtime cost blocks practical CI usage.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
