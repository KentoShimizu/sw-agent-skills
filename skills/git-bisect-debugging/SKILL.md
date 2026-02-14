---
name: git-bisect-debugging
description: "Specialized workflow for locating regression-introducing commits with git bisect and deterministic checks. Use when Git history, branching, synchronization, or recovery workflows are the core concern; do not use for CI workflow design or application behavior implementation."
---

# Git Bisect Debugging

## Trigger Boundary
- Use when there is a known good revision and known bad revision.
- Do not use when no deterministic pass-fail check exists.
- Do not use for dependency vulnerability triage; use `security-vulnerability-management`.

## Goal
Isolate the first bad commit with objective pass-fail evidence.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the single schema and gate source.
- Track bisect artifacts with `GIT-BIS-*` IDs.
- Run machine validation: `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Known good commit and known bad commit
- Deterministic test or script for bisect classification
- Environment requirements for reproducible execution

## Outputs
- `GIT-BIS-*` culprit commit evidence
- Bisect log with classified steps
- Next-step fix or revert recommendation

## Workflow
1. Confirm deterministic reproduction with good and bad endpoints.
2. Start bisect and classify midpoint commits.
3. Automate classification when possible for consistency.
4. Validate culprit commit by replaying test around boundary.
5. Publish culprit evidence with contract validation record.

## Quality Gates
- Good/bad endpoints are validated before bisect starts.
- Classification command is deterministic and documented.
- Culprit commit is confirmed by repeatable verification.
- Bisect session log is preserved for auditability.

## Failure Handling
- Stop when classification is flaky or environment-dependent.
- Escalate when multiple interacting commits mask single-commit isolation.
