#!/bin/bash

# Zero-trust extractor: detect Google auth friction and fail over to local master.

CHECK_AUTH=$(curl -s -o /dev/null -w "%{http_code}" https://admin.google.com)

if [ "$CHECK_AUTH" != "200" ]; then
    echo "⚠️ FRICTION DETECTED: Google Identity Throttled."
    echo "🚀 ACTIVATING SOVEREIGN_LOCAL_MASTER..."
    # Sever Cloud-Auth, switch to local P24+Passkey Auth
    cloudflared tunnel restart --config ./local-master-config.yaml
    fish-engine play --asset "action_blocked.wav" # Alert the Architect
else
    echo "✅ IDENTITY_NOMINAL: Edge Sync Active."
fi
