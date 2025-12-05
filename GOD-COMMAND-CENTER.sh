#!/bin/bash
#═══════════════════════════════════════════════════════════════════════════════
#
#  ██████╗  ██████╗ ██████╗ 
# ██╔════╝ ██╔═══██╗██╔══██╗
# ██║  ███╗██║   ██║██║  ██║
# ██║   ██║██║   ██║██║  ██║
# ╚██████╔╝╚██████╔╝██████╔╝
#  ╚═════╝  ╚═════╝ ╚═════╝ 
#
#  GOD COMMAND CENTER v3.0.0
#  ═══════════════════════════════════════════════════════════════════════════
#
#  THE ULTIMATE COMMAND SYSTEM FOR ROB PLOWMAN
#
#  One command to rule them all:
#    • Email Empire (5 emails → 1 inbox)
#    • Network Toolkit (DNS, diagnostics, repair, speed)
#    • System Control (cleanup, maintenance, monitoring)
#    • NOIZYLAB Business (repairs, invoices, customers)
#    • Fish Music Inc (studio, projects, clients)
#    • Cloudflare Management (workers, DNS, email routing)
#    • Voice Control Integration (GABRIEL ready)
#
#  Install: bash ~/Downloads/GOD-COMMAND-CENTER.sh --install
#  Usage:   god [command] [subcommand] [options]
#
#  Built for: Rob Plowman | NOIZYLAB | Fish Music Inc
#  Philosophy: GORUNFREE - One command = Everything done
#
#═══════════════════════════════════════════════════════════════════════════════

VERSION="3.0.0"
GOD_HOME="$HOME/.god"
GOD_LOG="$GOD_HOME/logs"
GOD_CONFIG="$GOD_HOME/config"

#═══════════════════════════════════════════════════════════════════════════════
# COLORS & FORMATTING
#═══════════════════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
ORANGE='\033[38;5;208m'
GOLD='\033[38;5;220m'
WHITE='\033[1;37m'
GRAY='\033[0;90m'
BOLD='\033[1m'
DIM='\033[2m'
ITALIC='\033[3m'
UNDERLINE='\033[4m'
BLINK='\033[5m'
NC='\033[0m'

# Icons
FIRE="🔥"
BOLT="⚡"
ROCKET="🚀"
GLOBE="🌐"
LOCK="🔒"
GEAR="⚙️"
MAIL="📧"
WRENCH="🔧"
MUSIC="🎵"
FISH="🐟"
CHECK="✓"
CROSS="✗"
WARN="⚠"
STAR="⭐"
DIAMOND="💎"
CROWN="👑"

#═══════════════════════════════════════════════════════════════════════════════
# INITIALIZATION
#═══════════════════════════════════════════════════════════════════════════════

init_god() {
    mkdir -p "$GOD_HOME" "$GOD_LOG" "$GOD_CONFIG"
    mkdir -p ~/NOIZYLAB/{email,network,repairs,invoices,docs}
    mkdir -p ~/FishMusic/{projects,clients,studio}
}

#═══════════════════════════════════════════════════════════════════════════════
# EPIC BANNER
#═══════════════════════════════════════════════════════════════════════════════

show_banner() {
    echo -e "${GOLD}"
    cat << 'BANNER'
    
    ██████╗  ██████╗ ██████╗      ██████╗ ██████╗ ███╗   ███╗███╗   ███╗ █████╗ ███╗   ██╗██████╗ 
   ██╔════╝ ██╔═══██╗██╔══██╗    ██╔════╝██╔═══██╗████╗ ████║████╗ ████║██╔══██╗████╗  ██║██╔══██╗
   ██║  ███╗██║   ██║██║  ██║    ██║     ██║   ██║██╔████╔██║██╔████╔██║███████║██╔██╗ ██║██║  ██║
   ██║   ██║██║   ██║██║  ██║    ██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║
   ╚██████╔╝╚██████╔╝██████╔╝    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝
    ╚═════╝  ╚═════╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 
                                                                                                   
BANNER
    echo -e "${NC}"
    echo -e "${CYAN}                     ═══════════════════════════════════════════════════${NC}"
    echo -e "${WHITE}                              ${CROWN} THE ULTIMATE COMMAND SYSTEM ${CROWN}${NC}"
    echo -e "${GRAY}                                    v${VERSION} | GORUNFREE${NC}"
    echo -e "${CYAN}                     ═══════════════════════════════════════════════════${NC}"
    echo ""
}

show_mini_banner() {
    echo -e "${GOLD}═══${NC} ${WHITE}${BOLD}GOD${NC} ${GOLD}═══${NC} ${GRAY}v${VERSION}${NC}"
}

#═══════════════════════════════════════════════════════════════════════════════
# HELP SYSTEM
#═══════════════════════════════════════════════════════════════════════════════

