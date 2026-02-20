# Git Governance Contract

## Scope
Apply this contract to all `git-*` skills:
- `git-branch-strategy`
- `git-commit-hygiene`
- `git-rebase-workflow`
- `git-merge-conflict-resolution`
- `git-cherry-pick-hotfix`
- `git-history-investigation`
- `git-bisect-debugging`
- `git-revert-recovery`
- `git-release-tagging`
- `git-pr-sync-workflow`

Use project-specific ID naming rules. Example ID patterns in this contract are non-binding.
Treat this document as operational guidance, not a mandatory schema.
When repository-specific rules exist, follow those first; otherwise use this as a default operating method.

## Profile Inference Contract (Canonical)
Do not require `artifact_kind` in manifests.
Determine artifact profile from execution context and manifest content:
- Strategy and policy records: no execution-specific check keys are present.
- PR-sync records: `checks.pr_opened` plus sync-mode keys are present.
- Rebase execution records: `checks.pr_opened=false` and `checks.rebase_used=true`.
- Release tag records: `checks.signed_tag_verified=true`.
- Compliance evidence records: `privacy_evidence` is present and complete.

For repository operations, filename and location are valid project-level routing controls.

## ID Format Policy (Project-Defined)
- `artifact_id` is optional and project-defined.
- Keep one repository-level ID policy and enforce it consistently.
- `checks.id_format_validated=true` must represent validation against that policy.
- Example IDs (non-binding):
  - `GIT-BRN-001`
  - `GIT-CMT-20260214-001`
  - `GIT-RBS-20260214-001`
  - `GIT-MRG-20260214-001`
  - `GIT-CHP-20260214-001`
  - `GIT-HIS-20260214-001`
  - `GIT-BIS-20260214-001`
  - `GIT-RVT-20260214-001`
  - `GIT-REL-20260214-001`
  - `GIT-PRS-20260214-001`
  - `GIT-CMP-20260214-001`

## Lifecycle States
- Strategy/policy records: `draft`, `reviewed`, `approved`, `deprecated`
- Release tag records: `prepared`, `reviewed`, `released`, `superseded`
- Compliance evidence records: `draft`, `reviewed`, `approved`, `expired`
- Execution records (`rebase`, `merge conflict`, `cherry-pick`, `history`, `bisect`, `revert`, `pr sync`):
  - `draft`, `reviewed`, `executed`, `rejected`
- `invalid` is allowed for all profiles only to retire collided or voided IDs.

## Compliance Baseline (US, Japan, EU)
- Prevent personal data and secrets from entering commit history.
- Record lawful basis and cross-border transfer control when personal data is handled.
- Preserve auditability of approvals, execution records, and rollback decisions.
- Enforce retention and deletion policy for exported logs or evidence artifacts.

## Recommended Check Keys
Recommended common keys in `checks`:
- `id_format_validated` (boolean)
- `branch_protection_verified` (boolean)
- `ci_required_checks_green` (boolean)
- `secret_scan_passed` (boolean)
- `history_rewrite_policy_compliant` (boolean)
- `handles_personal_data` (boolean)

Profile-specific keys (recommended when applicable):
- PR-sync profile
  - `pr_opened` (boolean)
  - `merge_sync_used` (boolean)
  - `rebase_used` (boolean)
  - `repository_merge_only_policy` (boolean)
- Rebase execution profile
  - `pr_opened` (boolean)
  - `rebase_used` (boolean)
- Release tag profile
  - `signed_tag_verified` (boolean)

## Privacy Evidence Guidance
When `checks.handles_personal_data` is `true`, include `privacy_evidence` with:
- `lawful_basis_or_consent`
- `pii_data_inventory`
- `data_minimization_decision`
- `retention_and_deletion_policy`
- `cross_border_transfer_control`
- `data_subject_rights_process`
- `redaction_and_access_control`

## Approval Matrix
- Required for all Git workflow artifacts:
  - Repository Owner
  - Engineering Owner
- Required for release tag, revert, and cherry-pick records:
  - Security Reviewer
- Required when `checks.handles_personal_data` is `true`:
  - Privacy Reviewer

## Optional Consistency Check
- Optional: `python3 scripts/validate_git_contract.py --manifest <path/to/manifest.json>` from `skills/git-branch-strategy`.
- Recommended structured fields: `state`, `approvers`, and `checks`.
- `artifact_id` is optional. If present, keep it non-empty.

## Operational Handling (Recommended)
- Escalate when identifier policy checks fail (`checks.id_format_validated=false`).
- Escalate when lifecycle state is invalid.
- Escalate when required approvers are missing.
- Escalate when critical checks fail.
- When `state` is `invalid`, context-specific execution checks are not enforced.
- For `pr_sync_record` artifacts:
  - `checks.pr_opened` should be `true`.
  - Prefer exactly one of `checks.merge_sync_used` or `checks.rebase_used` as `true`.
  - When `checks.repository_merge_only_policy` is `true`, `checks.rebase_used` should be `false`.
- For `rebase_execution_record` artifacts:
  - `checks.pr_opened` should be `false`.
  - `checks.rebase_used` should be `true`.
- For `release_tag_record` artifacts:
  - `checks.signed_tag_verified` should be `true`.
