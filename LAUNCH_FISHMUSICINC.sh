#!/bin/bash
# FISH MUSIC INC - MASTER LAUNCHER
# One command to access ALL systems
# Created by CB_01 for ROB - GORUNFREE! 🎸🔥

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

show_banner() {
    clear
    echo ""
    echo "🎸 FISH MUSIC INC - MASTER CONTROL"
    echo "Built by CB_01 | GORUNFREE! 🔥"
    echo ""
}

show_main_menu() {
    echo -e "${BLUE}════════════════════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}                    FISH MUSIC INC COMMAND CENTER${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${GREEN}🌐 NETWORK & INFRASTRUCTURE${NC}"
    echo -e "   [1] MC96 Network System (optimize/scan/monitor)"
    echo -e "   [2] Master Dashboard (view all systems)"
    echo -e "   [3] DNS Repair Tool"
    echo ""
    echo -e "${GREEN}🎵 SPOTIFY & MUSIC${NC}"
    echo -e "   [4] Spotify Manager (playlists/analysis)"
    echo -e "   [5] Spotify Hot Rod (deep analysis/optimization)"
    echo -e "   [6] Music Discovery Engine (find tracks)"
    echo ""
    echo -e "${GREEN}📧 EMAIL & COMMUNICATION${NC}"
    echo -e "   [7] Gmail Setup Guide (S-SEES + Divine Emperor)"
    echo ""
    echo -e "${GREEN}🎸 MUSIC PRODUCTION${NC}"
    echo -e "   [8] Find All Music (scan 80+ TB archive)"
    echo -e "   [9] Client Portfolio (FUEL/McDonald's/Microsoft/Deadwood)"
    echo -e "   [10] Release Automation (singles/EPs/albums)"
    echo ""
    echo -e "${GREEN}💼 BUSINESS${NC}"
    echo -e "   [11] Backup Master (manage 19 volumes)"
    echo -e "   [12] Client Manager (invoices/projects)"
    echo ""
    echo -e "${CYAN}🚀 QUICK ACTIONS${NC}"
    echo -e "   [Q] Quick Status (all systems)"
    echo -e "   [W] Open Portfolio Website"
    echo -e "   [S] Open Spotify Profile"
    echo ""
    echo -e "${MAGENTA}   [H] Help & Documentation"
    echo -e "   [X] Exit${NC}"
    echo ""
    echo -e "${BLUE}════════════════════════════════════════════════════════════════════${NC}"
    echo ""
}

wait_key() {
    echo ""
    echo -e "${YELLOW}Press any key to continue...${NC}"
    read -n 1 -s
}

# Menu handlers
mc96_menu() {
    cd "$SCRIPT_DIR/tools/scripts"
    ./mc96_launcher.sh
}

master_dashboard() {
    cd "$SCRIPT_DIR/tools/scripts"
    python3 master_dashboard.py
    wait_key
}

dns_repair() {
    echo -e "${YELLOW}🔥 DNS REPAIR TOOL${NC}"
    echo ""
    echo "Available scripts:"
    echo "  1. sudo bash ~/Downloads/DNS-REPAIR.sh (full protocol)"
    echo "  2. sudo bash ~/Downloads/FIX-DNS-NOW.sh (quick fix)"
    echo ""
    wait_key
}

spotify_manager() {
    cd "$SCRIPT_DIR/api/integrations"
    python3 spotify_manager.py --profile
    wait_key
}

spotify_hotrod() {
    cd "$SCRIPT_DIR/api/integrations"
    echo -e "${YELLOW}🔥 SPOTIFY HOT ROD${NC}"
    echo ""
    echo "Commands:"
    echo "  python3 spotify_hotrod.py analyze <playlist_url>"
    echo "  python3 spotify_hotrod.py optimize <playlist_url> <method>"
    echo ""
    echo "Methods: energy_flow, bpm_ascending, mood_journey, key_flow"
    echo ""
    wait_key
}

music_discovery() {
    cd "$SCRIPT_DIR/ai/music-recommender"
    echo -e "${YELLOW}🎵 MUSIC DISCOVERY ENGINE${NC}"
    echo ""
    echo "Commands:"
    echo "  python3 spotify_discovery_engine.py mood <happy/sad/energetic/etc>"
    echo "  python3 spotify_discovery_engine.py bpm <min> <max>"
    echo "  python3 spotify_discovery_engine.py workout <cardio/strength/yoga> <duration>"
    echo ""
    wait_key
}

