#!/bin/bash
# INSTANT Superior Drummer 3 Info - Ultra Fast!

SD3="/Volumes/MAG 4TB/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3"

cat << 'EOF'
╔════════════════════════════════════════════════════════════════╗
║          🥁 SUPERIOR DRUMMER 3 - INSTANT ACCESS 🥁             ║
╚════════════════════════════════════════════════════════════════╝

📍 MAIN LOCATION:
EOF

echo "   $SD3"
echo ""
echo "🎵 GROOVE CATEGORIES:"
echo ""

# Quick counts using cached find
echo "   📂 Ballad (200@)       : $(find "$SD3" -path "*200@*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo "   📂 Half-Time (300@)    : $(find "$SD3" -path "*300@*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo "   📂 Midtempo (400@)     : $(find "$SD3" -path "*400@*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves ⭐"
echo "   📂 Uptempo (500@)      : $(find "$SD3" -path "*500@*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo "   📂 Extras (600@)       : $(find "$SD3" -path "*600@*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo ""

echo "⚡ QUICK CATEGORIES:"
echo ""
echo "   🥁 Straight 4/4       : $(find "$SD3" -path "*STRAIGHT*4#4*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo "   🎺 Swing 4/4          : $(find "$SD3" -path "*SWING*4#4*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo "   🎸 Brushes            : $(find "$SD3" -path "*BRUSHES*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo "   🥁 Snare Rolls        : $(find "$SD3" -path "*SNARE*ROLL*" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ') grooves"
echo ""

TOTAL=$(find "$SD3" -name "*.mid" 2>/dev/null | wc -l | tr -d ' ')
SIZE=$(du -sh "$SD3" 2>/dev/null | awk '{print $1}')

echo "📊 TOTAL: $TOTAL grooves | Size: $SIZE"
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "🚀 QUICK ACTIONS:"
echo ""
echo "  1. Browse all:    open \"$SD3\""
echo "  2. List all:      ls -R \"$SD3\" | grep .mid"
echo "  3. Find by tempo: grep -r '120' \"$SD3\""
echo ""
echo "═══════════════════════════════════════════════════════════════"
EOF

