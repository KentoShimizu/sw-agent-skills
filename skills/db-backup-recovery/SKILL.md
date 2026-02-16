---
name: db-backup-recovery
description: "Design and verify database backup/restore strategy against explicit RPO/RTO targets. Use when data durability, retention, and disaster recovery readiness must be proven with restore evidence; do not use for query tuning or schema modeling tasks."
---

# DB Backup Recovery

## Overview
Use this skill to ensure backups are not only taken but also restorable within required recovery objectives.

## Inputs To Gather
- RPO/RTO targets by system criticality.
- Data retention/legal constraints.
- Backup mechanisms (snapshot, logical dump, incremental, WAL/binlog).
- Recovery environments and access controls.

## Deliverables
- Backup policy (frequency, retention, encryption, storage locations).
- Restore runbook with role responsibilities.
- Restore-test evidence and objective compliance report.
- Gap list with remediation priorities.

## Quick Example
- Target: `RPO <= 15 min`, `RTO <= 60 min`.
- Plan: nightly full + 5-min incremental log shipping.
- Verification: monthly restore drill to isolated environment; measure actual RPO/RTO.

## Quality Standard
- Backup policy maps directly to RPO/RTO targets.
- Restore process is scripted/runbooked and repeatedly tested.
- Integrity verification includes checksum and application-level sanity checks.
- Access and key-management controls protect backup artifacts.

## Workflow
1. Define recovery objectives and compliance constraints.
2. Select backup pattern and retention schedule.
3. Define restore procedure and required dependencies.
4. Run restore drills and record measured outcomes.
5. Close objective gaps with concrete remediation actions.

## Failure Conditions
- Stop when restore evidence is missing or stale.
- Stop when measured RPO/RTO misses required objectives.
- Escalate when backups are inaccessible, unencrypted, or unverifiable.
