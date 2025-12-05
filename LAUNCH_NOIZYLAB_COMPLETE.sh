#!/bin/bash
################################################################################
# NoizyLab Complete System Launcher
################################################################################
# Launches all NoizyLab services including:
# - Master Dashboard
# - Slack Integration (API + Dashboard)
# - Network Agent (DGS1210 monitoring)
# - Email Intelligence
# - All supporting services
################################################################################

set -e

NOIZYLAB_ROOT="/Users/m2ultra/NOIZYLAB"
cd "$NOIZYLAB_ROOT"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ASCII Art
echo -e "${PURPLE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗██████╗║
║   ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╔══██╗║
║   ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████████╔╝║
║   ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══████╔══╝ ║
║   ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ████║    ║
║   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╚═╝    ║
║                                                               ║
║              Complete System Launcher v1.0                   ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
echo -e "${CYAN}🚀 Starting NoizyLab Complete System...${NC}"
echo ""

# Check environment
echo -e "${BLUE}📋 Checking environment...${NC}"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python 3 found${NC}"

# Check Slack configuration
if [ -z "$SLACK_BOT_TOKEN" ]; then
    echo -e "${YELLOW}⚠️  SLACK_BOT_TOKEN not set${NC}"
    echo -e "   ${YELLOW}Slack integration will be disabled${NC}"
    SLACK_ENABLED=false
else
    echo -e "${GREEN}✅ Slack configured${NC}"
    SLACK_ENABLED=true
fi

# Check Network Agent configuration
DGS1210_IP="${DGS1210_IP:-192.168.1.1}"
SNMP_COMMUNITY="${SNMP_COMMUNITY:-public}"
MC96_PORTS="${MC96_PORTS:-1,2,3}"

echo -e "${GREEN}✅ Network Agent configured (Switch: $DGS1210_IP)${NC}"

echo ""
echo -e "${CYAN}🎬 Launching services...${NC}"
echo ""

# Store PIDs
PIDS=()

# Function to start service
start_service() {
    local name=$1
    local command=$2
    local port=$3
    
    echo -e "${BLUE}🔧 Starting $name...${NC}"
    eval "$command" &
    local pid=$!
    PIDS+=($pid)
    echo -e "${GREEN}   ✅ Started (PID: $pid, Port: $port)${NC}"
    sleep 2
}

# 1. Start Slack API Server
if [ "$SLACK_ENABLED" = true ]; then
    start_service \
        "Slack API Server" \
        "cd $NOIZYLAB_ROOT/integrations/slack && python3 slack_api_server.py" \
        "8003"
fi

# 2. Start Network Agent
start_service \
    "Network Agent (DGS1210)" \
    "cd $NOIZYLAB_ROOT/network && python3 network_agent_service.py" \
    "8005"

# 3. Start Slack Dashboard
if [ "$SLACK_ENABLED" = true ]; then
    start_service \
        "Slack Dashboard" \
        "cd $NOIZYLAB_ROOT/integrations/slack && streamlit run slack_dashboard.py --server.port 8506 --server.headless true" \
        "8506"
fi

# 4. Start Master Dashboard
start_service \
    "Master Dashboard" \
    "cd $NOIZYLAB_ROOT/master-dashboard && streamlit run master-dashboard.py --server.port 8501 --server.headless true" \
    "8501"

# Wait for services to start
echo ""
echo -e "${CYAN}⏳ Waiting for services to initialize...${NC}"
sleep 5

# Health checks
echo ""
echo -e "${CYAN}🏥 Running health checks...${NC}"
echo ""

check_service() {
    local name=$1
    local url=$2
    
    if curl -s "$url" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ $name${NC}"
        return 0
    else
        echo -e "${RED}❌ $name (not responding)${NC}"
        return 1
    fi
}

# Check Master Dashboard
check_service "Master Dashboard" "http://localhost:8501"

# Check Slack services
if [ "$SLACK_ENABLED" = true ]; then
    check_service "Slack API" "http://localhost:8003/health"
    check_service "Slack Dashboard" "http://localhost:8506"
