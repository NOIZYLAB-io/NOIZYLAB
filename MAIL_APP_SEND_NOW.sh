#!/bin/bash
# 🍎 USE MAIL.APP TO SEND EMAIL - NO PASSWORDS!!

echo ""
echo "🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎"
echo "  SENDING VIA APPLE MAIL.APP - NO PASSWORDS!!"
echo "🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎"
echo ""

TO_EMAIL=${1:-"rsplowman@icloud.com"}

echo "📧 Sending test email to: $TO_EMAIL"
echo "🍎 Using Mail.app..."
echo ""

# Use AppleScript to send via Mail.app
osascript << EOF
tell application "Mail"
    set newMessage to make new outgoing message with properties {subject:"🍎 EMAIL WORKS via Mail.app!!", content:"ROB - If you see this, MAIL.APP WORKS!!

Sent: $(date)
Method: Apple Mail.app
No passwords needed!!

If Mail.app is configured with rsplowman@icloud.com, 
this email was sent using that account!

GORUNFREE!! 🚀

CB_01", visible:false}
    
    tell newMessage
        make new to recipient at end of to recipients with properties {address:"$TO_EMAIL"}
        send
    end tell
end tell
EOF

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
    echo "  ✅✅✅ EMAIL SENT VIA MAIL.APP!! ✅✅✅"
    echo "🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
    echo ""
    echo "📬 Email sent to: $TO_EMAIL"
    echo "⏰ Time: $(date +%H:%M:%S)"
    echo ""
    echo "CHECK YOUR INBOX NOW!!"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🍎 MAIL.APP WORKS!! NO PASSWORDS!! 🍎"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "This used YOUR configured email in Mail.app!"
    echo "No SMTP setup needed!!"
    echo ""
    echo "GORUNFREE!! 🚀"
    echo ""
else
    echo ""
    echo "❌ Mail.app might not be configured yet"
    echo ""
    echo "TO FIX:"
    echo "1. Open Mail.app"
    echo "2. Add account: rsplowman@icloud.com"
    echo "3. Let it sync"
    echo "4. Run this script again"
    echo ""
fi

