# 🔐 Complete Setup Confirmation Checklist
## Domains, Email, Cloudflare & Google - ALL DEVICES

**Domains:** `noizylab.ca` | `fishmusicinc.com`  
**Date:** 2024-11-22  
**Status:** ⚠️ Verification Required

---

## 📋 PRE-FLIGHT CHECKLIST

### ☁️ Cloudflare Configuration

#### ✅ Cloudflare Account Setup
- [ ] Cloudflare account active for both domains
- [ ] Both domains added to Cloudflare:
  - [ ] `noizylab.ca` - Status: Active
  - [ ] `fishmusicinc.com` - Status: Active
- [ ] Cloudflare API Token created:
  - [ ] Token: `_____________________` (stored in terraform.tfvars)
  - [ ] Permissions: `Zone.DNS (Edit)` + `Zone.Zone (Read)`
  - [ ] Token verified and working

#### ✅ Cloudflare Zone IDs
- [ ] `noizylab.ca` Zone ID: `_____________________`
- [ ] `fishmusicinc.com` Zone ID: `_____________________`
- [ ] Zone IDs verified in Cloudflare Dashboard

#### ✅ Cloudflare DNS Records Status
Check current DNS records in Cloudflare:
- [ ] MX records exist for both domains
- [ ] TXT records exist (SPF, DKIM, DMARC, MTA-STS, TLSRPT)
- [ ] No conflicting records
- [ ] DNS propagation verified

---

### 📧 Google Workspace Setup

#### ✅ Google Workspace Account
- [ ] Google Workspace subscription active
- [ ] Admin access verified: `https://admin.google.com`
- [ ] Both domains verified in Google Admin:
  - [ ] `noizylab.ca` - Verified ✅
  - [ ] `fishmusicinc.com` - Verified ✅

#### ✅ Gmail Configuration
- [ ] Gmail enabled for both domains:
  - [ ] `noizylab.ca` - Gmail: Enabled
  - [ ] `fishmusicinc.com` - Gmail: Enabled
- [ ] Email routing configured
- [ ] Catch-all addresses configured (if needed)

#### ✅ User Mailboxes Created
**noizylab.ca:**
- [ ] `rsp@noizylab.ca` - Created & Tested
- [ ] `help@noizylab.ca` - Created & Tested
- [ ] `hello@noizylab.ca` - Created & Tested
- [ ] `dmarc-reports@noizylab.ca` - Created for DMARC reports
- [ ] `tlsrpt@noizylab.ca` - Created for TLS reports

**fishmusicinc.com:**
- [ ] `rp@fishmusicinc.com` - Created & Tested
- [ ] `info@fishmusicinc.com` - Created & Tested
- [ ] `dmarc-reports@fishmusicinc.com` - Created for DMARC reports
- [ ] `tlsrpt@fishmusicinc.com` - Created for TLS reports

#### ✅ DKIM Keys Generated
- [ ] **noizylab.ca DKIM:**
  - [ ] DKIM authentication enabled in Google Admin
  - [ ] DKIM selector: `google` (default)
  - [ ] Public key retrieved: `_____________________`
  - [ ] Key format verified (base64, no headers/footers)

- [ ] **fishmusicinc.com DKIM:**
  - [ ] DKIM authentication enabled in Google Admin
  - [ ] DKIM selector: `google` (default)
  - [ ] Public key retrieved: `_____________________`
  - [ ] Key format verified (base64, no headers/footers)

**How to get DKIM keys:**
1. Go to: Google Admin Console → Apps → Google Workspace → Gmail
2. Select: Authenticate email
3. Select domain → Show Authentication
4. Copy DKIM public key (text only, no formatting)

---

### 🗄️ Terraform Configuration

#### ✅ Terraform Setup
- [ ] Terraform installed: `terraform version`
- [ ] Terraform version: `_____________________` (>= 1.6.0 required)
- [ ] Cloudflare provider available
- [ ] Configuration files located: `/Users/m2ultra/NOIZYLAB/misc/`

