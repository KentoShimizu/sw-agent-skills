---
name: deployment-strategy-canary
description: Specialized workflow for canary rollout guardrails and progressive risk containment. Use when build, test, release, and rollout gates must be designed or changed; do not use for application-domain algorithm or schema decisions.
---

# Deployment Strategy Canary

## Trigger Boundary
- Use when release safety, deployment sequencing, or rollback controls are required.
- Do not use for business-priority ranking of requirements; use `requirement-prioritization`.
- Do not use for runtime incident retrospectives; use `incident-postmortem`.

## Goal
Deliver changes safely with repeatable, auditable release mechanics.

## Inputs
- Change scope and risk profile
- Domain evidence for canary rollout guardrails and progressive risk containment
- Operational, compliance, and rollout constraints

## Outputs
- Canary rollout plan with promotion criteria
- Decision log for canary rollout guardrails and progressive risk containment
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for canary rollout guardrails and progressive risk containment.
2. Produce options and select an approach for canary rollout guardrails and progressive risk containment.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using canary metric and abort-threshold validation.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for canary rollout guardrails and progressive risk containment are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when canary promotion criteria or abort rules are undefined.
- Escalate when accepted risk exceeds team policy thresholds.
