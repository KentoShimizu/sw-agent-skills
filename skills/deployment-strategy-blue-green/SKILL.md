---
name: deployment-strategy-blue-green
description: Specialized workflow for blue-green cutover safety and fast rollback readiness. Trigger when releases require near-zero-downtime environment switching with explicit cutover checks, rollback criteria, and traffic flip procedures; do not use for application-domain algorithm or schema decisions.
---

# Deployment Strategy Blue Green

## Trigger Boundary
- Use when release safety, deployment sequencing, or rollback controls are required.
- Do not use for business-priority ranking of requirements; use `requirement-prioritization`.
- Do not use for runtime incident retrospectives; use `incident-postmortem`.

## Goal
Deliver changes safely with repeatable, auditable release mechanics.

## Inputs
- Change scope and risk profile
- Domain evidence for blue-green cutover safety and fast rollback readiness
- Operational, compliance, and rollout constraints

## Outputs
- Blue-green deployment runbook
- Decision log for blue-green cutover safety and fast rollback readiness
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for blue-green cutover safety and fast rollback readiness.
2. Produce options and select an approach for blue-green cutover safety and fast rollback readiness.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using switch-over rehearsal with rollback timing evidence.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for blue-green cutover safety and fast rollback readiness are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when cutover cannot be reversed within operational limits.
- Escalate when accepted risk exceeds team policy thresholds.
