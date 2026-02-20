# Canary Promotion Rules

## Promotion Prerequisites
- Guardrails must remain inside defined thresholds for hold window.
- No unresolved severity-1 incidents in canary cohort.

## Stop Rules
- Any hard guardrail breach triggers stop or rollback.
- Unknown telemetry quality issues block further promotion.
