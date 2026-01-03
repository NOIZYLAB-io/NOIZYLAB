#!/usr/bin/env bash
#═══════════════════════════════════════════════════════════════════════════════
# M2G Claude Voice Pack - macOS Installer
# 
# Installs:
#   • m2g-say    - OS voice wrapper (picks best available voice)
#   • claudev    - Claude CLI wrapper with spoken status
#
# Usage after install:
#   m2g-say "hello world"
#   claudev "explain quantum computing"
#   SAY=0 claudev "silent mode"
#═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

ROOT="${HOME}/m2g/claude-voice"
mkdir -p "${ROOT}"

echo "═══════════════════════════════════════════════════════════════"
echo "  M2G Claude Voice Pack - macOS Installer"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Installing to: ${ROOT}"
echo ""

#───────────────────────────────────────────────────────────────────────────────
# m2g-say - macOS voice wrapper
#───────────────────────────────────────────────────────────────────────────────
cat > "${ROOT}/m2g-say" <<'EOF'
#!/usr/bin/env bash
#═══════════════════════════════════════════════════════════════════════════════
# m2g-say - macOS text-to-speech wrapper
# Automatically picks the best available voice
#═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

TEXT="${*:-}"
[[ -z "${TEXT}" ]] && exit 0

# Voice preference order (high-quality first)
PREFERRED_VOICES=(
  "Samantha (Enhanced)"
  "Alex (Enhanced)"
  "Jamie (Enhanced)"
  "Daniel (Enhanced)"
  "Samantha"
  "Alex"
  "Jamie"
  "Daniel"
  "Karen"
  "Moira"
)

pick_voice() {
  for v in "${PREFERRED_VOICES[@]}"; do
    if /usr/bin/say -v "$v" "" 2>/dev/null; then
      echo "$v"
      return 0
    fi
  done
  echo ""
}

# Cache voice selection for performance
VOICE_CACHE="${HOME}/.m2g-say-voice"
if [[ -f "${VOICE_CACHE}" ]]; then
  VOICE="$(cat "${VOICE_CACHE}")"
  # Verify cached voice still works
  if ! /usr/bin/say -v "${VOICE}" "" 2>/dev/null; then
    VOICE=""
  fi
fi

if [[ -z "${VOICE:-}" ]]; then
  VOICE="$(pick_voice)"
  if [[ -n "${VOICE}" ]]; then
    echo "${VOICE}" > "${VOICE_CACHE}"
  fi
fi

# Speak the text
if [[ -n "${VOICE}" ]]; then
  /usr/bin/say -v "${VOICE}" "${TEXT}"
else
  /usr/bin/say "${TEXT}"
fi
EOF
chmod +x "${ROOT}/m2g-say"
echo "✓ Created m2g-say"

#───────────────────────────────────────────────────────────────────────────────
# claudev - Claude CLI wrapper with voice status
#───────────────────────────────────────────────────────────────────────────────
cat > "${ROOT}/claudev" <<'EOF'
#!/usr/bin/env bash
#═══════════════════════════════════════════════════════════════════════════════
# claudev - Claude CLI wrapper with spoken status
#
# Environment variables:
#   SAY=0         Disable voice (default: 1)
#   CLAUDE_BIN    Force specific CLI (default: auto-detect)
#   M2G_VOICE     Custom status messages (json)
#
# Usage:
#   claudev "your prompt here"
#   claudev --model claude-sonnet-4-20250514 "prompt"
#   SAY=0 claudev "silent mode"
#   CLAUDE_BIN=m2g-claude claudev "use specific cli"
#═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

# Configuration
SAY="${SAY:-1}"
CLAUDE_BIN="${CLAUDE_BIN:-}"

# Voice function
speak() {
  if [[ "${SAY}" == "1" ]] && command -v m2g-say >/dev/null 2>&1; then
    m2g-say "$*" &
  fi
}

# Auto-detect Claude CLI
pick_claude() {
  if [[ -n "${CLAUDE_BIN}" ]] && command -v "${CLAUDE_BIN}" >/dev/null 2>&1; then
    echo "${CLAUDE_BIN}"
    return
  fi
  
  # Priority order: m2g-claude (custom) > claude (official) > claude-code
  for cli in m2g-claude claude claude-code; do
    if command -v "$cli" >/dev/null 2>&1; then
      echo "$cli"
      return
    fi
  done
  
  echo ""
}

