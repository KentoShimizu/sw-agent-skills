---
name: api-design-rest
description: Specialized workflow for resource-oriented endpoint design and HTTP semantic consistency. Use when defining external API contracts, compatibility rules, and request/response behavior; do not use for storage-internal schema design or CI/CD orchestration.
---

# Api Design Rest

## Trigger Boundary
- Use when service interface contracts or compatibility rules are being defined.
- Do not use for storage internals; use `db-*`.
- Do not use for CI release orchestration; use `ci-cd-pipeline-design`.

## Goal
Deliver stable interfaces with predictable behavior and upgrade paths.

## Inputs
- Change scope and risk profile
- Domain evidence for resource-oriented endpoint design and HTTP semantic consistency
- Operational, compliance, and rollout constraints

## Outputs
- REST resource and endpoint specification
- Decision log for resource-oriented endpoint design and HTTP semantic consistency
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for resource-oriented endpoint design and HTTP semantic consistency.
2. Produce options and select an approach for resource-oriented endpoint design and HTTP semantic consistency.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using endpoint contract validation with status and error semantics.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for resource-oriented endpoint design and HTTP semantic consistency are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when resource model or HTTP semantics are inconsistent.
- Escalate when accepted risk exceeds team policy thresholds.
