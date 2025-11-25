#!/bin/bash
#===============================================================================
# NOIZYLAB TOKEN CLI
# Command-line tool for managing API tokens
#===============================================================================

set -e

# Configuration
NOIZYLAB_DIR="$HOME/.noizylab"
CONFIG_FILE="$NOIZYLAB_DIR/token-config.json"
TOKEN_CACHE="$NOIZYLAB_DIR/tokens.json"
VERSION="1.0.0"

# Default API endpoint
API_BASE="${NOIZYLAB_API_URL:-https://noizylab.ca}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

mkdir -p "$NOIZYLAB_DIR"

#===============================================================================
# UTILITIES
#===============================================================================

log() { echo -e "${CYAN}[noizylab]${NC} $1"; }
log_success() { echo -e "${GREEN}✓${NC} $1"; }
log_warning() { echo -e "${YELLOW}!${NC} $1"; }
log_error() { echo -e "${RED}✗${NC} $1"; }

print_banner() {
    echo -e "${PURPLE}${BOLD}"
    cat << 'EOF'
    ╔═══════════════════════════════════════════════════════════╗
    ║   _   _  ___  ___ _______   ___      _    ___             ║
    ║  | \ | |/ _ \|_ _|__  /\ \ / / |    / \  | __ )           ║
    ║  |  \| | | | || |  / /  \ V /| |   / _ \ |  _ \           ║
    ║  | |\  | |_| || | / /_   | | | |__/ ___ \| |_) |          ║
    ║  |_| \_|\___/|___/____|  |_| |____/_/   \_\____/          ║
    ║                                                           ║
    ║              TOKEN MANAGEMENT CLI v1.0                    ║
    ╚═══════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# Check for required tools
