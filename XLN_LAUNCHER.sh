#!/bin/bash
#═══════════════════════════════════════════════════════════════════════════════
#  🎹 XLN AUDIO MASTER LIBRARY MANAGEMENT SYSTEM
#     Addictive Drums • Addictive Keys • XO • Trigger
#═══════════════════════════════════════════════════════════════════════════════

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/xln_audio_master.py"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

print_menu() {
    clear
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                              ║"
    echo "║   ██╗  ██╗██╗     ███╗   ██╗     █████╗ ██╗   ██╗██████╗ ██╗ ██████╗         ║"
    echo "║   ╚██╗██╔╝██║     ████╗  ██║    ██╔══██╗██║   ██║██╔══██╗██║██╔═══██╗        ║"
    echo "║    ╚███╔╝ ██║     ██╔██╗ ██║    ███████║██║   ██║██║  ██║██║██║   ██║        ║"
    echo "║    ██╔██╗ ██║     ██║╚██╗██║    ██╔══██║██║   ██║██║  ██║██║██║   ██║        ║"
    echo "║   ██╔╝ ██╗███████╗██║ ╚████║    ██║  ██║╚██████╔╝██████╔╝██║╚██████╔╝        ║"
    echo "║   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝         ║"
    echo "║                                                                              ║"
    echo "║       🎹 ADDICTIVE DRUMS • ADDICTIVE KEYS • XO • TRIGGER 🎹                  ║"
    echo "║                                                                              ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "  ${GREEN}[1]${NC} 🔍 ${CYAN}QUICK SCAN${NC}      - Fast scan across all volumes"
    echo -e "  ${GREEN}[2]${NC} 🔬 ${CYAN}DEEP SCAN${NC}       - Comprehensive analysis with duplicates"
    echo -e "  ${GREEN}[3]${NC} 🧪 ${CYAN}TEST${NC}            - Verify file integrity"
    echo -e "  ${GREEN}[4]${NC} 🔧 ${CYAN}HEAL${NC}            - Fix permissions and structure (dry run)"
    echo -e "  ${GREEN}[5]${NC} 🔧 ${MAGENTA}HEAL + APPLY${NC}   - Fix all issues (APPLIES CHANGES)"
    echo -e "  ${GREEN}[6]${NC} ⚡ ${CYAN}OPTIMIZE${NC}        - Remove duplicates (dry run)"
    echo -e "  ${GREEN}[7]${NC} ⚡ ${MAGENTA}OPTIMIZE + APPLY${NC} - Remove duplicates (APPLIES CHANGES)"
    echo -e "  ${GREEN}[8]${NC} 📦 ${CYAN}ORGANIZE${NC}        - Reorganize to master library (dry run)"
    echo -e "  ${GREEN}[9]${NC} 📦 ${MAGENTA}ORGANIZE + APPLY${NC} - Reorganize (APPLIES CHANGES)"
    echo -e "  ${GREEN}[F]${NC} 🚀 ${YELLOW}FULL PIPELINE${NC}  - Run all operations"
    echo -e "  ${GREEN}[R]${NC} 📄 ${CYAN}REPORT${NC}          - Generate detailed report"
    echo ""
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  ${RED}[Q]${NC} Exit"
    echo ""
}

run_command() {
    echo ""
    echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}Running: python3 $PYTHON_SCRIPT $1${NC}"
    echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════════════════${NC}"
    echo ""
    python3 "$PYTHON_SCRIPT" $1
    echo ""
    echo -e "${CYAN}Press Enter to continue...${NC}"
    read
}

while true; do
    print_menu
    echo -e -n "${GREEN}Select option: ${NC}"
    read -n 1 choice
    echo ""
    
    case $choice in
        1) run_command "scan --quick" ;;
        2) run_command "deep" ;;
        3) run_command "test" ;;
        4) run_command "heal" ;;
        5) run_command "heal --apply" ;;
        6) run_command "optimize" ;;
        7) run_command "optimize --apply" ;;
        8) run_command "organize" ;;
        9) run_command "organize --apply" ;;
        [Ff]) run_command "full" ;;
        [Rr]) run_command "report" ;;
        [Qq]) 
            echo -e "${GREEN}Goodbye! 🎹${NC}"
            exit 0 
            ;;
        *) 
            echo -e "${RED}Invalid option${NC}"
            sleep 1
            ;;
    esac
done
