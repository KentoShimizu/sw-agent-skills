---
name: git-revert-recovery
description: "Specialized workflow for recovering safely from problematic merges or commits using explicit revert strategy. Trigger when a bad commit or merge has landed and rollback intent, blast radius, and follow-up recovery steps must be defined explicitly; do not use for CI workflow design or application behavior implementation."
---

# Git Revert Recovery

## Trigger Boundary
- Use when already-pushed commits must be undone safely.
- Do not use for private local history cleanup; use `git-rebase-workflow`.
- Do not use as a substitute for root-cause analysis in incidents.

## Goal
Restore stable behavior quickly without destructive history rewriting.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the single schema and gate source.
- Track revert artifacts with `GIT-RVT-*` IDs.
- Run machine validation: `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Problematic commit or merge identifiers
- Blast radius and urgency assessment
- Verification and communication requirements

## Outputs
- `GIT-RVT-*` revert execution record
- Validation results for recovered branch state
- Follow-up action list for permanent fix

## Workflow
1. Confirm rollback target and expected recovered behavior.
2. Choose revert scope (single commit, range, or merge revert).
3. Execute revert and resolve any secondary conflicts.
4. Validate critical paths and regression-sensitive flows.
5. Communicate rollback impact with security review evidence.

## Quality Gates
- Revert target is explicitly identified and justified.
- Recovery validation passes for critical user paths.
- Rollback communication includes impact and ownership.
- Security Reviewer approval is present for `GIT-RVT-*` artifacts.

## Failure Handling
- Stop when revert scope is ambiguous or unverified.
- Escalate when rollback does not restore expected stability.