gmail_setup() {
    echo -e "${YELLOW}📧 GMAIL SETUP GUIDES${NC}"
    echo ""
    echo "Documentation:"
    echo "  • S-SEES Escalation: $SCRIPT_DIR/api/integrations/GMAIL_ESCALATION_README.md"
    echo "  • Divine Emperor Dashboard: $SCRIPT_DIR/api/integrations/GMAIL_DASHBOARD_SETUP.md"
    echo ""
    echo "Apps Script: https://script.google.com"
    echo ""
    wait_key
}

find_music() {
    cd "$SCRIPT_DIR/ai/metadata-scanner"
    echo -e "${YELLOW}🎸 FINDING ALL YOUR MUSIC...${NC}"
    echo ""
    python3 find_all_music.py
    wait_key
}

client_portfolio() {
    cd "$SCRIPT_DIR/business/accounting"
    python3 client_manager.py
    wait_key
}

release_automation() {
    cd "$SCRIPT_DIR/tools/scripts"
    python3 release_automation.py
    wait_key
}

backup_master() {
    cd "$SCRIPT_DIR/tools/scripts"
    python3 backup_master.py
    wait_key
}

quick_status() {
    cd "$SCRIPT_DIR/tools/scripts"
    python3 master_dashboard.py
}

open_website() {
    open "$SCRIPT_DIR/website/public/index.html"
    echo -e "${GREEN}✅ Portfolio website opened in browser!${NC}"
    sleep 2
}

open_spotify() {
    open "https://open.spotify.com/user/fishmusicinc"
    echo -e "${GREEN}✅ Spotify profile opened in browser!${NC}"
    sleep 2
}

show_help() {
    clear
    echo -e "${CYAN}📚 FISH MUSIC INC - HELP & DOCUMENTATION${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════${NC}"
    echo ""
    echo -e "${YELLOW}WHAT IS THIS SYSTEM?${NC}"
    echo "  Complete professional music business infrastructure:"
    echo "  • Network optimization (MC96ECOUNIVERSE)"
    echo "  • Email automation (S-SEES + Divine Emperor)"
    echo "  • Spotify power tools (analysis/optimization/discovery)"
    echo "  • Music archive management (80+ TB)"
    echo "  • Client & project management"
    echo "  • Release automation"
    echo "  • Backup systems"
    echo ""
    echo -e "${YELLOW}QUICK START:${NC}"
    echo "  Press [Q] for Quick Status to see all systems"
    echo "  Press [2] for Master Dashboard"
    echo "  Press [W] to view your portfolio website"
    echo "  Press [S] to open your Spotify"
    echo ""
    echo -e "${YELLOW}DOCUMENTATION:${NC}"
    echo "  • MC96: tools/scripts/MC96_README.md"
    echo "  • Spotify: api/integrations/SPOTIFY_HOTROD_README.md"
    echo "  • Email: api/integrations/GMAIL_DASHBOARD_SETUP.md"
    echo ""
    wait_key
}

# Main menu loop
while true; do
    show_banner
    show_main_menu

    echo -n -e "${GREEN}Select option: ${NC}"
    read -n 1 choice
    echo ""
    echo ""

    case $choice in
        1) mc96_menu ;;
        2) master_dashboard ;;
        3) dns_repair ;;
        4) spotify_manager ;;
        5) spotify_hotrod ;;
        6) music_discovery ;;
        7) gmail_setup ;;
        8) find_music ;;
        9) client_portfolio ;;
        10|0) release_automation ;;
        11) backup_master ;;
        12) echo "Client Manager coming..." && wait_key ;;
        [Qq]) quick_status && wait_key ;;
        [Ww]) open_website ;;
        [Ss]) open_spotify ;;
        [Hh]) show_help ;;
        [Xx])
            echo -e "${YELLOW}👋 GORUNFREE! 🎸🔥${NC}"
            echo ""
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid option. Try again.${NC}"
            sleep 2
            ;;
    esac
done

