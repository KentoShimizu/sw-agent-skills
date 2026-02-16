---
name: playwright
description: "Playwright CLI workflow for browser-level user-journey verification. Use when web flows require executable browser evidence (traces, screenshots, reproducible command logs) before merge or release; do not use for pure unit/API-only checks."
---

# Playwright

## Trigger Boundary
- Use when the core need is browser-level flow verification with artifacts.
- Typical requests:
  - `主要ユーザーフローをブラウザ実行で再現証跡付きで確認したい`
  - `DOM更新後の要素参照ミスを防いでE2Eを安定させたい`
  - `失敗時にtrace/screenshot付きで報告したい`
- Do not use when:
  - API契約のみの検証（`testing-contract`）
  - 関数単位のロジック検証（`testing-unit`）

## Goal
Produce deterministic browser evidence for functional and UX flow validation.

## Inputs
- Target URLs and critical flow definition
- Credentials/fixtures from environment variables or secret store
- Artifact requirements (`trace`, `screenshot`, `video` if needed)

## Outputs
- Reproducible Playwright command sequence
- playwright execution package with artifacts and replay steps
- Findings list with exact replay references

## Workflow
1. Clarify decision question, existing project testing policy, and non-negotiable constraints for browser-level flow verification with artifacts.
2. Map risks to required test depth and execution tiers (fast gate vs full gate).
3. Design at least two viable strategies and compare feedback latency, maintenance cost, and flakiness risk.
4. Select one strategy and document why alternatives were not chosen.
5. Design happy-path, edge-path, and failure-path checks with explicit expected outcomes.
6. Execute verification and capture reproducible evidence using step-by-step browser run evidence with deterministic replay.
7. Publish residual risks, follow-up actions, and owner accountability.

## Quality Gates
- Trigger fit is explicit, and alternative testing levels were consciously considered.
- Decision rationale is evidence-based, not preference-based.
- Assumptions, unknowns, and confidence level are documented.
- Evidence is reproducible with exact commands/artifacts.
- Residual risks include owner, due date, and verification plan.
- Release gating criteria and rollback signals are explicit for production-impacting changes.

## Failure Handling
- Stop when automation prerequisites are missing or secure credential injection is unavailable.
- Escalate when external instability prevents deterministic replay despite retries.

## Bundled Resources
- `references/trigger-and-examples.md`: concrete trigger phrases, non-matching requests, and expected deliverable shape.
