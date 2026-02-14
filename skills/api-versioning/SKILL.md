---
name: api-versioning
description: Specialized workflow for version lifecycle governance and compatibility transition planning. Use when defining external API contracts, compatibility rules, and request/response behavior; do not use for storage-internal schema design or CI/CD orchestration.
---

# Api Versioning

## Trigger Boundary
- Use when service interface contracts or compatibility rules are being defined.
- Do not use for storage internals; use `db-*`.
- Do not use for CI release orchestration; use `ci-cd-pipeline-design`.

## Goal
Deliver stable interfaces with predictable behavior and upgrade paths.

## Inputs
- Change scope and risk profile
- Domain evidence for version lifecycle governance and compatibility transition planning
- Operational, compliance, and rollout constraints

## Outputs
- API versioning policy and deprecation plan
- Decision log for version lifecycle governance and compatibility transition planning
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for version lifecycle governance and compatibility transition planning.
2. Produce options and select an approach for version lifecycle governance and compatibility transition planning.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using compatibility test matrix across supported versions.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for version lifecycle governance and compatibility transition planning are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when version transitions break supported client integrations.
- Escalate when accepted risk exceeds team policy thresholds.
