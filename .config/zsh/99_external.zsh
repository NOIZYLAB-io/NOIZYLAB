# ============================================================================
# 99_external.zsh - Third Party Integrations
# ============================================================================

# --- Windsurf ---
export PATH="/Users/m2ultra/.codeium/windsurf/bin:$PATH"

# --- Antigravity ---
export PATH="/Users/m2ultra/.antigravity/antigravity/bin:$PATH"

# --- Antigravity Brain Integrations ---
if [ -f "/Users/m2ultra/.gemini/antigravity/brain/10fbcc11-34da-430e-a226-19c05f0cf69d/terminal_velocity.zsh" ]; then
    source "/Users/m2ultra/.gemini/antigravity/brain/10fbcc11-34da-430e-a226-19c05f0cf69d/terminal_velocity.zsh"
fi

# Hot Rod Settings
if [ -f "/Users/m2ultra/.gemini/antigravity/scratch/hot_rod_settings.zsh" ]; then
    source "/Users/m2ultra/.gemini/antigravity/scratch/hot_rod_settings.zsh"
fi

# --- Homebrew (Ensure it's loaded last to override system if needed) ---
if [[ -x /opt/homebrew/bin/brew ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi
