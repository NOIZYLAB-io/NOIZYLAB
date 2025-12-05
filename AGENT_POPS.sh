#!/bin/bash
# AGENT_POPS.sh
# System Health & Wisdom Agent for macOS
# GORUNFREEX5000

LOG_DIR="$HOME/Library/Logs/MC96_Agents"
LOG_FILE="$LOG_DIR/POPS_$(date +%Y%m%d).log"

mkdir -p "$LOG_DIR"

log() {
    echo "[$(date '+%H:%M:%S')] [POPS] $1" | tee -a "$LOG_FILE"
}

log "🔧 POPS starting - System Health & Elder Wisdom"

# MC96ECOUNIVERSE devices
DEVICES=("10.90.90.90" "10.90.90.10" "10.90.90.20" "10.90.90.30" "10.90.90.15")
DEVICE_NAMES=("MC96 Switch" "GOD (Mac Studio)" "GABRIEL (HP Omen)" "MIKE (MacPro)" "DaFixer (MacBook Pro)")

while true; do
    log "🔧 Checking MC96ECOUNIVERSE network health..."
    
    # Network monitoring
    for i in "${!DEVICES[@]}"; do
        IP="${DEVICES[$i]}"
        NAME="${DEVICE_NAMES[$i]}"
        
        if ping -c 1 -W 1 "$IP" >/dev/null 2>&1; then
            log "  ✓ $NAME ($IP) online"
        else
            log "  ✗ $NAME ($IP) OFFLINE!"
        fi
    done
    
    # System health on GOD
    CPU=$(top -l 1 | grep "CPU usage" | awk '{print $3}' | sed 's/%//')
    MEMORY=$(vm_stat | perl -ne '/page size of (\d+)/ and $size=$1; /Pages active:\s+(\d+)/ and printf("%.1f", $1 * $size / 1073741824);')
    log "  CPU: ${CPU}% | RAM: ${MEMORY}GB active"
    
    # Disk health - THE_AQUARIUM protection
    DISK_FREE=$(df -h / | tail -1 | awk '{print $4}')
    log "  Disk free: $DISK_FREE"
    
    # Wisdom check
    HOUR=$(date +%H)
    if [ "$HOUR" -ge 23 ] || [ "$HOUR" -le 5 ]; then
        log "🔧 Elder wisdom: Late night detected - consider rest, Rob"
    fi
    
    log "🔧 Health check complete - next in 3 min"
    sleep 180
done
