---
name: db-replication-sharding
description: "Replication and sharding workflow for scaling read/write throughput while managing consistency, failover, and data distribution risk. Use when single-node limits are reached or resilience requires topology changes; do not use for local query tuning only."
---

# DB Replication Sharding

## Overview
Use this skill to design data topology that scales safely without hiding consistency and operability costs.

## Scope Boundaries
- Throughput, storage, or availability limits exceed single-instance capacity.
- Read/write scaling requires replication or partitioning.
- Regional or tenant growth pressures topology redesign.

## Core Judgments
- Replication mode and consistency expectations for read paths.
- Shard key strategy and future rebalancing feasibility.
- Cross-shard query/transaction requirements.
- Failover behavior and recovery-time expectations.

## Practitioner Heuristics
- Choose shard keys by access locality and growth distribution, not by convenience.
- Read replicas are eventually consistent systems; classify which reads can tolerate lag.
- Cross-shard joins and transactions should be exceptions with explicit ownership.
- Topology decisions must include operational playbooks for failover and rebalancing.

## Workflow
1. Profile read/write distribution and growth projections.
2. Select replication topology by availability and consistency needs.
3. Evaluate shard key candidates and hotspot risk.
4. Design routing, rebalancing, and failover behavior.
5. Define application-level behaviors for lag, split-brain prevention, and retries.
6. Document expansion path and de-risking milestones.

## Common Failure Modes
- Shard key creates unbounded hotspots as tenants grow.
- Replica lag assumptions leak into business-critical reads.
- Rebalancing is planned as manual emergency work only.

## Failure Conditions
- Stop when shard key cannot support projected growth distribution.
- Stop when consistency expectations contradict selected topology.
- Escalate when failover and rebalancing are operationally infeasible.
