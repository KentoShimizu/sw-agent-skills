# Sync Strategy Selection

## Choose Merge When
- Repository policy requires preserving merge context.
- PR review continuity is prioritized over linear history.

## Choose Rebase When
- Repository policy enforces linear history.
- Team can handle rewritten commit SHAs safely.

## Never Do
- Strategy switches without documenting rationale.
- Sync operations that skip re-running required checks.
