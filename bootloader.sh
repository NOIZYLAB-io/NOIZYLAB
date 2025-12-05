#!/bin/bash
# NoizyLab OS Bootloader
# Initializes the entire system on first run

set -e

BASE="/Users/m2ultra/NOIZYLAB/noizylab-os"
SUPERCODE_DIR="$BASE/supercode"

echo "🚀 NoizyLab OS Bootloader"
echo "========================="
echo ""

# Check if already bootstrapped
if [ -f "$BASE/.bootstrapped" ]; then
    echo "✔️  System already bootstrapped"
    echo "   Run './supercode/SUPERBUILD.sh' to rebuild"
    exit 0
fi

# Step 1: Create directory structure
echo "📁 Creating directory structure..."
mkdir -p "$BASE/workers"
mkdir -p "$BASE/ai/router/bin"
mkdir -p "$BASE/ai/agents"
mkdir -p "$BASE/d1"
mkdir -p "$BASE/db/schema"
mkdir -p "$BASE/migrations/sql"
mkdir -p "$BASE/scripts"
mkdir -p "$BASE/supercode"
mkdir -p "$BASE/portal/src"
mkdir -p "$BASE/.noizy/cursor"

# Step 2: Create .env template if missing
if [ ! -f "$BASE/.env" ]; then
    echo "📝 Creating .env template..."
    cat > "$BASE/.env.template" << 'ENVEOF'
# Cloudflare Credentials
CF_ACCOUNT_ID=your_account_id_here
CF_API_TOKEN=your_api_token_here

# AI Provider Keys
GEMINI_API_KEY=your_gemini_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here

# D1 Database
D1_DATABASE_NAME=noizylab

# Environment
NODE_ENV=development
ENVEOF
    echo "⚠️  Created .env.template — please copy to .env and fill in values"
fi

# Step 3: Install global dependencies
echo "📦 Checking global dependencies..."
if ! command -v wrangler >/dev/null 2>&1; then
    echo "  Installing wrangler CLI..."
    npm install -g wrangler
fi

if ! command -v node >/dev/null 2>&1; then
    echo "❌ Node.js not found. Please install Node.js 18+ first."
    exit 1
fi

# Step 4: Setup Cursor config
echo "⚙️  Setting up Cursor configuration..."
if [ -f "$SUPERCODE_DIR/cursor-supercode.json" ]; then
    mkdir -p "$BASE/.noizy/cursor"
    cp "$SUPERCODE_DIR/cursor-supercode.json" "$BASE/.noizy/cursor/rules.json"
    echo "  ✔️  Cursor rules installed"
fi

# Step 5: Initialize root package.json if missing
if [ ! -f "$BASE/package.json" ]; then
    echo "📦 Creating root package.json..."
    cat > "$BASE/package.json" << 'PKGEOF'
{
  "name": "noizylab-os",
  "version": "1.0.0",
  "description": "NoizyLab Operating System",
  "private": true,
  "workspaces": [
    "workers/*",
    "ai/router",
    "portal"
  ],
  "scripts": {
    "superbuild": "./supercode/SUPERBUILD.sh",
    "guardian": "./supercode/guardian.sh",
    "test": "./supercode/test-harness.sh",
    "deploy": "./supercode/cf-supercode.js"
  },
  "devDependencies": {
    "@cloudflare/workers-types": "^4.20240122.0",
    "typescript": "^5.3.3",
    "wrangler": "^3.19.0"
  }
}
PKGEOF
fi

# Step 6: Create gitignore if missing
if [ ! -f "$BASE/.gitignore" ]; then
    echo "📝 Creating .gitignore..."
    cat > "$BASE/.gitignore" << 'GITEOF'
# Environment
.env
.env.local
.env.*.local

# Dependencies
node_modules/
.pnp
.pnp.js

# Build outputs
dist/
build/
.wrangler/

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Cloudflare
.wrangler/
.dev.vars
GITEOF
fi

# Step 7: Mark as bootstrapped
touch "$BASE/.bootstrapped"
echo ""
echo "✨ Bootstrapping complete!"
echo ""
echo "Next steps:"
echo "  1. Copy .env.template to .env and fill in your credentials"
echo "  2. Run: ./supercode/SUPERBUILD.sh"
echo "  3. Run: ./supercode/guardian.sh (to verify system health)"
echo ""

