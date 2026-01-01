#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════════════════════════╗
# ║                    🚀 CODEMASTER MEGA LAUNCHER 🚀                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════╝

CODEMASTER_DIR="/Users/m2ultra/NOIZYLAB/CODEMASTER"
VENV="$CODEMASTER_DIR/.venv/bin/python"
SCRIPT="$CODEMASTER_DIR/codemaster_unified.py"
PORT=8000

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
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
║              ⚡ MEGA LAUNCHER v2.4.0 - HYPERVELOCITY EDITION ⚡                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

case "$1" in
    start)
        echo -e "${GREEN}🚀 Starting CODEMASTER MEGA...${NC}"
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
            echo -e "${CYAN}   MEGA:      http://localhost:$PORT/mega/${NC}"
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
            curl -s http://localhost:$PORT/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'VERSION: {d[\"version\"]}'); print(f'SERVICES: {len(d[\"services\"])} online'); print(f'SWARM: {d[\"swarm\"][\"agents\"]} agents'); print(f'MEGA: {d[\"mega\"][\"hypervelocity\"]}')"
        else
            echo -e "${YELLOW}❌ CODEMASTER is not running${NC}"
        fi
        ;;
    
    logs)
        tail -f /tmp/codemaster.log
        ;;
    
    mega)
        echo -e "${CYAN}⚡ MEGA ENGINE STATUS:${NC}"
        curl -s http://localhost:$PORT/mega/status | python3 -m json.tool
        ;;
    
    scan)
        PATH_ARG="${2:-/Users/m2ultra/NOIZYLAB}"
        DEPTH_ARG="${3:-10}"
        echo -e "${CYAN}⚡ MEGA SCAN: $PATH_ARG (depth: $DEPTH_ARG)${NC}"
        curl -s -X POST http://localhost:$PORT/mega/scan \
            -H "Content-Type: application/json" \
            -d "{\"path\": \"$PATH_ARG\", \"depth\": $DEPTH_ARG}" \
            | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'📊 Files: {d[\"total_files\"]:,}'); print(f'📝 Lines: {d[\"total_lines\"]:,}'); print(f'💾 Bytes: {d[\"total_bytes\"]:,}'); print(f'🔥 Complexity: {d[\"complexity_score\"]:,}'); print(f'⚡ Speed: {d[\"performance\"][\"files_per_second\"]:,.0f} files/sec')"
        ;;
    
    grep)
        if [ -z "$2" ]; then
            echo -e "${RED}Usage: $0 grep <pattern> [path]${NC}"
            exit 1
        fi
        PATTERN="$2"
        PATH_ARG="${3:-/Users/m2ultra/NOIZYLAB}"
        echo -e "${CYAN}⚡ MEGA GREP: '$PATTERN' in $PATH_ARG${NC}"
        curl -s -X POST http://localhost:$PORT/mega/grep \
            -H "Content-Type: application/json" \
            -d "{\"pattern\": \"$PATTERN\", \"path\": \"$PATH_ARG\", \"limit\": 30}" \
            | python3 -m json.tool
        ;;
    
    turbo)
        echo -e "${CYAN}🚀 TURBO ENGINE STATUS:${NC}"
        curl -s http://localhost:$PORT/turbo/ | python3 -m json.tool
        ;;
    
    swarm)
        echo -e "${CYAN}🐟 SWARM STATUS (11 AGENTS):${NC}"
        curl -s http://localhost:$PORT/swarm/agents | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Total Agents: {d[\"total\"]}'); print('─'*60); [print(f'{v[\"emoji\"]} {k:15} │ {v[\"role\"]:25} │ {v.get(\"type\",\"ai\")}') for k,v in d['agents'].items()]"
        ;;
    
    family)
        echo -e "${CYAN}👨‍👩‍👧‍👦 FAMILY HIVE MEMBERS:${NC}"
        curl -s http://localhost:$PORT/swarm/agents | python3 -c "import sys,json; d=json.load(sys.stdin); family=[k for k,v in d['agents'].items() if v.get('type')=='human']; print('─'*60); [print(f'{d[\"agents\"][m][\"emoji\"]} {m:15} │ {d[\"agents\"][m][\"role\"]:25} │ {d[\"agents\"][m].get(\"bio\",\"\")[:40]}') for m in family]"
        ;;
    
    brain)
        echo -e "${CYAN}🧠 AI BRAIN STATUS:${NC}"
        curl -s http://localhost:$PORT/ai/brain | python3 -m json.tool
        ;;
    
    cache)
        echo -e "${CYAN}📦 MEGA CACHE STATUS:${NC}"
        curl -s http://localhost:$PORT/mega/cache | python3 -m json.tool
        ;;
    
    *)
        echo "Usage: $0 {start|stop|restart|status|logs|mega|scan|grep|turbo|swarm|family|brain|cache}"
        echo ""
        echo "Commands:"
        echo "  start         - Start CODEMASTER MEGA"
        echo "  stop          - Stop CODEMASTER"
        echo "  restart       - Restart CODEMASTER"
        echo "  status        - Show health status"
        echo "  logs          - Tail the logs"
        echo ""
        echo "⚡ MEGA ENGINE:"
        echo "  mega          - Show MEGA engine status"
        echo "  scan [path]   - TURBO scan a directory"
        echo "  grep <pattern> [path] - HYPER grep search"
        echo "  cache         - Show cache statistics"
        echo ""
        echo "🐟 SWARM:"
        echo "  swarm         - Show all SWARM agents"
        echo "  family        - Show FAMILY hive members"
        echo ""
        echo "🚀 OTHER:"
        echo "  turbo         - Show TURBO engine status"
        echo "  brain         - Show AI Brain status"
        exit 1
        ;;
esac
