---
name: git-merge-conflict-resolution
description: "Specialized workflow for resolving Git merge conflicts with explicit intent tracking and verification. Trigger when merge or rebase conflicts occur and teams need intent-preserving conflict resolution with post-merge verification before integration; do not use for CI workflow design or application behavior implementation."
---

# Git Merge Conflict Resolution

## Trigger Boundary
- Use when merge operations produce textual or semantic conflicts.
- Do not use for product-level requirement prioritization; use `requirement-prioritization`.
- Do not use for post-incident rollback strategy; use `git-revert-recovery`.

## Goal
Resolve conflicts deterministically while preserving both correctness and intent.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the single schema and gate source.
- Track conflict resolution artifacts with `GIT-MRG-*` IDs.
- Run machine validation: `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Conflicted files and conflict markers
- Intent of each conflicting change set
- Required tests and verification scope

## Outputs
- `GIT-MRG-*` conflict resolution record
- File-level intent mapping for resolved hunks
- Verification evidence for resolved behavior

## Workflow
1. Classify conflicts by domain and behavioral impact.
2. Compare both sides' intent before editing conflict regions.
3. Resolve conflicts with minimal unintended side effects.
4. Re-run targeted and regression tests for affected paths.
5. Publish resolution record with contract validation evidence.

## Quality Gates
- Every resolved conflict has a clear intent rationale.
- No conflict markers remain in tracked files.
- Affected tests pass after conflict resolution.
- History rewrite policy and branch protections remain compliant.

## Failure Handling
- Stop when conflict intent cannot be reconstructed reliably.
- Escalate when semantic conflicts require domain-owner arbitration.
