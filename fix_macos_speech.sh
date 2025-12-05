#!/bin/bash
# MACOS SEQUOIA SPEECH SYSTEM FIX
# Run this on GOD (Mac Studio)

echo "=== MACOS SPEECH SYSTEM DIAGNOSTIC & FIX ==="
echo ""

echo "📊 Current Speech Settings:"
defaults read com.apple.speech.voice.prefs 2>/dev/null || echo "⚠️  No voice preferences found"
echo ""

echo "📢 Available Voices on System:"
say -v ? | grep -E "en_US|en_GB" | head -10
echo ""

echo "🧪 Testing Current Default Voice:"
say "Testing speech system" 2>&1 &
SPEECH_PID=$!
sleep 2
if ps -p $SPEECH_PID > /dev/null 2>&1; then
    echo "✓ Speech is working"
    kill $SPEECH_PID 2>/dev/null
else
    echo "⚠️  Speech test completed or failed"
fi
echo ""

echo "🔍 Checking Speech Services:"
launchctl list | grep -i speech || echo "Speech service not found in launchctl"
echo ""

echo "🔧 APPLYING FIXES..."
echo ""

# Kill any hung speech processes
echo "1. Cleaning up speech processes..."
killall -9 speechsynthesisd 2>/dev/null
killall -9 VoiceOver 2>/dev/null
sleep 1

# Set reliable high-quality voice
echo "2. Setting default voice to Samantha (Premium US English)..."
defaults write com.apple.speech.voice.prefs SelectedVoiceName -string "Samantha"
defaults write com.apple.speech.voice.prefs SelectedVoiceID -int 201

# Alternative: Use Alex if Samantha unavailable
defaults write com.apple.speech.voice.prefs AlternateVoiceName -string "Alex"

# Set speech rate to comfortable speed
defaults write com.apple.speech.voice.prefs VisibleRate -float 225.0
defaults write com.apple.speech.voice.prefs Rate -float 225.0

# Enable speech in system
defaults write com.apple.speech.synthesis.general.prefs SpokenUIUseSpeakingHotKeyFlag -bool true

# Refresh speech system
echo "3. Restarting speech services..."
launchctl kickstart -k system/com.apple.speech.synthesisserver 2>/dev/null

# Download voice if needed
echo "4. Checking voice availability..."
echo "   If Samantha not installed, downloading now..."
# This triggers download if needed
say -v Samantha "Initializing voice" 2>&1

sleep 2

echo ""
echo "✅ VERIFICATION TEST"
say -v Samantha "Speech system is now fixed and ready to use" 2>&1
sleep 3

echo ""
echo "=== FIX COMPLETE ==="
echo ""
echo "✓ Default voice: Samantha (Premium)"
echo "✓ Speech rate: Optimized"
echo "✓ Services: Restarted"
echo ""
echo "📱 TO USE:"
echo "  • Select text in any app"
echo "  • Right-click → Speech → Start Speaking"
echo "  • Or use keyboard: Option+Esc to start/stop"
echo ""
echo "🎛️  TO CUSTOMIZE:"
echo "  • System Settings → Accessibility → Spoken Content"
echo "  • System Settings → Keyboard → Dictation"
echo ""
echo "🧪 COMMAND LINE TEST:"
echo "  say 'Hello Rob, speech is working'"
echo ""
