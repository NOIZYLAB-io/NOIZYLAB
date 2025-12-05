#!/bin/bash
# MC96ECOUNIVERSE MASTER LAUNCHER
# One command to rule them all!
# Created by CB_01 for ROB - GORUNFREE! 🚀

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# Banner
clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║              🔥 MC96ECOUNIVERSE MASTER LAUNCHER 🔥             ║"
echo "║                                                                ║"
echo "║              Ultimate Network Performance System               ║"
echo "║                     Created by CB_01                           ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Function to show menu
show_menu() {
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}  MC96ECOUNIVERSE COMMAND CENTER${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${GREEN}  [1]${NC} 🚀 Optimize Network (Requires sudo)"
    echo -e "${GREEN}  [2]${NC} 🔍 Scan for MC96 Devices"
    echo -e "${GREEN}  [3]${NC} 🕸️  Build Mesh Network"
    echo -e "${GREEN}  [4]${NC} 📊 Real-Time Monitor"
    echo -e "${GREEN}  [5]${NC} 🔧 Auto-Healing Diagnostics"
    echo -e "${GREEN}  [6]${NC} 📈 Analytics Report"
    echo ""
    echo -e "${CYAN}  [A]${NC} ⚡ AUTO-COMPLETE: Full System Setup (All steps)"
    echo -e "${CYAN}  [Q]${NC} 🏁 Quick Start (Optimize + Scan + Mesh)"
    echo ""
    echo -e "${MAGENTA}  [H]${NC} 📚 Help & Documentation"
    echo -e "${MAGENTA}  [X]${NC} 🚪 Exit"
    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
}

# Function to wait for key
wait_key() {
    echo ""
    echo -e "${YELLOW}Press any key to continue...${NC}"
    read -n 1 -s
}

# Option 1: Optimize Network
optimize_network() {
    echo -e "${YELLOW}🚀 OPTIMIZING NETWORK...${NC}"
    echo ""
    sudo "$SCRIPT_DIR/mc96_optimize.sh"
    wait_key
}

# Option 2: Scan Network
scan_network() {
    echo -e "${YELLOW}🔍 SCANNING FOR MC96 DEVICES...${NC}"
    echo ""
    python3 "$SCRIPT_DIR/mc96_scan.py"
    wait_key
}

# Option 3: Build Mesh
build_mesh() {
    echo -e "${YELLOW}🕸️  BUILDING MESH NETWORK...${NC}"
    echo ""
    python3 "$SCRIPT_DIR/mc96_mesh.py"
    wait_key
}

# Option 4: Monitor
launch_monitor() {
    echo -e "${YELLOW}📊 LAUNCHING REAL-TIME MONITOR...${NC}"
    echo ""
    echo -e "${CYAN}Press Ctrl+C to exit monitor${NC}"
    sleep 2
    python3 "$SCRIPT_DIR/mc96_monitor.py"
}

# Option 5: Auto-Heal
run_autoheal() {
    echo -e "${YELLOW}🔧 RUNNING AUTO-HEALING DIAGNOSTICS...${NC}"
    echo ""
    python3 "$SCRIPT_DIR/mc96_autoheal.py"
    wait_key
}

# Option 6: Analytics
run_analytics() {
    echo -e "${YELLOW}📈 GENERATING ANALYTICS REPORT...${NC}"
    echo ""
    python3 "$SCRIPT_DIR/mc96_analytics.py"
    wait_key
}

