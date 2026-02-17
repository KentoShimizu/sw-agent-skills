---
name: git-commit-hygiene
description: "Enforce atomic commits, clear commit messages, and auditable change intent before push or review. Use when commit granularity, message clarity, and traceability must be improved; do not use for CI workflow design or application behavior implementation."
---

# Git Commit Hygiene

## Overview
Use this skill to create commit history that reviewers can reason about and operators can bisect safely.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Commit message quality rules:
  - `references/commit-message-quality-rules.md`

## Templates And Assets
- Commit slicing checklist:
  - `assets/commit-slicing-checklist.md`
- Commit message template:
  - `assets/commit-message-template.txt`

## Inputs To Gather
- Changed files and logical change boundaries.
- Team commit message conventions and compliance constraints.
- Risk profile of the change set (critical path vs local refactor).
- Required verification scope before push.

## Deliverables
- Logical commit slicing plan.
- Commit messages with explicit intent/rationale.
- Verification notes per commit (tests/checks run).
- Traceability-ready history for review and rollback.

## Workflow
1. Separate unrelated changes using `assets/commit-slicing-checklist.md`.
2. Write commit messages from `assets/commit-message-template.txt` and `references/commit-message-quality-rules.md`.
3. Ensure each commit is independently reviewable and reversible.
4. Run required tests/checks before push.
5. Re-check history for mixed intent, hidden generated noise, and sensitive content.

## Quality Standard
- Each commit has one primary behavioral intent.
- Messages explain why and risk, not only file changes.
- Commit sequence is bisect-friendly for regression analysis.
- Sensitive data never appears in staged history.

## Failure Conditions
- Stop when a commit mixes unrelated behavior changes.
- Stop when a commit cannot be validated independently.
- Escalate when traceability/compliance requirements cannot be met with current history.
