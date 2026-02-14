---
name: kubernetes-security
description: Specialized workflow for cluster hardening, workload isolation, and policy enforcement. Use when container, orchestration, or infrastructure runtime configuration is central; do not use for API contract design or requirement prioritization.
---

# Kubernetes Security

## Trigger Boundary
- Use when runtime packaging, orchestration, or infrastructure controls must be defined.
- Do not use for product requirement decomposition; use `requirements-*` or `user-story-writing`.
- Do not use for post-incident review output; use `incident-postmortem`.

## Goal
Establish reproducible, secure, and operable runtime platforms.

## Inputs
- Change scope and risk profile
- Domain evidence for cluster hardening, workload isolation, and policy enforcement
- Operational, compliance, and rollout constraints

## Outputs
- Kubernetes security control matrix
- Decision log for cluster hardening, workload isolation, and policy enforcement
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for cluster hardening, workload isolation, and policy enforcement.
2. Produce options and select an approach for cluster hardening, workload isolation, and policy enforcement.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using policy and runtime security control verification.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for cluster hardening, workload isolation, and policy enforcement are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when critical workloads run without required isolation or policy guards.
- Escalate when accepted risk exceeds team policy thresholds.
