---
name: db-query-optimization
description: "Optimize query behavior through rewrites, plan analysis, and access-path adjustments for hot workloads. Use when query latency, throughput, or plan instability blocks SLO targets and concrete query-level fixes are required; do not use for broad schema governance decisions."
---

# DB Query Optimization

## Overview
Use this skill to reduce query cost and stabilize execution plans for high-impact workloads.

## Inputs To Gather
- Problem queries with actual latency/resource data.
- Current execution plans and row-estimation quality.
- Relevant schema/index metadata.
- Workload context (concurrency, parameter distribution, cache effects).

## Deliverables
- Query rewrite and plan-improvement recommendations.
- Root-cause map (scan amplification, bad join order, misestimation, etc.).
- Validation plan with baseline vs post-change metrics.
- Regression watchpoints for future plan drift.

## Quick Example
- Symptom: parameter-sensitive plan regression.
- Fix options: query shape stabilization, statistics refresh, targeted hint/pattern change.
- Verification: p95 latency and buffer reads across representative parameter sets.

## Quality Standard
- Recommendations are rooted in measured plan evidence.
- Optimization preserves functional correctness.
- Parameter variability and data skew are explicitly considered.
- Success criteria include latency and resource metrics.

## Workflow
1. Establish baseline metrics and capture representative plans.
2. Diagnose dominant cost driver per query.
3. Propose rewrite/index/statistics changes.
4. Test across realistic parameter and concurrency ranges.
5. Publish optimized form and monitoring guardrails.

## Failure Conditions
- Stop when no representative workload evidence is available.
- Stop when optimization changes semantics or correctness.
- Escalate when plan instability persists across realistic parameter sets.
