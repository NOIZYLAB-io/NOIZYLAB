#!/bin/bash
# 📊 DASHBOARD - SYSTEM MONITORING
# Fish Music Inc - CB_01

echo "📊 Starting system dashboard..."

# Check if Netdata installed
if ! command -v netdata >/dev/null 2>&1; then
    echo "[+] Installing Netdata..."
    brew install netdata
fi

# Start Netdata
brew services start netdata >/dev/null 2>&1

sleep 2

if lsof -i :19999 >/dev/null 2>&1; then
    echo "✅ Dashboard online!"
    echo ""
    echo "🌐 Access at: http://localhost:19999"
    echo ""
    echo "Metrics available:"
    echo "  • CPU usage (per-core)"
    echo "  • RAM usage"
    echo "  • Disk I/O"
    echo "  • Network traffic"
    echo "  • Process list"
    echo "  • GPU stats (if supported)"
else
    echo "❌ Dashboard failed to start"
    echo "   Manual start: brew services start netdata"
fi

echo ""
