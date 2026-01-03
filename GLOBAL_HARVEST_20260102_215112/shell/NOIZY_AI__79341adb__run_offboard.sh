#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
# run_offboard.sh - Local runner for NOIZYLAB offboarding
# ═══════════════════════════════════════════════════════════════════════════════
#
# Usage:
#   ./run_offboard.sh                    # Dry run (default)
#   DRY_RUN=false ./run_offboard.sh      # Execute removals
#
# Required environment:
#   GH_TOKEN or GITHUB_TOKEN            # GitHub PAT with admin:org
#   CLAUDE_API_KEY or ANTHROPIC_API_KEY # For AI classification (optional)
#   CLAUDE_API_URL                      # Claude endpoint (optional)
#
# Optional:
#   ORG=NOIZYLAB                        # GitHub org (default: NOIZYLAB)
#   ALLOW_EMAIL=rsplowman@icloud.com    # Allowlist (default: rsplowman@icloud.com)
#   CONFIDENCE_THRESHOLD=0.95           # AI threshold (default: 0.95)
#
# ═══════════════════════════════════════════════════════════════════════════════

set -euo pipefail

# Configuration
DRY_RUN="${DRY_RUN:-true}"
export ORG="${ORG:-NOIZYLAB}"
export ALLOW_EMAIL="${ALLOW_EMAIL:-rsplowman@icloud.com}"
export CONFIDENCE_THRESHOLD="${CONFIDENCE_THRESHOLD:-0.95}"

# Colors (if terminal supports)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "═══════════════════════════════════════════════════════════"
echo "NOIZYLAB OFFBOARDING PIPELINE"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Org:        $ORG"
echo "Allowlist:  $ALLOW_EMAIL"
echo "Threshold:  $CONFIDENCE_THRESHOLD"
echo "Dry run:    $DRY_RUN"
echo ""

# Check dependencies
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo -e "${RED}ERROR: Python not found${NC}"
    exit 1
fi
PYTHON=$(command -v python3 || command -v python)

if ! command -v gh &> /dev/null; then
    echo -e "${YELLOW}WARNING: gh CLI not found - using direct API${NC}"
fi

# Check token
if [ -z "${GH_TOKEN:-}" ] && [ -z "${GITHUB_TOKEN:-}" ]; then
    echo -e "${RED}ERROR: Set GH_TOKEN or GITHUB_TOKEN${NC}"
    exit 1
fi

# Create artifacts directory
mkdir -p artifacts

# ═══════════════════════════════════════════════════════════════════════════════
# STAGE 1: INVENTORY
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}[1/5] Gathering inventory...${NC}"
$PYTHON scripts/gather_full_inventory.py \
    --org "$ORG" \
    --out artifacts/inventory.json

# ═══════════════════════════════════════════════════════════════════════════════
# STAGE 2: AI CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}[2/5] AI classification...${NC}"

# Check if AI is available, fallback to rules if not
if [ -z "${CLAUDE_API_KEY:-}" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    echo -e "${YELLOW}  No CLAUDE_API_KEY - using rule-based classification${NC}"
    FORCE_RULES="--force-rules"
else
    FORCE_RULES=""
fi

$PYTHON scripts/ai_validate.py \
    --inventory artifacts/inventory.json \
    --out artifacts/plan.json \
    $FORCE_RULES

# ═══════════════════════════════════════════════════════════════════════════════
# STAGE 3: SCHEMA VALIDATION
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}[3/5] Validating plan schema...${NC}"
$PYTHON scripts/schema_validator.py --plan artifacts/plan.json --fix || {
    echo -e "${RED}Schema validation failed${NC}"
    exit 1
}

