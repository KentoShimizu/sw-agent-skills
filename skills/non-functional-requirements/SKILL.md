---
name: non-functional-requirements
description: "Quality attribute specification workflow after functional requirements are defined. Use when approved functional requirements need measurable performance/reliability/security/operability/compliance targets before implementation planning; do not use for initial requirement elicitation or sprint task breakdown."
---

# Non Functional Requirements

## Overview
Use this skill to define measurable quality constraints that are enforceable before release.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- NFR threshold definition rules:
  - `references/nfr-threshold-definition-rules.md`

## Templates And Assets
- NFR specification template:
  - `assets/nfr-spec-template.csv`
- NFR observability mapping template:
  - `assets/nfr-observability-mapping-template.md`

## Inputs To Gather
- Approved functional requirement baseline.
- Workload assumptions and operating context.
- Security/legal/compliance obligations.
- Existing telemetry and operational response capabilities.

## Deliverables
- Measurable NFR set with owners and linked requirements.
- Signal/alert/runbook mapping for release-blocking NFRs.
- Threshold rationale and escalation policy.

## Workflow
1. Define NFR set with `assets/nfr-spec-template.csv`.
2. Apply threshold rules from `references/nfr-threshold-definition-rules.md`.
3. Map each NFR to telemetry and runbooks via `assets/nfr-observability-mapping-template.md`.
4. Mark release-blocking NFRs and owner accountability.
5. Publish review-ready NFR baseline.

## Quality Standard
- Every NFR is measurable with unit, threshold, and owner.
- Release-blocking NFRs are observable in production.
- Threshold choices reflect user/business risk.

## Failure Conditions
- Stop when NFRs are qualitative and non-measurable.
- Stop when required telemetry/runbook coverage is missing.
- Escalate when legal/compliance constraints cannot be operationalized.
