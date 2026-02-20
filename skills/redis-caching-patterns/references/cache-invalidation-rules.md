# Cache Invalidation Rules

- Prefer explicit invalidation tied to write events when correctness is strict.
- TTL should reflect data freshness and update frequency.
- Cache policy must define acceptable stale-read window.
