# Google Email Aliases Setup Guide

## Email Addresses to Configure:
- `rp@fishmusicinc.com` → `rsplowman@gmail.com`
- `rsp@noizylab.ca` → `rsplowman@gmail.com`
- `help@noizylab.ca` → `rsplowman@gmail.com` (Note: you typed "noiylab" but assuming "noizylab")

---

## IMPORTANT: Two Different Approaches

### Option 1: Regular Gmail (Free) - Limited
**What you CAN do:**
- Add Gmail aliases like: `rsplowman+alias@gmail.com`
- Cannot use custom domains (fishmusicinc.com, noizylab.ca)

**Limitation:** Regular Gmail accounts cannot receive email at custom domain addresses.

---

### Option 2: Google Workspace (Required for Custom Domains)
**What you NEED:**
- Google Workspace account (paid, ~$6-12/month per user)
- Domain ownership of:
  - `fishmusicinc.com`
  - `noizylab.ca`
- DNS access to configure MX records

---

## Setup Steps for Google Workspace

### Step 1: Verify Domain Ownership

1. **Sign up for Google Workspace:**
   - Go to: https://workspace.google.com/
   - Choose a plan (Business Starter recommended)
   - Use your primary email: `rsplowman@gmail.com` as admin

2. **Add Your Domains:**
   - In Google Admin Console → Domains
   - Add `fishmusicinc.com`
   - Add `noizylab.ca`
   - Follow verification steps

### Step 2: Configure DNS Records

For each domain, add these DNS records:

#### For `fishmusicinc.com`:
```
Type: MX
Priority: 1
Value: ASPMX.L.GOOGLE.COM

Type: MX
Priority: 5
Value: ALT1.ASPMX.L.GOOGLE.COM

Type: MX
Priority: 5
Value: ALT2.ASPMX.L.GOOGLE.COM

Type: MX
Priority: 10
Value: ALT3.ASPMX.L.GOOGLE.COM

Type: MX
Priority: 10
Value: ALT4.ASPMX.L.GOOGLE.COM

Type: TXT
Name: @
Value: v=spf1 include:_spf.google.com ~all
```

#### For `noizylab.ca`:
```
(Same MX records as above)
```

### Step 3: Create Email Aliases

1. **In Google Admin Console:**
   - Go to: Users → Select `rsplowman@gmail.com` (or your Workspace user)
   - Click: "Email aliases"
   - Add aliases:
     - `rp@fishmusicinc.com`
     - `rsp@noizylab.ca`
     - `help@noizylab.ca`

2. **Alternative: Create User Groups**
   - Create groups for each alias
   - Add `rsplowman@gmail.com` as member
   - Emails to aliases will forward to your main account

---

## Quick Setup Script (Manual Steps)

Since Google Workspace requires web-based configuration, here's a checklist:

```bash
# This script creates a setup checklist
cat > ~/Desktop/GOOGLE_ALIASES_SETUP.txt << 'EOF'
GOOGLE EMAIL ALIASES SETUP CHECKLIST
====================================

□ Sign up for Google Workspace
  → https://workspace.google.com/
  → Use rsplowman@gmail.com as admin

□ Verify domain ownership:
  □ fishmusicinc.com
  □ noizylab.ca

□ Configure DNS MX records (at domain registrar):
  □ fishmusicinc.com MX records
  □ noizylab.ca MX records

□ Add email aliases in Google Admin:
  □ rp@fishmusicinc.com → rsplowman@gmail.com
  □ rsp@noizylab.ca → rsplowman@gmail.com
  □ help@noizylab.ca → rsplowman@gmail.com

□ Test email delivery:
  □ Send test email to rp@fishmusicinc.com
  □ Send test email to rsp@noizylab.ca
  □ Send test email to help@noizylab.ca

□ Configure email client (if needed):
  □ Add aliases to macOS Mail
  □ Configure send-as addresses
EOF
```

---

## Alternative: Email Forwarding (Simpler, Free)

If you don't want Google Workspace, you can:

1. **Use your domain registrar's email forwarding:**
   - Most registrars offer free email forwarding
   - Forward: `rp@fishmusicinc.com` → `rsplowman@gmail.com`
   - Forward: `rsp@noizylab.ca` → `rsplowman@gmail.com`
   - Forward: `help@noizylab.ca` → `rsplowman@gmail.com`

2. **Configure in Gmail to send as:**
   - Gmail Settings → Accounts → "Send mail as"
   - Add each alias
   - Verify via email confirmation

---

## macOS Mail App Configuration

Once aliases are set up, configure macOS Mail:

1. **Add Gmail Account:**
   - Mail → Preferences → Accounts
   - Add: `rsplowman@gmail.com`

2. **Add Send-As Addresses:**
   - Select Gmail account
   - Click "Email Address" → "Edit Email Addresses"
   - Add:
     - `rp@fishmusicinc.com`
     - `rsp@noizylab.ca`
     - `help@noizylab.ca`

---

## Cost Estimate

- **Google Workspace:** ~$6-12/month per user
- **Domain Email Forwarding:** Usually FREE with domain registration
- **Regular Gmail:** FREE (but can't use custom domains)

---

## Recommendation

**For quick setup:** Use domain registrar's email forwarding (FREE)
**For professional setup:** Google Workspace (paid, but full control)

---

## Next Steps

1. Check if you have Google Workspace account
2. If not, decide: Workspace (paid) or forwarding (free)
3. Configure DNS records at domain registrar
4. Set up aliases/forwarding
5. Test email delivery

---

**Created:** $(date)
**For:** rsplowman@gmail.com
**Aliases:** rp@fishmusicinc.com, rsp@noizylab.ca, help@noizylab.ca

