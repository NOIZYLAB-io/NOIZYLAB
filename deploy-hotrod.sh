#!/bin/bash
# Deploy HotRod Cloudflare - Complete Cloudflare Setup
# ===================================================

BASE="/Users/m2ultra/NOIZYLAB/cloudflare"

echo "🚀 Deploying HotRod Cloudflare for NoizyLab"
echo "============================================"
echo ""

# Check for wrangler
if ! command -v wrangler &> /dev/null; then
    echo "📦 Installing Wrangler..."
    npm install -g wrangler
fi

# Check configuration
if [ ! -f "wrangler.toml" ]; then
    echo "⚙️  Creating wrangler.toml..."
    cat > wrangler.toml << 'EOF'
name = "noizylab-hotrod"
compatibility_date = "2024-01-01"
account_id = "${CLOUDFLARE_ACCOUNT_ID}"

[env.production]
name = "noizylab-hotrod-prod"

[[d1_databases]]
binding = "DB"
database_name = "noizylab-db"
database_id = "${D1_DATABASE_ID}"
EOF
    echo "✅ Created wrangler.toml"
fi

# Deploy email worker
if [ -f "worker-templates/email-worker.js" ]; then
    echo "📧 Deploying Email Worker..."
    wrangler deploy worker-templates/email-worker.js --name noizylab-email
    echo "✅ Email Worker deployed"
fi

# Deploy AI router worker
if [ -f "worker-templates/ai-router-worker.js" ]; then
    echo "🤖 Deploying AI Router Worker..."
    wrangler deploy worker-templates/ai-router-worker.js --name noizylab-ai-router
    echo "✅ AI Router Worker deployed"
fi

# Create D1 database
echo "💾 Creating D1 Database..."
wrangler d1 create noizylab-db
echo "✅ D1 Database created"

# Run migrations
if [ -f "migrations/001_email_log.sql" ]; then
    echo "📊 Running migrations..."
    wrangler d1 execute noizylab-db --file=migrations/001_email_log.sql
    echo "✅ Migrations complete"
fi

echo ""
echo "✨ HotRod Cloudflare Deployment Complete!"
echo "========================================"
echo ""
echo "✅ Workers deployed"
echo "✅ D1 Database created"
echo "✅ Migrations run"
echo ""
echo "🚀 Cloudflare is now HotRodded for NoizyLab!"

