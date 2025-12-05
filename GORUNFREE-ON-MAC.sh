#!/bin/bash
################################################################################
# GORUNFREE-ON-MAC.sh
# Execute this on your Mac (GOD or DaFixer) to activate everything
################################################################################

clear
cat << 'EOF'
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║                     🚀 GORUNFREE 🚀                            ║
║                                                                ║
║              ACTIVATING YOUR LEGENDARY SYSTEM                  ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
EOF

echo ""
echo "🎯 This will activate all 16 Cloudflare Workers across 3 domains"
echo ""
echo "📍 Current location: $(pwd)"
echo ""

# Check if we're in the right directory
if [ ! -f "ACTIVATE-ALL-AGENTS.sh" ]; then
    echo "❌ Error: ACTIVATE-ALL-AGENTS.sh not found"
    echo ""
    echo "Make sure you:"
    echo "  1. Downloaded GORUNFREE-PACKAGE.tar.gz from Claude"
    echo "  2. Extracted it: tar -xzf GORUNFREE-PACKAGE.tar.gz"
    echo "  3. Changed to directory: cd cloudflare-workers"
    echo "  4. Run this script again"
    echo ""
    exit 1
fi

echo "✅ Found ACTIVATE-ALL-AGENTS.sh"
echo ""

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo "⚠️  wrangler not found. Installing..."
    npm install -g wrangler
fi
echo "✅ wrangler is installed"
echo ""

# Check authentication
echo "🔐 Checking Cloudflare authentication..."
if wrangler whoami &> /dev/null; then
    echo "✅ Already authenticated with Cloudflare"
else
    echo "⚠️  Not authenticated. Opening browser for login..."
    wrangler login
fi
echo ""

# Ask about secrets
echo "🔑 SECRET CONFIGURATION"
echo ""
echo "Do you want to configure secrets now?"
echo "  - Anthropic API key (AI features)"
echo "  - Twilio credentials (SMS)"
echo "  - Stripe credentials (payments)"
echo ""
read -p "Configure secrets? (y/n) [n]: " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🔧 Launching secret configuration wizard..."
    ./SETUP-SECRETS.sh
else
    echo "⏭️  Skipping secrets (you can add them later)"
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "🚀 ACTIVATING ALL WORKERS NOW!"
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""

# Execute the activation script
./ACTIVATE-ALL-AGENTS.sh

# Check the result
if [ $? -eq 0 ]; then
    echo ""
    echo "════════════════════════════════════════════════════════════"
    echo ""
    echo "✨✨✨ GORUNFREE COMPLETE! ✨✨✨"
    echo ""
    echo "Your legendary system is now LIVE!"
    echo ""
    echo "🌐 Check your workers:"
    echo "   https://health-monitoring-system.noizylab-ca.workers.dev/status"
    echo ""
    echo "📊 View analytics:"
    echo "   https://unified-analytics-dashboard.noizylab-ca.workers.dev"
    echo ""
    echo "🤖 Try Workers AI:"
    echo "   https://workers-ai-enhanced.noizylab-ca.workers.dev"
    echo ""
    echo "════════════════════════════════════════════════════════════"
else
    echo ""
    echo "⚠️  Activation completed with warnings"
    echo "   Check the log file for details"
    echo "   Some workers may need secrets configured"
    echo ""
    echo "Run: ./CHECK-SYSTEM-STATUS.sh to diagnose"
fi

echo ""
exit 0
