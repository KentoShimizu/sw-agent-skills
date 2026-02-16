---
name: stakeholder-interview
description: Internal decision-maker interview workflow for constraints and policy capture. Trigger when requirement progress is blocked by missing decisions from business, engineering, legal, or operations stakeholders and structured interviews are needed to extract constraints; do not use for end-user behavior research.
---

# Stakeholder Interview

## Trigger Boundary
- Use when internal decision authority and policy constraints must be clarified.
- Do not use for end-user needs validation; use `user-research`.
- Do not use to finalize requirement baseline; hand off to `requirements-definition`.

## Goal
Capture authoritative internal decisions and constraints with auditable traceability.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Stakeholder map with authority boundaries
- Interview objectives and decision-focused questions
- Existing requirement hypotheses

## Outputs
- `INT-*` interview records with source and authority context
- Confirmed constraints and explicit decision statements
- Conflict list with owner and follow-up date

## Workflow
1. Prioritize interviews by risk and decision criticality.
2. Run structured interviews with role-specific question sets.
3. Record outcomes under `INT-*` IDs with authority tags.
4. Classify statements as fact, policy, assumption, or preference.
5. Send confirmation summary and resolve contradictions.

## Quality Gates
- Each claim has source, authority level, and timestamp.
- Contradictions are escalated with explicit options.
- Personal data is masked in shared notes.
- Follow-up actions have owner and due date.

## Failure Handling
- Re-interview when authority is insufficient for decisions.
- Stop synthesis when lawful basis for stored data is missing.
