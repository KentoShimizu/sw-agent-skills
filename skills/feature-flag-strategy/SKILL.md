---
name: feature-flag-strategy
description: Specialized workflow for flag lifecycle governance and blast-radius control. Use when runtime flag lifecycle, rollout safety, and kill-switch governance are in scope; do not use for statistical experiment design and analysis.
---

# Feature Flag Strategy

## Trigger Boundary
- Use when release safety, deployment sequencing, or rollback controls are required.
- Do not use for business-priority ranking of requirements; use `requirement-prioritization`.
- Do not use for runtime incident retrospectives; use `incident-postmortem`.

## Goal
Deliver changes safely with repeatable, auditable release mechanics.

## Inputs
- Change scope and risk profile
- Domain evidence for flag lifecycle governance and blast-radius control
- Operational, compliance, and rollout constraints

## Outputs
- Feature flag catalog with ownership and expiry
- Decision log for flag lifecycle governance and blast-radius control
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for flag lifecycle governance and blast-radius control.
2. Produce options and select an approach for flag lifecycle governance and blast-radius control.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using flag targeting and kill-switch behavior verification.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for flag lifecycle governance and blast-radius control are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when feature flags lack ownership, expiry, or safe disable paths.
- Escalate when accepted risk exceeds team policy thresholds.
