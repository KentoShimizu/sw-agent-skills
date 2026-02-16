# Project-Specific Decision Calibration Framework

## Purpose
Use this framework to avoid generic architecture rules that ignore project context.
It defines how to derive no-go checks and threshold values from evidence in the current task.

## Evidence Sources (Mandatory)
Derive every high-impact decision criterion from all available sources:

1. Requirement evidence
- Functional and non-functional requirements
- Compliance and policy constraints
- Service-level objectives and reliability targets

2. Existing implementation evidence
- Current topology, dependencies, and data boundaries
- Incident history, latency profiles, and operational bottlenecks
- Team ownership map and deployment workflow constraints

3. Stakeholder and user-direction evidence
- Explicit direction in the current conversation
- Product, legal, and operations constraints
- Timeline and delivery-risk tolerance

If one source is missing, mark assumptions explicitly and lower decision confidence.

## No-Go Derivation Method
Do not define universal no-go rules. Define project-scoped checks using this format:

- `condition`: Observable condition that blocks an option
- `evidence`: Artifacts proving the condition
- `risk`: Why the condition is unacceptable for this project
- `owner`: Role that approves overriding the no-go check

Template:

- No-go if `<condition>` because `<risk>`, evidenced by `<artifact links>`, override owner `<role>`.

Good no-go checks are:
- Falsifiable (pass/fail from evidence)
- Time-bounded (valid for this phase or release)
- Traceable to requirement or implementation facts

## Threshold Design Method
Define threshold *types* first, then set values.

### Common threshold types
- Latency budget threshold
- Throughput or concurrency threshold
- Consistency tolerance threshold
- Recovery objective threshold (RTO/RPO)
- Ownership capacity threshold (team and on-call load)
- Cost volatility threshold
- Compliance exposure threshold

### For each threshold, record
- `rationale`: Why this threshold matters to project success
- `measurement_method`: How it is measured and by which telemetry
- `observation_window`: Time window and environment scope
- `decision_value`: Current value and units
- `redecision_trigger`: When to revisit the threshold

## Confidence and Escalation
For each decision, record confidence (`high`, `medium`, `low`) and why.

Escalate when:
- No-go checks depend on assumptions rather than evidence
- Threshold values cannot be measured in the current environment
- Stakeholder directions conflict and no priority rule is defined

## Output Contract
Every architecture decision artifact should include:

- Project-scoped no-go checks with evidence links
- Threshold table with rationale and measurement method
- Explicit assumptions and confidence level
- Re-decision trigger and owner