fi

# Check Network Agent
check_service "Network Agent" "http://localhost:8005/health"

# Display status
echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🎉 NoizyLab System Launched Successfully!${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${CYAN}📡 Access Points:${NC}"
echo ""
echo -e "  ${GREEN}🎛️  Master Dashboard:${NC}      http://localhost:8501"
if [ "$SLACK_ENABLED" = true ]; then
    echo -e "  ${GREEN}💬 Slack Dashboard:${NC}       http://localhost:8506"
    echo -e "  ${GREEN}📨 Slack API:${NC}             http://localhost:8003"
fi
echo -e "  ${GREEN}🌐 Network Agent:${NC}         http://localhost:8005"
echo ""

echo -e "${CYAN}🔌 Network Monitoring:${NC}"
echo ""
echo -e "  Switch IP: $DGS1210_IP"
echo -e "  MC96 Ports: $MC96_PORTS"
echo -e "  ${GREEN}✅ Auto-handshake enabled${NC}"
echo ""

if [ "$SLACK_ENABLED" = true ]; then
    echo -e "${CYAN}💬 Slack Integration:${NC}"
    echo ""
    echo -e "  ${GREEN}✅ Real-time notifications enabled${NC}"
    echo -e "  Channels:"
    echo -e "    • Alerts: ${SLACK_ALERTS_CHANNEL:-#noizylab-alerts}"
    echo -e "    • Monitoring: ${SLACK_MONITORING_CHANNEL:-#noizylab-monitor}"
    echo -e "    • Network: ${SLACK_NETWORK_CHANNEL:-#noizylab-network}"
    echo ""
fi

echo -e "${CYAN}🎯 What's Running:${NC}"
echo ""
echo -e "  ${GREEN}✅${NC} Master control dashboard"
if [ "$SLACK_ENABLED" = true ]; then
    echo -e "  ${GREEN}✅${NC} Slack notifications & commands"
fi
echo -e "  ${GREEN}✅${NC} DGS1210 port monitoring"
echo -e "  ${GREEN}✅${NC} Automatic device detection"
echo -e "  ${GREEN}✅${NC} MC96 auto-handshake system"
echo ""

echo -e "${CYAN}🔍 Test It:${NC}"
echo ""
if [ "$SLACK_ENABLED" = true ]; then
    echo -e "  ${YELLOW}# Send test Slack notification${NC}"
    echo -e "  curl -X POST http://localhost:8003/notify/system-alert \\"
    echo -e "    -H 'Content-Type: application/json' \\"
    echo -e "    -d '{\"title\":\"Test\",\"message\":\"System online!\",\"level\":\"success\"}'"
    echo ""
fi
echo -e "  ${YELLOW}# Check network status${NC}"
echo -e "  curl http://localhost:8005/ports | jq"
echo ""
echo -e "  ${YELLOW}# Plug a device into your DGS1210 and watch the magic! 🪄${NC}"
echo ""

echo -e "${CYAN}🛑 To Stop All Services:${NC}"
echo ""
echo -e "  kill ${PIDS[@]}"
echo ""

# Save PIDs
echo "${PIDS[@]}" > "$NOIZYLAB_ROOT/.noizylab_pids"
echo -e "${BLUE}PIDs saved to .noizylab_pids${NC}"

# Setup trap for cleanup
cleanup() {
    echo ""
    echo -e "${YELLOW}🛑 Shutting down NoizyLab services...${NC}"
    for pid in "${PIDS[@]}"; do
        if kill -0 $pid 2>/dev/null; then
            echo -e "${BLUE}   Stopping PID $pid...${NC}"
            kill $pid 2>/dev/null || true
        fi
    done
    echo -e "${GREEN}✅ All services stopped${NC}"
    exit 0
}

trap cleanup SIGINT SIGTERM

echo -e "${GREEN}✨ NoizyLab is ready! Press Ctrl+C to stop all services.${NC}"
echo ""

# Keep script running
wait

