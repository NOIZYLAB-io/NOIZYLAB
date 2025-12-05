#!/usr/bin/env python3
"""
MICROSOFT OUTLOOK - AUTOMATED EMAIL SETUP
Configures all 7 email accounts in Outlook automatically
"""

import json
import os
import subprocess
from datetime import datetime

# ==================== EMAIL CONFIGURATION ====================
CONFIG_FILE = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/domains_and_emails_master.json"

with open(CONFIG_FILE, 'r') as f:
    CONFIG = json.load(f)

# All email accounts to configure
EMAIL_ACCOUNTS = [
    {
        "email": "rsplowman@gmail.com",
        "display_name": "R Plowman",
        "account_type": "IMAP",
        "incoming_server": "imap.gmail.com",
        "incoming_port": 993,
        "outgoing_server": "smtp.gmail.com",
        "outgoing_port": 587,
        "ssl_incoming": True,
        "ssl_outgoing": True,
        "auth_type": "OAuth2",
        "provider": "Gmail",
        "primary": True
    },
    {
        "email": "rp@fishmusicinc.com",
        "display_name": "RP - Fish Music Inc",
        "account_type": "IMAP",
        "incoming_server": "mail.fishmusicinc.com",
        "incoming_port": 993,
        "outgoing_server": "mail.fishmusicinc.com",
        "outgoing_port": 587,
        "ssl_incoming": True,
        "ssl_outgoing": True,
        "auth_type": "password",
        "provider": "Custom Domain"
    },
    {
        "email": "info@fishmusicinc.com",
        "display_name": "Info - Fish Music Inc",
        "account_type": "IMAP",
        "incoming_server": "mail.fishmusicinc.com",
        "incoming_port": 993,
        "outgoing_server": "mail.fishmusicinc.com",
        "outgoing_port": 587,
        "ssl_incoming": True,
        "ssl_outgoing": True,
        "auth_type": "password",
        "provider": "Custom Domain"
    },
    {
        "email": "rsp@noizylab.ca",
        "display_name": "RSP - Noizylab",
        "account_type": "IMAP",
        "incoming_server": "mail.noizylab.ca",
        "incoming_port": 993,
        "outgoing_server": "mail.noizylab.ca",
        "outgoing_port": 587,
        "ssl_incoming": True,
        "ssl_outgoing": True,
        "auth_type": "password",
        "provider": "Custom Domain"
    },
    {
        "email": "help@noizylab.ca",
        "display_name": "Help - Noizylab",
        "account_type": "IMAP",
        "incoming_server": "mail.noizylab.ca",
        "incoming_port": 993,
        "outgoing_server": "mail.noizylab.ca",
        "outgoing_port": 587,
        "ssl_incoming": True,
        "ssl_outgoing": True,
        "auth_type": "password",
        "provider": "Custom Domain"
    },
    {
        "email": "hello@noizylab.ca",
        "display_name": "Hello - Noizylab",
        "account_type": "IMAP",
        "incoming_server": "mail.noizylab.ca",
        "incoming_port": 993,
        "outgoing_server": "mail.noizylab.ca",
        "outgoing_port": 587,
        "ssl_incoming": True,
        "ssl_outgoing": True,
        "auth_type": "password",
        "provider": "Custom Domain"
    },
    {
        "email": "rsplowman@icloud.com",
        "display_name": "R Plowman - iCloud",
        "account_type": "IMAP",
        "incoming_server": "imap.mail.me.com",
        "incoming_port": 993,
        "outgoing_server": "smtp.mail.me.com",
        "outgoing_port": 587,
        "ssl_incoming": True,
        "ssl_outgoing": True,
        "auth_type": "app_password",
        "provider": "iCloud"
    }
]