#### ✅ Configuration Files Status
- [ ] `main.tf` - ✅ Complete (both domains configured)
- [ ] `variables.tf` - ✅ Complete
- [ ] `versions.tf` - ✅ Complete
- [ ] `terraform.tfvars` - ⚠️ **NEEDS VALUES** (contains API tokens/keys)
- [ ] `terraform.tfvars.example` - ✅ Template available

#### ✅ terraform.tfvars Configuration
Edit `/Users/m2ultra/NOIZYLAB/misc/terraform.tfvars` and verify:
- [ ] `cloudflare_api_token` = `[YOUR_TOKEN]`
- [ ] `zone_noizylab_ca` = `[ZONE_ID]`
- [ ] `zone_fishmusicinc_com` = `[ZONE_ID]`
- [ ] `dkim_public_key_noizylab` = `[DKIM_KEY]`
- [ ] `dkim_public_key_fish` = `[DKIM_KEY]`
- [ ] DMARC policies set (quarantine/reject)
- [ ] DMARC reporting emails configured

---

## 🖥️ DEVICE SETUP CHECKLIST

### 📱 macOS Devices

#### ✅ Mail App Configuration
- [ ] Mail.app configured for `rsp@noizylab.ca`
- [ ] Mail.app configured for `rp@fishmusicinc.com`
- [ ] IMAP settings:
  - [ ] Incoming: `imap.gmail.com:993` (SSL)
  - [ ] Outgoing: `smtp.gmail.com:587` (TLS)
  - [ ] Authentication: OAuth 2.0 or App Password
- [ ] Test send/receive successful
- [ ] Folders syncing correctly

#### ✅ Browser Access
- [ ] Gmail web interface accessible: `https://mail.google.com`
- [ ] Both accounts accessible via browser
- [ ] Bookmarks configured
- [ ] Browser extensions installed (if needed)

#### ✅ Calendar & Contacts
- [ ] Google Calendar app configured
- [ ] Contacts syncing with Google
- [ ] Calendar events syncing
- [ ] Shared calendars accessible

---

### 📱 iOS Devices (iPhone/iPad)

#### ✅ Mail App Configuration
- [ ] Settings → Mail → Accounts
- [ ] `rsp@noizylab.ca` account added
- [ ] `rp@fishmusicinc.com` account added
- [ ] IMAP settings configured:
  - [ ] Incoming: `imap.gmail.com:993`
  - [ ] Outgoing: `smtp.gmail.com:587`
  - [ ] OAuth 2.0 authentication
- [ ] Push notifications enabled
- [ ] Test send/receive successful

#### ✅ Gmail App (Alternative)
- [ ] Gmail app installed from App Store
- [ ] Both accounts logged in
- [ ] Notifications configured
- [ ] Widget configured (if needed)

#### ✅ Calendar & Contacts
- [ ] Settings → Calendar → Accounts
- [ ] Google accounts added
- [ ] Calendar syncing enabled
- [ ] Contacts syncing enabled

#### ✅ Device-Specific Settings
- [ ] Passcode/Touch ID/Face ID enabled
- [ ] Two-factor authentication enabled
- [ ] Find My iPhone enabled
- [ ] iCloud backup configured

---

### 🤖 Android Devices

#### ✅ Gmail App Configuration
- [ ] Gmail app installed (from Play Store)
- [ ] `rsp@noizylab.ca` account added
- [ ] `rp@fishmusicinc.com` account added
- [ ] OAuth 2.0 authentication
- [ ] Sync enabled for mail, contacts, calendar
- [ ] Notifications configured
- [ ] Test send/receive successful

#### ✅ Email App (Alternative)
- [ ] Default email app configured
- [ ] IMAP/SMTP settings configured:
  - [ ] Incoming: `imap.gmail.com:993`
  - [ ] Outgoing: `smtp.gmail.com:587`
  - [ ] Authentication: OAuth 2.0 or App Password
