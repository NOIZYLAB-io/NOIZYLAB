#!/bin/bash
###############################################################################
#  NOIZYLAB BACKUP SCRIPT
#  Comprehensive backup for critical system files and configurations
###############################################################################

set -euo pipefail

# --- CONFIGURATION ---
BACKUP_ROOT="${BACKUP_ROOT:-$HOME/NOIZYLAB_BACKUPS}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$BACKUP_ROOT/$TIMESTAMP"
LOG_FILE="$BACKUP_ROOT/backup.log"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# --- SETUP ---
mkdir -p "$BACKUP_DIR"
mkdir -p "$BACKUP_ROOT"

echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${GREEN}NOIZYLAB BACKUP - $TIMESTAMP${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""

log "Starting backup to $BACKUP_DIR"

# --- BACKUP FUNCTIONS ---

backup_zsh_config() {
    log "Backing up ZSH configuration..."
    mkdir -p "$BACKUP_DIR/zsh"

    cp "$HOME/.zshrc" "$BACKUP_DIR/zsh/" 2>/dev/null || true
    cp -r "$HOME/.config/zsh" "$BACKUP_DIR/zsh/config" 2>/dev/null || true

    echo -e "${GREEN}[OK] ZSH config backed up${NC}"
}

backup_secrets() {
    log "Backing up secrets (encrypted)..."
    mkdir -p "$BACKUP_DIR/secrets"

    if [ -f "$HOME/.env.secrets" ]; then
        # Create encrypted backup
        if command -v openssl &>/dev/null; then
            openssl enc -aes-256-cbc -salt -pbkdf2 \
                -in "$HOME/.env.secrets" \
                -out "$BACKUP_DIR/secrets/env.secrets.enc" \
                -pass pass:"noizylab_$TIMESTAMP" 2>/dev/null || \
            cp "$HOME/.env.secrets" "$BACKUP_DIR/secrets/env.secrets"
            echo -e "${GREEN}[OK] Secrets backed up (encrypted)${NC}"
        else
            cp "$HOME/.env.secrets" "$BACKUP_DIR/secrets/env.secrets"
            chmod 600 "$BACKUP_DIR/secrets/env.secrets"
            echo -e "${YELLOW}[OK] Secrets backed up (not encrypted)${NC}"
        fi
    fi
}

backup_gabriel() {
    log "Backing up GABRIEL core files..."
    mkdir -p "$BACKUP_DIR/gabriel"

    # Core Python files
    cp "$HOME/NOIZYLAB/GABRIEL/gabriel.py" "$BACKUP_DIR/gabriel/" 2>/dev/null || true
    cp "$HOME/NOIZYLAB/GABRIEL/gorunfree" "$BACKUP_DIR/gabriel/" 2>/dev/null || true
    cp "$HOME/NOIZYLAB/GABRIEL/codemaster.py" "$BACKUP_DIR/gabriel/" 2>/dev/null || true

    # Config files
    cp -r "$HOME/NOIZYLAB/GABRIEL/config" "$BACKUP_DIR/gabriel/" 2>/dev/null || true

    # Scripts
    cp -r "$HOME/NOIZYLAB/GABRIEL/scripts" "$BACKUP_DIR/gabriel/" 2>/dev/null || true

    echo -e "${GREEN}[OK] GABRIEL core backed up${NC}"
}

backup_claude_config() {
    log "Backing up Claude configuration..."
    mkdir -p "$BACKUP_DIR/claude"

    cp "$HOME/CLAUDE.md" "$BACKUP_DIR/claude/" 2>/dev/null || true
    cp "$HOME/NOIZYLAB/CLAUDE.md" "$BACKUP_DIR/claude/NOIZYLAB_CLAUDE.md" 2>/dev/null || true
    cp -r "$HOME/.claude/settings.json" "$BACKUP_DIR/claude/" 2>/dev/null || true
    cp -r "$HOME/.claude/settings.local.json" "$BACKUP_DIR/claude/" 2>/dev/null || true

    echo -e "${GREEN}[OK] Claude config backed up${NC}"
}

backup_git_config() {
    log "Backing up Git configuration..."
    mkdir -p "$BACKUP_DIR/git"

    cp "$HOME/.gitconfig" "$BACKUP_DIR/git/" 2>/dev/null || true
    cp "$HOME/.gitignore" "$BACKUP_DIR/git/global_gitignore" 2>/dev/null || true

    echo -e "${GREEN}[OK] Git config backed up${NC}"
}

backup_ssh_config() {
    log "Backing up SSH configuration..."
    mkdir -p "$BACKUP_DIR/ssh"

    cp "$HOME/.ssh/config" "$BACKUP_DIR/ssh/" 2>/dev/null || true
    cp "$HOME/.ssh/known_hosts" "$BACKUP_DIR/ssh/" 2>/dev/null || true
    # Note: NOT backing up private keys for security

    echo -e "${GREEN}[OK] SSH config backed up (keys excluded)${NC}"
}

backup_homebrew() {
    log "Backing up Homebrew packages list..."
    mkdir -p "$BACKUP_DIR/homebrew"

    if command -v brew &>/dev/null; then
        brew list --formula > "$BACKUP_DIR/homebrew/formulae.txt" 2>/dev/null || true
        brew list --cask > "$BACKUP_DIR/homebrew/casks.txt" 2>/dev/null || true
        brew bundle dump --file="$BACKUP_DIR/homebrew/Brewfile" 2>/dev/null || true
        echo -e "${GREEN}[OK] Homebrew packages listed${NC}"
    else
        echo -e "${YELLOW}[--] Homebrew not installed${NC}"
    fi
}

backup_vscode() {
    log "Backing up VSCode settings..."
    mkdir -p "$BACKUP_DIR/vscode"

    VSCODE_DIR="$HOME/Library/Application Support/Code/User"
    if [ -d "$VSCODE_DIR" ]; then
        cp "$VSCODE_DIR/settings.json" "$BACKUP_DIR/vscode/" 2>/dev/null || true
        cp "$VSCODE_DIR/keybindings.json" "$BACKUP_DIR/vscode/" 2>/dev/null || true
        code --list-extensions > "$BACKUP_DIR/vscode/extensions.txt" 2>/dev/null || true
        echo -e "${GREEN}[OK] VSCode settings backed up${NC}"
    else
        echo -e "${YELLOW}[--] VSCode not found${NC}"
    fi
}

create_manifest() {
    log "Creating backup manifest..."

    cat > "$BACKUP_DIR/MANIFEST.md" << EOF
# NOIZYLAB Backup Manifest

**Created:** $(date '+%Y-%m-%d %H:%M:%S')
**Hostname:** $(hostname)
**User:** $(whoami)

## Contents

- \`zsh/\` - ZSH configuration files
- \`secrets/\` - Encrypted API keys and tokens
- \`gabriel/\` - GABRIEL core files and scripts
- \`claude/\` - Claude configuration
- \`git/\` - Git configuration
- \`ssh/\` - SSH configuration (keys excluded)
- \`homebrew/\` - Package lists and Brewfile
- \`vscode/\` - VSCode settings and extensions

## Restore Instructions

1. Copy files to their respective locations
2. For secrets: \`openssl enc -aes-256-cbc -d -pbkdf2 -in env.secrets.enc -out ~/.env.secrets\`
3. For Homebrew: \`brew bundle --file=Brewfile\`
4. For VSCode: \`cat extensions.txt | xargs -L 1 code --install-extension\`

## Backup Size

$(du -sh "$BACKUP_DIR" | cut -f1)
EOF

    echo -e "${GREEN}[OK] Manifest created${NC}"
}

cleanup_old_backups() {
    log "Cleaning up old backups (keeping last 10)..."

    cd "$BACKUP_ROOT"
    ls -dt */ 2>/dev/null | tail -n +11 | xargs rm -rf 2>/dev/null || true

    echo -e "${GREEN}[OK] Old backups cleaned${NC}"
}

# --- MAIN ---
backup_zsh_config
backup_secrets
backup_gabriel
backup_claude_config
backup_git_config
backup_ssh_config
backup_homebrew
backup_vscode
create_manifest
cleanup_old_backups

# --- SUMMARY ---
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${GREEN}BACKUP COMPLETE${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""
echo "Location: $BACKUP_DIR"
echo "Size: $(du -sh "$BACKUP_DIR" | cut -f1)"
echo ""
log "Backup completed successfully"
