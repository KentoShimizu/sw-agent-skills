---
name: git-rebase-workflow
description: "Specialized workflow for linearizing local branch history with safe rebase practices before integration. Trigger when branch history needs cleanup or linearization prior to merge and rebase risk (conflicts, dropped commits, rewritten history impact) must be controlled; do not use for CI workflow design or application behavior implementation."
---

# Git Rebase Workflow

## Trigger Boundary
- Use only when local feature branch history needs cleanup before PR creation.
- Do not use once a PR is open; use `git-pr-sync-workflow`.
- Do not use on shared protected branches.

## Goal
Keep local branch history coherent and review-ready without losing change intent.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the primary reference for recommended structure.
- Track rebase artifacts with project-defined IDs (for example `GIT-RBS-*`).
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Current branch divergence from target base branch
- Team policy for force-push and rewritten history
- PR status and branch sharing status

## Outputs
- project-defined ID (for example `GIT-RBS-*`) rebased branch execution record
- Conflict resolution notes for rewritten commits
- Push plan aligned with rewrite policy

## Workflow
1. Verify the branch is unshared and `checks.pr_opened=false`.
2. Fetch latest target branch and inspect divergence.
3. Rebase feature commits onto target base in logical order.
4. Resolve conflicts commit-by-commit with behavioral verification.
5. Run tests, then push with approved force-with-lease policy.

## Quality Gates
- Rebased commits preserve original behavioral intent.
- Conflict resolutions are verified with tests.
- `checks.pr_opened=false` and `checks.rebase_used=true` are satisfied.
- History rewrite complies with team policy and branch protections.

## Failure Handling
- Stop when a PR is already open for the branch.
- Stop when rebase would rewrite shared protected history.
- Escalate when rewrite policy exceptions are requested.
