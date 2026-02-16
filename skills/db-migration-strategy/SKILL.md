---
name: db-migration-strategy
description: "Plan safe schema and data migrations with rollout sequencing, backfill controls, and rollback viability. Use when database changes must ship without service disruption across versions; do not use for first-pass conceptual schema modeling."
---

# DB Migration Strategy

## Overview
Use this skill to design migration sequences that remain safe under rolling deployments and partial-version coexistence.

## Inputs To Gather
- Current and target schema versions.
- Application rollout model (rolling, blue/green, canary).
- Data volume and backfill cost.
- Downtime tolerance and rollback constraints.

## Deliverables
- Migration sequence (expand -> migrate/backfill -> contract).
- Compatibility matrix by app version and schema state.
- Backfill execution/monitoring plan.
- Rollback strategy and decision triggers.

## Quick Example
- Add non-null column:
  1. Add nullable column with default handling in code.
  2. Deploy app that writes both old/new fields.
  3. Backfill historical rows in batches.
  4. Enforce non-null constraint.
  5. Remove old field usage after full cutover.

## Quality Standard
- Sequence avoids breaking running old/new versions.
- Backfill is throttled, observable, and resumable.
- Contract phase occurs only after compatibility is proven.
- Rollback path is tested for each irreversible step.

## Workflow
1. Classify migration risk and compatibility constraints.
2. Design phased sequence with explicit guardrails.
3. Define backfill strategy (batch size, throttling, retries).
4. Validate sequence in staging with production-like scale.
5. Execute progressively with rollback checkpoints.

## Failure Conditions
- Stop when migration step is not backward/forward compatible as required.
- Stop when rollback path is undefined for high-risk phase.
- Escalate when backfill duration threatens release windows or SLOs.