check_dependencies() {
    local missing=()

    if ! command -v curl &>/dev/null; then
        missing+=("curl")
    fi

    if ! command -v jq &>/dev/null; then
        missing+=("jq")
    fi

    if [ ${#missing[@]} -gt 0 ]; then
        log_error "Missing required tools: ${missing[*]}"
        echo "Install with: brew install ${missing[*]}"
        exit 1
    fi
}

# Load configuration
load_config() {
    if [ -f "$CONFIG_FILE" ]; then
        API_BASE=$(jq -r '.api_base // "https://noizylab.ca"' "$CONFIG_FILE")
        ADMIN_TOKEN=$(jq -r '.admin_token // ""' "$CONFIG_FILE")
    fi
}

# Save configuration
save_config() {
    cat > "$CONFIG_FILE" << EOF
{
    "api_base": "$API_BASE",
    "admin_token": "$ADMIN_TOKEN",
    "updated_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF
    chmod 600 "$CONFIG_FILE"
}

# API request helper
api_request() {
    local method="$1"
    local endpoint="$2"
    local data="$3"

    local headers=(-H "Content-Type: application/json")

    if [ -n "$ADMIN_TOKEN" ]; then
        headers+=(-H "Authorization: Bearer $ADMIN_TOKEN")
    fi

    local url="${API_BASE}${endpoint}"

    if [ -n "$data" ]; then
        curl -s -X "$method" "$url" "${headers[@]}" -d "$data"
    else
        curl -s -X "$method" "$url" "${headers[@]}"
    fi
}

#===============================================================================
# COMMANDS
#===============================================================================

cmd_configure() {
    print_banner
    echo -e "${CYAN}Configure NOIZYLAB Token CLI${NC}"
    echo ""

    # API Base URL
    echo -n "API Base URL [$API_BASE]: "
    read -r input_url
    if [ -n "$input_url" ]; then
        API_BASE="$input_url"
    fi

    # Admin Token
    echo -n "Admin Token: "
    read -rs input_token
    echo ""
    if [ -n "$input_token" ]; then
        ADMIN_TOKEN="$input_token"
    fi

    save_config
    log_success "Configuration saved to $CONFIG_FILE"
}

cmd_login() {
    local email="$1"
    local password="$2"

    if [ -z "$email" ]; then
        echo -n "Email: "
        read -r email
    fi

    if [ -z "$password" ]; then
        echo -n "Password: "
        read -rs password
        echo ""
    fi

    log "Authenticating..."

    local response
    response=$(api_request POST "/admin/login" "{\"email\":\"$email\",\"password\":\"$password\"}")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        ADMIN_TOKEN=$(echo "$response" | jq -r '.data.session.token')
        save_config
        log_success "Logged in successfully!"

        local user_name
        user_name=$(echo "$response" | jq -r '.data.user.name')
        echo -e "Welcome, ${CYAN}$user_name${NC}!"
    else
        local error
        error=$(echo "$response" | jq -r '.error // "Login failed"')
        log_error "$error"
        exit 1
    fi
}

cmd_logout() {
    if [ -z "$ADMIN_TOKEN" ]; then
        log_warning "Not logged in"
        return
    fi

    api_request POST "/admin/logout" &>/dev/null
    ADMIN_TOKEN=""
    save_config
    log_success "Logged out successfully"
}

cmd_whoami() {
    if [ -z "$ADMIN_TOKEN" ]; then
        log_error "Not logged in. Run: noizylab-token login"
        exit 1
    fi

    local response
    response=$(api_request GET "/admin/me")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        echo -e "${CYAN}Current User:${NC}"
        echo "$response" | jq -r '.data.user | "  Name: \(.name)\n  Email: \(.email)\n  Role: \(.role)\n  2FA: \(if .twoFactorEnabled then "Enabled" else "Disabled" end)"'
    else
        log_error "Failed to get user info"
    fi
}

cmd_list() {
    log "Fetching tokens..."

    local response
    response=$(api_request GET "/tokens?includeInactive=true")

    if ! echo "$response" | jq -e '.success' &>/dev/null; then
        log_error "Failed to fetch tokens"
        exit 1
    fi

    local count
    count=$(echo "$response" | jq -r '.data.total')

    echo ""
    echo -e "${CYAN}${BOLD}API Tokens${NC} (${count} total)"
    echo -e "${DIM}────────────────────────────────────────────────────────────${NC}"

    if [ "$count" = "0" ]; then
        echo -e "  ${DIM}No tokens found. Create one with: noizylab-token create${NC}"
        return
    fi

    echo "$response" | jq -r '.data.tokens[] |
        if .isActive then "\u001b[32m● Active\u001b[0m" else "\u001b[31m○ Inactive\u001b[0m" end +
        "  " + .name +
        "\n    ID: " + .id +
        "\n    Key: " + .keyPrefix +
        "\n    Scopes: " + (.scopes | join(", ")) +
        "\n    Created: " + .createdAt +
        "\n"'
}

cmd_create() {
    local name=""
    local scopes=""
    local expires=""
    local ratelimit=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --name|-n)
                name="$2"
                shift 2
                ;;
            --scopes|-s)
                scopes="$2"
                shift 2
                ;;
            --expires|-e)
                expires="$2"
                shift 2
                ;;
            --ratelimit|-r)
                ratelimit="$2"
                shift 2
                ;;
            *)
                shift
                ;;
        esac
    done

    # Interactive mode if no arguments
    if [ -z "$name" ]; then
        echo -e "${CYAN}Create New Token${NC}"
        echo ""

        echo -n "Token Name: "
        read -r name

        echo ""
        echo "Available Scopes:"
        echo "  1. email:send      - Send emails"
        echo "  2. email:read      - Read email logs"
        echo "  3. templates:read  - Read templates"
        echo "  4. templates:write - Create/update templates"
        echo "  5. analytics:read  - View analytics"
        echo "  6. webhooks:manage - Manage webhooks"
        echo "  7. batch:send      - Send batch emails"
        echo "  8. api-keys:manage - Manage API keys"
        echo ""
        echo -n "Scopes (comma-separated numbers, e.g., 1,2,3): "
        read -r scope_nums

        # Convert numbers to scope names
        local scope_map=("email:send" "email:read" "templates:read" "templates:write" "analytics:read" "webhooks:manage" "batch:send" "api-keys:manage")
        local selected_scopes=()

        IFS=',' read -ra nums <<< "$scope_nums"
        for num in "${nums[@]}"; do
            num=$(echo "$num" | tr -d ' ')
            if [[ "$num" =~ ^[1-8]$ ]]; then
                selected_scopes+=("${scope_map[$((num-1))]}")
            fi
        done

        scopes=$(IFS=','; echo "${selected_scopes[*]}")

        echo ""
        echo -n "Expires in days (empty for no expiry): "
        read -r expires

        echo -n "Rate limit (requests/hour, empty for default): "
        read -r ratelimit
    fi

    if [ -z "$name" ] || [ -z "$scopes" ]; then
        log_error "Name and scopes are required"
        exit 1
    fi

    # Build JSON payload
    local scopes_array
    scopes_array=$(echo "$scopes" | tr ',' '\n' | jq -R . | jq -s .)

    local payload="{\"name\":\"$name\",\"scopes\":$scopes_array"

    if [ -n "$expires" ]; then
        payload+=",\"expiresInDays\":$expires"
    fi

    if [ -n "$ratelimit" ]; then
        payload+=",\"rateLimit\":$ratelimit"
    fi

    payload+="}"

    log "Creating token..."

    local response
    response=$(api_request POST "/tokens" "$payload")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        echo ""
        log_success "Token created successfully!"
        echo ""

        local raw_key
        raw_key=$(echo "$response" | jq -r '.data.rawKey')
        local token_id
        token_id=$(echo "$response" | jq -r '.data.token.id')

        echo -e "${YELLOW}${BOLD}⚠️  IMPORTANT: Save this token now!${NC}"
        echo -e "${YELLOW}It will only be shown once and cannot be retrieved later.${NC}"
        echo ""
        echo -e "${CYAN}Token ID:${NC} $token_id"
        echo -e "${CYAN}API Token:${NC}"
        echo ""
        echo -e "  ${GREEN}${BOLD}$raw_key${NC}"
        echo ""

        # Copy to clipboard if available
        if command -v pbcopy &>/dev/null; then
            echo "$raw_key" | pbcopy
            log_success "Token copied to clipboard!"
        elif command -v xclip &>/dev/null; then
            echo "$raw_key" | xclip -selection clipboard
            log_success "Token copied to clipboard!"
        fi

        # Save to local cache
        echo "$response" | jq '.data.token' >> "$TOKEN_CACHE"
    else
        local error
        error=$(echo "$response" | jq -r '.error.message // "Failed to create token"')
        log_error "$error"
        exit 1
    fi
}

