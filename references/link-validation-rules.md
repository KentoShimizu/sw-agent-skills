# Link Validation Rules

This repository validates documentation links with:
`python3 scripts/validate_skill_links.py --root .`

## Scope
- Validate markdown links in these documents by default:
  - `skills/*/SKILL.md`
  - `skills/*/references/**/*.md`
  - `references/**/*.md`
- Validate repository-relative file paths only.

## Included Targets
- Relative paths such as `./path/file.md` and `../path/file.md`
- Repository paths such as `skills/...`, `scripts/...`, and `references/...`
- Root-style repository paths (`/skills/...`) when they resolve under repository root

## Excluded Targets
- External URLs (`http://`, `https://`)
- Email links (`mailto:`)
- Section anchors (`#...`)
- Skill trigger links (`$skill-name` style)

## Inline Code Policy
- Default behavior: inline code spans are not validated as links.
- Rationale: command examples often contain execution paths (for example `./gradlew`, `/tmp/...`) that are runtime-specific and are not markdown links.
- Optional strict mode: include inline code spans only when explicitly requested via `--scan-code-spans`.

## Authoring Guidance
- Use markdown links for files that should be validated.
- Keep command examples inside code fences or inline code.
- Avoid mixing prose links and shell fragments in the same token.
- Prefer repository-relative paths over machine-specific absolute paths.

## CI Recommendation
Run both checks in CI:
1. Default docs validation: `python3 scripts/validate_skill_links.py --root .`
2. Optional strict sweep: `python3 scripts/validate_skill_links.py --root . --scan-code-spans`
