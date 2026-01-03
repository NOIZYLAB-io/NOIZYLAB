#!/bin/bash
# AUTO-DEPLOYMENT SCRIPT
set -e

echo "🚀 Deploying NOIZYLAB OS..."

# Deploy super-worker
cd workers/super-worker
wrangler deploy
cd ../..

# Deploy intake
cd workers/intake
wrangler deploy
cd ../..

# Deploy MC96
cd workers/mc96
wrangler deploy
cd ../..

# Apply migrations
wrangler d1 migrations apply noizylab-db --remote

echo "✅ Deployment complete!"
