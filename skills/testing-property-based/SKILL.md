---
name: testing-property-based
description: "Property-based testing workflow for invariant validation over wide input spaces. Use when correctness depends on rules that must hold for many generated/randomized inputs beyond hand-picked examples; do not use for narrow deterministic unit examples only."
---

# Testing Property Based

## Trigger Boundary
- Use when the core need is invariant validation with generated inputs.
- Typical requests:
  - `入力空間が広く、例ベースだけでは漏れが怖い`
  - `エンコード/デコードの恒等性を保証したい`
  - `集約ロジックの不変条件を乱択で検証したい`
- Do not use when:
  - 固定ケースのみで十分な小規模ロジック（`testing-unit` を使う）
  - UI導線検証（`testing-e2e` / `playwright` を使う）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for invariant validation with generated inputs
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- property specification and generator strategy
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for invariant validation with generated inputs.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using property runs with shrinking traces for failing cases.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when core invariants are undefined or repeatedly violated without diagnosis.
- Escalate when generator quality prevents meaningful domain coverage.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
