---
name: git-bisect-debugging
description: "Locate regression-introducing commits using git bisect with deterministic classification. Use when a reproducible regression exists but the introducing commit is unknown; do not use for CI workflow design or application behavior implementation."
---

# Git Bisect Debugging

## Overview
Use this skill to isolate first-bad commits quickly and reproducibly, so fixes target root cause instead of symptoms.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Determinism guidance:
  - `references/bisect-determinism-guidance.md`

## Templates And Assets
- Session log template:
  - `assets/bisect-session-log-template.md`
- Verification checklist:
  - `assets/bisect-checklist.md`

## Inputs To Gather
- Known good commit and known bad commit.
- Deterministic pass/fail command for classification.
- Environment requirements for reproducible execution.
- Evidence expectations for culprit validation.

## Deliverables
- Culprit commit candidate with evidence trail.
- Bisect session log with classified steps.
- Confidence statement and next action recommendation.

## Workflow
1. Validate good/bad endpoints and deterministic classifier command.
2. Run bisect and classify commits consistently.
3. Capture classifications in `assets/bisect-session-log-template.md`.
4. Re-validate candidate culprit around boundary commits.
5. Close with `assets/bisect-checklist.md` and next-step recommendation.

## Quality Standard
- Good/bad endpoints are verified before bisect begins.
- Classification is deterministic and repeatable.
- Culprit claim is supported by reproducible evidence.
- Session records are sufficient for peer audit.

## Failure Conditions
- Stop when classification is flaky or environment-dependent.
- Stop when no reliable good/bad endpoints can be identified.
- Escalate when interacting commits prevent single-commit isolation.