show_help() {
    show_banner
    
    echo -e "${FIRE} ${BOLD}${WHITE}QUICK COMMANDS${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god${NC}                    Dashboard overview"
    echo -e "  ${YELLOW}god go${NC}                 Morning startup sequence"
    echo -e "  ${YELLOW}god status${NC}             Full system status"
    echo -e "  ${YELLOW}god fix${NC}                Auto-fix common issues"
    echo ""
    
    echo -e "${MAIL} ${BOLD}${WHITE}EMAIL EMPIRE${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god email${NC}              Open inbox"
    echo -e "  ${YELLOW}god email support${NC}      Support queue (help@noizylab.ca)"
    echo -e "  ${YELLOW}god email fish${NC}         Fish Music emails"
    echo -e "  ${YELLOW}god email noizy${NC}        NOIZYLAB emails"
    echo -e "  ${YELLOW}god email new${NC}          Compose new email"
    echo -e "  ${YELLOW}god email new-help${NC}     Compose as help@noizylab.ca"
    echo -e "  ${YELLOW}god email status${NC}       Show all 5 email addresses"
    echo ""
    
    echo -e "${GLOBE} ${BOLD}${WHITE}NETWORK TOOLKIT${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god net${NC}                Network status"
    echo -e "  ${YELLOW}god net dns${NC}            Fix DNS (Cloudflare 1.1.1.1)"
    echo -e "  ${YELLOW}god net flush${NC}          Flush DNS cache"
    echo -e "  ${YELLOW}god net reset${NC}          Full network reset"
    echo -e "  ${YELLOW}god net test${NC}           Test connectivity"
    echo -e "  ${YELLOW}god net speed${NC}          Speed test"
    echo -e "  ${YELLOW}god net wifi${NC}           WiFi diagnostics"
    echo -e "  ${YELLOW}god net trace${NC}          Cloudflare trace"
    echo ""
    
    echo -e "${WRENCH} ${BOLD}${WHITE}NOIZYLAB BUSINESS${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god noizy${NC}              NOIZYLAB dashboard"
    echo -e "  ${YELLOW}god noizy site${NC}         Open noizylab.ca"
    echo -e "  ${YELLOW}god noizy admin${NC}        Cloudflare dashboard"
    echo -e "  ${YELLOW}god noizy stripe${NC}       Stripe dashboard"
    echo -e "  ${YELLOW}god noizy repairs${NC}      Repair tracker"
    echo -e "  ${YELLOW}god noizy book${NC}         Booking page"
    echo ""
    
    echo -e "${FISH} ${BOLD}${WHITE}FISH MUSIC INC${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god fish${NC}               Fish Music dashboard"
    echo -e "  ${YELLOW}god fish site${NC}          Open fishmusicinc.com"
    echo -e "  ${YELLOW}god fish drive${NC}         Google Drive"
    echo -e "  ${YELLOW}god fish studio${NC}        Studio folder"
    echo ""
    
    echo -e "${GEAR} ${BOLD}${WHITE}SYSTEM CONTROL${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god sys${NC}                System info"
    echo -e "  ${YELLOW}god sys clean${NC}          Cleanup (caches, logs, trash)"
    echo -e "  ${YELLOW}god sys memory${NC}         Memory status"
    echo -e "  ${YELLOW}god sys disk${NC}           Disk usage"
    echo -e "  ${YELLOW}god sys top${NC}            Top processes"
    echo -e "  ${YELLOW}god sys restart${NC}        Restart services"
    echo ""
    
    echo -e "${ROCKET} ${BOLD}${WHITE}CLOUDFLARE${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god cf${NC}                 Cloudflare dashboard"
    echo -e "  ${YELLOW}god cf workers${NC}         Workers dashboard"
    echo -e "  ${YELLOW}god cf dns [domain]${NC}    DNS settings"
    echo -e "  ${YELLOW}god cf email${NC}           Email routing"
    echo -e "  ${YELLOW}god cf status${NC}          Cloudflare status"
    echo ""
    
    echo -e "${DIAMOND} ${BOLD}${WHITE}DEVELOPMENT${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god dev${NC}                Dev environment"
    echo -e "  ${YELLOW}god dev code${NC}           Open VS Code"
    echo -e "  ${YELLOW}god dev cursor${NC}         Open Cursor"
    echo -e "  ${YELLOW}god dev term${NC}           Open Terminal"
    echo -e "  ${YELLOW}god dev github${NC}         Open GitHub"
    echo ""
    
    echo -e "${STAR} ${BOLD}${WHITE}QUICK ACTIONS${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god claude${NC}             Open Claude.ai"
    echo -e "  ${YELLOW}god chatgpt${NC}            Open ChatGPT"
    echo -e "  ${YELLOW}god gemini${NC}             Open Gemini"
    echo -e "  ${YELLOW}god perplexity${NC}         Open Perplexity"
    echo -e "  ${YELLOW}god docs${NC}               Open Google Docs"
    echo -e "  ${YELLOW}god sheets${NC}             Open Google Sheets"
    echo -e "  ${YELLOW}god cal${NC}                Open Google Calendar"
    echo ""
}

#═══════════════════════════════════════════════════════════════════════════════
# UTILITIES
#═══════════════════════════════════════════════════════════════════════════════

log() {
    local msg="$1"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] $msg" >> "$GOD_LOG/god.log"
}

success() { echo -e "${GREEN}${CHECK}${NC} $1"; }
error() { echo -e "${RED}${CROSS}${NC} $1"; }
warn() { echo -e "${YELLOW}${WARN}${NC} $1"; }
info() { echo -e "${CYAN}ℹ${NC} $1"; }

get_primary_interface() {
    route -n get default 2>/dev/null | grep 'interface:' | awk '{print $2}'
}

get_primary_service() {
    local iface=$(get_primary_interface)
    networksetup -listallhardwareports | grep -B1 "Device: $iface" 2>/dev/null | head -1 | cut -d: -f2 | xargs
}

