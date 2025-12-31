#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Git Sync
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🔄
# @raycast.packageName Developer

# Documentation:
# @raycast.description Sync all NOIZYLAB repos to GitHub
# @raycast.author NOIZYLAB

echo "🔄 Syncing NOIZYLAB repositories..."
echo ""

~/.local/bin/noizy-sync

echo ""
echo "✅ Sync complete!"
