---
name: django-app-development
description: "Django application development workflow. Use when framework-specific application structure and runtime behavior must be implemented or revised; do not use for repository-wide architecture governance or release management policy."
---

# Django App Development

## Trigger Boundary
- Use when building or refactoring Django apps and modules.
- Do not use for Django-independent Python utility scripts.
- Do not use for frontend-only component architecture.

## Goal
Maintain clear Django app boundaries with reliable model, view, and configuration behavior.

## Inputs
- Domain model and feature requirements
- App/module boundaries and settings constraints
- Security and migration policies

## Outputs
- App structure and responsibility map
- Model/view/form/service interaction plan
- Migration and verification checklist

## Workflow
1. Partition features into coherent Django apps by domain.
2. Define models with explicit constraints and indexes.
3. Keep views thin and move domain logic into services/managers.
4. Manage settings by environment without hidden defaults.
5. Validate migrations, permissions, and critical user flows.

## Quality Gates
- App boundaries reduce coupling and circular imports.
- Migrations are reversible where required and reviewed.
- Auth and permission checks are explicit on protected routes.
- Settings are environment-driven and fail fast when missing.

## Failure Handling
- Stop when app responsibilities overlap without clear ownership.
- Escalate when migration risk or permission model is unresolved.
