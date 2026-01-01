#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════════════════════════╗
# ║                    🚀 CODEMASTER TURBO LAUNCHER 🚀                                 ║
# ╚═══════════════════════════════════════════════════════════════════════════════════╝

CODEMASTER_DIR="/Users/m2ultra/NOIZYLAB/CODEMASTER"
VENV="$CODEMASTER_DIR/.venv/bin/python"
SCRIPT="$CODEMASTER_DIR/codemaster_unified.py"
PORT=8000

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${CYAN}"
cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════════╗
║       ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗        ║
║      ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝        ║
║      ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║███████╗   ██║           ║
║      ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║           ║
║      ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║           ║
║       ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝           ║
║                    🚀 TURBO LAUNCHER v2.3.0 🚀                                     ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

case "$1" in
    start)
        echo -e "${GREEN}🚀 Starting CODEMASTER TURBO...${NC}"
        pkill -f codemaster_unified 2>/dev/null
        sleep 1
        cd "$CODEMASTER_DIR"
        nohup "$VENV" "$SCRIPT" > /tmp/codemaster.log 2>&1 &
        sleep 2
        if curl -s http://localhost:$PORT/health > /dev/null; then
            echo -e "${GREEN}✅ CODEMASTER is running on http://localhost:$PORT${NC}"
            echo -e "${CYAN}   Dashboard: http://localhost:$PORT${NC}"
            echo -e "${CYAN}   API Docs:  http://localhost:$PORT/docs${NC}"
            echo -e "${CYAN}   Health:    http://localhost:$PORT/health${NC}"
        else
            echo -e "${YELLOW}⚠️ CODEMASTER may still be starting. Check /tmp/codemaster.log${NC}"
        fi
        ;;
    
    stop)
        echo -e "${YELLOW}🛑 Stopping CODEMASTER...${NC}"
        pkill -f codemaster_unified
        echo -e "${GREEN}✅ CODEMASTER stopped${NC}"
        ;;
    
    restart)
        "$0" stop
        sleep 1
        "$0" start
        ;;
    
    status)
        if curl -s http://localhost:$PORT/health > /dev/null 2>&1; then
            echo -e "${GREEN}✅ CODEMASTER is running${NC}"
            curl -s http://localhost:$PORT/health | python3 -m json.tool
        else
            echo -e "${YELLOW}❌ CODEMASTER is not running${NC}"
        fi
        ;;
    
    logs)
        tail -f /tmp/codemaster.log
        ;;
    
    turbo)
        echo -e "${CYAN}⚡ TURBO ENGINE STATUS:${NC}"
        curl -s http://localhost:$PORT/turbo/ | python3 -m json.tool
        ;;
    
    swarm)
        echo -e "${CYAN}🐟 SWARM STATUS:${NC}"
        curl -s http://localhost:$PORT/swarm/agents | python3 -m json.tool
        ;;
    
    brain)
        echo -e "${CYAN}🧠 AI BRAIN STATUS:${NC}"
        curl -s http://localhost:$PORT/ai/brain | python3 -m json.tool
        ;;
    
    *)
        echo "Usage: $0 {start|stop|restart|status|logs|turbo|swarm|brain}"
        echo ""
        echo "Commands:"
        echo "  start   - Start CODEMASTER TURBO"
        echo "  stop    - Stop CODEMASTER"
        echo "  restart - Restart CODEMASTER"
        echo "  status  - Show health status"
        echo "  logs    - Tail the logs"
        echo "  turbo   - Show TURBO engine status"
        echo "  swarm   - Show SWARM agents status"
        echo "  brain   - Show AI Brain status"
        exit 1
        ;;
esac
