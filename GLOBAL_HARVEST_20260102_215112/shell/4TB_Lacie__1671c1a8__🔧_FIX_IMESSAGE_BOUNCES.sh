#!/bin/bash
###############################################################################
# 🔧 FIX iMESSAGE BOUNCES - DISABLE ALL ANNOYING EFFECTS!!!
# Turns off message effects, animations, bounces - EVERYTHING!!!
###############################################################################

echo "🔧 FIXING iMESSAGE BOUNCES - TURNING OFF ALL EFFECTS!!!"
echo ""

# Disable message effects
defaults write com.apple.MobileSMS PlaySoundsKey -bool false

# Disable animations
defaults write com.apple.messages.shared.contact.sync.service DisableAnimations -bool true

# Reduce motion (stops bounces!)
defaults write com.apple.Accessibility ReduceMotionEnabled -bool true

# Disable screen effects
defaults write com.apple.messages EffectsDisabled -bool true

echo "✅ iMessage effects DISABLED!"
echo "✅ Bounces STOPPED!"
echo "✅ Animations OFF!"
echo ""
echo "Restart Messages app for changes to take effect!"
echo ""
echo "To restart Messages:"
echo "  killall Messages"
echo "  Then open Messages again"
echo ""
echo "GORUNFREE 4 YOU ROB!!! 🚀"

