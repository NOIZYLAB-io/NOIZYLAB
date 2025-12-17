#!/bin/bash
# QUICK_EMAIL_SETUP.command
# One-click email alias setup - fully automated

clear

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     🚀 QUICK EMAIL ALIASES SETUP (One-Click)                        ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# Open all necessary pages automatically
echo "📧 Opening Gmail settings..."
open "https://mail.google.com/mail/u/0/#settings/accounts"

sleep 2

echo "📧 Opening ImprovMX (free email forwarding)..."
open "https://improvmx.com/"

sleep 2

echo "📧 Opening setup guide..."
open "$HOME/Desktop/EMAIL_SETUP_VOICE_GUIDE.txt"

echo ""
echo "✅ All pages opened!"
echo ""
echo "📋 Next steps (use voice or keyboard):"
echo ""
echo "GMAIL SETUP:"
echo "  1. Page is open - scroll to 'Send mail as'"
echo "  2. Click 'Add another email address'"
echo "  3. Add: rp@fishmusicinc.com"
echo "  4. Verify via email"
echo "  5. Repeat for: rsp@noizylab.ca, help@noizylab.ca"
echo ""
echo "IMPROVMX SETUP (for receiving emails):"
echo "  1. Sign up (free, 2 minutes)"
echo "  2. Add domains: fishmusicinc.com, noizylab.ca"
echo "  3. Forward to: rsplowman@gmail.com"
echo ""
echo "🎤 Voice commands available:"
echo "  Say: 'Click [button name]'"
echo "  Say: 'Type [text]'"
echo "  Say: 'Scroll down'"
echo ""
echo "⌨️  Keyboard shortcuts:"
echo "  TAB: Navigate"
echo "  SPACE: Click"
echo "  RETURN: Submit"
echo ""

say "Email setup pages opened. Follow the on-screen instructions."


