# ═══════════════════════════════════════════════════════════════════════════
# NOIZYLAB Zsh Configuration
# Optimized for M2 Ultra Mac Studio + Audio/AI Development
# ═══════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# PATH Configuration
# ─────────────────────────────────────────────────────────────────────────────
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"

# ─────────────────────────────────────────────────────────────────────────────
# Environment Variables
# ─────────────────────────────────────────────────────────────────────────────
export EDITOR="code-insiders --wait"
export VISUAL="$EDITOR"
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"

# Python (Homebrew)
export PYTHON_PATH="/opt/homebrew/bin/python3"

# Node.js memory limit for large projects
export NODE_OPTIONS="--max-old-space-size=8192"

# ─────────────────────────────────────────────────────────────────────────────
# History Configuration
# ─────────────────────────────────────────────────────────────────────────────
HISTFILE=~/.zsh_history
HISTSIZE=50000
SAVEHIST=50000
setopt EXTENDED_HISTORY          # Write timestamp to history
setopt HIST_EXPIRE_DUPS_FIRST    # Expire duplicates first
setopt HIST_IGNORE_DUPS          # Don't record duplicates
setopt HIST_IGNORE_SPACE         # Don't record commands starting with space
setopt HIST_VERIFY               # Show before executing history commands
setopt SHARE_HISTORY             # Share history between sessions
setopt INC_APPEND_HISTORY        # Add commands immediately

# ─────────────────────────────────────────────────────────────────────────────
# Prompt (Clean + Git-aware)
# ─────────────────────────────────────────────────────────────────────────────
autoload -Uz vcs_info
precmd() { vcs_info }
zstyle ':vcs_info:git:*' formats ' %F{cyan}(%b)%f'
setopt PROMPT_SUBST

# Two-line prompt: path + git branch on first line, arrow on second
PROMPT='%F{blue}%~%f${vcs_info_msg_0_}
%F{magenta}❯%f '

# ─────────────────────────────────────────────────────────────────────────────
# Completion System
# ─────────────────────────────────────────────────────────────────────────────
autoload -Uz compinit && compinit -C
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'  # Case insensitive
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*:descriptions' format '%F{yellow}-- %d --%f'

# ─────────────────────────────────────────────────────────────────────────────
# Key Bindings
# ─────────────────────────────────────────────────────────────────────────────
bindkey -e                           # Emacs mode
bindkey '^[[A' history-search-backward
bindkey '^[[B' history-search-forward
bindkey '^[[1;5C' forward-word       # Ctrl+Right
bindkey '^[[1;5D' backward-word      # Ctrl+Left

# ─────────────────────────────────────────────────────────────────────────────
# Aliases - Navigation
# ─────────────────────────────────────────────────────────────────────────────
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias ~='cd ~'

# ─────────────────────────────────────────────────────────────────────────────
# Aliases - Listing (using ls, fallback to eza if installed)
# ─────────────────────────────────────────────────────────────────────────────
if command -v eza &> /dev/null; then
    alias ls='eza --icons'
    alias ll='eza -la --icons --git'
    alias la='eza -a --icons'
    alias lt='eza --tree --level=2 --icons'
else
    alias ls='ls -G'
    alias ll='ls -laGh'
    alias la='ls -AG'
fi

# ─────────────────────────────────────────────────────────────────────────────
# Aliases - Git (supplement gitconfig aliases)
# ─────────────────────────────────────────────────────────────────────────────
alias g='git'
alias gs='git status -sb'
alias ga='git add'
alias gaa='git add --all'
alias gc='git commit'
alias gcm='git commit -m'
alias gp='git push'
alias gpl='git pull'
alias gco='git checkout'
alias gb='git branch'
alias gd='git diff'
alias glog='git lg'

# ─────────────────────────────────────────────────────────────────────────────
# Aliases - Development
# ─────────────────────────────────────────────────────────────────────────────
alias py='python3'
alias pip='pip3'
alias ni='npm install'
alias nr='npm run'
alias nrd='npm run dev'
alias nrb='npm run build'

# ─────────────────────────────────────────────────────────────────────────────
# Aliases - System
# ─────────────────────────────────────────────────────────────────────────────
alias reload='source ~/.zshrc'
alias zshrc='$EDITOR ~/.zshrc'
alias hosts='sudo $EDITOR /etc/hosts'
alias flushdns='sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder'
alias ports='lsof -i -P -n | grep LISTEN'

# ─────────────────────────────────────────────────────────────────────────────
# Aliases - Claude Code
# ─────────────────────────────────────────────────────────────────────────────
alias cc='claude'
alias ccr='claude --resume'
alias ccc='claude --continue'