# Find CLI
CLI="$(pick_claude)"
if [[ -z "${CLI}" ]]; then
  echo "claudev: no Claude CLI found" >&2
  echo "Install one of: m2g-claude, claude, claude-code" >&2
  exit 127
fi

# Check for help flags (don't speak for these)
for arg in "$@"; do
  case "$arg" in
    -h|--help|-v|--version)
      exec "${CLI}" "$@"
      ;;
  esac
done

# Run with voice status
speak "Claude starting"

START_TIME=$(date +%s)
set +e
"${CLI}" "$@"
RC=$?
set -e
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

if [[ $RC -eq 0 ]]; then
  if [[ $DURATION -gt 5 ]]; then
    speak "Claude done, ${DURATION} seconds"
  else
    speak "Claude done"
  fi
else
  speak "Claude error, code ${RC}"
fi

exit $RC
EOF
chmod +x "${ROOT}/claudev"
echo "✓ Created claudev"

#───────────────────────────────────────────────────────────────────────────────
# m2g-ask - Quick one-liner helper
#───────────────────────────────────────────────────────────────────────────────
cat > "${ROOT}/m2g-ask" <<'EOF'
#!/usr/bin/env bash
#═══════════════════════════════════════════════════════════════════════════════
# m2g-ask - Quick Claude question (clipboard or argument)
#═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

PROMPT="${*:-}"

# If no argument, try clipboard
if [[ -z "${PROMPT}" ]]; then
  if command -v pbpaste >/dev/null 2>&1; then
    PROMPT="$(pbpaste 2>/dev/null || echo '')"
  fi
fi

if [[ -z "${PROMPT}" ]]; then
  echo "Usage: m2g-ask 'your question'" >&2
  echo "       Or copy text to clipboard first" >&2
  exit 1
fi

exec claudev "${PROMPT}"
EOF
chmod +x "${ROOT}/m2g-ask"
echo "✓ Created m2g-ask"

#───────────────────────────────────────────────────────────────────────────────
# Create symlinks in /usr/local/bin
#───────────────────────────────────────────────────────────────────────────────
echo ""
echo "Creating symlinks in /usr/local/bin (may require password)..."

if [[ ! -d /usr/local/bin ]]; then
  sudo mkdir -p /usr/local/bin
fi

sudo ln -sf "${ROOT}/m2g-say" /usr/local/bin/m2g-say
sudo ln -sf "${ROOT}/claudev" /usr/local/bin/claudev
sudo ln -sf "${ROOT}/m2g-ask" /usr/local/bin/m2g-ask

echo "✓ Symlinks created"

#───────────────────────────────────────────────────────────────────────────────
# Create uninstaller
#───────────────────────────────────────────────────────────────────────────────
cat > "${ROOT}/uninstall.sh" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
echo "Removing M2G Claude Voice Pack..."
sudo rm -f /usr/local/bin/m2g-say /usr/local/bin/claudev /usr/local/bin/m2g-ask
rm -rf "${HOME}/m2g/claude-voice"
rm -f "${HOME}/.m2g-say-voice"
echo "✓ Uninstalled"
EOF
chmod +x "${ROOT}/uninstall.sh"

#───────────────────────────────────────────────────────────────────────────────
# Done
#───────────────────────────────────────────────────────────────────────────────
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  ✓ M2G Claude Voice Pack Installed"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Commands available:"
echo "  m2g-say \"text\"     - Speak text"
echo "  claudev \"prompt\"   - Claude with voice status"
echo "  m2g-ask \"question\" - Quick question (or use clipboard)"
echo ""
echo "Options:"
echo "  SAY=0 claudev ...  - Disable voice"
echo "  CLAUDE_BIN=xxx     - Force specific CLI"
echo ""
echo "Uninstall:"
echo "  ${ROOT}/uninstall.sh"
echo ""

# Announce success
m2g-say "Claude voice pack installed" 2>/dev/null || true
