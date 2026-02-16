---
name: infrastructure-as-code
description: Specialized workflow for declarative infrastructure change management and drift prevention. Trigger when infrastructure changes must be represented declaratively with reviewable plans, module boundaries, state safety, and drift controls before apply; do not use for API contract design or requirement prioritization.
---

# Infrastructure As Code

## Trigger Boundary
- Use when runtime packaging, orchestration, or infrastructure controls must be defined.
- Do not use for product requirement decomposition; use `requirements-*` or `user-story-writing`.
- Do not use for post-incident review output; use `incident-postmortem`.

## Goal
Establish reproducible, secure, and operable runtime platforms.

## Inputs
- Change scope and risk profile
- Domain evidence for declarative infrastructure change management and drift prevention
- Operational, compliance, and rollout constraints

## Outputs
- Infrastructure plan and apply policy
- Decision log for declarative infrastructure change management and drift prevention
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for declarative infrastructure change management and drift prevention.
2. Produce options and select an approach for declarative infrastructure change management and drift prevention.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using plan review and drift-detection outputs.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for declarative infrastructure change management and drift prevention are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when infrastructure changes cannot be reviewed or reproduced declaratively.
- Escalate when accepted risk exceeds team policy thresholds.
