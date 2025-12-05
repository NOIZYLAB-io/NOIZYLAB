#!/usr/bin/env python3
"""
🐟 FISH MUSIC EMAIL SETUP WIZARD
Quick setup for all email providers
"""

import json
import os

PROVIDERS = {
    "gmail": {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "use_tls": True,
        "notes": "Use App Password (not regular password). Enable 2FA first, then create app password."
    },
    "outlook": {
        "smtp_server": "smtp-mail.outlook.com",
        "smtp_port": 587,
        "use_tls": True,
        "notes": "Use your Microsoft account password"
    },
    "microsoft365": {
        "smtp_server": "smtp.office365.com",
        "smtp_port": 587,
        "use_tls": True,
        "notes": "For business Microsoft 365 accounts"
    },
    "fastmail": {
        "smtp_server": "smtp.fastmail.com",
        "smtp_port": 587,
        "use_tls": True,
        "notes": "Use App Password from Settings > Password & Security"
    },
    "sendgrid": {
        "smtp_server": "smtp.sendgrid.net",
        "smtp_port": 587,
        "use_tls": True,
        "notes": "Username is 'apikey', password is your API key"
    },
    "mailgun": {
        "smtp_server": "smtp.mailgun.org",
        "smtp_port": 587,
        "use_tls": True,
        "notes": "Use your Mailgun SMTP credentials"
    }
}

def setup_wizard():
    """Interactive setup wizard"""
    print("🐟 FISH MUSIC EMAIL SETUP WIZARD")
    print("=" * 50)
    print()
    
    # Choose provider
    print("Available providers:")
    for i, (key, provider) in enumerate(PROVIDERS.items(), 1):
        print(f"  {i}. {key.title()}")
    print()
    
    choice = input("Choose provider (1-6) or type custom: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(PROVIDERS):
        provider_key = list(PROVIDERS.keys())[int(choice) - 1]
        provider = PROVIDERS[provider_key]
    else:
        # Custom provider
        provider = {
            "smtp_server": input("SMTP server: "),
            "smtp_port": int(input("SMTP port (usually 587): ") or "587"),
            "use_tls": input("Use TLS? (y/n): ").lower() == 'y',
            "notes": ""
        }
        provider_key = "custom"
    
    print(f"\n📋 Provider: {provider_key.title()}")
    if provider.get('notes'):
        print(f"ℹ️  {provider['notes']}")
    print()
    
    # Get credentials
    from_email = input("From email (e.g., rsp@fishmusicinc.com): ").strip()
    from_name = input("From name (e.g., Fish Music Inc): ").strip() or "Fish Music Inc"
    username = input(f"SMTP username (usually {from_email}): ").strip() or from_email
    password = input("SMTP password/app password: ").strip()
    
    # Create config
    config = {
        "smtp_server": provider["smtp_server"],
        "smtp_port": provider["smtp_port"],
        "use_tls": provider["use_tls"],
        "from_email": from_email,
        "from_name": from_name,
        "username": username,
        "password": password,
        "provider": provider_key
    }
    
    # Save config
    with open('email_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("\n✅ Configuration saved to email_config.json")
    print()
    
    # Test?
    test = input("Send test email? (y/n): ").strip().lower()
    if test == 'y':
        test_email = input("Test email address: ").strip()
        print("\n🚀 Sending test email...")
        os.system(f"python3 fish_mail.py test {test_email}")
    
    print("\n🎉 Setup complete! You can now use:")
    print("  python3 fish_mail.py test <email>")
    print("  python3 fish_mail.py welcome <email> <name>")
    print("  python3 fish_mail.py receipt <email> <name> <track> <price> <order_id>")
    print("  python3 fish_mail.py download <email> <name> <track> <url>")
    print()
    print("GORUNFREE! 🚀")

if __name__ == "__main__":
    setup_wizard()
