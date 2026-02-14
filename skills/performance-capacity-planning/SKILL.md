---
name: performance-capacity-planning
description: Specialized workflow for resource forecasting, headroom policy, and growth scenario readiness. Use when throughput, latency, or resource-efficiency bottlenecks must be measured and mitigated; do not use for non-performance functional acceptance decisions.
---

# Performance Capacity Planning

## Trigger Boundary
- Use when latency, throughput, or resource saturation must be measured and improved.
- Do not use for product roadmap prioritization; use `project-estimation` or `technical-roadmapping`.
- Do not use for compliance control reviews alone; use `security-*`.

## Goal
Improve system performance with measurable and sustainable gains.

## Inputs
- Change scope and risk profile
- Domain evidence for resource forecasting, headroom policy, and growth scenario readiness
- Operational, compliance, and rollout constraints

## Outputs
- Capacity planning model and threshold policy
- Decision log for resource forecasting, headroom policy, and growth scenario readiness
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for resource forecasting, headroom policy, and growth scenario readiness.
2. Produce options and select an approach for resource forecasting, headroom policy, and growth scenario readiness.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using traffic-growth simulation against capacity assumptions.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for resource forecasting, headroom policy, and growth scenario readiness are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when capacity plan cannot support forecasted demand.
- Escalate when accepted risk exceeds team policy thresholds.
