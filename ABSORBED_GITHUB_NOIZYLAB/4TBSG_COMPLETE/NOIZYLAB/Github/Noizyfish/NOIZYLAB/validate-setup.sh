#!/bin/bash
# VALIDATE COMPLETE SETUP
# Checks everything is configured correctly

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKER_DIR="$ROOT/workers/ai-super-worker"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }

echo "🔍 Validating Setup..."
echo ""

errors=0
warnings=0

# Check files exist
echo "📁 Checking files..."
[ -f "$WORKER_DIR/src/index.ts" ] && print_success "Worker code exists" || { print_error "Worker code missing"; ((errors++)); }
[ -f "$WORKER_DIR/wrangler.toml" ] && print_success "wrangler.toml exists" || { print_error "wrangler.toml missing"; ((errors++)); }
[ -f "$WORKER_DIR/package.json" ] && print_success "package.json exists" || { print_error "package.json missing"; ((errors++)); }
[ -f "$WORKER_DIR/migrations/001_initial.sql" ] && print_success "Migration exists" || { print_error "Migration missing"; ((errors++)); }

echo ""

# Check configuration
echo "⚙️  Checking configuration..."
cd "$WORKER_DIR"

if grep -q "REPLACE_WITH" wrangler.toml; then
    print_warning "wrangler.toml contains placeholders:"
    grep "REPLACE_WITH" wrangler.toml
    ((warnings++))
else
    print_success "wrangler.toml configured"
fi

echo ""

# Check dependencies
echo "📦 Checking dependencies..."
if [ -d "node_modules" ]; then
    print_success "Dependencies installed"
else
    print_error "Dependencies not installed"
    ((errors++))
fi

echo ""

# Check Cloudflare
echo "☁️  Checking Cloudflare..."
if wrangler whoami &> /dev/null; then
    print_success "Logged into Cloudflare"
else
    print_warning "Not logged into Cloudflare"
    ((warnings++))
fi

echo ""

# Summary
echo "════════════════════════════════════════"
if [ $errors -eq 0 ] && [ $warnings -eq 0 ]; then
    echo -e "${GREEN}✅ Setup is perfect!${NC}"
    exit 0
elif [ $errors -eq 0 ]; then
    echo -e "${YELLOW}⚠️  Setup complete with $warnings warning(s)${NC}"
    exit 0
else
    echo -e "${RED}❌ Setup has $errors error(s) and $warnings warning(s)${NC}"
    exit 1
fi

