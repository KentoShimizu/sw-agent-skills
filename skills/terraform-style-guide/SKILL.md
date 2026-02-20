---
name: terraform-style-guide
description: "Style, review, and refactoring standards for Terraform infrastructure-as-code. Trigger when `.tf` or `.tfvars` source/modules/workflow configuration is created, changed, or reviewed and IaC-specific quality rules (module boundaries, variable typing, state safety, plan/apply discipline) must be enforced. Do not use for CloudFormation, Pulumi, or application-runtime coding conventions unless Terraform artifacts are also changed. Combine with language-specific guides only when application code and IaC both change."
---

# Terraform Style Guide

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

Apply this checklist when writing or reviewing Terraform code.

## Trigger Reference

- Use `references/trigger-matrix.md` as the canonical trigger and co-activation matrix.
- Resolve skill activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...` when automation is available.
- Validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Architecture and module design
## Quality Gate Reference

- Use `references/quality-gate-command-matrix.md` for CI check-only vs local autofix command mapping.

1. Keep modules small, focused, and reusable by responsibility.
2. Separate environment composition from reusable module internals.
3. Expose clear module interfaces with typed inputs and minimal outputs.
4. Keep dependency direction explicit; avoid hidden cross-module coupling.

## Naming and code structure

1. Use consistent `snake_case` names for variables, locals, resources, and outputs.
2. Keep resource blocks readable with logical grouping.
3. Use `locals` for repeated expressions and derived values.
4. Replace unexplained literals with named locals/constants and include units (`rotation_days`).

## Variables and configuration safety

1. Define variable types explicitly and add validation rules.
2. Mark sensitive values with `sensitive = true`.
3. Require critical inputs explicitly and fail plan/apply when missing.
4. Do not hardcode fallback defaults for required environment-derived values.

## State and lifecycle discipline

1. Use remote state with locking for collaborative environments.
2. Keep state boundaries intentional to reduce blast radius.
3. Review lifecycle rules (`create_before_destroy`, `prevent_destroy`) explicitly.
4. Avoid unmanaged drift; reconcile differences intentionally.

## Security and compliance

1. Enforce least-privilege IAM and narrow resource policies.
2. Enable encryption at rest and in transit where supported.
3. Avoid exposing secrets in plain text outputs or logs.
4. Run policy/security scanners before merge.

## Performance and scalability

1. Avoid unnecessary resource churn by stabilizing identifiers and `for_each` keys.
2. Keep plans deterministic and readable in large stacks.
3. Split very large stacks to keep plan/apply time bounded.
4. Minimize provider/API call volume where possible.

## Testing and verification

1. Run validation and lint checks on every change.
2. Review `terraform plan` output carefully for destructive actions.
3. Add environment-specific integration checks for critical modules.
4. Document manual rollback/remediation steps for risky infra changes.

## Observability and operations

1. Emit infrastructure changes through auditable pipelines.
2. Track drift, failed applies, and policy violations.
3. Ensure runbooks exist for failed deployment recovery.
4. Keep change approvals explicit for high-impact resources.

## CI required quality gates (check-only)

1. Run `terraform fmt -check -recursive`.
2. Run `terraform validate`.
3. Run `tflint` (or project linter equivalent).
4. Run `tfsec`/`checkov` (or project policy scanner equivalent).

## Optional autofix commands (local)

1. Run `terraform fmt -recursive` to apply formatting.
