# 🎯 ROB'S EMAIL EMPIRE - MASTER CONFIG
## 5 Emails. One Inbox. Zero Friction.

---

## THE 5 EMAILS

| # | Address | Domain | Purpose |
|---|---------|--------|---------|
| 1 | `rp@fishmusicinc.com` | Fish Music | PRIMARY - Your main |
| 2 | `info@fishmusicinc.com` | Fish Music | General inquiries |
| 3 | `rsp@noizylab.ca` | NOIZYLAB | Repair business |
| 4 | `help@noizylab.ca` | NOIZYLAB | Customer support |
| 5 | `hello@noizylab.ca` | NOIZYLAB | Friendly contact |

---

## 🔥 THE GOAL

```
ALL 5 EMAILS → rp@fishmusicinc.com inbox
SEND FROM → Any of the 5 addresses
ONE INBOX → Rules everything
```

---

## ⚡ STEP 1: ADD "SEND AS" ADDRESSES

**URL:** `https://mail.google.com/mail/u/0/#settings/accounts`

In **"Send mail as"** section, click **"Add another email address"** for each:

### Fish Music (Google Workspace - Same Domain)
```
✅ rp@fishmusicinc.com      → Already there (primary)
➕ info@fishmusicinc.com    → Add as alias
```

### NOIZYLAB (Different Domain - Needs SMTP)
```
➕ rsp@noizylab.ca
➕ help@noizylab.ca  
➕ hello@noizylab.ca
```

**For noizylab.ca addresses, use these SMTP settings:**
```
SMTP Server: smtp.gmail.com
Port: 587
Username: rsp@noizylab.ca (or your Google Workspace login)
Password: App Password (generate at myaccount.google.com)
TLS: Yes
```

---

## ⚡ STEP 2: FORWARDING SETUP

### For fishmusicinc.com emails:
**In Google Workspace Admin** (`admin.google.com`):
1. Users → Select user → Email aliases
2. Add `info@fishmusicinc.com` as alias to `rp@`
3. Done - same inbox automatically

### For noizylab.ca emails:
**Option A: Google Workspace Aliases** (if noizylab.ca is on Workspace)
- Add as aliases to main account

**Option B: Cloudflare Email Routing** (if using Cloudflare)
- Dashboard → Email → Email Routing
- Add routes:
```
rsp@noizylab.ca    → rp@fishmusicinc.com
help@noizylab.ca   → rp@fishmusicinc.com
hello@noizylab.ca  → rp@fishmusicinc.com
```

---

## ⚡ STEP 3: GMAIL FILTERS (Auto-Label)

**URL:** `https://mail.google.com/mail/u/0/#settings/filters`

Create these filters:

### Filter 1: Fish Music
```
Matches: to:(info@fishmusicinc.com)
Do this: Apply label "🐟 Fish Music", Never send to Spam
```

### Filter 2: NOIZYLAB Support
```
Matches: to:(help@noizylab.ca)
Do this: Apply label "🔧 NOIZYLAB Support", Star it, Never send to Spam
```

### Filter 3: NOIZYLAB General
```
Matches: to:(hello@noizylab.ca OR rsp@noizylab.ca)
Do this: Apply label "🔧 NOIZYLAB", Never send to Spam
```

---

## ⚡ STEP 4: PROFESSIONAL SIGNATURES

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
║  ALL → rp@fishmusicinc.com (ONE INBOX)                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## ✅ VERIFICATION CHECKLIST

After setup, test each:

```
□ Send test TO info@fishmusicinc.com → Arrives in rp@ inbox?
□ Send test TO rsp@noizylab.ca → Arrives in rp@ inbox?
□ Send test TO help@noizylab.ca → Arrives in rp@ inbox?
□ Send test TO hello@noizylab.ca → Arrives in rp@ inbox?
□ Reply FROM info@ → Shows correct sender?
□ Reply FROM rsp@ → Shows correct sender?
□ Reply FROM help@ → Shows correct sender?
□ Reply FROM hello@ → Shows correct sender?
□ Labels applied automatically?
□ Signatures showing correctly?
```

---

## 🚀 DONE = EMAIL EMPIRE COMPLETE

One inbox. Five identities. Zero friction.

**GORUNFREE ✓**
