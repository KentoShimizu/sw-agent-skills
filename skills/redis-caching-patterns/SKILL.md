---
name: redis-caching-patterns
description: "Redis caching workflow for application performance. Use when framework-specific application structure and runtime behavior must be implemented or revised; do not use for repository-wide architecture governance or release management policy."
---

# Redis Caching Patterns

## Trigger Boundary
- Use when Redis is introduced or tuned for cache/session/queue-like workloads.
- Do not use for primary relational schema design.
- Do not use for in-memory caching that does not involve Redis.

## Goal
Improve latency and throughput with explicit cache correctness and invalidation policy.

## Inputs
- Target read/write hotspots and latency objectives
- Data freshness and consistency requirements
- Eviction policy and memory constraints

## Outputs
- Key namespace and TTL strategy
- Cache invalidation and degradation behavior plan
- Observability checklist for hit rate, memory, and evictions

## Workflow
1. Identify cache candidates by read amplification and recomputation cost.
2. Design key schema with clear namespace and versioning.
3. Define TTL, invalidation triggers, and stale-read tolerance.
4. Add protection against cache stampede and hot-key concentration.
5. Monitor hit rate, latency, and eviction behavior to iterate policy.

## Quality Gates
- Key naming and ownership are consistent across services.
- Invalidation strategy matches freshness requirements.
- Cache failures do not silently corrupt correctness expectations.
- Metrics allow quick detection of cache regressions.

## Failure Handling
- Stop when invalidation policy cannot guarantee correctness bounds.
- Escalate when cache behavior increases tail latency or error rates.
