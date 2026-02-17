# Design Governance Defaults (Project-First)

## Scope
Use this reference for design and UX skills when a project does not already define governance rules.
It is intentionally advisory and non-binding.

## Rule Precedence
Always apply rules in this order:
1. Existing repository or organization rules
2. Product/team conventions documented in the project
3. This default reference (only when 1 and 2 are missing)

## ID Policy
- Use project-defined ID naming if it already exists.
- If no naming policy exists, define a provisional ID pattern in the artifact itself.
- Treat any example IDs in skills as non-binding.
- Do not force a global prefix across unrelated projects.

## Lifecycle Policy
- Use project-defined lifecycle states when available.
- If missing, a lightweight default is acceptable (for example: `draft`, `reviewed`, `approved`, `rejected`).
- Keep lifecycle policy explicit in each artifact package.

## Review and Approval Policy
- Required approvers are project-defined.
- If no policy exists, use a minimal default:
  - Design owner for all design artifacts
  - Engineering owner when implementation is affected
  - Accessibility, Privacy, Legal reviewers only when risk profile requires them

## Localization and Privacy Policy
- Locale coverage is project-defined. Do not enforce fixed locale sets.
- Privacy evidence is required only when personal data handling or project policy requires it.
- Avoid forcing privacy/legal fields for documentation-only deliverables unless explicitly requested.

## Validation Policy
- For documentation-only workflows, validation is optional by default.
- Run validation only when the project explicitly opts into governed mode.
- The validator should enforce only project-declared requirements, not organization-specific hardcoded rules.

## Optional Manifest Hints
Projects that want governed validation can declare requirements in a manifest `policy` block.

Example (non-binding):

```json
{
  "artifact_id": "PROJECT-123",
  "state": "reviewed",
  "approvers": ["Design Owner", "Engineering Owner"],
  "checks": {
    "id_format_validated": true,
    "a11y_reviewed": true,
    "locales": ["ja-JP", "en-US"]
  },
  "policy": {
    "require_artifact_id": true,
    "allowed_states": ["draft", "reviewed", "approved", "rejected"],
    "required_approvers": ["Design Owner"],
    "required_checks": ["id_format_validated"],
    "required_locales": ["ja-JP"]
  }
}
```

## Operational Handling
- Escalate only when project-required fields are missing.
- If no project policy exists, keep outputs practical and do not block delivery with governance-only checks.
