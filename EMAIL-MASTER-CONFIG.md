# 🎯 ROB'S EMAIL EMPIRE - MASTER CONFIG (M365 HUB)
## Primary Account Hierarchy - Microsoft 365 Central Hub

---

## PRIMARY ACCOUNT HIERARCHY

| Priority | Email | Service | Purpose |
|----------|-------|---------|---------|
| 🥇 1 | `rsplowman@outlook.com` | **Microsoft 365** | PRIMARY LOGIN - All MS services |
| 🥈 2 | `rsplowman@icloud.com` | Apple/iCloud | Apple ecosystem, Passkeys |
| 🥉 3 | `rp@fishmusicinc.com` | Fish Music | Primary business email |
| 4 | `rsp@noizylab.ca` | NOIZYLAB | Business/Git identity |
| 5 | `info@fishmusicinc.com` | Fish Music | General inquiries |
| 6 | `help@noizylab.ca` | NOIZYLAB | Customer support |
| 7 | `hello@noizylab.ca` | NOIZYLAB | Friendly contact |

---

## 🔥 THE GOAL

```
ALL EMAILS → rsplowman@outlook.com (M365 HUB)
PRIMARY LOGIN → Microsoft 365 services
UNIFIED HUB → All business systems
CENTRAL AUTH → Single sign-on everywhere
```

---

## ⚡ STEP 1: MICROSOFT 365 HUB SETUP

**Primary Account:** `rsplowman@outlook.com` (Microsoft 365)

**URL:** `https://outlook.office.com`

### M365 Hub Configuration
```
Primary Account: rsplowman@outlook.com
Service: Microsoft 365 (Office 365)
SMTP: smtp.office365.com:587
IMAP: outlook.office365.com:993
Auth: Modern OAuth 2.0
```

### Forwarding Setup - All to M365 Hub
```
rp@fishmusicinc.com    → rsplowman@outlook.com
info@fishmusicinc.com  → rsplowman@outlook.com
rsp@noizylab.ca        → rsplowman@outlook.com
help@noizylab.ca       → rsplowman@outlook.com
hello@noizylab.ca      → rsplowman@outlook.com
```

---

## ⚡ STEP 2: SPF/DKIM/DMARC CONFIGURATION

### Microsoft 365 SPF Record
```
v=spf1 include:spf.protection.outlook.com -all
```

### Cloudflare Email Routing
**For noizylab.ca and fishmusicinc.com:**
- Dashboard → Email → Email Routing
- Add routes to rsplowman@outlook.com

### DKIM Setup
- Microsoft 365 Admin → Exchange → Mail flow → DKIM
- Enable for all domains

### DMARC Policy
```
v=DMARC1; p=quarantine; rua=mailto:rsplowman@outlook.com
```

---

## ⚡ STEP 3: OUTLOOK FILTERS (Auto-Label)

**URL:** `https://outlook.office.com` → Settings → Mail → Rules

Create these filters:

### Filter 1: Microsoft 365 Primary
```
Matches: to:(rsplowman@outlook.com)
Do this: Apply category "🔵 M365 Primary", Pin to top
```

### Filter 2: Fish Music
```
Matches: to:(rp@fishmusicinc.com OR info@fishmusicinc.com)
Do this: Apply category "🐟 Fish Music", Move to Fish Music folder
```

### Filter 3: NOIZYLAB Support
```
Matches: to:(help@noizylab.ca)
Do this: Apply category "🔧 NOIZYLAB Support", Flag, Move to NOIZYLAB Support
```

### Filter 4: NOIZYLAB General
```
Matches: to:(hello@noizylab.ca OR rsp@noizylab.ca)
Do this: Apply category "🔧 NOIZYLAB", Move to NOIZYLAB folder
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
