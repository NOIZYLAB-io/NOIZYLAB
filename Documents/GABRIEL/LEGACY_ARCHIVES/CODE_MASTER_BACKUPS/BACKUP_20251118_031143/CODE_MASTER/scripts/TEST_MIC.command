#!/bin/bash
# TEST_MIC.command
# Test your microphone setup

clear

echo "🎤 TESTING YOUR MICROPHONE..."
echo ""

echo "Opening Sound settings to test mic..."
open "x-apple.systempreferences:com.apple.preference.sound"

sleep 2

echo ""
echo "📋 TEST STEPS:"
echo ""
echo "1. Sound settings opened"
echo "2. Click 'Input' tab"
echo "3. Select your mic:"
echo "   • iPhone Microphone"
echo "   • OR Beats Studio Pro"
echo "4. Speak into your mic"
echo "5. Watch the level meter - it should move when you speak"
echo ""
echo "If the meter moves → Mic is working! ✅"
echo "If it doesn't move → Check connection"
echo ""

say "Sound settings opened. Select your microphone and speak into it. Watch the level meter to see if it's working."

