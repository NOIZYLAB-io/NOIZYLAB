# Email Setup Quick Reference

## Your Email Accounts

### Personal/Business:
1. **rsp@noizylab.ca** - Custom domain email
2. **help@noizylab.ca** - Custom domain email
3. **rsplowman@icloud.com** - iCloud email (to add to Gmail account)
4. **rp@fishmusicinc.com** - Business email (check for verification emails)

### Gmail:
- Your Gmail account (to add to Mac Mail)

---

## Quick Setup Guide

### 1. Gmail in Mac Mail
**Use IT Genius:** Email Setup → Option 8
**Or run:** `python3 setup_gmail_macmail.py`

### 2. Add rsplowman@icloud.com to Gmail Account
**Use IT Genius:** Email Setup → Option 9
**Or:** Go to https://myaccount.google.com/ → Personal info → Email → Add alternate email

### 3. Setup noizylab.ca Emails (rsp@noizylab.ca, help@noizylab.ca)
**Use IT Genius:** Email Setup → Option 5 (Custom Domain Email)

**You'll need:**
- IMAP Server (usually: mail.noizylab.ca or provided by hosting)
- SMTP Server (usually: mail.noizylab.ca or provided by hosting)
- Ports: 993 (IMAP), 587 (SMTP)
- Security: SSL/TLS
- Username: rsp@noizylab.ca or help@noizylab.ca
- Password: Your email account password

**To find exact settings:**
- Check with your web hosting provider
- Check cPanel or hosting control panel
- Check email provider documentation

### 4. Check Verification Email to rp@fishmusicinc.com

**Where to check:**
1. **Mac Mail app** - Open Mail, select rp@fishmusicinc.com account
2. **Webmail** - Log into your email provider's webmail
3. **Check Spam folder** - Verification emails sometimes go there

**What to look for:**
- Emails with subject containing "verification" or "verify"
- From Google, Microsoft, or your hosting provider
- Usually arrive within a few minutes

---

## IT Genius Navigation

**Main Menu → Email Account Setup:**
- Option 1: Setup Gmail Account
- Option 2: Setup iCloud Account
- Option 5: Setup Custom Domain Email ← **Use this for noizylab.ca**
- Option 8: Gmail in Mac Mail - Step-by-Step Guide
- Option 9: Add Alternate Email to Gmail Account

---

## Common Email Server Settings

### Standard Web Hosting (cPanel):
- IMAP: mail.yourdomain.com (Port 993, SSL/TLS)
- SMTP: mail.yourdomain.com (Port 587, STARTTLS)

### Google Workspace:
- IMAP: imap.gmail.com (Port 993, SSL/TLS)
- SMTP: smtp.gmail.com (Port 587, STARTTLS)

### Microsoft 365:
- IMAP: outlook.office365.com (Port 993, SSL/TLS)
- SMTP: smtp.office365.com (Port 587, STARTTLS)

---

## Need Help?

1. **Run IT Genius:** `python3 it_genius.py`
2. **Use Email Setup module** for step-by-step guidance
3. **Check documentation files:**
   - `gmail_macmail_setup.md`
   - `noizylab_email_setup.md`

