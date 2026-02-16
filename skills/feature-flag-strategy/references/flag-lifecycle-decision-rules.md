# Flag Lifecycle Decision Rules

## Use A Flag When
- You need staged exposure with measurable rollback controls.
- You need emergency disable capability for risky changes.

## Do Not Use A Flag When
- The behavior is permanent and has no rollout uncertainty.
- The flag would become long-lived policy with no owner/expiry.

## Lifecycle Requirements
- Every flag needs owner, kill-switch, and expected retirement date.
