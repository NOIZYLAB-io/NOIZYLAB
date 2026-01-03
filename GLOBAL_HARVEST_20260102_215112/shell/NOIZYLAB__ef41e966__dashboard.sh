#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# 🎮 NOIZYLAB MASTER CONTROL - System Dashboard
# ═══════════════════════════════════════════════════════════════

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
GABRIEL_ROOT="/Users/m2ultra/NOIZYLAB/GABRIEL"
CODEMASTER_ROOT="/Users/m2ultra/NOIZYLAB/CODEMASTER"

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
║                   🎮 MASTER CONTROL DASHBOARD 🎮                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# System Info
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}📊 SYSTEM STATUS${NC}"
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"

# Hardware
CPU_CORES=$(sysctl -n hw.ncpu 2>/dev/null || nproc 2>/dev/null || echo "?")
ARCH=$(uname -m)
MEM_TOTAL=$(sysctl -n hw.memsize 2>/dev/null)
if [ -n "$MEM_TOTAL" ]; then
    MEM_GB=$((MEM_TOTAL / 1024 / 1024 / 1024))
else
    MEM_GB="?"
fi

echo -e "\n${CYAN}🖥️  Hardware:${NC}"
echo -e "   CPU: ${GREEN}${CPU_CORES} cores${NC} (${ARCH})"
echo -e "   RAM: ${GREEN}${MEM_GB} GB${NC}"

if [[ "$ARCH" == "arm64" ]] && [[ "$CPU_CORES" -ge 20 ]]; then
    echo -e "   ${GREEN}🔥 M2 ULTRA DETECTED!${NC}"
fi

# Python/Dependencies
echo -e "\n${CYAN}🐍 Python Environment:${NC}"
PYTHON_VER=$(python3 --version 2>&1)
echo -e "   ${GREEN}${PYTHON_VER}${NC}"

# Check dependencies
for pkg in httpx psutil uvloop; do
    if python3 -c "import $pkg" 2>/dev/null; then
        echo -e "   ${GREEN}✓${NC} $pkg"
    else
        echo -e "   ${RED}✗${NC} $pkg (run: pip3 install $pkg)"
    fi
done

# GABRIEL Status
echo -e "\n${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}👼 GABRIEL STATUS${NC}"
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"

if [ -d "$GABRIEL_ROOT" ]; then
    echo -e "   📁 Location: ${GREEN}$GABRIEL_ROOT${NC}"
    
    # TURBO files
    echo -e "\n   ${CYAN}⚡ TURBO Files:${NC}"
    for turbo in TURBO_GABRIEL.py TURBO_GABRIEL_V2.py TURBO_GABRIEL_ULTIMATE.py; do
        if [ -f "$GABRIEL_ROOT/CODE/$turbo" ]; then
            size=$(ls -lh "$GABRIEL_ROOT/CODE/$turbo" | awk '{print $5}')
            echo -e "   ${GREEN}✓${NC} $turbo ($size)"
        else
            echo -e "   ${RED}✗${NC} $turbo"
        fi
    done
    
    # Turbo modules
    echo -e "\n   ${CYAN}📦 Turbo Modules:${NC}"
    MODULE_COUNT=$(find "$GABRIEL_ROOT/CODE/turbo" -name "*.py" 2>/dev/null | wc -l | tr -d ' ')
    echo -e "   ${GREEN}$MODULE_COUNT${NC} Python modules in turbo/"
else
    echo -e "   ${RED}✗ GABRIEL not found at $GABRIEL_ROOT${NC}"
fi

# CODEMASTER Status
echo -e "\n${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}🔧 CODEMASTER STATUS${NC}"
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"

if [ -d "$CODEMASTER_ROOT" ]; then
    echo -e "   📁 Location: ${GREEN}$CODEMASTER_ROOT${NC}"
    
    # Services
    echo -e "\n   ${CYAN}🚀 Microservices:${NC}"
    for svc in vault catalog evidence ai_gateway fleet mc96 mesh observability god_brain; do
        svc_file=$(find "$CODEMASTER_ROOT" -name "*${svc}*.py" 2>/dev/null | head -1)
        if [ -n "$svc_file" ]; then
            echo -e "   ${GREEN}✓${NC} $svc"
        else
            echo -e "   ${YELLOW}?${NC} $svc"
        fi
    done
    
    # Portal
    echo -e "\n   ${CYAN}🌐 Portal:${NC}"
    if [ -f "$CODEMASTER_ROOT/apps/portal/src/portal.py" ]; then
        echo -e "   ${GREEN}✓${NC} portal.py"
    fi
    
    TEMPLATE_COUNT=$(find "$CODEMASTER_ROOT/apps/portal/templates" -name "*.html" 2>/dev/null | wc -l | tr -d ' ')
    echo -e "   ${GREEN}$TEMPLATE_COUNT${NC} HTML templates"
    
    # Docker
    echo -e "\n   ${CYAN}🐳 Docker:${NC}"
    if [ -f "$CODEMASTER_ROOT/infra/compose/docker-compose.yml" ]; then
        echo -e "   ${GREEN}✓${NC} docker-compose.yml"
    fi
else
    echo -e "   ${RED}✗ CODEMASTER not found at $CODEMASTER_ROOT${NC}"
fi

# Service Health Check
echo -e "\n${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}🏥 SERVICE HEALTH (localhost)${NC}"
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"

check_service() {
    local name=$1
    local port=$2
    if curl -s --connect-timeout 1 "http://localhost:$port/health" >/dev/null 2>&1; then
        echo -e "   ${GREEN}●${NC} $name (port $port)"
    else
        echo -e "   ${RED}○${NC} $name (port $port)"
    fi
}

echo -e "\n   ${CYAN}CODEMASTER Services:${NC}"
check_service "Vault" 8000
check_service "Catalog" 8001
check_service "Evidence" 8002
check_service "AI Gateway" 8100
check_service "Fleet" 8200
check_service "MC96" 8300
check_service "Mesh" 8400
check_service "GOD Brain" 8500
check_service "Observability" 9090
check_service "Portal" 8080

# Quick Actions
echo -e "\n${WHITE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}⚡ QUICK ACTIONS${NC}"
echo -e "${WHITE}═══════════════════════════════════════════════════════════════${NC}"

echo -e "\n   ${CYAN}Launch TURBO:${NC}"
echo -e "   ./turbo.sh              # Interactive TURBO shell"
echo -e "   ./turbo.sh health       # Health check"
echo -e "   python3 TURBO_GABRIEL_ULTIMATE.py"

echo -e "\n   ${CYAN}Start CODEMASTER:${NC}"
echo -e "   cd $CODEMASTER_ROOT/infra/compose"
echo -e "   docker compose up -d"

echo -e "\n   ${CYAN}View Portal:${NC}"
echo -e "   open http://localhost:8080"

echo -e "\n${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${WHITE}                    🚀 SYSTEM READY 🚀                          ${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
