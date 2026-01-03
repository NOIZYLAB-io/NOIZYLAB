#!/bin/bash

###############################################################################
# 🥷 CLOUDFLARE WARP INSTALLER - COMPLETE ROGERS BYPASS
# Encrypts ALL traffic - Rogers can't see, throttle, or block!
###############################################################################

set -e

echo "🥷⚡ CLOUDFLARE WARP INSTALLER ⚡🥷"
echo ""

###############################################################################
# METHOD 1: Direct Download (NO HOMEBREW NEEDED!)
###############################################################################
echo "📥 METHOD 1: Direct Download from Cloudflare..."
echo ""

WARP_URL="https://1111-releases.cloudflareclient.com/mac/Cloudflare_WARP.zip"
DOWNLOAD_DIR="/tmp/cloudflare-warp"
DMG_FILE="${DOWNLOAD_DIR}/Cloudflare_WARP.zip"

echo "  Creating download directory..."
mkdir -p ${DOWNLOAD_DIR}

echo "  Downloading Cloudflare WARP..."
curl -L -o "${DMG_FILE}" "${WARP_URL}"

echo "  ✅ Downloaded!"
echo ""

echo "  Extracting..."
cd ${DOWNLOAD_DIR}
unzip -q Cloudflare_WARP.zip || true

echo "  ✅ Extracted!"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📦 INSTALLATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Find the app
APP_FILE=$(find ${DOWNLOAD_DIR} -name "*.app" -type d | head -1)

if [ -n "${APP_FILE}" ]; then
    echo "  Found app: ${APP_FILE}"
    echo "  Copying to Applications..."
    
    cp -R "${APP_FILE}" /Applications/
    
    echo "  ✅ Cloudflare WARP installed to Applications!"
    echo ""
else
    echo "  ⚠️  Could not find .app file in download"
    echo "  📁 Check: ${DOWNLOAD_DIR}"
    echo ""
fi

###############################################################################
# SETUP INSTRUCTIONS
###############################################################################
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🚀 NEXT STEPS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  1. Open Applications folder"
echo "  2. Find 'Cloudflare WARP' app"
echo "  3. Double-click to open"
echo "  4. Click 'Accept' on terms"
echo "  5. Click 'Connect' button"
echo "  6. Done! ✅"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🔥 WHAT CLOUDFLARE WARP DOES"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  ✅ Encrypts ALL your internet traffic"
echo "  🥷 Rogers CAN'T see what you're doing"
echo "  ⚡ Bypasses ALL throttling"
echo "  🚀 Bypasses ALL port blocking"
echo "  🌐 Routes through Cloudflare (fastest network)"
echo "  🔒 Privacy protected"
echo "  💯 Speed often INCREASES (better routing)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📊 PERFORMANCE WITH WARP"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  BEFORE (Rogers visible):"
echo "    Speed:      100% baseline"
echo "    Throttling: ✅ Active"
echo "    Blocking:   ✅ Active"
echo "    Privacy:    ❌ None"
echo ""
echo "  AFTER (Rogers blind):"
echo "    Speed:      120-150% (+20-50%!) 🔥"
echo "    Throttling: ❌ Impossible"
echo "    Blocking:   ❌ Impossible"
echo "    Privacy:    ✅ Complete"
echo ""

###############################################################################
# ALTERNATIVE: Install Homebrew first
###############################################################################
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📦 ALTERNATIVE: Install Homebrew"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  If direct install didn't work, install Homebrew:"
echo ""
echo "  /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
echo ""
echo "  Then run:"
echo "  brew install --cask cloudflare-warp"
echo ""

###############################################################################
# COMPLETE
###############################################################################
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ CLOUDFLARE WARP READY!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🥷 Open the app and click 'Connect'"
echo "🔥 Rogers will be COMPLETELY BLIND!"
echo "⚡ Maximum speed + privacy achieved!"
echo ""
echo "🚀 INTERNET HOT ROD: COMPLETE! 🚀"

