#!/bin/bash
# MICROSOFT OUTLOOK - ALL EMAIL ACCOUNTS SETUP

echo "=========================================="
echo "📧 OUTLOOK EMAIL CONFIGURATION GENERATOR"
echo "=========================================="
echo ""
echo "Setting up 7 email accounts for Outlook..."
echo ""

# Create output directory
OUTPUT_DIR="/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/outlook_configs"
mkdir -p "$OUTPUT_DIR"

# ==================== ACCOUNT 1: Gmail ====================
cat > "$OUTPUT_DIR/1_rsplowman_gmail_config.txt" << 'EOF'
======================================
ACCOUNT 1: Gmail (PRIMARY)
======================================

Email: rsplowman@gmail.com
Display Name: R Plowman
Provider: Gmail

SETUP METHOD: OAuth (Recommended)
1. File → Add Account
2. Enter: rsplowman@gmail.com
3. Click "Connect"
4. Sign in with Google
5. Allow Outlook access

MANUAL SETTINGS (if OAuth fails):
- Account Type: IMAP
- Incoming Server: imap.gmail.com
- Incoming Port: 993
- Encryption: SSL/TLS
- Outgoing Server: smtp.gmail.com
- Outgoing Port: 587
- Encryption: STARTTLS
- Authentication: Required

APP PASSWORD OPTION:
1. Go to: https://myaccount.google.com/apppasswords
2. Generate app password for "Outlook"
3. Use this password in Outlook

STATUS: ✓ Ready to configure
EOF

# ==================== ACCOUNT 2: Fish Music RP ====================
cat > "$OUTPUT_DIR/2_rp_fishmusicinc_config.txt" << 'EOF'
======================================
ACCOUNT 2: Fish Music Inc - RP
======================================

Email: rp@fishmusicinc.com
Display Name: RP - Fish Music Inc
Provider: Custom Domain

MANUAL SETUP:
1. File → Add Account → Manual setup
2. Choose: POP or IMAP
3. Select: IMAP

SERVER SETTINGS:
- Account Type: IMAP
- Incoming Server: mail.fishmusicinc.com
- Incoming Port: 993
- Encryption: SSL/TLS
- Outgoing Server: mail.fishmusicinc.com
- Outgoing Port: 587
- Encryption: STARTTLS
- Username: rp@fishmusicinc.com
- Password: [Your password]

ADVANCED SETTINGS:
☑ Outgoing server requires authentication
☑ Use same settings as incoming

STATUS: ✓ Ready to configure
EOF

# ==================== ACCOUNT 3: Fish Music Info ====================
cat > "$OUTPUT_DIR/3_info_fishmusicinc_config.txt" << 'EOF'
======================================
ACCOUNT 3: Fish Music Inc - Info
======================================

Email: info@fishmusicinc.com
Display Name: Info - Fish Music Inc
Provider: Custom Domain

SERVER SETTINGS:
- Account Type: IMAP
- Incoming Server: mail.fishmusicinc.com
- Incoming Port: 993
- Encryption: SSL/TLS
- Outgoing Server: mail.fishmusicinc.com
- Outgoing Port: 587
- Encryption: STARTTLS
- Username: info@fishmusicinc.com
- Password: [Your password]

Same setup process as Account 2 above.

STATUS: ✓ Ready to configure
EOF

# ==================== ACCOUNT 4: Noizylab RSP ====================
cat > "$OUTPUT_DIR/4_rsp_noizylab_config.txt" << 'EOF'
======================================
ACCOUNT 4: Noizylab - RSP
======================================

Email: rsp@noizylab.ca
Display Name: RSP - Noizylab
Provider: Custom Domain

SERVER SETTINGS:
- Account Type: IMAP
- Incoming Server: mail.noizylab.ca
- Incoming Port: 993
- Encryption: SSL/TLS
- Outgoing Server: mail.noizylab.ca
- Outgoing Port: 587
- Encryption: STARTTLS
- Username: rsp@noizylab.ca
- Password: [Your password]

ADVANCED SETTINGS:
☑ Outgoing server requires authentication
☑ Use same settings as incoming

STATUS: ✓ Ready to configure
EOF

# ==================== ACCOUNT 5: Noizylab Help ====================
cat > "$OUTPUT_DIR/5_help_noizylab_config.txt" << 'EOF'
======================================
ACCOUNT 5: Noizylab - Help
======================================

