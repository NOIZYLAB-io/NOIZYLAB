#!/bin/bash
# NOIZYLAB API KEY SETUP
# GORUNFREE - One command sets everything

set -e

echo "🔑 NOIZYLAB CLAUDE API KEY SETUP"
echo "================================"
echo ""

# Check if key provided
if [ -z "$1" ]; then
    echo "Usage: $0 YOUR-API-KEY"
    echo ""
    echo "Example:"
    echo "  $0 sk-ant-api03-xxxxxxxxxxxxx"
    echo ""
    echo "Get your key at: https://console.anthropic.com/settings/keys"
    exit 1
fi

API_KEY="$1"

# Validate key format
if [[ ! $API_KEY == sk-ant-* ]]; then
    echo "❌ Invalid API key format"
    echo "Key should start with: sk-ant-"
    exit 1
fi

echo "✅ API key format valid"
echo ""

# Update DEPLOY.sh
echo "📝 Updating DEPLOY.sh with API key..."

sed -i.bak '/\[vars\]/,/^EOF/ {
    /ENVIRONMENT = "production"/a\
ANTHROPIC_API_KEY = "'"$API_KEY"'"
}' DEPLOY.sh

echo "✅ DEPLOY.sh updated"
echo ""

# Deploy
echo "🚀 Deploying with new API key..."
./DEPLOY.sh

echo ""
echo "================================"
echo "✅ API KEY CONFIGURED & DEPLOYED"
echo "================================"
echo ""
echo "Test AI diagnostics:"
echo "  curl -X POST https://noizylab-api.fishmusicinc.workers.dev/api/diagnose \\"
echo "    -H 'Content-Type: application/json' \\"
echo "    -d '{\"repair_id\":\"TEST-001\",\"device_type\":\"Desktop\",\"issue_description\":\"Won't boot\"}'"
echo ""
echo "Or open Tech Dashboard and run a diagnostic on any repair."
