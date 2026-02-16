---
name: github-actions-workflow-design
description: "GitHub Actions workflow design and maintenance process. Trigger when repository automation on GitHub (build/test/release jobs, trigger rules, permissions, caching, concurrency, environments) must be created or revised; do not use for non-GitHub runtime architecture or data-layer design."
---

# Github Actions Workflow Design

## Trigger Boundary
- Use when `.github/workflows/*.yml` design or refactoring is required.
- Do not use for troubleshooting a specific failing run only; use `github-fix-ci` first.
- Do not use for non-GitHub CI platforms.

## Goal
Build reliable, maintainable, and fast GitHub Actions workflows.

## Inputs
- Required checks and branch protection policy
- Build/test/deploy steps and runtime matrix
- Secrets policy and environment separation

## Outputs
- Workflow specification with job graph and triggers
- Reusable action and cache strategy
- Validation checklist for pull request and main branch runs

## Workflow
1. Define trigger events (`pull_request`, `push`, `workflow_dispatch`) and scope.
2. Split jobs by responsibility and wire explicit dependencies.
3. Add deterministic setup, caching, and artifact boundaries.
4. Guard deploy jobs with environment approvals and least-privilege tokens.
5. Verify workflow with representative branch and PR scenarios.

## Quality Gates
- Required checks align with branch protection rules.
- Workflow runtime is measured and optimized where possible.
- Secrets and permissions are least privilege per job.
- Failure logs are actionable without manual deep inspection.

## Failure Handling
- Stop when required job boundaries or permissions are ambiguous.
- Escalate when workflow design conflicts with repository governance.

## References
- `references/actions-permissions-matrix.md`
- `references/workflow-snippets.md`
