#!/usr/bin/env bash
set -euo pipefail

# Usage:
#  - configure via environment variables:
#      DEFAULT_BRANCH (required)
#      EXECUTE (true/false) default false -> when true actually deletes remote branches
#      KEEP_DAYS (integer days) default 30
#      PROTECTED_CSV (comma separated extra protected branch names) default main,master
#      ALLOW_PRUNE (true/false) default true
#      REPO_URL must be set to an authenticated remote if deletions are to be executed
#
# Behavior:
#  - Fetches all remote refs, lists candidate branches not equal to default or protected.
#  - Candidate selection: branches merged into DEFAULT_BRANCH OR last commit older than KEEP_DAYS.
#  - Default is dry-run; to actually delete set EXECUTE=true and ensure REPO_URL uses token auth.

DEFAULT_BRANCH="${DEFAULT_BRANCH:-}"
EXECUTE="${EXECUTE:-false}"
KEEP_DAYS="${KEEP_DAYS:-30}"
PROTECTED_CSV="${PROTECTED_CSV:-main,master}"
ALLOW_PRUNE="${ALLOW_PRUNE:-true}"
REPO_URL="${REPO_URL:-origin}"

if [[ -z "$DEFAULT_BRANCH" ]]; then
  echo "ERROR: DEFAULT_BRANCH must be set"
  exit 2
fi

echo "Starting maintenance: default branch = $DEFAULT_BRANCH"
echo "Execute deletions: $EXECUTE"
echo "Keep branches with commits newer than: $KEEP_DAYS days"
echo "Protected branches: $PROTECTED_CSV"
echo "Allow prune/gc: $ALLOW_PRUNE"

# Prepare git
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

# Ensure we have all remote branches
git remote set-url origin "${REPO_URL}" || true
git fetch --prune --all

# Build protected set
IFS=',' read -r -a PROTECTED_ARR <<< "$PROTECTED_CSV"
PROTECTED_SET=()
for b in "${PROTECTED_ARR[@]}"; do
  PROTECTED_SET+=("$b")
done
PROTECTED_SET+=("$DEFAULT_BRANCH")

# helper to check protected
is_protected() {
  local b="$1"
  for p in "${PROTECTED_SET[@]}"; do
    if [[ "$b" == "$p" ]]; then
      return 0
    fi
  done
  return 1
}

# compute cutoff epoch
if [[ "$KEEP_DAYS" -gt 0 ]]; then
  CUTOFF_EPOCH=$(date -d "-${KEEP_DAYS} days" +%s)
else
  CUTOFF_EPOCH=0
fi

# list remote branches
mapfile -t REMOTE_BRANCHES < <(git for-each-ref --format='%(refname:short)' refs/remotes/origin | sed 's|origin/||' || true)

CANDIDATES=()

for branch in "${REMOTE_BRANCHES[@]}"; do
  # skip HEAD and empty
  if [[ -z "$branch" ]] || [[ "$branch" == "HEAD" ]]; then
    continue
  fi

  # skip protected/default
  if is_protected "$branch"; then
    echo "Skipping protected branch: $branch"
    continue
  fi

  # find last commit timestamp on the branch (remote)
  last_commit_epoch=$(git log -1 --format="%ct" "origin/${branch}" 2>/dev/null || echo 0)
  merged=false

  # Check if branch is merged into default branch
  # We check whether branch tip is an ancestor of origin/DEFAULT_BRANCH
  if git merge-base --is-ancestor "origin/${branch}" "origin/${DEFAULT_BRANCH}" >/dev/null 2>&1; then
    merged=true
  fi

  older_than_cutoff=false
  if [[ "$last_commit_epoch" -ne 0 ]]; then
    if [[ "$last_commit_epoch" -lt "$CUTOFF_EPOCH" ]]; then
      older_than_cutoff=true
    fi
  else
    # branch with no commits? treat as older
    older_than_cutoff=true
  fi

  # decide candidate if merged OR older than cutoff
  if [[ "$merged" == "true" ]] || [[ "$older_than_cutoff" == "true" ]]; then
    CANDIDATES+=("$branch")
    echo "Candidate: $branch (merged=$merged, last_commit=$(date -d @${last_commit_epoch} --iso-8601=seconds 2>/dev/null || echo 'unknown'))"
  else
    echo "Keeping active unmerged branch: $branch"
  fi
done

if [[ "${#CANDIDATES[@]}" -eq 0 ]]; then
  echo "No candidate branches found for deletion."
else
  echo ""
  echo "Summary of candidate branches (${#CANDIDATES[@]}):"
  for c in "${CANDIDATES[@]}"; do
    echo "  - $c"
  done
fi

if [[ "$EXECUTE" != "true" ]]; then
  echo ""
  echo "DRY RUN: to actually delete branches re-run with EXECUTE=true (e.g., workflow_dispatch input or set in env)."
  exit 0
fi

# Confirm we have a remote URL that can delete
if [[ "$REPO_URL" == "origin" ]]; then
  echo "ERROR: REPO_URL not set to an authenticated URL; cannot perform deletions."
  exit 3
fi

# perform deletions
for branch in "${CANDIDATES[@]}"; do
  echo "Deleting remote branch: $branch"
  # double-check not protected
  if is_protected "$branch"; then
    echo "Skipping protected branch (double-check): $branch"
    continue
  fi
  # delete remote branch
  git push "${REPO_URL}" --delete "refs/heads/${branch}" || {
    echo "Warning: deletion failed for $branch (may be protected or already removed)"
  }
done

# Optional prune & garbage collect locally in runner
if [[ "$ALLOW_PRUNE" == "true" ]]; then
  git remote prune origin || true
  # local gc
  git gc --aggressive --prune=now || true
fi

echo "Maintenance run complete."
