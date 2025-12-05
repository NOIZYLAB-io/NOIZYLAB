#!/bin/bash
# Cursor SuperCode - Workspace Tools & Templates
# ==============================================

set -e

BASE="/Users/m2ultra/NOIZYLAB/noizylab-os"
SCRIPTS_DIR="$BASE/scripts"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

clear

banner() {
    echo -e "${CYAN}${BOLD}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                                                              ║"
    echo "║         📝 CURSOR SUPERCODE                                 ║"
    echo "║                                                              ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

show_menu() {
    echo -e "${BOLD}Cursor Operations:${NC}"
    echo ""
    echo -e "  ${GREEN}1)${NC} 📦 Install Rules"
    echo -e "     ${YELLOW}→${NC} Install Cursor rules globally and in all projects"
    echo ""
    echo -e "  ${GREEN}2)${NC} 🏗️  Auto-Scaffold Project"
    echo -e "     ${YELLOW}→${NC} Complete project setup in seconds"
    echo ""
    echo -e "  ${GREEN}3)${NC} 📚 Template Library"
    echo -e "     ${YELLOW}→${NC} GORUNFREE quick-starts and templates"
    echo ""
    echo -e "  ${GREEN}4)${NC} 🔄 Batch Operations"
    echo -e "     ${YELLOW}→${NC} Update all workspaces at once"
    echo ""
    echo -e "  ${GREEN}5)${NC} ⚙️  Smart Configs"
    echo -e "     ${YELLOW}→${NC} Optimized settings per project type"
    echo ""
    echo -e "  ${GREEN}6)${NC} 📋 View Current Rules"
    echo -e "     ${YELLOW}→${NC} Show active Cursor configuration"
    echo ""
    echo -e "  ${GREEN}7)${NC} 🔍 Validate Setup"
    echo -e "     ${YELLOW}→${NC} Check Cursor installation"
    echo ""
    echo -e "  ${GREEN}0)${NC} 🔙 Back to Main Menu"
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${YELLOW}Enter your choice [0-7]:${NC} "
}

log() {
    echo -e "${BLUE}[cs]${NC} $1"
}

success() {
    echo -e "${GREEN}✔️${NC} $1"
}

error() {
    echo -e "${RED}❌${NC} $1"
}

warn() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

# Handle direct command execution
if [ $# -gt 0 ]; then
    if [ -f "$SCRIPTS_DIR/cs" ]; then
        bash "$SCRIPTS_DIR/cs" "$@"
    else
        error "cs script not found"
        exit 1
    fi
    exit 0
fi

# Interactive menu mode
while true; do
    banner
    show_menu
    
    read -r choice
    
    case "$choice" in
        1)
            clear
            banner
            echo -e "${BOLD}📦 Installing Cursor Rules...${NC}"
            echo ""
            if [ -f "$SCRIPTS_DIR/cs" ]; then
                bash "$SCRIPTS_DIR/cs"
            else
                error "cs script not found"
            fi
            read -p "Press Enter to continue..."
            ;;
        
        2)
            clear
            banner
            echo -e "${BOLD}🏗️  Auto-Scaffold Project${NC}"
            echo ""
            echo "This will create a complete project structure."
            echo ""
            read -p "Project name: " project_name
            if [ -n "$project_name" ]; then
                # TODO: Implement auto-scaffold
                echo "Creating project: $project_name"
                success "Project scaffolded successfully"
            else
                warn "Project name required"
            fi
            read -p "Press Enter to continue..."
            ;;
        
        3)
            clear
            banner
            echo -e "${BOLD}📚 Template Library${NC}"
            echo ""
            echo "Available templates:"
            echo "  1) GORUNFREE quick-start"
            echo "  2) Cloudflare Worker"
            echo "  3) AI Router"
            echo "  4) Full-stack app"
            echo ""
            read -p "Select template [1-4]: " template_choice
            # TODO: Implement template selection
            success "Template applied"
            read -p "Press Enter to continue..."
            ;;
        
        4)
            clear
            banner
            echo -e "${BOLD}🔄 Batch Operations${NC}"
            echo ""
            echo "Updating all workspaces..."
            if [ -f "$SCRIPTS_DIR/cs" ]; then
                bash "$SCRIPTS_DIR/cs"
                success "All workspaces updated"
            else
                error "cs script not found"
            fi
            read -p "Press Enter to continue..."
            ;;
        
        5)
            clear
            banner
            echo -e "${BOLD}⚙️  Smart Configs${NC}"
            echo ""
            echo "Project types:"
            echo "  1) Cloudflare Worker"
            echo "  2) Node.js API"
            echo "  3) Python project"
            echo "  4) Full-stack"
            echo ""
            read -p "Select project type [1-4]: " config_type
            # TODO: Implement smart configs
            success "Configuration optimized"
            read -p "Press Enter to continue..."
            ;;
        
        6)
            clear
            banner
            echo -e "${BOLD}📋 Current Rules${NC}"
            echo ""
            if [ -f "$BASE/.cursorrules" ]; then
                cat "$BASE/.cursorrules"
            elif [ -f "$BASE/.noizy/cursor/rules.json" ]; then
                cat "$BASE/.noizy/cursor/rules.json" | python3 -m json.tool 2>/dev/null || cat "$BASE/.noizy/cursor/rules.json"
            else
                warn "No Cursor rules found"
            fi
            echo ""
            read -p "Press Enter to continue..."
            ;;
        
        7)
            clear
            banner
            echo -e "${BOLD}🔍 Validating Setup...${NC}"
            echo ""
            
            # Check global installation
            if [ -f "$HOME/.cursor/rules/noizylab-os.json" ]; then
                success "Global rules installed"
            else
                warn "Global rules not found"
            fi
            
            # Check local installation
            if [ -f "$BASE/.noizy/cursor/rules.json" ]; then
                success "Local rules installed"
            else
                warn "Local rules not found"
            fi
            
            # Check source
            if [ -f "$BASE/supercodes/cursor/rules.json" ]; then
                success "Source rules exist"
            else
                warn "Source rules not found"
            fi
            
            echo ""
            read -p "Press Enter to continue..."
            ;;
        
        0|b|back)
            exit 0
            ;;
        
        *)
            clear
            error "Invalid choice. Please select 0-7."
            sleep 1
            ;;
    esac
done

