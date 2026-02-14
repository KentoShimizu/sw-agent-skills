---
name: git-pr-sync-workflow
description: "Specialized workflow for keeping pull request branches synchronized with target branch changes and review expectations. Use when Git history, branching, synchronization, or recovery workflows are the core concern; do not use for CI workflow design or application behavior implementation."
---

# Git Pr Sync Workflow

## Trigger Boundary
- Use when an open PR drifts from its target branch.
- Do not use for selective emergency backports; use `git-cherry-pick-hotfix`.
- Do not use for pre-PR local history cleanup; use `git-rebase-workflow`.

## Goal
Keep open PR branches merge-ready with minimal integration surprises.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the single schema and gate source.
- Track PR sync artifacts with `GIT-PRS-*` IDs.
- Run machine validation: `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Current PR branch divergence and target branch status
- Required checks and review policies
- Repository synchronization policy for open PRs

## Outputs
- `GIT-PRS-*` synchronized PR branch record
- Conflict and resolution notes for reviewers
- Updated validation evidence after synchronization

## Workflow
1. Confirm the PR is open and synchronization is required.
2. Apply the repository-approved synchronization strategy (merge or rebase) to the PR branch.
3. Resolve conflicts and preserve review context.
4. Re-run required CI and targeted manual checks.
5. Update PR notes with sync rationale, risk impact, and contract validation evidence.

## Quality Gates
- `checks.pr_opened=true` for synchronization records.
- Exactly one synchronization strategy is recorded (`checks.merge_sync_used` xor `checks.rebase_used`).
- Selected synchronization strategy complies with repository policy.
- Required checks pass after synchronization.
- Conflict decisions are documented for reviewers.

## Failure Handling
- Stop when synchronization strategy violates repository policy.
- Stop when sync introduces unresolved semantic conflicts.
- Escalate when branch drift repeatedly breaks required checks.
