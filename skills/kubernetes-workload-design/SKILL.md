---
name: kubernetes-workload-design
description: "Kubernetes workload design workflow for resource sizing, autoscaling behavior, and safe rollout strategy. Use when workload specs need concrete sizing and resilience decisions to meet reliability/performance targets; do not use for API contract design or requirement prioritization."
---

# Kubernetes Workload Design

## Overview
Use this skill to design Kubernetes workloads that scale predictably and roll out safely under real traffic behavior.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Autoscaling and rollout decision rules:
  - `references/autoscaling-and-rollout-decision-rules.md`

## Templates And Assets
- Workload sizing template:
  - `assets/workload-sizing-template.md`
- Rollout strategy checklist:
  - `assets/rollout-strategy-checklist.md`

## Inputs To Gather
- Traffic profile and latency/SLO targets.
- CPU/memory/concurrency characteristics.
- Rollout risk tolerance and availability requirements.
- Observability signals for scaling and rollback decisions.

## Deliverables
- Workload sizing and scaling plan.
- Rollout strategy with guardrails and rollback triggers.
- Resilience assumptions and saturation behavior notes.
- Verification plan for load and deployment behavior.

## Workflow
1. Define resource and scaling assumptions in `assets/workload-sizing-template.md`.
2. Choose scaling/rollout strategy using `references/autoscaling-and-rollout-decision-rules.md`.
3. Validate rollout readiness via `assets/rollout-strategy-checklist.md`.
4. Run representative load and rollout verification.
5. Publish residual capacity and rollout risks with owners.

## Quality Standard
- Resource sizing reflects measured workload behavior.
- Autoscaling avoids oscillation and delayed recovery.
- Rollout controls match service criticality.
- Rollback criteria are objective and monitored.

## Failure Conditions
- Stop when workload design lacks safe rollout or capacity guarantees.
- Stop when autoscaling signals do not correlate with user impact.
- Escalate when saturation risk remains unmitigated.
