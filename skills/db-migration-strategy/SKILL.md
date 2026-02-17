---
name: db-migration-strategy
description: "Schema migration strategy workflow for sequencing changes, compatibility windows, and rollback-safe rollout in live systems. Use when schema evolution impacts running services; do not use for static greenfield schemas without deployment constraints."
---

# DB Migration Strategy

## Overview
Use this skill to evolve schemas in production without service disruption or hidden data corruption.

## Scope Boundaries
- Schema changes affect live read/write paths.
- Multiple service versions must coexist during rollout.
- Data backfill or contract transition is required.

## Core Judgments
- Migration pattern: expand-contract, dual-write, shadow-read, or phased cutover.
- Compatibility window duration and supported versions.
- Backfill approach and execution safety.
- Rollback semantics and data reconciliation strategy.

## Practitioner Heuristics
- Prefer additive/compatible changes before destructive cleanup.
- Separate schema deployment from application behavior switch.
- Dual-write without reconciliation plan is a corruption risk.
- Large backfills need throttling and progress observability tied to business impact.

## Workflow
1. Define change classes: additive, transitional, destructive.
2. Sequence schema and application releases for compatibility.
3. Plan data migration/backfill and failure handling.
4. Define cutover trigger and rollback decision points.
5. Execute deprecation/removal only after compatibility window closes.
6. Document residual migration debt and retirement deadlines.

## Common Failure Modes
- Breaking changes shipped before all consumers are updated.
- Backfill jobs compete with production traffic and cause incidents.
- Rollback plan restores code but not data semantics.

## Failure Conditions
- Stop when compatibility window cannot be supported operationally.
- Stop when rollback semantics for migrated data are undefined.
- Escalate when migration risk exceeds release risk tolerance.
