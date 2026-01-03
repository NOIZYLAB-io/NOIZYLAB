#!/bin/bash
# Setup Email Routing for noizylab.ca
# ===================================

BASE="/Users/m2ultra/NOIZYLAB/cloudflare"

echo "📧 Setting Up Email Routing for noizylab.ca"
echo "============================================"
echo ""

cd "$BASE"

# Check for API token
if [ -z "$CLOUDFLARE_API_TOKEN" ]; then
    echo "⚠️  CLOUDFLARE_API_TOKEN not set"
    echo "   Set it with: export CLOUDFLARE_API_TOKEN='your-token'"
    echo ""
fi

# Set zone ID
export CLOUDFLARE_ZONE_ID="1323e14ace0c8d7362612d5b5c0d41bb"

echo "🌐 Zone ID: $CLOUDFLARE_ZONE_ID"
echo "📧 Domain: noizylab.ca"
echo ""

# Run setup
python3 setup-email-routing.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "🔗 View in Dashboard:"
echo "   https://dash.cloudflare.com/1323e14ace0c8d7362612d5b5c0d41bb/noizylab.ca/email/routing/overview"
echo ""