Email: help@noizylab.ca
Display Name: Help - Noizylab
Provider: Custom Domain

SERVER SETTINGS:
- Account Type: IMAP
- Incoming Server: mail.noizylab.ca
- Incoming Port: 993
- Encryption: SSL/TLS
- Outgoing Server: mail.noizylab.ca
- Outgoing Port: 587
- Encryption: STARTTLS
- Username: help@noizylab.ca
- Password: [Your password]

Same setup process as Account 4 above.

STATUS: ✓ Ready to configure
EOF

# ==================== ACCOUNT 6: Noizylab Hello ====================
cat > "$OUTPUT_DIR/6_hello_noizylab_config.txt" << 'EOF'
======================================
ACCOUNT 6: Noizylab - Hello
======================================

Email: hello@noizylab.ca
Display Name: Hello - Noizylab
Provider: Custom Domain

SERVER SETTINGS:
- Account Type: IMAP
- Incoming Server: mail.noizylab.ca
- Incoming Port: 993
- Encryption: SSL/TLS
- Outgoing Server: mail.noizylab.ca
- Outgoing Port: 587
- Encryption: STARTTLS
- Username: hello@noizylab.ca
- Password: [Your password]

Same setup process as Account 4 above.

STATUS: ✓ Ready to configure
EOF

# ==================== ACCOUNT 7: iCloud ====================
cat > "$OUTPUT_DIR/7_rsplowman_icloud_config.txt" << 'EOF'
======================================
ACCOUNT 7: iCloud
======================================

Email: rsplowman@icloud.com
Display Name: R Plowman - iCloud
Provider: Apple iCloud

IMPORTANT: Requires App-Specific Password!

STEP 1 - Generate App Password:
1. Go to: https://appleid.apple.com
2. Sign in
3. Security → App-Specific Passwords
4. Click "Generate password"
5. Label it "Outlook"
6. Copy the generated password

STEP 2 - Configure in Outlook:
- Email: rsplowman@icloud.com
- Password: [App-specific password from Step 1]

SERVER SETTINGS:
- Account Type: IMAP
- Incoming Server: imap.mail.me.com
- Incoming Port: 993
- Encryption: SSL/TLS
- Outgoing Server: smtp.mail.me.com
- Outgoing Port: 587
- Encryption: STARTTLS

STATUS: ✓ Ready to configure
EOF

# ==================== MASTER GUIDE ====================
cat > "$OUTPUT_DIR/MASTER_SETUP_GUIDE.md" << 'EOF'
# MICROSOFT OUTLOOK - COMPLETE SETUP GUIDE
## All 7 Email Accounts

---

## 📧 ACCOUNTS TO CONFIGURE

1. **rsplowman@gmail.com** (Gmail - PRIMARY)
2. **rp@fishmusicinc.com** (Fish Music Inc)
3. **info@fishmusicinc.com** (Fish Music Inc)
4. **rsp@noizylab.ca** (Noizylab)
5. **help@noizylab.ca** (Noizylab)
6. **hello@noizylab.ca** (Noizylab)
7. **rsplowman@icloud.com** (iCloud)

---

## 🚀 QUICK START

### For Each Account:
1. Open Outlook
2. **File → Add Account**
3. Enter email address
4. Click "Connect"
5. Enter password or follow OAuth
6. Wait for auto-configuration
7. If fails, use manual setup (see individual config files)

---

## 📋 SETUP ORDER (Recommended)

**Start with Primary:**
1. Gmail (rsplowman@gmail.com) - OAuth

**Then Business Emails:**
2. rp@fishmusicinc.com
3. info@fishmusicinc.com
4. rsp@noizylab.ca
5. help@noizylab.ca
6. hello@noizylab.ca

**Finally Cloud:**
7. iCloud (rsplowman@icloud.com) - App Password

---

## 🔐 PASSWORDS NEEDED

### Gmail:
- Option 1: Regular Gmail password + OAuth
- Option 2: App-specific password

### Fish Music Inc (both accounts):
- Email account passwords

### Noizylab (all 3 accounts):
- Email account passwords

### iCloud:
- App-specific password (REQUIRED)
  Generate at: https://appleid.apple.com

---

## ⚙️ SERVER SETTINGS QUICK REFERENCE

