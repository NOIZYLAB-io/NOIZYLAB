#!/bin/bash
###############################################################################
# Start Network Agent Service
###############################################################################

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🚀 Starting NoizyLab Network Agent..."
echo "======================================"

# Configuration
SWITCH_IP="${DGS1210_IP:-192.168.1.1}"
SNMP_COMMUNITY="${SNMP_COMMUNITY:-public}"
MC96_PORTS="${MC96_PORTS:-1,2,3}"

echo ""
echo "⚙️  Configuration:"
echo "  Switch IP: $SWITCH_IP"
echo "  SNMP Community: $SNMP_COMMUNITY"
echo "  MC96 Ports: $MC96_PORTS"
echo ""

# Start Network Agent Service
echo "🔧 Starting Network Agent Service (port 8005)..."
python3 network_agent_service.py &
AGENT_PID=$!
echo "   PID: $AGENT_PID"

echo ""
echo "✅ Network Agent Started!"
echo ""
echo "📡 Endpoints:"
echo "  API: http://localhost:8005"
echo "  Health: http://localhost:8005/health"
echo "  Ports: http://localhost:8005/ports"
echo "  Devices: http://localhost:8005/devices"
echo "  MC96: http://localhost:8005/mc96/devices"
echo ""
echo "To stop service:"
echo "  kill $AGENT_PID"
echo ""

# Save PID
echo "$AGENT_PID" > network_agent.pid
echo "PID saved to network_agent.pid"

