#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# ⚡🚀 NOIZYLAB MEGA LAUNCHER 🚀⚡
# ═══════════════════════════════════════════════════════════════
# One command to rule them all!

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Paths
NOIZY_ROOT="/Users/m2ultra/NOIZYLAB"
GABRIEL_ROOT="$NOIZY_ROOT/GABRIEL/CODE"
CODEMASTER_ROOT="$NOIZY_ROOT/CODEMASTER"

clear

echo -e "${CYAN}"
cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║    ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗            ║
║    ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗           ║
║    ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝           ║
║    ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗           ║
║    ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝           ║
║    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝           ║
║                                                                               ║
║                      ⚡🚀 MEGA LAUNCHER 🚀⚡                                   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Menu
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}Choose your destiny:${NC}"
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  ${CYAN}1)${NC} 🚀 ${GREEN}TURBO GABRIEL${NC} - Launch interactive AI assistant"
echo -e "  ${CYAN}2)${NC} 🔧 ${GREEN}CODEMASTER${NC} - Start all services (local)"
echo -e "  ${CYAN}3)${NC} 🐳 ${GREEN}DOCKER MODE${NC} - Start with Docker Compose"
echo -e "  ${CYAN}4)${NC} 🧪 ${GREEN}TEST ALL${NC} - Run integration tests"
echo -e "  ${CYAN}5)${NC} 📊 ${GREEN}DASHBOARD${NC} - Show system status"
echo -e "  ${CYAN}6)${NC} 🛑 ${GREEN}STOP ALL${NC} - Stop all services"
echo -e "  ${CYAN}7)${NC} 🌐 ${GREEN}PORTAL${NC} - Open web portal"
echo -e "  ${CYAN}q)${NC} 👋 ${YELLOW}EXIT${NC}"
echo ""
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo -n "Enter choice [1-7, q]: "

read -r choice

case "$choice" in
    1)
        echo -e "\n${GREEN}⚡ Launching TURBO GABRIEL...${NC}\n"
        cd "$GABRIEL_ROOT"
        python3 TURBO_GABRIEL_ULTIMATE.py
        ;;
    2)
        echo -e "\n${GREEN}🔧 Starting CODEMASTER (local)...${NC}\n"
        cd "$CODEMASTER_ROOT"
        python3 run_local.py
        ;;
    3)
        echo -e "\n${GREEN}🐳 Starting CODEMASTER (Docker)...${NC}\n"
        cd "$CODEMASTER_ROOT"
        ./start.sh
        ;;
    4)
        echo -e "\n${GREEN}🧪 Running integration tests...${NC}\n"
        cd "$CODEMASTER_ROOT"
        python3 test_integration.py
        ;;
    5)
        "$NOIZY_ROOT/dashboard.sh"
        ;;
    6)
        echo -e "\n${YELLOW}🛑 Stopping all services...${NC}\n"
        
        # Stop local Python services
        echo "Stopping local services..."
        cd "$CODEMASTER_ROOT" 2>/dev/null && python3 run_local.py --stop 2>/dev/null || true
        
        # Stop Docker services
        echo "Stopping Docker services..."
        cd "$CODEMASTER_ROOT/infra/compose" 2>/dev/null && docker compose down 2>/dev/null || true
        
        echo -e "\n${GREEN}✓ All services stopped${NC}\n"
        ;;
    7)
        echo -e "\n${GREEN}🌐 Opening portal...${NC}\n"
        open "http://localhost:8080"
        ;;
    q|Q)
        echo -e "\n${YELLOW}👋 Goodbye!${NC}\n"
        exit 0
        ;;
    *)
        echo -e "\n${RED}Unknown option. Try again.${NC}\n"
        exec "$0"
        ;;
esac
