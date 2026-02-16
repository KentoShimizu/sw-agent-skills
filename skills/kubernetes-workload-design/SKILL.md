---
name: kubernetes-workload-design
description: Specialized workflow for resource sizing, rollout behavior, and workload resilience design. Trigger when Kubernetes workload specs need concrete sizing, autoscaling, availability, and rollout strategy decisions to meet reliability and performance targets; do not use for API contract design or requirement prioritization.
---

# Kubernetes Workload Design

## Trigger Boundary
- Use when runtime packaging, orchestration, or infrastructure controls must be defined.
- Do not use for product requirement decomposition; use `requirements-*` or `user-story-writing`.
- Do not use for post-incident review output; use `incident-postmortem`.

## Goal
Establish reproducible, secure, and operable runtime platforms.

## Inputs
- Change scope and risk profile
- Domain evidence for resource sizing, rollout behavior, and workload resilience design
- Operational, compliance, and rollout constraints

## Outputs
- Workload design spec with scaling and rollout controls
- Decision log for resource sizing, rollout behavior, and workload resilience design
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for resource sizing, rollout behavior, and workload resilience design.
2. Produce options and select an approach for resource sizing, rollout behavior, and workload resilience design.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using autoscaling and rollout behavior tests.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for resource sizing, rollout behavior, and workload resilience design are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when workload design lacks safe rollout or capacity guarantees.
- Escalate when accepted risk exceeds team policy thresholds.
