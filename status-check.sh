#!/bin/bash
# NOIZYLAB SYSTEM STATUS CHECK
# Quick health verification

echo "🔍 NOIZYLAB System Status Check"
echo "================================"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check API Health
echo -n "API Health: "
API_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" https://noizylab-api.fishmusicinc.workers.dev/api/health)
if [ "$API_RESPONSE" = "200" ]; then
    echo -e "${GREEN}✓ Operational${NC}"
else
    echo -e "${RED}✗ Failed (HTTP $API_RESPONSE)${NC}"
fi

# Check Customer Portal
echo -n "Customer Portal: "
CUSTOMER_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" https://noizylab-customer.fishmusicinc.workers.dev)
if [ "$CUSTOMER_RESPONSE" = "200" ]; then
    echo -e "${GREEN}✓ Online${NC}"
else
    echo -e "${RED}✗ Failed (HTTP $CUSTOMER_RESPONSE)${NC}"
fi

# Check Tech Dashboard
echo -n "Tech Dashboard: "
TECH_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" https://noizylab-tech.fishmusicinc.workers.dev)
if [ "$TECH_RESPONSE" = "200" ]; then
    echo -e "${GREEN}✓ Online${NC}"
else
    echo -e "${RED}✗ Failed (HTTP $TECH_RESPONSE)${NC}"
fi

echo ""

# Get Dashboard Data
echo "📊 Today's Stats:"
DASHBOARD=$(curl -s https://noizylab-api.fishmusicinc.workers.dev/api/dashboard)

if [ $? -eq 0 ]; then
    echo "$DASHBOARD" | jq -r '.today | "  Completed: \(.completed // 0) / 12\n  Revenue: $\(.revenue // 0)\n  In Progress: \(.in_progress // 0)\n  Pending: \(.pending // 0)"'
else
    echo -e "${RED}  Unable to fetch stats${NC}"
fi

echo ""

# Check Database
echo -n "Database: "
DB_CHECK=$(wrangler d1 info noizylab-repairs 2>&1)
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Connected${NC}"
else
    echo -e "${RED}✗ Connection failed${NC}"
fi

echo ""
echo "================================"
echo "Status check complete"
