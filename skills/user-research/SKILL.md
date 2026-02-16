---
name: user-research
description: End-user behavior research workflow for validating user needs and pain points. Trigger when product decisions need evidence from representative end users and assumptions must be validated through interviews, tests, or usage evidence; do not use for internal stakeholder policy or governance decisions.
---

# User Research

## Trigger Boundary
- Use when user behavior evidence is required to validate product assumptions.
- Do not use for internal policy constraints; use `stakeholder-interview`.
- Do not use to finalize requirement wording; hand off to `requirements-definition`.

## Goal
Produce evidence-backed user insights that improve requirement quality and priority.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Research hypotheses and decision questions
- Target segments and recruitment criteria
- Existing analytics and support signals

## Outputs
- `UR-*` session records and synthesized insights
- Evidence links (`EVD-*`) backing findings
- Requirement implications and confidence levels

## Workflow
1. Define decision-linked research questions and success criteria.
2. Select method aligned to risk, timeline, and evidence gap.
3. Recruit representative participants and document sampling risk.
4. Capture structured observations and assign `UR-*` / `EVD-*` IDs.
5. Synthesize insights and map implications to `REQ-*` candidates.

## Quality Gates
- Findings are traceable to auditable evidence IDs.
- Sample limitations and confidence levels are explicit.
- Sensitive data is protected in all shared artifacts.
- Requirement implications are clearly linked and testable.

## Failure Handling
- Reject conclusions from non-representative or underpowered samples.
- Stop publication when consent, retention, or access controls are undefined.
