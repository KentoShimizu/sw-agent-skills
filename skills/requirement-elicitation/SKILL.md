---
name: requirement-elicitation
description: Evidence gathering workflow before requirement writing. Trigger when requirement inputs are incomplete and teams must collect, reconcile, and structure evidence from stakeholders, artifacts, and constraints before drafting formal requirements; do not use for formal baseline synthesis, which belongs to requirements-definition.
---

# Requirement Elicitation

## Trigger Boundary
- Use when requirements are not yet explicit and evidence must be gathered.
- Do not use to finalize canonical requirement wording; use `requirements-definition`.
- Do not use to rank release scope; use `requirement-prioritization`.

## Goal
Collect high-confidence requirement inputs with provenance and conflict visibility.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Stakeholder list and decision map
- Existing docs, tickets, incident records, and analytics
- Initial hypotheses and known constraint areas

## Outputs
- Requirement candidates with confidence and source IDs
- Conflict list and dependency findings
- Prioritized clarification questions

## Workflow
1. Define evidence targets by uncertainty and business impact.
2. Gather signals from interviews, documents, and system artifacts.
3. Register findings with `INT-*`, `UR-*`, or `EVD-*` IDs.
4. Classify findings as requirement, constraint, assumption, or unknown.
5. Deduplicate terms and normalize vocabulary before handoff.

## Quality Gates
- Every candidate has an auditable source ID.
- Contradictions are documented, not merged silently.
- Unknowns are prioritized by delivery risk.
- Personal data handling controls are defined before circulation.

## Failure Handling
- Re-run collection when findings rely on single weak sources.
- Stop when lawful basis or retention policy is undefined for collected data.
