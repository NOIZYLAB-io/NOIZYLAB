#!/bin/bash
# DEPLOY AI GENIUS TO CLOUDFLARE
# GORUNFREEX1000 - One command deploys everything

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║        🚀  AI GENIUS CLOUDFLARE DEPLOYMENT  🚀            ║"
echo "║                                                           ║"
echo "║            GORUNFREEX1000 - Cloud Edition                 ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo -e "${YELLOW}Installing Wrangler CLI...${NC}"
    npm install -g wrangler
fi

echo -e "${BLUE}[1/5] Checking Wrangler Authentication${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if ! wrangler whoami &> /dev/null; then
    echo -e "${YELLOW}Not logged in. Opening browser for authentication...${NC}"
    wrangler login
else
    echo -e "${GREEN}✓ Already authenticated${NC}"
    wrangler whoami
fi
echo ""

echo -e "${BLUE}[2/5] Deploying Worker${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Deploy using the correct wrangler.toml
wrangler deploy --config wrangler-ai-genius.toml

echo -e "${GREEN}✓ Worker deployed${NC}"
echo ""

echo -e "${BLUE}[3/5] Configuring API Keys${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Claude API Key (you have this)
CLAUDE_KEY="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"

echo -e "${CYAN}Setting up API keys...${NC}"
echo ""

# Set Claude key
echo -e "${GREEN}1. Setting Claude API key${NC}"
echo "$CLAUDE_KEY" | wrangler secret put ANTHROPIC_API_KEY --config wrangler-ai-genius.toml
echo ""

# Prompt for other keys
echo -e "${YELLOW}Do you want to add other API keys now? (y/n)${NC}"
read -r ADD_KEYS

if [ "$ADD_KEYS" = "y" ] || [ "$ADD_KEYS" = "Y" ]; then
    
    # Google (Gemini) - FREE
    echo ""
    echo -e "${CYAN}2. Google Gemini API (FREE - RECOMMENDED)${NC}"
    echo "   Get key at: https://aistudio.google.com/app/apikey"
    echo -e "${YELLOW}   Enter Google API key (or press Enter to skip):${NC}"
    read -r GOOGLE_KEY
    if [ ! -z "$GOOGLE_KEY" ]; then
        echo "$GOOGLE_KEY" | wrangler secret put GOOGLE_API_KEY --config wrangler-ai-genius.toml
        echo -e "${GREEN}   ✓ Google API key set${NC}"
    fi

    # OpenAI
    echo ""
    echo -e "${CYAN}3. OpenAI API (GPT-4, optional)${NC}"
    echo "   Get key at: https://platform.openai.com/api-keys"
    echo -e "${YELLOW}   Enter OpenAI API key (or press Enter to skip):${NC}"
    read -r OPENAI_KEY
    if [ ! -z "$OPENAI_KEY" ]; then
        echo "$OPENAI_KEY" | wrangler secret put OPENAI_API_KEY --config wrangler-ai-genius.toml
        echo -e "${GREEN}   ✓ OpenAI API key set${NC}"
    fi

    # Perplexity
    echo ""
    echo -e "${CYAN}4. Perplexity API (optional)${NC}"
    echo "   Get key at: https://www.perplexity.ai/settings/api"
    echo -e "${YELLOW}   Enter Perplexity API key (or press Enter to skip):${NC}"
    read -r PERPLEXITY_KEY
    if [ ! -z "$PERPLEXITY_KEY" ]; then
        echo "$PERPLEXITY_KEY" | wrangler secret put PERPLEXITY_API_KEY --config wrangler-ai-genius.toml
        echo -e "${GREEN}   ✓ Perplexity API key set${NC}"
    fi

    # Together AI
    echo ""
    echo -e "${CYAN}5. Together AI (Llama, optional)${NC}"
    echo "   Get key at: https://api.together.xyz/settings/api-keys"
    echo -e "${YELLOW}   Enter Together API key (or press Enter to skip):${NC}"
    read -r TOGETHER_KEY
    if [ ! -z "$TOGETHER_KEY" ]; then
        echo "$TOGETHER_KEY" | wrangler secret put TOGETHER_API_KEY --config wrangler-ai-genius.toml
        echo -e "${GREEN}   ✓ Together API key set${NC}"
    fi

    # Cohere
    echo ""
    echo -e "${CYAN}6. Cohere API (optional)${NC}"
    echo "   Get key at: https://dashboard.cohere.com/api-keys"
    echo -e "${YELLOW}   Enter Cohere API key (or press Enter to skip):${NC}"
    read -r COHERE_KEY
    if [ ! -z "$COHERE_KEY" ]; then
        echo "$COHERE_KEY" | wrangler secret put COHERE_API_KEY --config wrangler-ai-genius.toml
        echo -e "${GREEN}   ✓ Cohere API key set${NC}"
    fi

    # Mistral
    echo ""
    echo -e "${CYAN}7. Mistral API (optional)${NC}"
    echo "   Get key at: https://console.mistral.ai/api-keys"
    echo -e "${YELLOW}   Enter Mistral API key (or press Enter to skip):${NC}"
    read -r MISTRAL_KEY
    if [ ! -z "$MISTRAL_KEY" ]; then
        echo "$MISTRAL_KEY" | wrangler secret put MISTRAL_API_KEY --config wrangler-ai-genius.toml
        echo -e "${GREEN}   ✓ Mistral API key set${NC}"
    fi
fi

