---
name: privacy-by-design
description: "Privacy-by-design workflow for embedding data minimization, lawful basis, and user-rights readiness into feature and UX design decisions. Use when privacy controls must be embedded in product and UX decisions before implementation; do not use for narrow infrastructure tuning that does not affect personal-data handling."
---

# Privacy By Design

## Trigger Boundary
- Use when user data is collected, transformed, or exposed by a feature.
- Do not use for low-level vulnerability triage only; use `security-*`.
- Do not use for post-incident retrospective artifacts; use `incident-postmortem`.

## Goal
Make privacy controls explicit and enforceable before implementation.

## Inputs
- Feature scope and data-flow summary
- Data categories, storage paths, and transfer boundaries
- Regulatory obligations for US, Japan, and EU markets

## Outputs
- Privacy control matrix with ownership
- Data minimization and retention decisions
- User-rights and consent handling requirements

## Workflow
1. Map data lifecycle from collection to deletion.
2. Define lawful basis and consent handling rules.
3. Minimize collected data and remove unnecessary identifiers.
4. Define retention, deletion, and access-control policies.
5. Validate cross-border transfer and audit requirements.

## Quality Gates
- Every personal data element has explicit purpose and lawful basis.
- Retention/deletion behavior is defined and testable.
- User-rights request flow is operationally feasible.
- Required privacy approvals are documented.

## Failure Handling
- Stop when lawful basis or purpose limitation is undefined.
- Escalate when cross-border transfer safeguards are missing.
