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
  --project-root <path>                 Project root for local scope (default: current dir)
  -h, --help                            Show this help

Notes:
  - local scope supports Codex, Claude, and OpenCode.
  - installer downloads the latest release snapshot and installs from it.
  - installer manages only directories listed in .sw-agent-skills-managed.
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

is_valid_skill_name() {
  local skill_name="$1"
  printf '%s' "${skill_name}" | grep -Eq '^[A-Za-z0-9._-]+$'
}

array_contains() {
  local needle="$1"
  shift
  local item
  for item in "$@"; do
    if [ "${item}" = "${needle}" ]; then
      return 0
    fi
  done
  return 1
}

read_managed_skill_names() {
  local managed_state_path="$1"
  local managed_name

  if [ ! -f "${managed_state_path}" ]; then
    return 0
  fi

  while IFS= read -r managed_name; do
    [ -z "${managed_name}" ] && continue
    if [ "${managed_name}" = "." ] || [ "${managed_name}" = ".." ] || ! is_valid_skill_name "${managed_name}"; then
      die "invalid managed skill entry in ${managed_state_path}: ${managed_name}"
    fi
    printf '%s\n' "${managed_name}"
  done < "${managed_state_path}"
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
PROJECT_ROOT="$(pwd)"
OFFICIAL_RELEASE_REPO_GIT_URL="https://github.com/KentoShimizu/sw-agent-skills.git"
OFFICIAL_RELEASE_ARCHIVE_BASE_URL="https://github.com/KentoShimizu/sw-agent-skills"
RELEASE_TAG=""
RELEASE_TEMP_DIR=""
MANAGED_STATE_FILE_NAME=".sw-agent-skills-managed"

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
    --project-root)
      [ $# -ge 2 ] || die "--project-root requires a value"
      PROJECT_ROOT="$2"
      shift 2
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

prepare_release_source
SOURCE_DIR="$(resolve_dir "${SOURCE_DIR}")"

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
  local managed_state_path="${target_root}/${MANAGED_STATE_FILE_NAME}"
  local managed_state_tmp_path="${managed_state_path}.tmp.$$"
  local previous_managed_skill_names=()
  local current_managed_skill_names=()

  mkdir -p "${target_root}"

  if [ -f "${managed_state_path}" ]; then
    while IFS= read -r managed_name; do
      if ! array_contains "${managed_name}" "${previous_managed_skill_names[@]+"${previous_managed_skill_names[@]}"}"; then
        previous_managed_skill_names+=("${managed_name}")
      fi
    done < <(read_managed_skill_names "${managed_state_path}")
  else
    for source_skill_dir in "${VALID_SOURCE_SKILL_DIRS[@]}"; do
      local source_skill_name
      source_skill_name="$(basename "${source_skill_dir}")"
      local source_destination_skill_dir="${target_root}/${source_skill_name}"
      if [ -e "${source_destination_skill_dir}" ] || [ -L "${source_destination_skill_dir}" ]; then
        previous_managed_skill_names+=("${source_skill_name}")
      fi
    done
  fi

  for source_skill_dir in "${VALID_SOURCE_SKILL_DIRS[@]}"; do
    local skill_name
    skill_name="$(basename "${source_skill_dir}")"
    local destination_skill_dir="${target_root}/${skill_name}"

    if [ "${skill_name}" = "." ] || [ "${skill_name}" = ".." ] || ! is_valid_skill_name "${skill_name}"; then
      die "invalid source skill directory name: ${skill_name}"
    fi

    if [ -e "${destination_skill_dir}" ] || [ -L "${destination_skill_dir}" ]; then
      if ! array_contains "${skill_name}" "${previous_managed_skill_names[@]+"${previous_managed_skill_names[@]}"}"; then
        die "${label} target exists and is not managed by installer: ${destination_skill_dir}"
      fi
    fi
  done

  for managed_skill_name in "${previous_managed_skill_names[@]+"${previous_managed_skill_names[@]}"}"; do
    local managed_destination_skill_dir="${target_root}/${managed_skill_name}"
    if [ -e "${managed_destination_skill_dir}" ] || [ -L "${managed_destination_skill_dir}" ]; then
      rm -rf "${managed_destination_skill_dir}"
    fi
  done

  for source_skill_dir in "${VALID_SOURCE_SKILL_DIRS[@]}"; do
    local skill_name
    skill_name="$(basename "${source_skill_dir}")"
    local destination_skill_dir="${target_root}/${skill_name}"

    cp -R "${source_skill_dir}" "${destination_skill_dir}"
    current_managed_skill_names+=("${skill_name}")

    installed_count=$((installed_count + 1))
  done

  : > "${managed_state_tmp_path}"
  for managed_skill_name in "${current_managed_skill_names[@]}"; do
    printf '%s\n' "${managed_skill_name}" >> "${managed_state_tmp_path}"
  done
  mv "${managed_state_tmp_path}" "${managed_state_path}"

  printf 'installed: %s (%s) new=%d\n' "${label}" "${target_root}" "${installed_count}"
}

printf 'release-version: %s\n' "${RELEASE_TAG}"
printf 'source: %s\n' "${SOURCE_DIR}"
printf 'scope: %s\n' "${SCOPE}"

for i in "${!TARGET_PATHS[@]}"; do
  install_skills_into_target_root "${TARGET_LABELS[$i]}" "${TARGET_PATHS[$i]}"
done

printf 'done.\n'
