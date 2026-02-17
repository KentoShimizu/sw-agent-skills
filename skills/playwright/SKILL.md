---
name: playwright
description: "Playwright browser verification workflow for user-journey evidence with deterministic replay artifacts. Use when web flows require executable browser evidence (trace/screenshot/replay logs) before merge or release; do not use for pure unit/API-only checks."
---

# Playwright

## Overview
Use this skill to validate browser-level behavior with reproducible artifacts that engineers can replay exactly.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Trigger examples:
  - `references/trigger-and-examples.md`
- Replay determinism rules:
  - `references/replay-determinism-rules.md`

## Templates And Assets
- Test plan template:
  - `assets/playwright-test-plan-template.md`
- Command profile template:
  - `assets/playwright-command-profile-template.md`
- Artifact checklist:
  - `assets/playwright-artifact-checklist.md`

## Inputs To Gather
- Critical flows and acceptance expectations.
- Target browsers/devices and environment constraints.
- Auth/test-data setup and security constraints.
- Required artifacts for failure triage.

## Deliverables
- Browser test scenario plan.
- Local-fast and CI-full command profiles.
- Trace/screenshot/video evidence for failures.
- Residual flakiness and ownership log.

## Workflow
1. Define scenarios with `assets/playwright-test-plan-template.md`.
2. Define command profiles in `assets/playwright-command-profile-template.md`.
3. Apply deterministic execution rules from `references/replay-determinism-rules.md`.
4. Execute and capture artifacts.
5. Validate evidence completeness via `assets/playwright-artifact-checklist.md`.

## Quality Standard
- Browser evidence is replayable without hidden steps.
- Artifacts map to explicit scenarios and failures.
- Critical flows include happy/edge/failure coverage.

## Failure Conditions
- Stop when prerequisites for deterministic replay are missing.
- Stop when artifacts cannot reproduce observed failures.
- Escalate when external instability prevents reliable browser evidence.
