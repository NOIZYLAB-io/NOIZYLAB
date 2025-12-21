# ============================================================================
# 10_functions.zsh - Shell Functions & Logic
# ============================================================================

# --- AI HELPERS ---
# --- AI HELPERS ---
# 'ask' is now a binary in ~/bin/ask
code() { ask "Generate code for: $*" | colout -l python 2>/dev/null || cat; }
rrsay() { "$HOME/rr.sh" infer "$*"; }

# --- FILE ORGANIZATION ---
organize-by-type() {
    local target_dir="${1:-.}"
    echo "📂 Creating organization structure in $target_dir..."
    mkdir -p "$target_dir/_ORGANIZED/BY_TYPE"/{PYTHON,JAVASCRIPT,JSON,TYPESCRIPT,SHELL,DOCS,OTHER}
    
    find "$target_dir" -maxdepth 1 -type f -name "*.py" -exec mv {} "$target_dir/_ORGANIZED/BY_TYPE/PYTHON/" \; 2>/dev/null
    find "$target_dir" -maxdepth 1 -type f -name "*.json" -exec mv {} "$target_dir/_ORGANIZED/BY_TYPE/JSON/" \; 2>/dev/null
    find "$target_dir" -maxdepth 1 -type f -name "*.js" -exec mv {} "$target_dir/_ORGANIZED/BY_TYPE/JAVASCRIPT/" \; 2>/dev/null
    find "$target_dir" -maxdepth 1 -type f -name "*.ts" -exec mv {} "$target_dir/_ORGANIZED/BY_TYPE/TYPESCRIPT/" \; 2>/dev/null
    find "$target_dir" -maxdepth 1 -type f -name "*.sh" -exec mv {} "$target_dir/_ORGANIZED/BY_TYPE/SHELL/" \; 2>/dev/null
    find "$target_dir" -maxdepth 1 -type f -name "*.md" -exec mv {} "$target_dir/_ORGANIZED/BY_TYPE/DOCS/" \; 2>/dev/null
    
    echo "✅ Organization complete!"
}

# --- SYNC ---
sync-drives() {
    echo "🔄 Syncing all NOIZYLAB drives..."
    rsync -av --progress --delete "$NOIZYLAB_HOME/" "$DRIVE_RSP/NOISYLABZ/backup/" 2>&1 | tail -10
}

# --- DASHBOARD ---
dashboard() {
    clear
    echo "╔════════════════════════════════════════════════════════╗"
    echo "║        🎯 NOIZYLAB DEVELOPMENT DASHBOARD 🎯           ║"
    echo "╚════════════════════════════════════════════════════════╝"
    echo ""
    echo "📍 System:"
    echo "   Computer: $(scutil --get ComputerName)"
    echo "   IP: $(ipconfig getifaddr en0)"
    echo ""
    echo "🚀 Quick Launch Commands:"
    echo "   noizy     - God Mode"
    echo "   nd, rd    - Navigate Drives"
    echo "   gpush     - Git Push"
    echo "   dashboard - Show this dashboard"
    echo ""
}
