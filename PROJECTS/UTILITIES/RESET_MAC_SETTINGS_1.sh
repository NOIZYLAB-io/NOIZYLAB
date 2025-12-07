#!/bin/bash
# ============================================
# RESET macOS SEQUOIA TO APPLE DEFAULTS
# For GOD (Mac Studio M2 Ultra)
# ============================================
# GORUNFREE - One command, everything reset
# ============================================

echo "=========================================="
echo "RESETTING macOS SETTINGS TO APPLE DEFAULTS"
echo "$(date)"
echo "=========================================="

# Kill System Settings if open
killall "System Settings" 2>/dev/null

echo "[1/12] Resetting Dock..."
defaults delete com.apple.dock 2>/dev/null
killall Dock

echo "[2/12] Resetting Finder..."
defaults delete com.apple.finder 2>/dev/null
killall Finder

echo "[3/12] Resetting Menu Bar..."
defaults delete com.apple.controlcenter 2>/dev/null

echo "[4/12] Resetting Keyboard settings..."
defaults delete com.apple.keyboard 2>/dev/null
defaults delete com.apple.HIToolbox 2>/dev/null

echo "[5/12] Resetting Trackpad/Mouse..."
defaults delete com.apple.AppleMultitouchTrackpad 2>/dev/null
defaults delete com.apple.driver.AppleBluetoothMultitouch.trackpad 2>/dev/null
defaults delete com.apple.mouse 2>/dev/null

echo "[6/12] Resetting Sound settings..."
defaults delete com.apple.sound.beep 2>/dev/null
defaults delete com.apple.systemsound 2>/dev/null

echo "[7/12] Resetting Display settings..."
defaults delete com.apple.windowserver 2>/dev/null

echo "[8/12] Resetting Accessibility..."
defaults delete com.apple.Accessibility 2>/dev/null
defaults delete com.apple.universalaccess 2>/dev/null

echo "[9/12] Resetting Network preferences..."
defaults delete com.apple.networkConnect 2>/dev/null

echo "[10/12] Resetting Spotlight..."
defaults delete com.apple.Spotlight 2>/dev/null

echo "[11/12] Resetting Global Preferences..."
defaults delete NSGlobalDomain 2>/dev/null

echo "[12/12] Clearing preference caches..."
rm -rf ~/Library/Preferences/ByHost/* 2>/dev/null
rm -rf ~/Library/Caches/com.apple.preferencepanes* 2>/dev/null

echo ""
echo "=========================================="
echo "RESET COMPLETE"
echo "=========================================="
echo ""
echo "RESTART REQUIRED - Run this command:"
echo "sudo shutdown -r now"
echo ""
echo "Or say: 'Hey Siri, restart my Mac'"
echo "=========================================="
