---
name: runbook-authoring
description: Specialized workflow for operational procedure clarity for on-call responders. Use when documentation artifacts are the primary deliverable; do not use for writing production feature logic unless documenting already-approved outcomes.
---

# Runbook Authoring

## Trigger Boundary
- Use when production visibility, reliability targets, or incident response workflows are needed.
- Do not use for feature-level functional spec writing; use `requirements-*`.
- Do not use for pure code-style conformance checks.

## Goal
Maintain production reliability through measurable operational controls.

## Inputs
- Change scope and risk profile
- Domain evidence for operational procedure clarity for on-call responders
- Operational, compliance, and rollout constraints

## Outputs
- Runbook with decision tree and execution steps
- Decision log for operational procedure clarity for on-call responders
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for operational procedure clarity for on-call responders.
2. Produce options and select an approach for operational procedure clarity for on-call responders.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using tabletop drill for runbook usability.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for operational procedure clarity for on-call responders are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when runbook steps are ambiguous or missing rollback actions.
- Escalate when accepted risk exceeds team policy thresholds.