cmd_revoke() {
    local token_id="$1"

    if [ -z "$token_id" ]; then
        echo -n "Token ID to revoke: "
        read -r token_id
    fi

    echo -e "${YELLOW}Are you sure you want to revoke token $token_id?${NC}"
    echo -n "This will immediately stop all API access. (y/N): "
    read -r confirm

    if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
        log "Cancelled"
        return
    fi

    log "Revoking token..."

    local response
    response=$(api_request POST "/tokens/$token_id/revoke")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        log_success "Token revoked successfully"
    else
        local error
        error=$(echo "$response" | jq -r '.error.message // "Failed to revoke token"')
        log_error "$error"
        exit 1
    fi
}

cmd_rotate() {
    local token_id="$1"

    if [ -z "$token_id" ]; then
        echo -n "Token ID to rotate: "
        read -r token_id
    fi

    echo -e "${YELLOW}This will create a new token and deactivate the old one.${NC}"
    echo -n "Continue? (y/N): "
    read -r confirm

    if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
        log "Cancelled"
        return
    fi

    log "Rotating token..."

    local response
    response=$(api_request POST "/tokens/$token_id/rotate")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        echo ""
        log_success "Token rotated successfully!"
        echo ""

        local raw_key
        raw_key=$(echo "$response" | jq -r '.data.rawKey')
        local new_id
        new_id=$(echo "$response" | jq -r '.data.token.id')

        echo -e "${YELLOW}${BOLD}⚠️  IMPORTANT: Save this new token now!${NC}"
        echo -e "${YELLOW}The old token has been deactivated.${NC}"
        echo ""
        echo -e "${CYAN}New Token ID:${NC} $new_id"
        echo -e "${CYAN}Old Token ID:${NC} $token_id (deactivated)"
        echo -e "${CYAN}New API Token:${NC}"
        echo ""
        echo -e "  ${GREEN}${BOLD}$raw_key${NC}"
        echo ""

        # Copy to clipboard
        if command -v pbcopy &>/dev/null; then
            echo "$raw_key" | pbcopy
            log_success "New token copied to clipboard!"
        fi
    else
        local error
        error=$(echo "$response" | jq -r '.error.message // "Failed to rotate token"')
        log_error "$error"
        exit 1
    fi
}

