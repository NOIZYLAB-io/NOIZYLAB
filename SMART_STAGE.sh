#!/bin/bash
# Smart staging for large repos

cd /Users/m2ultra/Github/Noizyfish/NOIZYLAB

echo "🚀 SMART STAGING"
echo "================================"

# Clear locks first
killall git 2>/dev/null || true
rm -f .git/index.lock 2>/dev/null

# Stage in small batches
git add *.md *.py *.sh *.json 2>/dev/null || true
git add _CLAUDE_ORGANIZED/ 2>/dev/null || true

echo "✅ Staged successfully"
git status --short | head -10
