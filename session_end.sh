#!/bin/bash
# Client Session End & Summary
CLIENT="${1:-Unknown Client}"
cd /Users/m2ultra/NOIZYLAB/backend
LOGFILE="../logs/nlctl-$(date +%Y%m%d).log"
TIMESTAMP=$(date +%Y-%m-%dT%H:%M:%S)
echo "$TIMESTAMP [SESSION-END] Client: $CLIENT" >> "$LOGFILE"

# Create summary file
SUMMARY_DIR="../sessions"
mkdir -p "$SUMMARY_DIR"
SUMMARY_FILE="$SUMMARY_DIR/${CLIENT}-$(date +%Y%m%d)-session.md"

echo "# Session Summary: $CLIENT" > "$SUMMARY_FILE"
echo "Date: $(date +%Y-%m-%d)" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"
echo "## System Status" >> "$SUMMARY_FILE"
python3 nlctl.py status >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"
echo "## AI Summary" >> "$SUMMARY_FILE"
python3 nlctl.py ai-summary --lines 200 >> "$SUMMARY_FILE"

echo "✅ SESSION ENDED: $CLIENT"
echo "📄 Summary saved: $SUMMARY_FILE"
