#!/bin/bash
DOMAIN="fishmusicinc.com"
EMAIL="rp@$DOMAIN"

echo "🔧 Setting up domain: $DOMAIN"
godaddy-cli domain create $DOMAIN --privacy full

echo "🔐 Enabling SSL and DNSSEC"
godaddy-cli ssl enable $DOMAIN
godaddy-cli dnssec enable $DOMAIN

echo "📧 Provisioning email: $EMAIL"
godaddy-cli email create --domain $DOMAIN --address "rp" --plan "Microsoft365"

echo "✅ Domain $DOMAIN and email $EMAIL setup complete"
