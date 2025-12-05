#!/bin/bash
# CLOUDFLARE AI COMPLETE CLI
# Brings Cloudflare AI up to speed - setup, test, deploy, manage

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKER_DIR="$ROOT/workers/ai-super-worker"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}\n"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check prerequisites
check_prerequisites() {
    print_header "CHECKING PREREQUISITES"
    
    local missing=0
    
    if ! command -v wrangler &> /dev/null; then
        print_error "Wrangler CLI not found"
        echo "Install: npm install -g wrangler"
        missing=1
    else
        print_success "Wrangler CLI installed"
    fi
    
    if ! command -v node &> /dev/null; then
        print_error "Node.js not found"
        missing=1
    else
        print_success "Node.js installed ($(node --version))"
    fi
    
    if ! command -v npm &> /dev/null; then
        print_error "npm not found"
        missing=1
    else
        print_success "npm installed ($(npm --version))"
    fi
    
    if [ $missing -eq 1 ]; then
        print_error "Missing prerequisites. Please install them first."
        exit 1
    fi
}

# Setup Cloudflare AI worker
setup_worker() {
    print_header "SETTING UP CLOUDFLARE AI WORKER"
    
    cd "$ROOT"
    
    # Create worker directory if it doesn't exist
    mkdir -p "$WORKER_DIR/src"
    
    # Check if worker files exist
    if [ ! -f "$WORKER_DIR/src/index.ts" ]; then
        print_warning "Worker files not found. Creating from template..."
        
        # Copy from template or create
        if [ -f "$ROOT/workers/ai-super-worker/src/index.ts" ]; then
            print_success "Worker files already exist"
        else
            print_error "Worker source not found. Run bootstrap first."
            exit 1
        fi
    else
        print_success "Worker files found"
    fi
    
    # Install dependencies
    cd "$WORKER_DIR"
    if [ ! -f "package.json" ]; then
        print_warning "Creating package.json..."
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
    fi
    
    if [ ! -d "node_modules" ]; then
        print_warning "Installing dependencies..."
        npm install
        print_success "Dependencies installed"
    else
        print_success "Dependencies already installed"
    fi
}

# Configure Cloudflare
configure_cloudflare() {
    print_header "CONFIGURING CLOUDFLARE"
    
    cd "$WORKER_DIR"
    
    if [ ! -f "wrangler.toml" ]; then
        print_warning "Creating wrangler.toml..."
        cat > wrangler.toml << 'WRANGLEREOF'
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

[[r2_buckets]]
binding = "R2"
bucket_name = "noizylab-ai-cache"

[ai]
binding = "AI"
WRANGLEREOF
        print_warning "wrangler.toml created. Please update with your IDs!"
    else
        print_success "wrangler.toml exists"
    fi
    
    # Check if logged in
    if ! wrangler whoami &> /dev/null; then
        print_warning "Not logged into Cloudflare"
        echo "Run: wrangler login"
        read -p "Login now? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            wrangler login
            print_success "Logged into Cloudflare"
        fi
    else
        print_success "Logged into Cloudflare"
        wrangler whoami
    fi
}

# Create D1 database
setup_database() {
    print_header "SETTING UP D1 DATABASE"
    
    cd "$WORKER_DIR"
    
    # Check if database exists
    local db_exists=$(wrangler d1 list 2>/dev/null | grep -c "noizylab-db" || echo "0")
    
    if [ "$db_exists" -eq "0" ]; then
        print_warning "Creating D1 database..."
        wrangler d1 create noizylab-db
        print_success "Database created"
        print_warning "Update database_id in wrangler.toml with the ID above!"
    else
        print_success "Database exists"
    fi
    
    # Apply migrations
    if [ -f "$ROOT/migrations/sql/001_initial_schema.sql" ]; then
        print_warning "Applying migrations..."
        
        # Create migrations directory in worker
        mkdir -p migrations
        
        # Copy migration
        cp "$ROOT/migrations/sql/001_initial_schema.sql" migrations/001_initial_schema.sql
        
        # Add AI interactions table if not exists
        if ! grep -q "ai_interactions" migrations/001_initial_schema.sql 2>/dev/null; then
            cat >> migrations/001_initial_schema.sql << 'SQLEOF'

-- AI interactions
CREATE TABLE IF NOT EXISTS ai_interactions (
  id TEXT PRIMARY KEY,
  model TEXT NOT NULL,
  prompt TEXT,
  tokens INTEGER,
  latency INTEGER,
  created_at INTEGER
);
SQLEOF
        fi
        
        # Apply locally
        wrangler d1 migrations apply noizylab-db --local
        print_success "Migrations applied (local)"
        
        read -p "Apply to remote database? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            wrangler d1 migrations apply noizylab-db --remote
            print_success "Migrations applied (remote)"
        fi
    else
        print_warning "No migrations found. Creating basic schema..."
        mkdir -p migrations
        cat > migrations/001_initial.sql << 'SQLEOF'
CREATE TABLE IF NOT EXISTS ai_interactions (
  id TEXT PRIMARY KEY,
  model TEXT NOT NULL,
  prompt TEXT,
  tokens INTEGER,
  latency INTEGER,
  created_at INTEGER
);
SQLEOF
        wrangler d1 migrations apply noizylab-db --local
        print_success "Basic schema created"
    fi
}

# Setup KV namespace
setup_kv() {
    print_header "SETTING UP KV NAMESPACE"
    
    local kv_exists=$(wrangler kv:namespace list 2>/dev/null | grep -c "KV" || echo "0")
    
    if [ "$kv_exists" -eq "0" ]; then
        print_warning "Creating KV namespace..."
        wrangler kv:namespace create "KV"
        print_success "KV namespace created"
        print_warning "Update KV id in wrangler.toml with the ID above!"
    else
        print_success "KV namespace exists"
    fi
}