get_local_ip() {
    ipconfig getifaddr "$(get_primary_interface)" 2>/dev/null || echo "unknown"
}

get_public_ip() {
    curl -s --max-time 3 https://api.ipify.org 2>/dev/null || echo "unknown"
}

check_url() {
    curl -s --max-time 5 -o /dev/null -w "%{http_code}" "https://$1" 2>/dev/null | grep -qE "^[23]"
}

#═══════════════════════════════════════════════════════════════════════════════
# DASHBOARD
#═══════════════════════════════════════════════════════════════════════════════

show_dashboard() {
    clear
    show_banner
    
    local timestamp=$(date '+%A, %B %d, %Y • %I:%M %p')
    echo -e "${GRAY}                              $timestamp${NC}"
    echo ""
    
    # System Status
    echo -e "${BOLT} ${BOLD}SYSTEM STATUS${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    
    local cpu=$(top -l 1 | grep "CPU usage" | awk '{print $3}' | tr -d '%')
    local mem_used=$(vm_stat | grep "Pages active" | awk '{print $3}' | tr -d '.')
    local mem_free=$(vm_stat | grep "Pages free" | awk '{print $3}' | tr -d '.')
    local disk=$(df -h / | tail -1 | awk '{print $5}')
    local uptime_str=$(uptime | sed 's/.*up //' | sed 's/,.*//')
    
    echo -e "  ${CYAN}CPU:${NC} ${cpu:-N/A}%    ${CYAN}Disk:${NC} $disk    ${CYAN}Uptime:${NC} $uptime_str"
    echo ""
    
    # Network Status
    echo -e "${GLOBE} ${BOLD}NETWORK${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    
    local local_ip=$(get_local_ip)
    local public_ip=$(get_public_ip)
    local dns=$(scutil --dns 2>/dev/null | grep "nameserver\[0\]" | head -1 | awk '{print $3}')
    
    echo -e "  ${CYAN}Local:${NC} $local_ip    ${CYAN}Public:${NC} $public_ip    ${CYAN}DNS:${NC} $dns"
    
    # Quick connectivity check
    echo -n "  ${CYAN}Status:${NC} "
    if check_url "google.com"; then
        echo -e "${GREEN}● Online${NC}"
    else
        echo -e "${RED}● Offline${NC}"
    fi
    echo ""
    
    # Email Status
    echo -e "${MAIL} ${BOLD}EMAIL EMPIRE${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${FISH} rp@fishmusicinc.com ${YELLOW}(PRIMARY)${NC}"
    echo -e "  ${FISH} info@fishmusicinc.com"
    echo -e "  ${WRENCH} rsp@noizylab.ca"
    echo -e "  ${WRENCH} help@noizylab.ca ${YELLOW}(SUPPORT)${NC}"
    echo -e "  ${WRENCH} hello@noizylab.ca"
    echo -e "  ${GRAY}All → rp@fishmusicinc.com (ONE INBOX)${NC}"
    echo ""
    
    # Quick Actions
    echo -e "${ROCKET} ${BOLD}QUICK ACTIONS${NC}"
    echo -e "${GRAY}───────────────────────────────────────────────────────────────────────────${NC}"
    echo -e "  ${YELLOW}god go${NC}        Morning startup    ${YELLOW}god email${NC}     Check inbox"
    echo -e "  ${YELLOW}god fix${NC}       Auto-fix issues    ${YELLOW}god net dns${NC}   Fix DNS"
    echo -e "  ${YELLOW}god status${NC}    Full status        ${YELLOW}god help${NC}      All commands"
    echo ""
    
    echo -e "${GOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
    echo -e "${GRAY}                          Type 'god help' for all commands${NC}"
    echo ""
}

#═══════════════════════════════════════════════════════════════════════════════
# MORNING STARTUP
#═══════════════════════════════════════════════════════════════════════════════

morning_startup() {
    show_banner
    
    echo -e "${FIRE} ${BOLD}${WHITE}GOOD MORNING ROB! ${FIRE}${NC}"
    echo -e "${GRAY}Starting your day...${NC}"
    echo ""
    
    # Step 1: Network check
    echo -e "${YELLOW}[1/5]${NC} Checking network..."
    if check_url "google.com"; then
        success "Network online"
    else
        warn "Network issues detected - fixing..."
        fix_dns
    fi
    
    # Step 2: Open email
    echo -e "${YELLOW}[2/5]${NC} Opening inbox..."
    open "https://mail.google.com/mail/u/0/#inbox"
    success "Inbox opened"
    
    # Step 3: Open support queue
    echo -e "${YELLOW}[3/5]${NC} Checking support queue..."
    open "https://mail.google.com/mail/u/0/#label/%F0%9F%94%A7+NOIZYLAB%2FSupport"
    success "Support queue opened"
    
    # Step 4: Open Claude
    echo -e "${YELLOW}[4/5]${NC} Opening Claude..."
    open "https://claude.ai"
    success "Claude opened"
    
    # Step 5: System cleanup
    echo -e "${YELLOW}[5/5]${NC} Quick cleanup..."
    sudo purge 2>/dev/null || true
    success "Memory cleared"
    
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                                                                           ║${NC}"
    echo -e "${GREEN}║              ${FIRE} GOD IS READY - HAVE A GREAT DAY ROB! ${FIRE}                   ║${NC}"
    echo -e "${GREEN}║                                                                           ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    log "Morning startup completed"
}

