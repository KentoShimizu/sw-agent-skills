---
name: github-release-management
description: "Package and publish GitHub Releases with exact version/tag mapping, accurate release notes, and artifact integrity controls. Use when release publication on GitHub must be prepared or updated; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Release Management

## Overview
Use this skill to publish GitHub Releases that are accurate, traceable, and operationally usable by consumers.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Release note structure guidance:
  - `references/release-note-format.md`

## Templates And Assets
- Release publication checklist:
  - `assets/github-release-checklist.md`

## Inputs To Gather
- Version target and release tag/commit mapping.
- Changelog sources (PRs, commits, issues).
- Artifact inventory, integrity policy, and compatibility notes.
- Approval and communication requirements.

## Deliverables
- Draft/final GitHub Release package.
- Release notes with upgrade and breaking-change guidance.
- Verified artifact links and integrity evidence.
- Post-release verification record.

## Workflow
1. Confirm release scope and freeze target commit.
2. Generate notes with `scripts/draft_release_notes.py`.
3. Validate notes format and completeness via `references/release-note-format.md`.
4. Verify publication readiness with `assets/github-release-checklist.md`.
5. Publish release and capture verification/follow-up actions.

## Scripts
- Generate draft notes from commit range:
  - `python3 scripts/draft_release_notes.py --repo . --version v1.2.3 --from-ref <base_ref> --to-ref HEAD`
- Write output file:
  - `python3 scripts/draft_release_notes.py --repo . --version v1.2.3 --from-ref <base_ref> --to-ref HEAD --out /tmp/release-notes.md`

## Quality Standard
- Release notes reflect shipped changes without ambiguity.
- Version/tag mapping is exact and immutable.
- Breaking changes and migration guidance are explicit.
- Artifacts are available and integrity-verified.

## Failure Conditions
- Stop when release scope, version, or tag mapping is inconsistent.
- Stop when artifact integrity cannot be verified.
- Escalate when breaking-change guidance is incomplete for public release.
