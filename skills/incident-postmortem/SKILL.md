---
name: incident-postmortem
description: Specialized workflow for incident root cause analysis and systemic prevention actions. Trigger after incident stabilization when teams need a rigorous timeline, root-cause chain, contributing factors, and prevention actions with clear ownership; do not use for active incident command and real-time mitigation.
---

# Incident Postmortem

## Trigger Boundary
- Use when production visibility, reliability targets, or incident response workflows are needed.
- Do not use for feature-level functional spec writing; use `requirements-*`.
- Do not use for pure code-style conformance checks.

## Goal
Maintain production reliability through measurable operational controls.

## Inputs
- Change scope and risk profile
- Domain evidence for incident root cause analysis and systemic prevention actions
- Operational, compliance, and rollout constraints

## Outputs
- Postmortem report with corrective action owners
- Decision log for incident root cause analysis and systemic prevention actions
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for incident root cause analysis and systemic prevention actions.
2. Produce options and select an approach for incident root cause analysis and systemic prevention actions.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using evidence-backed timeline and five-whys consistency check.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for incident root cause analysis and systemic prevention actions are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when root cause remains speculative without supporting evidence.
- Escalate when accepted risk exceeds team policy thresholds.
