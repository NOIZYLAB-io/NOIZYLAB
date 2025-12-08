#!/usr/bin/env python3
"""
🍎 iCLOUD EMAIL TEST - APPLE MAIL SMTP
Using rsplowman@icloud.com - Should be EASIER than Gmail!
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

print("\n" + "🍎" * 40)
print("   iCLOUD EMAIL TEST - USING APPLE!!")
print("🍎" * 40 + "\n")

FROM_EMAIL = "rsplowman@icloud.com"
SMTP_SERVER = "smtp.mail.me.com"
SMTP_PORT = 587

print("📧 SENDING FROM: rsplowman@icloud.com")
print("🌐 SMTP Server: smtp.mail.me.com")
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🔑 iCLOUD APP-SPECIFIC PASSWORD:")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()
print("1. Go to: https://appleid.apple.com")
print("2. Sign In → Security section")
print("3. Under 'App-Specific Passwords' click 'Generate'")
print("4. Label it: 'NoizyLab'")
print("5. COPY the password (format: xxxx-xxxx-xxxx-xxxx)")
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

# Get app password
app_password = input("Paste iCloud App-Specific Password: ").strip().replace("-", "")

if not app_password:
    print("\n❌ No password entered!")
    exit(1)

# Get recipient
to_email = input("\nSend test to (default: rsplowman@icloud.com): ").strip()
if not to_email:
    to_email = FROM_EMAIL

print()
print("🚀" * 40)
print("   SENDING EMAIL VIA iCLOUD...")
print("🚀" * 40)
print()

try:
    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "🍎 iCLOUD EMAIL WORKS!! Test from NoizyLab"
    msg['From'] = f"Rob @ NoizyLab <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Date'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    
    # Text version
    text = f"""
🍎 iCLOUD EMAIL IS WORKING!!

ROB - If you're reading this, YOUR EMAIL IS FIXED!! ✅

Method: Apple iCloud SMTP
From: {FROM_EMAIL}
To: {to_email}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

NO MORE EMAIL PAIN!!

YOU CAN NOW:
✅ Send customer emails from rsplowman@icloud.com
✅ Send invoices
✅ Send receipts
✅ Automate everything!!

GORUNFREE!! 🚀

CB_01 - Your LIFELUV ENGR
NoizyLab | noizylab.ca
"""
    
    # HTML version
    html = f"""
<!DOCTYPE html>
<html>
<body style="margin: 0; padding: 20px; background: #f0f0f0; font-family: Arial, sans-serif;">
    <div style="max-width: 600px; margin: 0 auto; background: white; border-radius: 10px; overflow: hidden;">
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #007AFF 0%, #5856D6 100%); padding: 40px; text-align: center; color: white;">
            <h1 style="margin: 0; font-size: 3rem;">🍎</h1>
            <h2 style="margin: 10px 0 0 0;">iCLOUD EMAIL WORKS!!</h2>
        </div>
        
        <!-- Success -->
        <div style="background: #00ff88; color: #0f0f23; padding: 25px; text-align: center;">
            <h2 style="margin: 0; font-size: 1.8rem;">✅ YOUR EMAIL IS FIXED!!</h2>
        </div>
        
        <!-- Content -->
        <div style="padding: 40px;">
            <p style="font-size: 1.2rem; line-height: 1.8; margin-bottom: 20px;">
                <strong>ROB</strong> - If you're reading this email, <strong>YOUR EMAIL SYSTEM IS WORKING!!</strong>
            </p>
            
            <div style="background: #f4f4f4; padding: 20px; border-radius: 5px; margin: 20px 0;">
                <strong>Method:</strong> Apple iCloud SMTP<br>
                <strong>From:</strong> {FROM_EMAIL}<br>
                <strong>To:</strong> {to_email}<br>
                <strong>Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </div>
            
            <h3 style="color: #007AFF;">NO MORE EMAIL PAIN!!</h3>
            
            <h3 style="color: #00ff88; margin-top: 25px;">You Can Now:</h3>
            <ul style="line-height: 2.2; font-size: 1.1rem;">
                <li>✅ Send customer emails from rsplowman@icloud.com</li>
                <li>✅ Send invoices professionally</li>
                <li>✅ Send receipts automatically</li>
                <li>✅ Automate ALL email tasks</li>
            </ul>
            
            <div style="background: #007AFF; color: white; padding: 25px; border-radius: 8px; text-align: center; margin-top: 30px;">
                <p style="font-size: 1.8rem; font-weight: bold; margin: 0;">
                    EMAILS FIXED!! ✅
                </p>
            </div>
            
            <p style="font-size: 1.8rem; font-weight: bold; text-align: center; color: #00ff88; margin-top: 30px;">
                GORUNFREE!! 🚀
            </p>
        </div>
        
        <!-- Footer -->
        <div style="background: #f4f4f4; padding: 20px; text-align: center;">
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
    
    # Connect to iCloud SMTP
    print("📤 Connecting to Apple iCloud SMTP...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=15)
    server.starttls()
    
    print("🔐 Authenticating with Apple...")
    server.login(FROM_EMAIL, app_password)
    
    print(f"📧 Sending to {to_email}...")
    server.send_message(msg)
    server.quit()
    
    print()
    print("🎉" * 40)
    print("   ✅✅✅ EMAIL SENT VIA iCLOUD!! ✅✅✅")
    print("🎉" * 40)
    print()
    print(f"📬 Email sent to: {to_email}")
    print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("CHECK YOUR INBOX NOW!!")
    print("(Should arrive within seconds!)")
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🍎 APPLE MAIL WORKS!! NO MORE PAIN!! 🍎")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()
    print("GORUNFREE!! 🚀")
    print()
    
    # Save working config
    import json
    config = {
        "provider": "icloud",
        "smtp_server": SMTP_SERVER,
        "smtp_port": SMTP_PORT,
        "from_email": FROM_EMAIL,
        "username": FROM_EMAIL,
        "password": app_password,
        "working": True,
        "tested": datetime.now().isoformat()
    }
    
    with open('icloud_working_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("💾 iCloud config saved!!")
    print()
    
except smtplib.SMTPAuthenticationError:
    print()
    print("❌" * 40)
    print("   AUTHENTICATION FAILED!!")
    print("❌" * 40)
    print()
    print("The app-specific password is wrong.")
    print()
    print("GET IT HERE:")
    print("  https://appleid.apple.com")
    print("  → Sign In")
    print("  → Security section")
    print("  → App-Specific Passwords → Generate")
    print()
    
except Exception as e:
    print()
    print("❌" * 40)
    print(f"   ERROR: {e}")
    print("❌" * 40)
    print()

