#!/usr/bin/env bash
#═══════════════════════════════════════════════════════════════════════════════
#  NOIZYDIGGER - NOIZYHIVE Cloudflare Tunnel Manager
#  Zero Latency. Maximum Power. god.noizy.ai
#  "We Dig Deep Into The Cloud"
#═══════════════════════════════════════════════════════════════════════════════
set -eo pipefail

VERSION="2.0.0"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Configuration
TUNNEL_NAME="${TUNNEL_NAME:-god}"
DOMAIN="${DOMAIN:-god.noizy.ai}"
LOCAL_PORT="${LOCAL_PORT:-8080}"
API_PORT="${API_PORT:-8081}"
CLOUDFLARED_DIR="$HOME/.cloudflared"
CONFIG_FILE="$CLOUDFLARED_DIR/config.yml"
CREDENTIALS_FILE="$CLOUDFLARED_DIR/${TUNNEL_NAME}.json"
LOG_DIR="$HOME/noizyhive/god/logs"
LOG_FILE="$LOG_DIR/noizydigger.log"
PID_FILE="$LOG_DIR/noizydigger.pid"
API_PID_FILE="$LOG_DIR/api.pid"
TOKEN_FILE="$CLOUDFLARED_DIR/.tunnel_token"
PLIST_NAME="ai.noizy.god-tunnel"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
METRICS_FILE="$LOG_DIR/metrics.json"

# Performance tuning
CONNECT_TIMEOUT=5
HEALTH_INTERVAL=30
MAX_RETRIES=3

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Create directories
mkdir -p "$CLOUDFLARED_DIR" "$LOG_DIR"

log() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $*"
    echo -e "$msg" | tee -a "$LOG_FILE"
}

log_metric() {
    local event="$1"
    local value="$2"
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    echo "{\"ts\":\"$timestamp\",\"event\":\"$event\",\"value\":\"$value\"}" >> "$METRICS_FILE"
}

fast_check() {
    # Ultra-fast connectivity check
    curl -s --connect-timeout 1 --max-time 2 "$1" &>/dev/null
}

