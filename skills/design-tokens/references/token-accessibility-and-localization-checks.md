# Token Accessibility And Localization Checks

## Accessibility Checks
- Verify text/background contrast for primary, secondary, and disabled states.
- Verify non-text contrast for focus indicators and interactive boundaries.
- Verify state distinguishability (default, hover, active, focus, disabled) without relying on color alone.
- Verify motion tokens respect reduced-motion preferences where required.

## Localization Checks
- Verify typography tokens maintain readability under 1.3x to 1.8x text expansion.
- Verify spacing tokens preserve hierarchy when labels become longer in translated locales.
- Verify line-height and letter-spacing tokens do not clip non-Latin scripts.
- Verify bidirectional layout support when locale direction changes.

## Coverage Scope
- Critical flows first (sign-in, checkout, payment, destructive actions).
- At least one representative screen per surface and theme mode.
- Include loading, empty, error, and success states.

## Failure Criteria
- Any contrast failure on critical text/action states.
- Any clipped or overlapping localized text in core flows.
- Any focus state that is visually ambiguous or invisible.
- Any state where semantic meaning changes across locales.
