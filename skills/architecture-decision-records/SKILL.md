---
name: architecture-decision-records
description: "Architecture Decision Record authoring and lifecycle governance for significant technical decisions. Use when system boundaries, module relationships, and architecture-level constraints are being defined; do not use for single-module implementation refactors without architecture impact."
---

# Architecture Decision Records

## Trigger Boundary
- Use when a significant architecture decision must be recorded or revised.
- Do not use to evaluate alternatives from scratch; use `architecture-tradeoff-analysis` first.
- Do not use to model runtime structure visually; use `architecture-c4-modeling`.

## Goal
Maintain auditable and current decision history for architecture evolution.

## Shared Architecture Contract (Canonical)
- Use `skills/architecture-principles/references/architecture-governance-contract.md` as the only schema source.
- Validate all IDs, lifecycle states, and gate rules against the canonical contract.
- Do not define local ID formats or alternate state machines.

## Compliance & Governance Baseline (US, Japan, EU)
- Capture compliance and privacy rationale in each relevant ADR.
- Preserve change history and approval traceability for audits.
- Prepare or reference an `ARC-CMP-*` evidence package for each high-impact decision.

## Inputs
- Decision statement and context
- Evaluated options and tradeoff evidence
- Risks, constraints, and stakeholder approvals

## Outputs
- ADR documents with status lifecycle
- Supersession links between related ADRs
- Decision consequences and follow-up actions

## Workflow
1. Create ADR with context, decision, options, and consequences.
2. Reference related drivers, risks, diagrams, and evidence package IDs.
3. Set status: proposed, accepted, rejected, or superseded.
4. Record approvers and decision date.
5. Update or supersede ADR when assumptions change.

## Quality Gates
- Every major decision has an ADR identifier.
- ADR rationale includes rejected options.
- `ARC-CMP-*` evidence package is complete and approved.
- High-impact decisions have required approver matrix.

## Failure Handling
- Stop when decision rationale lacks option evidence.
- Stop when canonical contract validation fails.
- Escalate when high-impact ADRs lack explicit approval ownership.
