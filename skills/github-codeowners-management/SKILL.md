---
name: github-codeowners-management
description: "CODEOWNERS governance process. Use when GitHub-native workflows, review routing, checks, or releases are the primary scope; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Codeowners Management

## Trigger Boundary
- Use when CODEOWNERS rules must be created, updated, or audited.
- Do not use for individual PR comment handling; use `github-address-comments`.
- Do not use for organization-wide access policy outside repository scope.

## Goal
Ensure ownership mapping routes reviews to the correct maintainers with minimal ambiguity.

## Inputs
- Repository directory ownership map
- Team boundaries and backup owners
- Required reviewer policy by path sensitivity

## Outputs
- CODEOWNERS mapping proposal
- Ownership conflict and gap report
- Review routing verification checklist

## Workflow
1. Map high-change and high-risk paths to explicit owners.
2. Define primary and secondary reviewers for critical areas.
3. Detect overlaps, uncovered paths, and noisy wildcard rules.
4. Validate routing against recent PR samples.
5. Publish update with maintenance and escalation rules.

## Scripts
- Lint CODEOWNERS:
  - `python3 scripts/lint_codeowners.py --path .github/CODEOWNERS --policy team`
- Enforce required patterns:
  - `python3 scripts/lint_codeowners.py --path .github/CODEOWNERS --policy team --require-pattern '/.github/workflows/*'`
- GitHub semantics mode (without strict team catch-all ordering):
  - `python3 scripts/lint_codeowners.py --path .github/CODEOWNERS --policy github`

## Quality Gates
- Critical paths have explicit, active owners.
- Wildcard rules do not override sensitive path ownership unintentionally.
- Ownership map is maintainable as teams evolve.
- Review routing matches expected maintainers in practice.

## Failure Handling
- Stop when ownership is unresolved for critical paths.
- Escalate when staffing gaps prevent enforceable ownership.

## References
- `references/codeowners-patterns.md`
