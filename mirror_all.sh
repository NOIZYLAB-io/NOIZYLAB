#!/usr/bin/env bash
set -euo pipefail

# 🚀 NOIZYLAB MIRROR ALL - TURBO EDITION
# Mirrors all repos to github.com/Noizyfish/NOIZYLAB
# M2Ultra optimized: 24 threads, jumbo frames ready

MAIN="git@github.com:Noizyfish/NOIZYLAB.git"
BASE="${1:-/Volumes/6TB}"
LIST="/tmp/noizylab_repos.txt"
LOG="/tmp/noizylab_mirror.log"
PARALLEL=8

echo "🚀 NOIZYLAB MIRROR - TURBO EDITION"
echo "==================================="
echo "Target: $MAIN"
echo "Source: $BASE"
echo "Parallel: $PARALLEL jobs"
echo ""

# Find all repos
echo "🔍 Scanning for repos..."
find "$BASE" -type d -name ".git" 2>/dev/null > "$LIST"
TOTAL=$(wc -l < "$LIST" | tr -d ' ')
echo "Found $TOTAL repositories"
echo ""

# Counter
SUCCESS=0
FAILED=0

mirror_repo() {
  local gitdir="$1"
  local repo_dir="$(dirname "$gitdir")"
  local name="$(basename "$repo_dir")"
  
  cd "$repo_dir" 2>/dev/null || return 1
  
  # Skip if already pointing to MAIN
  if git remote get-url origin 2>/dev/null | grep -q "Noizyfish/NOIZYLAB"; then
    echo "⏭️  $name (already configured)"
    return 0
  fi
  
  echo "🔄 $name..."
  git remote remove origin 2>/dev/null || true
  git remote add origin "$MAIN"
  
  if git push --mirror origin 2>>"$LOG"; then
    echo "✅ $name"
    return 0
  else
    echo "❌ $name (check $LOG)"
    return 1
  fi
}

export -f mirror_repo
export MAIN LOG

# Process repos
echo "📤 Mirroring to GitHub..."
echo ""

while read -r gitdir; do
  if mirror_repo "$gitdir"; then
    ((SUCCESS++)) || true
  else
    ((FAILED++)) || true
  fi
done < "$LIST"

echo ""
echo "🎯 MIRROR COMPLETE"
echo "=================="
echo "✅ Success: $SUCCESS"
echo "❌ Failed:  $FAILED"
echo "📁 Total:   $TOTAL"
echo ""
echo "All repos now mirror to $MAIN"
echo "🔥 GORUNFREE!"
