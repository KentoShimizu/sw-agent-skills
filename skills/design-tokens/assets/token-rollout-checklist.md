# Token Rollout Checklist

## Planning
- [ ] Target surfaces and repositories are identified.
- [ ] Token adoption scope is split into manageable rollout phases.
- [ ] Owners are assigned for each phase.
- [ ] Risk level is documented for each critical flow.

## Token Design Quality
- [ ] Naming follows `references/token-naming-rules.md`.
- [ ] Layering is valid (`core -> semantic -> component`).
- [ ] No direct raw value usage remains in newly changed code.
- [ ] Deprecated tokens have replacements and timeline.

## Accessibility And Localization
- [ ] Contrast checks pass for critical text/action states.
- [ ] Focus/hover/pressed/disabled states remain distinguishable.
- [ ] Typography tokens preserve readability for long localized strings.
- [ ] Locale expansion scenarios are tested for key surfaces.

## Engineering Readiness
- [ ] Build artifacts include updated token bundles.
- [ ] Snapshot/visual regression tests are updated.
- [ ] Search checks confirm migration progress.
- [ ] Rollback path is documented and verified.

## Release Decision
- [ ] Blocking issues are closed or explicitly accepted.
- [ ] Sign-off owners approved release.
- [ ] Post-release monitoring window is defined.