# Setup R2 bucket
setup_r2() {
    print_header "SETTING UP R2 BUCKET"
    
    local r2_exists=$(wrangler r2 bucket list 2>/dev/null | grep -c "noizylab-ai-cache" || echo "0")
    
    if [ "$r2_exists" -eq "0" ]; then
        print_warning "Creating R2 bucket..."
        wrangler r2 bucket create noizylab-ai-cache
        print_success "R2 bucket created"
    else
        print_success "R2 bucket exists"
    fi
}

# Test worker locally
test_worker() {
    print_header "TESTING WORKER LOCALLY"
    
    cd "$WORKER_DIR"
    
    print_warning "Starting local dev server..."
    print_warning "Press Ctrl+C to stop after testing"
    echo ""
    echo "Test endpoints:"
    echo "  GET  http://localhost:8787/api/ai/models"
    echo "  POST http://localhost:8787/api/ai/chat"
    echo ""
    echo "Example test:"
    echo '  curl -X POST http://localhost:8787/api/ai/chat \\'
    echo '    -H "Content-Type: application/json" \\'
    echo '    -d '"'"'{"prompt":"Hello, how are you?","model":"llama-3.1-8b"}'"'"
    echo ""
    
    read -p "Start dev server? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        wrangler dev
    fi
}

# Deploy worker
deploy_worker() {
    print_header "DEPLOYING WORKER"
    
    cd "$WORKER_DIR"
    
    print_warning "Deploying to Cloudflare..."
    wrangler deploy
    
    print_success "Worker deployed!"
    echo ""
    echo "Your AI worker is live at:"
    echo "  https://ai-super-worker.YOUR_SUBDOMAIN.workers.dev"
    echo "  or"
    echo "  https://ai.noizylab.ca (if route configured)"
}

# Check status
check_status() {
    print_header "CLOUDFLARE AI STATUS"
    
    cd "$WORKER_DIR"
    
    echo "📊 Worker Status:"
    if wrangler deployments list &> /dev/null; then
        wrangler deployments list | head -5
    else
        print_warning "No deployments found"
    fi
    
    echo ""
    echo "🗄️  Database Status:"
    wrangler d1 list | grep noizylab || print_warning "Database not found"
    
    echo ""
    echo "💾 KV Status:"
    wrangler kv:namespace list | grep KV || print_warning "KV namespace not found"
    
    echo ""
    echo "🪣 R2 Status:"
    wrangler r2 bucket list | grep noizylab || print_warning "R2 bucket not found"
}

# Quick test
quick_test() {
    print_header "QUICK TEST"
    
    local url="${1:-http://localhost:8787}"
    
    echo "Testing: $url"
    echo ""
    
    # Test models endpoint
    echo "1. Testing /api/ai/models..."
    curl -s "$url/api/ai/models" | jq '.' || echo "Failed"
    echo ""
    
    # Test chat endpoint
    echo "2. Testing /api/ai/chat..."
    curl -s -X POST "$url/api/ai/chat" \
      -H "Content-Type: application/json" \
      -d '{"prompt":"Say hello","model":"llama-3.1-8b"}' | jq '.' || echo "Failed"
    echo ""
    
    print_success "Tests complete"
}

# Main menu
show_menu() {
    print_header "CLOUDFLARE AI COMPLETE CLI"
    echo "1. 🔍 Check Prerequisites"
    echo "2. 📦 Setup Worker"
    echo "3. ⚙️  Configure Cloudflare"
    echo "4. 🗄️  Setup Database"
    echo "5. 💾 Setup KV Namespace"
    echo "6. 🪣 Setup R2 Bucket"
    echo "7. 🧪 Test Worker (Local)"
    echo "8. 🚀 Deploy Worker"
    echo "9. 📊 Check Status"
    echo "10. ⚡ Quick Test"
    echo "11. 🔥 Full Setup (All Steps)"
    echo "0. Exit"
    echo ""
}

# Full setup
full_setup() {
    print_header "FULL SETUP - BRINGING CLOUDFLARE AI UP TO SPEED"
    
    check_prerequisites
    setup_worker
    configure_cloudflare
    setup_database
    setup_kv
    setup_r2
    
    print_header "SETUP COMPLETE!"
    echo ""
    echo "Next steps:"
    echo "  1. Update wrangler.toml with your IDs"
    echo "  2. Run: ./scripts/cf-ai-cli.sh test"
    echo "  3. Run: ./scripts/cf-ai-cli.sh deploy"
    echo ""
}

# Main
main() {
    case "${1:-menu}" in
        check)
            check_prerequisites
            ;;
        setup)
            setup_worker
            ;;
        config)
            configure_cloudflare
            ;;
        db)
            setup_database
            ;;
        kv)
            setup_kv
            ;;
        r2)
            setup_r2
            ;;
        test)
            test_worker
            ;;
        deploy)
            deploy_worker
            ;;
        status)
            check_status
            ;;
        quick-test)
            quick_test "${2:-http://localhost:8787}"
            ;;
        full|all)
            full_setup
            ;;
        menu|*)
            while true; do
                show_menu
                read -p "Select option: " choice
                case $choice in
                    1) check_prerequisites ;;
                    2) setup_worker ;;
                    3) configure_cloudflare ;;
                    4) setup_database ;;
                    5) setup_kv ;;
                    6) setup_r2 ;;
                    7) test_worker ;;
                    8) deploy_worker ;;
                    9) check_status ;;
                    10) quick_test ;;
                    11) full_setup ;;
                    0) exit 0 ;;
                    *) print_error "Invalid option" ;;
                esac
                echo ""
                read -p "Press Enter to continue..."
            done
            ;;
    esac
}

main "$@"

