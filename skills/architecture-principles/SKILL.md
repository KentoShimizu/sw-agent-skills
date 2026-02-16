---
name: architecture-principles
description: "Architecture principle and guardrail definition before selecting concrete topology. Trigger when teams have competing architecture proposals and need explicit decision principles, constraints, and review guardrails before choosing any concrete pattern; do not use to choose one implementation pattern without principle alignment."
---

# Architecture Principles

## Trigger Boundary
- Use when architecture drivers are known but principles and guardrails are undefined.
- Do not use to choose between concrete architecture options; use `architecture-tradeoff-analysis`.
- Do not use to document finalized decisions; use `architecture-decision-records`.

## Goal
Define stable architecture principles that guide consistent decisions across teams.

## Shared Architecture Contract (Canonical)
- Use `skills/architecture-principles/references/architecture-governance-contract.md` as the only schema source.
- Validate all IDs, lifecycle states, and gate rules against the canonical contract.
- Run machine validation: `python3 skills/architecture-principles/scripts/validate_architecture_contract.py --manifest <path/to/manifest.json>`.
- Block host-specific path leakage with `python3 scripts/validate_no_absolute_paths.py`.
- Start from valid samples when drafting manifests:
  - `skills/architecture-principles/references/samples/arc-prn-manifest.valid.json`
  - `skills/architecture-principles/references/samples/arc-cmp-manifest.valid.json`
- Use the field-level guidance reference:
  - `skills/architecture-principles/references/manifest-field-guide.md`
- Do not define local ID formats or alternate state machines.

## Compliance & Governance Baseline (US, Japan, EU)
- Encode privacy, security, residency, and transfer constraints as explicit principles.
- Treat legal obligations as hard architecture constraints.
- Prepare an `ARC-CMP-*` evidence package for review.

## Inputs
- Business goals and quality attribute priorities
- Regulatory and security constraints
- Team topology and operational constraints

## Outputs
- Principle catalog with rationale and anti-patterns
- Guardrail checklist for design reviews
- Open principle conflicts and decision owners

## Workflow
1. Translate business goals into measurable architecture drivers.
2. Draft principles with rationale, tradeoffs, and scope.
3. Define anti-pattern examples for each principle.
4. Convert principles into reviewable guardrail checks.
5. Resolve conflicts and assign owners for future revisions.

## Quality Gates
- Every principle is testable in architecture review.
- Principle set contains no unresolved contradictions.
- `ARC-CMP-*` evidence package exists and is complete.
- Required approvers are assigned according to the contract.

## Failure Handling
- Stop when principles are vague or not reviewable.
- Stop when canonical contract validation fails.
- Escalate when mandatory legal constraints conflict with product goals.
