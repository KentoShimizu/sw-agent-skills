---
name: git-release-tagging
description: "Create immutable release tags and traceable release notes from Git history. Use when release cuts require consistent tag naming, immutability guarantees, and bounded changelog traceability; do not use for CI workflow design or application behavior implementation."
---

# Git Release Tagging

## Overview
Use this skill to cut releases with immutable tags and auditable change boundaries.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Versioning and immutability rules:
  - `references/tag-versioning-and-immutability.md`

## Templates And Assets
- Release tagging runbook:
  - `assets/release-tagging-runbook-template.md`
- Release notes template:
  - `assets/release-notes-template.md`

## Inputs To Gather
- Target release commit SHA and readiness evidence.
- Versioning policy and reserved tag namespace.
- Approval requirements and release communication needs.
- Rollback strategy if release validation fails post-cut.

## Deliverables
- Annotated release tag bound to a specific commit.
- Release notes mapped to bounded commit range.
- Verification record for tag integrity and publication status.
- Traceable release artifact metadata for audit.

## Workflow
1. Validate preconditions using `assets/release-tagging-runbook-template.md`.
2. Confirm naming and immutability constraints from `references/tag-versioning-and-immutability.md`.
3. Create annotated release tag and verify target commit binding.
4. Draft and publish release notes with `assets/release-notes-template.md`.
5. Record post-cut verification and handoff artifacts.

## Quality Standard
- Tag naming follows one consistent policy.
- Published tag is immutable and never re-pointed.
- Release notes are bounded, accurate, and actionable.
- Release cut can be traced from tag -> commit range -> notes.

## Failure Conditions
- Stop when release commit readiness is not proven.
- Stop when tag naming collides with existing published tags.
- Escalate when immutability cannot be guaranteed on current hosting setup.
