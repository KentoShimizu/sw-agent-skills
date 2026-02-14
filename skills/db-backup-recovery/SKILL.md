---
name: db-backup-recovery
description: Specialized workflow for backup retention, restore reliability, and recovery time objectives. Use when schema, indexing, query planning, transaction semantics, migration safety, or durability behavior is in scope; do not use for API boundary design or infrastructure provisioning.
---

# Db Backup Recovery

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for backup retention, restore reliability, and recovery time objectives
- Operational, compliance, and rollout constraints

## Outputs
- Backup and recovery verification matrix
- Decision log for backup retention, restore reliability, and recovery time objectives
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for backup retention, restore reliability, and recovery time objectives.
2. Produce options and select an approach for backup retention, restore reliability, and recovery time objectives.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using periodic restore drills with RPO/RTO evidence.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for backup retention, restore reliability, and recovery time objectives are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when restore procedures are untested or RPO/RTO targets are unmet.
- Escalate when accepted risk exceeds team policy thresholds.
