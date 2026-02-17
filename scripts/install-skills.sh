#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Install skills for Codex, Claude Code, and OpenCode.

Usage:
  scripts/install-skills.sh [options]

Options:
  --agent <all|codex|claude|opencode>   Target agent (default: all)
  --scope <global|local>                Install scope (default: global)
  --source <path>                       Source skills directory (optional)
  --project-root <path>                 Project root for local scope (default: current dir)
  --force                               Replace existing target directories
  -h, --help                            Show this help

Notes:
  - local scope supports Codex, Claude, and OpenCode.
  - when --source is omitted, installer downloads a release snapshot and installs from it.
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

run_cmd() {
  "$@"
}

resolve_dir() {
  local raw="$1"
  [ -d "${raw}" ] || die "directory not found: ${raw}"
  (cd "${raw}" && pwd)
}

resolve_latest_release_tag() {
  local tags

  tags="$(
    git ls-remote --refs --tags "${OFFICIAL_RELEASE_REPO_GIT_URL}" "v*" \
      | awk -F/ '{print $3}' \
      | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' || true
  )"

  [ -n "${tags}" ] || die "no stable release tags found in repository: ${OFFICIAL_RELEASE_REPO_GIT_URL}"
  printf '%s\n' "${tags}" | sort -V | tail -n 1
}

prepare_release_source() {
  local resolved_tag
  local archive_url
  local archive_path
  local extracted_root

  require_cmd git
  require_cmd curl
  require_cmd tar
  require_cmd awk
  require_cmd grep
  require_cmd sort

  resolved_tag="$(resolve_latest_release_tag)"

  RELEASE_TAG="${resolved_tag}"
  RELEASE_TEMP_DIR="$(mktemp -d)"
  archive_path="${RELEASE_TEMP_DIR}/release.tar.gz"
  archive_url="${OFFICIAL_RELEASE_ARCHIVE_BASE_URL}/archive/refs/tags/${resolved_tag}.tar.gz"

  curl -fsSL "${archive_url}" -o "${archive_path}" \
    || die "failed to download release archive: ${archive_url}"
  tar -xzf "${archive_path}" -C "${RELEASE_TEMP_DIR}" \
    || die "failed to extract release archive: ${archive_path}"

  extracted_root="$(find "${RELEASE_TEMP_DIR}" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
  [ -n "${extracted_root}" ] || die "failed to locate extracted release directory"

  SOURCE_DIR="${extracted_root}/skills"
  [ -d "${SOURCE_DIR}" ] || die "skills directory not found in release archive: ${SOURCE_DIR}"
}

AGENT="all"
SCOPE="global"
SOURCE_DIR=""
SOURCE_MODE="release"
PROJECT_ROOT="$(pwd)"
OFFICIAL_RELEASE_REPO_GIT_URL="https://github.com/KentoShimizu/sw-agent-skills.git"
OFFICIAL_RELEASE_ARCHIVE_BASE_URL="https://github.com/KentoShimizu/sw-agent-skills"
RELEASE_TAG=""
RELEASE_TEMP_DIR=""
FORCE=false

cleanup_release_temp_dir() {
  if [ -n "${RELEASE_TEMP_DIR}" ] && [ -d "${RELEASE_TEMP_DIR}" ]; then
    rm -rf "${RELEASE_TEMP_DIR}"
  fi
}

trap cleanup_release_temp_dir EXIT

while [ $# -gt 0 ]; do
  case "$1" in
    --agent)
      [ $# -ge 2 ] || die "--agent requires a value"
      AGENT="$2"
      shift 2
      ;;
    --scope)
      [ $# -ge 2 ] || die "--scope requires a value"
      SCOPE="$2"
      shift 2
      ;;
    --source)
      [ $# -ge 2 ] || die "--source requires a value"
      SOURCE_DIR="$2"
      SOURCE_MODE="local"
      shift 2
      ;;
    --project-root)
      [ $# -ge 2 ] || die "--project-root requires a value"
      PROJECT_ROOT="$2"
      shift 2
      ;;
    --force)
      FORCE=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown option: $1"
      ;;
  esac
done

