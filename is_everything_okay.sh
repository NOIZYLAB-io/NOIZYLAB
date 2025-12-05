#!/bin/bash
# Is Everything Okay? - Voice-friendly check
cd /Users/m2ultra/NOIZYLAB/backend
echo "🤔 IS EVERYTHING OKAY?"
echo ""
STATUS=$(python3 nlctl.py status 2>&1)
echo "$STATUS"

# Count failures
FAILS=$(echo "$STATUS" | grep -c "FAIL")
if [ "$FAILS" -eq 0 ]; then
    echo ""
    echo "✅ ALL SYSTEMS OPERATIONAL!"
    say "All systems operational" 2>/dev/null
else
    echo ""
    echo "⚠️ $FAILS SYSTEM(S) DOWN!"
    say "$FAILS systems down" 2>/dev/null
fi
