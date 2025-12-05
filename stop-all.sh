#!/bin/bash
# STOP ALL SERVICES
# Cleanly shutdown all AI GENIUS systems

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${YELLOW}Stopping all services...${NC}"
echo ""

# Stop services by PID files
for PID_FILE in .*.pid; do
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        SERVICE_NAME=$(basename "$PID_FILE" .pid | sed 's/^.//')
        
        if ps -p $PID > /dev/null 2>&1; then
            echo "  Stopping $SERVICE_NAME (PID: $PID)"
            kill $PID 2>/dev/null
            sleep 1
            
            # Force kill if still running
            if ps -p $PID > /dev/null 2>&1; then
                kill -9 $PID 2>/dev/null
            fi
        fi
        
        rm "$PID_FILE"
    fi
done

# Kill by port as backup
PORTS=(7777 8888 9999)
for PORT in "${PORTS[@]}"; do
    PID=$(lsof -ti:$PORT 2>/dev/null) || true
    if [ ! -z "$PID" ]; then
        echo "  Killing process on port $PORT"
        kill -9 $PID 2>/dev/null || true
    fi
done

echo ""
echo -e "${GREEN}✓ All services stopped${NC}"
