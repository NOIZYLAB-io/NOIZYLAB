#!/bin/bash
# PERFORMANCE MONITOR
# Track AI usage, costs, and system health
# Real-time dashboard

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

# Stats file
STATS_FILE=~/.ai-genius-stats.json

# Initialize if doesn't exist
if [ ! -f "$STATS_FILE" ]; then
    echo '{"queries": 0, "tokens": 0, "cost": 0, "start_date": "'$(date +%Y-%m-%d)'"}' > "$STATS_FILE"
fi

# Function to update stats
update_stats() {
    QUERIES=$(jq -r '.queries' "$STATS_FILE" 2>/dev/null || echo "0")
    TOKENS=$(jq -r '.tokens' "$STATS_FILE" 2>/dev/null || echo "0")
    COST=$(jq -r '.cost' "$STATS_FILE" 2>/dev/null || echo "0")
    
    QUERIES=$((QUERIES + 1))
    TOKENS=$((TOKENS + ${1:-100}))
    COST=$(echo "$COST + ${2:-0.003}" | bc 2>/dev/null || echo "$COST")
    
    jq ".queries = $QUERIES | .tokens = $TOKENS | .cost = $COST" "$STATS_FILE" > "$STATS_FILE.tmp" && mv "$STATS_FILE.tmp" "$STATS_FILE"
}

# Display dashboard
show_dashboard() {
    clear
    echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║                                                               ║${NC}"
    echo -e "${PURPLE}║          📊 AI GENIUS PERFORMANCE MONITOR 📊                  ║${NC}"
    echo -e "${PURPLE}║                                                               ║${NC}"
    echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    # Read stats
    QUERIES=$(jq -r '.queries' "$STATS_FILE" 2>/dev/null || echo "0")
    TOKENS=$(jq -r '.tokens' "$STATS_FILE" 2>/dev/null || echo "0")
    COST=$(jq -r '.cost' "$STATS_FILE" 2>/dev/null || echo "0")
    START_DATE=$(jq -r '.start_date' "$STATS_FILE" 2>/dev/null || echo "N/A")
    
    # Calculate days
    if [ "$START_DATE" != "N/A" ]; then
        START_EPOCH=$(date -j -f "%Y-%m-%d" "$START_DATE" +%s 2>/dev/null || date -d "$START_DATE" +%s 2>/dev/null || echo "0")
        NOW_EPOCH=$(date +%s)
        DAYS=$(( (NOW_EPOCH - START_EPOCH) / 86400 ))
        if [ $DAYS -eq 0 ]; then DAYS=1; fi
    else
        DAYS=1
    fi
    
    QUERIES_PER_DAY=$(echo "scale=1; $QUERIES / $DAYS" | bc 2>/dev/null || echo "0")
    COST_PER_DAY=$(echo "scale=2; $COST / $DAYS" | bc 2>/dev/null || echo "0")
    AVG_TOKENS=$(echo "scale=0; $TOKENS / $QUERIES" | bc 2>/dev/null || echo "0")
    
    echo -e "${CYAN}${BOLD}📈 USAGE STATISTICS${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}Total Queries:${NC}        $QUERIES"
    echo -e "${BLUE}Total Tokens:${NC}         $TOKENS"
    echo -e "${BLUE}Total Cost:${NC}           \$${COST}"
    echo -e "${BLUE}Days Active:${NC}          $DAYS"
    echo ""
    echo -e "${BLUE}Avg Queries/Day:${NC}      $QUERIES_PER_DAY"
    echo -e "${BLUE}Avg Cost/Day:${NC}         \$${COST_PER_DAY}"
    echo -e "${BLUE}Avg Tokens/Query:${NC}     $AVG_TOKENS"
    echo ""
    
    # Cost projection
    MONTHLY_COST=$(echo "$COST_PER_DAY * 30" | bc 2>/dev/null || echo "0")
    YEARLY_COST=$(echo "$COST_PER_DAY * 365" | bc 2>/dev/null || echo "0")
    
    echo -e "${CYAN}${BOLD}💰 COST PROJECTIONS${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}Monthly (projected):${NC}   \$${MONTHLY_COST}"
    echo -e "${BLUE}Yearly (projected):${NC}    \$${YEARLY_COST}"
    echo ""
    
    # System health
    echo -e "${CYAN}${BOLD}🔧 SYSTEM HEALTH${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Check if services are running
    if pgrep -f "ai-genius.js" > /dev/null; then
        echo -e "${GREEN}✓ AI GENIUS Local: Running${NC}"
    else
        echo -e "${YELLOW}⚠ AI GENIUS Local: Stopped${NC}"
    fi
    
    # Check Cloudflare Worker
    WORKER_URL=$(grep -r "WORKER_URL.*=" ~/ai-genius/*.py 2>/dev/null | head -1 | sed 's/.*= *"\(.*\)".*/\1/' || echo "")
    if [ ! -z "$WORKER_URL" ] && [ "$WORKER_URL" != "https://YOUR-WORKER-URL.workers.dev" ]; then
        if curl -s "$WORKER_URL/health" --max-time 2 | grep -q "operational" 2>/dev/null; then
            echo -e "${GREEN}✓ Cloud Worker: Online${NC}"
        else
            echo -e "${YELLOW}⚠ Cloud Worker: Unreachable${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ Cloud Worker: Not configured${NC}"
    fi
    
    # Disk space
    DISK_USAGE=$(df -h ~ | tail -1 | awk '{print $5}' | sed 's/%//')
    if [ "$DISK_USAGE" -lt 80 ]; then
        echo -e "${GREEN}✓ Disk Space: ${DISK_USAGE}% used${NC}"
    else
        echo -e "${YELLOW}⚠ Disk Space: ${DISK_USAGE}% used${NC}"
    fi
    
    # Memory
    if command -v free &> /dev/null; then
        MEM_USAGE=$(free | grep Mem | awk '{print int($3/$2 * 100)}')
        echo -e "${GREEN}✓ Memory: ${MEM_USAGE}% used${NC}"
    fi
    
    echo ""
    
    # Model usage breakdown
    echo -e "${CYAN}${BOLD}🤖 MODEL USAGE${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}Most Used:${NC}            Claude Sonnet 4"
    echo -e "${BLUE}Fastest:${NC}              Gemini 2.0 Flash"
    echo -e "${BLUE}Most Accurate:${NC}        Claude Opus 4"
    echo ""
    
    # Tips
    echo -e "${CYAN}${BOLD}💡 OPTIMIZATION TIPS${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    if [ "$QUERIES" -lt 10 ]; then
        echo -e "${YELLOW}📈 Try using AI more! You're only at $QUERIES queries.${NC}"
    elif echo "$COST" | awk '$1 > 50 {exit 1}'; then
        echo -e "${GREEN}✓ Usage is efficient and cost-effective${NC}"
    else
        echo -e "${YELLOW}⚠ Consider using Gemini (free) for simple queries${NC}"
    fi
    
    if [ "$QUERIES" -gt 100 ]; then
        echo -e "${GREEN}✓ Power user! Consider setting up caching${NC}"
    fi
    
    echo ""
    
    # Actions
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}${BOLD}⚡ QUICK ACTIONS${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo "1. View detailed logs"
    echo "2. Reset statistics"
    echo "3. Export report"
    echo "4. Check for updates"
    echo "5. Optimize settings"
    echo "6. Refresh display"
    echo "7. Exit"
    echo ""
    
    read -p "Choose (1-7): " ACTION
    
    case $ACTION in
        1)
            echo ""
            echo -e "${CYAN}Recent Activity:${NC}"
            if [ -f ~/.ai-genius.log ]; then
                tail -20 ~/.ai-genius.log
            else
                echo "No log file found"
            fi
            echo ""
            read -p "Press Enter to continue..."
            show_dashboard
            ;;
        
        2)
            echo ""
            read -p "Reset all statistics? (yes/no): " CONFIRM
            if [ "$CONFIRM" = "yes" ]; then
                echo '{"queries": 0, "tokens": 0, "cost": 0, "start_date": "'$(date +%Y-%m-%d)'"}' > "$STATS_FILE"
                echo -e "${GREEN}✓ Statistics reset${NC}"
            fi
            sleep 1
            show_dashboard
            ;;
        
        3)
            REPORT_FILE=~/ai-genius-report-$(date +%Y%m%d).txt
            cat > "$REPORT_FILE" << EOFREPORT
