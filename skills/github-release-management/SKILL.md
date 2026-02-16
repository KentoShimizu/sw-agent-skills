---
name: github-release-management
description: "GitHub release packaging process. Trigger when a release must be prepared on GitHub with version/tag alignment, release-note quality, artifact linkage, and publication controls before announcement; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Release Management

## Trigger Boundary
- Use when creating GitHub Releases for production or staged delivery.
- Do not use for generic git tag mechanics alone; use `git-release-tagging`.
- Do not use for deployment orchestration details; use `ci-cd-pipeline-design`.

## Goal
Publish clear and auditable GitHub Releases with correct artifact mapping.

## Inputs
- Version target and release branch/commit
- Changelog source (PRs, commits, issues)
- Release artifact inventory and checksum policy

## Outputs
- Release draft/final package with notes
- Tagged commit linkage and artifact references
- Post-release verification checklist

## Workflow
1. Confirm release scope and freeze target commit.
2. Generate release notes from merged changes and notable fixes.
3. Validate artifacts, checksums, and compatibility notes.
4. Publish release with clear upgrade and rollback guidance.
5. Record post-release verification and follow-up actions.

## Scripts
- Generate draft notes from commit range:
  - `python3 scripts/draft_release_notes.py --repo . --version v1.2.3 --from-ref <base_ref> --to-ref HEAD`
- Write output file:
  - `python3 scripts/draft_release_notes.py --repo . --version v1.2.3 --from-ref <base_ref> --to-ref HEAD --out /tmp/release-notes.md`

## Quality Gates
- Release notes reflect actual shipped changes.
- Version/tag mapping is exact and immutable.
- Critical migration or breaking changes are explicit.
- Artifacts are downloadable and integrity-checked.

## Failure Handling
- Stop when release scope or artifact set is inconsistent.
- Escalate when breaking-change guidance is incomplete.

## References
- `references/release-note-format.md`
