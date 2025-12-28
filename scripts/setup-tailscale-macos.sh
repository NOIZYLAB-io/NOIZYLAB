#!/bin/bash
# Tailscale Setup Script for macOS - NOIZYLAB
# This script automates the installation and initial configuration of Tailscale on macOS

set -e

echo "=== NOIZYLAB Tailscale Setup for macOS ==="
echo ""

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "Error: This script is for macOS only."
    exit 1
fi

# Function to check if Homebrew is installed
check_homebrew() {
    if ! command -v brew &> /dev/null; then
        echo "Homebrew is not installed. Installing Homebrew first..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    else
        echo "✓ Homebrew is already installed"
    fi
}

# Function to install Tailscale
install_tailscale() {
    if command -v tailscale &> /dev/null; then
        echo "✓ Tailscale is already installed"
        tailscale version
    else
        echo "Installing Tailscale via Homebrew..."
        brew install --cask tailscale
        echo "✓ Tailscale installed successfully"
    fi
}

# Function to start Tailscale
start_tailscale() {
    echo ""
    echo "Starting Tailscale..."
    
    # Open Tailscale app
    open -a Tailscale
    
    echo ""
    echo "✓ Tailscale app has been launched"
    echo ""
    echo "Next steps:"
    echo "1. Click the Tailscale icon in your menu bar"
    echo "2. Sign in with your account (Google, Microsoft, GitHub, or Email)"
    echo "3. Your device will automatically join your Tailscale network"
    echo ""
    echo "After authentication, run: tailscale status"
    echo "to verify your connection"
}

# Main execution
main() {
    echo "Starting Tailscale setup process..."
    echo ""
    
    check_homebrew
    echo ""
    
    install_tailscale
    echo ""
    
    start_tailscale
    
    echo ""
    echo "=== Setup Complete ==="
    echo "For detailed configuration options, see: CODE_MASTER/TAILSCALE_SETUP.md"
}

main
