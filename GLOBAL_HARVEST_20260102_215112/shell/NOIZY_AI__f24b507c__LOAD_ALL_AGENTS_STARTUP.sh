#!/bin/bash
# LOAD_ALL_AGENTS_STARTUP.sh
# Master startup loader for all MC96 agents on macOS
# GORUNFREEX5000

AGENT_DIR="$HOME/Library/Application Support/MC96_Agents"
LOG_DIR="$HOME/Library/Logs/MC96_Agents"

mkdir -p "$LOG_DIR"

STARTUP_LOG="$LOG_DIR/STARTUP_$(date +%Y%m%d).log"

log() {
    echo "[$(date '+%H:%M:%S')] $1" | tee -a "$STARTUP_LOG"
}

log "🚀 MC96 Agent System Starting..."
log "GORUNFREEX5000 - Auto-startup initiated"

# Start each agent in background
AGENTS=("LUCY" "POPS" "ENGR_KEITH" "DREAM" "ALEX_WARD" "WARDIE" "FLEET")

for AGENT in "${AGENTS[@]}"; do
    AGENT_SCRIPT="$AGENT_DIR/AGENT_${AGENT}.sh"
    
    if [ -f "$AGENT_SCRIPT" ]; then
        # Start agent in background
        nohup "$AGENT_SCRIPT" > /dev/null 2>&1 &
        AGENT_PID=$!
        log "✓ Started AGENT_${AGENT} (PID: $AGENT_PID)"
        sleep 1
    else
        log "✗ AGENT_${AGENT}.sh not found at $AGENT_SCRIPT"
    fi
done

log "🚀 All agents started - running in background"
log "View logs: $LOG_DIR"

# Show notification
osascript -e 'display notification "All 4 agents running in background" with title "MC96 Agent System" subtitle "GORUNFREEX5000 Ready"' 2>/dev/null
