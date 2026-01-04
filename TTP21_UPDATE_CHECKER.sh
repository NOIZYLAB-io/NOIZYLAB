#!/bin/bash

# ═══════════════════════════════════════════════════════════════════
# TECHTOOL PRO 21.0.6 - UPDATE & VERIFICATION
# ═══════════════════════════════════════════════════════════════════
# Latest Release: December 19, 2025 (v21.0.6)
# Size: 48.4 MB
# ═══════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║         TECHTOOL PRO 21.0.6 - UPDATE CHECKER                     ║
║              Latest Release: December 19, 2025                   ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# ═══════════════════════════════════════════════════════════════════
# CHECK CURRENT VERSION
# ═══════════════════════════════════════════════════════════════════

echo -e "${YELLOW}Checking installed TechTool Pro version...${NC}"
echo ""

TTP_APP="/Applications/Techtool Pro.app"
TTP_PLIST="$TTP_APP/Contents/Info.plist"

if [ -d "$TTP_APP" ]; then
    echo -e "${GREEN}✓ TechTool Pro found at: $TTP_APP${NC}"
    
    if [ -f "$TTP_PLIST" ]; then
        CURRENT_VERSION=$(/usr/libexec/PlistBuddy -c "Print :CFBundleShortVersionString" "$TTP_PLIST" 2>/dev/null)
        if [ -n "$CURRENT_VERSION" ]; then
            echo -e "${CYAN}Current Version: $CURRENT_VERSION${NC}"
        else
            echo -e "${YELLOW}⚠ Could not read version info${NC}"
        fi
    fi
else
    echo -e "${RED}✗ TechTool Pro not found in /Applications${NC}"
    echo -e "${YELLOW}Please install TechTool Pro 21 first${NC}"
    exit 1
fi

echo ""

# ═══════════════════════════════════════════════════════════════════
# LATEST VERSION INFO
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}LATEST VERSION: 21.0.6 (December 19, 2025)${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}What's New in 21.0.6:${NC}"
echo ""
echo "🌐 Added French, German, and Japanese localization support"
echo "🐛 Fixed crash in Disk Image tool (network volumes)"
echo "🔧 Resolved Volume Cloning duplicate function failure"
echo "⚡ Fixed 'About This Mac' interrupting progress tracking"
echo "📊 Fixed crash when deleting multiple reports"
echo "🔄 Updated Sparkle framework to v2.8.1"
echo "✨ Minor fixes and general enhancements"
echo ""

# ═══════════════════════════════════════════════════════════════════
# UPDATE INSTRUCTIONS
# ═══════════════════════════════════════════════════════════════════

echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}HOW TO UPDATE:${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}METHOD 1: In-App Update (RECOMMENDED)${NC}"
echo "1. Launch TechTool Pro"
echo "2. Go to: TechTool Pro menu → Check for Update..."
echo "3. Follow the prompts to download and install"
echo ""

echo -e "${GREEN}METHOD 2: Manual Download${NC}"
echo "1. Login to your Micromat account:"
echo "   ${CYAN}https://www.micromat.com/login${NC}"
echo "2. Download the latest version (48.4 MB)"
echo "3. Replace existing app with new version"
echo ""

# ═══════════════════════════════════════════════════════════════════
# WHY THIS UPDATE MATTERS FOR NOIZYLAB
# ═══════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}WHY 21.0.6 MATTERS FOR YOUR 50TB CLEANUP:${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo "✅ VOLUME CLONING FIX:"
echo "   - You can now safely clone drives before repair"
echo "   - Critical for backing up 40-year archive"
echo "   - Duplicate clone function now works correctly"
echo ""

echo "✅ DISK IMAGE FIX:"
echo "   - Network volume crash resolved"
echo "   - Important if using networked storage"
echo "   - Safer operations across all drives"
echo ""

echo "✅ STABILITY IMPROVEMENTS:"
echo "   - No more crashes during multi-report deletion"
echo "   - Progress tracking more reliable"
echo "   - Better overall stability for long repair jobs"
echo ""

echo "✅ UPDATED FRAMEWORK:"
echo "   - Sparkle 2.8.1 = better security"
echo "   - More reliable updates going forward"
echo "   - Improved performance"
echo ""

# ═══════════════════════════════════════════════════════════════════
# VERIFICATION AFTER UPDATE
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}AFTER UPDATING, VERIFY:${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo "1. Check version number:"
echo "   TechTool Pro → About TechTool Pro"
echo "   Should show: 21.0.6"
echo ""

echo "2. Test Volume Cloning:"
echo "   Tools → Volume Cloning"
echo "   Verify duplicate clone option works"
echo ""

echo "3. Run this script again to confirm:"
echo "   bash ~/NOIZYLAB/TTP21_UPDATE_CHECKER.sh"
echo ""

# ═══════════════════════════════════════════════════════════════════
# INTEGRATION WITH HOT ROD GUIDE
# ═══════════════════════════════════════════════════════════════════

echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}AFTER UPDATING TO 21.0.6:${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo "Run the Hot Rod optimization guide:"
echo ""
echo "  ${CYAN}bash ~/NOIZYLAB/TTP21_HOT_ROD_GUIDE.sh${NC}"
echo ""
echo "This will configure TTP 21.0.6 for maximum speed on:"
echo "  • 12TB"
echo "  • RED DRAGON"
echo "  • 6TB"
echo "  • 4TB Lacie"
echo ""

# ═══════════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════════

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}QUICK REFERENCE:${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
VERSION HISTORY:
  21.0.6 - Dec 19, 2025 - Latest (cloning fixes, stability)
  21.0.5 - Earlier 2025 - Previous release
  21.0.0 - 2024 - Initial release

FILE SIZE: 48.4 MB

SYSTEM REQUIREMENTS:
  • macOS 14 Sonoma or later
  • Intel or Apple Silicon (M1/M2/M3)
  • 4GB RAM minimum (192GB recommended for hot rod mode!)

MICROMAT SUPPORT:
  • Website: https://www.micromat.com
  • Support: https://www.micromat.com/support
  • Release Notes: https://www.micromat.com/techtool-pro-21-0-6-released/

EOF

echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}🚀 READY TO UPDATE & HOT ROD YOUR DRIVES!${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo ""

# Prompt to launch TechTool Pro for update
echo -e "${GREEN}Launch TechTool Pro now to check for updates? (y/n)${NC}"
read -r RESPONSE

if [[ "$RESPONSE" =~ ^[Yy]$ ]]; then
    echo ""
    echo -e "${CYAN}Launching TechTool Pro...${NC}"
    open -a "Techtool Pro" 2>/dev/null || open -a "TechTool Pro" 2>/dev/null
    echo ""
    echo "Once launched:"
    echo "  1. Go to: TechTool Pro menu"
    echo "  2. Select: Check for Update..."
    echo "  3. Install version 21.0.6"
    echo ""
else
    echo ""
    echo -e "${YELLOW}Update manually when ready.${NC}"
    echo ""
fi

echo -e "${GREEN}✓ Update check complete!${NC}"
echo ""
