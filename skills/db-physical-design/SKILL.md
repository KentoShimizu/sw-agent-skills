---
name: db-physical-design
description: "Design physical storage layout, partitioning, and engine-specific settings to meet scale and latency objectives. Use when logical schema is stable and runtime behavior depends on storage organization; do not use for conceptual domain modeling or requirement prioritization."
---

# DB Physical Design

## Overview
Use this skill to translate logical schema into engine-aware physical design that sustains target scale.

## Inputs To Gather
- Logical schema and query workload profile.
- Data growth forecast and retention policy.
- Engine capabilities/limits (partitioning, compression, storage classes).
- Backup/recovery and maintenance window constraints.

## Deliverables
- Partitioning and storage layout strategy.
- Hot/cold data placement policy.
- Maintenance strategy (vacuum/reorg/compaction where applicable).
- Capacity-risk plan with growth triggers.

## Quick Example
- Partition large event table by month and tenant key.
- Keep last 90 days on fast storage, archive older partitions to cheaper tier.
- Define partition pruning expectation for key analytics queries.

## Quality Standard
- Layout choices are tied to workload and growth evidence.
- Partition key supports both write distribution and dominant queries.
- Maintenance overhead is budgeted and operationally feasible.
- Recovery objectives remain achievable under chosen layout.

## Workflow
1. Profile workload and growth characteristics.
2. Evaluate storage/partition options supported by engine.
3. Select layout with capacity and performance tradeoffs.
4. Define maintenance and archival operations.
5. Validate expected behavior with representative queries.

## Failure Conditions
- Stop when physical design conflicts with recovery requirements.
- Stop when partitioning strategy cannot avoid hotspotting.
- Escalate when capacity risk exceeds planned expansion horizon.
