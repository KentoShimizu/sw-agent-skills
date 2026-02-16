---
name: ci-cd-pipeline-design
description: Specialized workflow for pipeline stage design, gate sequencing, and build reproducibility. Trigger when build/test/release/rollout flow is new or changing and teams need explicit gate criteria, stage order, artifact traceability, and rollback safety before adoption; do not use for application-domain algorithm or schema decisions.
---

# Ci Cd Pipeline Design

## Trigger Boundary
- Use when release safety, deployment sequencing, or rollback controls are required.
- Do not use for business-priority ranking of requirements; use `requirement-prioritization`.
- Do not use for runtime incident retrospectives; use `incident-postmortem`.

## Goal
Deliver changes safely with repeatable, auditable release mechanics.

## Inputs
- Change scope and risk profile
- Domain evidence for pipeline stage design, gate sequencing, and build reproducibility
- Operational, compliance, and rollout constraints

## Outputs
- CI/CD stage and gate specification
- Decision log for pipeline stage design, gate sequencing, and build reproducibility
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for pipeline stage design, gate sequencing, and build reproducibility.
2. Produce options and select an approach for pipeline stage design, gate sequencing, and build reproducibility.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using pipeline dry-runs across success and failure paths.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for pipeline stage design, gate sequencing, and build reproducibility are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when release-critical gates are missing or non-deterministic.
- Escalate when accepted risk exceeds team policy thresholds.
