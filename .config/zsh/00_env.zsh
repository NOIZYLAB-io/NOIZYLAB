# ============================================================================
# 00_env.zsh - Environment Variables & Secrets
# ============================================================================

# --- GOD Command Center ---
export PATH="$HOME/bin:$PATH"
export PATH="/opt/homebrew/bin:$PATH"
export PATH="/Users/m2ultra/scripts/mail_manager_pro/bin:$PATH"

# --- API KEYS ---
# OpenAI (Project Key)
export OPENAI_API_KEY="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"
# Anthropic
export ANTHROPIC_API_KEY="your_correct_key"

# --- NOIZYLAB CORE ---
export NOIZYLAB_HOME="/Users/m2ultra/.claude-worktrees/NOIZYLAB/upbeat-moore"
export RR_ROOT="$HOME/NOIZYLAB_GIT_STAGING/repairrob"
export RR_SRC="$RR_ROOT/src"

# --- GABRIEL CORE ---
export GABRIEL="$HOME/NOIZYLAB/GABRIEL"

# --- DRIVES ---
export DRIVE_RED_DRAGON="/Volumes/RED DRAGON"
export DRIVE_RSP="/Volumes/RSP"
export DRIVE_DATA="/Volumes/RSP/NOISYLABZ"

# --- EDITOR ---
export EDITOR="nano"
export PAGER="cat" # As requested in some system prompts/defaults

# --- CONFIGURATION END ---
export OLLAMA_NUM_PARALLEL=4
export OLLAMA_MAX_LOADED_MODELS=3
export OLLAMA_FLASH_ATTENTION=1
source ~/.ai-env/bin/activate 2>/dev/null
