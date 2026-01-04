# ==============================================================================
# NOIZYLAB COMMAND ALIASES
# Add to ~/.zshrc: source ~/NOIZYLAB/scripts/aliases.sh
# ==============================================================================

# GORUNFREE - The main command
alias gorunfree='bash ~/NOIZYLAB/scripts/GORUNFREE_MASTER.sh'
alias grf='gorunfree'

# Quick status
alias status='bash ~/NOIZYLAB/scripts/status.sh'
alias health='bash ~/NOIZYLAB/scripts/health.sh'
alias optimize='sudo bash ~/NOIZYLAB/scripts/optimize.sh'

# DAZEFLOW - Daily tracker
alias dazeflow='bash ~/NOIZYLAB/scripts/dazeflow.sh'
alias df='dazeflow'
alias today='dazeflow show'
alias focus='dazeflow focus'
alias win='dazeflow win'

# Navigation
alias lab='cd ~/NOIZYLAB'
alias gab='cd ~/NOIZYLAB/GABRIEL'
alias scripts='cd ~/NOIZYLAB/scripts'

# Quick edits
alias labconfig='code ~/NOIZYLAB'

# Cloudflare
alias workers='wrangler deployments list'
alias deploy='cd ~/NOIZYLAB/GABRIEL/src/workers/noizylab && wrangler deploy'

# System
alias purge='sudo purge'
alias top5='ps aux | sort -nrk 3 | head -6'

# Git shortcuts for NOIZYLAB
alias gs='git status'
alias gp='git pull'
alias gc='git commit -am'

echo "🔥 NOIZYLAB aliases loaded"
