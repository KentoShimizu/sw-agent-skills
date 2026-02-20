---
name: security-secrets-management
description: "Security workflow for secret inventory, storage, distribution, rotation, and auditability controls. Use when API keys, credentials, certificates, or signing secrets lifecycle decisions are required; do not use for generic config management that excludes sensitive material."
---

# Security Secrets Management

## Overview
Use this skill to prevent secret exposure and ensure secrets remain manageable throughout their lifecycle.

## Scope Boundaries
- New secrets are introduced or existing secrets are rotated/migrated.
- Secret storage and runtime distribution mechanisms are being designed.
- Secret exposure response and revocation capability need verification.

## Templates And Assets
- Secrets inventory template:
  - `assets/secrets-inventory-template.csv`

## Inputs To Gather
- Secret inventory by owner, purpose, and environment.
- Storage and access architecture (vault/KMS/secret manager, runtime injection path).
- Rotation cadence, revocation requirements, and dependency constraints.
- Audit and compliance obligations for access and change tracking.

## Deliverables
- Secret lifecycle policy covering creation, storage, usage, rotation, and retirement.
- Access control model with least-privilege and break-glass constraints.
- Rotation runbook with rehearsal and rollback guidance.
- Detection and response playbook for secret leakage events.

## Workflow
1. Build/refresh secret inventory with `assets/secrets-inventory-template.csv`.
2. Enforce non-hardcoded secret policy across source, CI, build artifacts, and logs.
3. Choose distribution model (pull, sidecar, env injection, runtime fetch) based on blast radius and operability.
4. Define rotation strategy by secret type, including coordinated client update order.
5. Implement auditing for secret reads, writes, and policy changes.
6. Rehearse emergency rotation and revoke compromised credentials end-to-end.
7. Verify decommissioned secrets cannot still authenticate.

## Quality Standard
- Every secret has a clear owner and rotation/revocation process.
- Runtime access is identity-bound and minimally scoped.
- Secret exposure can be detected and remediated quickly.
- Audit trails support incident and compliance investigations.

## Failure Conditions
- Stop when any production secret is stored in plaintext repositories.
- Stop when rotation cannot be executed without prolonged outage.
- Escalate when secret access is unaudited or broadly shared.
