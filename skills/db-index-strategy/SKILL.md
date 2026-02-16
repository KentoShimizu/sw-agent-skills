---
name: db-index-strategy
description: "Design index strategy for critical read/write access paths using query patterns and update cost constraints. Use when query latency or scan amplification depends on index choices and tradeoffs must be explicit; do not use for high-level conceptual modeling."
---

# DB Index Strategy

## Overview
Use this skill to choose indexes that improve real workload performance without unacceptable write amplification.

## Inputs To Gather
- Top slow/high-frequency queries with predicates and sort patterns.
- Current execution plans and scan/selectivity metrics.
- Write volume and mutation cost tolerance.
- Cardinality and data distribution characteristics.

## Deliverables
- Index plan (new/changed/dropped indexes) with rationale.
- Expected plan changes for critical queries.
- Write-impact assessment and storage overhead estimate.
- Verification checklist for post-change performance.

## Quick Example
- Query: `WHERE tenant_id = ? AND created_at >= ? ORDER BY created_at DESC LIMIT 50`.
- Candidate index: `(tenant_id, created_at DESC)`.
- Rejection rationale: single-column `created_at` index causes tenant-wide scan.

## Quality Standard
- Each index maps to one or more concrete query patterns.
- Column order matches filter/sort usage, not guesswork.
- Redundant/unused indexes are identified for cleanup.
- Write and storage impact are assessed before rollout.

## Workflow
1. Rank critical queries by frequency and impact.
2. Analyze plans and identify access-path bottlenecks.
3. Propose index candidates with expected plan effects.
4. Assess write/storage tradeoffs and redundancy.
5. Validate with explain/analyze and workload sampling.

## Failure Conditions
- Stop when index choice is not tied to a concrete query path.
- Stop when write amplification risk is unbounded.
- Escalate when plan stability remains poor after candidate evaluation.
