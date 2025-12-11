# 📧 Email Account Setup Guide

NoizyLab supports multiple email providers. Set up your accounts easily!

---

## 🚀 Quick Setup

```bash
python3 ~/NOIZYLAB/email-intelligence/setup-email-accounts.py
```

Or add to main menu (coming soon).

---

## 📋 Supported Providers

### 1. **iCloud** 🍎
- **SMTP**: smtp.mail.me.com:587
- **IMAP**: imap.mail.me.com:993
- **Use**: Your @icloud.com, @me.com, or @mac.com email
- **Note**: Requires App-Specific Password if 2FA enabled

### 2. **Microsoft Exchange** 📧
- **SMTP**: smtp.office365.com:587
- **IMAP**: outlook.office365.com:993
- **Use**: Microsoft 365, Outlook.com, Hotmail
- **Note**: Works with Office 365 and personal Outlook accounts

### 3. **Google** 🔵
- **SMTP**: smtp.gmail.com:587
- **IMAP**: imap.gmail.com:993
- **Use**: Gmail, Google Workspace
- **Note**: **Requires App Password** (not regular password)
  - Get from: https://myaccount.google.com/apppasswords
  - Enable 2-Step Verification first

### 4. **Yahoo** 📮
- **SMTP**: smtp.mail.yahoo.com:587
- **IMAP**: imap.mail.yahoo.com:993
- **Use**: Yahoo Mail accounts
- **Note**: May require App Password

### 5. **AOL** 📬
- **SMTP**: smtp.aol.com:587
- **IMAP**: imap.aol.com:993
- **Use**: AOL Mail accounts

### 6. **Other Mail Account** ⚙️
- **Custom SMTP/IMAP**
- **Use**: Any email provider with custom settings
- **Note**: You'll need to provide server details

---

## 🔧 Setup Process

### Step 1: Launch Setup Wizard
```bash
python3 ~/NOIZYLAB/email-intelligence/setup-email-accounts.py
```

### Step 2: Select Provider
Choose from the list:
- `1` - iCloud
- `2` - Microsoft Exchange
- `3` - Google
- `4` - Yahoo
- `5` - AOL
- `6` - Other Mail Account

### Step 3: Enter Details
- **Email Address**: Your full email
- **Password**: Your password (or App Password for Gmail)
- **Display Name**: How your name appears

### Step 4: Test Connection
- Optionally test SMTP connection
- Verify credentials work

### Step 5: Save Identity
- Save as email identity
- Use in NoizyLab CORE

---

## 🔐 Provider-Specific Notes

### Gmail Setup
1. Enable 2-Step Verification:
   - https://myaccount.google.com/security
2. Generate App Password:
   - https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the 16-character password
3. Use App Password (not regular password) in setup

### iCloud Setup
1. Enable 2FA in Apple ID settings
2. Generate App-Specific Password:
   - https://appleid.apple.com
   - Sign in > Security > App-Specific Passwords
3. Use App-Specific Password in setup

### Microsoft Exchange
- Works with:
  - Office 365 business accounts
  - Outlook.com personal accounts
  - Hotmail accounts
- Use your regular password

### Yahoo Mail
- May require App Password:
  - Account Security > Generate app password
- Use App Password if 2FA enabled

---

## 💡 Tips

### Multiple Accounts
- Run setup wizard multiple times
- Each account becomes a separate identity
- Switch between identities when sending

### Security
- Use App Passwords when available
- Never share your passwords
- Store credentials securely

### Testing
- Always test connection before saving
- Verify you can send/receive
- Check spam folder if emails don't arrive

---

## 🎯 Using Configured Accounts

After setup, accounts are available in:
- **NoizyLab CORE** - Select identity when sending
- **Smart Composer** - Choose from configured accounts
- **Email Config** - View/edit in `config/email_config.json`

---

## 🔄 Managing Accounts

### View Configured Accounts
```bash
cat ~/NOIZYLAB/email-intelligence/config/email_config.json
```

### Edit Account
1. Edit `config/email_config.json`
2. Or run setup wizard again
3. Use same identity key to update

### Remove Account
1. Edit `config/email_config.json`
2. Remove identity from `identities` section
3. Save file

---

## ❓ Troubleshooting

### "Connection failed"
- Check email and password
- Verify server settings
- Try App Password (Gmail/iCloud)
- Check firewall/network

### "Authentication failed"
- Use App Password for Gmail
- Enable "Less secure apps" (not recommended)
- Check 2FA settings

### "Server not found"
- Verify server addresses
- Check internet connection
- Try different port (465 for SSL)

---

## 📊 Quick Reference

| Provider | SMTP Server | Port | TLS |
|----------|------------|------|-----|
| iCloud | smtp.mail.me.com | 587 | Yes |
| Exchange | smtp.office365.com | 587 | Yes |
| Google | smtp.gmail.com | 587 | Yes |
| Yahoo | smtp.mail.yahoo.com | 587 | Yes |
| AOL | smtp.aol.com | 587 | Yes |

---

**Ready to set up your email accounts?** Run the setup wizard! 🚀

