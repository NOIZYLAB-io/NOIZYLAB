#!/bin/bash
# One-Tap Log Peek
LOGDIR="/Users/m2ultra/NOIZYLAB/logs"
LATEST=$(ls -t "$LOGDIR"/nlctl-*.log 2>/dev/null | head -1)
if [ -n "$LATEST" ]; then
    echo "📋 Opening: $LATEST"
    open -a TextEdit "$LATEST"
else
    echo "❌ No log files found"
fi
