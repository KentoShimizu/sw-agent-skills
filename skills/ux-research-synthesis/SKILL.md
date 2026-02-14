---
name: ux-research-synthesis
description: "UX research synthesis workflow for translating qualitative and quantitative findings into prioritized design actions. Use when UX, interaction, visual, or design-governance artifacts are the primary deliverable; do not use for backend data-model or deployment pipeline decisions."
---

# UX Research Synthesis

## Trigger Boundary
- Use when research data exists but design implications are unclear.
- Do not use for running stakeholder interviews; use `stakeholder-interview`.
- Do not use for direct interface handoff packaging; use `figma-handoff`.

## Goal
Turn research evidence into high-confidence, actionable design direction.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Track synthesis packages with `UX-RSR-*` IDs.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Research transcripts, notes, analytics, and observations
- Product goals and known design hypotheses
- Segment definitions and sampling limitations

## Outputs
- Synthesized findings package with `UX-RSR-*` ID
- Prioritized design implications and risk notes
- Confidence level and evidence traceability map
- Privacy evidence package for research handling decisions

## Workflow
1. Normalize research inputs and remove duplicate signals.
2. Cluster findings by user goal and failure pattern.
3. Distinguish observed facts from hypotheses.
4. Map findings to design implications and priority.
5. Publish synthesis with confidence, limitations, and privacy evidence.

## Quality Gates
- Every implication links back to evidence.
- Confidence level and sampling limits are explicit.
- Contradictory signals are surfaced, not hidden.
- Privacy Reviewer approval is always present.
- Contract validation passes including privacy evidence requirements.

## Failure Handling
- Stop when evidence traceability is missing.
- Stop when Privacy Reviewer approval is missing.
- Escalate when synthesis relies on non-representative samples.
