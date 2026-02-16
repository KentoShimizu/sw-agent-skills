---
name: docker-basics
description: Specialized workflow for container runtime fundamentals and reproducible local execution. Trigger when a service must be containerized or run reproducibly across developer/CI environments and base-image, runtime, and execution assumptions need to be made explicit; do not use for API contract design or requirement prioritization.
---

# Docker Basics

## Trigger Boundary
- Use when runtime packaging, orchestration, or infrastructure controls must be defined.
- Do not use for product requirement decomposition; use `requirements-*` or `user-story-writing`.
- Do not use for post-incident review output; use `incident-postmortem`.

## Goal
Establish reproducible, secure, and operable runtime platforms.

## Inputs
- Change scope and risk profile
- Domain evidence for container runtime fundamentals and reproducible local execution
- Operational, compliance, and rollout constraints

## Outputs
- Container runtime baseline checklist
- Decision log for container runtime fundamentals and reproducible local execution
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for container runtime fundamentals and reproducible local execution.
2. Produce options and select an approach for container runtime fundamentals and reproducible local execution.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using clean-environment image run verification.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for container runtime fundamentals and reproducible local execution are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when container behavior differs from documented runtime assumptions.
- Escalate when accepted risk exceeds team policy thresholds.
