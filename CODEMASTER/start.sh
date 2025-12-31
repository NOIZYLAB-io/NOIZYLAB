#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# 🚀 CODEMASTER STARTUP SCRIPT
# ═══════════════════════════════════════════════════════════════

set -e

CODEMASTER_ROOT="/Users/m2ultra/NOIZYLAB/CODEMASTER"
NOIZY_ROOT="/Users/m2ultra/NOIZY_AI"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}"
cat << 'EOF'
╔═══════════════════════════════════════════════════════════════╗
║  🚀 CODEMASTER STARTUP                                        ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Create data directories
echo -e "${YELLOW}📁 Creating data directories...${NC}"
mkdir -p "$NOIZY_ROOT/vault"
mkdir -p "$NOIZY_ROOT/catalog"
mkdir -p "$NOIZY_ROOT/evidence_packs"
mkdir -p "$NOIZY_ROOT/fleet"
mkdir -p "$NOIZY_ROOT/mc96/configs"
mkdir -p "$NOIZY_ROOT/cache/ai"
mkdir -p "$NOIZY_ROOT/logs"
echo -e "${GREEN}✓ Directories created${NC}"

# Check Docker
echo -e "\n${YELLOW}🐳 Checking Docker...${NC}"
if ! command -v docker &> /dev/null; then
    echo "Docker not found! Please install Docker Desktop."
    exit 1
fi

if ! docker info &> /dev/null; then
    echo "Docker daemon not running! Please start Docker Desktop."
    exit 1
fi
echo -e "${GREEN}✓ Docker is running${NC}"

# Build and start
echo -e "\n${YELLOW}🔨 Building and starting services...${NC}"
cd "$CODEMASTER_ROOT/infra/compose"

# Start services
docker compose up -d --build

echo -e "\n${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ CODEMASTER STARTED!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "\n📊 Service URLs:"
echo -e "   Portal:       http://localhost:8080"
echo -e "   Vault:        http://localhost:8000"
echo -e "   Catalog:      http://localhost:8001"
echo -e "   Evidence:     http://localhost:8002"
echo -e "   AI Gateway:   http://localhost:8100"
echo -e "   Fleet:        http://localhost:8200"
echo -e "   MC96:         http://localhost:8300"
echo -e "   Mesh:         http://localhost:8400"
echo -e "\n💻 Commands:"
echo -e "   docker compose logs -f    # View logs"
echo -e "   docker compose ps         # Check status"
echo -e "   docker compose down       # Stop services"
echo ""
