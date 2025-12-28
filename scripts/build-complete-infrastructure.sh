#!/bin/bash
# NOIZYLAB Complete Tailscale Infrastructure Setup
# This master script orchestrates the entire Tailscale deployment for NOIZYLAB

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
LOG_FILE="/tmp/noizylab-tailscale-setup-$(date +%Y%m%d-%H%M%S).log"

# Function to log messages
log() {
    echo -e "${CYAN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}✗${NC} $1" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}!${NC} $1" | tee -a "$LOG_FILE"
}

log_info() {
    echo -e "${BLUE}ℹ${NC} $1" | tee -a "$LOG_FILE"
}

# Banner
show_banner() {
    echo -e "${MAGENTA}"
    cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗ ║
║   ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗║
║   ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝║
║   ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗║
║   ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝║
║   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ ║
║                                                           ║
║         Complete Tailscale Infrastructure Setup          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# Check prerequisites
check_prerequisites() {
    log "Checking prerequisites..."
    
    local missing_deps=()
    
    # Check for required commands
    if ! command -v curl &> /dev/null; then
        missing_deps+=("curl")
    fi
    
    if [ ${#missing_deps[@]} -gt 0 ]; then
        log_error "Missing required dependencies: ${missing_deps[*]}"
        log_info "Install missing dependencies and try again"
        return 1
    fi
    
    log_success "All prerequisites met"
    return 0
}

# Step 1: Install Tailscale
install_tailscale() {
    echo ""
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    log "${MAGENTA}Step 1/5: Installing Tailscale${NC}"
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Detect platform
    if [[ "$OSTYPE" == "darwin"* ]]; then
        log "Detected macOS platform"
        if [ -f "$SCRIPT_DIR/setup-tailscale-macos.sh" ]; then
            bash "$SCRIPT_DIR/setup-tailscale-macos.sh" 2>&1 | tee -a "$LOG_FILE"
        else
            log_error "macOS setup script not found"
            return 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        log "Detected Linux platform"
        if [ -f "$SCRIPT_DIR/setup-tailscale-linux.sh" ]; then
            bash "$SCRIPT_DIR/setup-tailscale-linux.sh" 2>&1 | tee -a "$LOG_FILE"
        else
            log_error "Linux setup script not found"
            return 1
        fi
    else
        log_error "Unsupported platform: $OSTYPE"
        log_info "For Windows, run: .\\scripts\\setup-tailscale-windows.ps1"
        return 1
    fi
    
    log_success "Tailscale installation complete"
    return 0
}

# Step 2: Wait for authentication
wait_for_authentication() {
    echo ""
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    log "${MAGENTA}Step 2/5: Waiting for Authentication${NC}"
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    echo ""
    
    log_info "Please complete authentication in your browser if prompted"
    log_info "Waiting for Tailscale to connect..."
    
    local retries=0
    local max_retries=30
    
    while [ $retries -lt $max_retries ]; do
        if tailscale status &> /dev/null; then
            log_success "Tailscale connected successfully"
            return 0
        fi
        
        echo -n "."
        sleep 2
        ((retries++))
    done
    
    echo ""
    log_error "Tailscale did not connect within timeout"
    log_info "Run 'sudo tailscale up' manually and try again"
    return 1
}

# Step 3: Configure Tailscale
configure_tailscale() {
    echo ""
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    log "${MAGENTA}Step 3/5: Configuring Tailscale${NC}"
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    echo ""
    
    read -p "$(echo -e ${YELLOW}Would you like to run interactive configuration? \(y/N\): ${NC})" -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if [ -f "$SCRIPT_DIR/configure-tailscale.sh" ]; then
            bash "$SCRIPT_DIR/configure-tailscale.sh" 2>&1 | tee -a "$LOG_FILE"
        else
            log_error "Configuration script not found"
            return 1
        fi
    else
        log_info "Skipping interactive configuration"
        log_info "You can run './scripts/configure-tailscale.sh' later"
    fi
    
    log_success "Configuration step complete"
    return 0
}

# Step 4: Run health check
run_health_check() {
    echo ""
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    log "${MAGENTA}Step 4/5: Running Health Check${NC}"
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    echo ""
    
    if [ -f "$SCRIPT_DIR/healthcheck-tailscale.sh" ]; then
        bash "$SCRIPT_DIR/healthcheck-tailscale.sh" 2>&1 | tee -a "$LOG_FILE"
        local health_status=$?
        
        if [ $health_status -eq 0 ]; then
            log_success "Health check passed"
        else
            log_warning "Health check reported issues"
            log_info "Review the output above for details"
        fi
    else
        log_error "Health check script not found"
        return 1
    fi
    
    return 0
}

# Step 5: Setup ACLs
setup_acls() {
    echo ""
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    log "${MAGENTA}Step 5/5: ACL Configuration${NC}"
    log "${MAGENTA}════════════════════════════════════════════════════════${NC}"
    echo ""
    
    local acl_template="$PROJECT_ROOT/config/tailscale-acl-template.json"
    
    if [ -f "$acl_template" ]; then
        log_info "ACL template available at: $acl_template"
        log_info "To apply ACLs:"
        echo ""
        echo "  1. Review and customize the template:"
        echo "     ${CYAN}cat $acl_template${NC}"
        echo ""
        echo "  2. Apply at Tailscale admin console:"
        echo "     ${CYAN}https://login.tailscale.com/admin/acls${NC}"
        echo ""
        echo "  3. See detailed documentation:"
        echo "     ${CYAN}cat $PROJECT_ROOT/config/README.md${NC}"
        echo ""
        
        log_success "ACL setup information provided"
    else
        log_warning "ACL template not found"
    fi
    
    return 0
}

# Generate summary
generate_summary() {
    echo ""
    log "${GREEN}════════════════════════════════════════════════════════${NC}"
    log "${GREEN}Setup Complete!${NC}"
    log "${GREEN}════════════════════════════════════════════════════════${NC}"
    echo ""
    
    log_success "Tailscale infrastructure setup completed successfully"
    echo ""
    
    echo -e "${CYAN}Next Steps:${NC}"
    echo "  1. Apply ACL configuration at: https://login.tailscale.com/admin/acls"
    echo "  2. Add devices to your Tailscale network"
    echo "  3. Configure MagicDNS for easy hostname access"
    echo "  4. Set up subnet routing if needed"
    echo ""
    
    echo -e "${CYAN}Quick Commands:${NC}"
    echo "  View status:      ${GREEN}tailscale status${NC}"
    echo "  View IP:          ${GREEN}tailscale ip${NC}"
    echo "  Health check:     ${GREEN}./scripts/healthcheck-tailscale.sh${NC}"
    echo "  Configure:        ${GREEN}./scripts/configure-tailscale.sh${NC}"
    echo ""
    
    echo -e "${CYAN}Documentation:${NC}"
    echo "  Setup Guide:      ./CODE_MASTER/TAILSCALE_SETUP.md"
    echo "  Scripts Docs:     ./scripts/README.md"
    echo "  Config Docs:      ./config/README.md"
    echo ""
    
    log_info "Log file saved to: $LOG_FILE"
    echo ""
}

# Main execution
main() {
    show_banner
    
    log "Starting NOIZYLAB Tailscale Infrastructure Setup"
    log "Log file: $LOG_FILE"
    echo ""
    
    # Check prerequisites
    if ! check_prerequisites; then
        log_error "Prerequisites check failed"
        exit 1
    fi
    
    # Step 1: Install
    if ! install_tailscale; then
        log_error "Installation failed"
        exit 1
    fi
    
    # Step 2: Wait for auth
    if ! wait_for_authentication; then
        log_error "Authentication failed"
        exit 1
    fi
    
    # Step 3: Configure
    configure_tailscale
    
    # Step 4: Health check
    run_health_check
    
    # Step 5: ACL setup
    setup_acls
    
    # Generate summary
    generate_summary
    
    log_success "All done! Enjoy your secure Tailscale network!"
}

# Run main function
main "$@"
