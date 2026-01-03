#!/bin/bash
# iOS Email Deployment Script
# Helps deploy email configuration to all iOS devices

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     🚀 iOS EMAIL DEPLOYMENT - EXECUTION SCRIPT          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

PROFILES_DIR="$HOME/.it_genius/ios_profiles"
COMBINED_PROFILE="$PROFILES_DIR/all_email_accounts.mobileconfig"

# Check if profiles exist
if [ ! -f "$COMBINED_PROFILE" ]; then
    echo "⚠️  Profiles not found. Generating now..."
    cd "$(dirname "$0")"
    python3 create_ios_email_profiles.py
    echo ""
fi

echo "✅ Profiles ready!"
echo ""
echo "📁 Profile Location:"
echo "   $COMBINED_PROFILE"
echo ""

# List available profiles
echo "📋 Available Profiles:"
ls -lh "$PROFILES_DIR"/*.mobileconfig 2>/dev/null | awk '{print "   ✅", $9}'
echo ""

# Open Finder for AirDrop
echo "🚀 Opening Finder for AirDrop..."
echo "   → Select 'all_email_accounts.mobileconfig'"
echo "   → Right-click → Share → AirDrop"
echo "   → Select your iOS device"
echo ""

open "$PROFILES_DIR"

echo "📱 INSTALLATION STEPS:"
echo ""
echo "1. AirDrop 'all_email_accounts.mobileconfig' to iOS device"
echo "2. On iOS: Open the file when it arrives"
echo "3. Go to Settings → Profile Downloaded"
echo "4. Tap 'Install'"
echo "5. Enter device passcode"
echo "6. Enter email passwords for each account"
echo "7. Verify in Settings → Mail → Accounts"
echo ""
echo "✅ Repeat for all iOS devices!"
echo ""
echo "📚 See DEPLOY_TO_IOS.md for detailed instructions"

