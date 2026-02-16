---
name: documentation-api-reference
description: Specialized workflow for API reference completeness, accuracy, and client usability. Trigger when API contracts already exist and client-facing reference docs must be authored or updated with precise endpoints/schemas/errors/examples before release or external consumption; do not use for writing production feature logic unless documenting already-approved outcomes.
---

# Documentation Api Reference

## Trigger Boundary
- Use when engineering knowledge must be captured in durable, reviewable documents.
- Do not use for source code implementation tasks.
- Do not use for runtime production alert tuning; use `observability-*`.

## Goal
Create clear documentation that supports execution and auditability.

## Inputs
- Change scope and risk profile
- Domain evidence for API reference completeness, accuracy, and client usability
- Operational, compliance, and rollout constraints

## Outputs
- API reference quality checklist
- Decision log for API reference completeness, accuracy, and client usability
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for API reference completeness, accuracy, and client usability.
2. Produce options and select an approach for API reference completeness, accuracy, and client usability.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using sample request/response and edge-case doc verification.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for API reference completeness, accuracy, and client usability are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when API documentation omits required behavior or constraints.
- Escalate when accepted risk exceeds team policy thresholds.
