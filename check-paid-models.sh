#!/bin/bash
# CHECK ALL PAID MODELS
# Verifies API keys and paid service access

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║           💰  PAID MODELS ACCESS CHECK  💰                ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

FOUND=0
MISSING=0
WORKING=0
FAILED=0

# Check 1: Claude (Anthropic) API
echo -e "${BLUE}[1] Claude API (Anthropic)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check in files
CLAUDE_KEY=$(grep -r "sk-ant-api03-jdXjxMTODL" . 2>/dev/null | head -1 | grep -o "sk-ant-api03-[a-zA-Z0-9_-]*")

if [ ! -z "$CLAUDE_KEY" ]; then
    KEY_START="${CLAUDE_KEY:0:20}"
    KEY_END="${CLAUDE_KEY: -10}"
    echo -e "${GREEN}✓ API Key Found${NC}"
    echo -e "  Key: ${CYAN}${KEY_START}...${KEY_END}${NC}"
    ((FOUND++))
    
    # Test the key
    echo -n "  Testing API... "
    RESPONSE=$(curl -s -w "%{http_code}" -o /tmp/claude_test.json \
        https://api.anthropic.com/v1/messages \
        -H "x-api-key: $CLAUDE_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -H "content-type: application/json" \
        -d '{
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 10,
            "messages": [{"role": "user", "content": "Hi"}]
        }' 2>/dev/null)
    
    if [ "$RESPONSE" = "200" ]; then
        echo -e "${GREEN}✓ WORKING${NC}"
        echo -e "  ${GREEN}✓ Claude Sonnet 4 accessible${NC}"
        echo -e "  Cost: \$3/M input, \$15/M output"
        ((WORKING++))
    else
        echo -e "${RED}✗ API Error (HTTP $RESPONSE)${NC}"
        ((FAILED++))
    fi
    
    # Check where it's configured
    echo -e "  Configured in:"
    grep -l "sk-ant-api03-jdXjxMTODL" *.sh *.js 2>/dev/null | while read file; do
        echo -e "    - $file"
    done
else
    echo -e "${RED}✗ API Key Not Found${NC}"
    echo -e "  Get one at: ${CYAN}https://console.anthropic.com${NC}"
    ((MISSING++))
fi
echo ""

# Check 2: GitHub Copilot
echo -e "${BLUE}[2] GitHub Copilot${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if command -v gh &> /dev/null; then
    if gh auth status 2>&1 | grep -q "Logged in"; then
        echo -e "${GREEN}✓ GitHub CLI authenticated${NC}"
        ((FOUND++))
        
        # Check Copilot subscription
        echo -n "  Checking Copilot subscription... "
        # This would require actual GitHub API call
        echo -e "${YELLOW}⚠ Manual verification needed${NC}"
        echo -e "  Visit: ${CYAN}https://github.com/settings/copilot${NC}"
    else
        echo -e "${YELLOW}⚠ GitHub CLI not authenticated${NC}"
        echo -e "  Login: ${CYAN}gh auth login${NC}"
        ((MISSING++))
    fi
else
    echo -e "${YELLOW}⚠ GitHub CLI not installed${NC}"
    echo -e "  Install: ${CYAN}brew install gh${NC}"
    echo -e "  Cost: \$10/month"
    ((MISSING++))
fi
echo ""

# Check 3: OpenAI (ChatGPT) API
echo -e "${BLUE}[3] OpenAI API (ChatGPT, GPT-4)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
OPENAI_KEY=$(security find-generic-password -a $USER -s "openai_api_key" -w 2>/dev/null || echo "")

if [ ! -z "$OPENAI_KEY" ]; then
    echo -e "${GREEN}✓ API Key Found in Keychain${NC}"
    echo -e "  Key: ${CYAN}sk-...${OPENAI_KEY: -10}${NC}"
    ((FOUND++))
    
    # Test the key
    echo -n "  Testing API... "
    RESPONSE=$(curl -s -w "%{http_code}" -o /tmp/openai_test.json \
        https://api.openai.com/v1/models \
        -H "Authorization: Bearer $OPENAI_KEY" 2>/dev/null)
    
    if [ "$RESPONSE" = "200" ]; then
        echo -e "${GREEN}✓ WORKING${NC}"
        echo -e "  ${GREEN}✓ GPT-4o, GPT-4 Turbo accessible${NC}"
        echo -e "  Cost: \$2.50-\$10/M tokens"
        ((WORKING++))
    else
        echo -e "${RED}✗ API Error (HTTP $RESPONSE)${NC}"
        ((FAILED++))
    fi
else
    echo -e "${YELLOW}⚠ API Key Not Found${NC}"
    echo -e "  Get one at: ${CYAN}https://platform.openai.com/api-keys${NC}"
    echo -e "  Note: ChatGPT Free (web) available without API key"
    ((MISSING++))
fi
echo ""

# Check 4: Google AI (Gemini) - FREE but check anyway
echo -e "${BLUE}[4] Google AI (Gemini)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
GOOGLE_KEY=$(security find-generic-password -a $USER -s "google_api_key" -w 2>/dev/null || echo "")

