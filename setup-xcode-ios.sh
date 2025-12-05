#!/bin/bash
# Xcode & iOS Setup for Email Development
# ========================================

echo "📱 Xcode & iOS Email Setup"
echo "=========================="
echo ""

# Check Xcode
if ! command -v xcodebuild &> /dev/null; then
    echo "📦 Installing Xcode Command Line Tools..."
    xcode-select --install
    echo "✅ Xcode tools installed"
else
    echo "✅ Xcode already installed"
fi

# Check for connected iOS devices
echo ""
echo "📱 Checking for iOS devices..."
devices=$(xcrun xctrace list devices 2>/dev/null | grep -i "iphone\|ipad" || echo "No devices found")

if [ "$devices" != "No devices found" ]; then
    echo "✅ iOS devices detected:"
    echo "$devices"
else
    echo "⚠️  No iOS devices connected"
    echo "   Connect your iPhone/iPad via USB"
fi

# Create iOS project structure
PROJECT_DIR="/Users/m2ultra/NOIZYLAB/ios-email-setup"
mkdir -p "$PROJECT_DIR"

echo ""
echo "📁 Creating iOS project structure..."
cat > "$PROJECT_DIR/README.md" << 'EOF'
# iOS Email Setup Project

## Setup Steps

### 1. Open Xcode
```bash
open -a Xcode
```

### 2. Create New Project
- File → New → Project
- iOS → App
- Name: NoizyLabEmail
- Team: Select your Apple ID

### 3. Configure Signing
- Select project in navigator
- Signing & Capabilities
- Add your Apple ID team
- Enable "Automatically manage signing"

### 4. Connect Device
- Connect iPhone/iPad via USB
- Trust computer on device
- Select device in Xcode toolbar
- Enable Developer Mode (Settings → Privacy & Security)

### 5. Build & Run
- Click Run button
- App will install on device

## Email Configuration

Use the generated iOS configs from:
~/NOIZYLAB/email-intelligence/ios-configs/
EOF

echo "✅ Project structure created: $PROJECT_DIR"

# Generate email configs
echo ""
echo "📧 Generating email configurations..."
cd /Users/m2ultra/NOIZYLAB/email-intelligence
python3 setup-ios-emails.py >/dev/null 2>&1

echo ""
echo "✅ Xcode & iOS setup complete!"
echo ""
echo "📋 Next Steps:"
echo "   1. Open Xcode: open -a Xcode"
echo "   2. Create new iOS project"
echo "   3. Use configs from: ios-configs/"
echo "   4. Build and run on device"
echo ""

