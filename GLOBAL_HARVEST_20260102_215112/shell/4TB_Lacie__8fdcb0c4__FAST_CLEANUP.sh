#!/usr/bin/env bash
# FAST CLEANUP - Quick organization without heavy scanning

set -e

NOIZYLAB="/Users/m2ultra/NOIZYLAB"
SCRIPTS="$NOIZYLAB/scripts"
DOCS="$NOIZYLAB/docs"
ARCHIVE="$NOIZYLAB/.archive/old-versions"

echo "🚀 FAST NOIZYLAB CLEANUP"
echo "=========================="
echo ""

# Create directories
mkdir -p "$SCRIPTS" "$DOCS" "$ARCHIVE"

moved=0

# Move scripts (quick, no scanning)
echo "📦 Moving scripts..."
for f in "$NOIZYLAB"/*.sh; do
    if [ -f "$f" ]; then
        basename=$(basename "$f")
        if [[ "$basename" != "FAST_CLEANUP.sh" && "$basename" != "MASTER_CLEANUP_ORGANIZER.sh" && "$basename" != "media_offload.sh" ]]; then
            mv "$f" "$SCRIPTS/" 2>/dev/null && echo "  ✓ $basename" && moved=$((moved + 1)) || true
        fi
    fi
done

# Move Python scripts
echo "📦 Moving Python scripts..."
for f in "$NOIZYLAB"/*.py; do
    if [ -f "$f" ]; then
        basename=$(basename "$f")
        if [[ ! "$basename" =~ ^(QUICK_ORGANIZE|disk_usage_analyzer|CHECK_AGENTS)\.py$ ]]; then
            mv "$f" "$SCRIPTS/" 2>/dev/null && echo "  ✓ $basename" && moved=$((moved + 1)) || true
        fi
    fi
done

# Move docs (keep README.md)
echo "📄 Moving documentation..."
for f in "$NOIZYLAB"/*.md; do
    if [ -f "$f" ]; then
        basename=$(basename "$f")
        if [[ "$basename" != "README.md" && "$basename" != "STRUCTURE.md" ]]; then
            mv "$f" "$DOCS/" 2>/dev/null && echo "  ✓ $basename" && moved=$((moved + 1)) || true
        fi
    fi
done

# Archive versioned scripts
echo "📦 Archiving old versions..."
for f in "$NOIZYLAB"/*_V*.sh "$NOIZYLAB"/*_V*.py; do
    if [ -f "$f" ]; then
        mv "$f" "$ARCHIVE/" 2>/dev/null && echo "  ✓ $(basename "$f")" && moved=$((moved + 1)) || true
    fi
done

# Quick cleanup
echo "🧹 Quick cleanup..."
find "$NOIZYLAB" -name ".DS_Store" -delete 2>/dev/null || true
echo "  ✓ Removed .DS_Store files"

echo ""
echo "✅ DONE! Moved $moved files"
echo ""
echo "Your agents:"
echo "  🟣 GABRIEL: node $NOIZYLAB/gabriel-cli.mjs"
echo "  🔵 MC96: node $NOIZYLAB/mc96-cli.mjs"
echo ""
echo "To check what's running: python3 $NOIZYLAB/CHECK_AGENTS.py"

