---
name: security-authorization
description: Specialized workflow for access decision modeling and least-privilege enforcement. Trigger when security controls, abuse-path analysis, or vulnerability treatment are central; do not use for non-security quality optimization.
---

# Security Authorization

## Trigger Boundary
- Use when security controls, abuse paths, or compliance obligations must be defined.
- Do not use for non-security product prioritization; use requirement or roadmap skills.
- Do not use for purely aesthetic UI decisions.

## Goal
Reduce exploitable risk with verifiable security controls.

## Inputs
- Change scope and risk profile
- Domain evidence for access decision modeling and least-privilege enforcement
- Operational, compliance, and rollout constraints

## Outputs
- Authorization policy matrix
- Decision log for access decision modeling and least-privilege enforcement
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for access decision modeling and least-privilege enforcement.
2. Produce options and select an approach for access decision modeling and least-privilege enforcement.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using privilege boundary and escalation-path verification.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for access decision modeling and least-privilege enforcement are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when authorization rules allow privilege escalation or over-broad access.
- Escalate when accepted risk exceeds team policy thresholds.
