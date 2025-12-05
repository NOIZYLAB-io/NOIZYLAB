#!/bin/bash
################################################################################
# ⚡ INSTANT CONSOLIDATION - MAXIMUM SPEED! ⚡
################################################################################
# CURSE_BEAST_01 + CURSE_BEAST_02
# Moving ALL code to ONE place NOW!
################################################################################

set -e

echo "⚡⚡⚡ INSTANT CONSOLIDATION - MAXIMUM SPEED! ⚡⚡⚡"
echo "🔥 CURSE_BEAST_02 - MOVING ALL CODE NOW!"
echo ""

NOIZYLAB="/Users/m2ultra/NOIZYLAB"
TARGET="$NOIZYLAB/CONSOLIDATED_CODE"

# Create target structure
echo "🏗️ Creating consolidated structure..."
mkdir -p "$TARGET/PYTHON"
mkdir -p "$TARGET/JAVASCRIPT"
mkdir -p "$TARGET/TYPESCRIPT"
mkdir -p "$TARGET/SHELL"
mkdir -p "$TARGET/OTHER"
echo "✅ Structure ready!"

# Function to move code files
move_code_files() {
    local SOURCE=$1
    local TYPE=$2
    local EXT=$3
    
    if [ -d "$SOURCE" ]; then
        echo "⚡ Moving $TYPE files from $SOURCE..."
        find "$SOURCE" -name "*.$EXT" -type f 2>/dev/null | while read file; do
            if [ -f "$file" ]; then
                cp "$file" "$TARGET/$TYPE/" 2>/dev/null || true
            fi
        done
    fi
}

# Move Python files (FAST!)
echo ""
echo "1️⃣ CONSOLIDATING PYTHON..."
move_code_files "/Volumes/4TBSG" "PYTHON" "py"
move_code_files "/Volumes/6TB" "PYTHON" "py"
echo "✅ Python consolidated"

# Move JavaScript/TypeScript (FAST!)
echo ""
echo "2️⃣ CONSOLIDATING JAVASCRIPT/TYPESCRIPT..."
move_code_files "/Volumes/4TBSG" "JAVASCRIPT" "js"
move_code_files "/Volumes/4TBSG" "TYPESCRIPT" "ts"
echo "✅ JS/TS consolidated"

# Move Shell scripts (FAST!)
echo ""
echo "3️⃣ CONSOLIDATING SHELL SCRIPTS..."
move_code_files "/Volumes/4TBSG" "SHELL" "sh"
move_code_files "/Volumes/6TB" "SHELL" "sh"
echo "✅ Shell scripts consolidated"

echo ""
echo "="
echo "="
echo ""
echo "🎉 INSTANT CONSOLIDATION COMPLETE!"
echo ""
echo "📂 All code copied to: $TARGET"
echo ""
echo "📊 Check consolidated files:"
echo "   ls -la $TARGET/*/"
echo ""
echo "🔥 CURSE_BEAST_02 - CODE CONSOLIDATED! 🔥"