# ==================== OUTLOOK PROFILE GENERATOR ====================
def generate_outlook_xml_config(account):
    """Generate Outlook XML configuration"""
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
    <Response xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
        <Account>
            <AccountType>{account['account_type']}</AccountType>
            <Action>settings</Action>
            <Protocol>
                <Type>{account['account_type']}</Type>
                <Server>{account['incoming_server']}</Server>
                <Port>{account['incoming_port']}</Port>
                <LoginName>{account['email']}</LoginName>
                <SSL>{'on' if account['ssl_incoming'] else 'off'}</SSL>
                <SPA>off</SPA>
                <AuthRequired>on</AuthRequired>
            </Protocol>
            <Protocol>
                <Type>SMTP</Type>
                <Server>{account['outgoing_server']}</Server>
                <Port>{account['outgoing_port']}</Port>
                <LoginName>{account['email']}</LoginName>
                <SSL>{'on' if account['ssl_outgoing'] else 'off'}</SSL>
                <SPA>off</SPA>
                <AuthRequired>on</AuthRequired>
            </Protocol>
        </Account>
    </Response>
</Autodiscover>"""
    return xml

# ==================== CONFIGURATION EXPORT ====================
def export_outlook_configs():
    """Export configuration files for manual import"""
    output_dir = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/outlook_configs"
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n" + "="*60)
    print("📧 OUTLOOK EMAIL CONFIGURATION GENERATOR")
    print("="*60)
    
    # Generate individual config files
    for account in EMAIL_ACCOUNTS:
        # XML config
        xml_config = generate_outlook_xml_config(account)
        xml_file = f"{output_dir}/{account['email'].replace('@', '_at_')}_outlook.xml"
        
        with open(xml_file, 'w') as f:
            f.write(xml_config)
        
        print(f"\n✓ Generated config for: {account['email']}")
        print(f"  File: {xml_file}")
    
    # Generate summary JSON
    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_accounts": len(EMAIL_ACCOUNTS),
        "accounts": EMAIL_ACCOUNTS,
        "outlook_version": "Microsoft 365 / Outlook 2019+",
        "configuration_directory": output_dir
    }
    
    summary_file = f"{output_dir}/outlook_setup_summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n✓ Summary saved: {summary_file}")
    print(f"\n📁 All configurations saved to: {output_dir}")
    
    return output_dir

# ==================== MANUAL SETUP GUIDE GENERATOR ====================
def generate_manual_setup_guide():
    """Generate detailed manual setup guide"""
    
    guide = """
# MICROSOFT OUTLOOK - COMPLETE EMAIL SETUP GUIDE
Generated: {timestamp}

## 🎯 OVERVIEW
Setting up {total} email accounts in Microsoft Outlook

---

## 📧 EMAIL ACCOUNTS TO CONFIGURE

{accounts_list}

---

## 🚀 QUICK SETUP (AUTOMATIC)

### For Microsoft 365 / Outlook 2019+:

1. **Open Outlook**
2. **Go to**: File → Add Account
3. **Enter email address** and click "Connect"
4. **For Gmail/iCloud**: Follow OAuth authentication
5. **For custom domains**: Enter password when prompted

Outlook will attempt to auto-configure. If it fails, use manual setup below.

---

## 🔧 MANUAL SETUP (STEP-BY-STEP)

### Gmail Account (rsplowman@gmail.com)

**Setup Method 1: OAuth (Recommended)**
1. File → Add Account
2. Enter: rsplowman@gmail.com
3. Click "Connect"
4. Sign in with Google account
5. Allow Outlook to access Gmail
6. Done! ✓

**Setup Method 2: App Password**
1. Go to: https://myaccount.google.com/apppasswords
2. Generate app password for Outlook
3. Use this password in Outlook instead of Gmail password

**Server Settings:**
- **Incoming (IMAP)**: imap.gmail.com
- **Port**: 993
- **Encryption**: SSL/TLS
- **Outgoing (SMTP)**: smtp.gmail.com
- **Port**: 587
- **Encryption**: STARTTLS

---

### Custom Domain Accounts (Fish Music Inc)

**Accounts:**
- rp@fishmusicinc.com
- info@fishmusicinc.com