# ═══════════════════════════════════════════════════════════════════════════════
# VERIFY RSPLOWMAN
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}[3.5] Verifying rsplowman protected...${NC}"
if command -v jq &> /dev/null; then
    if jq -e '.remove[] | select(.login | ascii_downcase == "rsplowman")' artifacts/plan.json > /dev/null 2>&1; then
        echo -e "${RED}CRITICAL: rsplowman found in remove list! Aborting.${NC}"
        exit 1
    fi
    echo -e "${GREEN}  ✅ rsplowman NOT in remove list${NC}"
else
    grep -i '"login".*"rsplowman"' artifacts/plan.json | head -5 || true
fi

# ═══════════════════════════════════════════════════════════════════════════════
# DISPLAY SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "PLAN SUMMARY"
echo "═══════════════════════════════════════════════════════════"
if command -v jq &> /dev/null; then
    echo "Preserve: $(jq '.preserve | length' artifacts/plan.json)"
    echo "Remove:   $(jq '.remove | length' artifacts/plan.json)"
    echo "Review:   $(jq '.review | length' artifacts/plan.json)"
    echo ""
    echo "Preserve list:"
    jq -r '.preserve[] | "  ✅ \(.login)"' artifacts/plan.json 2>/dev/null || echo "  (none)"
    echo ""
    echo "Remove list:"
    jq -r '.remove[] | "  ❌ \(.login)"' artifacts/plan.json 2>/dev/null || echo "  (none)"
else
    cat artifacts/plan.summary.txt 2>/dev/null || cat artifacts/plan.json
fi
echo "═══════════════════════════════════════════════════════════"

# ═══════════════════════════════════════════════════════════════════════════════
# DRY RUN CHECK
# ═══════════════════════════════════════════════════════════════════════════════
if [ "$DRY_RUN" = "true" ]; then
    echo ""
    echo -e "${YELLOW}DRY RUN COMPLETE - No changes made${NC}"
    echo ""
    echo "To execute: DRY_RUN=false ./run_offboard.sh"
    echo ""
    echo "Artifacts:"
    echo "  - artifacts/inventory.json"
    echo "  - artifacts/plan.json"
    echo "  - artifacts/plan.summary.txt"
    exit 0
fi

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIRMATION
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${RED}⚠️  DESTRUCTIVE OPERATION ⚠️${NC}"
echo ""
read -p "Type 'EXECUTE' to proceed with removals: " CONFIRM
if [ "$CONFIRM" != "EXECUTE" ]; then
    echo "Aborted."
    exit 0
fi

# ═══════════════════════════════════════════════════════════════════════════════
# STAGE 4: EXECUTE
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}[4/5] Executing removals...${NC}"
$PYTHON scripts/execute_plan.py \
    --plan artifacts/plan.json \
    --org "$ORG" \
    --out artifacts/execution_log.json

# ═══════════════════════════════════════════════════════════════════════════════
# STAGE 5: GENERATE ROLLBACK
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}[5/5] Generating rollback script...${NC}"
$PYTHON scripts/generate_rollback.py \
    --audit artifacts/execution_log.json \
    --org "$ORG" \
    --out artifacts/rollback.sh

# ═══════════════════════════════════════════════════════════════════════════════
# SIGN ARTIFACTS
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}Signing artifacts...${NC}"
$PYTHON scripts/artifact_signer.py --dir artifacts --checksums-only

# ═══════════════════════════════════════════════════════════════════════════════
# COMPLETE
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo "═══════════════════════════════════════════════════════════"
echo -e "${GREEN}EXECUTION COMPLETE${NC}"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Artifacts:"
echo "  - artifacts/inventory.json"
echo "  - artifacts/plan.json"
echo "  - artifacts/execution_log.json"
echo "  - artifacts/rollback.sh"
echo ""
echo -e "${YELLOW}NEXT STEPS:${NC}"
echo "  1. ROTATE YOUR PAT IMMEDIATELY"
echo "  2. Verify remaining members: https://github.com/orgs/$ORG/people"
echo "  3. Check audit log: https://github.com/orgs/$ORG/settings/audit-log"
echo ""
