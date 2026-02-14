# CI Failure Taxonomy

## Purpose
Use this guide to classify failing checks before proposing a fix.

## Categories
- `test_regression`: Assertion or behavior mismatch in code under test.
- `env_configuration`: Missing environment variable, secret, or runtime setup drift.
- `dependency_drift`: Lockfile mismatch, package resolution conflict, or missing artifact.
- `flaky_execution`: Non-deterministic test behavior or timing race.
- `workflow_misconfiguration`: Incorrect Actions YAML, matrix, condition, or permissions.
- `external_service_unavailable`: Upstream outage or transient network/service error.

## Triage Sequence
1. Identify first deterministic failure line from logs.
2. Map to one category above.
3. Confirm if failure reproduces locally.
4. Define minimal fix scope that removes the root cause.
5. Record unresolved blockers with owner and next action.

## Evidence Checklist
- Failing check name
- Run URL
- First actionable log snippet
- Root-cause category
- Verification command used locally
