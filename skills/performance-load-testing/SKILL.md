---
name: performance-load-testing
description: Specialized workflow for load profile realism, bottleneck detection, and saturation behavior. Trigger when systems need realistic load/stress validation against throughput and latency targets and teams must identify saturation points before rollout; do not use for non-performance functional acceptance decisions.
---

# Performance Load Testing

## Trigger Boundary
- Use when latency, throughput, or resource saturation must be measured and improved.
- Do not use for product roadmap prioritization; use `project-estimation` or `technical-roadmapping`.
- Do not use for compliance control reviews alone; use `security-*`.

## Goal
Improve system performance with measurable and sustainable gains.

## Inputs
- Change scope and risk profile
- Domain evidence for load profile realism, bottleneck detection, and saturation behavior
- Operational, compliance, and rollout constraints

## Outputs
- Load test plan with target workload profiles
- Decision log for load profile realism, bottleneck detection, and saturation behavior
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for load profile realism, bottleneck detection, and saturation behavior.
2. Produce options and select an approach for load profile realism, bottleneck detection, and saturation behavior.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using load-test execution and bottleneck evidence.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for load profile realism, bottleneck detection, and saturation behavior are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when load test does not cover production-critical traffic patterns.
- Escalate when accepted risk exceeds team policy thresholds.