print_banner() {
    echo -e "${CYAN}"
    cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════╗
║   ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██████╗ ██╗ ██████╗  ██████╗ ███████╗██████╗  ║
║   ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██╔══██╗██║██╔════╝ ██╔════╝ ██╔════╝██╔══██╗ ║
║   ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║  ██║██║██║  ███╗██║  ███╗█████╗  ██████╔╝ ║
║   ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║  ██║██║██║   ██║██║   ██║██╔══╝  ██╔══██╗ ║
║   ██║ ╚████║╚██████╔╝██║███████╗   ██║   ██████╔╝██║╚██████╔╝╚██████╔╝███████╗██║  ██║ ║
║   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ║
║                                                                                        ║
║                    "WE DIG DEEP INTO THE CLOUD"                                        ║
║                    NOIZYHIVE CLOUDFLARE TUNNEL v1.0                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

#───────────────────────────────────────────────────────────────────────────────
# SETUP COMMANDS
#───────────────────────────────────────────────────────────────────────────────

cmd_setup() {
    print_banner
    log "${WHITE}Setting up GOD tunnel...${NC}"

    # Check cloudflared
    if ! command -v cloudflared &>/dev/null; then
        log "${RED}cloudflared not installed. Installing...${NC}"
        brew install cloudflare/cloudflare/cloudflared
    fi

    log "${GREEN}cloudflared version: $(cloudflared --version)${NC}"

    # Login if needed
    if [[ ! -f "$HOME/.cloudflared/cert.pem" ]]; then
        log "${YELLOW}Logging into Cloudflare...${NC}"
        cloudflared tunnel login
    fi

    log "${GREEN}Setup complete!${NC}"
}

cmd_tunnel_install() {
    log "${WHITE}Installing cloudflared...${NC}"
    if command -v brew &>/dev/null; then
        brew install cloudflare/cloudflare/cloudflared
    else
        log "${RED}Homebrew not found. Install manually.${NC}"
        exit 1
    fi
    log "${GREEN}cloudflared installed: $(cloudflared --version)${NC}"
}

cmd_tunnel_login() {
    log "${WHITE}Logging into Cloudflare...${NC}"
    cloudflared tunnel login
    log "${GREEN}Login successful!${NC}"
}

cmd_tunnel_create() {
    log "${WHITE}Creating tunnel: ${TUNNEL_NAME}${NC}"

    # Check if tunnel exists
    if cloudflared tunnel list | grep -q "$TUNNEL_NAME"; then
        log "${YELLOW}Tunnel '$TUNNEL_NAME' already exists${NC}"
        return 0
    fi

    cloudflared tunnel create "$TUNNEL_NAME"
    log "${GREEN}Tunnel '$TUNNEL_NAME' created!${NC}"

    # Get tunnel ID
    TUNNEL_ID=$(cloudflared tunnel list | grep "$TUNNEL_NAME" | awk '{print $1}')
    log "Tunnel ID: $TUNNEL_ID"
}

cmd_tunnel_config() {
    log "${WHITE}Configuring tunnel...${NC}"

    # Get tunnel ID
    TUNNEL_ID=$(cloudflared tunnel list | grep "$TUNNEL_NAME" | awk '{print $1}')

    if [[ -z "$TUNNEL_ID" ]]; then
        log "${RED}Tunnel not found. Create it first with: ./god.sh tunnel-create${NC}"
        exit 1
    fi

    # Find credentials file
    CREDS_FILE=$(find "$CLOUDFLARED_DIR" -name "*.json" | head -1)

    if [[ -z "$CREDS_FILE" ]]; then
        log "${RED}Credentials file not found${NC}"
        exit 1
    fi

    # Create config
    cat > "$CONFIG_FILE" << EOF
tunnel: $TUNNEL_ID
credentials-file: $CREDS_FILE

ingress:
  - hostname: $DOMAIN
    service: http://localhost:$LOCAL_PORT
  - hostname: api.noizy.ai
    service: http://localhost:$LOCAL_PORT
  - service: http_status:404
EOF

    log "${GREEN}Config written to $CONFIG_FILE${NC}"
    cat "$CONFIG_FILE"
}

cmd_tunnel_route() {
    log "${WHITE}Routing DNS for $DOMAIN...${NC}"

    TUNNEL_ID=$(cloudflared tunnel list | grep "$TUNNEL_NAME" | awk '{print $1}')

    cloudflared tunnel route dns "$TUNNEL_ID" "$DOMAIN" || {
        log "${YELLOW}DNS route may already exist${NC}"
    }

    # Also route api.noizy.ai if needed
    cloudflared tunnel route dns "$TUNNEL_ID" "api.noizy.ai" 2>/dev/null || true

    log "${GREEN}DNS routing configured!${NC}"
}

#───────────────────────────────────────────────────────────────────────────────
# RUN COMMANDS
#───────────────────────────────────────────────────────────────────────────────

cmd_start() {
    log "${WHITE}Starting NOIZYDIGGER API Server v2.0...${NC}"

    # Kill existing
    pkill -f "python.*api_server.py" 2>/dev/null || true
    pkill -f "python.*$LOCAL_PORT" 2>/dev/null || true
    sleep 1

    # Start high-performance API server
    cd "$SCRIPT_DIR"

    export API_PORT="$LOCAL_PORT"
    export DOMAIN="$DOMAIN"

    python3 "$SCRIPT_DIR/api_server.py" >> "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"

    sleep 2

    # Verify startup
    if kill -0 $(cat "$PID_FILE" 2>/dev/null) 2>/dev/null; then
        log "${GREEN}API Server started on port $LOCAL_PORT (PID: $(cat $PID_FILE))${NC}"
        log "${GREEN}Dashboard: http://localhost:$LOCAL_PORT${NC}"
        log_metric "server_start" "success"
    else
        log "${RED}Server failed to start${NC}"
        log_metric "server_start" "failed"
    fi
}

cmd_tunnel_start() {
    log "${WHITE}Starting Cloudflare tunnel...${NC}"

    if [[ ! -f "$CONFIG_FILE" ]]; then
        log "${RED}Config not found. Run: ./god.sh tunnel-config${NC}"
        exit 1
    fi

    # Kill existing tunnel
    pkill -f "cloudflared tunnel run" 2>/dev/null || true
    sleep 1

    # Start tunnel
    cloudflared tunnel run "$TUNNEL_NAME" >> "$LOG_FILE" 2>&1 &
    local pid=$!

    sleep 3

    if kill -0 $pid 2>/dev/null; then
        log "${GREEN}Tunnel running (PID: $pid)${NC}"
        log "${GREEN}Access at: https://$DOMAIN${NC}"
    else
        log "${RED}Tunnel failed to start. Check logs.${NC}"
        tail -20 "$LOG_FILE"
    fi
}

cmd_stop() {
    log "${WHITE}Stopping services...${NC}"

    # Stop tunnel
    pkill -f "cloudflared tunnel run" 2>/dev/null && log "Tunnel stopped" || true

    # Stop server
    if [[ -f "$PID_FILE" ]]; then
        kill $(cat "$PID_FILE") 2>/dev/null && log "Server stopped" || true
        rm -f "$PID_FILE"
    fi

    pkill -f "python.*$LOCAL_PORT" 2>/dev/null || true

    log "${GREEN}All services stopped${NC}"
}

cmd_restart() {
    cmd_stop
    sleep 2
    cmd_start
    cmd_tunnel_start
}

#───────────────────────────────────────────────────────────────────────────────
# STATUS & MONITORING
#───────────────────────────────────────────────────────────────────────────────

cmd_status() {
    print_banner

    echo -e "${WHITE}SERVICE STATUS${NC}"
    echo "─────────────────────────────────────────────────────────────────"

    # Tunnel status
    if pgrep -f "cloudflared tunnel run" &>/dev/null; then
        echo -e "  ${GREEN}●${NC} Cloudflare Tunnel: RUNNING"
    else
        echo -e "  ${RED}○${NC} Cloudflare Tunnel: STOPPED"
    fi

    # Server status
    if pgrep -f "python.*$LOCAL_PORT" &>/dev/null; then
        echo -e "  ${GREEN}●${NC} Local Server (:$LOCAL_PORT): RUNNING"
    else
        echo -e "  ${RED}○${NC} Local Server (:$LOCAL_PORT): STOPPED"
    fi

    # DNS check
    echo
    echo -e "${WHITE}DNS STATUS${NC}"
    echo "─────────────────────────────────────────────────────────────────"
    local dns_result=$(dig +short "$DOMAIN" 2>/dev/null)
    if [[ -n "$dns_result" ]]; then
        echo -e "  ${GREEN}●${NC} $DOMAIN → $dns_result"
    else
        echo -e "  ${RED}○${NC} $DOMAIN → NOT RESOLVING"
    fi

    # Connectivity check
    echo
    echo -e "${WHITE}CONNECTIVITY${NC}"
    echo "─────────────────────────────────────────────────────────────────"
    if curl -s --max-time 5 "http://localhost:$LOCAL_PORT" &>/dev/null; then
        echo -e "  ${GREEN}●${NC} localhost:$LOCAL_PORT → ACCESSIBLE"
    else
        echo -e "  ${RED}○${NC} localhost:$LOCAL_PORT → NOT ACCESSIBLE"
    fi

    if curl -s --max-time 10 "https://$DOMAIN" &>/dev/null; then
        echo -e "  ${GREEN}●${NC} https://$DOMAIN → ACCESSIBLE"
    else
        echo -e "  ${YELLOW}○${NC} https://$DOMAIN → NOT YET ACCESSIBLE"
    fi

    echo
}

cmd_logs() {
    echo -e "${WHITE}Showing last 50 lines of logs...${NC}"
    tail -50 "$LOG_FILE" 2>/dev/null || echo "No logs yet"
}

cmd_logs_follow() {
    echo -e "${WHITE}Following logs... (Ctrl+C to stop)${NC}"
    tail -f "$LOG_FILE"
}

#───────────────────────────────────────────────────────────────────────────────
# LAUNCHD SERVICE
#───────────────────────────────────────────────────────────────────────────────

cmd_launchd_install() {
    log "${WHITE}Installing launchd service...${NC}"

    cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$PLIST_NAME</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>$SCRIPT_DIR/god.sh</string>
        <string>run-all</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>$LOG_FILE</string>
    <key>StandardErrorPath</key>
    <string>$LOG_FILE</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
    </dict>
</dict>
</plist>
EOF

    launchctl unload "$PLIST_PATH" 2>/dev/null || true
    launchctl load "$PLIST_PATH"

    log "${GREEN}Service installed and started!${NC}"
    log "Check with: launchctl list | grep noizyhive"
}

cmd_launchd_uninstall() {
    log "${WHITE}Removing launchd service...${NC}"
    launchctl unload "$PLIST_PATH" 2>/dev/null || true
    rm -f "$PLIST_PATH"
    log "${GREEN}Service removed${NC}"
}

cmd_run_all() {
    # Used by launchd - runs everything
    cmd_start
    sleep 2
    cmd_tunnel_start

    # Keep alive
    while true; do
        sleep 60

        # Check and restart if needed
        if ! pgrep -f "cloudflared tunnel run" &>/dev/null; then
            log "${YELLOW}Tunnel died, restarting...${NC}"
            cmd_tunnel_start
        fi

        if ! pgrep -f "python.*$LOCAL_PORT" &>/dev/null; then
            log "${YELLOW}Server died, restarting...${NC}"
            cmd_start
        fi
    done
}

#───────────────────────────────────────────────────────────────────────────────
# QUICK CONNECT (Zero Trust Token Method)
#───────────────────────────────────────────────────────────────────────────────

cmd_quick_connect() {
    local token="$1"

    if [[ -z "$token" ]]; then
        print_banner
        echo -e "${WHITE}QUICK CONNECT - Cloudflare Zero Trust${NC}"
        echo "─────────────────────────────────────────────────────────────────"
        echo ""
        echo "To connect using the Cloudflare Dashboard:"
        echo ""
        echo "  1. Go to: https://one.dash.cloudflare.com → Networks → Tunnels"
        echo "  2. Click 'Create a tunnel'"
        echo "  3. Select 'Cloudflared' connector"
        echo "  4. Name your tunnel (e.g., 'god')"
        echo "  5. Copy the connector token"
        echo "  6. Run: ${CYAN}noizydigger quick-connect <YOUR_TOKEN>${NC}"
        echo ""
        echo "Or use the legacy method:"
        echo "  ${CYAN}noizydigger tunnel-login${NC}"
        echo ""
        return 1
    fi

    log "${WHITE}Connecting with Zero Trust token...${NC}"

    # Start local server first
    cmd_start

    sleep 2

    # Run tunnel with token
    log "${WHITE}Starting Cloudflare tunnel with connector token...${NC}"
    pkill -f "cloudflared tunnel run" 2>/dev/null || true
    sleep 1

    cloudflared tunnel run --token "$token" >> "$LOG_FILE" 2>&1 &
    local pid=$!

    sleep 5

    if kill -0 $pid 2>/dev/null; then
        log "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        log "${GREEN}TUNNEL CONNECTED!${NC}"
        log "${GREEN}PID: $pid${NC}"
        log "${GREEN}Configure your public hostname in Cloudflare Dashboard${NC}"
        log "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    else
        log "${RED}Tunnel failed to start. Check logs:${NC}"
        tail -20 "$LOG_FILE"
    fi
}

#───────────────────────────────────────────────────────────────────────────────
# HEALTH CHECK API
#───────────────────────────────────────────────────────────────────────────────

cmd_health() {
    local status="healthy"
    local tunnel_ok=false
    local server_ok=false

    pgrep -f "cloudflared tunnel run" &>/dev/null && tunnel_ok=true
    pgrep -f "python.*$LOCAL_PORT" &>/dev/null && server_ok=true

    if ! $tunnel_ok || ! $server_ok; then
        status="degraded"
    fi

    cat << EOF
{
  "status": "$status",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "node": "GOD",
  "services": {
    "tunnel": $tunnel_ok,
    "server": $server_ok
  },
  "domain": "$DOMAIN",
  "port": $LOCAL_PORT
}
EOF
}

#───────────────────────────────────────────────────────────────────────────────
# HELP
#───────────────────────────────────────────────────────────────────────────────

cmd_help() {
    print_banner
    cat << EOF
${WHITE}COMMANDS${NC}
─────────────────────────────────────────────────────────────────

${CYAN}SETUP${NC}
  setup              Full initial setup
  tunnel-install     Install cloudflared
  tunnel-login       Login to Cloudflare
  tunnel-create      Create tunnel
  tunnel-config      Generate config
  tunnel-route       Setup DNS routing

${CYAN}RUNNING${NC}
  start              Start local server
  tunnel-start       Start tunnel
  stop               Stop all services
  restart            Restart all services
  run-all            Run everything (for launchd)

${CYAN}MONITORING${NC}
  status             Show service status
  logs               Show recent logs
  logs-follow        Follow logs live
  health             JSON health check

${CYAN}LAUNCHD${NC}
  launchd-install    Install auto-start service
  launchd-uninstall  Remove auto-start service

${CYAN}QUICK START${NC}
  ./god.sh setup
  ./god.sh tunnel-create
  ./god.sh tunnel-config
  ./god.sh tunnel-route
  ./god.sh start
  ./god.sh tunnel-start
  ./god.sh status

EOF
}

#───────────────────────────────────────────────────────────────────────────────
# MAIN
#───────────────────────────────────────────────────────────────────────────────

main() {
    local cmd="${1:-help}"

    case "$cmd" in
        setup)              cmd_setup ;;
        tunnel-install)     cmd_tunnel_install ;;
        tunnel-login)       cmd_tunnel_login ;;
        tunnel-create)      cmd_tunnel_create ;;
        tunnel-config)      cmd_tunnel_config ;;
        tunnel-route)       cmd_tunnel_route ;;
        start)              cmd_start ;;
        tunnel-start)       cmd_tunnel_start ;;
        stop)               cmd_stop ;;
        restart)            cmd_restart ;;
        run-all)            cmd_run_all ;;
        status)             cmd_status ;;
        logs)               cmd_logs ;;
        logs-follow)        cmd_logs_follow ;;
        health)             cmd_health ;;
        launchd-install)    cmd_launchd_install ;;
        launchd-uninstall)  cmd_launchd_uninstall ;;
        quick-connect|qc)   cmd_quick_connect "$2" ;;
        help|-h|--help)     cmd_help ;;
        *)
            echo "Unknown command: $cmd"
            cmd_help
            exit 1
            ;;
    esac
}

main "$@"
