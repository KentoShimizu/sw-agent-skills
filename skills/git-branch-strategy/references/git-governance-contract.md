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

Do not redefine ID formats, lifecycle states, approval gates, or synchronization policy in individual skill files.

## ID Schema (Single Source of Truth)
- `GIT-BRN-<NNN>`: `^GIT-BRN-[0-9]{3,}$`
  - Branch strategy policy
- `GIT-CMT-<YYYYMMDD>-<NNN>`: `^GIT-CMT-[0-9]{8}-[0-9]{3,}$`
  - Commit hygiene evidence package
- `GIT-RBS-<YYYYMMDD>-<NNN>`: `^GIT-RBS-[0-9]{8}-[0-9]{3,}$`
  - Rebase execution record
- `GIT-MRG-<YYYYMMDD>-<NNN>`: `^GIT-MRG-[0-9]{8}-[0-9]{3,}$`
  - Merge conflict resolution record
- `GIT-CHP-<YYYYMMDD>-<NNN>`: `^GIT-CHP-[0-9]{8}-[0-9]{3,}$`
  - Cherry-pick hotfix record
- `GIT-HIS-<YYYYMMDD>-<NNN>`: `^GIT-HIS-[0-9]{8}-[0-9]{3,}$`
  - History investigation report
- `GIT-BIS-<YYYYMMDD>-<NNN>`: `^GIT-BIS-[0-9]{8}-[0-9]{3,}$`
  - Bisect evidence record
- `GIT-RVT-<YYYYMMDD>-<NNN>`: `^GIT-RVT-[0-9]{8}-[0-9]{3,}$`
  - Revert recovery record
- `GIT-REL-<YYYYMMDD>-<NNN>`: `^GIT-REL-[0-9]{8}-[0-9]{3,}$`
  - Release tagging record
- `GIT-PRS-<YYYYMMDD>-<NNN>`: `^GIT-PRS-[0-9]{8}-[0-9]{3,}$`
  - PR synchronization record
- `GIT-CMP-<YYYYMMDD>-<NNN>`: `^GIT-CMP-[0-9]{8}-[0-9]{3,}$`
  - Compliance evidence package

## Issuance Rules
- Allocate IDs sequentially per prefix namespace.
- Keep IDs immutable and append-only.
- Never reuse retired IDs.
- On collision, issue a new ID and mark the old ID as `invalid` with reason.

## Lifecycle States
- `GIT-BRN-*`: `draft`, `reviewed`, `approved`, `deprecated`
- `GIT-REL-*`: `prepared`, `reviewed`, `released`, `superseded`
- `GIT-CMP-*`: `draft`, `reviewed`, `approved`, `expired`
- `GIT-CMT-*`, `GIT-RBS-*`, `GIT-MRG-*`, `GIT-CHP-*`, `GIT-HIS-*`, `GIT-BIS-*`, `GIT-RVT-*`, `GIT-PRS-*`:
  - `draft`, `reviewed`, `executed`, `rejected`
- `invalid` is allowed for all prefixes only to retire collided or voided IDs.

## Compliance Baseline (US, Japan, EU)
- Prevent personal data and secrets from entering commit history.
- Record lawful basis and cross-border transfer control when personal data is handled.
- Preserve auditability of approvals, execution records, and rollback decisions.
- Enforce retention and deletion policy for exported logs or evidence artifacts.

## Required Check Keys
Manifest `checks` must include all of the following common keys:
- `id_format_validated` (boolean)
- `branch_protection_verified` (boolean)
- `ci_required_checks_green` (boolean)
- `secret_scan_passed` (boolean)
- `history_rewrite_policy_compliant` (boolean)
- `handles_personal_data` (boolean)

Prefix-specific required keys:
- `GIT-PRS-*`
  - `pr_opened` (boolean)
  - `merge_sync_used` (boolean)
  - `rebase_used` (boolean)
  - `repository_merge_only_policy` (boolean)
- `GIT-RBS-*`
  - `pr_opened` (boolean)
  - `rebase_used` (boolean)
- `GIT-REL-*`
  - `signed_tag_verified` (boolean)
- Other prefixes do not require the above four keys.

## Privacy Evidence Requirements
When `checks.handles_personal_data` is `true`, `privacy_evidence` is mandatory and must include:
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
- Required for `GIT-REL-*`, `GIT-RVT-*`, `GIT-CHP-*`:
  - Security Reviewer
- Required when `checks.handles_personal_data` is `true`:
  - Privacy Reviewer

## Machine Validation
- Run `python3 scripts/validate_git_contract.py --manifest <path/to/manifest.json>` from `skills/git-branch-strategy`.
- Manifest must include `artifact_id`, `state`, `approvers`, and `checks`.

## Gate Policy
- Block release or execution when required IDs are missing or malformed.
- Block release or execution when lifecycle state is invalid for the artifact type.
- Block release or execution when required approvers are missing.
- Block release or execution when required checks fail.
- When `state` is `invalid`, prefix-specific execution checks are not enforced.
- For `GIT-PRS-*` artifacts:
  - `checks.pr_opened` must be `true`.
  - Exactly one of `checks.merge_sync_used` or `checks.rebase_used` must be `true`.
  - When `checks.repository_merge_only_policy` is `true`, `checks.rebase_used` must be `false`.
- For `GIT-RBS-*` artifacts:
  - `checks.pr_opened` must be `false`.
  - `checks.rebase_used` must be `true`.
- For `GIT-REL-*` artifacts:
  - `checks.signed_tag_verified` must be `true`.
