---
name: testing-tdd
description: "Red-green-refactor workflow for test-first implementation feedback loops. Use when behavior and design must evolve safely through small increments backed by failing-then-passing tests; do not use for post-hoc test backfilling only."
---

# Testing Tdd

## Trigger Boundary
- Use when the core need is test-first red-green-refactor discipline.
- Typical requests:
  - `新機能をTDDで安全に進めたい`
  - `設計を小さく検証しながら進めたい`
  - `リファクタ時の回帰不安を最小化したい`
- Do not use when:
  - 実装後にまとめてテスト追加するだけの作業
  - 負荷試験や運用監視の設計

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for test-first red-green-refactor discipline
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- commit-level red-green-refactor evidence
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for test-first red-green-refactor discipline.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using trace of failing test -> minimal fix -> refactor with green suite.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when implementation proceeds without preceding failing tests.
- Escalate when cycle time is blocked by oversized steps or missing seams.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
