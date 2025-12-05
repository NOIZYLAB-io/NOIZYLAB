#!/bin/bash

################################################################################
# CHECK-SYSTEM-STATUS.sh
# Comprehensive system health and status checker
################################################################################

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

clear
echo -e "${PURPLE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              SYSTEM STATUS CHECK                          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"
echo ""

# Counters
TOTAL=16
HEALTHY=0
UNHEALTHY=0
UNKNOWN=0

# Function to test endpoint
test_endpoint() {
    local name=$1
    local url=$2
    
    echo -ne "${CYAN}Testing ${name}...${NC} "
    
    # Try to fetch with timeout
    response=$(curl -s -o /dev/null -w "%{http_code}" "$url" --max-time 10 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        if [ "$response" -eq 200 ] || [ "$response" -eq 301 ] || [ "$response" -eq 302 ]; then
            echo -e "${GREEN}✅ HEALTHY (${response})${NC}"
            ((HEALTHY++))
            return 0
        else
            echo -e "${YELLOW}⚠️  WARNING (${response})${NC}"
            ((UNHEALTHY++))
            return 1
        fi
    else
        echo -e "${RED}❌ DOWN${NC}"
        ((UNHEALTHY++))
        return 2
    fi
}

echo -e "${CYAN}Checking all 16 workers...${NC}"
echo ""

# NOIZYLAB.CA Workers
echo -e "${PURPLE}═══ NOIZYLAB.CA (7 workers) ═══${NC}"
test_endpoint "Business Portal     " "https://noizylab-business-worker.noizylab-ca.workers.dev/health"
test_endpoint "Workflow Engine     " "https://noizylab-workflow-worker.noizylab-ca.workers.dev/health"
test_endpoint "AI Support          " "https://ai-genius-worker.noizylab-ca.workers.dev/health"
test_endpoint "Email Automation    " "https://noizylab-email-automation.noizylab-ca.workers.dev/health"
test_endpoint "SMS Notifications   " "https://noizylab-sms-notifications.noizylab-ca.workers.dev/health"
echo ""

# FISHMUSICINC.COM Workers
echo -e "${PURPLE}═══ FISHMUSICINC.COM (2 workers) ═══${NC}"
test_endpoint "Client Portal       " "https://fishmusicinc-portal-worker.fishmusicinc-com.workers.dev/health"
test_endpoint "AI Music Assistant  " "https://fishmusicinc-ai-assistant.fishmusicinc-com.workers.dev/health"
echo ""

# NOIZY.AI Workers
echo -e "${PURPLE}═══ NOIZY.AI (2 workers) ═══${NC}"
test_endpoint "API Gateway         " "https://noizyai-api-worker.noizy-ai.workers.dev/health"
test_endpoint "Advanced Gateway    " "https://noizyai-advanced-gateway.noizy-ai.workers.dev/health"
echo ""

# Cross-Platform Workers
echo -e "${PURPLE}═══ CROSS-PLATFORM (5 workers) ═══${NC}"
test_endpoint "Analytics Dashboard " "https://unified-analytics-dashboard.noizylab-ca.workers.dev/health"
test_endpoint "Customer Portal     " "https://customer-self-service-portal.noizylab-ca.workers.dev/health"
test_endpoint "Payment System      " "https://payment-processing-system.noizylab-ca.workers.dev/health"
test_endpoint "Health Monitoring   " "https://health-monitoring-system.noizylab-ca.workers.dev/health"
test_endpoint "Workers AI          " "https://workers-ai-enhanced.noizylab-ca.workers.dev/health"
echo ""

# Summary
echo -e "${PURPLE}════════════════════════════════════════════${NC}"
echo ""

health_percent=$((HEALTHY * 100 / TOTAL))

echo -e "${CYAN}╔═══════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║           STATUS SUMMARY                  ║${NC}"
echo -e "${CYAN}╠═══════════════════════════════════════════╣${NC}"
echo -e "${CYAN}║  Total Workers:     ${TOTAL}                    ║${NC}"
echo -e "${CYAN}║  Healthy:           ${GREEN}${HEALTHY}${CYAN}                     ║${NC}"
echo -e "${CYAN}║  Unhealthy:         ${YELLOW}${UNHEALTHY}${CYAN}                     ║${NC}"
echo -e "${CYAN}║  Health Rate:       ${GREEN}${health_percent}%${CYAN}                   ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════╝${NC}"
echo ""

# Overall status
if [ $HEALTHY -eq $TOTAL ]; then
    echo -e "${GREEN}✨✨✨ PERFECT! ALL SYSTEMS OPERATIONAL! ✨✨✨${NC}"
    echo ""
    echo -e "${CYAN}Your legendary system is running at 100% capacity.${NC}"
    exit 0
elif [ $HEALTHY -ge $((TOTAL * 75 / 100)) ]; then
    echo -e "${GREEN}✅ SYSTEM OPERATIONAL${NC}"
    echo ""
    echo -e "${CYAN}Most workers are healthy. Some may need secrets configured.${NC}"
    exit 0
elif [ $HEALTHY -ge $((TOTAL / 2)) ]; then
    echo -e "${YELLOW}⚠️  SYSTEM DEGRADED${NC}"
    echo ""
    echo -e "${YELLOW}Several workers need attention. Check secrets and deployment status.${NC}"
    exit 1
else
    echo -e "${RED}❌ SYSTEM CRITICAL${NC}"
    echo ""
    echo -e "${RED}Most workers are down. Run ACTIVATE-ALL-AGENTS.sh to redeploy.${NC}"
    exit 2
fi
