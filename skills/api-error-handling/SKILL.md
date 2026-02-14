---
name: api-error-handling
description: Specialized workflow for error taxonomy, status mapping, and debuggable failure contracts. Use when defining external API contracts, compatibility rules, and request/response behavior; do not use for storage-internal schema design or CI/CD orchestration.
---

# Api Error Handling

## Trigger Boundary
- Use when service interface contracts or compatibility rules are being defined.
- Do not use for storage internals; use `db-*`.
- Do not use for CI release orchestration; use `ci-cd-pipeline-design`.

## Goal
Deliver stable interfaces with predictable behavior and upgrade paths.

## Inputs
- Change scope and risk profile
- Domain evidence for error taxonomy, status mapping, and debuggable failure contracts
- Operational, compliance, and rollout constraints

## Outputs
- API error model and response schema
- Decision log for error taxonomy, status mapping, and debuggable failure contracts
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for error taxonomy, status mapping, and debuggable failure contracts.
2. Produce options and select an approach for error taxonomy, status mapping, and debuggable failure contracts.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using error scenario testing with contract assertions.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for error taxonomy, status mapping, and debuggable failure contracts are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when error responses are ambiguous or non-actionable for clients.
- Escalate when accepted risk exceeds team policy thresholds.
