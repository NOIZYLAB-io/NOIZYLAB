#!/usr/bin/env python3
"""
🔥 SEND TEST EMAIL NOW - SIMPLE & WORKS!!
Just enter your Gmail app password and SEE the email!!
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

print()
print("🔥" * 30)
print("     EMAIL TEST - SEND & SEE IT WORKING NOW!!")
print("🔥" * 30)
print()

# Gmail settings
FROM_EMAIL = "rsp@noizyfish.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

print("📧 SENDING FROM: rsp@noizyfish.com")
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🔑 GET YOUR GMAIL APP PASSWORD (2 MINUTES):")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()
print("1. Open: https://myaccount.google.com/security")
print("2. Turn on '2-Step Verification' (if not on)")
print("3. Search for 'App Passwords'")
print("4. Select 'Mail' and click 'Generate'")
print("5. Copy the 16-character password")
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

# Get credentials
app_password = input("Paste your Gmail App Password here: ").strip()

if not app_password:
    print("❌ No password entered!")
    exit(1)

to_email = input("\nSend test email to (press Enter for rsp@noizyfish.com): ").strip()
if not to_email:
    to_email = FROM_EMAIL

print()
print("🚀" * 30)
print("     SENDING EMAIL NOW...")
print("🚀" * 30)
print()

try:
    # Create beautiful email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "🔥 YOUR EMAIL WORKS!! Test from CB_01"
    msg['From'] = f"NoizyLab <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Date'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    
    # Text version
    text = f"""
🔥 EMAIL SYSTEM IS WORKING!!

ROB - If you're reading this email, YOUR EMAIL SYSTEM IS FIXED!! ✅

This was sent from your NoizyLab email system.

Sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
From: {FROM_EMAIL}
To: {to_email}

YOU CAN NOW:
✅ Send customer receipts automatically
✅ Send download links
✅ Send invoices
✅ Automate everything!!

NO MORE EMAIL PAIN!!

GORUNFREE! 🚀

CB_01 - Your LIFELUV ENGR
NoizyLab | noizylab.ca
"""
    
    # HTML version
    html = f"""
<!DOCTYPE html>
<html>
<body style="margin: 0; padding: 20px; background: #f0f0f0; font-family: Arial, sans-serif;">
    <div style="max-width: 600px; margin: 0 auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #ff0000 0%, #ff6600 100%); padding: 40px; text-align: center; color: white;">
            <h1 style="margin: 0; font-size: 3rem;">🔥</h1>
            <h2 style="margin: 10px 0 0 0; font-size: 2rem;">EMAIL WORKS!!</h2>
        </div>
        
        <!-- Success Banner -->
        <div style="background: #00ff88; color: #0f0f23; padding: 30px; text-align: center;">
            <h2 style="margin: 0; font-size: 2rem;">✅ YOUR EMAILS ARE FIXED!!</h2>
        </div>
        
        <!-- Content -->
        <div style="padding: 40px;">
            <p style="font-size: 1.3rem; line-height: 1.8; margin-bottom: 20px;">
                <strong>ROB</strong> - If you're reading this email, <strong>YOUR EMAIL SYSTEM IS WORKING PERFECTLY!!</strong>
            </p>
            
            <div style="background: #f4f4f4; padding: 20px; border-radius: 5px; margin: 20px 0;">
                <strong>Sent:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
                <strong>From:</strong> {FROM_EMAIL}<br>
                <strong>To:</strong> {to_email}<br>
                <strong>System:</strong> NoizyLab Email Platform
            </div>
            
            <h3 style="color: #00ff88; margin-top: 30px;">You Can Now:</h3>
            <ul style="line-height: 2; font-size: 1.1rem;">
                <li>✅ Send customer receipts automatically</li>
                <li>✅ Send download links</li>
                <li>✅ Send invoices</li>
                <li>✅ Automate ALL email tasks</li>
            </ul>
            
            <div style="background: #0f0f23; color: white; padding: 20px; border-radius: 5px; text-align: center; margin-top: 30px;">
                <p style="font-size: 1.5rem; font-weight: bold; margin: 0; color: #00ff88;">
                    NO MORE EMAIL PAIN!!
                </p>
            </div>
            
            <p style="font-size: 1.8rem; font-weight: bold; text-align: center; color: #00ff88; margin-top: 30px;">
                GORUNFREE! 🚀
            </p>
        </div>
        
        <!-- Footer -->
        <div style="background: #f4f4f4; padding: 20px; text-align: center; border-top: 2px solid #00ff88;">
            <p style="margin: 0; font-size: 12px; color: #666;">
                <strong>CB_01 - Your LIFELUV ENGR</strong><br>
                NoizyLab Portal | noizylab.ca
            </p>
        </div>
    </div>
</body>
</html>
"""
    
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))
    
    # Connect and send
    print("📤 Connecting to Gmail...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=15)
    server.starttls()
    
    print("🔐 Authenticating...")
    server.login(FROM_EMAIL, app_password)
    
    print(f"📧 Sending to {to_email}...")
    server.send_message(msg)
    server.quit()
    
    print()
    print("🎉" * 30)
    print("     EMAIL SENT SUCCESSFULLY!!")
    print("🎉" * 30)
    print()
    print("✅✅✅ CHECK YOUR INBOX NOW!! ✅✅✅")
    print()
    print(f"📬 Email sent to: {to_email}")
    print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("You should see it within SECONDS!!")
    print("(Check spam folder if not in inbox)")
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🎉 YOUR EMAILS ARE FIXED!! 🎉")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()
    print("GORUNFREE! 🚀")
    print()
    
except smtplib.SMTPAuthenticationError:
    print()
    print("❌" * 30)
    print("     AUTHENTICATION FAILED!!")
    print("❌" * 30)
    print()
    print("The app password is wrong or 2FA isn't enabled.")
    print()
    print("STEPS TO FIX:")
    print("1. Go to https://myaccount.google.com/security")
    print("2. Make sure 2-Step Verification is ON")
    print("3. Search 'App Passwords'")
    print("4. Create new password for 'Mail'")
    print("5. Run this script again")
    print()
    
except Exception as e:
    print()
    print("❌" * 30)
    print(f"     ERROR: {e}")
    print("❌" * 30)
    print()
    print("Check your internet connection and try again.")
    print()

