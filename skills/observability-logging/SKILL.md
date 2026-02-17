---
name: observability-logging
description: "Observability logging workflow for structured schema, correlation, and incident triage utility. Use when services need logging standards or revisions for diagnosable incidents; do not use for business-feature implementation logic."
---

# Observability Logging

## Overview
Use this skill to standardize logs so incidents can be diagnosed quickly and safely.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Logging field and retention rules:
  - `references/logging-field-and-retention-rules.md`

## Templates And Assets
- Logging schema template:
  - `assets/logging-schema-template.md`
- Log triage checklist:
  - `assets/log-triage-checklist.md`

## Inputs To Gather
- Incident triage requirements and common failure modes.
- Required correlation fields and security constraints.
- Retention, redaction, and access policy requirements.
- Queryability needs for on-call workflows.

## Deliverables
- Logging schema and policy baseline.
- Redaction/retention controls.
- Triage validation evidence for key incident scenarios.

## Workflow
1. Define schema in `assets/logging-schema-template.md`.
2. Apply retention/redaction policy from `references/logging-field-and-retention-rules.md`.
3. Validate triage utility using `assets/log-triage-checklist.md`.
4. Fix gaps in correlation and error context fields.
5. Publish logging standard and ownership.

## Quality Standard
- Logs contain required triage context and correlation IDs.
- Sensitive data handling is explicit and enforced.
- Retention and access are policy-compliant.

## Failure Conditions
- Stop when logs lack required incident context.
- Stop when sensitive data redaction is not reliable.
- Escalate when logging policy conflicts with compliance requirements.
