---
name: db-index-strategy
description: Specialized workflow for index selection for critical read and write access paths. Use when schema, indexing, query planning, transaction semantics, migration safety, or durability behavior is in scope; do not use for API boundary design or infrastructure provisioning.
---

# Db Index Strategy

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for index selection for critical read and write access paths
- Operational, compliance, and rollout constraints

## Outputs
- Index strategy plan per high-volume query
- Decision log for index selection for critical read and write access paths
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for index selection for critical read and write access paths.
2. Produce options and select an approach for index selection for critical read and write access paths.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using execution plan review and index impact measurement.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for index selection for critical read and write access paths are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when hot queries lack index coverage or write amplification risk is unknown.
- Escalate when accepted risk exceeds team policy thresholds.
