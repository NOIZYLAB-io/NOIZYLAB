#!/bin/bash
# FISH MUSIC INC - ONE-COMMAND CLOUDFLARE DNS SETUP
# Usage: ./setup-cloudflare-dns.sh YOUR_CLOUDFLARE_API_TOKEN

set -e

API_TOKEN="$1"
ZONE_ID="2446d788cc4280f5ea22a9948410c355"
DOMAIN="fishmusicinc.com"

if [ -z "$API_TOKEN" ]; then
    echo "❌ ERROR: Provide your Cloudflare API token"
    echo ""
    echo "Get it here: https://dash.cloudflare.com/profile/api-tokens"
    echo "Create token with: Zone.DNS.Edit permission"
    echo ""
    echo "Usage: ./setup-cloudflare-dns.sh YOUR_API_TOKEN"
    exit 1
fi

echo ""
echo "🚀 FISH MUSIC INC - CLOUDFLARE DNS SETUP"
echo "========================================"
echo ""

# Function to add DNS record
add_record() {
    local type=$1
    local name=$2
    local content=$3
    local proxied=$4
    local priority=$5
    
    echo "Adding: $type $name → $content"
    
    JSON_DATA=$(cat <<EOF
{
    "type": "$type",
    "name": "$name",
    "content": "$content",
    "proxied": $proxied,
    "ttl": 1
}
EOF
    )
    
    if [ "$type" = "MX" ]; then
        JSON_DATA=$(cat <<EOF
{
    "type": "$type",
    "name": "$name",
    "content": "$content",
    "proxied": $proxied,
    "priority": $priority,
    "ttl": 1
}
EOF
        )
    fi
    
    curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
         -H "Authorization: Bearer $API_TOKEN" \
         -H "Content-Type: application/json" \
         --data "$JSON_DATA" | grep -q '"success":true' && echo "  ✅ Added" || echo "  ⚠️  May already exist"
}

# Add A records
add_record "A" "$DOMAIN" "192.0.2.1" "true" ""
add_record "A" "www" "192.0.2.1" "true" ""

# Add CNAME records
add_record "CNAME" "api" "$DOMAIN" "true" ""
add_record "CNAME" "webhooks" "$DOMAIN" "true" ""
add_record "CNAME" "shop" "$DOMAIN" "true" ""
add_record "CNAME" "portal" "$DOMAIN" "true" ""
add_record "CNAME" "studio" "$DOMAIN" "true" ""

echo ""
echo "✅ DNS RECORDS ADDED!"
echo ""
echo "⚠️  IMPORTANT: Update A records with real IP when you deploy website!"
echo "    Current placeholder: 192.0.2.1"
echo ""
echo "📧 NEXT STEP: Enable Cloudflare Email Routing"
echo "    Go to: https://dash.cloudflare.com/$ZONE_ID/fishmusicinc.com/email/routing"
echo "    Click 'Get started' - Cloudflare auto-configures email DNS"
echo "    Add forwards:"
echo "      rp@fishmusicinc.com → rsp@noizyfish.com"
echo "      gofish@fishmusicinc.com → rsp@noizyfish.com"
echo ""
echo "🚀 GORUNFREE!"
echo ""


