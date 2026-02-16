# Design Governance Contract

## Scope
Apply this contract to all design-related skills:
- `design-*`
- `interaction-design`
- `information-architecture`
- `localization-qa`
- `visual-design`
- `accessibility-design`
- `responsive-layout-design`
- `ux-research-synthesis`
- `figma-handoff`

Use project-specific ID naming policies. Example IDs are non-binding.
Treat this document as operational guidance, not a mandatory schema.
When repository-specific rules exist, follow those first; otherwise use this as a default operating method.

## Manifest Profile Model (Canonical)
Profile is inferred from manifest content and context, not from fixed ID prefixes.

Examples:
- User-facing design review/check manifests
- UX research synthesis manifests
- Figma handoff manifests

## ID Format Policy (Project-Defined)
- `artifact_id` is optional and project-defined.
- If present, it must be non-empty and follow your repository ID policy.
- `checks.id_format_validated=true` means validation against that policy has been completed.

## Lifecycle States
Allowed states:
- `proposed`, `accepted`, `deprecated`
- `draft`, `reviewed`, `approved`, `rejected`
- `prepared`, `released`, `superseded`

## Accessibility and Localization Gates
- Target WCAG 2.2 AA as minimum baseline (`checks.wcag_aa`).
- Validate keyboard navigation (`checks.keyboard_navigation`).
- Validate visible focus states (`checks.visible_focus_states`).
- Validate color contrast (`checks.color_contrast`).
- Validate semantic structure (`checks.semantic_structure`).
- Validate screen reader reading order for key flows (`checks.screen_reader_order`).
- Validate localization for US English (`en-US`), Japanese (`ja-JP`), and at least two EU locales (`checks.locales`).
- Validate text expansion (`checks.text_expansion`) and truncation behavior (`checks.text_truncation`).

## Privacy Evidence Requirements
A privacy evidence package is mandatory when:
- `checks.user_facing_change` is `true`, or
- `privacy_evidence` is explicitly provided.

Include the following fields:
- `lawful_basis_or_consent`
- `pii_data_inventory`
- `data_minimization_decision`
- `retention_and_deletion_policy`
- `cross_border_transfer_control`
- `data_subject_rights_process`
- `redaction_and_access_control`

## Approval Matrix
- Required: Design Owner
- Required: Engineering Owner for implementation feasibility
- Required: Accessibility Reviewer for user-facing changes
- Required: Privacy Reviewer when privacy evidence is required
- Required when legal/compliance-sensitive UX is affected: Legal Reviewer

## Optional Consistency Check
- Optional: run `python3 scripts/validate_design_contract.py --manifest <path/to/manifest.json>` from `skills/design-principles`.
- Recommended structured manifest fields: `state`, `approvers`, and `checks` (plus optional `artifact_id`).
- Recommended: include `checks.user_facing_change` as `true` or `false`.
- Recommended accessibility check keys:
  - `checks.wcag_aa`
  - `checks.keyboard_navigation`
  - `checks.visible_focus_states`
  - `checks.color_contrast`
  - `checks.semantic_structure`
  - `checks.screen_reader_order`
  - `checks.text_expansion`
  - `checks.text_truncation`

## Operational Handling (Recommended)
- Escalate when IDs are malformed or inconsistent with the project policy.
- Escalate when lifecycle state is invalid for the selected process.
- Escalate when required approvers are missing.
- Escalate when accessibility or localization checks fail.
- Escalate when privacy evidence requirements are incomplete.
- Do not add fallback UI logic for new designs; define explicit failure and empty states instead.
