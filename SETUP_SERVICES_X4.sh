#!/bin/bash
# ULTRA-FAST X4 SPEED SERVICE INTEGRATION SETUP

echo "=========================================="
echo "🚀 SERVICES INTEGRATION SETUP - X4 SPEED"
echo "=========================================="
echo ""

# Create environment configuration file
ENV_FILE="/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/.env_services"

cat > "$ENV_FILE" << 'EOF'
# ==================== SERVICE API KEYS ====================
# Cloudflare Configuration
export CLOUDFLARE_API_KEY="your_cloudflare_api_key_here"
export CLOUDFLARE_EMAIL="your_cloudflare_email_here"
export CF_ZONE_FISHMUSICINC="your_fishmusicinc_zone_id_here"
export CF_ZONE_NOIZYLAB="your_noizylab_zone_id_here"

# GoDaddy Configuration
export GODADDY_API_KEY="your_godaddy_api_key_here"
export GODADDY_API_SECRET="your_godaddy_api_secret_here"

# Slack Webhook
export SLACK_WEBHOOK_URL="your_slack_webhook_url_here"

# Microsoft 365 Configuration
export MS365_CLIENT_ID="your_ms365_client_id_here"
export MS365_CLIENT_SECRET="your_ms365_client_secret_here"
export MS365_TENANT_ID="your_ms365_tenant_id_here"

# Google Workspace Configuration
export GOOGLE_WORKSPACE_CREDS="/path/to/google-service-account.json"
EOF

echo "✓ Environment configuration file created: $ENV_FILE"
echo ""
echo "📝 NEXT STEPS:"
echo "  1. Edit $ENV_FILE with your actual API keys"
echo "  2. Run: source $ENV_FILE"
echo "  3. Run: python3 MASTER_SERVICES_INTEGRATION_X4.py"
echo ""
echo "🔑 WHERE TO GET API KEYS:"
echo ""
echo "CLOUDFLARE:"
echo "  • Go to: https://dash.cloudflare.com/profile/api-tokens"
echo "  • Create Global API Key or use API Token"
echo "  • Zone IDs: Dashboard > Domain > Overview (right sidebar)"
echo ""
echo "GODADDY:"
echo "  • Go to: https://developer.godaddy.com/keys"
echo "  • Create Production Key"
echo ""
echo "SLACK:"
echo "  • Go to: https://api.slack.com/apps"
echo "  • Create app > Incoming Webhooks > Add New Webhook"
echo ""
echo "MICROSOFT 365:"
echo "  • Go to: https://portal.azure.com"
echo "  • Azure Active Directory > App registrations > New registration"
echo "  • Get Client ID, Client Secret, Tenant ID"
echo ""
echo "GOOGLE WORKSPACE:"
echo "  • Go to: https://console.cloud.google.com"
echo "  • APIs & Services > Credentials > Create Service Account"
echo "  • Download JSON key file"
echo ""
echo "=========================================="
echo "✅ Setup ready! Edit .env_services and run!"
echo "=========================================="

# Make the Python script executable
chmod +x "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/MASTER_SERVICES_INTEGRATION_X4.py"

echo ""
echo "🚀 Quick Start:"
echo "  source $ENV_FILE"
echo "  python3 MASTER_SERVICES_INTEGRATION_X4.py"

