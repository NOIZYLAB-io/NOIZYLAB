#!/bin/bash
# Quick scan of 4TBSG for code files and consolidate to NOIZYLAB

echo "================================"
echo "4TBSG CODE SCANNER"
echo "================================"

SOURCE="/Volumes/4TBSG"
TARGET="/Users/m2ultra/NOIZYLAB/CODE_FROM_4TBSG"

echo ""
echo "📍 Source: $SOURCE"
echo "📍 Target: $TARGET"
echo ""

# Create target directory
mkdir -p "$TARGET"

echo "🔍 Scanning for code files..."
echo ""

# Count files by type
echo "Python files:"
PY_COUNT=$(find "$SOURCE" -name "*.py" -type f 2>/dev/null | wc -l | tr -d ' ')
echo "  Found: $PY_COUNT files"

echo "JavaScript files:"
JS_COUNT=$(find "$SOURCE" -name "*.js" -type f 2>/dev/null | wc -l | tr -d ' ')
echo "  Found: $JS_COUNT files"

echo "Shell scripts:"
SH_COUNT=$(find "$SOURCE" -name "*.sh" -type f 2>/dev/null | wc -l | tr -d ' ')
echo "  Found: $SH_COUNT files"

echo "TypeScript files:"
TS_COUNT=$(find "$SOURCE" -name "*.ts" -type f 2>/dev/null | wc -l | tr -d ' ')
echo "  Found: $TS_COUNT files"

TOTAL=$((PY_COUNT + JS_COUNT + SH_COUNT + TS_COUNT))
echo ""
echo "✅ Total code files: $TOTAL"
echo ""

# Show top-level directories with code
echo "📁 Code locations:"
find "$SOURCE" -maxdepth 2 -type d -not -path "*/.*" 2>/dev/null | while read dir; do
    CODE_IN_DIR=$(find "$dir" -maxdepth 1 -type f \( -name "*.py" -o -name "*.js" -o -name "*.sh" \) 2>/dev/null | wc -l | tr -d ' ')
    if [ "$CODE_IN_DIR" -gt 0 ]; then
        echo "  $dir: $CODE_IN_DIR files"
    fi
done

echo ""
echo "Ready to consolidate? Run with --execute to copy all code to NOIZYLAB"
