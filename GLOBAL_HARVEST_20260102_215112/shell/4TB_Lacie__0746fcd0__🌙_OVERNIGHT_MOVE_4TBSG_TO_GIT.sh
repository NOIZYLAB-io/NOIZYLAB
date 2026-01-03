#!/bin/bash
###############################################################################
# 🌙 OVERNIGHT MOVE - 4TBSG → GITHUB/NOIZYFISH/NOIZYLAB
# Moves ALL code while ROB sleeps!
# GONE BY MORNING!!!
###############################################################################

echo "🌙 OVERNIGHT MOVE STARTING - 4TBSG → GITHUB!!!"
echo ""
echo "CB_01 working while ROB sleeps..."
echo "By morning: ALL CODE IN GIT!!! ✅"
echo ""

SOURCE="/Volumes/4TBSG"
DEST="$HOME/Github/Noizyfish/NOIZYLAB"

echo "📂 Creating destination structure..."
mkdir -p "$DEST"

echo "✅ Destination ready!"
echo ""

echo "⚡ MOVING ALL CODE & PROJECTS..."
echo ""

# Move NOIZYLAB folder
if [ -d "$SOURCE/NOIZYLAB" ]; then
    echo "📁 Moving: NOIZYLAB folder..."
    rsync -av --progress "$SOURCE/NOIZYLAB/" "$DEST/4TBSG_NOIZYLAB/" >> /tmp/overnight_move.log 2>&1
    echo "   ✅ NOIZYLAB moved!"
fi

# Move Projects
if [ -d "$SOURCE/Projects" ]; then
    echo "📁 Moving: Projects folder..."
    rsync -av --progress "$SOURCE/Projects/" "$DEST/4TBSG_PROJECTS/" >> /tmp/overnight_move.log 2>&1
    echo "   ✅ Projects moved!"
fi

# Move 2026_SFX
if [ -d "$SOURCE/2026_SFX" ]; then
    echo "📁 Moving: 2026_SFX..."
    rsync -av --progress "$SOURCE/2026_SFX/" "$DEST/4TBSG_SFX/" >> /tmp/overnight_move.log 2>&1
    echo "   ✅ SFX moved!"
fi

# Move FACTORY_FRESH_ORGANIZED
if [ -d "$SOURCE/FACTORY_FRESH_ORGANIZED" ]; then
    echo "📁 Moving: FACTORY_FRESH_ORGANIZED..."
    rsync -av --progress "$SOURCE/FACTORY_FRESH_ORGANIZED/" "$DEST/4TBSG_ORGANIZED/" >> /tmp/overnight_move.log 2>&1
    echo "   ✅ Organized content moved!"
fi

# Move documentation
if [ -d "$SOURCE/DOCUMENTATION" ]; then
    echo "📁 Moving: DOCUMENTATION..."
    rsync -av --progress "$SOURCE/DOCUMENTATION/" "$DEST/4TBSG_DOCS/" >> /tmp/overnight_move.log 2>&1
    echo "   ✅ Documentation moved!"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ OVERNIGHT MOVE COMPLETE!!!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📂 All code now in: $DEST/"
echo "📋 Full log: /tmp/overnight_move.log"
echo ""
echo "🌅 BY MORNING: 4TBSG CODE = GONE TO GIT!!!"
echo ""
echo "💜 CB_01 worked while ROB slept!"
echo "✅ Everything organized in Github!"
echo ""
echo "GORUNFREE X1000!!! 🚀"

