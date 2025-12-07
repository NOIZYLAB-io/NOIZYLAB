# MICROSOFT OUTLOOK - COMPLETE SETUP GUIDE
## All Email Accounts - M365 Hub Central

---

## 📧 ACCOUNTS TO CONFIGURE (PRIORITY ORDER)

1. **rsplowman@outlook.com** (Microsoft 365 - PRIMARY HUB)
2. **rsplowman@icloud.com** (iCloud - Apple ecosystem)
3. **rp@fishmusicinc.com** (Fish Music Inc)
4. **info@fishmusicinc.com** (Fish Music Inc)
5. **rsp@noizylab.ca** (Noizylab)
6. **help@noizylab.ca** (Noizylab)
7. **hello@noizylab.ca** (Noizylab)

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

**Start with M365 Hub (Primary):**
1. Outlook (rsplowman@outlook.com) - M365 OAuth

**Then Apple Ecosystem:**
2. iCloud (rsplowman@icloud.com) - App Password

**Then Business Emails:**
3. rp@fishmusicinc.com
4. info@fishmusicinc.com
5. rsp@noizylab.ca
6. help@noizylab.ca
7. hello@noizylab.ca

---

## 🔐 PASSWORDS NEEDED

### Microsoft 365 (Primary Hub):
- rsplowman@outlook.com: M365 password + Modern OAuth
- Full Microsoft 365 integration

### iCloud:
- App-specific password (REQUIRED)
  Generate at: https://appleid.apple.com

### Fish Music Inc (both accounts):
- Email account passwords

### Noizylab (all 3 accounts):
- Email account passwords

---

## ⚙️ SERVER SETTINGS QUICK REFERENCE

| Domain | IMAP Server | SMTP Server | Ports |
|--------|-------------|-------------|-------|
| Microsoft 365 | outlook.office365.com | smtp.office365.com | 993/587 |
| iCloud | imap.mail.me.com | smtp.mail.me.com | 993/587 |
| Fish Music | imap.gmail.com | smtp.gmail.com | 993/587 |
| Noizylab | imap.gmail.com | smtp.gmail.com | 993/587 |

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
