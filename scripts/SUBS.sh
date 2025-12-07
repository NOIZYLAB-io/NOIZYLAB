#!/bin/bash
#╔══════════════════════════════════════════════════════════════════════════════╗
#║                                                                              ║
#║   ███████╗██╗   ██╗██████╗ ███████╗                                         ║
#║   ██╔════╝██║   ██║██╔══██╗██╔════╝                                         ║
#║   ███████╗██║   ██║██████╔╝███████╗                                         ║
#║   ╚════██║██║   ██║██╔══██╗╚════██║                                         ║
#║   ███████║╚██████╔╝██████╔╝███████║                                         ║
#║   ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝                                         ║
#║                                                                              ║
#║              SUBSCRIPTION TRACKER & OPTIMIZER                                ║
#║                   Know Where Your Money Goes                                 ║
#║                                                                              ║
#╚══════════════════════════════════════════════════════════════════════════════╝

DATA_FILE="$HOME/.subscriptions.json"

# ============================================================================
# ROB'S KNOWN/LIKELY SUBSCRIPTIONS
# ============================================================================

show_subscription_audit() {
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                    SUBSCRIPTION AUDIT                                        ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🧠 AI & DEVELOPMENT - THE ESSENTIALS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    printf "%-25s %-12s %-15s %s\n" "SERVICE" "PRICE" "BILLING" "STATUS"
    echo "─────────────────────────────────────────────────────────────────────────────"
    printf "%-25s %-12s %-15s %s\n" "Claude Pro (Opus)" "\$20/mo" "Monthly" "✅ KEEP - Primary AI"
    printf "%-25s %-12s %-15s %s\n" "Cursor Pro" "\$20/mo" "Monthly" "✅ KEEP - Code Editor"
    printf "%-25s %-12s %-15s %s\n" "GitHub Copilot" "\$10/mo" "Monthly" "⚠️  REVIEW - Redundant?"
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "☁️  APPLE ECOSYSTEM"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    printf "%-25s %-12s %-15s %s\n" "iCloud+" "~\$13/mo" "Monthly" "✅ KEEP - 2TB Storage"
    printf "%-25s %-12s %-15s %s\n" "Apple Music" "\$11/mo" "Monthly" "❓ CHECK - Using it?"
    printf "%-25s %-12s %-15s %s\n" "Apple TV+" "\$10/mo" "Monthly" "❓ CHECK - Using it?"
    printf "%-25s %-12s %-15s %s\n" "Apple One Bundle" "\$26/mo" "Monthly" "💡 CONSIDER - Saves \$\$"
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🛠️  BUSINESS & PRODUCTIVITY"  
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    printf "%-25s %-12s %-15s %s\n" "Cloudflare (Free)" "\$0" "N/A" "✅ FREE - Workers/DNS"
    printf "%-25s %-12s %-15s %s\n" "Domain: noizylab.ca" "~\$20/yr" "Annual" "✅ KEEP - Business"
    printf "%-25s %-12s %-15s %s\n" "Domain: fishmusic.ca" "~\$20/yr" "Annual" "✅ KEEP - Creative"
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "❓ POSSIBLE - CHECK YOUR ACCOUNTS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    printf "%-25s %-12s %-15s %s\n" "Spotify" "\$11/mo" "Monthly" "❓ Or Apple Music?"
    printf "%-25s %-12s %-15s %s\n" "Netflix" "\$16-23/mo" "Monthly" "❓ Still using?"
    printf "%-25s %-12s %-15s %s\n" "Adobe CC" "\$55+/mo" "Monthly" "❓ Or alternatives?"
    printf "%-25s %-12s %-15s %s\n" "Microsoft 365" "\$10/mo" "Monthly" "❓ Need it?"
    printf "%-25s %-12s %-15s %s\n" "Dropbox" "\$12/mo" "Monthly" "⚠️  CANCEL - Use iCloud"
    printf "%-25s %-12s %-15s %s\n" "Google One" "\$3-10/mo" "Monthly" "⚠️  CANCEL - Use iCloud"
    printf "%-25s %-12s %-15s %s\n" "ChatGPT Plus" "\$20/mo" "Monthly" "⚠️  CANCEL - Have Claude"
    echo ""
}

# ============================================================================
# RECOMMENDED STACK
# ============================================================================

show_recommended() {
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                    💎 RECOMMENDED STACK FOR ROB                              ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ KEEP THESE (Essential)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "   🧠 Claude Pro (Opus)         \$20/mo   - Your primary AI brain"
    echo "   💻 Cursor Pro                \$20/mo   - AI code editor"
    echo "   ☁️  iCloud+ 2TB               \$13/mo   - Apple ecosystem storage"
    echo "   🌐 Domains (2)               ~\$3/mo   - noizylab.ca + fishmusic.ca"
    echo ""
    echo "   ─────────────────────────────────────"
    echo "   ESSENTIAL TOTAL:             ~\$56/mo"
    echo ""
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "⚠️  REVIEW THESE (Maybe Cancel)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "   🤖 GitHub Copilot            \$10/mo   - Cursor has AI built in!"
    echo "   🤖 ChatGPT Plus              \$20/mo   - You have Claude Opus!"
    echo "   📦 Dropbox                   \$12/mo   - Use iCloud instead"
    echo "   📦 Google One                \$10/mo   - Use iCloud instead"
    echo ""
    echo "   ─────────────────────────────────────"
    echo "   POTENTIAL SAVINGS:           ~\$52/mo = \$624/year!"
    echo ""
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "💡 OPTIMIZATION TIPS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "   • Cursor Pro INCLUDES AI coding - Copilot may be redundant"
    echo "   • Claude Opus is your AI - ChatGPT Plus is duplicate"
    echo "   • iCloud 2TB covers storage - cancel Dropbox/Google One"
    echo "   • Apple One bundle could save if you use Music+TV+"
    echo "   • Annual billing often saves 15-20%"
    echo ""
}

