---
name: nextjs-app-router
description: "Next.js App Router implementation workflow. Use when framework-specific application structure and runtime behavior must be implemented or revised; do not use for repository-wide architecture governance or release management policy."
---

# Nextjs App Router

## Trigger Boundary
- Use when implementing or refactoring Next.js App Router (`app/`) architecture.
- Do not use for legacy Pages Router migration planning only.
- Do not use for backend-only API concerns outside Next.js runtime.

## Goal
Deliver predictable route composition and data fetching behavior in Next.js App Router projects.

## Inputs
- Route structure and nested layout requirements
- Server/client component boundaries
- Caching, revalidation, and SEO constraints

## Outputs
- Route and layout map with rendering strategy
- Data-fetching and cache-control plan
- Error/loading boundary checklist

## Workflow
1. Define route groups, nested layouts, and shared UI boundaries.
2. Decide server vs client component ownership by interaction needs.
3. Configure fetch caching and revalidation per route criticality.
4. Implement loading, error, and not-found boundaries explicitly.
5. Validate route transitions and data consistency under navigation.

## Quality Gates
- Route tree is explicit and maintainable.
- Server/client boundaries are intentional and minimal.
- Cache/revalidation settings match freshness requirements.
- All user flows have explicit loading and error states.

## Failure Handling
- Stop when server/client responsibilities are mixed without rationale.
- Escalate when route data consistency cannot be guaranteed.
