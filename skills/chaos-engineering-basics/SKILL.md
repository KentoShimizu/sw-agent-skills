---
name: chaos-engineering-basics
description: "Design and execute controlled chaos experiments to validate resilience assumptions with explicit steady-state metrics, blast-radius limits, and abort rules. Use when reliability claims need evidence before wider rollout; do not use for active incident command or postmortem-only reporting."
---

# Chaos Engineering Basics

## Overview
Use this skill to design safe, evidence-driven fault injection experiments that verify system resilience under realistic failure conditions.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Inputs To Gather
- Critical user journeys and service dependency map.
- Current SLI/SLO and alert signal quality.
- Failure budget, allowed blast radius, and rollback authority.
- Existing runbooks and on-call escalation paths.

## Deliverables
- Experiment charter (hypothesis, steady state, blast radius, abort criteria).
- Fault-injection plan (what fails, where, for how long, at what traffic share).
- Observation plan (metrics, logs, traces, and decision thresholds).
- Findings with remediation owners and re-test schedule.

## Quick Start Example

### Example experiment charter
- Hypothesis: "API p95 remains < 400ms when one cache node fails."
- Steady-state metrics: p95 latency, error rate, queue depth.
- Blast radius: 5% traffic, one AZ only, 10 minutes max.
- Abort immediately if:
  - error rate > 2x baseline for 3 minutes,
  - user checkout success drops below threshold,
  - paging alerts fire in unrelated services.

### Example decision rule
- `pass`: steady-state metrics remain inside pre-registered limits.
- `fail`: any hard guardrail breaches abort threshold.
- `inconclusive`: observability gaps prevent causal interpretation.

## Quality Standard
- Steady state is measurable and agreed before injection.
- Abort/rollback conditions are explicit and executable.
- Blast radius is bounded by environment, traffic, and time.
- Experiment outcomes produce owned remediation actions.
- Re-test conditions are defined for failed assumptions.

## Workflow
1. Select one reliability assumption tied to a business-critical flow.
2. Define steady-state metrics and hard guardrails.
3. Design smallest useful fault experiment with bounded blast radius.
4. Run experiment under live observation with explicit abort authority.
5. Classify result (pass/fail/inconclusive) and capture learning.
6. Assign remediation and schedule follow-up verification.

## Failure Conditions
- Stop when steady-state metric or abort threshold is undefined.
- Stop when observability cannot detect degradation quickly.
- Escalate when proposed blast radius exceeds approved risk budget.
