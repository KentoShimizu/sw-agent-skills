---
name: git-commit-hygiene
description: "Specialized workflow for enforcing atomic commits, clear commit messages, and auditable change intent. Trigger when changes are being prepared for commit and commit granularity, message clarity, and traceability must be enforced before push or review; do not use for CI workflow design or application behavior implementation."
---

# Git Commit Hygiene

## Trigger Boundary
- Use when commit quality, traceability, or reviewability must be improved.
- Do not use for architecture decision records; use `architecture-decision-records`.
- Do not use for source code style conventions; use language `*-style-guide` skills.

## Goal
Produce commit history that is easy to review, bisect, and audit.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the primary reference for recommended structure.
- Track commit hygiene artifacts with project-defined IDs (for example `GIT-CMT-*`).
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Changed files and logical change boundaries
- Team commit message conventions
- Compliance and traceability requirements

## Outputs
- project-defined ID (for example `GIT-CMT-*`) commit slicing and hygiene report
- Commit message standard and examples
- Pre-push and CI checklist for history quality

## Workflow
1. Separate unrelated changes into distinct logical commits.
2. Write intent-first commit messages with scope and rationale.
3. Verify each commit builds and passes relevant tests.
4. Run secret scanning on staged history in pre-push and CI.
5. Publish commit checklist and contract validation evidence.

## Quality Gates
- Each commit has one primary intent and reversible scope.
- Commit messages explain why, not only what changed.
- Commits are testable and bisect-friendly.
- Secret scan passes before push (`checks.secret_scan_passed=true`).

## Failure Handling
- Stop when a commit mixes unrelated behavioral changes.
- Stop when secret scan detects credentials or personal data leakage.
- Escalate when traceability requirements are unmet by current history.
