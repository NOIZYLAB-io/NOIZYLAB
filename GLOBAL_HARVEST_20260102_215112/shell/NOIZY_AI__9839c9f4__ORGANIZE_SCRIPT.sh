#!/bin/bash
# ORGANIZE_SCRIPT.sh - Move executed script to collection

SCRIPT_PATH="$1"
CATEGORY="${2:-executed}"

if [ -z "$SCRIPT_PATH" ]; then
    echo "Usage: ORGANIZE_SCRIPT.sh <script_path> [category]"
    exit 1
fi

COLLECTION_DIR="$HOME/Documents/NOIZYLAB/scripts_collection"
TARGET_DIR="$COLLECTION_DIR/$CATEGORY"

mkdir -p "$TARGET_DIR"

if [ -f "$SCRIPT_PATH" ]; then
    SCRIPT_NAME=$(basename "$SCRIPT_PATH")
    mv "$SCRIPT_PATH" "$TARGET_DIR/$SCRIPT_NAME"
    echo "✅ Moved $SCRIPT_NAME to $TARGET_DIR/"
else
    echo "❌ Script not found: $SCRIPT_PATH"
fi