case "${AGENT}" in
  all|codex|claude|opencode) ;;
  *) die "--agent must be one of: all, codex, claude, opencode" ;;
esac

case "${SCOPE}" in
  global|local) ;;
  *) die "--scope must be one of: global, local" ;;
esac

if [ "${SOURCE_MODE}" = "local" ]; then
  SOURCE_DIR="$(resolve_dir "${SOURCE_DIR}")"
else
  prepare_release_source
  SOURCE_DIR="$(resolve_dir "${SOURCE_DIR}")"
fi

if [ "${SCOPE}" = "local" ]; then
  PROJECT_ROOT="$(resolve_dir "${PROJECT_ROOT}")"
fi

VALID_SOURCE_SKILL_DIRS=()
while IFS= read -r skill_dir; do
  if [ -f "${skill_dir}/SKILL.md" ]; then
    VALID_SOURCE_SKILL_DIRS+=("${skill_dir}")
  fi
done < <(find "${SOURCE_DIR}" -mindepth 1 -maxdepth 1 -type d | sort)

if [ ${#VALID_SOURCE_SKILL_DIRS[@]} -eq 0 ]; then
  die "no skills found under source directory: ${SOURCE_DIR}"
fi

TARGET_LABELS=()
TARGET_PATHS=()

add_target() {
  TARGET_LABELS+=("$1")
  TARGET_PATHS+=("$2")
}

if [ "${SCOPE}" = "global" ]; then
  if [ "${AGENT}" = "all" ] || [ "${AGENT}" = "codex" ]; then
    add_target "codex" "${HOME}/.codex/skills"
  fi
  if [ "${AGENT}" = "all" ] || [ "${AGENT}" = "claude" ]; then
    add_target "claude" "${HOME}/.claude/skills"
  fi
  if [ "${AGENT}" = "all" ] || [ "${AGENT}" = "opencode" ]; then
    add_target "opencode" "${HOME}/.config/opencode/skills"
  fi
else
  if [ "${AGENT}" = "all" ] || [ "${AGENT}" = "codex" ]; then
    add_target "codex(local)" "${PROJECT_ROOT}/.codex/skills"
  fi
  if [ "${AGENT}" = "all" ] || [ "${AGENT}" = "claude" ]; then
    add_target "claude(local)" "${PROJECT_ROOT}/.claude/skills"
  fi
  if [ "${AGENT}" = "all" ] || [ "${AGENT}" = "opencode" ]; then
    add_target "opencode(local)" "${PROJECT_ROOT}/.opencode/skills"
  fi
fi

if [ ${#TARGET_PATHS[@]} -eq 0 ]; then
  die "no installation targets resolved"
fi

install_skills_into_target_root() {
  local label="$1"
  local target_root="$2"
  local installed_count=0

  run_cmd mkdir -p "${target_root}"

  for source_skill_dir in "${VALID_SOURCE_SKILL_DIRS[@]}"; do
    local skill_name
    skill_name="$(basename "${source_skill_dir}")"
    local destination_skill_dir="${target_root}/${skill_name}"

    if [ -e "${destination_skill_dir}" ] || [ -L "${destination_skill_dir}" ]; then
      if [ "${FORCE}" != true ]; then
        die "${label} target exists: ${destination_skill_dir} (use --force to replace)"
      fi
      run_cmd rm -rf "${destination_skill_dir}"
    fi

    run_cmd cp -R "${source_skill_dir}" "${destination_skill_dir}"

    installed_count=$((installed_count + 1))
  done

  printf 'installed: %s (%s) new=%d\n' "${label}" "${target_root}" "${installed_count}"
}

printf 'source-mode: %s\n' "${SOURCE_MODE}"
if [ "${SOURCE_MODE}" = "release" ]; then
  printf 'release-version: %s\n' "${RELEASE_TAG}"
fi
printf 'source: %s\n' "${SOURCE_DIR}"
printf 'scope: %s\n' "${SCOPE}"

for i in "${!TARGET_PATHS[@]}"; do
  install_skills_into_target_root "${TARGET_LABELS[$i]}" "${TARGET_PATHS[$i]}"
done

printf 'done.\n'
