---
name: security-authentication
description: Specialized workflow for identity verification flows and credential assurance controls. Trigger when security controls, abuse-path analysis, or vulnerability treatment are central; do not use for non-security quality optimization.
---

# Security Authentication

## Trigger Boundary
- Use when security controls, abuse paths, or compliance obligations must be defined.
- Do not use for non-security product prioritization; use requirement or roadmap skills.
- Do not use for purely aesthetic UI decisions.

## Goal
Reduce exploitable risk with verifiable security controls.

## Inputs
- Change scope and risk profile
- Domain evidence for identity verification flows and credential assurance controls
- Operational, compliance, and rollout constraints

## Outputs
- Authentication threat and control mapping
- Decision log for identity verification flows and credential assurance controls
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for identity verification flows and credential assurance controls.
2. Produce options and select an approach for identity verification flows and credential assurance controls.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using auth flow abuse-case and failure-path testing.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for identity verification flows and credential assurance controls are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when authentication controls do not enforce identity assurance requirements.
- Escalate when accepted risk exceeds team policy thresholds.