# ─────────────────────────────────────────────────────────────────────────────
# Aliases - Quick Directories (NOIZYLAB specific)
# ─────────────────────────────────────────────────────────────────────────────
alias noizy='cd ~/NOIZYLAB'
alias gabriel='cd ~/NOIZYLAB/GABRIEL'
alias docs='cd ~/Documents'
alias dl='cd ~/Downloads'

# ─────────────────────────────────────────────────────────────────────────────
# Functions
# ─────────────────────────────────────────────────────────────────────────────

# Create directory and cd into it
mkcd() { mkdir -p "$1" && cd "$1"; }

# Quick find file by name
ff() { find . -type f -iname "*$1*"; }

# Quick find directory by name
fd() { find . -type d -iname "*$1*"; }

# Extract any archive
extract() {
    if [ -f "$1" ]; then
        case "$1" in
            *.tar.bz2)   tar xjf "$1"     ;;
            *.tar.gz)    tar xzf "$1"     ;;
            *.bz2)       bunzip2 "$1"     ;;
            *.rar)       unrar x "$1"     ;;
            *.gz)        gunzip "$1"      ;;
            *.tar)       tar xf "$1"      ;;
            *.tbz2)      tar xjf "$1"     ;;
            *.tgz)       tar xzf "$1"     ;;
            *.zip)       unzip "$1"       ;;
            *.Z)         uncompress "$1"  ;;
            *.7z)        7z x "$1"        ;;
            *)           echo "'$1' cannot be extracted" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

# Quick HTTP server in current directory
serve() { python3 -m http.server "${1:-8000}"; }

# ─────────────────────────────────────────────────────────────────────────────
# Performance Optimizations
# ─────────────────────────────────────────────────────────────────────────────
# Skip global compinit if already done
skip_global_compinit=1

# Faster paste
zstyle ':bracketed-paste-magic' active-widgets '.self-*'

# ─────────────────────────────────────────────────────────────────────────────
# POWER USER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

# Quick directory bookmarks
hash -d noizy=~/NOIZYLAB
hash -d gabriel=~/NOIZYLAB/GABRIEL
hash -d dl=~/Downloads
hash -d docs=~/Documents

# Copy last command to clipboard
copylast() { fc -ln -1 | pbcopy && echo "Copied: $(pbpaste)"; }

# Open current dir in VS Code
c() { code-insiders "${1:-.}"; }

# Quick git operations
gac() { git add -A && git commit -m "${1:-update}"; }
gacp() { git add -A && git commit -m "${1:-update}" && git push; }

# Find and kill process by name
pskill() { ps aux | grep -i "$1" | grep -v grep | awk '{print $2}' | xargs kill -9; }

# Show top 10 largest files in current dir
bigfiles() { find . -type f -exec du -h {} + 2>/dev/null | sort -rh | head -20; }

# Quick JSON formatting
jsonf() { cat "$1" | jq .; }

# Create and enter temp directory
tmpdir() { cd "$(mktemp -d)"; pwd; }

# Quick find in history
h() { history | grep -i "$1"; }

# Port forwarding helper
portfwd() { ssh -N -L "$1:localhost:$1" "$2"; }

# Quick diff between two files with color
fdiff() { diff -u "$1" "$2" | bat --language diff; }

