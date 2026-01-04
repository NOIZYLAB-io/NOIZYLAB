#!/bin/bash
# QUICK STATUS - Check all volumes FAST

echo "🔍 QUICK STATUS CHECK"
echo ""

for vol in "12TB" "RED DRAGON" "6TB" "4TB Lacie"; do
    echo -n "$vol: "
    if timeout 2 ls "/Volumes/$vol" >/dev/null 2>&1; then
        count=$(timeout 2 ls "/Volumes/$vol" 2>/dev/null | wc -l | tr -d ' ')
        echo "✓ FAST ($count items)"
    else
        echo "✗ SLOW/BLOCKED"
    fi
done

echo ""
echo "Spotlight status:"
mdutil -s /Volumes/12TB 2>/dev/null || echo "  (check failed)"
