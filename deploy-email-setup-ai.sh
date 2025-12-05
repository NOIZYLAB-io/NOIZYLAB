#!/bin/bash
# Deploy Email Setup AI Worker for iOS
# ====================================

BASE="/Users/m2ultra/NOIZYLAB/cloudflare"

echo "🤖 Deploying Email Setup AI Worker"
echo "==================================="
echo ""

cd "$BASE"

# Check wrangler
if ! command -v wrangler &> /dev/null; then
    echo "📦 Installing Wrangler..."
    npm install -g wrangler
fi

# Login if needed
echo "🔐 Checking Cloudflare login..."
wrangler whoami >/dev/null 2>&1 || wrangler login

# Deploy worker
echo "🚀 Deploying worker..."
wrangler deploy --config wrangler-email-setup.toml

echo ""
echo "✅ Email Setup AI Worker deployed!"
echo ""
echo "📱 Access from iPad/iPhone:"
echo "   https://noizylab-email-setup-ai.your-subdomain.workers.dev"
echo ""
echo "🔗 Or use the URL shown after deployment"
echo ""

