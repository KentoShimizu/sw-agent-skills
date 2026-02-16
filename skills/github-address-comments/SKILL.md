---
name: github-address-comments
description: "Pull request comment resolution workflow with GitHub CLI. Trigger when review comments on GitHub PRs/issues need structured triage, code updates, and traceable resolution responses; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Address Comments

## Trigger Boundary
- Use when open PR review threads require implementation follow-up.
- Do not use for unrelated issue backlog triage.
- Do not use for feature expansion not requested in review context.

## Goal
Close review loops with precise fixes and clear reviewer-facing responses.

## Inputs
- Target PR information
- Open review comments and thread status
- Repository validation requirements

## Outputs
- Prioritized comment-action mapping
- Code changes for selected comments
- Thread-by-thread response summary with verification notes

## Workflow
1. Confirm `gh` authentication and identify active PR.
2. Fetch comments and group by severity, risk, and dependency.
3. Align on which threads are in scope for this pass.
4. Implement focused fixes and run relevant tests.
5. Reply on each addressed thread with concrete change references.

## Scripts
- Fetch review threads:
  - `python3 scripts/fetch_review_threads.py --repo . --pr <number>`
- JSON output for tooling:
  - `python3 scripts/fetch_review_threads.py --repo . --pr <number> --json`

## Quality Gates
- Every addressed comment maps to code changes or explicit rationale.
- High-severity comments are resolved before cosmetic requests.
- Verification evidence is provided for behavior-affecting fixes.
- Responses are specific enough for reviewers to validate quickly.

## Failure Handling
- Stop when comment intent or scope is ambiguous.
- Escalate when requested change conflicts with system constraints or policy.

## References
- `references/reply-templates.md`
