#!/bin/bash
# INSTALL PREREQUISITES FOR NOIZYLAB OS
# Installs Node.js, npm, and Wrangler CLI

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_header() {
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}\n"
}

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

print_header "INSTALLING PREREQUISITES"

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    print_warning "Homebrew not found"
    print_info "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    print_success "Homebrew installed"
else
    print_success "Homebrew found"
fi

# Install Node.js
if ! command -v node &> /dev/null; then
    print_info "Installing Node.js..."
    brew install node
    print_success "Node.js installed"
else
    print_success "Node.js already installed: $(node --version)"
fi

# Install npm (comes with Node.js, but verify)
if ! command -v npm &> /dev/null; then
    print_error "npm not found (should come with Node.js)"
    exit 1
else
    print_success "npm already installed: $(npm --version)"
fi

# Install Wrangler CLI
if ! command -v wrangler &> /dev/null; then
    print_info "Installing Wrangler CLI..."
    npm install -g wrangler
    print_success "Wrangler CLI installed"
else
    print_success "Wrangler CLI already installed: $(wrangler --version 2>/dev/null || echo 'installed')"
fi

print_header "PREREQUISITES INSTALLED"
echo ""
echo "✅ Node.js: $(node --version)"
echo "✅ npm: $(npm --version)"
echo "✅ Wrangler: $(wrangler --version 2>/dev/null || echo 'installed')"
echo ""
print_success "All prerequisites ready!"
echo ""
print_info "You can now run: ./scripts/MASTER_SETUP.sh"

