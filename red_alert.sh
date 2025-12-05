#!/bin/bash
# RED ALERT - Full System Pulse
cd /Users/m2ultra/NOIZYLAB/backend
echo "🚨 RED ALERT - FULL SYSTEM PULSE 🚨"
echo ""
python3 nlctl.py status
echo ""
echo "════════════════════════════════════"
python3 nlctl.py ai-summary --lines 200
