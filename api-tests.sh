#!/bin/bash
# NOIZYLAB API TESTING EXAMPLES
# Demonstrates all API endpoints with curl

API_URL="https://noizylab-api.fishmusicinc.workers.dev"

echo "🧪 NOIZYLAB API Testing Suite"
echo "=============================="
echo ""

# 1. Health Check
echo "1️⃣  Health Check"
echo "GET $API_URL/api/health"
curl -s $API_URL/api/health | jq .
echo ""
echo "---"
echo ""

# 2. Create Customer
echo "2️⃣  Create Customer"
echo "POST $API_URL/api/customers"
CUSTOMER_DATA='{
  "name": "John Test",
  "email": "john.test@example.com",
  "phone": "555-0123",
  "city": "Toronto",
  "province": "ON"
}'
echo "Data: $CUSTOMER_DATA"
CUSTOMER_RESPONSE=$(curl -s -X POST $API_URL/api/customers \
  -H "Content-Type: application/json" \
  -d "$CUSTOMER_DATA")
echo "$CUSTOMER_RESPONSE" | jq .
CUSTOMER_ID=$(echo "$CUSTOMER_RESPONSE" | jq -r .customer_id)
echo ""
echo "---"
echo ""

# 3. Get Customer
echo "3️⃣  Get Customer"
echo "GET $API_URL/api/customers/$CUSTOMER_ID"
curl -s $API_URL/api/customers/$CUSTOMER_ID | jq .
echo ""
echo "---"
echo ""

# 4. Create Repair
echo "4️⃣  Create Repair"
echo "POST $API_URL/api/repairs"
REPAIR_DATA='{
  "customer_id": "'$CUSTOMER_ID'",
  "device_type": "Desktop PC",
  "brand": "Dell",
  "model": "OptiPlex 7090",
  "issue_description": "Computer won't boot, fans spin but no display",
  "priority": "high"
}'
echo "Data: $REPAIR_DATA"
REPAIR_RESPONSE=$(curl -s -X POST $API_URL/api/repairs \
  -H "Content-Type: application/json" \
  -d "$REPAIR_DATA")
echo "$REPAIR_RESPONSE" | jq .
REPAIR_ID=$(echo "$REPAIR_RESPONSE" | jq -r .repair_id)
echo ""
echo "---"
echo ""

# 5. Get Repair
echo "5️⃣  Get Repair"
echo "GET $API_URL/api/repairs/$REPAIR_ID"
curl -s $API_URL/api/repairs/$REPAIR_ID | jq .
echo ""
echo "---"
echo ""

# 6. AI Diagnosis
echo "6️⃣  AI Diagnosis"
echo "POST $API_URL/api/diagnose"
DIAGNOSE_DATA='{
  "repair_id": "'$REPAIR_ID'",
  "device_type": "Desktop PC",
  "issue_description": "Computer won't boot, fans spin but no display"
}'
echo "Data: $DIAGNOSE_DATA"
curl -s -X POST $API_URL/api/diagnose \
  -H "Content-Type: application/json" \
  -d "$DIAGNOSE_DATA" | jq .
echo ""
echo "---"
echo ""

# 7. Update Repair Status
echo "7️⃣  Update Repair Status"
echo "PUT $API_URL/api/repairs/$REPAIR_ID"
UPDATE_DATA='{
  "status": "in_progress",
  "changed_by": "Rob",
  "notes": "Started diagnostics"
}'
echo "Data: $UPDATE_DATA"
curl -s -X PUT $API_URL/api/repairs/$REPAIR_ID \
  -H "Content-Type: application/json" \
  -d "$UPDATE_DATA" | jq .
echo ""
echo "---"
echo ""

# 8. List Repairs
echo "8️⃣  List All Repairs"
echo "GET $API_URL/api/repairs"
curl -s "$API_URL/api/repairs?limit=5" | jq .
echo ""
echo "---"
echo ""

# 9. Voice Command
echo "9️⃣  Voice Command Test"
echo "POST $API_URL/api/voice"
VOICE_DATA='{
  "command": "What is the status today?",
  "context": {}
}'
echo "Data: $VOICE_DATA"
curl -s -X POST $API_URL/api/voice \
  -H "Content-Type: application/json" \
  -d "$VOICE_DATA" | jq .
echo ""
echo "---"
echo ""

# 10. Dashboard Data
echo "🔟 Dashboard Data"
echo "GET $API_URL/api/dashboard"
curl -s $API_URL/api/dashboard | jq .
echo ""
echo "---"
echo ""

# 11. Today's Analytics
echo "1️⃣1️⃣  Today's Analytics"
echo "GET $API_URL/api/analytics/today"
curl -s $API_URL/api/analytics/today | jq .
echo ""
echo "---"
echo ""

# 12. Complete Repair
echo "1️⃣2️⃣  Complete Repair"
echo "PUT $API_URL/api/repairs/$REPAIR_ID"
COMPLETE_DATA='{
  "status": "completed",
  "actual_cost": 89.00,
  "actual_time": 2,
  "repair_notes": "Replaced faulty RAM module, tested thoroughly",
  "customer_satisfaction": 5,
  "payment_status": "paid",
  "changed_by": "Rob"
}'
echo "Data: $COMPLETE_DATA"
curl -s -X PUT $API_URL/api/repairs/$REPAIR_ID \
  -H "Content-Type: application/json" \
  -d "$COMPLETE_DATA" | jq .
echo ""
echo "---"
echo ""

echo "=============================="
echo "Testing Complete! ✅"
echo ""
echo "Test Customer ID: $CUSTOMER_ID"
echo "Test Repair ID: $REPAIR_ID"
echo ""
echo "These test records are now in your database."
echo "You can view them on the Tech Dashboard."
