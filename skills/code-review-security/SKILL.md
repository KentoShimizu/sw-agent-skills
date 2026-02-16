---
name: code-review-security
description: Specialized workflow for vulnerability exposure, data protection, and abuse-path risks. Trigger during review when a change crosses trust boundaries or may impact authn/authz, secrets handling, input validation, or sensitive-data exposure and needs security-first findings; do not use for non-security quality concerns.
---

# Code Review Security

## Trigger Boundary
- Use when code changes need merge-readiness evaluation with explicit findings.
- Do not use for architecture option selection; use `architecture-tradeoff-analysis`.
- Do not use for writing implementation code directly; use relevant domain skills.

## Goal
Find high-risk defects early and unblock high-confidence merges.

## Inputs
- Change scope and risk profile
- Domain evidence for vulnerability exposure, data protection, and abuse-path risks
- Operational, compliance, and rollout constraints

## Outputs
- Security review finding set with remediation priority
- Decision log for vulnerability exposure, data protection, and abuse-path risks
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for vulnerability exposure, data protection, and abuse-path risks.
2. Produce options and select an approach for vulnerability exposure, data protection, and abuse-path risks.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using threat-informed review against attack surfaces.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for vulnerability exposure, data protection, and abuse-path risks are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when high-severity security risks are unresolved.
- Escalate when accepted risk exceeds team policy thresholds.
