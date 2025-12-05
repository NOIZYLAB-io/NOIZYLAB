#!/bin/bash
# CHECK INSTALLATION STATUS
# Verifies everything is ready

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  INSTALLATION STATUS CHECK${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}\n"

cd "$ROOT"

errors=0
warnings=0

# Check prerequisites
echo "📦 PREREQUISITES:"
echo ""

if command -v node &> /dev/null; then
    echo -e "${GREEN}✅ Node.js: $(node --version)${NC}"
else
    echo -e "${RED}❌ Node.js: Not installed${NC}"
    ((errors++))
fi

if command -v npm &> /dev/null; then
    echo -e "${GREEN}✅ npm: $(npm --version)${NC}"
else
    echo -e "${RED}❌ npm: Not installed${NC}"
    ((errors++))
fi

if command -v wrangler &> /dev/null; then
    echo -e "${GREEN}✅ Wrangler: $(wrangler --version 2>/dev/null || echo 'installed')${NC}"
else
    echo -e "${RED}❌ Wrangler: Not installed${NC}"
    ((errors++))
fi

if command -v brew &> /dev/null; then
    echo -e "${GREEN}✅ Homebrew: $(brew --version | head -1)${NC}"
else
    echo -e "${YELLOW}⚠️  Homebrew: Not installed (optional)${NC}"
    ((warnings++))
fi

echo ""

# Check project files
echo "📁 PROJECT FILES:"
echo ""

[ -f "workers/ai-super-worker/src/index.ts" ] && echo -e "${GREEN}✅ Worker code${NC}" || { echo -e "${RED}❌ Worker code missing${NC}"; ((errors++)); }
[ -f "workers/ai-super-worker/wrangler.toml" ] && echo -e "${GREEN}✅ wrangler.toml${NC}" || { echo -e "${YELLOW}⚠️  wrangler.toml missing (will be created)${NC}"; ((warnings++)); }
[ -f "scripts/MASTER_SETUP.sh" ] && echo -e "${GREEN}✅ Master setup script${NC}" || { echo -e "${RED}❌ Master setup script missing${NC}"; ((errors++)); }
[ -f "scripts/setup-cloudflare-gemini.sh" ] && echo -e "${GREEN}✅ Setup script${NC}" || { echo -e "${RED}❌ Setup script missing${NC}"; ((errors++)); }
[ -f "migrations/sql/001_initial_schema.sql" ] && echo -e "${GREEN}✅ Database migration${NC}" || { echo -e "${YELLOW}⚠️  Migration missing (will be created)${NC}"; ((warnings++)); }

echo ""

# Check Cloudflare login
echo "☁️  CLOUDFLARE:"
echo ""

if command -v wrangler &> /dev/null; then
    if wrangler whoami &> /dev/null; then
        echo -e "${GREEN}✅ Logged into Cloudflare${NC}"
        wrangler whoami | head -1
    else
        echo -e "${YELLOW}⚠️  Not logged into Cloudflare${NC}"
        echo "   Run: wrangler login"
        ((warnings++))
    fi
else
    echo -e "${RED}❌ Cannot check (Wrangler not installed)${NC}"
fi

echo ""

# Summary
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
if [ $errors -eq 0 ] && [ $warnings -eq 0 ]; then
    echo -e "${GREEN}✅ INSTALLATION PERFECT - Ready to go!${NC}"
    echo ""
    echo "You can now run:"
    echo "  ./scripts/MASTER_SETUP.sh"
    exit 0
elif [ $errors -eq 0 ]; then
    echo -e "${YELLOW}⚠️  INSTALLATION READY with $warnings warning(s)${NC}"
    echo ""
    if [ $warnings -gt 0 ]; then
        echo "Warnings are non-critical. You can proceed with setup."
    fi
    exit 0
else
    echo -e "${RED}❌ INSTALLATION INCOMPLETE${NC}"
    echo ""
    echo "Missing prerequisites. Run:"
    echo "  ./scripts/install-prerequisites.sh"
    exit 1
fi

