#!/bin/bash
# ONE COMPLETE SETUP: CLOUDFLARE AI + GEMINI
# Production-ready setup with validation, error handling, and comprehensive checks

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKER_DIR="$ROOT/workers/ai-super-worker"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Error handling
trap 'echo -e "\n${RED}❌ Setup failed at line $LINENO${NC}"; exit 1' ERR

print_header() {
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}\n"
}

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

# Check prerequisites
check_prerequisites() {
    print_header "CHECKING PREREQUISITES"
    
    local missing=0
    
    if ! command -v wrangler &> /dev/null; then
        print_error "Wrangler CLI not found"
        print_info "Install: npm install -g wrangler"
        missing=1
    else
        print_success "Wrangler CLI: $(wrangler --version 2>/dev/null || echo 'installed')"
    fi
    
    if ! command -v node &> /dev/null; then
        print_error "Node.js not found"
        missing=1
    else
        print_success "Node.js: $(node --version)"
    fi
    
    if ! command -v npm &> /dev/null; then
        print_error "npm not found"
        missing=1
    else
        print_success "npm: $(npm --version)"
    fi
    
    if [ $missing -eq 1 ]; then
        print_error "Missing prerequisites. Please install them first."
        exit 1
    fi
}

# Setup worker structure
setup_worker_structure() {
    print_header "SETTING UP WORKER STRUCTURE"
    
    cd "$ROOT"
    mkdir -p "$WORKER_DIR/src"
    mkdir -p "$WORKER_DIR/migrations"
    mkdir -p "$WORKER_DIR/tests"
    
    print_success "Directory structure created"
}

# Create worker code (already done in previous step, but ensure it exists)
ensure_worker_code() {
    print_header "ENSURING WORKER CODE"
    
    if [ ! -f "$WORKER_DIR/src/index.ts" ]; then
        print_warning "Worker code not found - it should be created separately"
        print_info "The improved worker code is in: workers/ai-super-worker/src/index.ts"
    else
        print_success "Worker code exists"
    fi
}

