#!/bin/bash
declare -A EMAILS=(
  ["noizy.ai"]="rsp@noizy.ai"
  ["noizyfish.com"]="rsp@noizyfish.com"
)

for DOMAIN in "${!EMAILS[@]}"; do
  EMAIL="${EMAILS[$DOMAIN]}"
  echo "📨 Creating mailbox: $EMAIL"
  godaddy-cli email create --domain $DOMAIN --address "rsp" --plan "Microsoft365"
done
