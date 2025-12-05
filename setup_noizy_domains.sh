#!/bin/bash
for DOMAIN in "noizy.ai" "noizyfish.com"; do
  echo "🚀 Setting up $DOMAIN"
  godaddy-cli domain create $DOMAIN --privacy full
  godaddy-cli ssl enable $DOMAIN
  godaddy-cli dnssec enable $DOMAIN
done
