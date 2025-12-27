#!/bin/bash
# Monitoring script for Tailscale infrastructure
# Run this script periodically via cron to monitor Tailscale health

set -e

# Configuration
ALERT_EMAIL="${ALERT_EMAIL:-admin@noizylab.com}"
ALERT_WEBHOOK="${ALERT_WEBHOOK:-}"
LOG_FILE="${LOG_FILE:-/tmp/noizylab-tailscale-monitor.log}"
STATE_FILE="/tmp/noizylab-tailscale-state"

# Metrics
METRICS_FILE="/tmp/tailscale-metrics.json"

# Function to log with timestamp
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE" 2>/dev/null || echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Function to send alert
send_alert() {
    local severity="$1"
    local message="$2"
    
    log "ALERT [$severity]: $message"
    
    # Send email if configured
    if command -v mail &> /dev/null && [ -n "$ALERT_EMAIL" ]; then
        echo "$message" | mail -s "Tailscale Alert [$severity]" "$ALERT_EMAIL"
    fi
    
    # Send webhook if configured
    if [ -n "$ALERT_WEBHOOK" ]; then
        curl -X POST "$ALERT_WEBHOOK" \
            --max-time 10 --retry 2 \
            -H "Content-Type: application/json" \
            -d "{\"severity\":\"$severity\",\"message\":\"$message\",\"timestamp\":\"$(date -Iseconds)\"}" \
            &> /dev/null || true
    fi
}

# Get peer count
get_peer_count() {
    tailscale status 2>/dev/null | grep -v "^#" | tail -n +2 | wc -l || echo 0
}


# Check if Tailscale is installed
check_installed() {
    if ! command -v tailscale &> /dev/null; then
        send_alert "CRITICAL" "Tailscale is not installed"
        return 1
    fi
    return 0
}

# Check if Tailscale is running
check_running() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if ! pgrep -x "Tailscale" > /dev/null; then
            send_alert "CRITICAL" "Tailscale service is not running on macOS"
            return 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if ! systemctl is-active --quiet tailscaled; then
            send_alert "CRITICAL" "Tailscale service is not running on Linux"
            return 1
        fi
    fi
    return 0
}

# Check if connected to Tailscale network
check_connected() {
    if ! tailscale status &> /dev/null; then
        send_alert "CRITICAL" "Not connected to Tailscale network"
        return 1
    fi
    return 0
}

# Check peer connectivity
check_peers() {
    local peer_count=$(get_peer_count)
    
    # Store previous peer count
    local prev_peer_count=0
    if [ -f "$STATE_FILE" ]; then
        prev_peer_count=$(jq -r '.peer_count // 0' "$STATE_FILE" 2>/dev/null || echo 0)
    fi
    
    # Alert if all peers disconnected
    if [ "$prev_peer_count" -gt 0 ] && [ "$peer_count" -eq 0 ]; then
        send_alert "WARNING" "All Tailscale peers disconnected (was $prev_peer_count, now 0)"
    fi
    
    # Alert if peer count dropped significantly
    if [ "$prev_peer_count" -gt 5 ] && [ "$peer_count" -lt $((prev_peer_count / 2)) ]; then
        send_alert "WARNING" "Peer count dropped significantly (was $prev_peer_count, now $peer_count)"
    fi
    
    return 0
}

# Check network connectivity
check_network() {
    if ! tailscale netcheck &> /dev/null 2>&1; then
        send_alert "WARNING" "Tailscale network check failed"
        return 1
    fi
    return 0
}

# Collect metrics
collect_metrics() {
    local status_output=$(tailscale status 2>/dev/null || echo "")
    local ip=$(tailscale ip -4 2>/dev/null || echo "unknown")
    local peer_count=$(get_peer_count)
    
    # Create metrics JSON
    cat > "$METRICS_FILE" <<EOF
{
  "timestamp": "$(date -Iseconds)",
  "status": "$(tailscale status &> /dev/null && echo "connected" || echo "disconnected")",
  "ip": "$ip",
  "peer_count": $peer_count,
  "version": "$(tailscale version 2>/dev/null | head -1 || echo "unknown")"
}
EOF
    
    log "Metrics collected: IP=$ip, Peers=$peer_count"
}

# Update state
update_state() {
    local peer_count=$(get_peer_count)
    
    cat > "$STATE_FILE" <<EOF
{
  "timestamp": "$(date -Iseconds)",
  "peer_count": $peer_count,
  "last_check": "$(date +'%Y-%m-%d %H:%M:%S')"
}
EOF
}

# Generate status report
generate_report() {
    echo ""
    echo "=== Tailscale Monitoring Report ==="
    echo "Time: $(date)"
    echo ""
    
    if check_installed && check_running && check_connected; then
        echo "Status: ✓ Healthy"
        tailscale status | head -10
    else
        echo "Status: ✗ Issues detected"
    fi
    
    echo ""
    echo "Metrics file: $METRICS_FILE"
    echo "Log file: $LOG_FILE"
    echo ""
}

# Main monitoring function
main() {
    log "Starting Tailscale monitoring check"
    
    # Run all checks
    local all_ok=true
    
    check_installed || all_ok=false
    check_running || all_ok=false
    check_connected || all_ok=false
    check_peers || all_ok=false
    check_network || all_ok=false
    
    # Collect metrics if connected
    if check_connected; then
        collect_metrics
    fi
    
    # Update state
    update_state
    
    # Generate report if verbose
    if [ "${VERBOSE:-0}" -eq 1 ]; then
        generate_report
    fi
    
    if [ "$all_ok" = true ]; then
        log "All checks passed"
        return 0
    else
        log "Some checks failed"
        return 1
    fi
}

# Run main function
main "$@"
