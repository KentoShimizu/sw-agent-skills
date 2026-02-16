---
name: github-fix-ci
description: "GitHub Actions failure response workflow using GitHub CLI. Trigger when GitHub-hosted CI checks fail and teams need failure triage, log-based root-cause isolation, and a repair plan tied to specific failed jobs; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Fix Ci

## Trigger Boundary
- Use when PR checks in GitHub Actions are failing.
- Do not use for non-GitHub CI providers except reporting their details URL.
- Do not use to bypass failing checks without root-cause remediation.

## Goal
Reduce CI downtime by converting failing checks into validated, minimal fixes.

## Inputs
- PR identifier or current-branch PR context
- `gh` authentication with required scopes
- Failed check list and log access

## Outputs
- Root-cause summary with evidence links
- Approved remediation plan
- Code/test updates and post-fix verification status
- Unresolved blocker note with owner and next action when full green is not yet possible

## Workflow
1. Validate `gh` auth and resolve target PR.
2. Collect failing checks and obtain actionable log excerpts.
3. Identify root cause category (test failure, env drift, flaky infra, config regression).
4. Propose fix plan and wait for explicit approval before edits.
5. Implement, run local verification, and recheck PR checks.

## Scripts
- Run failure inspection:
  - `python3 scripts/inspect_pr_checks.py --repo . --pr <number>`
- JSON output for automation:
  - `python3 scripts/inspect_pr_checks.py --repo . --pr <number> --json`
- Partial log fetch failures are reported as `snippet_error` while processing continues for other checks.

## Quality Gates
- Failure diagnosis includes check name, run URL, and failing snippet.
- Fix scope is minimal and tied directly to root cause.
- Local validation mirrors the failing CI surface as closely as possible.
- Required checks are green, or unresolved external blockers are explicitly documented with owner and next action.

## Failure Handling
- Stop when `gh` authentication or permissions are insufficient.
- Escalate when failures originate outside GitHub Actions and logs are unavailable.

## References
- `references/ci-failure-taxonomy.md`
