---
name: performance-capacity-planning
description: "Performance capacity planning workflow for forecasting demand, defining headroom policy, and preventing saturation-related SLO breaches. Use when traffic growth or workload forecasts require explicit capacity and threshold decisions; do not use for non-performance functional acceptance decisions."
---

# Performance Capacity Planning

## Overview
Use this skill to build capacity plans that keep services reliable under growth and peak demand.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Capacity forecast rules:
  - `references/capacity-forecast-rules.md`

## Templates And Assets
- Capacity model template:
  - `assets/capacity-model-template.md`
- Headroom policy template:
  - `assets/headroom-policy-template.md`

## Inputs To Gather
- Current workload profile and growth assumptions.
- SLO/error-budget and availability constraints.
- Scaling mechanics and provisioning lead times.
- Peak-event and failure-mode scenarios.

## Deliverables
- Capacity model with risk-based thresholds.
- Headroom policy by service tier.
- Forecast-driven scaling and escalation plan.

## Workflow
1. Build model in `assets/capacity-model-template.md`.
2. Apply growth/headroom policy via `references/capacity-forecast-rules.md`.
3. Define thresholds and escalation points.
4. Validate against plausible growth and burst scenarios.
5. Publish ownership and review cadence.

## Quality Standard
- Forecast assumptions are explicit and testable.
- Headroom policy aligns with reliability objectives.
- Saturation thresholds trigger actionable responses.

## Failure Conditions
- Stop when plan cannot support forecasted demand.
- Stop when thresholds are non-actionable.
- Escalate when capacity risk exceeds policy tolerance.
