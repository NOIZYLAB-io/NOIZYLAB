#!/bin/bash
# ==============================================================================
#
#  ██████╗  ██████╗ ██████╗ ██╗   ██╗███╗   ██╗███████╗██████╗ ███████╗███████╗
# ██╔════╝ ██╔═══██╗██╔══██╗██║   ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔════╝
# ██║  ███╗██║   ██║██████╔╝██║   ██║██╔██╗ ██║█████╗  ██████╔╝█████╗  █████╗
# ██║   ██║██║   ██║██╔══██╗██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝  ██╔══╝
# ╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║     ██║  ██║███████╗███████╗
#  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
#
#                    NOIZYLAB SOVEREIGN IGNITION SEQUENCE
#                    ====================================
#                    The 3mm Miracle Starts Now
#                    Money While You Sleep. GORUNFREE.
#
# ==============================================================================

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
GOLD='\033[38;5;220m'
NC='\033[0m' # No Color

# Paths
SOVEREIGN_ROOT="${HOME}/NOIZYLAB/GABRIEL/sovereign"
VISION_DIR="${SOVEREIGN_ROOT}/vision"
MANIFESTS_DIR="${SOVEREIGN_ROOT}/manifests"
LOGS_DIR="${SOVEREIGN_ROOT}/logs"

# Create directories
mkdir -p "${VISION_DIR}" "${MANIFESTS_DIR}" "${LOGS_DIR}"

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

print_banner() {
    echo -e "${GOLD}"
    cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║  ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗               ║
║  ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗              ║
║  ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝              ║
║  ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗              ║
║  ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝              ║
║  ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝              ║
║                                                                               ║
║                    SOVEREIGN REPAIR PORTAL                                    ║
║                    AI-Powered. Premium. Autonomous.                           ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

log_step() {
    local step=$1
    local message=$2
    echo -e "${CYAN}[${step}]${NC} ${message}"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

check_dependency() {
    local cmd=$1
    if command -v "$cmd" &> /dev/null; then
        log_success "$cmd available"
        return 0
    else
        log_warning "$cmd not found"
        return 1
    fi
}

# ==============================================================================
# SYSTEM CHECKS
# ==============================================================================

run_system_checks() {
    log_step "1" "Running system checks..."

    echo ""
    echo "  Dependencies:"
    check_dependency "python3" || true
    check_dependency "node" || true
    check_dependency "wrangler" || true
    check_dependency "ffmpeg" || true

    echo ""
    echo "  Python packages:"
    python3 -c "import cv2; print('    ✓ OpenCV available')" 2>/dev/null || echo "    ⚠ OpenCV not installed"
    python3 -c "import reportlab; print('    ✓ ReportLab available')" 2>/dev/null || echo "    ⚠ ReportLab not installed"
    python3 -c "import aiohttp; print('    ✓ aiohttp available')" 2>/dev/null || echo "    ⚠ aiohttp not installed"

    echo ""
}

# ==============================================================================
# SERVICE LAUNCHERS
# ==============================================================================

start_sovereign_dashboard() {
    log_step "2" "Starting Sovereign Dashboard..."

    cd "${SOVEREIGN_ROOT}"

    if [ -f "sovereign_dashboard.py" ]; then
        python3 sovereign_dashboard.py &
        DASHBOARD_PID=$!
        echo "    PID: ${DASHBOARD_PID}"
        log_success "Dashboard started"
    else
        log_error "sovereign_dashboard.py not found"
    fi
}

start_vision_pipeline() {
    log_step "3" "Initializing Vision Pipeline..."

    cd "${SOVEREIGN_ROOT}/vision"

    if [ -f "forensic_capture.py" ]; then
        # Don't start as daemon, just verify it's available
        python3 -c "from forensic_capture import ForensicCapture; print('    Vision system ready')"
        log_success "Vision pipeline initialized"
    else
        log_warning "forensic_capture.py not found"
    fi
}

start_manifest_api() {
    log_step "4" "Deploying Manifest API..."

    local WORKER_DIR="${SOVEREIGN_ROOT}/workers/manifest-api"

    if [ -d "${WORKER_DIR}" ]; then
        cd "${WORKER_DIR}"

        # Check if wrangler is available
        if command -v wrangler &> /dev/null; then
            echo "    Checking worker status..."
            wrangler whoami 2>/dev/null || log_warning "Wrangler not authenticated"
            log_success "Manifest API ready (deploy with: wrangler deploy)"
        else
            log_warning "Wrangler not installed - API deployment skipped"
        fi
    else
        log_warning "Manifest API worker directory not found"
    fi
}

start_portal_frontend() {
    log_step "5" "Checking Portal Frontend..."

    local PORTAL_DIR="${HOME}/NOIZYLAB/GABRIEL/portal/frontend"

    if [ -d "${PORTAL_DIR}" ]; then
        cd "${PORTAL_DIR}"

        if [ -f "package.json" ]; then
            echo "    Portal ready at: https://portal.noizylab.ca"
            log_success "Portal frontend configured"
        fi
    else
        log_warning "Portal frontend directory not found"
    fi
}

# ==============================================================================
# DEMO MODE
# ==============================================================================

run_demo() {
    log_step "DEMO" "Running manifest generation demo..."

    cd "${SOVEREIGN_ROOT}"

    echo ""
    python3 manifest_generator.py

    echo ""
    log_success "Demo manifest generated in: ${MANIFESTS_DIR}"
}

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

main() {
    clear
    print_banner

    echo -e "${PURPLE}Initializing Sovereign Repair Portal...${NC}"
    echo ""

    # Run checks
    run_system_checks

    # Parse arguments
    case "${1:-}" in
        --demo)
            run_demo
            ;;
        --dashboard)
            start_sovereign_dashboard
            ;;
        --vision)
            start_vision_pipeline
            ;;
        --api)
            start_manifest_api
            ;;
        --portal)
            start_portal_frontend
            ;;
        --full|"")
            start_vision_pipeline
            start_manifest_api
            start_portal_frontend
            echo ""
            log_step "6" "Sovereign Portal Ready"
            echo ""
            ;;
        --help)
            echo "Usage: ./GORUNFREE.sh [option]"
            echo ""
            echo "Options:"
            echo "  --demo       Run manifest generation demo"
            echo "  --dashboard  Start sovereign dashboard"
            echo "  --vision     Initialize vision pipeline"
            echo "  --api        Deploy manifest API"
            echo "  --portal     Check portal frontend"
            echo "  --full       Start all services (default)"
            echo "  --help       Show this help"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac

    # Play success sound if available
    if [ -f "${HOME}/NOIZYLAB/fish_music/trust_signatures/noizylab_resolve.wav" ]; then
        afplay "${HOME}/NOIZYLAB/fish_music/trust_signatures/noizylab_resolve.wav" 2>/dev/null &
    fi

    echo ""
    echo -e "${GOLD}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GOLD}║                                                                               ║${NC}"
    echo -e "${GOLD}║                    SYSTEM STATUS: 100% SOVEREIGN                              ║${NC}"
    echo -e "${GOLD}║                                                                               ║${NC}"
    echo -e "${GOLD}║                    Money While You Sleep.                                     ║${NC}"
    echo -e "${GOLD}║                    Focus on Flow & Creative Miracles.                         ║${NC}"
    echo -e "${GOLD}║                                                                               ║${NC}"
    echo -e "${GOLD}║                              GORUNFREE!                                       ║${NC}"
    echo -e "${GOLD}║                                                                               ║${NC}"
    echo -e "${GOLD}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# Run
main "$@"
