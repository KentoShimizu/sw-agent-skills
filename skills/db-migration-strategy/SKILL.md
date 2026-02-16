---
name: db-migration-strategy
description: Specialized workflow for schema migration sequencing, rollout safety, and rollback viability. Trigger when schema changes require online migration planning, compatibility windows, and explicit rollback or forward-only decisions across environments; do not use for API boundary design or infrastructure provisioning.
---

# Db Migration Strategy

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for schema migration sequencing, rollout safety, and rollback viability
- Operational, compliance, and rollout constraints

## Outputs
- Migration execution plan with stage gates
- Decision log for schema migration sequencing, rollout safety, and rollback viability
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for schema migration sequencing, rollout safety, and rollback viability.
2. Produce options and select an approach for schema migration sequencing, rollout safety, and rollback viability.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using dry-run migration and rollback rehearsal.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for schema migration sequencing, rollout safety, and rollback viability are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when rollback path is undefined for destructive or high-risk steps.
- Escalate when accepted risk exceeds team policy thresholds.
