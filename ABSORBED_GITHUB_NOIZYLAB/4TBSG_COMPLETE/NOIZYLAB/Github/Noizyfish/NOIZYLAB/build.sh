#!/bin/zsh
#
# Build script for VoiceCommander installer
# Places LogicVoiceCommands.plist into Logic Pro support folder
#

# Config
IDENTIFIER="com.noizyfish.voicecommander"
VERSION="1.0.0"
PKGNAME="VoiceCommander-${VERSION}.pkg"

# Clean old build
rm -f "$PKGNAME"

# Build package
pkgbuild \
  --root payload \
  --identifier "$IDENTIFIER" \
  --version "$VERSION" \
  --install-location / \
  "$PKGNAME"

echo "✅ Build complete: $PKGNAME"

