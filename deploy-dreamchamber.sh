#!/bin/bash
# THE DREAMCHAMBER DEPLOYMENT
# GORUNFREE X1000 - One Command = All AI Models Accessible

set -e

echo "🌌 =================================="
echo "   THE DREAMCHAMBER DEPLOYMENT"
echo "   All AI Models of Repute"
echo "=================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

ACCOUNT_ID="1323e14ace0c8d7362612d5b5c0d41bb"
ANTHROPIC_KEY="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"

echo -e "${BLUE}Creating wrangler.toml...${NC}"

cat > wrangler-dreamchamber.toml << EOF
name = "dreamchamber"
main = "dreamchamber-worker.js"
compatibility_date = "2024-11-01"
account_id = "$ACCOUNT_ID"

[vars]
ENVIRONMENT = "production"
ANTHROPIC_API_KEY = "$ANTHROPIC_KEY"

# Optional API Keys - Add as you get them:
# OPENAI_API_KEY = "sk-proj-YOUR-KEY"
# GOOGLE_API_KEY = "YOUR-GOOGLE-KEY"
# TOGETHER_API_KEY = "YOUR-TOGETHER-KEY"
# MISTRAL_API_KEY = "YOUR-MISTRAL-KEY"
# PERPLEXITY_API_KEY = "pplx-YOUR-KEY"
# XAI_API_KEY = "YOUR-XAI-KEY"
EOF

echo -e "${GREEN}✓ Configuration created${NC}"
echo ""

echo -e "${BLUE}Deploying DREAMCHAMBER...${NC}"
wrangler deploy --config wrangler-dreamchamber.toml

echo ""
echo "🌌 =================================="
echo -e "${GREEN}   DREAMCHAMBER DEPLOYED!${NC}"
echo "=================================="
echo ""
echo "🚀 Access at:"
echo "   https://dreamchamber.fishmusicinc.workers.dev"
echo ""
echo "📊 Current Models Available:"
echo "   ✅ Claude Sonnet 4 (Anthropic)"
echo "   ✅ Claude Opus 4 (Anthropic)"
echo ""
echo "➕ To Add More Models:"
echo "   1. Get API keys from:"
echo "      • OpenAI: https://platform.openai.com/api-keys"
echo "      • Google: https://makersuite.google.com/app/apikey"
echo "      • Together AI: https://api.together.xyz/settings/api-keys"
echo "      • Mistral: https://console.mistral.ai/api-keys"
echo "      • Perplexity: https://www.perplexity.ai/settings/api"
echo "      • xAI: https://console.x.ai"
echo ""
echo "   2. Edit wrangler-dreamchamber.toml"
echo "   3. Uncomment and add your keys"
echo "   4. Run: wrangler deploy --config wrangler-dreamchamber.toml"
echo ""
echo "🎤 Features:"
echo "   • Voice input ready"
echo "   • Compare multiple models side-by-side"
echo "   • Cost tracking"
echo "   • Performance metrics"
echo "   • Touchscreen optimized"
echo ""
echo "💡 Quick Test:"
echo "   1. Open https://dreamchamber.fishmusicinc.workers.dev"
echo "   2. Select 'Claude Sonnet 4'"
echo "   3. Ask: 'Explain quantum computing in simple terms'"
echo "   4. See response"
echo ""
echo "🎯 Pro Tip:"
echo "   Start with Claude (already configured)"
echo "   Add other models as you need them"
echo "   Each model is optional"
echo ""
echo "GORUNFREE X1000 COMPLETE ✨"
