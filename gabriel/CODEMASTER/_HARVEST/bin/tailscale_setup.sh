#!/usr/bin/env bash
# ============================================================================
# TAILSCALE VPN SETUP & MANAGEMENT
# ============================================================================
# Comprehensive Tailscale setup for NOIZYLAB infrastructure
# Usage: tailscale_setup.sh [command]
# ============================================================================

set -euo pipefail

VERSION="1.0.0"

# === COLORS ===
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log_info()  { echo -e "${BLUE}ℹ${NC} $1"; }
log_ok()    { echo -e "${GREEN}✅${NC} $1"; }
log_warn()  { echo -e "${YELLOW}⚠️${NC} $1"; }
log_error() { echo -e "${RED}❌${NC} $1"; }
log_step()  { echo -e "${CYAN}▶${NC} $1"; }

show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║              TAILSCALE VPN MANAGER v${VERSION}                   ║"
    echo "║           NOIZYLAB Secure Network Infrastructure             ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# === INSTALLATION ===
cmd_install() {
    show_banner
    log_step "Installing Tailscale..."

    if [[ "$(uname)" == "Darwin" ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            log_info "Installing via Homebrew..."
            brew install tailscale

            log_ok "Tailscale installed!"
            echo ""
            log_info "To start Tailscale:"
            echo "  1. Start the daemon: sudo tailscaled &"
            echo "  2. Authenticate: tailscale up"
            echo ""
            log_info "Or install the Mac App Store version for menu bar integration"
        else
            log_error "Homebrew not found"
            log_info "Install from: https://tailscale.com/download/mac"
            exit 1
        fi
    elif [[ "$(uname)" == "Linux" ]]; then
        # Linux
        log_info "Installing via official script..."
        curl -fsSL https://tailscale.com/install.sh | sh
        log_ok "Tailscale installed!"
    else
        log_error "Unsupported OS: $(uname)"
        exit 1
    fi
}

# === STATUS ===
cmd_status() {
    show_banner

    if ! command -v tailscale &> /dev/null; then
        log_error "Tailscale not installed"
        log_info "Run: $0 install"
        exit 1
    fi

    log_step "Tailscale Status"
    echo ""

    # Check if connected
    if tailscale status &> /dev/null; then
        local status_json=$(tailscale status --json 2>/dev/null)

        local hostname=$(echo "$status_json" | jq -r '.Self.HostName // "unknown"')
        local tailnet=$(echo "$status_json" | jq -r '.MagicDNSSuffix // "unknown"')
        local ipv4=$(tailscale ip -4 2>/dev/null || echo "none")
        local ipv6=$(tailscale ip -6 2>/dev/null || echo "none")
        local online=$(echo "$status_json" | jq -r '.Self.Online // false')

        if [[ "$online" == "true" ]]; then
            log_ok "Connected to Tailnet"
        else
            log_warn "Tailscale daemon running but not online"
        fi

        echo ""
        echo "  Hostname:  $hostname"
        echo "  Tailnet:   $tailnet"
        echo "  IPv4:      $ipv4"
        echo "  IPv6:      $ipv6"
        echo ""

        log_step "Peer Devices"
        echo ""
        tailscale status 2>/dev/null | while read -r line; do
            echo "  $line"
        done
    else
        log_warn "Tailscale not running"
        log_info "Start with: sudo tailscaled & tailscale up"
    fi
}

# === CONNECT ===
cmd_up() {
    show_banner
    log_step "Connecting to Tailscale..."

    # Check if daemon is running
    if ! pgrep -x tailscaled > /dev/null; then
        log_info "Starting Tailscale daemon..."
        sudo tailscaled &
        sleep 2
    fi

    # Additional flags for NOIZYLAB setup
    local flags=""

    # Enable SSH if requested
    if [[ "${1:-}" == "--ssh" ]]; then
        flags="$flags --ssh"
        log_info "Enabling Tailscale SSH"
    fi

    # Enable exit node advertising if requested
    if [[ "${1:-}" == "--exit-node" ]]; then
        flags="$flags --advertise-exit-node"
        log_info "Advertising as exit node"
    fi

    # Connect
    tailscale up $flags

    log_ok "Connected!"
    cmd_status
}

# === DISCONNECT ===
cmd_down() {
    show_banner
    log_step "Disconnecting from Tailscale..."
    tailscale down
    log_ok "Disconnected"
}

# === SHARE FILE ===
cmd_send() {
    local file="$1"
    local target="${2:-}"

    if [[ ! -f "$file" ]]; then
        log_error "File not found: $file"
        exit 1
    fi

    if [[ -z "$target" ]]; then
        log_info "Available peers:"
        tailscale status | grep -v "^#" | awk '{print "  " $2}'
        echo ""
        read -p "Enter target hostname: " target
    fi

    log_step "Sending $file to $target..."
    tailscale file cp "$file" "${target}:"
    log_ok "File sent!"
}

# === RECEIVE FILES ===
cmd_receive() {
    local output_dir="${1:-$HOME/Downloads}"

    log_step "Waiting for incoming files..."
    log_info "Files will be saved to: $output_dir"

    mkdir -p "$output_dir"
    tailscale file get "$output_dir"
}

# === SSH ===
cmd_ssh() {
    local target="$1"

    if [[ -z "$target" ]]; then
        log_info "Available peers:"
        tailscale status | grep -v "^#" | awk '{print "  " $2}'
        echo ""
        read -p "Enter target hostname: " target
    fi

    log_step "Connecting to $target via Tailscale SSH..."
    ssh "$target"
}

# === NETWORK CONFIG ===
cmd_network() {
    show_banner
    log_step "Network Configuration"
    echo ""

    # Current DNS
    log_info "DNS Configuration:"
    tailscale dns status 2>/dev/null || echo "  (not available)"
    echo ""

    # Routes
    log_info "Advertised Routes:"
    tailscale status --json 2>/dev/null | jq -r '.Self.AllowedIPs[]? // "none"' | while read -r ip; do
        echo "  $ip"
    done
    echo ""

    # Exit nodes
    log_info "Available Exit Nodes:"
    tailscale exit-node list 2>/dev/null || echo "  (none available)"
}

# === HELP ===
cmd_help() {
    show_banner
    echo "Commands:"
    echo "  install              Install Tailscale"
    echo "  status               Show connection status"
    echo "  up [--ssh|--exit]    Connect to Tailscale"
    echo "  down                 Disconnect from Tailscale"
    echo "  send <file> [host]   Send file to peer"
    echo "  receive [dir]        Receive incoming files"
    echo "  ssh <host>           SSH to peer via Tailscale"
    echo "  network              Show network configuration"
    echo "  help                 Show this help"
    echo ""
    echo "NOIZYLAB Integration:"
    echo "  Use with MC96 Truth Scanner for secure sync:"
    echo "    mc96_truth_scanner.sh --sync --target <tailscale-host>"
    echo ""
    echo "  Enable file sharing between devices:"
    echo "    tailscale_setup.sh send report.tsv m2ultra-mac"
}

# === MAIN ===
main() {
    local cmd="${1:-status}"
    shift || true

    case "$cmd" in
        install)    cmd_install ;;
        status)     cmd_status ;;
        up)         cmd_up "$@" ;;
        down)       cmd_down ;;
        send)       cmd_send "$@" ;;
        receive)    cmd_receive "$@" ;;
        ssh)        cmd_ssh "$@" ;;
        network)    cmd_network ;;
        help|-h|--help) cmd_help ;;
        *)
            log_error "Unknown command: $cmd"
            cmd_help
            exit 1
            ;;
    esac
}

main "$@"
