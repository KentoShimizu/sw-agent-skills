---
name: release-management
description: Specialized workflow for release readiness coordination and risk sign-off governance. Trigger when a release decision needs explicit go/no-go criteria, cross-team readiness checks, rollback preparedness, and formal risk sign-off; do not use for application-domain algorithm or schema decisions.
---

# Release Management

## Trigger Boundary
- Use when release safety, deployment sequencing, or rollback controls are required.
- Do not use for business-priority ranking of requirements; use `requirement-prioritization`.
- Do not use for runtime incident retrospectives; use `incident-postmortem`.

## Goal
Deliver changes safely with repeatable, auditable release mechanics.

## Inputs
- Change scope and risk profile
- Domain evidence for release readiness coordination and risk sign-off governance
- Operational, compliance, and rollout constraints

## Outputs
- Release readiness checklist and decision record
- Decision log for release readiness coordination and risk sign-off governance
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for release readiness coordination and risk sign-off governance.
2. Produce options and select an approach for release readiness coordination and risk sign-off governance.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using go/no-go review with cross-team evidence.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for release readiness coordination and risk sign-off governance are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when release decision lacks required evidence or ownership sign-off.
- Escalate when accepted risk exceeds team policy thresholds.
