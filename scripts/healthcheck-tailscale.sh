#!/bin/bash
# Tailscale Health Check Script for NOIZYLAB
# This script verifies Tailscale connectivity and configuration

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=== NOIZYLAB Tailscale Health Check ==="
echo ""

# Check if Tailscale is installed
check_installed() {
    if command -v tailscale &> /dev/null; then
        echo -e "${GREEN}✓${NC} Tailscale is installed"
        tailscale version
        return 0
    else
        echo -e "${RED}✗${NC} Tailscale is not installed"
        return 1
    fi
}

# Check if Tailscale service is running
check_service() {
    echo ""
    echo "Checking Tailscale service..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if pgrep -x "Tailscale" > /dev/null; then
            echo -e "${GREEN}✓${NC} Tailscale service is running"
            return 0
        else
            echo -e "${RED}✗${NC} Tailscale service is not running"
            echo "  Start it from Applications or menu bar"
            return 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if systemctl is-active --quiet tailscaled; then
            echo -e "${GREEN}✓${NC} Tailscale service is running"
            return 0
        else
            echo -e "${RED}✗${NC} Tailscale service is not running"
            echo "  Start it with: sudo systemctl start tailscaled"
            return 1
        fi
    else
        echo -e "${YELLOW}?${NC} Cannot check service status on this platform"
        return 0
    fi
}

# Check if connected to Tailscale network
check_connection() {
    echo ""
    echo "Checking Tailscale connection..."
    
    if tailscale status &> /dev/null; then
        echo -e "${GREEN}✓${NC} Connected to Tailscale network"
        
        # Get Tailscale IP
        TS_IP=$(tailscale ip -4 2>/dev/null || echo "unavailable")
        echo "  Tailscale IP: $TS_IP"
        
        return 0
    else
        echo -e "${RED}✗${NC} Not connected to Tailscale network"
        echo "  Connect with: sudo tailscale up"
        return 1
    fi
}

# Check network connectivity
check_network() {
    echo ""
    echo "Checking network connectivity..."
    
    # Try to ping Tailscale coordination server
    if tailscale ping --c 1 --until-direct=false 100.100.100.100 &> /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} Can reach Tailscale coordination server"
        return 0
    else
        echo -e "${YELLOW}?${NC} Cannot verify coordination server connectivity"
        return 0
    fi
}

# Check peer connectivity
check_peers() {
    echo ""
    echo "Checking peer connectivity..."
    
    # Get list of peers
    PEER_COUNT=$(tailscale status --json 2>/dev/null | grep -o '"Online":true' | wc -l || echo 0)
    
    if [ "$PEER_COUNT" -gt 0 ]; then
        echo -e "${GREEN}✓${NC} Connected to $PEER_COUNT peer(s)"
        echo ""
        echo "Peer details:"
        tailscale status | head -20
    else
        echo -e "${YELLOW}!${NC} No peers connected"
        echo "  This is normal if you're the first device on the network"
    fi
}

# Check DNS configuration
check_dns() {
    echo ""
    echo "Checking DNS configuration..."
    
    if tailscale status --json 2>/dev/null | grep -q '"MagicDNS":true'; then
        echo -e "${GREEN}✓${NC} MagicDNS is enabled"
    else
        echo -e "${YELLOW}!${NC} MagicDNS is not enabled"
        echo "  Enable at: https://login.tailscale.com/admin/dns"
    fi
}

# Check subnet routes
check_routes() {
    echo ""
    echo "Checking subnet routes..."
    
    ROUTES=$(tailscale status --json 2>/dev/null | grep -o '"AdvertisedRoutes":\[[^]]*\]' || echo "")
    
    if [ -n "$ROUTES" ] && [ "$ROUTES" != '"AdvertisedRoutes":[]' ]; then
        echo -e "${GREEN}✓${NC} Subnet routes are advertised"
    else
        echo -e "${YELLOW}!${NC} No subnet routes advertised"
        echo "  Configure with: sudo tailscale up --advertise-routes=192.0.2.0/24"
    fi
}

# Check for updates
check_updates() {
    echo ""
    echo "Checking for updates..."
    
    CURRENT_VERSION=$(tailscale version | head -1 | awk '{print $1}')
    echo "  Current version: $CURRENT_VERSION"
    echo "  Check for updates at: https://tailscale.com/changelog"
}

# Performance test
check_performance() {
    echo ""
    echo "Checking performance..."
    
    # Run netcheck
    echo "Running network diagnostics..."
    tailscale netcheck 2>/dev/null | head -15 || echo "  Network diagnostics unavailable"
}

# Generate summary
generate_summary() {
    echo ""
    echo "=== Health Check Summary ==="
    echo ""
    
    ISSUES=0
    
    if ! check_installed &>/dev/null; then ((ISSUES++)); fi
    if ! check_service &>/dev/null; then ((ISSUES++)); fi
    if ! check_connection &>/dev/null; then ((ISSUES++)); fi
    
    if [ $ISSUES -eq 0 ]; then
        echo -e "${GREEN}✓ All critical checks passed${NC}"
    else
        echo -e "${RED}✗ $ISSUES critical issue(s) found${NC}"
    fi
    
    echo ""
    echo "For detailed configuration, see: CODE_MASTER/TAILSCALE_SETUP.md"
    echo "Admin console: https://login.tailscale.com/admin"
}

# Main execution
main() {
    FAILED=0
    
    check_installed || FAILED=1
    check_service || FAILED=1
    check_connection || FAILED=1
    
    if [ $FAILED -eq 0 ]; then
        check_network
        check_peers
        check_dns
        check_routes
        check_updates
        check_performance
    fi
    
    generate_summary
    
    return $FAILED
}

main
