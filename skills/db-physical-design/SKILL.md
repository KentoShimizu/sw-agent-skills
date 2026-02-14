---
name: db-physical-design
description: Specialized workflow for storage layout, partitioning, and engine-specific performance controls. Use when schema, indexing, query planning, transaction semantics, migration safety, or durability behavior is in scope; do not use for API boundary design or infrastructure provisioning.
---

# Db Physical Design

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for storage layout, partitioning, and engine-specific performance controls
- Operational, compliance, and rollout constraints

## Outputs
- Physical storage design specification
- Decision log for storage layout, partitioning, and engine-specific performance controls
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for storage layout, partitioning, and engine-specific performance controls.
2. Produce options and select an approach for storage layout, partitioning, and engine-specific performance controls.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using I/O and storage footprint profiling under target workloads.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for storage layout, partitioning, and engine-specific performance controls are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when storage layout cannot sustain expected load or growth.
- Escalate when accepted risk exceeds team policy thresholds.
