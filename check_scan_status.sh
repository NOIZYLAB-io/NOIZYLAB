#!/bin/bash
# Quick status check for duplicate scan

echo "🔍 Checking duplicate scan status..."
echo ""

# Check if scanner is running
if pgrep -f duplicate_scanner.py > /dev/null; then
    echo "✅ Scan is RUNNING"
    echo ""
    echo "Process info:"
    ps aux | grep duplicate_scanner.py | grep -v grep | awk '{print "  PID:", $2, "| CPU:", $3"%", "| Memory:", $4"%"}'
else
    echo "❌ Scan is NOT running"
fi

echo ""
echo "📊 Recent scan activity:"
tail -5 ~/duplicate_scan_report.txt 2>/dev/null || echo "  No report file yet..."

echo ""
echo "💾 Disk usage on MAG 4TB:"
df -h "/Volumes/MAG 4TB" | tail -1

