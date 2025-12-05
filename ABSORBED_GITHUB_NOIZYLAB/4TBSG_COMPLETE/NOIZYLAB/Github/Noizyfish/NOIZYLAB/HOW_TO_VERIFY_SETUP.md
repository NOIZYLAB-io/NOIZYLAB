# ✅ How to Verify Everything is Set Up

## Complete Verification Guide

This guide walks you through verifying that all components are properly configured:
- ✅ Domains (noizylab.ca, fishmusicinc.com)
- ✅ Email (Google Workspace)
- ✅ Cloudflare DNS
- ✅ Google Workspace
- ✅ All Devices

---

## 🚀 Quick Start: Automated Verification

### Step 1: Run DNS Verification Script

```bash
cd /Users/m2ultra/NOIZYLAB/misc
chmod +x verify-setup.sh
./verify-setup.sh
```

This script will:
- ✅ Check all MX records (email servers)
- ✅ Verify SPF records (email authentication)
- ✅ Verify DKIM records (email signing)
- ✅ Verify DMARC records (email policy)
- ✅ Verify MTA-STS records (TLS enforcement)
- ✅ Verify TLSRPT records (TLS reporting)

**Expected Result:** All checks should pass ✅

### Step 2: Run Email Connectivity Test

```bash
cd /Users/m2ultra/NOIZYLAB/misc
chmod +x test-email.sh
./test-email.sh
```

This script will:
- ✅ Test SMTP connectivity (outgoing email)
- ✅ Test IMAP connectivity (incoming email)
- ✅ Test DNS resolution
- ✅ Provide manual test instructions

---

## 📋 Manual Verification Checklist

### 1. Cloudflare DNS Verification

#### Check DNS Records in Cloudflare Dashboard

1. Go to: https://dash.cloudflare.com
2. Select domain: `noizylab.ca`
3. Go to **DNS** → **Records**
4. Verify these records exist:

**MX Records (5 total):**
- [ ] `noizylab.ca` → `ASPMX.L.GOOGLE.COM` (Priority: 1)
- [ ] `noizylab.ca` → `ALT1.ASPMX.L.GOOGLE.COM` (Priority: 5)
- [ ] `noizylab.ca` → `ALT2.ASPMX.L.GOOGLE.COM` (Priority: 5)
- [ ] `noizylab.ca` → `ALT3.ASPMX.L.GOOGLE.COM` (Priority: 10)
- [ ] `noizylab.ca` → `ALT4.ASPMX.L.GOOGLE.COM` (Priority: 10)

**TXT Records:**
- [ ] `noizylab.ca` → `v=spf1 include:_spf.google.com ~all` (SPF)
- [ ] `google._domainkey.noizylab.ca` → `v=DKIM1; k=rsa; p=[YOUR_KEY]` (DKIM)
- [ ] `_dmarc.noizylab.ca` → `v=DMARC1; p=quarantine; ...` (DMARC)
- [ ] `_mta-sts.noizylab.ca` → `v=STSv1; id=20240101000000` (MTA-STS)
- [ ] `_smtp._tls.noizylab.ca` → `v=TLSRPTv1; rua=mailto:...` (TLSRPT)

5. Repeat for `fishmusicinc.com`

#### Verify via Command Line

```bash
# Check MX records
dig +short MX noizylab.ca
dig +short MX fishmusicinc.com

# Check SPF
dig +short TXT noizylab.ca | grep spf
dig +short TXT fishmusicinc.com | grep spf

# Check DKIM
dig +short TXT google._domainkey.noizylab.ca
dig +short TXT google._domainkey.fishmusicinc.com

# Check DMARC
dig +short TXT _dmarc.noizylab.ca
dig +short TXT _dmarc.fishmusicinc.com

# Check MTA-STS
dig +short TXT _mta-sts.noizylab.ca
dig +short TXT _mta-sts.fishmusicinc.com

# Check TLSRPT
dig +short TXT _smtp._tls.noizylab.ca
dig +short TXT _smtp._tls.fishmusicinc.com
```

**Expected:** All commands should return records

---

### 2. Google Workspace Verification

#### Check Domain Verification

1. Go to: https://admin.google.com
2. Navigate: **Domains** → **Manage domains**
3. Verify:
   - [ ] `noizylab.ca` - Status: **Verified** ✅
   - [ ] `fishmusicinc.com` - Status: **Verified** ✅

#### Check Gmail Configuration

1. Go to: **Apps** → **Google Workspace** → **Gmail**
2. Verify:
   - [ ] Gmail enabled for `noizylab.ca`
   - [ ] Gmail enabled for `fishmusicinc.com`
   - [ ] Email routing configured

