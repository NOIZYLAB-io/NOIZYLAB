#!/bin/bash
# Tailscale Setup Script for Linux - NOIZYLAB
# This script automates the installation and initial configuration of Tailscale on Linux

set -e

echo "=== NOIZYLAB Tailscale Setup for Linux ==="
echo ""

# Detect Linux distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$ID
        VERSION=$VERSION_ID
    else
        echo "Error: Cannot detect Linux distribution"
        exit 1
    fi
    echo "Detected distribution: $DISTRO"
}

# Install Tailscale based on distribution
install_tailscale() {
    case $DISTRO in
        ubuntu|debian)
            echo "Installing Tailscale for Debian/Ubuntu..."
            
            # Get codename from /etc/os-release or use lsb_release
            if [ -f /etc/os-release ]; then
                . /etc/os-release
                CODENAME=$VERSION_CODENAME
            fi
            
            # Fallback to lsb_release if CODENAME is not set
            if [ -z "$CODENAME" ]; then
                if command -v lsb_release &> /dev/null; then
                    CODENAME=$(lsb_release -cs)
                else
                    echo "Installing lsb-release to detect version..."
                    sudo apt-get update
                    sudo apt-get install -y lsb-release
                    CODENAME=$(lsb_release -cs)
                fi
            fi
            
            # Verify CODENAME is set
            if [ -z "$CODENAME" ]; then
                echo "Error: Could not determine Ubuntu/Debian codename"
                exit 1
            fi
            
            # Add Tailscale repository
            curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/${CODENAME}.gpg | sudo tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null
            curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/${CODENAME}.list | sudo tee /etc/apt/sources.list.d/tailscale.list
            
            # Update and install
            sudo apt-get update
            sudo apt-get install -y tailscale
            
            echo "✓ Tailscale installed successfully"
            ;;
            
        fedora|rhel|centos)
            echo "Installing Tailscale for Fedora/RHEL..."
            
            # Ensure dnf-plugins-core is installed
            if ! sudo dnf config-manager --help &> /dev/null; then
                echo "Installing dnf-plugins-core..."
                sudo dnf install -y dnf-plugins-core
            fi
            
            # Add Tailscale repository
            sudo dnf config-manager --add-repo https://pkgs.tailscale.com/stable/fedora/tailscale.repo
            
            # Install
            sudo dnf install -y tailscale
            
            echo "✓ Tailscale installed successfully"
            ;;
            
        arch|manjaro)
            echo "Installing Tailscale for Arch Linux..."
            
            sudo pacman -S --noconfirm tailscale
            
            echo "✓ Tailscale installed successfully"
            ;;
            
        *)
            echo "Distribution not directly supported. Using universal install script..."
            echo "Downloading install script to /tmp/tailscale-install.sh for review..."
            
            curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
            
            echo ""
            echo "Please review the script at: /tmp/tailscale-install.sh"
            echo "Then run: sudo sh /tmp/tailscale-install.sh"
            exit 0
            ;;
    esac
}

# Enable and start Tailscale service
start_tailscale() {
    echo ""
    echo "Enabling and starting Tailscale service..."
    
    sudo systemctl enable --now tailscaled
    
    echo "✓ Tailscale service is running"
}

# Connect to Tailscale network
connect_tailscale() {
    echo ""
    echo "Connecting to Tailscale network..."
    echo ""
    
    sudo tailscale up
    
    echo ""
    echo "✓ Tailscale is now connected"
}

# Show status
show_status() {
    echo ""
    echo "=== Tailscale Status ==="
    tailscale status
    echo ""
    echo "=== Tailscale IP Address ==="
    tailscale ip -4
}

# Main execution
main() {
    # Check if already installed
    if command -v tailscale &> /dev/null; then
        echo "✓ Tailscale is already installed"
        tailscale version
        echo ""
        echo "To connect or reconnect, run: sudo tailscale up"
        exit 0
    fi
    
    detect_distro
    echo ""
    
    install_tailscale
    echo ""
    
    start_tailscale
    echo ""
    
    connect_tailscale
    echo ""
    
    show_status
    
    echo ""
    echo "=== Setup Complete ==="
    echo "For detailed configuration options, see: CODE_MASTER/TAILSCALE_SETUP.md"
}

main
