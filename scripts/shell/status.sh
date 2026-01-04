#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════════════════════════╗
# ║                    🔥 NOIZYLAB SYSTEM STATUS 🔥                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════════════╝

clear

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

echo -e "${CYAN}"
cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║    ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗                  ║
║    ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗                 ║
║    ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝                 ║
║    ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗                 ║
║    ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝                 ║
║    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝                  ║
║                                                                                   ║
║                         ⚡ SYSTEM STATUS DASHBOARD ⚡                              ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Check CODEMASTER UNIFIED
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${WHITE}                          🏛️  CODEMASTER UNIFIED                                   ${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════════════${NC}"

HEALTH=$(curl -s http://localhost:8000/health 2>/dev/null)

if [ -n "$HEALTH" ]; then
    echo -e "${GREEN}  Status: 🟢 ONLINE${NC}"
    
    # Parse health JSON
    UPTIME=$(echo "$HEALTH" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d['uptime_seconds']:.0f}\")" 2>/dev/null || echo "?")
    UVLOOP=$(echo "$HEALTH" | python3 -c "import sys,json; d=json.load(sys.stdin); print('✅' if d['optimizations']['uvloop'] else '❌')" 2>/dev/null || echo "?")
    ORJSON=$(echo "$HEALTH" | python3 -c "import sys,json; d=json.load(sys.stdin); print('✅' if d['optimizations']['orjson'] else '❌')" 2>/dev/null || echo "?")
    
    echo -e "${CYAN}  Uptime: ${UPTIME}s | UVLOOP: ${UVLOOP} | ORJSON: ${ORJSON}${NC}"
    echo ""
    
    echo -e "${YELLOW}  ╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}  ║                           SERVICES STATUS                                    ║${NC}"
    echo -e "${YELLOW}  ╠══════════════════════════════════════════════════════════════════════════════╣${NC}"
    
    # Check each service
    services=("vault:🔐 Vault" "catalog:📚 Catalog" "evidence:🔍 Evidence" "ai:🤖 AI Gateway" "fleet:🚀 Fleet" "mc96:🏛️ MC96" "mesh:🕸️ Mesh" "brain:🧠 GOD Brain" "metrics:📊 Metrics")
    
    for svc in "${services[@]}"; do
        path="${svc%%:*}"
        name="${svc#*:}"
        
        response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/${path}/" 2>/dev/null)
        
        if [ "$response" = "200" ]; then
            echo -e "${YELLOW}  ║  ${GREEN}🟢 ${name}${NC}${YELLOW} - ONLINE (/${path}/)                                      ║${NC}"
        else
            echo -e "${YELLOW}  ║  ${RED}🔴 ${name}${NC}${YELLOW} - OFFLINE                                                   ║${NC}"
        fi
    done
    
    echo -e "${YELLOW}  ╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    
    # Get metrics
    METRICS=$(curl -s http://localhost:8000/metrics/ 2>/dev/null)
    if [ -n "$METRICS" ]; then
        echo ""
        echo -e "${BLUE}  ╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${BLUE}  ║                              METRICS                                         ║${NC}"
        echo -e "${BLUE}  ╠══════════════════════════════════════════════════════════════════════════════╣${NC}"
        
        TOTAL_REQ=$(echo "$METRICS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['total_requests'])" 2>/dev/null || echo "0")
        AVG_LAT=$(echo "$METRICS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d['average_latency_ms']:.2f}\")" 2>/dev/null || echo "0")
        VAULT=$(echo "$METRICS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['memory']['vault_items'])" 2>/dev/null || echo "0")
        AGENTS=$(echo "$METRICS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['memory']['agents'])" 2>/dev/null || echo "0")
        MISSIONS=$(echo "$METRICS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['memory']['missions'])" 2>/dev/null || echo "0")
        
        echo -e "${BLUE}  ║  📊 Total Requests: ${TOTAL_REQ}                                                     ║${NC}"
        echo -e "${BLUE}  ║  ⚡ Avg Latency: ${AVG_LAT}ms                                                      ║${NC}"
        echo -e "${BLUE}  ║  🔐 Vault Items: ${VAULT}                                                           ║${NC}"
        echo -e "${BLUE}  ║  🚀 Agents: ${AGENTS}                                                               ║${NC}"
        echo -e "${BLUE}  ║  🎯 Missions: ${MISSIONS}                                                           ║${NC}"
        echo -e "${BLUE}  ╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    fi
else
    echo -e "${RED}  Status: 🔴 OFFLINE${NC}"
    echo -e "${YELLOW}  Start with: cd /Users/m2ultra/NOIZYLAB/CODEMASTER && python3 codemaster_unified.py &${NC}"
fi

echo ""
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${WHITE}                            🔥 TURBO GABRIEL                                       ${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════════════${NC}"

# Check if TURBO files exist
TURBO_DIR="/Users/m2ultra/NOIZYLAB/GABRIEL/CODE"

if [ -f "$TURBO_DIR/TURBO_GABRIEL_GODMODE.py" ]; then
    echo -e "${GREEN}  GOD MODE:    ✅ Ready - ${TURBO_DIR}/TURBO_GABRIEL_GODMODE.py${NC}"
else
    echo -e "${RED}  GOD MODE:    ❌ Not Found${NC}"
fi

if [ -f "$TURBO_DIR/TURBO_GABRIEL_ULTIMATE.py" ]; then
    echo -e "${GREEN}  ULTIMATE:    ✅ Ready - ${TURBO_DIR}/TURBO_GABRIEL_ULTIMATE.py${NC}"
else
    echo -e "${RED}  ULTIMATE:    ❌ Not Found${NC}"
fi

if [ -f "$TURBO_DIR/turbo.sh" ]; then
    echo -e "${GREEN}  LAUNCHER:    ✅ Ready - ${TURBO_DIR}/turbo.sh${NC}"
else
    echo -e "${RED}  LAUNCHER:    ❌ Not Found${NC}"
fi

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${WHITE}  📖 API Docs:     http://localhost:8000/docs${NC}"
echo -e "${WHITE}  🌐 Dashboard:    http://localhost:8000/${NC}"
echo -e "${WHITE}  ❤️  Health:       http://localhost:8000/health${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}  Quick Commands:${NC}"
echo -e "${WHITE}  • Start CODEMASTER: cd /Users/m2ultra/NOIZYLAB/CODEMASTER && python3 codemaster_unified.py &${NC}"
echo -e "${WHITE}  • TURBO GOD MODE:   cd /Users/m2ultra/NOIZYLAB/GABRIEL/CODE && python3 TURBO_GABRIEL_GODMODE.py health${NC}"
echo -e "${WHITE}  • This Dashboard:   /Users/m2ultra/NOIZYLAB/status.sh${NC}"
echo ""