#### Check DKIM Status

1. Go to: **Apps** → **Google Workspace** → **Gmail** → **Authenticate email**
2. Select domain: `noizylab.ca`
3. Verify:
   - [ ] DKIM authentication: **Enabled** ✅
   - [ ] DKIM key generated
   - [ ] Public key matches DNS record
4. Repeat for `fishmusicinc.com`

#### Check User Mailboxes

1. Go to: **Users**
2. Verify these users exist:

**noizylab.ca:**
- [ ] `rsp@noizylab.ca` - Active ✅
- [ ] `help@noizylab.ca` - Active ✅
- [ ] `hello@noizylab.ca` - Active ✅
- [ ] `dmarc-reports@noizylab.ca` - Active ✅
- [ ] `tlsrpt@noizylab.ca` - Active ✅

**fishmusicinc.com:**
- [ ] `rp@fishmusicinc.com` - Active ✅
- [ ] `info@fishmusicinc.com` - Active ✅
- [ ] `dmarc-reports@fishmusicinc.com` - Active ✅
- [ ] `tlsrpt@fishmusicinc.com` - Active ✅

---

### 3. Terraform Configuration Verification

#### Check Configuration Files

```bash
cd /Users/m2ultra/NOIZYLAB/misc
ls -la *.tf *.tfvars
```

Verify files exist:
- [ ] `main.tf` - ✅ Present
- [ ] `variables.tf` - ✅ Present
- [ ] `versions.tf` - ✅ Present
- [ ] `terraform.tfvars` - ✅ Present (with actual values)

#### Check terraform.tfvars Values

```bash
cd /Users/m2ultra/NOIZYLAB/misc
cat terraform.tfvars
```

Verify all values are filled:
- [ ] `cloudflare_api_token` = `[YOUR_TOKEN]` (not empty)
- [ ] `zone_noizylab_ca` = `[ZONE_ID]` (not empty)
- [ ] `zone_fishmusicinc_com` = `[ZONE_ID]` (not empty)
- [ ] `dkim_public_key_noizylab` = `[DKIM_KEY]` (not placeholder)
- [ ] `dkim_public_key_fish` = `[DKIM_KEY]` (not placeholder)

#### Test Terraform Configuration

```bash
cd /Users/m2ultra/NOIZYLAB/misc

# Initialize (if not done)
terraform init

# Plan (dry run - doesn't make changes)
terraform plan

# Review output
# Should show: "No changes" if already deployed
# Or show: "24 to add" if not deployed yet
```

---

### 4. Email Functionality Testing

#### Test 1: Send Email from noizylab.ca

1. **On any device**, send email:
   - **From:** `rsp@noizylab.ca`
   - **To:** Your personal email (Gmail, Outlook, etc.)
   - **Subject:** Test Email from noizylab.ca
   - **Body:** This is a test email

2. **Check recipient inbox:**
   - [ ] Email arrives
   - [ ] Email appears in inbox (not spam)

3. **In Gmail, check authentication:**
   - Open email
   - Click three dots → **Show original**
   - Look for:
     - [ ] `SPF: PASS`
     - [ ] `DKIM: PASS`
     - [ ] `DMARC: PASS`

#### Test 2: Send Email from fishmusicinc.com

1. Send email:
   - **From:** `rp@fishmusicinc.com`
   - **To:** Your personal email
   - **Subject:** Test Email from fishmusicinc.com

2. Verify:
   - [ ] Email arrives
   - [ ] Authentication passes (SPF/DKIM/DMARC)

#### Test 3: Receive Email to noizylab.ca

1. **From your personal email**, send to:
   - **To:** `rsp@noizylab.ca`
   - **Subject:** Test Email to noizylab.ca

2. **Check on ALL devices:**
   - [ ] iPhone: Email arrives
   - [ ] iPad: Email arrives
   - [ ] macOS: Email arrives
   - [ ] Other devices: Email arrives

#### Test 4: Receive Email to fishmusicinc.com

1. Send email:
   - **To:** `rp@fishmusicinc.com`
   - **Subject:** Test Email to fishmusicinc.com

2. Verify on all devices:
   - [ ] Email arrives everywhere

---

### 5. Device-Specific Verification

#### iPhone Verification

1. **Open Mail app**
2. Check:
   - [ ] Both accounts visible in account list
   - [ ] Can switch between accounts
   - [ ] Can send from both accounts
   - [ ] Can receive to both accounts
   - [ ] Push notifications working

3. **Settings** → **Mail** → **Accounts**
   - [ ] `rsp@noizylab.ca` - Configured ✅
   - [ ] `rp@fishmusicinc.com` - Configured ✅

