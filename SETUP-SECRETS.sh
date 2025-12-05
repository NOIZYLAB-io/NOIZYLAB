#!/bin/bash

################################################################################
# SETUP-SECRETS.sh
# Interactive script to configure all required secrets
################################################################################

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

clear
echo -e "${PURPLE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              SECRET CONFIGURATION WIZARD                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"
echo ""

echo -e "${CYAN}This script will help you configure all required secrets.${NC}"
echo -e "${CYAN}You can skip any secrets you don't have yet.${NC}"
echo ""
read -p "Press Enter to continue..."
echo ""

################################################################################
# ANTHROPIC API KEY
################################################################################

echo -e "${PURPLE}════ ANTHROPIC API KEY ════${NC}"
echo ""
echo -e "${CYAN}Required for:${NC}"
echo "  • noizylab-email-automation (AI-generated emails)"
echo "  • fishmusicinc-ai-assistant (AI music composition help)"
echo "  • noizyai-advanced-gateway (AI routing)"
echo ""
echo -e "${YELLOW}You have: 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${NC}"
echo ""
read -p "Configure Anthropic API key? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    read -p "Enter your Anthropic API key (or press Enter to use the one above): " anthropic_key
    
    if [ -z "$anthropic_key" ]; then
        anthropic_key="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"
    fi
    
    echo "$anthropic_key" | wrangler secret put ANTHROPIC_API_KEY --name noizylab-email-automation
    echo "$anthropic_key" | wrangler secret put ANTHROPIC_API_KEY --name fishmusicinc-ai-assistant
    echo "$anthropic_key" | wrangler secret put ANTHROPIC_API_KEY --name noizyai-advanced-gateway
    
    echo -e "${GREEN}✅ Anthropic API key configured${NC}"
else
    echo -e "${YELLOW}⚠️  Skipped Anthropic API key${NC}"
fi

echo ""

################################################################################
# TWILIO CREDENTIALS
################################################################################

echo -e "${PURPLE}════ TWILIO CREDENTIALS ════${NC}"
echo ""
echo -e "${CYAN}Required for:${NC}"
echo "  • noizylab-sms-notifications (SMS messaging)"
echo ""
read -p "Configure Twilio credentials? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    read -p "Enter your Twilio Account SID: " twilio_sid
    read -p "Enter your Twilio Auth Token: " twilio_token
    read -p "Enter your Twilio Phone Number (e.g., +15551234567): " twilio_phone
    
    echo "$twilio_sid" | wrangler secret put TWILIO_ACCOUNT_SID --name noizylab-sms-notifications
    echo "$twilio_token" | wrangler secret put TWILIO_AUTH_TOKEN --name noizylab-sms-notifications
    echo "$twilio_phone" | wrangler secret put TWILIO_PHONE_NUMBER --name noizylab-sms-notifications
    
    echo -e "${GREEN}✅ Twilio credentials configured${NC}"
else
    echo -e "${YELLOW}⚠️  Skipped Twilio credentials${NC}"
fi

echo ""

################################################################################
# STRIPE CREDENTIALS
################################################################################

echo -e "${PURPLE}════ STRIPE CREDENTIALS ════${NC}"
echo ""
echo -e "${CYAN}Required for:${NC}"
echo "  • payment-processing-system (Payment processing)"
echo ""
read -p "Configure Stripe credentials? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    read -p "Enter your Stripe Secret Key: " stripe_key
    read -p "Enter your Stripe Webhook Secret: " stripe_webhook
    
    echo "$stripe_key" | wrangler secret put STRIPE_SECRET_KEY --name payment-processing-system
    echo "$stripe_webhook" | wrangler secret put STRIPE_WEBHOOK_SECRET --name payment-processing-system
    
    echo -e "${GREEN}✅ Stripe credentials configured${NC}"
else
    echo -e "${YELLOW}⚠️  Skipped Stripe credentials${NC}"
fi

echo ""

################################################################################
# OPTIONAL: OPENAI API KEY
################################################################################

echo -e "${PURPLE}════ OPENAI API KEY (Optional) ════${NC}"
echo ""
echo -e "${CYAN}Optional for:${NC}"
echo "  • noizyai-api-worker (Additional AI model)"
echo ""
read -p "Configure OpenAI API key? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    read -p "Enter your OpenAI API key: " openai_key
    
    echo "$openai_key" | wrangler secret put OPENAI_API_KEY --name noizyai-api-worker
    
    echo -e "${GREEN}✅ OpenAI API key configured${NC}"
else
    echo -e "${YELLOW}⚠️  Skipped OpenAI API key${NC}"
fi

echo ""

################################################################################
# SUMMARY
################################################################################

echo -e "${PURPLE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              CONFIGURATION COMPLETE                       ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"
echo ""

echo -e "${GREEN}Secret configuration complete!${NC}"
echo ""
echo -e "${CYAN}Next steps:${NC}"
echo "  1. Run ./ACTIVATE-ALL-AGENTS.sh to deploy all workers"
echo "  2. Test your endpoints"
echo "  3. Monitor health at: https://health-monitoring-system.noizylab-ca.workers.dev/status"
echo ""

exit 0
