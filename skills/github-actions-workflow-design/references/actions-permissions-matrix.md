# Actions Permissions Matrix

## Principle
Use least privilege per job. Avoid repository-wide write permissions by default.

## Common Job Profiles
- Test-only jobs: `contents: read`
- Lint/static analysis: `contents: read`, optional `pull-requests: write` for annotations
- Release jobs: `contents: write`, optional `packages: write`
- Deployment jobs: scoped environment permissions plus required cloud auth only

## Security Rules
- Set top-level permissions to read-only baseline.
- Elevate permissions per job only when necessary.
- Keep `GITHUB_TOKEN` privileges minimal.
- Require environment approvals for production deploy jobs.