#### iPad Verification

1. **Open Mail app**
2. Check:
   - [ ] Both accounts configured
   - [ ] Multi-pane view works (landscape)
   - [ ] Can send/receive from both accounts
   - [ ] Split view works with other apps

#### macOS Verification

1. **Open Mail app**
2. Check:
   - [ ] Both accounts in sidebar
   - [ ] Can send from both accounts
   - [ ] Can receive to both accounts
   - [ ] Mail rules working (if configured)

#### Other Devices

- [ ] Windows: Email working
- [ ] Android: Email working
- [ ] Linux: Email working
- [ ] Web browser: Gmail accessible

---

### 6. Calendar & Contacts Verification

#### Calendar Sync

**On each device:**
- [ ] Calendar app shows Google calendars
- [ ] Can create events
- [ ] Events sync across devices
- [ ] Can view shared calendars

#### Contacts Sync

**On each device:**
- [ ] Contacts app shows Google contacts
- [ ] Can add/edit contacts
- [ ] Contacts sync across devices
- [ ] Contacts appear when composing email

---

## 🔍 Advanced Verification

### Check Email Authentication Scores

Use these tools to verify email reputation:

1. **MXToolbox Email Health:**
   - https://mxtoolbox.com/emailhealth/
   - Enter: `rsp@noizylab.ca`
   - Check: SPF, DKIM, DMARC scores

2. **Mail-Tester:**
   - https://www.mail-tester.com/
   - Send email to provided address
   - Check: Score should be 8-10/10

3. **Google Postmaster Tools:**
   - https://postmaster.google.com/
   - Add domain
   - Monitor: SPF, DKIM, DMARC pass rates

### Check DNS Propagation

```bash
# Check from different DNS servers
dig @8.8.8.8 +short MX noizylab.ca      # Google DNS
dig @1.1.1.1 +short MX noizylab.ca     # Cloudflare DNS
dig @208.67.222.222 +short MX noizylab.ca  # OpenDNS
```

All should return same results.

---

## ✅ Final Verification Checklist

### Infrastructure
- [ ] Cloudflare DNS records configured
- [ ] Google Workspace domains verified
- [ ] DKIM keys generated and in DNS
- [ ] Terraform configuration complete

### Email Functionality
- [ ] Can send from noizylab.ca
- [ ] Can send from fishmusicinc.com
- [ ] Can receive to noizylab.ca
- [ ] Can receive to fishmusicinc.com
- [ ] SPF authentication passes
- [ ] DKIM authentication passes
- [ ] DMARC authentication passes

### Devices
- [ ] iPhone: Email working
- [ ] iPad: Email working
- [ ] macOS: Email working
- [ ] Other devices: Email working
- [ ] Calendar syncing on all devices
- [ ] Contacts syncing on all devices

### Security
- [ ] Two-factor authentication enabled
- [ ] App passwords generated (if needed)
- [ ] Security policies configured

---

## 🆘 Troubleshooting

### If DNS Verification Fails

1. **Check Cloudflare Dashboard:**
   - Verify records exist
   - Check for typos
   - Verify zone IDs are correct

2. **Check Terraform:**
   ```bash
   cd /Users/m2ultra/NOIZYLAB/misc
   terraform plan
   ```
   - Review planned changes
   - Apply if needed: `terraform apply`

3. **Wait for Propagation:**
   - DNS changes can take 5-60 minutes
   - Cloudflare is usually instant

### If Email Sending Fails

1. **Check SMTP Settings:**
   - Server: `smtp.gmail.com`
   - Port: `587` (STARTTLS) or `465` (SSL)
   - Authentication: OAuth 2.0 or App Password

2. **Check Google Workspace:**
   - Verify account is active
   - Check for security alerts
   - Verify 2FA is working

### If Email Receiving Fails

1. **Check IMAP Settings:**
   - Server: `imap.gmail.com`
   - Port: `993` (SSL)
   - Authentication: OAuth 2.0

2. **Check MX Records:**
   ```bash
   dig +short MX noizylab.ca
   ```
   - Should show Google MX records

---

## 📞 Quick Reference

**Verification Scripts:**
- DNS: `./verify-setup.sh`
- Email: `./test-email.sh`

**Important Links:**
- Cloudflare: https://dash.cloudflare.com
- Google Admin: https://admin.google.com
- Gmail: https://mail.google.com

**Configuration Location:**
- `/Users/m2ultra/NOIZYLAB/misc/`

---

**Last Updated:** 2024-11-22  
**Status:** ✅ Ready for Verification

