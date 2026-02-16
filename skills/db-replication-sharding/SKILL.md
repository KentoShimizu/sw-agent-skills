---
name: db-replication-sharding
description: "Design replication topology and sharding strategy with explicit consistency, failover, and rebalancing policies. Use when scale, availability, or geo-distribution requires multi-node data architecture decisions; do not use for single-instance query micro-optimization."
---

# DB Replication Sharding

## Overview
Use this skill to choose replication and sharding patterns that scale safely without hidden consistency failures.

## Inputs To Gather
- Availability and latency targets by region/tenant.
- Read/write distribution and growth trajectory.
- Consistency requirements (strong/eventual/per-operation).
- Failover and operational maturity constraints.

## Deliverables
- Replication topology and consistency policy.
- Shard key strategy and rebalancing approach.
- Failure/failover behavior expectations.
- Operational checklist for lag, split-brain, hotspot, and rebalance risk.

## Quick Example
- Multi-tenant SaaS with uneven tenant sizes:
  - initial shard key: `tenant_id`.
  - hotspot mitigation: heavy-tenant isolation plan.
  - replication: primary + read replicas with lag guardrails.
  - failover: promote replica only when lag < threshold.

## Quality Standard
- Topology matches consistency and latency requirements.
- Shard key avoids predictable hotspotting under projected growth.
- Failover policy is explicit and tested.
- Rebalancing/migration plan minimizes customer impact.

## Workflow
1. Define consistency and availability requirements.
2. Evaluate replication and shard strategy options.
3. Choose topology with explicit tradeoffs.
4. Define failover, lag handling, and rebalance procedures.
5. Validate with failure simulations and load distribution tests.

## Failure Conditions
- Stop when consistency expectations conflict with selected topology.
- Stop when shard key cannot scale without hotspot collapse.
- Escalate when failover behavior is undefined or untested.
