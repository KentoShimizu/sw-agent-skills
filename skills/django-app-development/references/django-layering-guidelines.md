# Django Layering Guidelines

## Boundary Guidance
- Keep HTTP transport concerns in views/serializers/forms.
- Keep domain rules in services, managers, or domain modules.
- Keep persistence concerns in models/query layer.

## Common Smells
- Fat views with mixed domain logic.
- Implicit cross-app imports causing circular dependencies.
- Permission checks scattered inconsistently.
