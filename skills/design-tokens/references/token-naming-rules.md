# Token Naming Rules

## Naming Principles
- Prefer semantic intent over implementation detail.
- Keep names stable across component refactors.
- Encode state only when state-specific values differ.
- Avoid product- or page-specific names for shared tokens.

## Recommended Pattern
- Core: `<category>.<family>.<scale>`
  - Example: `color.blue.600`, `space.200`, `radius.100`
- Semantic: `<category>.<role>.<context>.<state>`
  - Example: `color.action.primary.default`
- Component: `<component>.<variant>.<property>.<state>`
  - Example: `button.primary.background.hover`

## Good Vs Bad Examples
- Good: `color.text.muted.default`
- Bad: `grayText2`
- Good: `space.layout.section.gap`
- Bad: `marginTop16`
- Good: `button.primary.foreground.disabled`
- Bad: `blueButtonTextDisabled`

## Anti-patterns
- Encoding hex values or pixel sizes into token IDs.
- Mixing component and semantic layers in one token name.
- Reusing one token for unrelated roles to avoid adding new semantic tokens.

## Review Questions
- Does the name describe "why this value exists" rather than "what the value is"?
- Will this name still make sense after a component redesign?
- Is this token scoped to the correct layer?
