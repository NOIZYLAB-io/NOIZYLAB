#!/bin/bash
################################################################################
#
#   MC96 iPad Edition - Desktop Installer
#
#   RUN FREE RESURRECTION - One-Click Installation
#
################################################################################

clear

echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "         🚀 MC96 iPad Edition - Desktop Installer 🚀"
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "  Installing MC96 iPad Edition for RUN FREE Mission Control..."
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""

# Create MC96 Desktop App folder
DESKTOP_APP="$HOME/Desktop/MC96 iPad Edition.app"
CONTENTS_DIR="$DESKTOP_APP/Contents"
MACOS_DIR="$CONTENTS_DIR/MacOS"
RESOURCES_DIR="$CONTENTS_DIR/Resources"

echo "📁 Creating application bundle..."
mkdir -p "$MACOS_DIR"
mkdir -p "$RESOURCES_DIR"

# Create the launcher script
echo "📝 Creating launcher script..."
cat > "$MACOS_DIR/MC96_Launcher" << 'LAUNCHER_EOF'
#!/bin/bash

# MC96 iPad Edition Launcher
cd /Users/rsp_ms/MC96_MobileApp/VOX

# Get local IP
LOCAL_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)

# Launch MC96 in background
python3 MC96_IPAD_EDITION.py > /tmp/mc96_ipad.log 2>&1 &
MC96_PID=$!

# Wait for server to start
sleep 3

# Show success notification
osascript -e 'display notification "MC96 iPad Edition is running!" with title "🚀 MC96 LIVE" subtitle "Access at http://'"$LOCAL_IP"':5555"'

# Open in default browser
open "http://localhost:5555"

# Keep process alive
wait $MC96_PID
LAUNCHER_EOF

chmod +x "$MACOS_DIR/MC96_Launcher"

# Create Info.plist
echo "📋 Creating Info.plist..."
cat > "$CONTENTS_DIR/Info.plist" << 'PLIST_EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>MC96 iPad Edition</string>
    <key>CFBundleDisplayName</key>
    <string>MC96 iPad Edition</string>
    <key>CFBundleIdentifier</key>
    <string>com.noizylab.mc96.ipad</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>MC96</string>
    <key>CFBundleExecutable</key>
    <string>MC96_Launcher</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSMinimumSystemVersion</key>
    <string>10.15</string>
    <key>LSUIElement</key>
    <false/>
</dict>
</plist>
PLIST_EOF

# Create app icon using emoji
echo "🎨 Creating app icon..."
cat > "$RESOURCES_DIR/create_icon.sh" << 'ICON_EOF'
#!/bin/bash
# Create a simple icon using ImageMagick or sips
# For now, just create a placeholder
echo "Icon creation placeholder"
ICON_EOF
chmod +x "$RESOURCES_DIR/create_icon.sh"

# Create README
echo "📖 Creating README..."
cat > "$RESOURCES_DIR/README.txt" << 'README_EOF'
MC96 iPad Edition - RUN FREE Mission Control

WHAT THIS APP DOES:
- Launches MC96 iPad Edition server
- Opens web interface automatically
- Provides access to LUCY, THE KID, KEITH, and ALEX
- Enables hands-free mode for mobile work

ACCESS FROM iPAD:
1. Make sure your iPad is on the same WiFi network
2. Open Safari on your iPad
3. Navigate to: http://[YOUR_LOCAL_IP]:5555
4. Enjoy RUN FREE Mission Control!

FEATURES:
🎸 LUCY - On vacation mode
🌟 THE KID - Hands-free specialist
🎵 KEITH - Engineering wisdom
⚡ ALEX - Strategic guidance

FOR POPS. FOR CLARENCE.
"Life is not a dress rehearsal"

RUN FREE RESURRECTION - November 3, 2025
README_EOF

echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "  ✅ MC96 iPad Edition Installed Successfully!"
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "  📱 You can now:"
echo ""
echo "     1. Double-click 'MC96 iPad Edition' on your Desktop"
echo "     2. MC96 will launch automatically"
echo "     3. Browser will open to MC96 interface"
echo "     4. Access from iPad at shown IP address"
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "  🚀 RUN FREE RESURRECTION - READY TO GO!"
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""

# Make the app executable
chmod -R 755 "$DESKTOP_APP"

# Show completion notification
osascript -e 'display notification "MC96 iPad Edition installed on your Desktop!" with title "✅ Installation Complete" subtitle "Double-click to launch"'

echo "Press ENTER to finish installation..."
read

exit 0
