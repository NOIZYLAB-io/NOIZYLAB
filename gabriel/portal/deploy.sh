#!/bin/bash
# NoizyLab Portal Deployment Script
# Deploys both API (Cloudflare Workers) and Frontend (Cloudflare Pages)

set -e

echo "🚀 NoizyLab Portal Deployment"
echo "================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check for required tools
check_requirements() {
    echo -e "${YELLOW}Checking requirements...${NC}"
    
    if ! command -v wrangler &> /dev/null; then
        echo -e "${RED}Error: wrangler not installed${NC}"
        echo "Install with: npm install -g wrangler"
        exit 1
    fi
    
    if ! command -v npm &> /dev/null; then
        echo -e "${RED}Error: npm not installed${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✓ All requirements met${NC}"
}

# Create R2 buckets if they don't exist
setup_r2() {
    echo -e "${YELLOW}Setting up R2 buckets...${NC}"
    
    # Check if buckets exist, create if not
    wrangler r2 bucket create gabriel-scans 2>/dev/null || echo "gabriel-scans already exists"
    wrangler r2 bucket create gabriel-references 2>/dev/null || echo "gabriel-references already exists"
    
    echo -e "${GREEN}✓ R2 buckets ready${NC}"
}

# Create KV namespaces if they don't exist
setup_kv() {
    echo -e "${YELLOW}Setting up KV namespaces...${NC}"
    
    # Create KV namespaces
    wrangler kv namespace create RESULTS 2>/dev/null || echo "RESULTS namespace exists"
    wrangler kv namespace create API_KEYS 2>/dev/null || echo "API_KEYS namespace exists"
    wrangler kv namespace create USERS 2>/dev/null || echo "USERS namespace exists"
    wrangler kv namespace create ANALYTICS 2>/dev/null || echo "ANALYTICS namespace exists"
    wrangler kv namespace create REFERENCES 2>/dev/null || echo "REFERENCES namespace exists"
    
    echo -e "${GREEN}✓ KV namespaces ready${NC}"
    echo -e "${YELLOW}NOTE: Update wrangler.toml with the KV namespace IDs${NC}"
}

# Set secrets
setup_secrets() {
    echo -e "${YELLOW}Setting up secrets...${NC}"
    echo "You will be prompted to enter each secret value"
    
    read -p "Set GEMINI_API_KEY? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        wrangler secret put GEMINI_API_KEY --name gabriel-vision-api
    fi
    
    read -p "Set ANTHROPIC_API_KEY? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        wrangler secret put ANTHROPIC_API_KEY --name gabriel-vision-api
    fi
    
    read -p "Set STRIPE_SECRET_KEY? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        wrangler secret put STRIPE_SECRET_KEY --name gabriel-vision-api
    fi
    
    read -p "Set STRIPE_WEBHOOK_SECRET? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        wrangler secret put STRIPE_WEBHOOK_SECRET --name gabriel-vision-api
    fi
    
    read -p "Set ELEVENLABS_API_KEY? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        wrangler secret put ELEVENLABS_API_KEY --name gabriel-vision-api
    fi
    
    echo -e "${GREEN}✓ Secrets configured${NC}"
}

# Deploy API Worker
deploy_api() {
    echo -e "${YELLOW}Deploying API Worker...${NC}"
    
    cd portal/api
    wrangler deploy
    cd ../..
    
    echo -e "${GREEN}✓ API deployed to api.noizylab.ai${NC}"
}

# Build and deploy frontend
deploy_frontend() {
    echo -e "${YELLOW}Building frontend...${NC}"
    
    cd portal/frontend
    npm install
    npm run build
    
    echo -e "${YELLOW}Deploying to Cloudflare Pages...${NC}"
    wrangler pages deploy dist --project-name=noizylab-portal
    
    cd ../..
    
    echo -e "${GREEN}✓ Frontend deployed${NC}"
}

# Deploy static landing page
deploy_landing() {
    echo -e "${YELLOW}Deploying landing page...${NC}"
    
    wrangler pages deploy portal/landing --project-name=noizylab
    
    echo -e "${GREEN}✓ Landing page deployed to noizylab.ai${NC}"
}

# Main deployment flow
main() {
    echo ""
    echo "Select deployment option:"
    echo "1) Full deployment (API + Frontend + Landing)"
    echo "2) API only"
    echo "3) Frontend only"
    echo "4) Landing page only"
    echo "5) Setup infrastructure (R2, KV, Secrets)"
    echo "6) Exit"
    echo ""
    
    read -p "Enter option (1-6): " option
    
    case $option in
        1)
            check_requirements
            deploy_api
            deploy_frontend
            deploy_landing
            echo -e "${GREEN}🎉 Full deployment complete!${NC}"
            ;;
        2)
            check_requirements
            deploy_api
            ;;
        3)
            check_requirements
            deploy_frontend
            ;;
        4)
            check_requirements
            deploy_landing
            ;;
        5)
            check_requirements
            setup_r2
            setup_kv
            setup_secrets
            ;;
        6)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid option${NC}"
            exit 1
            ;;
    esac
}

# Run main
main