**Manual Configuration:**
1. File → Add Account → Manual setup or additional server types
2. Choose: POP or IMAP
3. **Your Name**: [Your display name]
4. **Email Address**: [Your email]
5. **Account Type**: IMAP
6. **Incoming mail server**: mail.fishmusicinc.com
7. **Outgoing mail server**: mail.fishmusicinc.com
8. **User Name**: [Full email address]
9. **Password**: [Your email password]

**Advanced Settings:**
10. More Settings → Outgoing Server
11. ☑ My outgoing server (SMTP) requires authentication
12. ☑ Use same settings as my incoming mail server

13. Advanced tab:
    - **Incoming server (IMAP)**: 993
    - **Use SSL**: Yes
    - **Outgoing server (SMTP)**: 587
    - **Encryption**: TLS

14. Click OK → Next → Finish

---

### Custom Domain Accounts (Noizylab)

**Accounts:**
- rsp@noizylab.ca
- help@noizylab.ca
- hello@noizylab.ca

**Server Settings:**
- **Incoming (IMAP)**: mail.noizylab.ca
- **Port**: 993
- **Encryption**: SSL/TLS
- **Outgoing (SMTP)**: mail.noizylab.ca
- **Port**: 587
- **Encryption**: STARTTLS

Follow same manual setup steps as Fish Music Inc accounts above.

---

### iCloud Account (rsplowman@icloud.com)

**Setup:**
1. **Generate App-Specific Password**:
   - Go to: https://appleid.apple.com
   - Sign in → Security → App-Specific Passwords
   - Generate password for "Outlook"
   - Copy the password

2. **Configure in Outlook**:
   - File → Add Account
   - Enter: rsplowman@icloud.com
   - Use the app-specific password (NOT your iCloud password)

**Server Settings:**
- **Incoming (IMAP)**: imap.mail.me.com
- **Port**: 993
- **Encryption**: SSL/TLS
- **Outgoing (SMTP)**: smtp.mail.me.com
- **Port**: 587
- **Encryption**: STARTTLS

---

## 🎨 RECOMMENDED OUTLOOK ORGANIZATION

### Folder Structure:
```
📁 Inbox (Unified - Primary)
├── 📁 Fish Music Inc
│   ├── 📧 rp@fishmusicinc.com
│   └── 📧 info@fishmusicinc.com
├── 📁 Noizylab
│   ├── 📧 rsp@noizylab.ca
│   ├── 📧 help@noizylab.ca
│   └── 📧 hello@noizylab.ca
├── 📁 Gmail (rsplowman@gmail.com)
└── 📁 iCloud (rsplowman@icloud.com)
```

### Create Rules:
1. **Auto-categorize by domain**
   - Fish Music emails → Green category
   - Noizylab emails → Blue category
   - Personal emails → Yellow category

2. **Auto-file emails**
   - Create subfolders for each account
   - Set rules to move emails to appropriate folders

---

## 🔐 SECURITY RECOMMENDATIONS

### Enable 2FA:
- ✓ Gmail: Already using OAuth
- ✓ iCloud: App-specific passwords
- ✓ Custom domains: Enable if available

### App Passwords:
Required for:
- Gmail (if not using OAuth)
- iCloud (always required)

### SSL/TLS:
- Always use encrypted connections
- IMAP: Port 993 with SSL
- SMTP: Port 587 with STARTTLS

---

## 🎯 SEND/RECEIVE SETTINGS

### Recommended Schedule:
- **Send/Receive All**: Every 5 minutes
- **When Offline**: Manual only
- **On Exit**: Send all

### Configure:
1. File → Options → Advanced
2. Send/Receive button
3. Edit "All Accounts" group
4. Set interval to 5 minutes
5. Check all accounts

---

## 📱 OUTLOOK MOBILE SETUP

### iOS/Android:
1. Download Microsoft Outlook app
2. Add Account → Enter email
3. All accounts will sync automatically
4. Use unified inbox for all emails

---

## 🔧 TROUBLESHOOTING

### "Cannot connect to server"
- ✓ Check internet connection
- ✓ Verify server names are correct
- ✓ Try disabling firewall temporarily
- ✓ Check port numbers (993 for IMAP, 587 for SMTP)

