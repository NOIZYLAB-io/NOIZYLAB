#!/usr/bin/env python3
"""
🔥 SENDGRID - THIS ACTUALLY WORKS!! NO GOOGLE BULLSHIT!!
Sign up (2 min), get API key, SEND EMAIL. DONE.
"""

import requests
from datetime import datetime
import json
import os

print("\n" + "🔥" * 40)
print("   SENDGRID - THIS ACTUALLY FUCKING WORKS!!")
print("🔥" * 40 + "\n")

print("WHY SENDGRID:")
print("  ✅ NO 2FA bullshit")
print("  ✅ NO app passwords")
print("  ✅ Just ONE API key")
print("  ✅ 100 emails/day FREE")
print("  ✅ Actually designed for sending emails!")
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

# Check if API key exists
api_key = None
if os.path.exists('sendgrid_key.txt'):
    with open('sendgrid_key.txt', 'r') as f:
        api_key = f.read().strip()
    print("✅ Found saved SendGrid key")
else:
    print("GET YOUR SENDGRID API KEY (2 MINUTES):")
    print()
    print("1. Go to: https://signup.sendgrid.com")
    print("2. Sign up (use rsp@noizyfish.com)")
    print("3. Verify your email")
    print("4. Go to: Settings → API Keys")
    print("5. Click 'Create API Key'")
    print("6. Name it 'NoizyLab', Full Access")
    print("7. COPY the key (starts with 'SG.')")
    print()
    
    api_key = input("Paste SendGrid API key here: ").strip()
    
    if api_key:
        with open('sendgrid_key.txt', 'w') as f:
            f.write(api_key)
        print("✅ API key saved for future use")

if not api_key:
    print("\n❌ No API key provided!")
    print("\nGet it at: https://app.sendgrid.com/settings/api_keys")
    exit(1)

# Get recipient
to_email = input("\nSend test email to (default: rsp@noizyfish.com): ").strip()
if not to_email:
    to_email = "rsp@noizyfish.com"

print()
print("🚀" * 40)
print("   SENDING EMAIL VIA SENDGRID...")
print("🚀" * 40)
print()

try:
    url = "https://api.sendgrid.com/v3/mail/send"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "personalizations": [{
            "to": [{"email": to_email}],
            "subject": "🔥 SENDGRID WORKS!! No More Email Pain!!"
        }],
        "from": {
            "email": "rsp@noizyfish.com",
            "name": "NoizyLab"
        },
        "content": [{
            "type": "text/html",
            "value": f"""
<!DOCTYPE html>
<html>
<body style="font-family: Arial; padding: 40px; background: #f0f0f0;">
    <div style="max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px;">
        <div style="background: linear-gradient(135deg, #00ff88 0%, #00cc6a 100%); padding: 30px; text-align: center; border-radius: 10px; margin-bottom: 30px;">
            <h1 style="color: white; margin: 0; font-size: 2.5rem;">🔥</h1>
            <h2 style="color: white; margin: 10px 0 0 0;">SENDGRID WORKS!!</h2>
        </div>
        
        <div style="background: #00ff88; color: #0f0f23; padding: 20px; text-align: center; border-radius: 5px; margin: 20px 0;">
            <h2 style="margin: 0;">✅ YOUR EMAILS ARE FINALLY FIXED!!</h2>
        </div>
        
        <p style="font-size: 1.2rem; line-height: 1.8;">
            <strong>ROB</strong> - If you're reading this, <strong>SENDGRID WORKS!!</strong>
        </p>
        
        <p style="font-size: 1.1rem;">
            NO MORE:<br>
            ❌ Google 2FA bullshit<br>
            ❌ App password confusion<br>
            ❌ Authentication failures<br>
            ❌ Email pain!!
        </p>
        
        <p style="font-size: 1.1rem; margin-top: 20px;">
            YOU NOW HAVE:<br>
            ✅ Working email system<br>
            ✅ 100 emails/day FREE<br>
            ✅ Simple API key<br>
            ✅ Professional delivery<br>
            ✅ NO MORE PAIN!!
        </p>
        
        <div style="background: #f4f4f4; padding: 20px; border-radius: 5px; margin: 20px 0;">
            <strong>Sent:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            <strong>From:</strong> rsp@noizyfish.com<br>
            <strong>Method:</strong> SendGrid API<br>
            <strong>Status:</strong> WORKING!! ✅
        </div>
        
        <p style="font-size: 1.5rem; font-weight: bold; text-align: center; color: #00ff88; margin-top: 30px;">
            GORUNFREE!! 🚀
        </p>
        
        <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
        
        <p style="font-size: 12px; color: #666; text-align: center;">
            CB_01 - Your LIFELUV ENGR<br>
            NoizyLab | noizylab.ca
        </p>
    </div>
</body>
</html>
"""
        }]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 202:
        print("🎉" * 40)
        print("   ✅✅✅ EMAIL SENT VIA SENDGRID!! ✅✅✅")
        print("🎉" * 40)
        print()
        print(f"📬 Email sent to: {to_email}")
        print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
        print()
        print("CHECK YOUR INBOX NOW!!")
        print("(Should arrive within seconds!)")
        print()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("🎉 NO MORE EMAIL PAIN!! SENDGRID WORKS!! 🎉")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        print("GORUNFREE!! 🚀")
        print()
        
        # Save working config
        config = {
            "provider": "sendgrid",
            "api_key": api_key,
            "from_email": "rsp@noizyfish.com",
            "working": True,
            "tested": datetime.now().isoformat()
        }
        with open('working_config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print("💾 Config saved - emails ready to use!!")
        
    else:
        print(f"\n❌ SendGrid failed: {response.status_code}")
        print(f"Response: {response.text}")
        print()
        print("Check your API key at: https://app.sendgrid.com/settings/api_keys")
        
except Exception as e:
    print(f"\n❌ Error: {e}")
    print()
    print("Make sure you have requests installed:")
    print("  pip3 install requests")
    print()

