---
name: git-branch-strategy
description: "Specialized workflow for defining branch topology, lifecycle rules, and merge policy in Git repositories. Use when Git history, branching, synchronization, or recovery workflows are the core concern; do not use for CI workflow design or application behavior implementation."
---

# Git Branch Strategy

## Trigger Boundary
- Use when branch naming, protection, or merge flow rules must be defined.
- Do not use for API version compatibility decisions; use `api-versioning`.
- Do not use for release train scheduling; use `release-management`.

## Goal
Establish a predictable branch model that reduces merge risk and review friction.

## Shared Git Contract (Canonical)
- Use `references/git-governance-contract.md` as the single schema and gate source.
- Track branch strategy artifacts with `GIT-BRN-*` IDs.
- Run machine validation: `python3 scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Team size and repository collaboration model
- Release cadence and hotfix requirements
- Existing branch protection and CI constraints

## Outputs
- `GIT-BRN-*` branch topology policy (`main`, release, hotfix, feature)
- Naming and retention rules for branches
- Merge policy and protection gate checklist

## Workflow
1. Define stable and ephemeral branch classes with ownership.
2. Specify naming conventions and branch creation rules.
3. Set merge direction and approval requirements per branch class.
4. Define explicit PR synchronization policy (merge-only, rebase-allowed, or strategy-by-branch) and enforcement points.
5. Publish policy with enforcement steps and contract validation evidence.

## Quality Gates
- Every branch class has clear creation and deletion rules.
- Merge permissions and protection checks are explicit.
- Open-PR synchronization policy is documented and enforceable.
- Policy can be enforced with repository settings.

## Failure Handling
- Stop when branch classes overlap without clear ownership.
- Escalate when required protections cannot be enforced technically.