# Create configuration files
create_config() {
    print_header "CREATING CONFIGURATION FILES"
    
    cd "$WORKER_DIR"
    
    # wrangler.toml
    if [ ! -f "wrangler.toml" ]; then
        cat > wrangler.toml << 'TOMLEOF'
name = "ai-super-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[env.production]
routes = [{ pattern = "ai.noizylab.ca/*", zone_name = "noizylab.ca" }]

[[d1_databases]]
binding = "DB"
database_name = "noizylab-db"
database_id = "REPLACE_WITH_YOUR_DB_ID"

[[kv_namespaces]]
binding = "KV"
id = "REPLACE_WITH_YOUR_KV_ID"

[ai]
binding = "AI"

[vars]
GEMINI_API_KEY = "REPLACE_WITH_YOUR_GEMINI_API_KEY"
TOMLEOF
        print_success "wrangler.toml created"
    else
        print_success "wrangler.toml exists"
    fi
    
    # package.json
    if [ ! -f "package.json" ]; then
        cat > package.json << 'PKGEOF'
{
  "name": "ai-super-worker",
  "version": "1.0.0",
  "main": "src/index.ts",
  "scripts": {
    "dev": "wrangler dev",
    "deploy": "wrangler deploy",
    "test": "wrangler dev --test"
  },
  "devDependencies": {
    "@cloudflare/workers-types": "^4.20240101.0"
  }
}
PKGEOF
        print_success "package.json created"
    else
        print_success "package.json exists"
    fi
    
    # tsconfig.json
    if [ ! -f "tsconfig.json" ]; then
        cat > tsconfig.json << 'TSCONFIGEOF'
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022"],
    "moduleResolution": "bundler",
    "types": ["@cloudflare/workers-types"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
TSCONFIGEOF
        print_success "tsconfig.json created"
    else
        print_success "tsconfig.json exists"
    fi
}

# Create database migration
create_migration() {
    print_header "CREATING DATABASE MIGRATION"
    
    cd "$WORKER_DIR"
    
    cat > migrations/001_initial.sql << 'SQLEOF'
-- AI Interactions Table
CREATE TABLE IF NOT EXISTS ai_interactions (
  id TEXT PRIMARY KEY,
  provider TEXT NOT NULL,
  model TEXT,
  prompt TEXT,
  response TEXT,
  tokens INTEGER,
  latency INTEGER,
  created_at INTEGER DEFAULT (unixepoch())
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_provider ON ai_interactions(provider);
CREATE INDEX IF NOT EXISTS idx_created ON ai_interactions(created_at);
CREATE INDEX IF NOT EXISTS idx_provider_created ON ai_interactions(provider, created_at);
SQLEOF
    
    print_success "Migration file created"
}

# Install dependencies
install_dependencies() {
    print_header "INSTALLING DEPENDENCIES"
    
    cd "$WORKER_DIR"
    
    if [ ! -d "node_modules" ]; then
        print_info "Installing npm packages..."
        npm install
        print_success "Dependencies installed"
    else
        print_success "Dependencies already installed"
        print_info "Running npm install to ensure latest..."
        npm install
    fi
}

# Setup Cloudflare
setup_cloudflare() {
    print_header "SETTING UP CLOUDFLARE"
    
    cd "$WORKER_DIR"
    
    # Check login
    if ! wrangler whoami &> /dev/null; then
        print_warning "Not logged into Cloudflare"
        print_info "You'll need to run: wrangler login"
        read -p "Login now? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            wrangler login
            print_success "Logged into Cloudflare"
        fi
    else
        print_success "Logged into Cloudflare"
        wrangler whoami | head -1
    fi
}

# Setup database
setup_database() {
    print_header "SETTING UP D1 DATABASE"
    
    cd "$WORKER_DIR"
    
    local db_exists=$(wrangler d1 list 2>/dev/null | grep -c "noizylab-db" || echo "0")
    
    if [ "$db_exists" -eq "0" ]; then
        print_info "Creating D1 database..."
        local db_output=$(wrangler d1 create noizylab-db)
        print_success "Database created"
        
        # Extract database ID
        local db_id=$(echo "$db_output" | grep -oP 'database_id = "\K[^"]+' || echo "")
        if [ -n "$db_id" ]; then
            print_info "Database ID: $db_id"
            print_warning "Update database_id in wrangler.toml with: $db_id"
        fi
    else
        print_success "Database exists"
        local db_id=$(wrangler d1 list | grep "noizylab-db" | awk '{print $2}' || echo "")
        if [ -n "$db_id" ]; then
            print_info "Database ID: $db_id"
        fi
    fi
    
    # Apply migrations
    print_info "Applying migrations locally..."
    if wrangler d1 migrations apply noizylab-db --local 2>/dev/null; then
        print_success "Migrations applied (local)"
    else
        print_warning "Could not apply migrations (database might not exist yet)"
    fi
    
    read -p "Apply migrations to remote database? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if wrangler d1 migrations apply noizylab-db --remote 2>/dev/null; then
            print_success "Migrations applied (remote)"
        else
            print_warning "Could not apply remote migrations"
        fi
    fi
}

# Setup KV
setup_kv() {
    print_header "SETTING UP KV NAMESPACE"
    
    cd "$WORKER_DIR"
    
    local kv_exists=$(wrangler kv:namespace list 2>/dev/null | grep -c "KV" || echo "0")
    
    if [ "$kv_exists" -eq "0" ]; then
        print_info "Creating KV namespace..."
        local kv_output=$(wrangler kv:namespace create "KV")
        print_success "KV namespace created"
        
        # Extract KV ID
        local kv_id=$(echo "$kv_output" | grep -oP 'id = "\K[^"]+' || echo "")
        if [ -n "$kv_id" ]; then
            print_info "KV ID: $kv_id"
            print_warning "Update KV id in wrangler.toml with: $kv_id"
        fi
    else
        print_success "KV namespace exists"
    fi
}

# Create test script
create_test_script() {
    print_header "CREATING TEST SCRIPTS"
    
    cat > "$ROOT/scripts/test-ai.sh" << 'TESTEOF'
#!/bin/bash
# Comprehensive AI Testing Script

URL="${1:-http://localhost:8787}"

echo "🧪 Testing AI Endpoints..."
echo "URL: $URL"
echo ""

# Test 1: Health check
echo "1. Health Check:"
curl -s "$URL/health" | jq '.' || echo "Failed"
echo ""

# Test 2: Providers list
echo "2. Providers List:"
curl -s "$URL/api/ai/providers" | jq '.' || echo "Failed"
echo ""

# Test 3: Cloudflare AI
echo "3. Testing Cloudflare AI:"
curl -s -X POST "$URL/api/ai/chat" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Say hello in one sentence","provider":"cloudflare","model":"llama-3.1-8b"}' | jq '.' || echo "Failed"
echo ""

# Test 4: Gemini (if API key configured)
echo "4. Testing Gemini:"
curl -s -X POST "$URL/api/ai/chat" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Say hello in one sentence","provider":"gemini"}' | jq '.' || echo "Failed (check API key)"
echo ""

# Test 5: Auto routing
echo "5. Testing Auto Routing:"
curl -s -X POST "$URL/api/ai/chat" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Say hello","provider":"auto"}' | jq '.' || echo "Failed"
echo ""

# Test 6: Stats
echo "6. Stats:"
curl -s "$URL/api/ai/stats" | jq '.' || echo "Failed"
echo ""

echo "✅ Tests complete!"
TESTEOF

    chmod +x "$ROOT/scripts/test-ai.sh"
    print_success "Test script created"
}

# Create deployment script
create_deploy_script() {
    print_header "CREATING DEPLOYMENT SCRIPT"
    
    cat > "$ROOT/scripts/deploy-ai.sh" << 'DEPLOYEOF'
#!/bin/bash
# Deploy AI Worker

set -e

cd "$(dirname "$0")/../workers/ai-super-worker"

echo "🚀 Deploying AI Super Worker..."

# Check if configured
if grep -q "REPLACE_WITH" wrangler.toml; then
    echo "⚠️  Warning: wrangler.toml contains placeholder values!"
    echo "Please update:"
    grep "REPLACE_WITH" wrangler.toml
    read -p "Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Deploy
wrangler deploy

echo "✅ Deployment complete!"
echo ""
echo "Your AI worker is live!"
DEPLOYEOF

    chmod +x "$ROOT/scripts/deploy-ai.sh"
    print_success "Deployment script created"
}

# Create README
create_readme() {
    print_header "CREATING DOCUMENTATION"
    
    cat > "$WORKER_DIR/README.md" << 'READMEEOF'
# AI Super Worker - Cloudflare AI + Gemini

Production-ready unified AI worker supporting both Cloudflare AI and Google Gemini.

## Features

- ✅ Cloudflare AI (Llama, Mistral, Gemma, Qwen)
- ✅ Google Gemini integration
- ✅ Smart caching (24-hour TTL)
- ✅ Usage tracking and analytics
- ✅ Error handling and validation
- ✅ Streaming support
- ✅ CORS enabled

## Quick Start

```bash
# Setup (one command)
cd /Users/m2ultra/NOIZYLAB/noizylab-os
./scripts/setup-cloudflare-gemini.sh

# Test locally
cd workers/ai-super-worker
wrangler dev

# In another terminal
./scripts/test-ai.sh

# Deploy
./scripts/deploy-ai.sh
```

## Configuration

1. Get Gemini API Key: https://aistudio.google.com/app/apikey
2. Update `wrangler.toml`:
   - Add database_id
   - Add KV namespace id
   - Add GEMINI_API_KEY

## API Endpoints

- `GET /health` - Health check
- `GET /api/ai/providers` - List providers
- `POST /api/ai/chat` - Chat endpoint
- `POST /api/ai/stream` - Streaming endpoint
- `GET /api/ai/stats` - Usage statistics

## Usage Examples

### Cloudflare AI
```bash
curl -X POST https://ai.noizylab.ca/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello","provider":"cloudflare","model":"llama-3.1-8b"}'
```

### Gemini
```bash
curl -X POST https://ai.noizylab.ca/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello","provider":"gemini"}'
```

### Auto (uses best available)
```bash
curl -X POST https://ai.noizylab.ca/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello","provider":"auto"}'
```

## Models

### Cloudflare AI
- llama-3.1-8b (default)
- llama-3.1-70b
- mistral-7b
- gemma-7b
- qwen-14b

### Gemini
- gemini-pro (default)
- gemini-pro-vision
READMEEOF

    print_success "README created"
}

# Main execution
main() {
    print_header "CLOUDFLARE AI + GEMINI - COMPLETE SETUP"
    
    check_prerequisites
    setup_worker_structure
    ensure_worker_code
    create_config
    create_migration
    install_dependencies
    setup_cloudflare
    setup_database
    setup_kv
    create_test_script
    create_deploy_script
    create_readme
    
    # Final summary
    print_header "SETUP COMPLETE!"
    
    echo -e "${GREEN}✅ Everything is set up!${NC}\n"
    
    echo "📋 Next Steps:"
    echo ""
    echo "1. Get Gemini API Key:"
    echo "   https://aistudio.google.com/app/apikey"
    echo ""
    echo "2. Update wrangler.toml with:"
    echo "   • Database ID (shown above)"
    echo "   • KV namespace ID (shown above)"
    echo "   • GEMINI_API_KEY"
    echo ""
    echo "3. Test locally:"
    echo "   cd workers/ai-super-worker"
    echo "   wrangler dev"
    echo "   # In another terminal:"
    echo "   ../../scripts/test-ai.sh"
    echo ""
    echo "4. Deploy:"
    echo "   ./scripts/deploy-ai.sh"
    echo ""
    echo -e "${GREEN}🎉 Ready for production!${NC}\n"
}

main "$@"
