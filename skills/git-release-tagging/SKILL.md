---
name: git-release-tagging
description: "Specialized workflow for creating immutable release tags and traceable release notes from Git history. Trigger when a release cut requires consistent tag naming, immutability guarantees, and changelog traceability from commit history; do not use for CI workflow design or application behavior implementation."
---

# Git Release Tagging

## Trigger Boundary
- Use when shipping a release candidate or production release from Git.
- Do not use for deployment runtime orchestration; use `ci-cd-pipeline-design`.
- Do not use for sprint planning or roadmap updates; use `technical-roadmapping`.

## Goal
Produce auditable, immutable release markers with clear change traceability.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the single schema and gate source.
- Track release tagging artifacts with `GIT-REL-*` IDs.
- Run machine validation: `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Release branch or commit SHA to tag
- Versioning policy and naming convention
- Release notes source and approval requirements

## Outputs
- `GIT-REL-*` signed annotated release tag record
- Release notes linked to commit range
- Verification checklist for tagged artifact

## Workflow
1. Validate release commit readiness and required approvals.
2. Create signed annotated tag with version and summary metadata.
3. Verify signature and confirm tag points to intended immutable commit.
4. Generate release notes from bounded commit range.
5. Publish tag and notes with distribution and verification record.

## Quality Gates
- Tag naming follows repository versioning policy.
- Tag is signed, signature verification passes, and protected tag policy is enforced.
- Release notes map clearly to included changes.
- Security Reviewer approval is present for `GIT-REL-*` artifacts.

## Failure Handling
- Stop when release commit is not fully validated.
- Stop when tag signature cannot be verified.
- Escalate when version naming conflicts with existing tags.
