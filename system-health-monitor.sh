#!/bin/bash
# SYSTEM HEALTH MONITOR
# Real-time monitoring of all AI GENIUS systems
# Displays comprehensive status dashboard

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

# Function to check if service is running
check_service() {
    pgrep -f "$1" > /dev/null
    return $?
}

# Function to check file exists
check_file() {
    [ -f "$1" ]
    return $?
}

# Function to check directory exists
check_dir() {
    [ -d "$1" ]
    return $?
}

# Function to test network connectivity
check_network() {
    curl -s --max-time 2 "$1" > /dev/null
    return $?
}

# Main dashboard loop
show_dashboard() {
    while true; do
        clear
        
        # Header
        echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${PURPLE}║                                                               ║${NC}"
        echo -e "${PURPLE}║          🏥 SYSTEM HEALTH MONITOR 🏥                          ║${NC}"
        echo -e "${PURPLE}║                                                               ║${NC}"
        echo -e "${PURPLE}║          Real-Time Status Dashboard                           ║${NC}"
        echo -e "${PURPLE}║          Last Update: $(date '+%Y-%m-%d %H:%M:%S')                    ║${NC}"
        echo -e "${PURPLE}║                                                               ║${NC}"
        echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        
        # System Overview
        echo -e "${CYAN}${BOLD}🖥️  SYSTEM OVERVIEW${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        # Platform
        PLATFORM=$(uname -s)
        echo -e "${BLUE}Platform:${NC}         $PLATFORM"
        
        # Hostname
        HOSTNAME=$(hostname)
        if [[ "$HOSTNAME" == *"GOD"* ]] || [[ "$HOSTNAME" == *"god"* ]]; then
            echo -e "${BLUE}Machine:${NC}          ${GREEN}GOD (Mac Studio M2 Ultra)${NC}"
        elif [[ "$HOSTNAME" == *"GABRIEL"* ]] || [[ "$HOSTNAME" == *"gabriel"* ]]; then
            echo -e "${BLUE}Machine:${NC}          ${GREEN}GABRIEL (HP Omen)${NC}"
        else
            echo -e "${BLUE}Machine:${NC}          $HOSTNAME"
        fi
        
        # Uptime
        UPTIME=$(uptime | awk '{print $3,$4}' | sed 's/,//')
        echo -e "${BLUE}Uptime:${NC}           $UPTIME"
        
        # Load average
        LOAD=$(uptime | awk -F'load average:' '{print $2}')
        echo -e "${BLUE}Load Average:${NC}     $LOAD"
        echo ""
        
        # Core Systems Check
        echo -e "${CYAN}${BOLD}🔧 CORE SYSTEMS${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        SYSTEMS_OK=0
        SYSTEMS_WARN=0
        SYSTEMS_ERROR=0
        
        # Check Python
        if command -v python3 &> /dev/null; then
            PYTHON_VER=$(python3 --version | awk '{print $2}')
            echo -e "${GREEN}✓${NC} Python 3:         Installed (v$PYTHON_VER)"
            SYSTEMS_OK=$((SYSTEMS_OK + 1))
        else
            echo -e "${RED}✗${NC} Python 3:         Missing"
            SYSTEMS_ERROR=$((SYSTEMS_ERROR + 1))
        fi
        
        # Check Node.js
        if command -v node &> /dev/null; then
            NODE_VER=$(node --version)
            echo -e "${GREEN}✓${NC} Node.js:          Installed ($NODE_VER)"
            SYSTEMS_OK=$((SYSTEMS_OK + 1))
        else
            echo -e "${YELLOW}⚠${NC} Node.js:          Not installed"
            SYSTEMS_WARN=$((SYSTEMS_WARN + 1))
        fi
        
        # Check pip
        if command -v pip3 &> /dev/null; then
            echo -e "${GREEN}✓${NC} pip3:             Available"
            SYSTEMS_OK=$((SYSTEMS_OK + 1))
        else
            echo -e "${RED}✗${NC} pip3:             Missing"
            SYSTEMS_ERROR=$((SYSTEMS_ERROR + 1))
        fi
        
        # Check npm
        if command -v npm &> /dev/null; then
            echo -e "${GREEN}✓${NC} npm:              Available"
            SYSTEMS_OK=$((SYSTEMS_OK + 1))
        else
            echo -e "${YELLOW}⚠${NC} npm:              Not installed"
            SYSTEMS_WARN=$((SYSTEMS_WARN + 1))
        fi
        
        echo ""
        
        # Directories Check
        echo -e "${CYAN}${BOLD}📁 INSTALLATION STATUS${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        DIRS_OK=0
        DIRS_ERROR=0
        
        # Check ai-genius
        if check_dir ~/ai-genius; then
            FILE_COUNT=$(find ~/ai-genius -type f | wc -l)
            DIR_SIZE=$(du -sh ~/ai-genius 2>/dev/null | cut -f1)
            echo -e "${GREEN}✓${NC} AI GENIUS:        Installed ($FILE_COUNT files, $DIR_SIZE)"
            DIRS_OK=$((DIRS_OK + 1))
        else
            echo -e "${RED}✗${NC} AI GENIUS:        Not found"
            DIRS_ERROR=$((DIRS_ERROR + 1))
        fi
        
        # Check ai-genius-pro
        if check_dir ~/ai-genius-pro; then
            FILE_COUNT=$(find ~/ai-genius-pro -type f | wc -l)
            DIR_SIZE=$(du -sh ~/ai-genius-pro 2>/dev/null | cut -f1)
            echo -e "${GREEN}✓${NC} AI GENIUS Pro:    Installed ($FILE_COUNT files, $DIR_SIZE)"
            DIRS_OK=$((DIRS_OK + 1))
        else
            echo -e "${YELLOW}⚠${NC} AI GENIUS Pro:    Not found"
            DIRS_ERROR=$((DIRS_ERROR + 1))
        fi
        
        # Check noizylab-perfect
        if check_dir ~/noizylab-perfect; then
            FILE_COUNT=$(find ~/noizylab-perfect -type f | wc -l)
            DIR_SIZE=$(du -sh ~/noizylab-perfect 2>/dev/null | cut -f1)
            echo -e "${GREEN}✓${NC} NOIZYLAB:         Installed ($FILE_COUNT files, $DIR_SIZE)"
            DIRS_OK=$((DIRS_OK + 1))
        else
            echo -e "${YELLOW}⚠${NC} NOIZYLAB:         Not found"
            DIRS_ERROR=$((DIRS_ERROR + 1))
        fi
        
        # Check backup directory
        if check_dir ~/ai-genius-backups; then
            BACKUP_COUNT=$(ls -1 ~/ai-genius-backups/*/ 2>/dev/null | wc -l)
            echo -e "${GREEN}✓${NC} Backups:          $BACKUP_COUNT backups available"
            DIRS_OK=$((DIRS_OK + 1))
        else
            echo -e "${YELLOW}⚠${NC} Backups:          No backups found"
        fi
        
        echo ""
        
        # AI Services Check
        echo -e "${CYAN}${BOLD}🤖 AI SERVICES${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        SERVICES_OK=0
        SERVICES_ERROR=0
        
        # Check Claude API
        echo -n -e "${BLUE}Claude API:${NC}       "
        if check_network "https://api.anthropic.com" 2>/dev/null; then
            echo -e "${GREEN}✓ Reachable${NC}"
            SERVICES_OK=$((SERVICES_OK + 1))
        else
            echo -e "${RED}✗ Unreachable${NC}"
            SERVICES_ERROR=$((SERVICES_ERROR + 1))
        fi
        
        # Check Google API
        echo -n -e "${BLUE}Gemini API:${NC}       "
        if check_network "https://generativelanguage.googleapis.com" 2>/dev/null; then
            echo -e "${GREEN}✓ Reachable${NC}"
            SERVICES_OK=$((SERVICES_OK + 1))
        else
            echo -e "${RED}✗ Unreachable${NC}"
            SERVICES_ERROR=$((SERVICES_ERROR + 1))
        fi
        
        # Check OpenAI API
        echo -n -e "${BLUE}OpenAI API:${NC}       "
        if check_network "https://api.openai.com" 2>/dev/null; then
            echo -e "${GREEN}✓ Reachable${NC}"
            SERVICES_OK=$((SERVICES_OK + 1))
        else
            echo -e "${YELLOW}⚠ Unreachable${NC}"
            SERVICES_ERROR=$((SERVICES_ERROR + 1))
        fi
        
        # Check Cloudflare Worker
        WORKER_URL=$(grep -r "WORKER_URL.*=" ~/ai-genius/*.py 2>/dev/null | head -1 | sed 's/.*= *"\(.*\)".*/\1/' || echo "")
        echo -n -e "${BLUE}Cloud Worker:${NC}     "
        if [ ! -z "$WORKER_URL" ] && [ "$WORKER_URL" != "https://YOUR-WORKER-URL.workers.dev" ]; then
            if curl -s "$WORKER_URL/health" --max-time 2 | grep -q "operational" 2>/dev/null; then
                echo -e "${GREEN}✓ Online${NC}"
                SERVICES_OK=$((SERVICES_OK + 1))
            else
                echo -e "${YELLOW}⚠ Unreachable${NC}"
            fi
        else
            echo -e "${YELLOW}⚠ Not configured${NC}"
        fi
        
        echo ""
        
        # Usage Statistics
        echo -e "${CYAN}${BOLD}📊 USAGE STATISTICS${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        if [ -f ~/.ai-genius-stats.json ]; then
            QUERIES=$(jq -r '.queries' ~/.ai-genius-stats.json 2>/dev/null || echo "0")
            TOKENS=$(jq -r '.tokens' ~/.ai-genius-stats.json 2>/dev/null || echo "0")
            COST=$(jq -r '.cost' ~/.ai-genius-stats.json 2>/dev/null || echo "0")
            
            echo -e "${BLUE}Total Queries:${NC}    $QUERIES"
            echo -e "${BLUE}Total Tokens:${NC}     $TOKENS"
            echo -e "${BLUE}Total Cost:${NC}       \$${COST}"
        else
            echo -e "${YELLOW}⚠ No usage data available${NC}"
        fi
        
        echo ""
        
        # Resource Usage
        echo -e "${CYAN}${BOLD}💻 RESOURCE USAGE${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        # Disk space
        DISK_USAGE=$(df -h ~ | tail -1 | awk '{print $5}' | sed 's/%//')
        DISK_AVAIL=$(df -h ~ | tail -1 | awk '{print $4}')
        echo -n -e "${BLUE}Disk Space:${NC}       "
        if [ "$DISK_USAGE" -lt 80 ]; then
            echo -e "${GREEN}${DISK_USAGE}% used ($DISK_AVAIL available)${NC}"
        elif [ "$DISK_USAGE" -lt 90 ]; then
            echo -e "${YELLOW}${DISK_USAGE}% used ($DISK_AVAIL available)${NC}"
        else
            echo -e "${RED}${DISK_USAGE}% used ($DISK_AVAIL available)${NC}"
        fi
        
        # Memory (if available)
        if command -v free &> /dev/null; then
            MEM_USAGE=$(free | grep Mem | awk '{print int($3/$2 * 100)}')
            MEM_TOTAL=$(free -h | grep Mem | awk '{print $2}')
            echo -n -e "${BLUE}Memory:${NC}           "
            if [ "$MEM_USAGE" -lt 80 ]; then
                echo -e "${GREEN}${MEM_USAGE}% used ($MEM_TOTAL total)${NC}"
            else
                echo -e "${YELLOW}${MEM_USAGE}% used ($MEM_TOTAL total)${NC}"
            fi
        fi
        
        # AI processes
        AI_PROCS=$(pgrep -fc "ai-genius|universal-ai|multi-model" || echo "0")
        echo -e "${BLUE}AI Processes:${NC}     $AI_PROCS running"
        
        echo ""
        
        # Overall Health Score
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo -e "${CYAN}${BOLD}🏥 OVERALL HEALTH${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        TOTAL_CHECKS=$((SYSTEMS_OK + SYSTEMS_WARN + SYSTEMS_ERROR + DIRS_OK + DIRS_ERROR + SERVICES_OK + SERVICES_ERROR))
        HEALTH_SCORE=$(echo "scale=0; ($SYSTEMS_OK + $DIRS_OK + $SERVICES_OK) * 100 / $TOTAL_CHECKS" | bc 2>/dev/null || echo "0")
        
        echo -n "Health Score: "
        if [ "$HEALTH_SCORE" -ge 90 ]; then
            echo -e "${GREEN}${BOLD}${HEALTH_SCORE}%${NC} ${GREEN}✓ EXCELLENT${NC}"
        elif [ "$HEALTH_SCORE" -ge 70 ]; then
            echo -e "${YELLOW}${BOLD}${HEALTH_SCORE}%${NC} ${YELLOW}⚠ GOOD${NC}"
        elif [ "$HEALTH_SCORE" -ge 50 ]; then
            echo -e "${YELLOW}${BOLD}${HEALTH_SCORE}%${NC} ${YELLOW}⚠ FAIR${NC}"
        else
            echo -e "${RED}${BOLD}${HEALTH_SCORE}%${NC} ${RED}✗ POOR${NC}"
        fi
        
        echo ""
        echo -e "${BLUE}Checks Passed:${NC}    $((SYSTEMS_OK + DIRS_OK + SERVICES_OK)) / $TOTAL_CHECKS"
        echo -e "${BLUE}Warnings:${NC}         $((SYSTEMS_WARN))"
        echo -e "${BLUE}Errors:${NC}           $((SYSTEMS_ERROR + DIRS_ERROR + SERVICES_ERROR))"
        
        echo ""
        
        # Quick Actions
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo -e "${CYAN}${BOLD}⚡ QUICK ACTIONS${NC}"
        echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        echo "R - Refresh | B - Backup | E - Emergency Recovery | Q - Quit"
        echo ""
        
        # Read input with timeout
        read -t 5 -n 1 ACTION
        
        case "$ACTION" in
            R|r)
                continue
                ;;
            B|b)
                echo ""
                echo "Running backup..."
                ~/noizylab-perfect/automated-backup.sh daily
                read -p "Press Enter to continue..."
                ;;
            E|e)
                echo ""
                echo "Starting emergency recovery..."
                ~/noizylab-perfect/emergency-recovery.sh
                read -p "Press Enter to continue..."
                ;;
            Q|q)
                clear
                echo -e "${GREEN}Goodbye!${NC}"
                exit 0
                ;;
        esac
        
        sleep 1
    done
}

# Start monitoring
show_dashboard