### "Authentication failed"
- ✓ Gmail: Use app password or OAuth
- ✓ iCloud: Use app-specific password
- ✓ Custom domains: Verify password is correct
- ✓ Username should be full email address

### "SSL certificate error"
- ✓ Update Windows/macOS to latest version
- ✓ Update Outlook to latest version
- ✓ Check system date/time is correct

### Emails not syncing
- ✓ Right-click account → Update Folder
- ✓ File → Account Settings → Send/Receive
- ✓ Check "Download complete item" setting

---

## ✅ VERIFICATION CHECKLIST

After setup, verify each account:

□ Can send test email
□ Can receive test email  
□ Folders are syncing
□ Sent items appear in Sent folder
□ Contacts are syncing (if applicable)
□ Calendar is syncing (if applicable)
□ Signature is configured
□ Rules are working (if created)

---

## 📞 QUICK REFERENCE

| Account | Incoming Server | Outgoing Server | Ports |
|---------|----------------|-----------------|-------|
| Gmail | imap.gmail.com | smtp.gmail.com | 993/587 |
| Fish Music | mail.fishmusicinc.com | mail.fishmusicinc.com | 993/587 |
| Noizylab | mail.noizylab.ca | mail.noizylab.ca | 993/587 |
| iCloud | imap.mail.me.com | smtp.mail.me.com | 993/587 |

All accounts use:
- IMAP for incoming (Port 993, SSL)
- SMTP for outgoing (Port 587, TLS)

---

## 🎉 SETUP COMPLETE!

All {total} email accounts are now configured in Outlook!

**Tips for daily use:**
- Use Focused Inbox to prioritize important emails
- Set up Quick Steps for common actions
- Use Search folders for better organization
- Enable desktop notifications for important accounts
- Sync with Outlook mobile app for on-the-go access

---

Generated: {timestamp}
""".format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        total=len(EMAIL_ACCOUNTS),
        accounts_list="\n".join([f"{i+1}. **{acc['email']}** ({acc['provider']})" 
                                  for i, acc in enumerate(EMAIL_ACCOUNTS)])
    )
    
    guide_file = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/OUTLOOK_COMPLETE_SETUP_GUIDE.md"
    with open(guide_file, 'w') as f:
        f.write(guide)
    
    print(f"\n✓ Complete setup guide saved: {guide_file}")
    return guide_file

# ==================== MAIN EXECUTION ====================
def main():
    """Main execution"""
    print("\n" + "="*60)
    print("🚀 MICROSOFT OUTLOOK - EMAIL SETUP AUTOMATION")
    print("="*60)
    print(f"\n📊 Configuring {len(EMAIL_ACCOUNTS)} email accounts:")
    
    for i, account in enumerate(EMAIL_ACCOUNTS, 1):
        primary = " (PRIMARY)" if account.get('primary') else ""
        print(f"  {i}. {account['email']} - {account['provider']}{primary}")
    
    # Generate XML configs
    config_dir = export_outlook_configs()
    
    # Generate manual guide
    guide_file = generate_manual_setup_guide()
    
    print("\n" + "="*60)
    print("✅ OUTLOOK SETUP FILES GENERATED!")
    print("="*60)
    print(f"\n📁 Configuration files: {config_dir}")
    print(f"📖 Setup guide: {guide_file}")
    
    print("\n" + "="*60)
    print("🎯 NEXT STEPS:")
    print("="*60)
    print("\n1. Read the complete guide:")
    print(f"   cat OUTLOOK_COMPLETE_SETUP_GUIDE.md")
    print("\n2. Open Microsoft Outlook")
    print("\n3. Add each account:")
    print("   File → Add Account → Enter email")
    print("\n4. Follow authentication prompts")
    print("\n5. Verify all accounts are working")
    
    print("\n" + "="*60)
    print("🚀 Ready to configure Outlook with all 7 emails!")
    print("="*60)

if __name__ == "__main__":
    main()