# ============================================================================
# FIND SUBSCRIPTIONS IN MAIL
# ============================================================================

search_mail_for_subs() {
    echo ""
    echo "🔍 Searching Mail for subscription receipts..."
    echo ""
    
    osascript << 'EOF'
tell application "Mail"
    activate
end tell

delay 0.5

tell application "System Events"
    tell process "Mail"
        keystroke "f" using {command down, option down}
        delay 0.3
        keystroke "receipt OR invoice OR subscription OR billing OR renewal"
        keystroke return
    end tell
end tell
EOF
    
    echo "   ✓ Mail opened - searching for all receipts/invoices"
    echo ""
    echo "   Look for emails from:"
    echo "   • receipts@stripe.com"
    echo "   • no-reply@apple.com"
    echo "   • billing@cursor.sh"
    echo "   • noreply@github.com"
    echo "   • payments@anthropic.com"
    echo ""
}

# ============================================================================
# QUICK LINKS TO MANAGE SUBSCRIPTIONS
# ============================================================================

open_subscription_managers() {
    echo ""
    echo "🔗 Opening subscription management pages..."
    echo ""
    
    # Apple Subscriptions
    echo "   Opening Apple subscriptions..."
    open "https://apps.apple.com/account/subscriptions"
    
    sleep 0.5
    
    # Claude/Anthropic
    echo "   Opening Claude account..."
    open "https://claude.ai/settings"
    
    sleep 0.5
    
    # Cursor
    echo "   Opening Cursor billing..."
    open "https://cursor.com/settings"
    
    sleep 0.5
    
    # GitHub
    echo "   Opening GitHub billing..."
    open "https://github.com/settings/billing"
    
    echo ""
    echo "   ✅ All subscription pages opened!"
    echo ""
}

# ============================================================================
# SUBSCRIPTION TRACKER DATA
# ============================================================================

init_tracker() {
    if [ ! -f "$DATA_FILE" ]; then
        cat > "$DATA_FILE" << 'JSON'
{
  "subscriptions": [
    {
      "name": "Claude Pro",
      "provider": "Anthropic",
      "price": 20.00,
      "currency": "USD",
      "billing": "monthly",
      "category": "AI",
      "status": "active",
      "essential": true,
      "url": "https://claude.ai/settings",
      "notes": "Primary AI - Opus access"
    },
    {
      "name": "Cursor Pro",
      "provider": "Cursor",
      "price": 20.00,
      "currency": "USD", 
      "billing": "monthly",
      "category": "Development",
      "status": "active",
      "essential": true,
      "url": "https://cursor.com/settings",
      "notes": "AI Code Editor"
    },
    {
      "name": "iCloud+ 2TB",
      "provider": "Apple",
      "price": 12.99,
      "currency": "CAD",
      "billing": "monthly",
      "category": "Storage",
      "status": "active",
      "essential": true,
      "url": "https://apps.apple.com/account/subscriptions",
      "notes": "Apple ecosystem storage"
    },
    {
      "name": "GitHub Copilot",
      "provider": "GitHub",
      "price": 10.00,
      "currency": "USD",
      "billing": "monthly",
      "category": "Development",
      "status": "review",
      "essential": false,
      "url": "https://github.com/settings/billing",
      "notes": "May be redundant with Cursor"
    }
  ],
  "last_audit": "",
  "monthly_total": 0,
  "annual_total": 0
}
JSON
        echo "   ✓ Created subscription tracker at $DATA_FILE"
    fi
}

# ============================================================================
# MAIN MENU
# ============================================================================

menu() {
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                    SUBSCRIPTION MANAGER                                      ║"
    echo "╠══════════════════════════════════════════════════════════════════════════════╣"
    echo "║                                                                              ║"
    echo "║   [1] 📋 Show Subscription Audit                                            ║"
    echo "║   [2] 💎 Show Recommended Stack                                             ║"
    echo "║   [3] 🔍 Search Mail for Receipts                                           ║"
    echo "║   [4] 🔗 Open All Subscription Pages                                        ║"
    echo "║   [5] 💳 Open Stripe Dashboard                                              ║"
    echo "║                                                                              ║"
    echo "║   [Q] Quit                                                                  ║"
    echo "║                                                                              ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo ""
}

# ============================================================================
# MAIN
# ============================================================================

main() {
    init_tracker
    
    say -r 200 "Subscription manager ready" &
    
    while true; do
        menu
        read -n1 -p "Select: " choice
        echo ""
        
        case $choice in
            1) show_subscription_audit ;;
            2) show_recommended ;;
            3) search_mail_for_subs ;;
            4) open_subscription_managers ;;
            5) open "https://dashboard.stripe.com" ;;
            q|Q) say "Goodbye" & exit 0 ;;
            *) ;;
        esac
    done
}

# Quick run
case "${1:-}" in
    --audit) show_subscription_audit ;;
    --recommend) show_recommended ;;
    --search) search_mail_for_subs ;;
    --open) open_subscription_managers ;;
    --all)
        show_subscription_audit
        show_recommended
        open_subscription_managers
        ;;
    *) main ;;
esac
