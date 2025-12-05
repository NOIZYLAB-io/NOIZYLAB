#!/bin/bash
# DEPLOY AI GATEWAY TO CLOUDFLARE - 10X SPEED
echo "🚀 DEPLOYING AI GATEWAY TO CLOUDFLARE"

# Install Wrangler if needed
if ! command -v wrangler &> /dev/null; then
    echo "Installing Wrangler..."
    npm install -g wrangler
fi

# Login to Cloudflare
echo "Login to Cloudflare:"
wrangler login

# Set secrets
echo ""
echo "Setting up secrets..."
echo "Enter GEMINI_API_KEY:"
wrangler secret put GEMINI_API_KEY

echo "Enter CLAUDE_API_KEY:"
wrangler secret put CLAUDE_API_KEY

echo "Enter INTERNAL_AUTH_TOKEN:"
wrangler secret put INTERNAL_AUTH_TOKEN

# Deploy
echo ""
echo "Deploying worker..."
wrangler deploy

echo ""
echo "✅ AI Gateway deployed!"
echo "Your gateway URL will be shown above"