- [ ] Test send/receive successful

#### ✅ Calendar & Contacts
- [ ] Google Calendar app installed
- [ ] Contacts app syncing with Google
- [ ] Calendar events syncing
- [ ] Widgets configured (if needed)

#### ✅ Device-Specific Settings
- [ ] Screen lock enabled
- [ ] Two-factor authentication enabled
- [ ] Device encryption enabled
- [ ] Google Backup enabled

---

### 💻 Windows Devices

#### ✅ Outlook Configuration
- [ ] Outlook installed (Office 365 or standalone)
- [ ] `rsp@noizylab.ca` account added
- [ ] `rp@fishmusicinc.com` account added
- [ ] IMAP settings:
  - [ ] Incoming: `imap.gmail.com:993`
  - [ ] Outgoing: `smtp.gmail.com:587`
  - [ ] Authentication: OAuth 2.0
- [ ] Test send/receive successful
- [ ] Calendar syncing

#### ✅ Mail App (Windows 10/11)
- [ ] Windows Mail app configured
- [ ] Both accounts added
- [ ] IMAP/SMTP configured
- [ ] Test send/receive successful

#### ✅ Browser Access
- [ ] Chrome/Edge configured
- [ ] Gmail bookmarked
- [ ] Browser extensions (if needed)

---

### 🌐 Linux Devices

#### ✅ Mail Client Configuration
- [ ] Thunderbird/Evolution/Mutt configured
- [ ] Both email accounts added
- [ ] IMAP settings:
  - [ ] Incoming: `imap.gmail.com:993`
  - [ ] Outgoing: `smtp.gmail.com:587`
  - [ ] OAuth 2.0 or App Password
- [ ] Test send/receive successful

#### ✅ Command Line Tools
- [ ] `mutt` or `neomutt` configured (if used)
- [ ] `offlineimap` or `mbsync` configured (if used)
- [ ] GPG encryption configured (if used)

---

## 🔍 DNS VERIFICATION CHECKLIST

### ✅ Verify DNS Records via Command Line

Run these commands on each device to verify DNS records:

#### noizylab.ca Verification:
```bash
# MX Records
dig +short MX noizylab.ca
# Expected: 5 Google MX records

# SPF Record
dig +short TXT noizylab.ca | grep spf
# Expected: "v=spf1 include:_spf.google.com ~all"

# DKIM Record
dig +short TXT google._domainkey.noizylab.ca
# Expected: "v=DKIM1; k=rsa; p=[YOUR_KEY]"

# DMARC Record
dig +short TXT _dmarc.noizylab.ca
# Expected: "v=DMARC1; p=quarantine; rua=mailto:..."

# MTA-STS Record
dig +short TXT _mta-sts.noizylab.ca
# Expected: "v=STSv1; id=20240101000000"

# TLSRPT Record
dig +short TXT _smtp._tls.noizylab.ca
# Expected: "v=TLSRPTv1; rua=mailto:..."
```

#### fishmusicinc.com Verification:
```bash
# Repeat all above commands replacing "noizylab.ca" with "fishmusicinc.com"
dig +short MX fishmusicinc.com
dig +short TXT fishmusicinc.com | grep spf
dig +short TXT google._domainkey.fishmusicinc.com
dig +short TXT _dmarc.fishmusicinc.com
dig +short TXT _mta-sts.fishmusicinc.com
dig +short TXT _smtp._tls.fishmusicinc.com
```

---

## 📧 EMAIL DELIVERY TEST CHECKLIST

### ✅ Send Test Emails

Test email delivery from ALL devices:

**From each device, send test email:**

1. **Send TO Gmail:**
   - [ ] From `rsp@noizylab.ca` to personal Gmail
   - [ ] From `rp@fishmusicinc.com` to personal Gmail
   - [ ] Check "Show original" in Gmail
   - [ ] Verify: SPF ✅ PASS | DKIM ✅ PASS | DMARC ✅ PASS

