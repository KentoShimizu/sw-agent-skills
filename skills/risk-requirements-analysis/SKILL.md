---
name: risk-requirements-analysis
description: "Requirement-level risk analysis before implementation commitment. Use when requirement-level quality attributes or risks must be formalized against existing requirement baselines; do not use for initial requirement elicitation or sprint task breakdown."
---

# Risk Requirements Analysis

## Trigger Boundary
- Use when `REQ-*` baseline exists and commitment risk must be evaluated.
- Do not use for initial requirement discovery; use `requirement-elicitation`.
- Do not use as the sole prioritization method; integrate with `requirement-prioritization`.

## Goal
Quantify requirement risk and define controls before release commitments.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Approved `REQ-*` and `NFR-*`
- Dependency map and delivery timeline
- Incident history and known failure modes

## Outputs
- `RSK-*` register linked to `REQ-*`
- Preventive controls, detection signals, and contingencies
- Residual-risk summary for decision makers

## Workflow
1. Enumerate failure scenarios by requirement and dependency.
2. Score impact, likelihood, and detectability for each scenario.
3. Create `RSK-*` entries and link to affected `REQ-*` IDs.
4. Define mitigation owner and contingency owner per risk.
5. Escalate release-blocking risks with decision deadlines.

## Quality Gates
- Critical `REQ-*` items have explicit risk entries.
- High severity risks have mitigation and contingency ownership.
- Residual risk is visible before release commitment.
- Compliance-related risks are not downgraded without legal sign-off.

## Failure Handling
- Stop when critical risks have no owner or no decision date.
- Stop when compliance risks are accepted without explicit authority.