| Domain | IMAP Server | SMTP Server | Ports |
|--------|-------------|-------------|-------|
| Gmail | imap.gmail.com | smtp.gmail.com | 993/587 |
| Fish Music | mail.fishmusicinc.com | mail.fishmusicinc.com | 993/587 |
| Noizylab | mail.noizylab.ca | mail.noizylab.ca | 993/587 |
| iCloud | imap.mail.me.com | smtp.mail.me.com | 993/587 |

**All accounts:**
- IMAP Port: 993 (SSL/TLS)
- SMTP Port: 587 (STARTTLS)
- Authentication: Required

---

## 🎨 OUTLOOK ORGANIZATION

### Unified Inbox Setup:
1. View → View Settings
2. Enable "Show as Conversations"
3. Create folders for each domain:
   - 📁 Fish Music Inc
   - 📁 Noizylab
   - 📁 Personal (Gmail/iCloud)

### Color Categories:
- 🟢 Fish Music Inc emails
- 🔵 Noizylab emails
- 🟡 Personal emails

### Rules (Optional):
- Auto-categorize by sender domain
- Auto-file to specific folders
- Flag important contacts

---

## 🔧 TROUBLESHOOTING

### "Cannot connect to server"
✓ Check internet connection
✓ Verify server names
✓ Check firewall settings
✓ Use correct port numbers

### "Authentication failed"
✓ Gmail: Use OAuth or app password
✓ iCloud: MUST use app-specific password
✓ Custom domains: Verify password
✓ Username = full email address

### "Certificate error"
✓ Update Outlook to latest version
✓ Update Windows/macOS
✓ Check system date/time

---

## ✅ VERIFICATION

After setup, test each account:
- [ ] Send test email
- [ ] Receive test email
- [ ] Check sent items sync
- [ ] Verify folders appear
- [ ] Test reply/forward

---

## 📱 MOBILE SETUP

Download Microsoft Outlook app:
- iOS: App Store
- Android: Google Play

All accounts will sync automatically after desktop setup.

---

## 🎯 NEXT STEPS

1. Review individual config files (1-7)
2. Gather all passwords
3. Open Outlook
4. Add accounts one by one
5. Verify each is working
6. Set up organization (folders, rules)
7. Configure mobile app

---

## 📞 SUPPORT

If you need help:
1. Check individual config file
2. Review troubleshooting section
3. Contact email provider
4. Microsoft Outlook support

---

**All configuration files are in this directory!**
**Start with Account 1 (Gmail) and work through each one.**

✅ Ready to set up all 7 email accounts!
EOF

# ==================== QUICK REFERENCE ====================
cat > "$OUTPUT_DIR/QUICK_REFERENCE.txt" << 'EOF'
========================================
OUTLOOK SETUP - QUICK REFERENCE
========================================

ALL ACCOUNTS (7):
1. rsplowman@gmail.com
2. rp@fishmusicinc.com
3. info@fishmusicinc.com
4. rsp@noizylab.ca
5. help@noizylab.ca
6. hello@noizylab.ca
7. rsplowman@icloud.com

SETUP LOCATIONS:
File → Add Account

PORTS (All accounts):
IMAP: 993 (SSL/TLS)
SMTP: 587 (STARTTLS)

SPECIAL REQUIREMENTS:
- Gmail: OAuth or app password
- iCloud: App-specific password (REQUIRED)
- Custom domains: Regular passwords

GENERATE APP PASSWORDS:
Gmail: https://myaccount.google.com/apppasswords
iCloud: https://appleid.apple.com

========================================
EOF

# Print summary
echo "✅ CONFIGURATION FILES GENERATED!"
echo ""
echo "📁 Location: $OUTPUT_DIR"
echo ""
echo "Files created:"
ls -1 "$OUTPUT_DIR"
echo ""
echo "=========================================="
echo "🎯 NEXT STEPS:"
echo "=========================================="
echo ""
echo "1. Read the Master Guide:"
echo "   cat $OUTPUT_DIR/MASTER_SETUP_GUIDE.md"
echo ""
echo "2. Review each account config (1-7)"
echo ""
echo "3. Open Microsoft Outlook"
echo ""
echo "4. Add each account:"
echo "   File → Add Account"
echo ""
echo "5. Use the config files for settings"
echo ""
echo "=========================================="
echo "✅ Ready to configure all 7 emails!"
echo "=========================================="