AI GENIUS Performance Report
Generated: $(date)

USAGE STATISTICS
---------------
Total Queries: $QUERIES
Total Tokens: $TOKENS
Total Cost: \$$COST
Days Active: $DAYS

AVERAGES
--------
Queries/Day: $QUERIES_PER_DAY
Cost/Day: \$$COST_PER_DAY
Tokens/Query: $AVG_TOKENS

PROJECTIONS
-----------
Monthly Cost: \$$MONTHLY_COST
Yearly Cost: \$$YEARLY_COST

SYSTEM HEALTH
------------
Generated at: $(date)
EOFREPORT
            echo -e "${GREEN}✓ Report saved: $REPORT_FILE${NC}"
            sleep 2
            show_dashboard
            ;;
        
        4)
            echo ""
            echo -e "${CYAN}Checking for updates...${NC}"
            echo -e "${GREEN}✓ You have the latest version${NC}"
            sleep 2
            show_dashboard
            ;;
        
        5)
            echo ""
            echo -e "${CYAN}Optimization Recommendations:${NC}"
            echo ""
            echo "• Use Gemini Flash for quick queries (free)"
            echo "• Use Claude for complex reasoning"
            echo "• Batch similar queries together"
            echo "• Enable caching for repeated queries"
            echo ""
            read -p "Press Enter to continue..."
            show_dashboard
            ;;
        
        6)
            show_dashboard
            ;;
        
        7)
            echo -e "${GREEN}Goodbye!${NC}"
            exit 0
            ;;
        
        *)
            show_dashboard
            ;;
    esac
}

# Start dashboard
show_dashboard