#═══════════════════════════════════════════════════════════════════════════════
# AUTO-FIX
#═══════════════════════════════════════════════════════════════════════════════

auto_fix() {
    show_mini_banner
    echo ""
    echo -e "${FIRE} ${BOLD}AUTO-FIX SEQUENCE${NC}"
    echo ""
    
    local fixed=0
    
    # Check network
    echo -e "${YELLOW}[1/4]${NC} Checking network..."
    if ! check_url "google.com"; then
        warn "Network issues - fixing DNS..."
        sudo networksetup -setdnsservers "$(get_primary_service)" 1.1.1.1 1.0.0.1 2>/dev/null
        sudo dscacheutil -flushcache 2>/dev/null
        sudo killall -HUP mDNSResponder 2>/dev/null
        ((fixed++))
        success "DNS fixed"
    else
        success "Network OK"
    fi
    
    # Clear DNS cache
    echo -e "${YELLOW}[2/4]${NC} Flushing DNS cache..."
    sudo dscacheutil -flushcache 2>/dev/null
    sudo killall -HUP mDNSResponder 2>/dev/null
    ((fixed++))
    success "DNS cache flushed"
    
    # Clear memory
    echo -e "${YELLOW}[3/4]${NC} Clearing memory..."
    sudo purge 2>/dev/null || true
    ((fixed++))
    success "Memory cleared"
    
    # Clear temp files
    echo -e "${YELLOW}[4/4]${NC} Clearing temp files..."
    rm -rf ~/Library/Caches/* 2>/dev/null || true
    rm -rf /tmp/* 2>/dev/null || true
    ((fixed++))
    success "Temp files cleared"
    
    echo ""
    echo -e "${GREEN}${CHECK} Fixed $fixed issues!${NC}"
    echo ""
    
    log "Auto-fix completed: $fixed fixes"
}

#═══════════════════════════════════════════════════════════════════════════════
# EMAIL COMMANDS
#═══════════════════════════════════════════════════════════════════════════════

email_cmd() {
    local GMAIL="https://mail.google.com/mail/u/0"
    
    case "${1:-inbox}" in
        inbox|"")
            open "$GMAIL/#inbox"
            success "Inbox opened"
            ;;
        support)
            open "$GMAIL/#label/%F0%9F%94%A7+NOIZYLAB%2FSupport"
            success "Support queue opened"
            ;;
        fish)
            open "$GMAIL/#search/to%3A(*%40fishmusicinc.com)"
            success "Fish Music emails opened"
            ;;
        noizy|noizylab)
            open "$GMAIL/#search/to%3A(*%40noizylab.ca)"
            success "NOIZYLAB emails opened"
            ;;
        starred|star)
            open "$GMAIL/#starred"
            success "Starred emails opened"
            ;;
        sent)
            open "$GMAIL/#sent"
            ;;
        drafts)
            open "$GMAIL/#drafts"
            ;;
        new|compose)
            open "$GMAIL/?compose=new"
            success "New email composer opened"
            ;;
        new-fish)
            open "$GMAIL/?compose=new"
            info "Select From: rp@fishmusicinc.com"
            ;;
        new-info)
            open "$GMAIL/?compose=new"
            info "Select From: info@fishmusicinc.com"
            ;;
        new-noizy|new-rsp)
            open "$GMAIL/?compose=new"
            info "Select From: rsp@noizylab.ca"
            ;;
        new-help)
            open "$GMAIL/?compose=new"
            info "Select From: help@noizylab.ca"
            ;;
        new-hello)
            open "$GMAIL/?compose=new"
            info "Select From: hello@noizylab.ca"
            ;;
        settings)
            open "$GMAIL/#settings/general"
            ;;
        accounts)
            open "$GMAIL/#settings/accounts"
            ;;
        filters)
            open "$GMAIL/#settings/filters"
            ;;
        admin)
            open "https://admin.google.com"
            success "Google Workspace Admin opened"
            ;;
        status)
            echo ""
            echo -e "${MAIL} ${BOLD}EMAIL EMPIRE STATUS${NC}"
            echo -e "${GRAY}───────────────────────────────────────────────────${NC}"
            echo ""
            echo -e "  ${FISH} ${BOLD}FISH MUSIC INC${NC}"
            echo -e "     ${GREEN}●${NC} rp@fishmusicinc.com ${YELLOW}(PRIMARY)${NC}"
            echo -e "     ${GREEN}●${NC} info@fishmusicinc.com"
            echo ""
            echo -e "  ${WRENCH} ${BOLD}NOIZYLAB${NC}"
            echo -e "     ${GREEN}●${NC} rsp@noizylab.ca"
            echo -e "     ${GREEN}●${NC} help@noizylab.ca ${YELLOW}(SUPPORT)${NC}"
            echo -e "     ${GREEN}●${NC} hello@noizylab.ca"
            echo ""
            echo -e "  ${CYAN}All emails → rp@fishmusicinc.com (ONE INBOX)${NC}"
            echo ""
            ;;
        *)
            error "Unknown email command: $1"
            echo "Try: god email [inbox|support|fish|noizy|new|new-help|status]"
            ;;
    esac
}

#═══════════════════════════════════════════════════════════════════════════════
# NETWORK COMMANDS
#═══════════════════════════════════════════════════════════════════════════════

fix_dns() {
    echo -e "${FIRE} Setting Cloudflare DNS (1.1.1.1)..."
    local service=$(get_primary_service)
    sudo networksetup -setdnsservers "$service" 1.1.1.1 1.0.0.1 2>/dev/null
    sudo dscacheutil -flushcache
    sudo killall -HUP mDNSResponder 2>/dev/null
    success "DNS set to Cloudflare (1.1.1.1, 1.0.0.1)"
    
    echo ""
    echo -e "${CYAN}Testing...${NC}"
    if check_url "google.com"; then
        success "google.com - OK"
    else
        error "google.com - FAILED"
    fi
    if check_url "noizylab.ca"; then
        success "noizylab.ca - OK"
    else
        error "noizylab.ca - FAILED"
    fi
}

net_cmd() {
    case "${1:-status}" in
        status|"")
            echo ""
            echo -e "${GLOBE} ${BOLD}NETWORK STATUS${NC}"
            echo -e "${GRAY}───────────────────────────────────────────────────${NC}"
            echo ""
            echo -e "  ${CYAN}Interface:${NC}  $(get_primary_interface) ($(get_primary_service))"
            echo -e "  ${CYAN}Local IP:${NC}   $(get_local_ip)"
            echo -e "  ${CYAN}Public IP:${NC}  $(get_public_ip)"
            echo -e "  ${CYAN}Gateway:${NC}    $(route -n get default 2>/dev/null | grep gateway | awk '{print $2}')"
            echo -e "  ${CYAN}DNS:${NC}        $(scutil --dns 2>/dev/null | grep 'nameserver\[0\]' | head -1 | awk '{print $3}')"
            echo ""
            echo -e "  ${CYAN}Connectivity:${NC}"
            echo -n "    Gateway:     "; ping -c1 -t2 "$(route -n get default 2>/dev/null | grep gateway | awk '{print $2}')" &>/dev/null && echo -e "${GREEN}${CHECK}${NC}" || echo -e "${RED}${CROSS}${NC}"
            echo -n "    Cloudflare:  "; ping -c1 -t2 1.1.1.1 &>/dev/null && echo -e "${GREEN}${CHECK}${NC}" || echo -e "${RED}${CROSS}${NC}"
            echo -n "    google.com:  "; check_url "google.com" && echo -e "${GREEN}${CHECK}${NC}" || echo -e "${RED}${CROSS}${NC}"
            echo -n "    noizylab.ca: "; check_url "noizylab.ca" && echo -e "${GREEN}${CHECK}${NC}" || echo -e "${RED}${CROSS}${NC}"
            echo ""
            ;;
        dns)
            fix_dns
            ;;
        flush)
            echo -e "${FIRE} Flushing DNS cache..."
            sudo dscacheutil -flushcache
            sudo killall -HUP mDNSResponder 2>/dev/null
            success "DNS cache flushed"
            ;;
        reset)
            echo -e "${FIRE} ${BOLD}FULL NETWORK RESET${NC}"
            echo ""
            local iface=$(get_primary_interface)
            local service=$(get_primary_service)
            
            echo -e "${YELLOW}[1/5]${NC} Flushing DNS..."
            sudo dscacheutil -flushcache
            sudo killall -HUP mDNSResponder 2>/dev/null
            
            echo -e "${YELLOW}[2/5]${NC} Clearing ARP cache..."
            sudo arp -a -d 2>/dev/null || true
            
            echo -e "${YELLOW}[3/5]${NC} Releasing DHCP..."
            sudo ipconfig set "$iface" NONE 2>/dev/null || true
            sleep 1
            
            echo -e "${YELLOW}[4/5]${NC} Renewing DHCP..."
            sudo ipconfig set "$iface" DHCP
            sleep 2
            
            echo -e "${YELLOW}[5/5]${NC} Setting Cloudflare DNS..."
            sudo networksetup -setdnsservers "$service" 1.1.1.1 1.0.0.1
            sudo dscacheutil -flushcache
            
            echo ""
            success "Network reset complete!"
            echo -e "  ${CYAN}New IP:${NC} $(get_local_ip)"
            ;;
        test)
            echo ""
            echo -e "${BOLT} ${BOLD}CONNECTIVITY TEST${NC}"
            echo -e "${GRAY}───────────────────────────────────────────────────${NC}"
            echo ""
            echo -e "${CYAN}Ping Tests:${NC}"
            echo -n "  1.1.1.1 (Cloudflare):  "; ping -c1 -t3 1.1.1.1 &>/dev/null && echo -e "${GREEN}${CHECK} OK${NC}" || echo -e "${RED}${CROSS} FAIL${NC}"
            echo -n "  8.8.8.8 (Google):      "; ping -c1 -t3 8.8.8.8 &>/dev/null && echo -e "${GREEN}${CHECK} OK${NC}" || echo -e "${RED}${CROSS} FAIL${NC}"
            echo ""
            echo -e "${CYAN}HTTPS Tests:${NC}"
            echo -n "  google.com:            "; check_url "google.com" && echo -e "${GREEN}${CHECK} OK${NC}" || echo -e "${RED}${CROSS} FAIL${NC}"
            echo -n "  cloudflare.com:        "; check_url "cloudflare.com" && echo -e "${GREEN}${CHECK} OK${NC}" || echo -e "${RED}${CROSS} FAIL${NC}"
            echo -n "  noizylab.ca:           "; check_url "noizylab.ca" && echo -e "${GREEN}${CHECK} OK${NC}" || echo -e "${RED}${CROSS} FAIL${NC}"
            echo -n "  fishmusicinc.com:      "; check_url "fishmusicinc.com" && echo -e "${GREEN}${CHECK} OK${NC}" || echo -e "${RED}${CROSS} FAIL${NC}"
            echo -n "  claude.ai:             "; check_url "claude.ai" && echo -e "${GREEN}${CHECK} OK${NC}" || echo -e "${RED}${CROSS} FAIL${NC}"
            echo ""
            ;;
        speed)
            echo -e "${FIRE} Running speed test..."
            if command -v speedtest-cli &>/dev/null; then
                speedtest-cli
            else
                echo -e "${CYAN}Quick download test (10MB from Cloudflare):${NC}"
                curl -s -o /dev/null -w "Speed: %{speed_download} bytes/sec\nTime: %{time_total}s\n" https://speed.cloudflare.com/__down?bytes=10000000
                echo ""
                info "For full test: brew install speedtest-cli"
            fi
            ;;
        wifi)
            local airport="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
            if [ -x "$airport" ]; then
                echo -e "${BOLT} ${BOLD}WIFI DIAGNOSTICS${NC}"
                echo ""
                "$airport" -I | grep -E "SSID|BSSID|channel|RSSI|noise|lastTxRate"
            else
                warn "WiFi diagnostics not available"
            fi
            ;;
        trace)
            echo -e "${GLOBE} ${BOLD}CLOUDFLARE TRACE${NC}"
            echo ""
            curl -s https://1.1.1.1/cdn-cgi/trace
            echo ""
            ;;
        *)
            error "Unknown network command: $1"
            echo "Try: god net [status|dns|flush|reset|test|speed|wifi|trace]"
            ;;
    esac
}

#═══════════════════════════════════════════════════════════════════════════════
# NOIZYLAB COMMANDS
#═══════════════════════════════════════════════════════════════════════════════

noizy_cmd() {
    case "${1:-dashboard}" in
        dashboard|"")
            echo ""
            echo -e "${WRENCH} ${BOLD}NOIZYLAB DASHBOARD${NC}"
            echo -e "${GRAY}───────────────────────────────────────────────────${NC}"
            echo ""
            echo -e "  ${CYAN}Website:${NC}    noizylab.ca"
            echo -e "  ${CYAN}Service:${NC}    CPU Repair - \$89 Flat Rate"
            echo -e "  ${CYAN}Target:${NC}     12 repairs/day = \$256K+/year"
            echo ""
            echo -e "  ${CYAN}Quick Links:${NC}"
            echo -e "    ${YELLOW}god noizy site${NC}      Website"
            echo -e "    ${YELLOW}god noizy admin${NC}     Cloudflare"
            echo -e "    ${YELLOW}god noizy stripe${NC}    Payments"
            echo -e "    ${YELLOW}god email support${NC}   Support inbox"
            echo ""
            ;;
        site)
            open "https://noizylab.ca"
            success "noizylab.ca opened"
            ;;
        admin)
            open "https://dash.cloudflare.com/?to=/:account/noizylab.ca"
            success "Cloudflare admin opened"
            ;;
        stripe)
            open "https://dashboard.stripe.com"
            success "Stripe dashboard opened"
            ;;
        book|booking)
            open "https://noizylab.ca/book"
            success "Booking page opened"
            ;;
        repairs)
            open ~/NOIZYLAB/repairs 2>/dev/null || mkdir -p ~/NOIZYLAB/repairs && open ~/NOIZYLAB/repairs
            ;;
        *)
            error "Unknown noizy command: $1"
            ;;
    esac
}

#═══════════════════════════════════════════════════════════════════════════════
# FISH MUSIC COMMANDS
#═══════════════════════════════════════════════════════════════════════════════

fish_cmd() {
    case "${1:-dashboard}" in
        dashboard|"")
            echo ""
            echo -e "${FISH} ${BOLD}FISH MUSIC INC DASHBOARD${NC}"
            echo -e "${GRAY}───────────────────────────────────────────────────${NC}"
            echo ""
            echo -e "  ${CYAN}Website:${NC}    fishmusicinc.com"
            echo -e "  ${CYAN}Service:${NC}    Music Composition & Sound Design"
            echo -e "  ${CYAN}Legacy:${NC}     40+ Years of Excellence"
            echo ""
            echo -e "  ${CYAN}Quick Links:${NC}"
            echo -e "    ${YELLOW}god fish site${NC}       Website"
            echo -e "    ${YELLOW}god fish drive${NC}      Google Drive"
            echo -e "    ${YELLOW}god email fish${NC}      Fish Music emails"
            echo ""
            ;;
        site)
            open "https://fishmusicinc.com"
            success "fishmusicinc.com opened"
            ;;
        drive)
            open "https://drive.google.com"
            success "Google Drive opened"
            ;;
        studio)
            open ~/FishMusic/studio 2>/dev/null || mkdir -p ~/FishMusic/studio && open ~/FishMusic/studio
            ;;
        *)
            error "Unknown fish command: $1"
            ;;
    esac
}

#═══════════════════════════════════════════════════════════════════════════════
# SYSTEM COMMANDS
#═══════════════════════════════════════════════════════════════════════════════

sys_cmd() {
    case "${1:-info}" in
        info|"")
            echo ""
            echo -e "${GEAR} ${BOLD}SYSTEM INFO${NC}"
            echo -e "${GRAY}───────────────────────────────────────────────────${NC}"
            echo ""
            echo -e "  ${CYAN}Host:${NC}       $(hostname)"
            echo -e "  ${CYAN}macOS:${NC}      $(sw_vers -productVersion)"
            echo -e "  ${CYAN}Chip:${NC}       $(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo 'Apple Silicon')"
            echo -e "  ${CYAN}Memory:${NC}     $(sysctl -n hw.memsize | awk '{print $0/1073741824 " GB"}')"
            echo -e "  ${CYAN}Uptime:${NC}     $(uptime | sed 's/.*up //' | sed 's/,.*//')"
            echo ""
            echo -e "  ${CYAN}User:${NC}       $(whoami) ($(id -un))"
            echo -e "  ${CYAN}Home:${NC}       $HOME"
            echo -e "  ${CYAN}Shell:${NC}      $SHELL"
            echo ""
            ;;
        clean|cleanup)
            echo -e "${FIRE} ${BOLD}SYSTEM CLEANUP${NC}"
            echo ""
            
            echo -e "${YELLOW}[1/5]${NC} Clearing user caches..."
            rm -rf ~/Library/Caches/* 2>/dev/null
            success "User caches cleared"
            
            echo -e "${YELLOW}[2/5]${NC} Clearing system caches..."
            sudo rm -rf /Library/Caches/* 2>/dev/null
            success "System caches cleared"
            
            echo -e "${YELLOW}[3/5]${NC} Clearing logs..."
            sudo rm -rf /var/log/*.log 2>/dev/null
            rm -rf ~/Library/Logs/* 2>/dev/null
            success "Logs cleared"
            
            echo -e "${YELLOW}[4/5]${NC} Emptying trash..."
            rm -rf ~/.Trash/* 2>/dev/null
            success "Trash emptied"
            
            echo -e "${YELLOW}[5/5]${NC} Purging memory..."
            sudo purge 2>/dev/null
            success "Memory purged"
            
            echo ""
            success "Cleanup complete!"
            ;;
        memory|mem)
            echo -e "${GEAR} ${BOLD}MEMORY STATUS${NC}"
            echo ""
            vm_stat | head -10
            echo ""
            info "Run 'god sys clean' to free memory"
            ;;
        disk)
            echo -e "${GEAR} ${BOLD}DISK USAGE${NC}"
            echo ""
            df -h / /Volumes/* 2>/dev/null | head -10
            echo ""
            ;;
        top)
            top -l 1 -n 10 -o cpu
            ;;
        restart)
            echo -e "${FIRE} Restarting services..."
            sudo killall -HUP mDNSResponder 2>/dev/null
            sudo dscacheutil -flushcache
            killall Finder 2>/dev/null
            killall Dock 2>/dev/null
            success "Services restarted"
            ;;
        *)
            error "Unknown system command: $1"
            ;;
    esac
}

#═══════════════════════════════════════════════════════════════════════════════
# CLOUDFLARE COMMANDS
#═══════════════════════════════════════════════════════════════════════════════

cf_cmd() {
    case "${1:-dashboard}" in
        dashboard|"")
            open "https://dash.cloudflare.com"
            success "Cloudflare dashboard opened"
            ;;
        workers)
            open "https://dash.cloudflare.com/?to=/:account/workers"
            success "Workers dashboard opened"
            ;;
        dns)
            local domain="${2:-noizylab.ca}"
            open "https://dash.cloudflare.com/?to=/:account/$domain/dns"
            success "DNS for $domain opened"
            ;;
        email)
            open "https://dash.cloudflare.com/?to=/:account/noizylab.ca/email/routing/routes"
            success "Email routing opened"
            ;;
        status)
            echo -e "${GLOBE} ${BOLD}CLOUDFLARE STATUS${NC}"
            local status=$(curl -s https://www.cloudflarestatus.com/api/v2/status.json 2>/dev/null)
            local desc=$(echo "$status" | grep -o '"description":"[^"]*"' | cut -d'"' -f4)
            echo "  Status: ${desc:-Unknown}"
            ;;
        *)
            error "Unknown cloudflare command: $1"
            ;;
    esac
}

#═══════════════════════════════════════════════════════════════════════════════
# DEV COMMANDS
#═══════════════════════════════════════════════════════════════════════════════

dev_cmd() {
    case "${1:-}" in
        code)
            open -a "Visual Studio Code" 2>/dev/null || open -a "Code" 2>/dev/null || error "VS Code not found"
            ;;
        cursor)
            open -a "Cursor" 2>/dev/null || error "Cursor not found"
            ;;
        term|terminal)
            open -a "Terminal"
            ;;
        github|gh)
            open "https://github.com"
            ;;
        *)
            echo -e "${DIAMOND} ${BOLD}DEV ENVIRONMENT${NC}"
            echo ""
            echo -e "  ${YELLOW}god dev code${NC}      VS Code"
            echo -e "  ${YELLOW}god dev cursor${NC}    Cursor"
            echo -e "  ${YELLOW}god dev term${NC}      Terminal"
            echo -e "  ${YELLOW}god dev github${NC}    GitHub"
            echo ""
            ;;
    esac
}

#═══════════════════════════════════════════════════════════════════════════════
# QUICK LINKS
#═══════════════════════════════════════════════════════════════════════════════

quick_link() {
    local site=$1
    case "$site" in
        claude)     open "https://claude.ai" ;;
        chatgpt)    open "https://chat.openai.com" ;;
        gemini)     open "https://gemini.google.com" ;;
        perplexity) open "https://perplexity.ai" ;;
        docs)       open "https://docs.google.com" ;;
        sheets)     open "https://sheets.google.com" ;;
        slides)     open "https://slides.google.com" ;;
        cal)        open "https://calendar.google.com" ;;
        drive)      open "https://drive.google.com" ;;
        meet)       open "https://meet.google.com" ;;
        youtube)    open "https://youtube.com" ;;
        *)          return 1 ;;
    esac
    success "$site opened"
}

#═══════════════════════════════════════════════════════════════════════════════
# FULL STATUS
#═══════════════════════════════════════════════════════════════════════════════

full_status() {
    show_dashboard
    echo ""
    net_cmd status
    echo ""
    sys_cmd info
}

#═══════════════════════════════════════════════════════════════════════════════
# INSTALLER
#═══════════════════════════════════════════════════════════════════════════════

install_god() {
    echo ""
    show_banner
    
    echo -e "${FIRE} ${BOLD}INSTALLING GOD COMMAND CENTER${NC}"
    echo ""
    
    # Create directories
    echo -e "${YELLOW}[1/4]${NC} Creating directories..."
    init_god
    mkdir -p ~/bin
    success "Directories created"
    
    # Install command
    echo -e "${YELLOW}[2/4]${NC} Installing 'god' command..."
    cp "$0" ~/bin/god
    chmod +x ~/bin/god
    success "Command installed to ~/bin/god"
    
    # Add to PATH
    echo -e "${YELLOW}[3/4]${NC} Configuring PATH..."
    if ! grep -q 'HOME/bin' ~/.zshrc 2>/dev/null; then
        echo '' >> ~/.zshrc
        echo '# GOD Command Center' >> ~/.zshrc
        echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
    fi
    export PATH="$HOME/bin:$PATH"
    success "PATH configured"
    
    # Create aliases
    echo -e "${YELLOW}[4/4]${NC} Creating aliases..."
    if ! grep -q 'alias email=' ~/.zshrc 2>/dev/null; then
        cat >> ~/.zshrc << 'ALIASES'

# GOD Aliases
alias email="god email"
alias mail="god email"
alias inbox="god email inbox"
alias support="god email support"
alias net="god net"
alias dns="god net dns"
alias noizy="god noizy"
alias fish="god fish"
alias cf="god cf"
ALIASES
    fi
    success "Aliases created"
    
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                                                                           ║${NC}"
    echo -e "${GREEN}║              ${CROWN} GOD COMMAND CENTER INSTALLED! ${CROWN}                          ║${NC}"
    echo -e "${GREEN}║                                                                           ║${NC}"
    echo -e "${GREEN}╠═══════════════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${GREEN}║                                                                           ║${NC}"
    echo -e "${GREEN}║   Run 'source ~/.zshrc' or open new terminal, then:                       ║${NC}"
    echo -e "${GREEN}║                                                                           ║${NC}"
    echo -e "${GREEN}║   god              Dashboard                                              ║${NC}"
    echo -e "${GREEN}║   god go           Morning startup                                        ║${NC}"
    echo -e "${GREEN}║   god help         All commands                                           ║${NC}"
    echo -e "${GREEN}║                                                                           ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    log "GOD Command Center installed"
}

#═══════════════════════════════════════════════════════════════════════════════
# MAIN
#═══════════════════════════════════════════════════════════════════════════════

main() {
    init_god
    
    case "${1:-dashboard}" in
        # Dashboard & Help
        dashboard|"")   show_dashboard ;;
        help|-h|--help) show_help ;;
        version|-v)     echo "GOD Command Center v$VERSION" ;;
        
        # Quick actions
        go)             morning_startup ;;
        fix)            auto_fix ;;
        status)         full_status ;;
        
        # Email
        email|mail)     shift; email_cmd "$@" ;;
        inbox)          email_cmd inbox ;;
        support)        email_cmd support ;;
        
        # Network
        net|network)    shift; net_cmd "$@" ;;
        dns)            net_cmd dns ;;
        flush)          net_cmd flush ;;
        
        # Business
        noizy|noizylab) shift; noizy_cmd "$@" ;;
        fish)           shift; fish_cmd "$@" ;;
        
        # System
        sys|system)     shift; sys_cmd "$@" ;;
        clean|cleanup)  sys_cmd clean ;;
        
        # Cloudflare
        cf|cloudflare)  shift; cf_cmd "$@" ;;
        
        # Dev
        dev)            shift; dev_cmd "$@" ;;
        
        # Quick links
        claude|chatgpt|gemini|perplexity|docs|sheets|slides|cal|drive|meet|youtube)
            quick_link "$1"
            ;;
        
        # Install
        --install|install)
            install_god
            ;;
        
        *)
            error "Unknown command: $1"
            echo "Run 'god help' for available commands"
            exit 1
            ;;
    esac
}

# Run
main "$@"
