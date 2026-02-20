# Server Client And Cache Rules

- Default to server components unless client interaction requires client components.
- Keep client components as leaf-level as practical.
- Choose caching/revalidation per route freshness and consistency needs.
- Avoid mixing contradictory cache policies in the same data path.
