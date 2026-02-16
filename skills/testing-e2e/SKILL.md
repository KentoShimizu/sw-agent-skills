---
name: testing-e2e
description: Specialized workflow for full-stack user journey integrity across integrated systems. Trigger when critical end-user flows must be validated across UI, APIs, and dependencies as integrated journeys before release; do not use for observability ownership or release scheduling policy.
---

# Testing E2e

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for full-stack user journey integrity across integrated systems
- Operational, compliance, and rollout constraints

## Outputs
- End-to-end critical journey test pack
- Decision log for full-stack user journey integrity across integrated systems
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for full-stack user journey integrity across integrated systems.
2. Produce options and select an approach for full-stack user journey integrity across integrated systems.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using production-like environment run for key journeys.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for full-stack user journey integrity across integrated systems are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when critical user journeys fail under integrated conditions.
- Escalate when accepted risk exceeds team policy thresholds.