cmd_info() {
    local token_id="$1"

    if [ -z "$token_id" ]; then
        echo -n "Token ID: "
        read -r token_id
    fi

    log "Fetching token info..."

    local response
    response=$(api_request GET "/tokens/$token_id")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        echo ""
        echo -e "${CYAN}${BOLD}Token Details${NC}"
        echo -e "${DIM}────────────────────────────────────────${NC}"

        echo "$response" | jq -r '.data.token |
            "Name: " + .name +
            "\nID: " + .id +
            "\nKey Prefix: " + .keyPrefix +
            "\nStatus: " + (if .isActive then "Active" else "Inactive" end) +
            "\nScopes: " + (.scopes | join(", ")) +
            "\nCreated: " + .createdAt +
            "\nLast Used: " + (.lastUsedAt // "Never") +
            "\nExpires: " + (.expiresAt // "Never")'

        echo ""
        echo -e "${CYAN}${BOLD}Usage Statistics${NC}"
        echo -e "${DIM}────────────────────────────────────────${NC}"

        echo "$response" | jq -r '.data.stats // {} |
            "Total Requests: " + (.totalRequests // 0 | tostring) +
            "\nLast 24h: " + (.last24Hours // 0 | tostring) +
            "\nLast 7d: " + (.last7Days // 0 | tostring) +
            "\nLast 30d: " + (.last30Days // 0 | tostring)'
    else
        local error
        error=$(echo "$response" | jq -r '.error.message // "Token not found"')
        log_error "$error"
        exit 1
    fi
}

cmd_test() {
    local token="$1"

    if [ -z "$token" ]; then
        echo -n "API Token to test: "
        read -r token
    fi

    log "Testing token..."

    local response
    response=$(curl -s -X GET "${API_BASE}/health" -H "Authorization: Bearer $token")

    if echo "$response" | jq -e '.status == "healthy"' &>/dev/null; then
        log_success "Token is valid and working!"
        echo ""
        echo "$response" | jq '.data'
    else
        log_error "Token test failed"
        echo "$response" | jq '.'
    fi
}

cmd_scopes() {
    log "Fetching available scopes..."

    local response
    response=$(api_request GET "/tokens/scopes")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        echo ""
        echo -e "${CYAN}${BOLD}Available Scopes${NC}"
        echo -e "${DIM}────────────────────────────────────────────────────────────${NC}"

        echo "$response" | jq -r '.data.scopes[] | "  \(.scope)\n    └─ \(.description)\n"'
    else
        log_error "Failed to fetch scopes"
    fi
}

cmd_audit() {
    local token_id="$1"
    local limit="${2:-20}"

    log "Fetching audit log..."

    local endpoint="/tokens/audit/log?limit=$limit"
    if [ -n "$token_id" ]; then
        endpoint+="&tokenId=$token_id"
    fi

    local response
    response=$(api_request GET "$endpoint")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        echo ""
        echo -e "${CYAN}${BOLD}Token Audit Log${NC}"
        echo -e "${DIM}────────────────────────────────────────────────────────────${NC}"

        local count
        count=$(echo "$response" | jq -r '.data.total')

        if [ "$count" = "0" ]; then
            echo "  No audit events found"
            return
        fi

        echo "$response" | jq -r '.data.logs[] |
            "[\(.timestamp)] \(.event)\n  Token: \(.tokenId // .newTokenId // "N/A")\n  IP: \(.ip)\n  By: \(.createdBy // .revokedBy // .rotatedBy // "system")\n"'
    else
        log_error "Failed to fetch audit log"
    fi
}

cmd_export() {
    local format="${1:-json}"
    local output="${2:-tokens-export}"

    log "Exporting tokens..."

    local response
    response=$(api_request GET "/tokens?includeInactive=true")

    if echo "$response" | jq -e '.success' &>/dev/null; then
        case "$format" in
            json)
                echo "$response" | jq '.data.tokens' > "${output}.json"
                log_success "Exported to ${output}.json"
                ;;
            csv)
                echo "id,name,status,scopes,created_at,last_used,expires_at" > "${output}.csv"
                echo "$response" | jq -r '.data.tokens[] |
                    [.id, .name, (if .isActive then "active" else "inactive" end),
                    (.scopes | join(";")), .createdAt, (.lastUsedAt // ""), (.expiresAt // "")] | @csv' >> "${output}.csv"
                log_success "Exported to ${output}.csv"
                ;;
            *)
                log_error "Unknown format: $format (use json or csv)"
                ;;
        esac
    else
        log_error "Failed to export tokens"
    fi
}

cmd_help() {
    print_banner
    echo "Usage: noizylab-token <command> [options]"
    echo ""
    echo "Commands:"
    echo "  configure          Configure CLI settings"
    echo "  login [email]      Login to admin dashboard"
    echo "  logout             Logout from admin dashboard"
    echo "  whoami             Show current user info"
    echo ""
    echo "  list               List all API tokens"
    echo "  create             Create a new API token"
    echo "  info <id>          Show token details and stats"
    echo "  revoke <id>        Revoke/deactivate a token"
    echo "  rotate <id>        Rotate a token (create new, deactivate old)"
    echo "  test <token>       Test if a token is valid"
    echo ""
    echo "  scopes             List available scopes"
    echo "  audit [id]         View token audit log"
    echo "  export [format]    Export tokens (json/csv)"
    echo ""
    echo "  help               Show this help message"
    echo "  version            Show version"
    echo ""
    echo "Options for 'create':"
    echo "  --name, -n         Token name"
    echo "  --scopes, -s       Comma-separated scopes"
    echo "  --expires, -e      Expiration in days"
    echo "  --ratelimit, -r    Rate limit (requests/hour)"
    echo ""
    echo "Examples:"
    echo "  noizylab-token configure"
    echo "  noizylab-token login admin@noizylab.ca"
    echo "  noizylab-token create --name 'My App' --scopes 'email:send,email:read'"
    echo "  noizylab-token list"
    echo "  noizylab-token revoke tok_abc123"
    echo "  noizylab-token export csv"
    echo ""
    echo "Environment:"
    echo "  NOIZYLAB_API_URL   API base URL (default: https://noizylab.ca)"
}

cmd_version() {
    echo "noizylab-token version $VERSION"
}

#===============================================================================
# MAIN
#===============================================================================

main() {
    check_dependencies
    load_config

    local command="${1:-help}"
    shift || true

    case "$command" in
        configure|config)
            cmd_configure "$@"
            ;;
        login)
            cmd_login "$@"
            ;;
        logout)
            cmd_logout
            ;;
        whoami|me)
            cmd_whoami
            ;;
        list|ls)
            cmd_list
            ;;
        create|new)
            cmd_create "$@"
            ;;
        info|show|get)
            cmd_info "$@"
            ;;
        revoke|deactivate)
            cmd_revoke "$@"
            ;;
        rotate)
            cmd_rotate "$@"
            ;;
        test|verify)
            cmd_test "$@"
            ;;
        scopes)
            cmd_scopes
            ;;
        audit|log)
            cmd_audit "$@"
            ;;
        export)
            cmd_export "$@"
            ;;
        help|-h|--help)
            cmd_help
            ;;
        version|-v|--version)
            cmd_version
            ;;
        *)
            log_error "Unknown command: $command"
            echo "Run 'noizylab-token help' for usage"
            exit 1
            ;;
    esac
}

main "$@"
