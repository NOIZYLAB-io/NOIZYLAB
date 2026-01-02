#!/bin/bash
#===============================================================================
# GABRIEL - Agent Shell Interface
# Invoke Circle of 8 agents from the command line
#===============================================================================

# Source this file: source ~/NOIZYLAB/GABRIEL/src/agents/fleet/agent_interface.sh

GABRIEL_ROOT="${GABRIEL_ROOT:-$HOME/NOIZYLAB/GABRIEL}"
WORKER_URL="${WORKER_URL:-https://antigravity.rsplowman.workers.dev}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

#-------------------------------------------------------------------------------
# Invoke any Circle of 8 agent
#-------------------------------------------------------------------------------
invoke_agent() {
    local agent_id="${1:-gabriel}"
    local message="${2:-Status report}"
    
    echo -e "${CYAN}⚡ Invoking ${agent_id^^}...${NC}"
    
    curl -s -X POST "${WORKER_URL}/circle/${agent_id}/invoke" \
        -H "Content-Type: application/json" \
        -d "{\"message\": \"${message}\"}" | jq .
}

# Shortcut functions for each agent
gabriel() { invoke_agent "gabriel" "$*"; }
shirl() { invoke_agent "shirl" "$*"; }
pops() { invoke_agent "pops" "$*"; }
engr_keith() { invoke_agent "engr_keith" "$*"; }
dream() { invoke_agent "dream" "$*"; }
heaven() { invoke_agent "heaven" "$*"; }
lucy() { invoke_agent "lucy" "$*"; }
sonic() { invoke_agent "sonic" "$*"; }

#-------------------------------------------------------------------------------
# Circle of 8 - Invoke all agents
#-------------------------------------------------------------------------------
circle_all() {
    local message="${1:-Status report}"
    echo -e "${PURPLE}🔮 Invoking the Circle of 8...${NC}"
    
    for agent in gabriel shirl pops engr_keith dream heaven lucy sonic; do
        echo -e "\n${YELLOW}━━━ ${agent^^} ━━━${NC}"
        invoke_agent "$agent" "$message"
    done
}

#-------------------------------------------------------------------------------
# Health check
#-------------------------------------------------------------------------------
check_health() {
    echo -e "${GREEN}🏥 Checking worker health...${NC}"
    curl -s "${WORKER_URL}/health" | jq .
}

#-------------------------------------------------------------------------------
# Quick status
#-------------------------------------------------------------------------------
status() {
    echo -e "${BLUE}📊 MC96ECOUNIVERSE Status${NC}"
    echo ""
    check_health
    echo ""
    echo -e "${GREEN}✅ Circle of 8 ready${NC}"
    echo -e "   gabriel shirl pops engr_keith dream heaven lucy sonic"
}

# Print help on source
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}🔮 Circle of 8 Agent Interface Loaded${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "Commands:"
echo -e "  ${GREEN}gabriel${NC} \"message\"     - Invoke GABRIEL (Warrior AI)"
echo -e "  ${GREEN}shirl${NC} \"message\"       - Invoke SHIRL (Business Ops)"
echo -e "  ${GREEN}pops${NC} \"message\"        - Invoke POPS (Creative Director)"
echo -e "  ${GREEN}engr_keith${NC} \"message\"  - Invoke ENGR_KEITH (Engineering)"
echo -e "  ${GREEN}dream${NC} \"message\"       - Invoke DREAM (Visionary)"
echo -e "  ${GREEN}heaven${NC} \"message\"      - Invoke HEAVEN (Orchestrator)"
echo -e "  ${GREEN}lucy${NC} \"message\"        - Invoke LUCY (Code Guardian)"
echo -e "  ${GREEN}sonic${NC} \"message\"       - Invoke SONIC (Audio Engine)"
echo ""
echo -e "  ${YELLOW}circle_all${NC} \"message\" - Invoke ALL agents"
echo -e "  ${YELLOW}status${NC}               - Check system status"
echo -e "  ${YELLOW}check_health${NC}         - Health check"
echo ""
