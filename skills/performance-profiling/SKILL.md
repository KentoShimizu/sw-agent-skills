---
name: performance-profiling
description: Specialized workflow for CPU, memory, and I/O hotspot identification and optimization guidance. Use when throughput, latency, or resource-efficiency bottlenecks must be measured and mitigated; do not use for non-performance functional acceptance decisions.
---

# Performance Profiling

## Trigger Boundary
- Use when latency, throughput, or resource saturation must be measured and improved.
- Do not use for product roadmap prioritization; use `project-estimation` or `technical-roadmapping`.
- Do not use for compliance control reviews alone; use `security-*`.

## Goal
Improve system performance with measurable and sustainable gains.

## Inputs
- Change scope and risk profile
- Domain evidence for CPU, memory, and I/O hotspot identification and optimization guidance
- Operational, compliance, and rollout constraints

## Outputs
- Profiling report with prioritized hotspots
- Decision log for CPU, memory, and I/O hotspot identification and optimization guidance
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for CPU, memory, and I/O hotspot identification and optimization guidance.
2. Produce options and select an approach for CPU, memory, and I/O hotspot identification and optimization guidance.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using before/after profiling comparison.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for CPU, memory, and I/O hotspot identification and optimization guidance are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when hotspots are identified but not attributable to concrete code paths.
- Escalate when accepted risk exceeds team policy thresholds.
