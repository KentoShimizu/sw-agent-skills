---
name: git-cherry-pick-hotfix
description: "Specialized workflow for selecting and applying minimal hotfix commits across branches via cherry-pick. Trigger when urgent fixes must be propagated to other maintained branches without pulling unrelated changes and commit selection risk must be controlled; do not use for CI workflow design or application behavior implementation."
---

# Git Cherry Pick Hotfix

## Trigger Boundary
- Use when a fix from one branch must be ported to another without full merge.
- Do not use for broad release synchronization; use `git-pr-sync-workflow`.
- Do not use for feature migration involving many dependent commits.

## Goal
Backport urgent fixes safely with minimal unrelated change propagation.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the primary reference for recommended structure.
- Track hotfix backports with project-defined IDs (for example `GIT-CHP-*`).
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Source fix commit hashes and dependency notes
- Target branch release constraints
- Verification scope for target environment

## Outputs
- project-defined ID (for example `GIT-CHP-*`) cherry-pick execution record
- Dependency and risk annotation per picked commit
- Target-branch verification checklist and result

## Workflow
1. Identify minimal commit set required for the fix.
2. Validate hidden dependencies before cherry-pick.
3. Apply commits in dependency-safe order.
4. Resolve conflicts and verify target branch behavior.
5. Record source-to-target mapping with security review evidence.

## Quality Gates
- Picked commits exclude unrelated feature changes.
- Dependency assumptions are explicitly validated.
- Target branch tests pass for impacted flows.
- Security Reviewer approval is present for project-defined ID (for example `GIT-CHP-*`) artifacts.

## Failure Handling
- Stop when hotfix requires broad dependency migration.
- Escalate when target branch behavior diverges from source assumptions.
