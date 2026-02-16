---
name: ux-research-synthesis
description: "UX research synthesis workflow for translating qualitative and quantitative findings into prioritized design actions. Trigger when UX research data from multiple sources must be synthesized into prioritized insights, patterns, and action plans for product/design decisions; do not use for backend data-model or deployment pipeline decisions."
---

# UX Research Synthesis

## Trigger Boundary
- Use when research data exists but design implications are unclear.
- Do not use for running stakeholder interviews; use `stakeholder-interview`.
- Do not use for direct interface handoff packaging; use `figma-handoff`.

## Goal
Turn research evidence into high-confidence, actionable design direction.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Research transcripts, notes, analytics, and observations
- Product goals and known design hypotheses
- Segment definitions and sampling limitations

## Outputs
- Synthesized findings package with project-defined ID (example: `UX-RSR-*` when no existing policy is available)
- Prioritized design implications and risk notes
- Confidence level and evidence traceability map
- Privacy evidence package when personal data handling or policy requires it

## Workflow
1. Normalize research inputs and remove duplicate signals.
2. Cluster findings by user goal and failure pattern.
3. Distinguish observed facts from hypotheses.
4. Map findings to design implications and priority.
5. Publish synthesis with confidence, limitations, and privacy evidence.

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Every implication links back to evidence.
- Confidence level and sampling limits are explicit.
- Contradictory signals are surfaced, not hidden.
- Policy-required approvers and privacy controls are explicitly recorded.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Stop when evidence traceability is missing.
- Stop when policy-required approvers are missing.
- Escalate when synthesis relies on non-representative samples.
