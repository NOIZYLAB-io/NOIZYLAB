#!/bin/bash
# Drop a Log Pin - Add timestamped note
cd /Users/m2ultra/NOIZYLAB/backend
NOTE="${1:-Manual checkpoint}"
LOGFILE="../logs/nlctl-$(date +%Y%m%d).log"
TIMESTAMP=$(date +%Y-%m-%dT%H:%M:%S)
echo "$TIMESTAMP [USER-NOTE] $NOTE" >> "$LOGFILE"
echo "📌 Logged: $NOTE"