2. **Send TO Outlook/Hotmail:**
   - [ ] From `rsp@noizylab.ca` to Outlook
   - [ ] From `rp@fishmusicinc.com` to Outlook
   - [ ] Verify delivery and authentication

3. **Send TO Yahoo:**
   - [ ] From `rsp@noizylab.ca` to Yahoo
   - [ ] From `rp@fishmusicinc.com` to Yahoo
   - [ ] Verify delivery and authentication

4. **Send TO Other Providers:**
   - [ ] ProtonMail
   - [ ] Apple iCloud
   - [ ] Other business emails
   - [ ] Verify delivery

5. **Receive Test Emails:**
   - [ ] Send TO `rsp@noizylab.ca` from external email
   - [ ] Send TO `rp@fishmusicinc.com` from external email
   - [ ] Verify received on ALL devices

---

## 🔒 SECURITY CHECKLIST

### ✅ Two-Factor Authentication
- [ ] Google Workspace 2FA enabled for all admin accounts
- [ ] Google Workspace 2FA enabled for all user accounts
- [ ] Backup codes saved securely
- [ ] Recovery email/phone configured

### ✅ App Passwords (if needed)
- [ ] App passwords generated for legacy apps
- [ ] App passwords stored securely
- [ ] App passwords documented

### ✅ Security Policies
- [ ] Google Workspace security policies configured
- [ ] Password policies enforced
- [ ] Device management policies set
- [ ] Data loss prevention (DLP) configured (if needed)

---

## 🧪 FINAL VERIFICATION

### ✅ Comprehensive Test

**On EACH device, verify:**

1. **Send Email:**
   - [ ] Can send from `rsp@noizylab.ca`
   - [ ] Can send from `rp@fishmusicinc.com`
   - [ ] Email arrives in recipient inbox
   - [ ] Authentication passes (SPF/DKIM/DMARC)

2. **Receive Email:**
   - [ ] Can receive emails sent to `rsp@noizylab.ca`
   - [ ] Can receive emails sent to `rp@fishmusicinc.com`
   - [ ] Push notifications working (mobile devices)
   - [ ] Notifications appear on all devices

3. **Calendar:**
   - [ ] Can view calendar on all devices
   - [ ] Can create/edit events
   - [ ] Events sync across devices

4. **Contacts:**
   - [ ] Contacts accessible on all devices
   - [ ] Contacts sync across devices
   - [ ] Can add/edit contacts

---

## 📝 QUICK REFERENCE

### 📧 Email Server Settings
```
IMAP (Incoming):
  Server: imap.gmail.com
  Port: 993
  Security: SSL/TLS

SMTP (Outgoing):
  Server: smtp.gmail.com
  Port: 587
  Security: STARTTLS
  Port: 465 (Alternative)
  Security: SSL
```

### 🔗 Important Links
- Google Admin: https://admin.google.com
- Gmail: https://mail.google.com
- Cloudflare Dashboard: https://dash.cloudflare.com
- Terraform Config: `/Users/m2ultra/NOIZYLAB/misc/`

### 🛠️ Troubleshooting Commands
```bash
# Check DNS propagation
dig @8.8.8.8 +short MX noizylab.ca
dig @1.1.1.1 +short MX noizylab.ca

# Test email connectivity
telnet smtp.gmail.com 587
telnet imap.gmail.com 993

# Verify DKIM
dig +short TXT google._domainkey.noizylab.ca

# Check DMARC reports
# (Check inbox of dmarc-reports@noizylab.ca)
```

---

## ✅ SIGN-OFF

**Setup Completed By:** _____________________  
**Date Completed:** _____________________  
**Verified On Devices:**
- [ ] macOS: _____________________
- [ ] iOS: _____________________
- [ ] Android: _____________________
- [ ] Windows: _____________________
- [ ] Linux: _____________________

**Notes:**
```
[Add any important notes or issues here]
```

---

**Last Updated:** 2024-11-22  
**Version:** 1.0  
**Status:** ⚠️ Requires Verification

