---
name: docker-compose-patterns
description: Specialized workflow for multi-service local orchestration and dependency wiring. Use when container, orchestration, or infrastructure runtime configuration is central; do not use for API contract design or requirement prioritization.
---

# Docker Compose Patterns

## Trigger Boundary
- Use when runtime packaging, orchestration, or infrastructure controls must be defined.
- Do not use for product requirement decomposition; use `requirements-*` or `user-story-writing`.
- Do not use for post-incident review output; use `incident-postmortem`.

## Goal
Establish reproducible, secure, and operable runtime platforms.

## Inputs
- Change scope and risk profile
- Domain evidence for multi-service local orchestration and dependency wiring
- Operational, compliance, and rollout constraints

## Outputs
- Compose topology specification
- Decision log for multi-service local orchestration and dependency wiring
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for multi-service local orchestration and dependency wiring.
2. Produce options and select an approach for multi-service local orchestration and dependency wiring.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using orchestration startup-order and healthcheck validation.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for multi-service local orchestration and dependency wiring are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when service dependencies are not consistently reproducible.
- Escalate when accepted risk exceeds team policy thresholds.
