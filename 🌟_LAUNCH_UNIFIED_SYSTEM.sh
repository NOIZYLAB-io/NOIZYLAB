#!/bin/bash
################################################################################
# 🌟 NOIZYLAB UNIFIED SYSTEM - MASTER LAUNCHER 🌟
################################################################################
# Starts TypeScript CLI + Python Backend + ALL services!
# CURSE_BEAST_01 + CURSE_BEAST_02 = MAXIMUM POWER!
################################################################################

set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
PURPLE='\033[0;35m'
RED='\033[0;31m'
NC='\033[0m'

clear

echo -e "${PURPLE}"
cat << "EOF"
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║        🌟 NOIZYLAB UNIFIED SYSTEM 🌟                      ║
║                                                            ║
║   TypeScript + Python = ULTIMATE PLATFORM                ║
║   CURSE_BEAST_01 + CURSE_BEAST_02 = MAXIMUM POWER        ║
║                                                            ║
║   "YestTomora — timeless wisdom, future-forward"         ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
echo -e "${CYAN}🚀 Starting COMPLETE UNIFIED SYSTEM...${NC}"
echo ""

cd /Users/m2ultra/NOIZYLAB

PIDS=()

# 1. Python Slack API
echo -e "${GREEN}1️⃣ Slack API (Python)...${NC}"
cd integrations/slack && python3 slack_api_server.py &
PIDS+=($!)
cd ../..

# 2. Network Agent
echo -e "${GREEN}2️⃣ Network Agent (MC96 Universe)...${NC}"
cd network && python3 network_agent_service.py &
PIDS+=($!)
cd ..

# 3. Unified Integration API
echo -e "${GREEN}3️⃣ Unified Integration API...${NC}"
python3 🌟_unified_integration_api.py &
PIDS+=($!)

# 4. Master Dashboard
echo -e "${GREEN}4️⃣ Master Dashboard...${NC}"
cd master-dashboard && streamlit run master-dashboard.py --server.port 8501 --server.headless true &
PIDS+=($!)
cd ..

# 5. Slack Dashboard
echo -e "${GREEN}5️⃣ Slack Dashboard...${NC}"
cd integrations/slack && streamlit run slack_dashboard.py --server.port 8506 --server.headless true &
PIDS+=($!)
cd ../..

sleep 5

echo ""
echo -e "${PURPLE}════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ NOIZYLAB UNIFIED SYSTEM ONLINE!${NC}"
echo -e "${PURPLE}════════════════════════════════════════════════${NC}"
echo ""

echo -e "${CYAN}📡 Access Points:${NC}"
echo ""
echo "  🎛️  Master Dashboard:       http://localhost:8501"
echo "  💬 Slack Dashboard:        http://localhost:8506"
echo "  🌟 Unified API:            http://localhost:8007"
echo "  📡 Slack API:              http://localhost:8003"
echo "  🌐 Network Agent:          http://localhost:8005"
echo ""

echo -e "${CYAN}💻 TypeScript CLI:${NC}"
echo "  npx noizylab setup         # Validate config"
echo "  npx noizylab email welcome # Send email"
echo "  npx noizylab users list    # List users"
echo "  npx noizylab alerts        # Slack alerts"
echo ""

echo -e "${CYAN}🐍 Python CLI:${NC}"
echo "  python3 noizylab_cli.py status    # System status"
echo "  python3 noizylab_cli.py network   # Network ops"
echo "  python3 noizylab_cli.py ai chat   # AI assistant"
echo "  python3 noizylab_cli.py universe  # MC96 Universe"
echo ""

echo -e "${CYAN}🦁 Curse Beasts:${NC}"
echo "  💜 CURSE_BEAST_01: Infrastructure (Active)"
echo "  🎵 CURSE_BEAST_02: Music/Media (Active)"
echo ""

echo "🛑 Stop: kill ${PIDS[@]}"
echo ""

trap "kill ${PIDS[@]} 2>/dev/null; exit 0" SIGINT SIGTERM

wait
