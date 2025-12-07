# 🎯 ROB'S EMAIL EMPIRE - MASTER CONFIG
## 6 Emails. One Inbox. Zero Friction.

---

## THE 6 EMAILS

| # | Address | Domain | Purpose |
|---|---------|--------|---------|
| 1 | `rsplowman@outlook.com` | Microsoft 365 | PRIMARY M365 LOGIN |
| 2 | `rp@fishmusicinc.com` | Fish Music | Business email |
| 3 | `info@fishmusicinc.com` | Fish Music | General inquiries |
| 4 | `rsp@noizylab.ca` | NOIZYLAB | Repair business |
| 5 | `help@noizylab.ca` | NOIZYLAB | Customer support |
| 6 | `hello@noizylab.ca` | NOIZYLAB | Friendly contact |

---

## 🔥 THE GOAL

```
ALL 6 EMAILS → rsplowman@outlook.com inbox
SEND FROM → Any of the 6 addresses
ONE INBOX → Microsoft 365 rules everything
```

---

## ⚡ STEP 1: ADD "SEND AS" ADDRESSES

**URL:** `https://outlook.office365.com/mail/options/mail/accounts`

In **"Connected accounts"** or **"Send from another address"** section:

### Primary Account
```
✅ rsplowman@outlook.com   → Primary M365 account
```

### Business Domains (Setup forwarding or aliases)
```
➕ rp@fishmusicinc.com     → Add as send-as
➕ info@fishmusicinc.com   → Add as send-as
➕ rsp@noizylab.ca         → Add as send-as
➕ help@noizylab.ca        → Add as send-as
➕ hello@noizylab.ca       → Add as send-as
```

**For custom domain addresses, use these SMTP settings:**
```
SMTP Server: smtp.office365.com
Port: 587
Username: rsplowman@outlook.com
Password: M365 Password or App Password
TLS: Yes
```

---

## ⚡ STEP 2: FORWARDING SETUP

### For all business emails:
**Option A: Microsoft 365 Email Forwarding**
- In your domain's email admin (cPanel, Google Workspace, etc.)
- Set up forwarding rules:
```
rp@fishmusicinc.com    → rsplowman@outlook.com
info@fishmusicinc.com  → rsplowman@outlook.com
rsp@noizylab.ca        → rsplowman@outlook.com
help@noizylab.ca       → rsplowman@outlook.com
hello@noizylab.ca      → rsplowman@outlook.com
```

**Option B: Cloudflare Email Routing** (if using Cloudflare)
- Dashboard → Email → Email Routing
- Add routes to rsplowman@outlook.com

---

## ⚡ STEP 3: OUTLOOK FILTERS (Auto-Label)

**URL:** `https://outlook.office365.com/mail/options/mail/rules`

Create these rules:

### Filter 1: Fish Music
```
When email arrives:
- To: rp@fishmusicinc.com OR info@fishmusicinc.com
Move to folder: 🐟 Fish Music
Mark as important
```

### Filter 2: NOIZYLAB Support
```
When email arrives:
- To: help@noizylab.ca
Move to folder: 🔧 NOIZYLAB Support
Star it
Mark as important
```

### Filter 3: NOIZYLAB General
```
When email arrives:
- To: hello@noizylab.ca OR rsp@noizylab.ca
Move to folder: 🔧 NOIZYLAB
```

---

## ⚡ STEP 4: PROFESSIONAL SIGNATURES

### For rsplowman@outlook.com
```
--
Rob Plowman
Microsoft 365 Primary Account

🌐 noizylab.ca | fishmusicinc.com
📧 rsplowman@outlook.com
```

### For rp@fishmusicinc.com
```
--
Rob Plowman
Composer | Sound Designer | Producer
Fish Music Inc. • 40+ Years

🌐 fishmusicinc.com
📧 rp@fishmusicinc.com
```

### For info@fishmusicinc.com
```
--
Fish Music Inc.
Professional Music Composition & Sound Design

🌐 fishmusicinc.com
📧 info@fishmusicinc.com
```

### For rsp@noizylab.ca
```
--
Rob Plowman
NOIZYLAB • CPU Repair Services
$89 Flat Rate • Fast Turnaround

🌐 noizylab.ca
📧 rsp@noizylab.ca
```

### For help@noizylab.ca
```
--
NOIZYLAB Support
CPU Repair Services • $89 Flat Rate

🌐 noizylab.ca
📧 help@noizylab.ca
📞 Book: noizylab.ca/book
```

### For hello@noizylab.ca
```
--
NOIZYLAB
Professional CPU Repair Services

🌐 noizylab.ca
📧 hello@noizylab.ca
```

---

## 🎯 QUICK REFERENCE CARD

```
╔═══════════════════════════════════════════════════════════════╗
║                    ROB'S EMAIL EMPIRE                        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  MICROSOFT 365 PRIMARY                                        ║
║  ────────────────────                                         ║
║  rsplowman@outlook.com    → PRIMARY M365 LOGIN               ║
║                                                               ║
║  FISH MUSIC INC                                               ║
║  ─────────────                                                ║
║  rp@fishmusicinc.com      → Primary business                 ║
║  info@fishmusicinc.com    → General inquiries                ║
║                                                               ║
║  NOIZYLAB                                                     ║
║  ────────                                                     ║
║  rsp@noizylab.ca          → Owner direct                     ║
║  help@noizylab.ca         → Customer support                 ║
║  hello@noizylab.ca        → New customer contact             ║
║                                                               ║
║  ALL → rsplowman@outlook.com (ONE INBOX)                     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## ✅ VERIFICATION CHECKLIST

After setup, test each:

```
□ Send test TO rsplowman@outlook.com → Arrives in inbox?
□ Send test TO rp@fishmusicinc.com → Arrives in Outlook inbox?
□ Send test TO info@fishmusicinc.com → Arrives in Outlook inbox?
□ Send test TO rsp@noizylab.ca → Arrives in Outlook inbox?
□ Send test TO help@noizylab.ca → Arrives in Outlook inbox?
□ Send test TO hello@noizylab.ca → Arrives in Outlook inbox?
□ Reply FROM rp@ → Shows correct sender?
□ Reply FROM info@ → Shows correct sender?
□ Reply FROM rsp@ → Shows correct sender?
□ Reply FROM help@ → Shows correct sender?
□ Reply FROM hello@ → Shows correct sender?
□ Folders/Rules applied automatically?
□ Signatures showing correctly?
```

---

## 🚀 DONE = EMAIL EMPIRE COMPLETE

One inbox. Six identities. Microsoft 365 primary. Zero friction.

**GORUNFREE ✓**