# Option A: Auto-Complete
auto_complete() {
    echo -e "${CYAN}⚡ AUTO-COMPLETE: Full System Setup${NC}"
    echo -e "${CYAN}═══════════════════════════════════${NC}"
    echo ""
    
    echo -e "${YELLOW}Step 1/5: Network Optimization${NC}"
    sudo "$SCRIPT_DIR/mc96_optimize.sh"
    echo ""
    
    echo -e "${YELLOW}Step 2/5: Device Scan${NC}"
    python3 "$SCRIPT_DIR/mc96_scan.py"
    echo ""
    
    echo -e "${YELLOW}Step 3/5: Mesh Network${NC}"
    python3 "$SCRIPT_DIR/mc96_mesh.py"
    echo ""
    
    echo -e "${YELLOW}Step 4/5: Auto-Healing Check${NC}"
    python3 "$SCRIPT_DIR/mc96_autoheal.py"
    echo ""
    
    echo -e "${YELLOW}Step 5/5: Analytics Report${NC}"
    python3 "$SCRIPT_DIR/mc96_analytics.py"
    echo ""
    
    echo -e "${GREEN}✅ AUTO-COMPLETE FINISHED!${NC}"
    echo -e "${GREEN}   MC96ECOUNIVERSE is fully operational!${NC}"
    wait_key
}

# Option Q: Quick Start
quick_start() {
    echo -e "${CYAN}🏁 QUICK START: Essential Setup${NC}"
    echo -e "${CYAN}════════════════════════════════${NC}"
    echo ""
    
    echo -e "${YELLOW}Step 1/3: Network Optimization${NC}"
    sudo "$SCRIPT_DIR/mc96_optimize.sh"
    echo ""
    
    echo -e "${YELLOW}Step 2/3: Device Scan${NC}"
    python3 "$SCRIPT_DIR/mc96_scan.py"
    echo ""
    
    echo -e "${YELLOW}Step 3/3: Mesh Network${NC}"
    python3 "$SCRIPT_DIR/mc96_mesh.py"
    echo ""
    
    echo -e "${GREEN}✅ QUICK START COMPLETE!${NC}"
    echo -e "${GREEN}   MC96 Mesh Network is ready!${NC}"
    wait_key
}

# Option H: Help
show_help() {
    clear
    echo -e "${CYAN}📚 MC96ECOUNIVERSE HELP & DOCUMENTATION${NC}"
    echo -e "${CYAN}═══════════════════════════════════════${NC}"
    echo ""
    echo -e "${YELLOW}WHAT IS MC96ECOUNIVERSE?${NC}"
    echo "  A complete high-performance networking system with:"
    echo "  • Jumbo Frames (MTU 9000) for 15-20% speed boost"
    echo "  • TCP/IP stack optimization"
    echo "  • Automatic device detection"
    echo "  • Full mesh tunnel networking"
    echo "  • Real-time monitoring"
    echo "  • Self-healing diagnostics"
    echo ""
    echo -e "${YELLOW}TYPICAL WORKFLOW:${NC}"
    echo "  1. Optimize Network (run after reboot)"
    echo "  2. Scan for Devices (find MC96 nodes)"
    echo "  3. Build Mesh (connect all nodes)"
    echo "  4. Monitor (watch performance)"
    echo ""
    echo -e "${YELLOW}RECOMMENDED: Quick Start [Q]${NC}"
    echo "  Runs optimize + scan + mesh in one go!"
    echo ""
    echo -e "${YELLOW}FULL DOCUMENTATION:${NC}"
    echo "  See: MC96_README.md in scripts directory"
    echo ""
    wait_key
}

# Main menu loop
while true; do
    clear
    echo -e "${CYAN}"
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║              🔥 MC96ECOUNIVERSE MASTER LAUNCHER 🔥             ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    echo ""
    
    show_menu
    
    echo -n -e "${GREEN}Select option: ${NC}"
    read -n 1 choice
    echo ""
    echo ""
    
    case $choice in
        1) optimize_network ;;
        2) scan_network ;;
        3) build_mesh ;;
        4) launch_monitor ;;
        5) run_autoheal ;;
        6) run_analytics ;;
        [Aa]) auto_complete ;;
        [Qq]) quick_start ;;
        [Hh]) show_help ;;
        [Xx]) 
            echo -e "${YELLOW}👋 GORUNFREE! 🎸🔥${NC}"
            echo ""
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid option. Please try again.${NC}"
            sleep 2
            ;;
    esac
done

