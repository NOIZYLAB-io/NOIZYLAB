#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# 🧠 MEMCELL BOOTSTRAP - ONE COMMAND SETUP
# ═══════════════════════════════════════════════════════════════
# Usage: curl -sL <url> | bash
#    or: bash bootstrap.sh
# ═══════════════════════════════════════════════════════════════

set -e
cd ~/NOIZYLAB/gabriel/memcell 2>/dev/null || cd ~/NOIZYLAB/gabriel/memcell

echo "⚡ MEMCELL BOOTSTRAP"
echo "━━━━━━━━━━━━━━━━━━━━"

# 1. Install MEMCELL
bash install.sh

# 2. Install MC96 Terminal
cd ../
bash install_mc96.sh 2>/dev/null || true

# 3. Setup CLEANSPACE
cd ../scripts
chmod +x cleanspace cleanspace.py 2>/dev/null || true

# 4. Initial capture
memcell capture 2>/dev/null || python3 ~/NOIZYLAB/gabriel/memcell/memcell.py capture

echo ""
echo "✅ BOOTSTRAP COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━"
echo "memcell recall \"today\"  ← try it"
