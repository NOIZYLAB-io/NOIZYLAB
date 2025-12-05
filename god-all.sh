#!/bin/bash
# GOD-ALL: Complete System Overview in One Command
# CB_01 - Fish Music Inc
# GORUNFREE! 🎸🔥

# Colors
G='\033[0;32m'
Y='\033[1;33m'
C='\033[0;36m'
M='\033[0;35m'
B='\033[1m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

clear
echo ""
echo -e "${B}${M}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${B}${M}║         🔥 GOD COMPLETE SYSTEM OVERVIEW 🔥                   ║${NC}"
echo -e "${B}${M}║         Mac Studio M2 Ultra 192GB                            ║${NC}"
echo -e "${B}${M}║         Fish Music Inc - CB_01                               ║${NC}"
echo -e "${B}${M}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Quick stats
echo -e "${B}${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${B}${Y}⚡ QUICK STATUS${NC}"
echo -e "${B}${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# CPU
CPU_BRAND=$(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "Unknown")
CPU_CORES=$(sysctl -n hw.logicalcpu)
LOAD=$(sysctl -n vm.loadavg | tr -d '{}' | awk '{print $1}')
echo -e "${G}CPU:${NC} $CPU_BRAND"
echo -e "${G}Cores:${NC} $CPU_CORES | ${G}Load:${NC} $LOAD"
echo ""

# Memory
TOTAL_RAM=$(($(sysctl -n hw.memsize) / 1024 / 1024 / 1024))
echo -e "${G}RAM:${NC} ${TOTAL_RAM}GB total"

# Get memory usage
MEM_USED=$(vm_stat | awk '/Pages active/ {active=$3} /Pages wired/ {wired=$4} END {printf "%.0f", (active+wired)*4096/1024/1024/1024}' | tr -d '.')
echo -e "${G}Memory Used:${NC} ~${MEM_USED}GB"
echo ""

# Disk
DISK_INFO=$(df -h / | tail -1)
DISK_USED=$(echo $DISK_INFO | awk '{print $3}')
DISK_AVAIL=$(echo $DISK_INFO | awk '{print $4}')
DISK_PCT=$(echo $DISK_INFO | awk '{print $5}')
echo -e "${G}Disk:${NC} $DISK_USED used / $DISK_AVAIL available ($DISK_PCT)"
echo ""

# Network
DNS=$(networksetup -getdnsservers "Wi-Fi" 2>/dev/null | head -1)
if [[ "$DNS" == "1.1.1.1" ]]; then
    echo -e "${G}DNS:${NC} ✅ Cloudflare Optimized"
else
    echo -e "${Y}DNS:${NC} $DNS"
fi
echo ""

# Uptime
echo -e "${G}Uptime:${NC} $(uptime | awk -F'up ' '{print $2}' | awk -F',' '{print $1}')"
echo ""

echo -e "${B}${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${B}${Y}🛠️  AVAILABLE TOOLS${NC}"
echo -e "${B}${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${C}OPTIMIZATION:${NC}"
echo -e "  ${G}god-boost-now.sh${NC}    10-sec emergency optimization"
echo -e "  ${G}god-quick.sh${NC}        30-sec daily boost"
echo -e "  ${G}god-hotrod.sh${NC}       15-min deep optimization"
echo -e "  ${G}god-cleanup.sh${NC}      Smart space recovery (interactive)"
echo ""
echo -e "${C}MONITORING:${NC}"
echo -e "  ${G}god-status.py${NC}       Full performance snapshot"
echo -e "  ${G}god-status.py -c${NC}    Continuous monitoring"
echo -e "  ${G}god-health.py${NC}       Health check with alerts"
echo -e "  ${G}god-health.py -d${NC}    Daemon mode (background logging)"
echo ""
echo -e "${C}DIAGNOSTICS:${NC}"
echo -e "  ${G}god-network.sh${NC}      Network diagnostics"
echo -e "  ${G}god-find-large.sh${NC}   Find large files"
echo -e "  ${G}god-voice-test.sh${NC}   Audio/voice testing"
echo ""

echo -e "${B}${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${B}${Y}⚡ QUICK COMMANDS${NC}"
echo -e "${B}${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${M}Emergency Boost:${NC}  cd $SCRIPT_DIR && ./god-boost-now.sh"
echo -e "${M}Full Status:${NC}      cd $SCRIPT_DIR && python3 god-status.py"
echo -e "${M}Live Monitor:${NC}     cd $SCRIPT_DIR && python3 god-status.py -c"
echo -e "${M}Network Check:${NC}    cd $SCRIPT_DIR && ./god-network.sh"
echo -e "${M}Find Big Files:${NC}   cd $SCRIPT_DIR && ./god-find-large.sh ~"
echo ""

echo -e "${B}${M}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${B}${M}║                    GORUNFREE! 🎸🔥                            ║${NC}"
echo -e "${B}${M}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""
