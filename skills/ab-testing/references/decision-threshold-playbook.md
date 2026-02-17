# Decision Threshold Playbook for AB Testing

## Purpose
Use this reference to translate business risk into concrete experiment thresholds and decisions.

## 1) Choose the Primary Decision Metric
- Pick exactly one metric for go/no-go.
- Metric should map directly to the release decision objective.
- Reject metrics that are noisy proxies with weak business linkage.

## 2) Set Risk Posture Explicitly
- Define:
  - `false_positive_cost`: cost of shipping a harmful change.
  - `false_negative_cost`: cost of rejecting a beneficial change.
- Typical mapping guidance:
  - High false-positive cost -> stricter acceptance criteria and stronger guardrails.
  - High false-negative cost -> higher power and larger sample.

## 3) Derive `MIN_DETECTABLE_EFFECT`
- Set minimum material impact worth shipping.
- Inputs:
  - business value per percentage-point move
  - implementation/operational cost
  - expected persistence of effect
- Reject "smallest detectable number" if not decision-relevant.

## 4) Define Guardrails Before Exposure
- Include user harm and operational harm metrics.
- Typical guardrails:
  - reliability/error rate
  - latency
  - abuse/fraud rates
  - customer support load
  - short-term revenue risk
- Guardrails must include explicit breach limits and response actions.

## 5) Assignment Unit Selection
- `user`: default when cross-session behavior matters.
- `session`: only when spillover across sessions is negligible.
- `org`: for B2B features with organization-level interference.
- `device`: only when identity is unavailable and cross-device leakage is acceptable.
- Always document contamination risks and mitigation.

## 6) Runtime and Analysis Method
- Fixed horizon:
  - use when planned sample/time budget is reliable.
- Sequential:
  - use when early stop for safety/value is needed.
  - predefine look cadence and stopping rules.
- Always declare multiplicity control when multiple hypotheses can influence decisions.

## 7) Interpretation Rules
- Ship:
  - primary metric meets pre-registered target
  - guardrails are within limits
- Iterate:
  - uncertainty too high or effect below material threshold
  - no severe guardrail breach
- Rollback:
  - severe primary harm or guardrail breach beyond allowed limit
- Hold:
  - data quality compromised (for example SRM/instrumentation failure)

## 8) Non-Negotiable Integrity Rules
- Do not rewrite decision criteria after observing outcomes.
- Do not treat post-hoc segment findings as confirmatory evidence.
- Do not ignore SRM or instrumentation failures when making decisions.
