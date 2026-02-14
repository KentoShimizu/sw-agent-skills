---
name: api-design-graphql
description: Specialized workflow for GraphQL schema boundaries, resolver behavior, and query safety. Use when defining external API contracts, compatibility rules, and request/response behavior; do not use for storage-internal schema design or CI/CD orchestration.
---

# Api Design Graphql

## Trigger Boundary
- Use when service interface contracts or compatibility rules are being defined.
- Do not use for storage internals; use `db-*`.
- Do not use for CI release orchestration; use `ci-cd-pipeline-design`.

## Goal
Deliver stable interfaces with predictable behavior and upgrade paths.

## Inputs
- Change scope and risk profile
- Domain evidence for GraphQL schema boundaries, resolver behavior, and query safety
- Operational, compliance, and rollout constraints

## Outputs
- GraphQL schema and resolver contract
- Decision log for GraphQL schema boundaries, resolver behavior, and query safety
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for GraphQL schema boundaries, resolver behavior, and query safety.
2. Produce options and select an approach for GraphQL schema boundaries, resolver behavior, and query safety.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using schema validation and resolver performance checks.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for GraphQL schema boundaries, resolver behavior, and query safety are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when schema changes break client expectations or resolver safeguards.
- Escalate when accepted risk exceeds team policy thresholds.
