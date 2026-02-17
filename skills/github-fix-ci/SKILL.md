---
name: github-fix-ci
description: "Respond to GitHub Actions failures with evidence-based triage, root-cause isolation, and minimal-risk fixes. Use when GitHub-hosted checks fail and teams need a repair plan tied to failed jobs; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Fix Ci

## Overview
Use this skill to move failed CI checks from symptoms to verified root-cause fixes without bypassing quality gates.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- CI failure taxonomy:
  - `references/ci-failure-taxonomy.md`

## Templates And Assets
- Failure triage template:
  - `assets/ci-failure-triage-template.md`

## Inputs To Gather
- PR identifier or current-branch PR context.
- `gh` authentication with required scopes.
- Failed check list, run URLs, and logs.
- Current branch changes and local reproducibility constraints.

## Deliverables
- Root-cause summary with evidence links.
- Approved fix plan with minimal change scope.
- Verification evidence (local + GitHub checks).
- Explicit blocker note when full green is not yet possible.

## Workflow
1. Resolve target PR and gather failures with `scripts/inspect_pr_checks.py`.
2. Record triage in `assets/ci-failure-triage-template.md`.
3. Classify root cause with `references/ci-failure-taxonomy.md`.
4. Propose remediation plan and wait for approval before edits.
5. Implement minimal fix and re-run relevant checks.

## Scripts
- Run failure inspection:
  - `python3 scripts/inspect_pr_checks.py --repo . --pr <number>`
- JSON output for automation:
  - `python3 scripts/inspect_pr_checks.py --repo . --pr <number> --json`
- Partial log fetch failures are reported as `snippet_error` while processing continues for other checks.

## Quality Standard
- Diagnosis includes check name, run URL, and concrete failing evidence.
- Fix scope is directly tied to identified root cause.
- Verification mirrors failing CI surface as closely as practical.
- Remaining blockers are explicit, owned, and time-bounded.

## Failure Conditions
- Stop when `gh` authentication or permissions are insufficient.
- Stop when root cause cannot be evidenced from logs or reproduction.
- Escalate when failures originate outside GitHub Actions and logs are unavailable.
