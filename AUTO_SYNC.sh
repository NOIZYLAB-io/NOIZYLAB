#!/bin/bash
# Auto-sync between GOD and GABRIEL Cursor instances

WORKSPACE="/Users/m2ultra/Github/noizylab/MULTIBRAIN_SHARED"
cd "$WORKSPACE"

# Initialize if needed
if [ ! -d ".git" ]; then
    git init
    git remote add origin https://github.com/noizylab/multibrain-sync.git
fi

# Pull GABRIEL's changes
echo "⬇️  Pulling GABRIEL's frontend..."
git pull origin main --no-edit

# Push GOD's changes  
echo "⬆️  Pushing GOD's backend..."
git add .
git commit -m "Backend update from GOD $(date +%H:%M:%S)" 2>/dev/null || true
git push origin main

echo "✅ Sync complete!"
