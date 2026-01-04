#!/bin/bash
# ==============================================================================
# NOIZYLAB HEALTH CHECK - REAL VERSION
# Built: 2026-01-04
# 
# Checks ACTUAL systems. Reports REAL numbers. NO BULLSHIT.
# ==============================================================================

echo "═══════════════════════════════════════════════════════════════════"
echo "🏥 NOIZYLAB HEALTH CHECK"
echo "   $(date '+%Y-%m-%d %H:%M:%S')"
echo "═══════════════════════════════════════════════════════════════════"
echo ""

# -----------------------------------------------------------------------------
# 1. SYSTEM RESOURCES
# -----------------------------------------------------------------------------
echo "💻 SYSTEM RESOURCES"
echo "───────────────────────────────────────────────────────────────────"

# CPU
CPU_USAGE=$(top -l 1 | grep "CPU usage" | awk '{print $3}' | tr -d '%')
echo "   CPU Usage:     ${CPU_USAGE}%"

# Memory
MEM_PRESSURE=$(memory_pressure 2>/dev/null | grep "System-wide memory free percentage" | awk '{print $5}' | tr -d '%') || MEM_PRESSURE="N/A"
echo "   Memory Free:   ${MEM_PRESSURE}%"

# Disk
DISK_INFO=$(df -h / | tail -1)
DISK_USED=$(echo "$DISK_INFO" | awk '{print $5}')
DISK_AVAIL=$(echo "$DISK_INFO" | awk '{print $4}')
echo "   Disk Used:     ${DISK_USED}"
echo "   Disk Free:     ${DISK_AVAIL}"
echo ""

# -----------------------------------------------------------------------------
# 2. NOIZY.AI STATUS (Real endpoint check)
# -----------------------------------------------------------------------------
echo "🌐 NOIZY.AI STATUS"
echo "───────────────────────────────────────────────────────────────────"

NOIZY_RESPONSE=$(curl -s -m 5 https://noizy.ai/ 2>/dev/null) || NOIZY_RESPONSE="TIMEOUT"

if echo "$NOIZY_RESPONSE" | grep -q "HEAVEN"; then
    echo "   noizy.ai:      ✅ ONLINE"
    VERSION=$(echo "$NOIZY_RESPONSE" | grep -o '"version":[0-9]*' | cut -d':' -f2) || VERSION="?"
    echo "   Version:       v${VERSION}"
    
    # Extract agents
    AGENTS=$(echo "$NOIZY_RESPONSE" | grep -o '"agents":\[[^]]*\]' | tr -d '[]"' | sed 's/agents://') || AGENTS="?"
    echo "   Agents:        ${AGENTS}"
else
    echo "   noizy.ai:      ❌ OFFLINE or ERROR"
    echo "   Response:      ${NOIZY_RESPONSE:0:50}..."
fi

# Check heaven subdomain
HEAVEN_RESPONSE=$(curl -s -m 5 -o /dev/null -w "%{http_code}" https://heaven.noizy.ai/ 2>/dev/null) || HEAVEN_RESPONSE="TIMEOUT"
if [ "$HEAVEN_RESPONSE" = "200" ]; then
    echo "   heaven.noizy:  ✅ ONLINE"
else
    echo "   heaven.noizy:  ⚠️  Status $HEAVEN_RESPONSE"
fi
echo ""

# -----------------------------------------------------------------------------
# 3. CLOUDFLARE STATUS
# -----------------------------------------------------------------------------
echo "☁️  CLOUDFLARE STATUS"
echo "───────────────────────────────────────────────────────────────────"

if command -v wrangler &> /dev/null; then
    WRANGLER_VERSION=$(wrangler --version 2>/dev/null | head -1) || WRANGLER_VERSION="unknown"
    echo "   Wrangler:      ✅ Installed (${WRANGLER_VERSION})"
else
    echo "   Wrangler:      ❌ Not installed"
fi

# Try to list workers (may need auth)
WORKERS=$(wrangler deployments list 2>/dev/null | head -5) || WORKERS="Auth required or error"
echo "   Workers:       (run 'wrangler deployments list' for details)"
echo ""

# -----------------------------------------------------------------------------
# 4. DEVELOPMENT TOOLS
# -----------------------------------------------------------------------------
echo "🛠️  DEVELOPMENT TOOLS"
echo "───────────────────────────────────────────────────────────────────"

# Node
if command -v node &> /dev/null; then
    NODE_V=$(node --version)
    echo "   Node.js:       ✅ ${NODE_V}"
else
    echo "   Node.js:       ❌ Not installed"
fi

# Python
if command -v python3 &> /dev/null; then
    PYTHON_V=$(python3 --version | awk '{print $2}')
    echo "   Python:        ✅ ${PYTHON_V}"
else
    echo "   Python:        ❌ Not installed"
fi

# Claude Code
if command -v claude &> /dev/null; then
    CLAUDE_V=$(claude --version 2>/dev/null | head -1) || CLAUDE_V="installed"
    echo "   Claude Code:   ✅ ${CLAUDE_V}"
else
    echo "   Claude Code:   ❌ Not installed"
fi

# Git
if command -v git &> /dev/null; then
    GIT_V=$(git --version | awk '{print $3}')
    echo "   Git:           ✅ ${GIT_V}"
else
    echo "   Git:           ❌ Not installed"
fi
echo ""

# -----------------------------------------------------------------------------
# 5. EXTERNAL DRIVES
# -----------------------------------------------------------------------------
echo "💾 EXTERNAL DRIVES"
echo "───────────────────────────────────────────────────────────────────"

# List mounted volumes (excluding system)
df -h | grep "/Volumes" | while read line; do
    MOUNT=$(echo "$line" | awk '{print $NF}')
    AVAIL=$(echo "$line" | awk '{print $4}')
    USED=$(echo "$line" | awk '{print $5}')
    NAME=$(basename "$MOUNT")
    echo "   ${NAME}: ${AVAIL} free (${USED} used)"
done

# Check if any drives found
if ! df -h | grep -q "/Volumes"; then
    echo "   No external drives mounted"
fi
echo ""

# -----------------------------------------------------------------------------
# 6. ACTIVE PROCESSES (Top CPU consumers)
# -----------------------------------------------------------------------------
echo "📈 TOP CPU CONSUMERS"
echo "───────────────────────────────────────────────────────────────────"
ps aux | sort -nrk 3,3 | head -6 | tail -5 | awk '{printf "   %-20s %s%%\n", $11, $3}'
echo ""

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------
echo "═══════════════════════════════════════════════════════════════════"
echo "✅ HEALTH CHECK COMPLETE"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "🔥 GORUNFREE"
echo ""
