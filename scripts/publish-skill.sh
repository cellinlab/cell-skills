#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  ./scripts/publish-skill.sh <skill-slug-or-path> --version <semver> [options]

Examples:
  ./scripts/publish-skill.sh deep-writer --version 0.1.0 --changelog "Initial public release"
  ./scripts/publish-skill.sh skills/opc-case-research --version 0.1.1 --tags latest,stable

Options:
  --version <semver>     Required. ClawHub publish version.
  --changelog <text>     Optional. Defaults to "Publish <slug> <version>".
  --tags <csv>           Optional. Defaults to "latest".
  --name <text>          Optional. Overrides the display name.
  --slug <slug>          Optional. Overrides the published slug.
  --site <url>           Optional. Exported as CLAWHUB_SITE for this run.
  --registry <url>       Optional. Exported as CLAWHUB_REGISTRY for this run.
  --dry-run              Print the resolved command without executing it.
  -h, --help             Show this help text.
EOF
}

require_command() {
  local name="$1"
  if ! command -v "$name" >/dev/null 2>&1; then
    echo "Missing required command: $name" >&2
    exit 1
  fi
}

resolve_clawhub_command() {
  if command -v clawhub >/dev/null 2>&1; then
    printf '%s\n' "clawhub"
    return 0
  fi

  if command -v npx >/dev/null 2>&1; then
    printf '%s\n' "npx -y clawhub"
    return 0
  fi

  echo "Missing required command: clawhub or npx" >&2
  exit 1
}

trim_quotes() {
  local value="$1"
  value="${value#\"}"
  value="${value%\"}"
  printf '%s\n' "$value"
}

title_case_slug() {
  printf '%s\n' "$1" | tr '-_' ' ' | awk '{
    for (i = 1; i <= NF; i++) {
      $i = toupper(substr($i, 1, 1)) tolower(substr($i, 2))
    }
    print
  }'
}

default_publish_slug() {
  local base="$1"
  if [[ "$base" == cell-* || "$base" == celf-* ]]; then
    printf '%s\n' "$base"
    return 0
  fi

  printf 'cell-%s\n' "$base"
}

resolve_repo_root() {
  local script_dir
  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  cd "$script_dir/.." && pwd
}

resolve_skill_dir() {
  local repo_root="$1"
  local input="$2"

  if [[ -d "$input" ]]; then
    cd "$input" && pwd
    return 0
  fi

  if [[ -d "$repo_root/$input" ]]; then
    cd "$repo_root/$input" && pwd
    return 0
  fi

  if [[ -d "$repo_root/skills/$input" ]]; then
    cd "$repo_root/skills/$input" && pwd
    return 0
  fi

  echo "Skill directory not found: $input" >&2
  exit 1
}

detect_display_name() {
  local skill_dir="$1"
  local agents_file="$skill_dir/agents/openai.yaml"

  if [[ -f "$agents_file" ]]; then
    local raw
    raw="$(sed -n 's/^[[:space:]]*display_name:[[:space:]]*//p' "$agents_file" | head -n 1)"
    if [[ -n "$raw" ]]; then
      trim_quotes "$raw"
      return 0
    fi
  fi

  title_case_slug "$(basename "$skill_dir")"
}

repo_root="$(resolve_repo_root)"
clawhub_runner="$(resolve_clawhub_command)"

if [[ $# -eq 0 ]]; then
  usage
  exit 1
fi

skill_input=""
version=""
changelog=""
tags="latest"
display_name=""
publish_slug=""
site=""
registry=""
dry_run="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --version)
      version="${2:-}"
      shift 2
      ;;
    --changelog)
      changelog="${2:-}"
      shift 2
      ;;
    --tags)
      tags="${2:-}"
      shift 2
      ;;
    --name)
      display_name="${2:-}"
      shift 2
      ;;
    --slug)
      publish_slug="${2:-}"
      shift 2
      ;;
    --site)
      site="${2:-}"
      shift 2
      ;;
    --registry)
      registry="${2:-}"
      shift 2
      ;;
    --dry-run)
      dry_run="true"
      shift
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage
      exit 1
      ;;
    *)
      if [[ -n "$skill_input" ]]; then
        echo "Unexpected extra argument: $1" >&2
        usage
        exit 1
      fi
      skill_input="$1"
      shift
      ;;
  esac
done

if [[ -z "$skill_input" ]]; then
  echo "Skill slug or path is required." >&2
  usage
  exit 1
fi

if [[ -z "$version" ]]; then
  echo "--version is required." >&2
  usage
  exit 1
fi

skill_dir="$(resolve_skill_dir "$repo_root" "$skill_input")"
skill_slug_default="$(basename "$skill_dir")"
skill_md="$skill_dir/SKILL.md"

if [[ ! -f "$skill_md" ]]; then
  echo "SKILL.md not found in $skill_dir" >&2
  exit 1
fi

if [[ -z "$publish_slug" ]]; then
  publish_slug="$(default_publish_slug "$skill_slug_default")"
fi

if [[ -z "$display_name" ]]; then
  display_name="$(detect_display_name "$skill_dir")"
fi

if [[ -z "$changelog" ]]; then
  changelog="Publish $publish_slug $version"
fi

if [[ -n "$site" ]]; then
  export CLAWHUB_SITE="$site"
fi

if [[ -n "$registry" ]]; then
  export CLAWHUB_REGISTRY="$registry"
fi

echo "Repo root:    $repo_root"
echo "Skill dir:    $skill_dir"
echo "Slug:         $publish_slug"
echo "Display name: $display_name"
echo "Version:      $version"
echo "Tags:         $tags"
echo "Changelog:    $changelog"
echo "Runner:       $clawhub_runner"

if [[ "$dry_run" == "true" ]]; then
  cat <<EOF
Command:
  $clawhub_runner publish "$skill_dir" \\
    --slug "$publish_slug" \\
    --name "$display_name" \\
    --version "$version" \\
    --tags "$tags" \\
    --changelog "$changelog"
EOF
  exit 0
fi

if [[ "$clawhub_runner" == "clawhub" ]]; then
  exec clawhub publish \
    "$skill_dir" \
    --slug "$publish_slug" \
    --name "$display_name" \
    --version "$version" \
    --tags "$tags" \
    --changelog "$changelog"
fi

require_command npx

exec npx -y clawhub publish \
  "$skill_dir" \
  --slug "$publish_slug" \
  --name "$display_name" \
  --version "$version" \
  --tags "$tags" \
  --changelog "$changelog"
