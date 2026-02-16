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

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, evidence handling, privacy handling, and artifact lifecycle.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Research hypotheses and decision questions
- Target segments and recruitment criteria
- Existing analytics and support signals

## Outputs
- Session records and synthesized insights with project-defined IDs (examples: `UR-*`, `EVD-*` when no existing policy is available)
- Evidence links backing findings
- Requirement implications and confidence levels

## Workflow
1. Define decision-linked research questions and success criteria.
2. Select method aligned to risk, timeline, and evidence gap.
3. Recruit representative participants and document sampling risk.
4. Capture structured observations and assign project-defined IDs.
5. Synthesize insights and map implications to project-defined requirement candidates (example: `REQ-*`).

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Findings are traceable to auditable evidence IDs.
- Sample limitations and confidence levels are explicit.
- Sensitive data is protected in all shared artifacts.
- Requirement implications are clearly linked and testable.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Reject conclusions from non-representative or underpowered samples.
- Stop publication when consent, retention, or access controls are undefined.