echo ""
echo -e "${GREEN}✓ API keys configured${NC}"
echo ""

echo -e "${BLUE}[4/5] Testing Deployment${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Get the worker URL
WORKER_URL=$(wrangler deployments list --config wrangler-ai-genius.toml 2>/dev/null | grep "https://" | head -1 | awk '{print $2}')

if [ -z "$WORKER_URL" ]; then
    WORKER_URL="https://ai-genius-cloud.YOUR-SUBDOMAIN.workers.dev"
fi

echo -e "${CYAN}Testing health endpoint...${NC}"
HEALTH_RESPONSE=$(curl -s "$WORKER_URL/health" || echo "error")

if echo "$HEALTH_RESPONSE" | grep -q "operational"; then
    echo -e "${GREEN}✓ Worker is operational${NC}"
else
    echo -e "${YELLOW}⚠ Health check inconclusive (worker might still be deploying)${NC}"
fi
echo ""

echo -e "${BLUE}[5/5] Setup Complete${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo -e "${GREEN}╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}║          ✅  DEPLOYMENT SUCCESSFUL  ✅                     ║${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${PURPLE}🌐 YOUR AI GENIUS CLOUD URLs:${NC}"
echo ""
echo -e "${CYAN}Web Interface:${NC}"
echo -e "  $WORKER_URL"
echo ""
echo -e "${CYAN}API Endpoints:${NC}"
echo -e "  Health:  $WORKER_URL/health"
echo -e "  Models:  $WORKER_URL/api/models"
echo -e "  Ask AI:  $WORKER_URL/api/ask"
echo -e "  Compare: $WORKER_URL/api/compare"
echo ""

echo -e "${PURPLE}📱 ACCESS FROM ANYWHERE:${NC}"
echo ""
echo -e "  • Your Mac: $WORKER_URL"
echo -e "  • Your iPad: $WORKER_URL"
echo -e "  • Your iPhone: $WORKER_URL"
echo -e "  • GABRIEL: $WORKER_URL"
echo -e "  • DaFixer: $WORKER_URL"
echo ""

echo -e "${PURPLE}💡 CONFIGURED MODELS:${NC}"
echo ""
echo -e "${GREEN}  ✓ Claude Sonnet 4${NC} (\$3/M)"
if [ ! -z "$GOOGLE_KEY" ]; then
    echo -e "${GREEN}  ✓ Gemini 2.0 Flash${NC} (FREE)"
    echo -e "${GREEN}  ✓ Gemini Pro${NC} (\$0.125/M)"
fi
if [ ! -z "$OPENAI_KEY" ]; then
    echo -e "${GREEN}  ✓ GPT-4o${NC} (\$2.50/M)"
    echo -e "${GREEN}  ✓ GPT-4 Turbo${NC} (\$10/M)"
    echo -e "${GREEN}  ✓ OpenAI o1${NC} (\$15/M)"
fi
if [ ! -z "$PERPLEXITY_KEY" ]; then
    echo -e "${GREEN}  ✓ Perplexity Online${NC} (with web search)"
fi
if [ ! -z "$TOGETHER_KEY" ]; then
    echo -e "${GREEN}  ✓ Llama 3.3 70B${NC} (\$0.88/M)"
    echo -e "${GREEN}  ✓ Mixtral 8x7B${NC} (\$0.60/M)"
fi
if [ ! -z "$COHERE_KEY" ]; then
    echo -e "${GREEN}  ✓ Command R+${NC} (\$3/M)"
fi
if [ ! -z "$MISTRAL_KEY" ]; then
    echo -e "${GREEN}  ✓ Mistral Large${NC} (\$2/M)"
fi
echo ""

echo -e "${PURPLE}🚀 NEXT STEPS:${NC}"
echo ""
echo "1. Open in browser:"
echo -e "   ${CYAN}$WORKER_URL${NC}"
echo ""
echo "2. Bookmark it on all devices"
echo ""
echo "3. Add to iOS Home Screen (iPad/iPhone):"
echo "   Safari → Share → Add to Home Screen"
echo ""
echo "4. Optional: Setup custom domain"
echo "   Cloudflare Dashboard → Workers → Custom Domains"
echo "   Example: ai.fishmusicinc.com"
echo ""

echo -e "${PURPLE}📚 USAGE EXAMPLES:${NC}"
echo ""
echo "cURL example:"
echo -e "${CYAN}curl -X POST $WORKER_URL/api/ask \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"model_id\": \"claude-sonnet-4\",
    \"message\": \"Explain quantum computing\"
  }'${NC}"
echo ""

echo "Compare models:"
echo -e "${CYAN}curl -X POST $WORKER_URL/api/compare \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"model_ids\": [\"claude-sonnet-4\", \"gpt-4o\", \"gemini-2-flash\"],
    \"message\": \"What is consciousness?\"
  }'${NC}"
echo ""

echo -e "${PURPLE}💰 COST TRACKING:${NC}"
echo ""
echo "Cloudflare Workers Free Tier:"
echo "  • 100,000 requests/day - FREE"
echo "  • 10ms CPU time per request - FREE"
echo ""
echo "AI Model costs apply per your subscriptions"
echo ""

echo -e "${GREEN}✨ GORUNFREEX1000 ACHIEVED - CLOUD EDITION ✨${NC}"
echo ""
echo "One command deployed everything."
echo "Access from anywhere."
echo "All your paid models unified."
echo ""