if [ ! -z "$GOOGLE_KEY" ]; then
    echo -e "${GREEN}✓ API Key Found in Keychain${NC}"
    echo -e "  Key: ${CYAN}AIza...${GOOGLE_KEY: -10}${NC}"
    ((FOUND++))
    
    echo -n "  Testing API... "
    RESPONSE=$(curl -s -w "%{http_code}" -o /tmp/google_test.json \
        "https://generativelanguage.googleapis.com/v1beta/models?key=$GOOGLE_KEY" 2>/dev/null)
    
    if [ "$RESPONSE" = "200" ]; then
        echo -e "${GREEN}✓ WORKING (FREE!)${NC}"
        echo -e "  ${GREEN}✓ Gemini 2.0 Flash, Gemini Pro accessible${NC}"
        echo -e "  Cost: \$0.075-\$0.125/M (essentially FREE)"
        ((WORKING++))
    else
        echo -e "${RED}✗ API Error (HTTP $RESPONSE)${NC}"
        ((FAILED++))
    fi
else
    echo -e "${YELLOW}⚠ API Key Not Found${NC}"
    echo -e "  Get FREE key at: ${CYAN}https://aistudio.google.com/app/apikey${NC}"
    ((MISSING++))
fi
echo ""

# Check 5: Cursor Pro
echo -e "${BLUE}[5] Cursor Pro${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if command -v cursor &> /dev/null || [ -d "/Applications/Cursor.app" ]; then
    echo -e "${GREEN}✓ Cursor installed${NC}"
    ((FOUND++))
    
    # Check for pro subscription
    if [ -f "$HOME/.cursor/state.json" ]; then
        if grep -q "pro" "$HOME/.cursor/state.json" 2>/dev/null; then
            echo -e "${GREEN}✓ Cursor Pro subscription detected${NC}"
            echo -e "  Cost: \$20/month"
            ((WORKING++))
        else
            echo -e "${YELLOW}⚠ Free version (Pro features limited)${NC}"
            echo -e "  Upgrade: ${CYAN}https://cursor.sh/pricing${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ Unable to detect subscription status${NC}"
        echo -e "  Check in Cursor: Settings → Account"
    fi
else
    echo -e "${YELLOW}⚠ Cursor not installed${NC}"
    echo -e "  Install: ${CYAN}brew install --cask cursor${NC}"
    echo -e "  Or: ${CYAN}https://cursor.sh${NC}"
    ((MISSING++))
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${PURPLE}SUMMARY${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${GREEN}✓ Found:        $FOUND${NC}"
echo -e "${GREEN}✓ Working:      $WORKING${NC}"
echo -e "${RED}✗ Failed:       $FAILED${NC}"
echo -e "${YELLOW}⚠ Missing:      $MISSING${NC}"
echo ""

# Accessible models
echo -e "${PURPLE}YOUR ACCESSIBLE PAID MODELS:${NC}"
echo ""

if [ $WORKING -gt 0 ]; then
    if curl -s https://api.anthropic.com/v1/messages -H "x-api-key: $CLAUDE_KEY" &>/dev/null; then
        echo -e "${GREEN}✓ Claude Sonnet 4${NC} - \$3/M input, \$15/M output"
        echo -e "  Model: claude-sonnet-4-20250514"
        echo -e "  200K context, best quality"
    fi
    
    if [ ! -z "$OPENAI_KEY" ]; then
        echo -e "${GREEN}✓ GPT-4o${NC} - \$2.50/M tokens"
        echo -e "${GREEN}✓ GPT-4 Turbo${NC} - \$10/M tokens"
    fi
    
    if [ ! -z "$GOOGLE_KEY" ]; then
        echo -e "${GREEN}✓ Gemini 2.0 Flash${NC} - \$0.075/M (FREE-tier pricing)"
        echo -e "${GREEN}✓ Gemini Pro${NC} - \$0.125/M"
    fi
    
    if command -v cursor &> /dev/null; then
        echo -e "${GREEN}✓ Cursor AI${NC} - GPT-4 integration"
    fi
else
    echo -e "${YELLOW}No paid API models currently accessible via API.${NC}"
    echo ""
    echo -e "You have ${GREEN}Claude API key configured${NC} in deployment files."
    echo -e "To activate it in AI GENIUS:"
    echo ""
    echo -e "  ${CYAN}security add-generic-password -a \$USER -s 'anthropic_api_key' -w '$CLAUDE_KEY'${NC}"
    echo ""
fi

echo ""
echo -e "${PURPLE}RECOMMENDATIONS:${NC}"
echo ""

if [ -z "$GOOGLE_KEY" ]; then
    echo -e "1. ${CYAN}Get FREE Gemini API key${NC}"
    echo -e "   ${CYAN}https://aistudio.google.com/app/apikey${NC}"
    echo -e "   (Essentially free, excellent quality)"
    echo ""
fi

if [ ! -z "$CLAUDE_KEY" ]; then
    echo -e "2. ${CYAN}Add Claude key to keychain${NC}"
    echo -e "   ${CYAN}security add-generic-password -a \$USER -s 'anthropic_api_key' -w '$CLAUDE_KEY'${NC}"
    echo ""
fi

if [ -z "$OPENAI_KEY" ]; then
    echo -e "3. ${YELLOW}Optional:${NC} Get OpenAI API key"
    echo -e "   ${CYAN}https://platform.openai.com/api-keys${NC}"
    echo -e "   (Or use ChatGPT Free web version)"
    echo ""
fi

if ! command -v cursor &> /dev/null; then
    echo -e "4. ${CYAN}Install Cursor (FREE)${NC}"
    echo -e "   ${CYAN}brew install --cask cursor${NC}"
    echo -e "   Best AI code editor"
    echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
