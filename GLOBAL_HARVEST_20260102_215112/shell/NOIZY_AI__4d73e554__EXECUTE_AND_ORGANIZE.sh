#!/bin/bash
# EXECUTE_AND_ORGANIZE.sh - Execute script then move it

SCRIPT_PATH="$1"
CATEGORY="${2:-executed}"

if [ -z "$SCRIPT_PATH" ]; then
    echo "Usage: EXECUTE_AND_ORGANIZE.sh <script_path> [category]"
    exit 1
fi

# Execute the script
echo "🚀 Executing: $SCRIPT_PATH"
bash "$SCRIPT_PATH"

# Move to collection
echo "📁 Organizing script..."
bash "$HOME/Documents/NOIZYLAB/scripts_collection/ORGANIZE_SCRIPT.sh" "$SCRIPT_PATH" "$CATEGORY"

echo "✅ Done!"
