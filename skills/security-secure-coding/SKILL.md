---
name: security-secure-coding
description: Specialized workflow for secure-by-default coding patterns and vulnerability prevention. Use when security controls, abuse-path analysis, or vulnerability treatment are central; do not use for non-security quality optimization.
---

# Security Secure Coding

## Trigger Boundary
- Use when security controls, abuse paths, or compliance obligations must be defined.
- Do not use for non-security product prioritization; use requirement or roadmap skills.
- Do not use for purely aesthetic UI decisions.

## Goal
Reduce exploitable risk with verifiable security controls.

## Inputs
- Change scope and risk profile
- Domain evidence for secure-by-default coding patterns and vulnerability prevention
- Operational, compliance, and rollout constraints

## Outputs
- Secure coding checklist mapped to threat classes
- Decision log for secure-by-default coding patterns and vulnerability prevention
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for secure-by-default coding patterns and vulnerability prevention.
2. Produce options and select an approach for secure-by-default coding patterns and vulnerability prevention.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using code-path review against known vulnerability patterns.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for secure-by-default coding patterns and vulnerability prevention are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when high-risk insecure patterns remain in critical paths.
- Escalate when accepted risk exceeds team policy thresholds.
