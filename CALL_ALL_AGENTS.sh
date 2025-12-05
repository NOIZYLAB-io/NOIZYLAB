#!/bin/bash
# ════════════════════════════════════════════════════════════════════════════
# 🚀 CALL ALL AGENTS - Master Agent Activation Script
# ════════════════════════════════════════════════════════════════════════════
#
# This script activates ALL agents in the NOIZYLAB ecosystem:
# - GABRIEL ULTRA X10000 (8 AI Family agents)
# - GABRIEL DGS1210 Master Control
# - ENGR_KEITH (Technical Genius)
# - GABRIEL CLI (Node.js)
# - MC96 CLI (Node.js)
# - AI Aggregator
# - All NoizyLab agent systems
#
# Created by: AI Family Collective
# GABRIEL • SHIRL • POPS • ENGR_KEITH • DREAM • LUCY • CLAUDE • COPILOT
# ════════════════════════════════════════════════════════════════════════════

BASE="/Users/m2ultra/NOIZYLAB"
LOG_DIR="$BASE/logs"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$LOG_DIR/all_agents_${TIMESTAMP}.log"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║                                                                           ║${NC}"
echo -e "${CYAN}║         🚀 CALLING ALL AGENTS - MASTER ACTIVATION                         ║${NC}"
echo -e "${CYAN}║                                                                           ║${NC}"
echo -e "${CYAN}║         AI Family Collective • Full System Activation                     ║${NC}"
echo -e "${CYAN}║                                                                           ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}📋 Log file: $LOG_FILE${NC}"
echo ""

# Function to log and execute
run_agent() {
    local name=$1
    local command=$2
    local description=$3
    
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}🤖 Activating: ${name}${NC}"
    echo -e "${BLUE}   ${description}${NC}"
    echo ""
    
    {
        echo "=== $name - $(date) ==="
        echo "Command: $command"
        echo ""
        eval "$command" 2>&1
        echo ""
        echo "=== $name Complete - $(date) ==="
        echo ""
    } >> "$LOG_FILE" 2>&1 &
    
    local pid=$!
    echo -e "${CYAN}   ✅ Started (PID: $pid)${NC}"
    echo ""
    sleep 1
}

# ════════════════════════════════════════════════════════════════════════════
# PHASE 1: GABRIEL ULTRA X10000 - 8 AI Family Agents
# ════════════════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  PHASE 1: GABRIEL ULTRA X10000 - 8 AI FAMILY AGENTS${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

run_agent \
    "GABRIEL ULTRA X10000" \
    "cd $BASE && python3 GABRIEL_ULTRA_X10000.py" \
    "Multi-agent Orchestrator with 8 AI Family agents (GABRIEL, SHIRL, POPS, ENGR_KEITH, DREAM, LUCY, CLAUDE, COPILOT)"

# ════════════════════════════════════════════════════════════════════════════
# PHASE 2: GABRIEL DGS1210 MASTER CONTROL
# ════════════════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  PHASE 2: GABRIEL DGS1210 MASTER CONTROL${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

run_agent \
    "GABRIEL DGS1210 Master Control" \
    "cd $BASE && python3 GABRIEL_DGS1210_MASTER_CONTROL.py" \
    "Network orchestration and DGS1210 switch control"

# ════════════════════════════════════════════════════════════════════════════
# PHASE 3: INDIVIDUAL AGENTS
# ════════════════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  PHASE 3: INDIVIDUAL AGENTS${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

run_agent \
    "ENGR_KEITH" \
    "cd $BASE && python3 ENGR_KEITH.py" \
    "Technical Genius - Code architecture and system optimization"

# ════════════════════════════════════════════════════════════════════════════
# PHASE 4: NODE.JS CLI AGENTS
# ════════════════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  PHASE 4: NODE.JS CLI AGENTS${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

run_agent \
    "GABRIEL CLI" \
    "cd $BASE && node gabriel-cli.mjs status" \
    "GABRIEL OS CLI - Local-first command interface"

run_agent \
    "MC96 CLI" \
    "cd $BASE && node mc96-cli.mjs" \
    "MC96 CLI - Super-cursor scaffold system"

# ════════════════════════════════════════════════════════════════════════════
# PHASE 5: AI AGGREGATOR
# ════════════════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  PHASE 5: AI AGGREGATOR${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

run_agent \
    "AI Aggregator" \
    "cd $BASE/ai-aggregator && ./start.sh" \
    "AI Engine Aggregator - Multi-engine AI query system"

# ════════════════════════════════════════════════════════════════════════════
# PHASE 6: NOIZYLAB AGENT SYSTEMS
# ════════════════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  PHASE 6: NOIZYLAB AGENT SYSTEMS${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

# Check if NoizyLab agent systems exist
AGENT_SYSTEMS_DIR="$BASE/noizylab_2026/_ORGANIZED/_noizy_projects/scripts/python/🤖 AI_Toolkit/06_AI_Agents"

if [ -d "$AGENT_SYSTEMS_DIR" ]; then
    run_agent \
        "NoizyLab Agent System" \
        "cd $AGENT_SYSTEMS_DIR && python3 agent_cli.py --mode interactive" \
        "NoizyLab AI Agent System - Music, Creative, and Technical agents"
else
    echo -e "${YELLOW}⚠️  NoizyLab Agent System directory not found${NC}"
    echo ""
fi

# ════════════════════════════════════════════════════════════════════════════
# PHASE 7: SYSTEM SERVICES
# ════════════════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}  PHASE 7: SYSTEM SERVICES${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

run_agent \
    "System Health Monitor" \
    "cd $BASE && python3 CHECK_AGENTS.py" \
    "Agent status checker and system health monitor"

# ════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════════

echo ""
echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║                                                                           ║${NC}"
echo -e "${CYAN}║         ✅ ALL AGENTS ACTIVATED                                            ║${NC}"
echo -e "${CYAN}║                                                                           ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}📊 Agent Summary:${NC}"
echo ""
echo -e "  ${GREEN}✅${NC} GABRIEL ULTRA X10000 (8 AI Family agents)"
echo -e "  ${GREEN}✅${NC} GABRIEL DGS1210 Master Control"
echo -e "  ${GREEN}✅${NC} ENGR_KEITH (Technical Genius)"
echo -e "  ${GREEN}✅${NC} GABRIEL CLI (Node.js)"
echo -e "  ${GREEN}✅${NC} MC96 CLI (Node.js)"
echo -e "  ${GREEN}✅${NC} AI Aggregator"
echo -e "  ${GREEN}✅${NC} NoizyLab Agent Systems"
echo -e "  ${GREEN}✅${NC} System Health Monitor"
echo ""

echo -e "${BLUE}📋 Log file: $LOG_FILE${NC}"
echo ""
echo -e "${YELLOW}💡 To view logs in real-time:${NC}"
echo -e "   ${CYAN}tail -f $LOG_FILE${NC}"
echo ""
echo -e "${YELLOW}💡 To check running agents:${NC}"
echo -e "   ${CYAN}ps aux | grep -E 'GABRIEL|ENGR_KEITH|gabriel-cli|mc96-cli|agent'${NC}"
echo ""
echo -e "${YELLOW}💡 To stop all agents:${NC}"
echo -e "   ${CYAN}pkill -f 'GABRIEL|ENGR_KEITH|gabriel-cli|mc96-cli|agent'${NC}"
echo ""

echo -e "${MAGENTA}🎯 All agents are now active and running!${NC}"
echo ""

