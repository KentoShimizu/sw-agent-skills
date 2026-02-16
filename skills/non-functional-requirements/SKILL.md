---
name: non-functional-requirements
description: "Quality attribute specification after functional requirements are defined. Trigger when approved functional requirements need measurable quality targets (performance, reliability, security, operability, compliance) and explicit risk constraints before implementation planning; do not use for initial requirement elicitation or sprint task breakdown."
---

# Non Functional Requirements

## Trigger Boundary
- Use when functional `REQ-*` baseline exists and quality constraints must be formalized.
- Do not use to discover functional scope; use `requirements-definition`.
- Do not use to write pass/fail implementation checks; use `acceptance-criteria-design`.

## Goal
Define measurable quality gates that are enforceable before release.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Approved `REQ-*` baseline
- Workload assumptions and operating context
- Security, legal, and compliance obligations

## Outputs
- `NFR-*` set with metric, threshold, and unit
- Validation method and runtime signal per NFR
- Owner and escalation policy for threshold breaches

## Workflow
1. Enumerate quality attributes relevant to the system context.
2. Create measurable `NFR-*` statements linked to `REQ-*` IDs.
3. Attach workload assumptions and measurement method.
4. Define observability signals, alert conditions, and runbook references.
5. Mark release-blocking NFRs and review with owners.

## Quality Gates
- Every NFR has metric, threshold, unit, and owner.
- Every NFR maps to an observable production signal.
- Jurisdictional obligations are represented as enforceable constraints.
- Runbook link exists for every release-blocking NFR.

## Failure Handling
- Stop when NFRs are qualitative or non-measurable.
- Stop when required telemetry or legal controls are unavailable.
