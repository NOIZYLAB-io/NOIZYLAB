#!/bin/bash
# Client Session Start
CLIENT="${1:-Unknown Client}"
cd /Users/m2ultra/NOIZYLAB/backend
LOGFILE="../logs/nlctl-$(date +%Y%m%d).log"
TIMESTAMP=$(date +%Y-%m-%dT%H:%M:%S)
echo "$TIMESTAMP [SESSION-START] Client: $CLIENT" >> "$LOGFILE"
echo "🚀 SESSION STARTED: $CLIENT"
python3 nlctl.py status
