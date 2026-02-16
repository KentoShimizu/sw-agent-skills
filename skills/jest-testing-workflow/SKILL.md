---
name: jest-testing-workflow
description: "Jest verification workflow for JavaScript/TypeScript codebases. Use when JS/TS changes need executable Jest evidence (unit/integration behavior, mocks, async/timer control, regression checks) before merge; do not use for browser-level E2E or language-agnostic policy design."
---

# Jest Testing Workflow

## Trigger Boundary
- Use when the core need is Jest-based verification in JS/TS.
- Typical requests:
  - `Jestでモック境界を見直してテストを安定化したい`
  - `fake timers を使う async テストのフレークを潰したい`
  - `CI向けJest実行プロファイルを整理したい`
- Do not use when:
  - 実ブラウザの導線検証（`playwright`）
  - Pythonテスト設計（`pytest-workflow`）

## Goal
Deliver maintainable Jest suites with deterministic behavior and actionable failures.

## Inputs
- Change scope and affected JS/TS modules
- Runtime assumptions (node/jsdom) and mocking boundaries
- CI constraints for runtime and coverage gates

## Outputs
- Jest test plan with mock/timer/env strategy
- Assertion plan for happy/edge/failure paths
- Command set for local-fast and CI-full runs

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for Jest-based verification in JS/TS.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using reproducible jest command set with deterministic outcomes.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.

## Failure Handling
- Stop when mock strategy hides behavior that must be integration-visible.
- Escalate when async/timer flakiness persists after deterministic controls.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
