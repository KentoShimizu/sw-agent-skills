---
name: testing-contract
description: "Provider-consumer compatibility testing for service interface changes. Use when APIs/events evolve and executable contract checks must guard backward/forward compatibility before release; do not use for UI-only validation or architecture topology decisions."
---

# Testing Contract

## Trigger Boundary
- Use when the core need is provider-consumer contract compatibility.
- Typical requests:
  - `APIレスポンス変更で既存consumerが壊れないか検証したい`
  - `イベントスキーマ変更を契約テストで担保したい`
  - `providerとconsumerのCIで互換性ゲートを張りたい`
- Do not use when:
  - 画面の見た目検証だけをしたい（`testing-e2e` / `playwright` を使う）
  - 単体ロジックの網羅をしたい（`testing-unit` を使う）

## Goal
Build sufficient, risk-aligned verification evidence to prevent regressions.

## Inputs
- Change scope, risk profile, and release constraints
- Domain evidence for provider-consumer contract compatibility
- Existing test assets, toolchain constraints, and known failure modes

## Outputs
- versioned contract set and compatibility matrix
- Decision record including alternatives and selected strategy
- Verification checklist with measurable pass/fail criteria

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for provider-consumer contract compatibility.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using contract verification runs for both provider and consumer pipelines.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when contract mismatches violate required compatibility policy.
- Escalate when no migration path exists for breaking changes.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
