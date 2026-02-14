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

Do not redefine ID formats, lifecycle states, approval gates, or privacy gates in individual skill files.

## ID Schema (Single Source of Truth)
- `DSN-PRN-<NNN>`: `^DSN-PRN-[0-9]{3,}$`
  - Design principle ID
- `DSN-SYS-<NNN>`: `^DSN-SYS-[0-9]{3,}$`
  - Design system foundation item ID
- `DSN-TOK-<CATEGORY>-<NNN>`: `^DSN-TOK-[A-Z0-9_]+-[0-9]{3,}$`
  - Design token ID
- `UX-FLW-<NNN>`: `^UX-FLW-[0-9]{3,}$`
  - Interaction flow ID
- `IA-NAV-<NNN>`: `^IA-NAV-[0-9]{3,}$`
  - Information architecture structure ID
- `VIS-SPEC-<NNN>`: `^VIS-SPEC-[0-9]{3,}$`
  - Visual spec ID
- `A11Y-CHK-<NNN>`: `^A11Y-CHK-[0-9]{3,}$`
  - Accessibility checklist ID
- `RESP-RUL-<NNN>`: `^RESP-RUL-[0-9]{3,}$`
  - Responsive layout rule ID
- `UX-RSR-<YYYYMMDD>-<NNN>`: `^UX-RSR-[0-9]{8}-[0-9]{3,}$`
  - User research synthesis ID
- `FIG-HND-<YYYYMMDD>-<NNN>`: `^FIG-HND-[0-9]{8}-[0-9]{3,}$`
  - Figma handoff package ID
- `DREV-<YYYYMMDD>-<NNN>`: `^DREV-[0-9]{8}-[0-9]{3,}$`
  - Design review result ID

## Issuance Rules
- Allocate IDs sequentially per prefix.
- Keep IDs immutable and append-only.
- Never reuse retired IDs.
- On collision, issue a new ID and mark old one as `invalid` with reason.

## Lifecycle States
- `DSN-PRN-*`: `proposed`, `accepted`, `deprecated`
- `DSN-SYS-*`: `proposed`, `accepted`, `deprecated`
- `DSN-TOK-*`: `proposed`, `accepted`, `deprecated`
- `UX-FLW-*`: `draft`, `reviewed`, `approved`, `deprecated`
- `IA-NAV-*`: `draft`, `reviewed`, `approved`, `deprecated`
- `VIS-SPEC-*`: `draft`, `reviewed`, `approved`, `deprecated`
- `A11Y-CHK-*`: `draft`, `reviewed`, `approved`, `rejected`
- `RESP-RUL-*`: `draft`, `reviewed`, `approved`, `deprecated`
- `UX-RSR-*`: `draft`, `reviewed`, `approved`, `rejected`
- `FIG-HND-*`: `prepared`, `reviewed`, `released`, `superseded`
- `DREV-*`: `draft`, `reviewed`, `approved`, `rejected`

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
A privacy evidence package is mandatory for:
- all `UX-RSR-*` artifacts
- all `FIG-HND-*` artifacts
- any manifest where `checks.user_facing_change` is `true`

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
- Required always for `UX-RSR-*`: Privacy Reviewer
- Required always for `FIG-HND-*`: Privacy Reviewer
- Required when legal/compliance-sensitive UX is affected: Legal Reviewer

## Machine Validation
- Run `python3 scripts/validate_design_contract.py --manifest <path/to/manifest.json>` from `skills/design-principles`.
- For CI or batch validation, run `python3 scripts/run_contract_validators.py --design-manifest <path/to/manifest.json>` from repository root.
- Manifest must include: `artifact_id`, `state`, `approvers`, and `checks`.
- Include `checks.user_facing_change` as `true` or `false`.
- Use the canonical accessibility check keys:
  - `checks.wcag_aa`
  - `checks.keyboard_navigation`
  - `checks.visible_focus_states`
  - `checks.color_contrast`
  - `checks.semantic_structure`
  - `checks.screen_reader_order`
  - `checks.text_expansion`
  - `checks.text_truncation`

## Gate Policy
- Block release when required IDs are missing or malformed.
- Block release when lifecycle state is invalid for the artifact type.
- Block release when required approvers are missing.
- Block release when accessibility or localization checks fail.
- Block release when privacy evidence requirements are incomplete.
- Do not add fallback UI logic for new designs; define explicit failure and empty states instead.
