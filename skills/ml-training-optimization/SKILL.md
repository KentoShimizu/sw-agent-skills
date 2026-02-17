---
name: ml-training-optimization
description: "ML training optimization workflow for convergence stability, efficiency, and cost control. Use when training runs are slow, unstable, or over budget and optimization decisions are required; do not use for generic API-layer or infrastructure-only changes."
---

# Ml Training Optimization

## Overview
Use this skill to improve training throughput and cost while preserving model quality and stability.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Convergence and budget rules:
  - `references/convergence-and-budget-rules.md`

## Templates And Assets
- Training optimization plan:
  - `assets/training-optimization-plan-template.md`

## Inputs To Gather
- Baseline runtime/cost/convergence behavior.
- Resource constraints and training budget.
- Quality guardrails to prevent regressions.
- Candidate optimization levers (data, algorithm, infra).

## Deliverables
- Optimization plan with prioritized interventions.
- Resource and convergence validation results.
- Cost/quality trade-off report.

## Workflow
1. Capture baseline and bottlenecks in `assets/training-optimization-plan-template.md`.
2. Apply `references/convergence-and-budget-rules.md` to bound risk.
3. Run targeted optimizations with controlled experiments.
4. Validate quality guardrails and budget impact.
5. Publish adopted changes and rollback criteria.

## Quality Standard
- Optimization decisions preserve target quality.
- Convergence behavior remains stable.
- Cost and runtime improvements are measurable.

## Failure Conditions
- Stop when optimization degrades quality beyond guardrails.
- Stop when instability increases despite speed gains.
- Escalate when budget constraints remain unmet.
