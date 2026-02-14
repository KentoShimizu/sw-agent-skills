---
name: documentation-architecture
description: Specialized workflow for architecture documentation clarity for boundaries and dependencies. Use when documentation artifacts are the primary deliverable; do not use for writing production feature logic unless documenting already-approved outcomes.
---

# Documentation Architecture

## Trigger Boundary
- Use when engineering knowledge must be captured in durable, reviewable documents.
- Do not use for source code implementation tasks.
- Do not use for runtime production alert tuning; use `observability-*`.

## Goal
Create clear documentation that supports execution and auditability.

## Inputs
- Change scope and risk profile
- Domain evidence for architecture documentation clarity for boundaries and dependencies
- Operational, compliance, and rollout constraints

## Outputs
- Architecture documentation map
- Decision log for architecture documentation clarity for boundaries and dependencies
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for architecture documentation clarity for boundaries and dependencies.
2. Produce options and select an approach for architecture documentation clarity for boundaries and dependencies.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using dependency-direction and ownership consistency review.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for architecture documentation clarity for boundaries and dependencies are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when architecture docs do not match implemented boundaries.
- Escalate when accepted risk exceeds team policy thresholds.
