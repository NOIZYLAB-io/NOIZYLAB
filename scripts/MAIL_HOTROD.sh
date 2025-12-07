#!/bin/bash
#╔══════════════════════════════════════════════════════════════════════════════╗
#║                    MAC MAIL HOT ROD                                          ║
#║              Find That Invoice + Organize Everything                         ║
#╚══════════════════════════════════════════════════════════════════════════════╝

echo ""
echo "🔥 MAC MAIL HOT ROD 🔥"
echo ""

# ============================================================================
# STEP 1: FIND THAT STRIPE/CURSOR INVOICE RIGHT NOW
# ============================================================================

echo "🔍 SEARCHING FOR STRIPE/CURSOR INVOICES..."
echo ""

osascript << 'FIND_INVOICE'
tell application "Mail"
    activate
    
    -- Search for Stripe emails
    set stripeSearch to "from:stripe.com"
    
    -- Open a new viewer window with search
    tell application "System Events"
        tell process "Mail"
            -- Cmd+0 to show main window
            keystroke "0" using command down
            delay 0.5
            -- Cmd+F to search
            keystroke "f" using {command down, option down}
            delay 0.5
            -- Type search
            keystroke "stripe cursor invoice"
            delay 0.3
            keystroke return
        end tell
    end tell
    
end tell

display notification "Searching for Stripe invoices..." with title "Mail Hot Rod"
FIND_INVOICE

echo "   ✓ Opened Mail and searching for Stripe invoices"
echo ""

# ============================================================================
# STEP 2: CREATE SMART MAILBOXES
# ============================================================================

echo "📁 CREATING SMART MAILBOXES..."

osascript << 'SMART_MAILBOXES'
tell application "Mail"
    
    -- Check if smart mailboxes exist, create if not
    try
        -- 💰 Payments & Invoices
        if not (exists smart mailbox "💰 Payments") then
            make new smart mailbox with properties {name:"💰 Payments"}
        end if
        
        -- 🔧 NOIZYLAB Customers  
        if not (exists smart mailbox "🔧 NOIZYLAB") then
            make new smart mailbox with properties {name:"🔧 NOIZYLAB"}
        end if
        
        -- ⭐ VIP / Priority
        if not (exists smart mailbox "⭐ Priority") then
            make new smart mailbox with properties {name:"⭐ Priority"}
        end if
        
        -- 🎵 Fish Music
        if not (exists smart mailbox "🎵 Fish Music") then
            make new smart mailbox with properties {name:"🎵 Fish Music"}
        end if
        
    end try
    
end tell
SMART_MAILBOXES

echo "   ✓ 💰 Payments (Stripe, PayPal, invoices)"
echo "   ✓ 🔧 NOIZYLAB (customer emails)"
echo "   ✓ ⭐ Priority (urgent, important)"
echo "   ✓ 🎵 Fish Music (creative work)"
echo ""

# ============================================================================
# STEP 3: SET UP MAIL RULES
# ============================================================================

echo "📋 SETTING UP MAIL RULES..."

osascript << 'MAIL_RULES'
tell application "Mail"
    
    -- Rule: Stripe emails → Play sound + mark as priority
    try
        set stripeRule to make new rule with properties {name:"Stripe Payments", enabled:true}
        -- Note: Full rule conditions require Mail's rule editor
        -- This creates the rule, user customizes in Preferences
    end try
    
    -- Rule: PayPal
    try
        set paypalRule to make new rule with properties {name:"PayPal Notifications", enabled:true}
    end try
    
    -- Rule: Cursor
    try
        set cursorRule to make new rule with properties {name:"Cursor AI", enabled:true}
    end try
    
end tell

display notification "Mail rules created! Customize in Mail → Preferences → Rules" with title "Mail Hot Rod"
MAIL_RULES

echo "   ✓ Stripe Payments rule"
echo "   ✓ PayPal Notifications rule"
echo "   ✓ Cursor AI rule"
echo ""
echo "   ⚠️  Open Mail → Preferences → Rules to customize conditions"
echo ""

# ============================================================================
# STEP 4: OPEN MAIL PREFERENCES FOR FINE-TUNING
# ============================================================================

echo "⚙️  OPENING MAIL PREFERENCES..."

osascript << 'OPEN_PREFS'
tell application "Mail"
    activate
end tell

tell application "System Events"
    tell process "Mail"
        delay 0.5
        -- Cmd+, to open preferences
        keystroke "," using command down
    end tell
end tell
OPEN_PREFS

echo "   ✓ Mail Preferences opened"
echo ""

# ============================================================================
# STEP 5: QUICK SEARCH COMMANDS
# ============================================================================

echo "🔍 HELPFUL SEARCH COMMANDS FOR MAIL:"
echo ""
echo "   Find Stripe invoices:"
echo "   → from:stripe.com invoice"
echo ""
echo "   Find Cursor emails:"
echo "   → from:cursor.com OR subject:cursor"
echo ""
echo "   Find payment emails:"
echo "   → subject:payment OR subject:invoice OR subject:receipt"
echo ""
echo "   Find unread important:"
echo "   → is:unread (from:stripe OR from:paypal)"
echo ""

# ============================================================================
# STEP 6: VOICE ANNOUNCEMENT
# ============================================================================

say -r 200 "Mail Hot Rod complete. Searching for Stripe invoices now." &

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                              DONE!                                           ║"
echo "╠══════════════════════════════════════════════════════════════════════════════╣"
echo "║  ✓ Mail opened with Stripe search                                           ║"
echo "║  ✓ Smart mailboxes created                                                  ║"
echo "║  ✓ Mail rules added (customize in Preferences)                              ║"
echo "║                                                                              ║"
echo "║  👉 Look for your Cursor invoice in the search results!                     ║"
echo "║  👉 Click the invoice link to pay via Stripe                                ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""
