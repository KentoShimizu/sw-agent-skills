---
name: documentation-rfc
description: Specialized workflow for decision proposal structure, trade-off clarity, and approval traceability. Trigger when a technical direction is not yet approved and stakeholders need an RFC that compares options, risks, and adoption plan with explicit decision records; do not use for writing production feature logic unless documenting already-approved outcomes.
---

# Documentation Rfc

## Trigger Boundary
- Use when engineering knowledge must be captured in durable, reviewable documents.
- Do not use for source code implementation tasks.
- Do not use for runtime production alert tuning; use `observability-*`.

## Goal
Create clear documentation that supports execution and auditability.

## Inputs
- Change scope and risk profile
- Domain evidence for decision proposal structure, trade-off clarity, and approval traceability
- Operational, compliance, and rollout constraints

## Outputs
- RFC package with alternatives and decision criteria
- Decision log for decision proposal structure, trade-off clarity, and approval traceability
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for decision proposal structure, trade-off clarity, and approval traceability.
2. Produce options and select an approach for decision proposal structure, trade-off clarity, and approval traceability.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using review feedback closure and decision trace check.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for decision proposal structure, trade-off clarity, and approval traceability are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when RFC lacks explicit alternatives or decision criteria.
- Escalate when accepted risk exceeds team policy thresholds.
