---
name: git-pr-sync-workflow
description: "Keep pull request branches synchronized with target branch updates using a safe, policy-aligned strategy. Use when a PR branch diverges from base and merge-vs-rebase plus conflict handling must be chosen safely; do not use for CI workflow design or application behavior implementation."
---

# Git Pr Sync Workflow

## Overview
Use this skill to synchronize open PR branches with minimal review disruption and predictable risk control.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Merge vs rebase decision guidance:
  - `references/sync-strategy-selection.md`

## Templates And Assets
- Sync decision log:
  - `assets/pr-sync-decision-log-template.md`
- Sync verification checklist:
  - `assets/pr-sync-checklist.md`

## Inputs To Gather
- Current PR divergence and base branch update scope.
- Repository policy for open-PR synchronization.
- CI requirements and review continuity expectations.
- Conflict complexity and affected critical files.

## Deliverables
- Chosen synchronization strategy with rationale.
- Conflict resolution notes for reviewers.
- Post-sync verification results.
- Updated PR context for review continuity.

## Workflow
1. Confirm sync necessity and policy constraints.
2. Choose strategy using `references/sync-strategy-selection.md`.
3. Execute sync and record rationale in `assets/pr-sync-decision-log-template.md`.
4. Resolve conflicts with reviewer-facing notes.
5. Re-run checks and verify completion via `assets/pr-sync-checklist.md`.

## Quality Standard
- Strategy choice is policy-compliant and explicitly justified.
- Conflict resolutions preserve intended behavior, not just clean merge state.
- Required checks are rerun after sync.
- Reviewer context is updated to avoid hidden history changes.

## Failure Conditions
- Stop when selected strategy violates repository policy.
- Stop when semantic conflicts remain unresolved after sync.
- Escalate when repeated drift indicates base-branch integration process issues.
