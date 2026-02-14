---
name: code-review-general
description: Specialized workflow for correctness, maintainability, and change risk in code reviews. Use during code review when correctness, maintainability, and change risk must be assessed; do not use for domain-specific security-only or performance-only review tracks.
---

# Code Review General

## Trigger Boundary
- Use when code changes need merge-readiness evaluation with explicit findings.
- Do not use for architecture option selection; use `architecture-tradeoff-analysis`.
- Do not use for writing implementation code directly; use relevant domain skills.

## Goal
Find high-risk defects early and unblock high-confidence merges.

## Inputs
- Change scope and risk profile
- Domain evidence for correctness, maintainability, and change risk in code reviews
- Operational, compliance, and rollout constraints

## Outputs
- Review findings log with severity and rationale
- Decision log for correctness, maintainability, and change risk in code reviews
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for correctness, maintainability, and change risk in code reviews.
2. Produce options and select an approach for correctness, maintainability, and change risk in code reviews.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using line-by-line evidence trace for each finding.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for correctness, maintainability, and change risk in code reviews are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when critical correctness defects remain unresolved.
- Escalate when accepted risk exceeds team policy thresholds.
