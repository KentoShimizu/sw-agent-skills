---
name: mlops-model-serving
description: "MLOps model serving workflow for serving topology, latency SLOs, and safe rollout controls. Use when deploying ML models to production serving paths with explicit reliability and rollback requirements; do not use for model-architecture research decisions."
---

# Mlops Model Serving

## Overview
Use this skill to deploy models with predictable latency/error behavior and controlled rollout risk.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Serving SLO and rollout rules:
  - `references/serving-slo-and-rollout-rules.md`

## Templates And Assets
- Serving readiness checklist:
  - `assets/serving-readiness-checklist.md`

## Inputs To Gather
- Serving topology and traffic profile.
- Latency/error SLO and error budget constraints.
- Rollout strategy and rollback capability.
- Observability and incident response expectations.

## Deliverables
- Serving architecture and rollout plan.
- SLO-aligned guardrails and alert thresholds.
- Readiness evidence and rollback criteria.

## Workflow
1. Define serving constraints and topology.
2. Apply `references/serving-slo-and-rollout-rules.md` for rollout policy.
3. Validate readiness with `assets/serving-readiness-checklist.md`.
4. Execute staged rollout and monitor guardrails.
5. Publish serving decision and residual risk ownership.

## Quality Standard
- Serving SLOs are measurable and enforced.
- Rollout blast radius is controlled.
- Rollback decisions are objective and fast.

## Failure Conditions
- Stop when serving cannot meet latency/reliability targets.
- Stop when rollback path is unverified.
- Escalate when rollout risk exceeds policy thresholds.
