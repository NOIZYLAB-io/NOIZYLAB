#!/bin/bash
# Daily Health Check
cd /Users/m2ultra/NOIZYLAB/backend
echo "☀️ DAILY HEALTH CHECK - $(date +%Y-%m-%d)"
echo ""
python3 nlctl.py status
echo ""
python3 nlctl.py ai-summary --lines 100
