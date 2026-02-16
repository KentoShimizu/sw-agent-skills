---
name: schema-evolution-governance
description: "Data schema evolution governance workflow for safe forward migration, compatibility control, and rollback readiness in operated systems. Trigger when shared schemas used by multiple services/consumers are changing and compatibility policy, migration sequencing, and fallback strategy must be governed end-to-end; do not use for isolated query micro-optimizations without schema lifecycle impact."
---

# Schema Evolution Governance

## Trigger Boundary
- Use when schema changes affect multiple services or historical data compatibility.
- Do not use for one-off query tuning; use `db-query-optimization`.
- Do not use for API consumer contract tests only; use `api-contract-testing`.

## Goal
Evolve schemas safely without breaking data integrity or dependent systems.

## Inputs
- Current schema and migration history
- Dependent services, jobs, and consumer contracts
- Data volume, retention, and rollback constraints

## Outputs
- Compatibility-aware schema change plan
- Migration sequence with validation checkpoints
- Rollback and recovery readiness criteria

## Workflow
1. Classify change type and compatibility impact.
2. Define phased migration strategy for operated systems.
3. Validate read/write compatibility across dependent systems.
4. Define rollback trigger, data recovery, and cutover criteria.
5. Publish execution and verification checklist.

## Quality Gates
- Compatibility impact is explicitly documented.
- Migration and rollback paths are both testable.
- Data integrity checks pass before and after cutover.
- Ownership exists for every migration phase.

## Failure Handling
- Stop when backward/forward compatibility is unverified.
- Escalate when rollback path is missing for operated systems.