# Docker shortcuts
dps() { docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"; }
dlog() { docker logs -f "$1"; }
dexec() { docker exec -it "$1" "${2:-sh}"; }
dstop() { docker stop $(docker ps -q); }
dclean() { docker system prune -af; }

# Kubernetes shortcuts
kp() { kubectl get pods "$@"; }
kl() { kubectl logs -f "$@"; }
kd() { kubectl describe "$@"; }
kx() { kubectl exec -it "$@" -- sh; }

# Quick HTTP requests
get() { curl -s "$1" | jq . 2>/dev/null || curl -s "$1"; }
post() { curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1" | jq . 2>/dev/null || curl -s -X POST -d "$2" "$1"; }

# Watch file changes
watchfile() { fswatch -o "$1" | xargs -n1 -I{} "${@:2}"; }

# Quick Python virtual env
venv() {
    if [[ -d .venv ]]; then
        source .venv/bin/activate
    elif [[ -d venv ]]; then
        source venv/bin/activate
    else
        python3 -m venv .venv && source .venv/bin/activate
    fi
}

# Quick npm scripts
nr() { npm run "$@"; }
nrs() { npm run start; }
nrt() { npm run test; }
nrb() { npm run build; }
nrd() { npm run dev; }

# Base64 encode/decode
b64e() { echo -n "$1" | base64; }
b64d() { echo -n "$1" | base64 -d; }

# URL encode/decode
urle() { python3 -c "import urllib.parse; print(urllib.parse.quote('$1'))"; }
urld() { python3 -c "import urllib.parse; print(urllib.parse.unquote('$1'))"; }

# Quick timestamp
ts() { date +%s; }
tsdate() { date -r "$1"; }

# Generate random string
randstr() { openssl rand -base64 "${1:-32}" | tr -dc 'a-zA-Z0-9' | head -c "${1:-32}"; echo; }

# Generate UUID
uuid() { uuidgen | tr '[:upper:]' '[:lower:]'; }

# Quick file hashing
md5f() { md5 -q "$1"; }
sha256f() { shasum -a 256 "$1" | cut -d' ' -f1; }

# Network utilities
myip() { curl -s ifconfig.me; echo; }
localip() { ipconfig getifaddr en0; }
flush() { sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder && echo "DNS flushed"; }

# Open man page in Preview as PDF
manpdf() { man -t "$1" | open -f -a Preview; }

# Quick note taking
note() {
    local notefile=~/.notes
    if [[ -n "$1" ]]; then
        echo "[$(date '+%Y-%m-%d %H:%M')] $*" >> "$notefile"
        echo "Note saved."
    else
        cat "$notefile" 2>/dev/null || echo "No notes yet."
    fi
}

# Calculator
calc() { python3 -c "print($*)"; }

# ─────────────────────────────────────────────────────────────────────────────
# FZF Integration (if installed)
# ─────────────────────────────────────────────────────────────────────────────
if command -v fzf &> /dev/null; then
    # Use fd for fzf if available
    if command -v fd &> /dev/null; then
        export FZF_DEFAULT_COMMAND='fd --type f --hidden --exclude .git'
        export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
        export FZF_ALT_C_COMMAND='fd --type d --hidden --exclude .git'
    fi

    export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border'

    # Quick file open with preview
    fo() {
        local file
        file=$(fzf --preview 'bat --color=always --style=numbers --line-range=:500 {}' --preview-window=right:60%)
        [[ -n "$file" ]] && code-insiders "$file"
    }

    # Git branch switcher
    fbr() {
        local branch
        branch=$(git branch -a | fzf | tr -d '[:space:]' | sed 's/remotes\/origin\///')
        [[ -n "$branch" ]] && git checkout "$branch"
    }

    # Git log browser
    flog() {
        git log --oneline --color=always | fzf --ansi --preview 'git show --color=always {1}'
    }

    # Kill process with fzf
    fkill() {
        local pid
        pid=$(ps -ef | fzf | awk '{print $2}')
        [[ -n "$pid" ]] && kill -9 "$pid"
    }
fi

# ─────────────────────────────────────────────────────────────────────────────
# Auto-suggestions and syntax highlighting (if installed)
# ─────────────────────────────────────────────────────────────────────────────
[[ -f /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]] && \
    source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh

[[ -f /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]] && \
    source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# ─────────────────────────────────────────────────────────────────────────────
# ADVANCED POWER USER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

# ══════════════════════════════════════════════════════════════════════════════
# FILE OPERATIONS
# ══════════════════════════════════════════════════════════════════════════════

# Backup a file with timestamp
backup() {
    local file="$1"
    [[ -f "$file" ]] && cp "$file" "${file}.backup.$(date +%Y%m%d_%H%M%S)"
}

# Create file with parent directories
touchp() {
    mkdir -p "$(dirname "$1")" && touch "$1"
}

# Safe remove with confirmation for multiple files
saferm() {
    if [[ $# -gt 3 ]]; then
        echo "Removing $# files:"
        printf '  %s\n' "$@"
        read -q "?Continue? (y/n) " && echo && rm -rf "$@"
    else
        rm -i "$@"
    fi
}

# Count files in directory
countfiles() {
    find "${1:-.}" -type f | wc -l
}

# Show directory size sorted
dirsize() {
    du -sh "${1:-.}"/* 2>/dev/null | sort -rh | head -20
}

# ══════════════════════════════════════════════════════════════════════════════
# DEVELOPMENT
# ══════════════════════════════════════════════════════════════════════════════

# Create Python virtual environment with uv
uvenv() {
    uv venv && source .venv/bin/activate
}

# Quick FastAPI project
fastapi-init() {
    local name="${1:-app}"
    mkdir -p "$name" && cd "$name"
    uv init
    uv add fastapi uvicorn
    cat > main.py << 'EOF'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF
    echo "Created FastAPI project: $name"
}

# Quick Next.js project
nextjs-init() {
    local name="${1:-app}"
    pnpm create next-app "$name" --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
    cd "$name"
    echo "Created Next.js project: $name"
}

# Find TODO/FIXME/HACK in codebase
todos() {
    rg -n "TODO|FIXME|HACK|XXX|BUG" --type-add 'code:*.{py,js,ts,tsx,jsx,go,rs,sh}' -t code "${1:-.}"
}

# Run command when files change
onchange() {
    local pattern="${1}"
    shift
    fswatch -o "$pattern" | xargs -n1 -I{} "$@"
}

# ══════════════════════════════════════════════════════════════════════════════
# GIT ENHANCED
# ══════════════════════════════════════════════════════════════════════════════

# Git clone and cd
gcl() {
    git clone "$1" && cd "$(basename "$1" .git)"
}

# Interactive branch delete
gbdel() {
    git branch | fzf -m | xargs -r git branch -d
}

# Show git stats for repo
gitstats() {
    echo "Commits: $(git rev-list --count HEAD)"
    echo "Contributors: $(git shortlog -sn | wc -l)"
    echo "First commit: $(git log --reverse --format='%ar' | head -1)"
    echo "Latest commit: $(git log -1 --format='%ar')"
    echo "Files: $(git ls-files | wc -l)"
    echo "Repo size: $(du -sh .git | cut -f1)"
}

# Quick conventional commit
feat() { git add -A && git commit -m "feat: $*"; }
fix() { git add -A && git commit -m "fix: $*"; }
docs() { git add -A && git commit -m "docs: $*"; }
chore() { git add -A && git commit -m "chore: $*"; }
refactor() { git add -A && git commit -m "refactor: $*"; }
test() { git add -A && git commit -m "test: $*"; }

# ══════════════════════════════════════════════════════════════════════════════
# DOCKER ENHANCED
# ══════════════════════════════════════════════════════════════════════════════

# Docker compose shortcuts
dcup() { docker compose up -d "$@"; }
dcdown() { docker compose down "$@"; }
dcrestart() { docker compose restart "$@"; }
dclogs() { docker compose logs -f "$@"; }
dcbuild() { docker compose build "$@"; }
dcps() { docker compose ps "$@"; }

# Docker cleanup
dkill() { docker kill $(docker ps -q) 2>/dev/null; }
drm() { docker rm $(docker ps -aq) 2>/dev/null; }
drmi() { docker rmi $(docker images -q) 2>/dev/null; }
dprune() { docker system prune -af --volumes; }

# Docker shell into container
dsh() {
    docker exec -it "$1" sh -c 'command -v bash >/dev/null && bash || sh'
}

# Docker image size
dsize() {
    docker images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}" | sort -k2 -h
}

# ══════════════════════════════════════════════════════════════════════════════
# KUBERNETES ENHANCED
# ══════════════════════════════════════════════════════════════════════════════

# Quick namespace switch
kns() {
    kubectl config set-context --current --namespace="$1"
}

# Get pods with wide output
kpw() { kubectl get pods -o wide "$@"; }

# Watch pods
kpwatch() { watch -n 2 "kubectl get pods $*"; }

# Quick port forward
kpf() {
    kubectl port-forward "$1" "${2}:${3:-$2}"
}

# Copy file from pod
kcp() {
    kubectl cp "$1:$2" "$3"
}

# Restart deployment
krestart() {
    kubectl rollout restart deployment "$1"
}

# ══════════════════════════════════════════════════════════════════════════════
# NETWORK & HTTP
# ══════════════════════════════════════════════════════════════════════════════

# Check if port is in use
isport() {
    lsof -i ":$1" 2>/dev/null || echo "Port $1 is free"
}

# Quick HTTP server with CORS
servecors() {
    python3 -c "
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f'Serving with CORS on http://localhost:{port}')
HTTPServer(('', port), CORSHandler).serve_forever()
" "${1:-8000}"
}

# Test URL response time
urltime() {
    curl -o /dev/null -s -w "DNS: %{time_namelookup}s\nConnect: %{time_connect}s\nTTFB: %{time_starttransfer}s\nTotal: %{time_total}s\n" "$1"
}

# Get headers
headers() {
    curl -sI "$1" | bat --language http
}

# Pretty JSON from URL
jget() {
    curl -s "$1" | jq .
}

# POST JSON
jpost() {
    curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1" | jq .
}

# ══════════════════════════════════════════════════════════════════════════════
# AUDIO/MEDIA
# ══════════════════════════════════════════════════════════════════════════════

# Convert to MP3
tomp3() {
    ffmpeg -i "$1" -codec:a libmp3lame -qscale:a 2 "${1%.*}.mp3"
}

# Convert to WAV
towav() {
    ffmpeg -i "$1" -acodec pcm_s16le -ar 44100 "${1%.*}.wav"
}

# Extract audio from video
extractaudio() {
    ffmpeg -i "$1" -vn -acodec copy "${1%.*}.aac"
}

# Get audio/video info
mediainfo() {
    ffprobe -v quiet -print_format json -show_format -show_streams "$1" | jq .
}

# Normalize audio
normalize() {
    ffmpeg -i "$1" -af loudnorm -c:a pcm_s16le "${1%.*}_normalized.wav"
}

# ══════════════════════════════════════════════════════════════════════════════
# JSON/YAML
# ══════════════════════════════════════════════════════════════════════════════

# JSON to YAML
j2y() { cat "$1" | yq -P; }

# YAML to JSON
y2j() { cat "$1" | yq -o=json; }

# Pretty print JSON file
jpp() { cat "$1" | jq .; }

# Edit JSON interactively
jedit() { cat "$1" | fx; }

# Query JSON with path
jpath() { cat "$1" | jq "$2"; }

# ══════════════════════════════════════════════════════════════════════════════
# SYSTEM INFO
# ══════════════════════════════════════════════════════════════════════════════

# System overview
sysinfo() {
    echo "═══════════════════════════════════════════════════════════"
    echo "Hostname: $(hostname)"
    echo "OS: $(sw_vers -productName) $(sw_vers -productVersion)"
    echo "Kernel: $(uname -r)"
    echo "CPU: $(sysctl -n machdep.cpu.brand_string)"
    echo "Cores: $(sysctl -n hw.ncpu)"
    echo "Memory: $(( $(sysctl -n hw.memsize) / 1073741824 )) GB"
    echo "Disk: $(df -h / | awk 'NR==2 {print $4 " free of " $2}')"
    echo "Uptime: $(uptime | awk -F'(up |,)' '{print $2}')"
    echo "═══════════════════════════════════════════════════════════"
}

# Top memory usage
topmem() {
    ps aux | sort -nrk 4 | head -10
}

# Top CPU usage
topcpu() {
    ps aux | sort -nrk 3 | head -10
}

# ══════════════════════════════════════════════════════════════════════════════
# CLIPBOARD
# ══════════════════════════════════════════════════════════════════════════════

# Clipboard to file
paste2file() { pbpaste > "$1"; }

# File to clipboard
file2clip() { cat "$1" | pbcopy; }

# Clipboard as JSON pretty
clipjson() { pbpaste | jq . | pbcopy && pbpaste; }

# ══════════════════════════════════════════════════════════════════════════════
# MISC UTILITIES
# ══════════════════════════════════════════════════════════════════════════════

# Quick timer
timer() {
    local seconds="${1:-60}"
    echo "Timer: $seconds seconds"
    sleep "$seconds" && osascript -e 'display notification "Timer Complete!" with title "Timer"' && afplay /System/Library/Sounds/Glass.aiff
}

# Stopwatch
stopwatch() {
    local start=$(date +%s)
    echo "Stopwatch started. Press Ctrl+C to stop."
    while true; do
        local elapsed=$(($(date +%s) - start))
        printf "\r%02d:%02d:%02d" $((elapsed/3600)) $((elapsed%3600/60)) $((elapsed%60))
        sleep 1
    done
}

# Weather (short)
wttr() { curl -s "wttr.in/${1:-}?format=3"; }

# Generate password
genpass() {
    openssl rand -base64 "${1:-32}" | tr -dc 'a-zA-Z0-9!@#$%' | head -c "${1:-32}"
    echo
}

# QR code in terminal
qr() { qrencode -t ANSI256 "$1"; }

# Cheat sheet
cheat() { curl -s "cheat.sh/$1"; }

# ─────────────────────────────────────────────────────────────────────────────
# ZOXIDE (Smart cd)
# ─────────────────────────────────────────────────────────────────────────────
if command -v zoxide &> /dev/null; then
    eval "$(zoxide init zsh)"
fi

# ─────────────────────────────────────────────────────────────────────────────
# STARSHIP PROMPT (if installed)
# ─────────────────────────────────────────────────────────────────────────────
if command -v starship &> /dev/null; then
    eval "$(starship init zsh)"
fi

# ─────────────────────────────────────────────────────────────────────────────
# ATUIN (Magical history)
# ─────────────────────────────────────────────────────────────────────────────
if command -v atuin &> /dev/null; then
    eval "$(atuin init zsh)"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Local Overrides (optional)
# ─────────────────────────────────────────────────────────────────────────────
[[ -f ~/.zshrc.local ]] && source ~/.zshrc.local
