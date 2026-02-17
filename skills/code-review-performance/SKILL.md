---
name: code-review-performance
description: "Run performance-focused code review when changes may affect latency, throughput, or CPU/memory/I/O efficiency on critical paths. Use for merge decisions requiring explicit performance-risk findings; do not use for broad non-performance review scope."
---

# Code Review Performance

## Overview
Use this skill to detect performance regressions before merge, especially on hot paths and high-traffic execution flows.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Inputs To Gather
- Hot-path endpoints/jobs and current performance budgets.
- Workload assumptions (QPS, payload size, concurrency, data cardinality).
- Existing benchmark/profiling evidence.
- Resource constraints (CPU, memory, I/O, network).

## Deliverables
- Performance findings prioritized by user impact.
- Budget-fit judgment (within budget / at risk / out of budget).
- Required follow-up checks (benchmark, profiling, load test).

## Finding Focus Areas
- Algorithmic growth (`O(n^2)` regressions, repeated scans).
- Allocation pressure and unnecessary object churn.
- I/O amplification (N+1 calls, repeated DB/API access).
- Contention/serialization bottlenecks under concurrency.
- Cache invalidation or cache-bypass risks.

## Quick Example
- Change adds per-item DB call inside loop over 10k records.
- Finding: high-severity throughput risk (N+1 query pattern).
- Fix direction: batch query + in-memory map, verify via benchmark.

## Quality Standard
- Each finding ties to an explicit performance budget or hotspot.
- Recommendations include measurement plan, not assumptions only.
- Risk classification includes expected scale sensitivity.
- Missing evidence (benchmark/profile) is flagged explicitly.

## Workflow
1. Identify changed hot paths and performance-sensitive flows.
2. Analyze algorithmic and resource behavior from diff.
3. Compare expected behavior with existing budgets.
4. Require measurement where uncertainty is material.
5. Publish findings with mitigation and verification steps.

## Failure Conditions
- Stop when high-risk regressions have no mitigation/verification plan.
- Escalate when performance impact cannot be bounded from available evidence.
