---
name: architecture-decision-records
description: "Capture high-impact architecture decisions as ADRs with rationale, alternatives, consequences, and lifecycle status. Use when a decision changes risk, cost, ownership, or reliability posture."
---

# Architecture Decision Records

## Overview
Use this skill to produce ADRs that make architecture decisions traceable and maintainable over time. ADRs are decision artifacts, not brainstorming notes.

## Inputs To Gather
- Decision statement and scope.
- Options considered and supporting evidence.
- Constraints, risks, approvals.
- Related incidents, diagrams, and requirements.

## Deliverables
- ADR document with lifecycle status.
- Explicit rationale for accepted and rejected options.
- Consequences and follow-up actions.
- Links to superseded or related ADRs.

## Quality Standard
- Context, decision, alternatives, consequences, and status are complete.
- Rationale is evidence-based, not preference-based.
- Operational impact and ownership are explicit.
- Re-decision triggers are defined.
- Supersession chain remains navigable.

## Workflow
1. Capture context, constraints, and decision scope.
2. Summarize alternatives with tradeoff evidence.
3. Record decision and concrete consequences.
4. Set status, owner, and approvals.
5. Link follow-ups and future re-decision triggers.

## Failure Conditions
- Stop when rationale lacks evidence.
- Stop when status or ownership is missing.
- Escalate when high-impact decisions bypass ADR capture.
