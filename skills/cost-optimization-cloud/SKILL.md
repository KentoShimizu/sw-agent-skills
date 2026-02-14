---
name: cost-optimization-cloud
description: "Cloud cost optimization workflow balancing spend, performance, and reliability. Use when cloud spend reduction must be balanced against reliability and performance constraints; do not use for purely functional product behavior design."
---

# Cost Optimization Cloud

## Trigger Boundary
- Use when cloud spend must be reduced without violating SLO or compliance.
- Do not use for one-off performance micro-optimizations; use `performance-*`.
- Do not use for architecture decision history management; use `architecture-decision-records`.

## Goal
Reduce spend while preserving reliability and user outcomes.

## Inputs
- Cost breakdown by service and environment
- Utilization and traffic seasonality data
- Reliability, compliance, and performance constraints

## Outputs
- Prioritized cost optimization actions with impact estimate
- Risk-aware implementation sequence
- Verification plan for savings and regression detection

## Workflow
1. Identify top cost drivers with workload attribution.
2. Propose optimization options and quantify expected impact.
3. Evaluate performance and reliability side effects.
4. Prioritize actions by ROI and implementation risk.
5. Validate savings and monitor for regressions after change.

## Quality Gates
- Savings estimate and confidence are explicit.
- Recommendations preserve reliability and compliance constraints.
- Implementation sequence minimizes blast radius.
- Post-change verification metrics are defined.

## Failure Handling
- Stop when cost actions violate reliability/compliance constraints.
- Escalate when savings estimates lack sufficient evidence.
