---
name: github-address-comments
description: "Resolve GitHub PR review comments with structured triage, focused code changes, and reviewer-verifiable responses. Use when review threads need implementation follow-up and traceable closure; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Address Comments

## Overview
Use this skill to turn review comments into prioritized, verified fixes and explicit thread closure evidence.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Templates And Assets
- Comment resolution log:
  - `assets/comment-resolution-log-template.md`

## Shared References
- Reviewer reply patterns:
  - `references/reply-templates.md`

## Inputs To Gather
- Target PR information.
- Open review comments and thread status.
- Repository validation requirements.
- Scope agreement for this response pass.

## Deliverables
- Prioritized comment-action mapping.
- Code changes scoped to accepted comment threads.
- Thread-by-thread responses with verification evidence.
- Deferred-item log for out-of-scope threads.

## Workflow
1. Confirm `gh` authentication and identify active PR.
2. Fetch comments using `scripts/fetch_review_threads.py`.
3. Prioritize threads by severity/risk/dependency and log in `assets/comment-resolution-log-template.md`.
4. Implement focused fixes and run relevant validation.
5. Reply with concrete change references using `references/reply-templates.md`.

## Scripts
- Fetch review threads:
  - `python3 scripts/fetch_review_threads.py --repo . --pr <number>`
- JSON output for tooling:
  - `python3 scripts/fetch_review_threads.py --repo . --pr <number> --json`

## Quality Standard
- Every addressed comment maps to code changes or explicit rationale.
- High-severity comments are handled before cosmetic threads.
- Behavior-affecting fixes include verification evidence.
- Responses are specific enough for quick reviewer validation.

## Failure Conditions
- Stop when comment intent or scope is ambiguous.
- Stop when requested change conflicts with approved product/architecture decisions.
- Escalate when required context is missing from reviewer discussion.
