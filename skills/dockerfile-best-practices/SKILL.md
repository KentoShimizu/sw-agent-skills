---
name: dockerfile-best-practices
description: Specialized workflow for image build efficiency, security posture, and deterministic builds. Trigger when Dockerfiles are created or modified and image size, build speed, supply-chain security, and reproducibility need deliberate optimization decisions; do not use for API contract design or requirement prioritization.
---

# Dockerfile Best Practices

## Trigger Boundary
- Use when runtime packaging, orchestration, or infrastructure controls must be defined.
- Do not use for product requirement decomposition; use `requirements-*` or `user-story-writing`.
- Do not use for post-incident review output; use `incident-postmortem`.

## Goal
Establish reproducible, secure, and operable runtime platforms.

## Inputs
- Change scope and risk profile
- Domain evidence for image build efficiency, security posture, and deterministic builds
- Operational, compliance, and rollout constraints

## Outputs
- Hardened Dockerfile review checklist
- Decision log for image build efficiency, security posture, and deterministic builds
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for image build efficiency, security posture, and deterministic builds.
2. Produce options and select an approach for image build efficiency, security posture, and deterministic builds.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using image layer and vulnerability scan evidence.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for image build efficiency, security posture, and deterministic builds are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when image includes avoidable risk or non-deterministic build inputs.
- Escalate when accepted risk exceeds team policy thresholds.
