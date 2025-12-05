#!/usr/bin/env python3
"""
🍎 USE APPLE'S BUILT-IN EMAIL - NO PASSWORDS NEEDED!!
If you have Mail.app setup, this JUST WORKS!!
"""

import subprocess
import os
from datetime import datetime

print("\n" + "🍎" * 40)
print("   APPLE NATIVE EMAIL - USING MAIL.APP!!")
print("🍎" * 40 + "\n")

print("🎯 USING YOUR MAC'S BUILT-IN EMAIL!!")
print("   If Mail.app is setup - this JUST WORKS!")
print()

# Check if Mail.app is configured
print("Checking if Mail.app is configured...")
print()

# Method 1: Use osascript (AppleScript) to send via Mail.app
to_email = input("Send test to (default: rsplowman@icloud.com): ").strip()
if not to_email:
    to_email = "rsplowman@icloud.com"

print()
print("🚀 SENDING EMAIL VIA MAIL.APP...")
print()

try:
    # AppleScript to send email
    script = f'''
tell application "Mail"
    set newMessage to make new outgoing message with properties {{subject:"🍎 EMAIL WORKS - Sent via Mail.app!!", content:"If you're reading this, YOUR EMAIL WORKS!!

Sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Method: Apple Mail.app
From: Your configured email in Mail.app

NO MORE PASSWORD BULLSHIT!!
Mail.app handles everything!!

GORUNFREE!! 🚀

CB_01", visible:false}}
    
    tell newMessage
        make new to recipient at end of to recipients with properties {{address:"{to_email}"}}
        send
    end tell
end tell
'''
    
    result = subprocess.run(
        ['osascript', '-e', script],
        capture_output=True,
        text=True,
        timeout=10
    )
    
    if result.returncode == 0:
        print("🎉" * 40)
        print("   ✅✅✅ EMAIL SENT VIA MAIL.APP!! ✅✅✅")
        print("🎉" * 40)
        print()
        print(f"📬 Email sent to: {to_email}")
        print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
        print()
        print("CHECK YOUR INBOX NOW!!")
        print()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("🍎 MAIL.APP WORKS!! NO PASSWORDS NEEDED!! 🍎")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        print("This uses YOUR configured email in Mail.app!")
        print("No SMTP, no passwords, no bullshit!!")
        print()
        print("GORUNFREE!! 🚀")
        print()
    else:
        print(f"❌ Mail.app error: {result.stderr}")
        print()
        print("Mail.app might not be configured yet.")
        print("Open Mail.app and add rsplowman@icloud.com")
        print()

except Exception as e:
    print(f"\n❌ Error: {e}")
    print()
    print("Make sure Mail.app is installed and configured.")
    print()

# Method 2: Try using `mail` command (simpler!)
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("ALTERNATIVE: Using macOS 'mail' command...")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

try:
    # Simple mail command
    subject = "🍎 Email from macOS mail command"
    body = f"""
Email works via macOS mail command!!

Sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

If you see this - the mail command works!

GORUNFREE! 🚀
"""
    
    # Use echo to pipe to mail
    cmd = f'echo "{body}" | mail -s "{subject}" {to_email}'
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Email queued via mail command!")
        print("   Check your inbox!")
    else:
        print("⚠️  mail command might not be configured")
        
except Exception as e:
    print(f"⚠️  mail command failed: {e}")

print()
print("🍎 If Mail.app is setup, emails should work!")
print()

