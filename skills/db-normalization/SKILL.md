---
name: db-normalization
description: "Decide normalization level and intentional denormalization boundaries to prevent anomalies while meeting query needs. Use when schema design must balance update integrity against read efficiency; do not use for index-only tuning or query-plan debugging."
---

# DB Normalization

## Overview
Use this skill to remove harmful redundancy first, then introduce denormalization only where justified by measurable read requirements.

## Inputs To Gather
- Current/proposed schema and update workflows.
- Anomaly risks (insert/update/delete anomalies).
- Read-path requirements and latency targets.
- Data freshness tolerance for duplicated fields.

## Deliverables
- Normalization decision record per table group.
- Intentional denormalization list with refresh strategy.
- Integrity controls to protect duplicated data.
- Test cases for anomaly prevention.

## Quick Example
- Normalize `customer_email` out of `orders` to avoid stale duplication.
- Denormalize `order_total_cached` only if read hot path requires it.
- Add refresh rule: update cached total on item mutation transaction.

## Quality Standard
- Normalization choice is driven by anomaly risk and workload evidence.
- Every denormalized field has owner, refresh rule, and staleness policy.
- Integrity checks exist for duplicated business-critical values.
- Tradeoff between write complexity and read latency is explicit.

## Workflow
1. Identify redundancy and anomaly-prone structures.
2. Normalize to remove unsafe duplication.
3. Reintroduce denormalization only for proven hot paths.
4. Define synchronization and consistency safeguards.
5. Validate with anomaly-focused test scenarios.

## Failure Conditions
- Stop when denormalization lacks refresh/consistency strategy.
- Stop when normalization breaks mandatory read-path latency without mitigation.
- Escalate when anomaly risk remains unresolved for critical entities.
