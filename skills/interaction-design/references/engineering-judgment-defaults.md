# Engineering Judgment Defaults (Project-First)

## Intent
Use these defaults to emulate professional engineering decision-making when project-specific rules are missing.
If the repository or organization already defines decision policy, use that policy first.

## Decision Protocol
1. Define the decision statement and success metric.
2. List at least two feasible options.
3. Identify hard constraints (compliance, deadlines, compatibility, staffing).
4. Score options using project-defined weights.
5. Recommend one option and record explicit trade-offs.

## Default Scoring Dimensions
Use project-defined dimensions and weights when available.
If missing, start with equal weights across:
- User value impact
- Delivery risk
- Effort and lead time
- Reversibility and rollback cost
- Operational cost (maintenance, support, incident risk)

## Risk Classification
Classify each proposal before sign-off.

- `LOW`: reversible change, limited user impact, fast rollback.
- `MEDIUM`: partial rollback complexity or multi-team coordination risk.
- `HIGH`: difficult rollback, legal/compliance exposure, or broad user impact.

## Execution Gates
- `LOW`: proceed with normal peer review.
- `MEDIUM`: require explicit mitigation and verification plan.
- `HIGH`: require owner escalation, rollback rehearsal, and post-release monitoring plan.

## Uncertainty Management
Always record:
- Assumptions (what is believed to be true)
- Unknowns (what is not verified yet)
- Confidence (`0.0-1.0`) with rationale
- Evidence quality (direct, indirect, stale, missing)

## Output Contract
For major decisions, include these sections in outputs:
- Recommended option
- Alternatives considered
- Trade-offs and rejected risks
- Validation plan (automated/manual)
- Operational safeguards (alerts/logging/runbook)
- Follow-up actions outside current scope

## Escalation Defaults
Escalate when any of the following holds:
- Required data for the decision is missing
- Decision affects legal/privacy/security boundaries
- High-risk irreversible change is proposed
- Cross-team ownership is unresolved

## Anti-Patterns
- Picking one option without alternatives
- Treating project-specific rules as optional
- Hiding uncertainty instead of documenting it
- Optimizing for speed while deferring known high-risk debt
