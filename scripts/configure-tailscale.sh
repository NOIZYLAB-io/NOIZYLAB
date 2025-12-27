#!/bin/bash
# Tailscale Configuration Script for NOIZYLAB
# This script helps configure Tailscale with NOIZYLAB-specific settings

set -e

echo "=== NOIZYLAB Tailscale Configuration ==="
echo ""

# Check if Tailscale is installed
if ! command -v tailscale &> /dev/null; then
    echo "Error: Tailscale is not installed"
    echo "Please run the appropriate setup script first:"
    echo "  - macOS: ./scripts/setup-tailscale-macos.sh"
    echo "  - Linux: ./scripts/setup-tailscale-linux.sh"
    exit 1
fi

# Check if connected
check_connection() {
    echo "Checking Tailscale connection status..."
    if ! tailscale status &> /dev/null; then
        echo "Error: Tailscale is not connected"
        echo "Please run: sudo tailscale up"
        exit 1
    fi
    echo "✓ Tailscale is connected"
}

# Display current configuration
show_current_config() {
    echo ""
    echo "=== Current Configuration ==="
    echo ""
    echo "Tailscale Status:"
    tailscale status
    echo ""
    echo "IP Address:"
    tailscale ip -4 2>/dev/null || echo "Not available"
    echo ""
    echo "DNS Settings:"
    tailscale status --json 2>/dev/null | grep -i dns || echo "DNS info not available via JSON"
}

# Enable MagicDNS
enable_magicdns() {
    echo ""
    echo "=== Enable MagicDNS ==="
    echo ""
    echo "MagicDNS allows you to access devices by name instead of IP."
    echo "Example: ssh noizylab-server instead of ssh 100.x.y.z"
    echo ""
    echo "To enable MagicDNS:"
    echo "1. Visit https://login.tailscale.com/admin/dns"
    echo "2. Enable 'MagicDNS'"
    echo "3. Optionally add custom nameservers for your internal domains"
    echo ""
    read -p "Press Enter to continue..."
}

# Configure subnet routing
configure_subnet_routing() {
    echo ""
    echo "=== Configure Subnet Routing ==="
    echo ""
    echo "Subnet routing allows access to your NOIZYLAB internal networks."
    echo ""
    read -p "Do you want to advertise subnet routes? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your network CIDR (e.g., 192.0.2.0/24): " SUBNET
        
        if [ -z "$SUBNET" ]; then
            echo "No subnet provided, skipping..."
            return
        fi
        
        echo "Advertising subnet: $SUBNET"
        sudo tailscale up --advertise-routes="$SUBNET"
        
        echo ""
        echo "✓ Subnet routes advertised"
        echo ""
        echo "⚠️  Important: Approve this route in the admin console:"
        echo "https://login.tailscale.com/admin/machines"
    fi
}

# Configure exit node
configure_exit_node() {
    echo ""
    echo "=== Configure Exit Node ==="
    echo ""
    echo "An exit node routes all your internet traffic through another device."
    echo ""
    read -p "Do you want to advertise this device as an exit node? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Advertising as exit node..."
        sudo tailscale up --advertise-exit-node
        
        echo ""
        echo "✓ Exit node advertised"
        echo ""
        echo "⚠️  Important: Approve this exit node in the admin console:"
        echo "https://login.tailscale.com/admin/machines"
    fi
}

# Set up SSH access
configure_ssh() {
    echo ""
    echo "=== Configure Tailscale SSH ==="
    echo ""
    echo "Tailscale SSH allows secure SSH access without managing keys."
    echo ""
    read -p "Do you want to enable Tailscale SSH on this device? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Enabling Tailscale SSH..."
        sudo tailscale up --ssh
        
        echo ""
        echo "✓ Tailscale SSH enabled"
        echo ""
        echo "You can now SSH into this device using:"
        echo "  ssh username@hostname"
        echo ""
        echo "Configure ACLs for SSH access at:"
        echo "https://login.tailscale.com/admin/acls"
    fi
}

# Configure tags
configure_tags() {
    echo ""
    echo "=== Configure Device Tags ==="
    echo ""
    echo "Tags help organize devices and control access via ACLs."
    echo "Common NOIZYLAB tags: noizylab-servers, noizylab-dev, noizylab-prod"
    echo ""
    read -p "Enter tags (comma-separated, e.g., tag:noizylab-servers,tag:production): " TAGS
    
    if [ -n "$TAGS" ]; then
        echo "Note: Tags must be configured in ACLs before use."
        echo "Visit: https://login.tailscale.com/admin/acls"
        echo ""
        echo "After configuring ACLs, apply tags via the admin console:"
        echo "https://login.tailscale.com/admin/machines"
    fi
}

# Set hostname
set_hostname() {
    echo ""
    echo "=== Set Tailscale Hostname ==="
    echo ""
    read -p "Enter a hostname for this device (e.g., noizylab-web-01): " HOSTNAME
    
    if [ -n "$HOSTNAME" ]; then
        echo "Setting hostname to: $HOSTNAME"
        sudo tailscale up --hostname="$HOSTNAME"
        echo "✓ Hostname set to: $HOSTNAME"
    fi
}

# Interactive menu
interactive_menu() {
    while true; do
        echo ""
        echo "=== Configuration Menu ==="
        echo "1. Show current configuration"
        echo "2. Enable MagicDNS"
        echo "3. Configure subnet routing"
        echo "4. Configure exit node"
        echo "5. Configure Tailscale SSH"
        echo "6. Configure device tags"
        echo "7. Set hostname"
        echo "8. Exit"
        echo ""
        read -p "Select option (1-8): " -n 1 -r
        echo ""
        
        case $REPLY in
            1) show_current_config ;;
            2) enable_magicdns ;;
            3) configure_subnet_routing ;;
            4) configure_exit_node ;;
            5) configure_ssh ;;
            6) configure_tags ;;
            7) set_hostname ;;
            8) break ;;
            *) echo "Invalid option" ;;
        esac
    done
}

# Main execution
main() {
    check_connection
    show_current_config
    
    echo ""
    read -p "Would you like to configure advanced options? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        interactive_menu
    fi
    
    echo ""
    echo "=== Configuration Complete ==="
    echo ""
    echo "For more information, see: CODE_MASTER/TAILSCALE_SETUP.md"
}

main
