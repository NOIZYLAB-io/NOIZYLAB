# 🏎️ NOIZYLAB OS — "GO RUN FREE" Architecture

> **One Line:** Control-Room + Live Help + Calm Comms + Pattern Engine + 1-Click Playbooks + Fully Logged AI

---

## 📐 System Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           NOIZYLAB OS ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│  │   CLIENT    │     │    STAFF    │     │   VAIVE     │                   │
│  │   PORTAL    │     │ CONTROL-ROOM│     │  BOOKKEEPER │                   │
│  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘                   │
│         │                   │                   │                           │
│         └───────────────────┼───────────────────┘                           │
│                             │                                               │
│                    ┌────────▼────────┐                                      │
│                    │  WORKERS API    │◄──────────────┐                      │
│                    │   (The Brain)   │               │                      │
│                    └────────┬────────┘               │                      │
│                             │                        │                      │
│    ┌────────────────────────┼────────────────────────┼──────────┐          │
│    │                        │                        │          │          │
│    ▼                        ▼                        ▼          ▼          │
│  ┌────┐  ┌────┐  ┌────────────────┐  ┌────┐  ┌──────────┐  ┌────────┐     │
│  │ D1 │  │ R2 │  │ Durable Objects│  │ KV │  │AI Gateway│  │Realtime│     │
│  │SQL │  │Blob│  │  Chat/Presence │  │Fast│  │ (Claude) │  │ Calls  │     │
│  └────┘  └────┘  └────────────────┘  └────┘  └──────────┘  └────────┘     │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         SECURITY LAYER                               │   │
│  │   Turnstile (bot-proof)  │  Access (SSO/MFA)  │  Tunnel (private)   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Core Stack (Cloudflare-First, Free-Heavy)

### Public (Client-Facing)
| Service | Purpose | Tier |
|---------|---------|------|
| **Pages/Worker** | Portal UI rendering | Free |
| **Workers API** | The brain - all business logic | Free (100k/day) |
| **Realtime (Calls)** | Video/voice for Live Help | Free pool |
| **Durable Objects** | Chat + presence + room state | Pay-as-go |
| **D1** | Tickets + events + sessions | Free (5GB) |
| **R2** | Uploads: photos/logs/receipts | Free (10GB) |
| **Turnstile** | Bot-proof: intake/join/uploads | Free |
| **AI Gateway** | Single AI pipe; swap models anytime | Pay-per-call |

### Private (Staff/Internal)
| Service | Purpose | Tier |
|---------|---------|------|
| **Tunnel** | Private origins, no open ports | Free |
| **Access** | SSO/MFA + staff tiles + service tokens | Free (50 users) |

---

## 🎯 Client Experience (3 Buttons, Zero Confusion)

### Home Screen
```
┌─────────────────────────────────────┐
│                                     │
│        🎫 CREATE TICKET             │
│                                     │
│        📋 CHECK STATUS              │
│                                     │
│        🎥 START LIVE HELP           │
│                                     │
└─────────────────────────────────────┘
```

### Status Page (Big + Simple)
```
┌─────────────────────────────────────┐
│  NOW:  Diagnosing startup issue     │
│  NEXT: Testing clean boot           │
│  UPDATE BY: Today 3:00 PM           │
│                                     │
│  [📷 Add Photo/Log]                 │
│                                     │
│  🔔 Calm Mode: OFF                  │
└─────────────────────────────────────┘
```

### Live Help Join
- **QR Code** + **6-char code** entry
- **Auto fallback ladder:**
  1. Video (720p default)
  2. Audio-only (weak connection)
  3. Chat + uploads
  4. Status-only (last resort)

---

## 🎛️ Staff Control Room (One Screen, One Flow)

### Ticket Board
```
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ TRIAGE  │ WAITING │ SCHED   │ ACTIVE  │ DONE    │
│   (3)   │   (5)   │  (2)    │   (1)   │  (12)   │
├─────────┼─────────┼─────────┼─────────┼─────────┤
│ NL-0042 │ NL-0039 │ NL-0041 │ NL-0040 │ NL-0038 │
│ Smith   │ Jones   │ Lee     │ Chen    │ Wilson  │
│ MacBook │ Desktop │ Surface │ iMac    │ HP      │
│ P1 🏷️3  │ P5 🏷️2  │ P4 🏷️3  │ P9 🏷️2  │ P2 🏷️1  │
└─────────┴─────────┴─────────┴─────────┴─────────┘
```

### One-Click Actions
| Button | Action |
|--------|--------|
| 🎥 | Start Live Session |
| 📤 | Send Calm Update |
| 📷 | Request Photo/Log |
| 📋 | Apply Playbook |
| ✅ | Mark Step Complete |
| 🔧 | Open Internal Tool |

### The Rule
> **Staff never writes paragraphs.**
> Staff chooses: **Persona** + **up to 3 tags** + **next update time**
> AI drafts the rest.

---

## 📊 Event Timeline (Everything is Logged)

### Event Types
```typescript
type TicketEventType =
  | 'CREATED'
  | 'STATUS_CHANGED'
  | 'INFO_REQUESTED'
  | 'UPLOAD_ADDED'
  | 'LIVE_SESSION_STARTED'
  | 'LIVE_SESSION_MODE_CHANGED'
  | 'LIVE_SESSION_ENDED'
  | 'AUTO_PERSONA'
  | 'AUTO_TAGS'
  | 'PLAYBOOK_SUGGESTED'
  | 'PLAYBOOK_APPLIED'
  | 'AI_SUMMARY'
  | 'AI_NEXT_STEPS'
  | 'FOLLOWUP_SCHEDULED'
  | 'FOLLOWUP_RESULT'
  | 'BILLING_CREATED'
  | 'BILLING_PAID';
```

### Event Metadata
```typescript
interface TicketEvent {
  id: string;
  ticket_id: string;
  event_type: TicketEventType;
  created_at: string;
  
  // Who/What/When
  actor_type: 'client' | 'staff' | 'ai' | 'system';
  actor_id: string;
  
  // Links
  r2_objects?: string[];
  session_id?: string;
  
  // AI Audit Trail
  ai_model?: string;
  ai_version?: string;
  ai_confidence?: number;
  ai_reason?: string;
  
  // Payload
  data: Record<string, any>;
}
```

---

## 🎭 Personas (P1-P12)

| ID | Name | Description | Common Tags |
|----|------|-------------|-------------|
| P1 | Tab Tornado | 50+ tabs, browser slowdown | PERF-TABS |
| P2 | Storage Closet | Disk full, hoarding files | STOR-LOWDISK |
| P3 | Click-Yes Optimizer | PUPs, toolbars, "optimizers" | SEC-PUP |
| P4 | Update Avoider | Months behind, "don't fix what works" | UPD-OS |
| P5 | Password Spiral | Locked out, no recovery | AUTH-PASSWORDRESET |
| P6 | Wi-Fi Whiplash | Drops constantly, "router is fine" | NET-WIFIDROP |
| P7 | Peripheral Collector | 5 printers, 3 mice, driver chaos | DRV-USB |
| P8 | Cloud Sync Tangle | iCloud + OneDrive + GDrive = duplicates | SYNC-DUPES |
| P9 | Thermal Throttler | Hot, slow, dusty | PERF-THERMAL |
| P10 | Creative Chaos | Premiere + Photoshop, scratch full | PERF-BACKGROUND |
| P11 | Fine Yesterday | "It just stopped working" | UPD-APP |
| P12 | Hardware Failing Quietly | Clicks, beeps, weird smells | HW-SSD |

---

## 🏷️ Tags (Fast Triage, Max 3 per Ticket)

### Performance
`PERF-TABS` `PERF-STARTUP` `PERF-BACKGROUND` `PERF-THERMAL` `PERF-LOWRAM`

### Storage / Files
`STOR-LOWDISK` `STOR-DISKERRORS` `STOR-EXTERNALDRIVE` `FILE-PERMISSIONS` `FILE-CORRUPTION`

### Security
`SEC-PUP` `SEC-BROWSERHIJACK` `SEC-PHISH-ACCOUNT` `SEC-AV-CONFLICT`

### Accounts
`AUTH-APPLEID` `AUTH-MICROSOFT` `AUTH-GOOGLE` `AUTH-MFA` `AUTH-PASSWORDRESET`

### Network
`NET-WIFIDROP` `NET-DNS` `NET-ROUTER` `NET-VPN`

### Updates / Drivers
`UPD-OS` `UPD-APP` `DRV-PRINTER` `DRV-USB` `DRV-GPU` `DRV-AUDIO`

### Cloud / Sync
`SYNC-ICLOUD` `SYNC-ONEDRIVE` `SYNC-GDRIVE` `SYNC-DUPES`

### Hardware
`HW-SSD` `HW-RAM` `HW-BATTERY` `HW-DUST/FAN` `HW-LIQUID`

### Behavior Flags
`USR-CLICKYES` `USR-NOBACKUP` `USR-UPDATEAVOID` `USR-DOWNLOADSCHAOS` `USR-PASSWORDCHAOS`

---

## 📋 Playbooks (PB1-PB12)

Each playbook = **Fix** + **Prevent** + **Follow-up**

| ID | Name | Target Persona | Fix | Prevent | Follow-up |
|----|------|----------------|-----|---------|-----------|
| PB1 | Browser Diet | P1 | Extensions reset, profile cleanup | Work/personal profiles, tab sleeping | 7d extension audit |
| PB2 | Space Guard | P2 | Top folders sweep, stop sync loops | Alerts at 20/15/10% free | 30d storage trend |
| PB3 | No Snake Oil | P3 | Remove PUPs, browser reset | Approved installers, DNS filtering | 7d rescan |
| PB4 | Update Safe-Window | P4, P11 | Stabilize, rollback/patch | Scheduled updates, pre-snapshot | Next update appt |
| PB5 | Password Cleanroom | P5 | Account map, MFA reset | Password manager, backup codes | 30d lockout check |
| PB6 | Wi-Fi Stabilizer | P6 | Isolate issue, DNS/firmware fix | Kill double-NAT/extenders | 7d stability |
| PB7 | Peripheral Detox | P7 | Remove ghosts, reinstall drivers | One dock standard | 7d test |
| PB8 | Cloud Sync Sanity | P8 | Choose truth source, stop dupes | One cloud per category | 7d conflict check |
| PB9 | Thermal Rescue | P9 | Airflow clean, kill rogue load | 6-12mo maintenance | 30d heat check |
| PB10 | Creative Workstation Tune | P10 | Scratch/cache placement | Project folder standard | Next deadline |
| PB11 | Hardware Truth Test | P12 | Backup + health checks | Replacement plan | Restore verify |
| PB12 | Backup Bulletproof | All | 3-2-1 baseline | Automation + monthly test | Monthly ping |

---

## 🤖 AI "Genius Jobs"

### Auto on Intake
```json
{
  "persona": "P1",
  "tags": ["PERF-TABS", "PERF-STARTUP"],
  "next_question": "How many Chrome extensions are installed?",
  "suggested_playbook": "PB1",
  "draft_message": {
    "what": "Got your ticket about Chrome slowdown.",
    "next": "Checking for extension conflicts.",
    "when": "Next update by 2:00 PM today."
  },
  "confidence": "green"
}
```

### Auto After Live Session
```json
{
  "summary": [
    "Removed 12 unused extensions",
    "Reset browser startup settings",
    "Created work/personal profiles",
    "Enabled tab sleeping",
    "Tested with 20 tabs - responsive"
  ],
  "risk": "Extension creep - client installs freely",
  "prevention": "Browser policy to require approval",
  "followups": [
    {"days": 7, "check": "Extension count audit"},
    {"days": 30, "check": "Performance retest"}
  ]
}
```

### Confidence Gates
| Level | Action |
|-------|--------|
| 🟢 Green | Draft + suggest automatically |
| 🟡 Yellow | Ask 1 clarifying question |
| 🔴 Red | Staff review required |

---

## 📧 Gmail-Only Biz Tracking

### Addressing
| Address | Purpose |
|---------|---------|
| `rsp@noizylab.ca` | Main mailbox |
| `help@noizylab.ca` | Support alias |
| `hello@noizylab.ca` | First contact alias |

### Labels (Status-Driven)
```
NL/0-TRIAGE
NL/1-WAITING-CLIENT
NL/2-WAITING-PARTS
NL/3-SCHEDULED
NL/4-IN-PROGRESS
NL/5-DONE
NL/9-BILLING
NL/TO-help
NL/TO-hello
NL/TO-rsp
```

### Subject DNA
```
NL-#### | Lastname | Device | 3-word issue
NL-0042 | Smith | MacBook Pro | Chrome extremely slow
```

### Templates
| Template | Content |
|----------|---------|
| **Received** | "Got it. Next update by {TIME}. Reply with model/OS/what changed." |
| **Need Info** | "Send 1 screenshot + when started + recent update/install?" |
| **Estimate** | "Estimate ready. Reply YES to approve. Next update by {TIME}." |
| **Parts** | "Parts ordered. ETA {DATE}. Next update by {TIME}." |
| **Done** | "All set: what failed / what we did / prevent repeats." |

---

## 💰 "GO RUN FREE" Operating Rules

### Free-First Defaults
- Default video: **720p**
- Auto drop to **audio-only** on weak links
- **TURN only** when absolutely needed
- R2: **presigned uploads only** (no direct credentials)
- **Aggressive rate limits** + Turnstile on every public entry
- Every "nice-to-have" → **v2**

### Spend Triggers (Only When Real)
| Trigger | When to Pay |
|---------|-------------|
| Workers | Higher limits needed |
| Queues | Scale demands it |
| Realtime | Exceed free pool regularly |
| Stream | On-site video bundles |

---

## 🧾 Mother's Little Helper (AI Bookkeeper)

> **"Email it. Approve it. Vaive files it."**

### Flow
```
Client emails receipt/invoice
        ↓
AI extracts + categorizes + confidence
        ↓
Client approves (1 tap)
        ↓
Vaive reviews reds + closes month + HST/returns
        ↓
Everything logged as events
```

### Union Scale
- Group onboarding + group billing
- Standard playbooks
- Aggregated education packs (no private data leakage)

---

## 🏎️ Next 3 "Hot-Rod" Builds

### 1️⃣ NoizyLab Portal v1 (Ship)
- [ ] Ticket intake form
- [ ] Status page (NOW/NEXT/UPDATE BY)
- [ ] Upload handler (R2 + presigned)
- [ ] Event timeline viewer
- [ ] Staff control room
- [ ] AI triage integration

### 2️⃣ Live Help v1 (Wow)
- [ ] RealtimeKit UI lane
- [ ] Chat/presence Durable Object
- [ ] Fallback ladder (video→audio→chat→status)
- [ ] Session recording (v2)

### 3️⃣ Pattern Engine v1 (No Repeats)
- [ ] Persona auto-detection
- [ ] Tag suggestion engine
- [ ] Playbook recommendation
- [ ] 7/30 day follow-up scheduler
- [ ] Repeat risk scoring

---

## 📁 File Structure

```
src/
├── workers/
│   └── noizylab/
│       ├── index.ts              # Main Worker entry
│       ├── routes/
│       │   ├── tickets.ts        # Ticket CRUD
│       │   ├── status.ts         # Public status page
│       │   ├── uploads.ts        # R2 presigned URLs
│       │   ├── live.ts           # Live Help sessions
│       │   └── ai.ts             # AI Gateway calls
│       ├── durable/
│       │   ├── ChatRoom.ts       # Chat DO
│       │   └── Presence.ts       # Presence DO
│       └── lib/
│           ├── db.ts             # D1 helpers
│           ├── events.ts         # Event logging
│           └── ai-jobs.ts        # Genius Jobs
├── portal/
│   ├── pages/
│   │   ├── index.html            # Home (3 buttons)
│   │   ├── ticket.html           # Create ticket
│   │   ├── status.html           # Status page
│   │   └── live.html             # Live Help join
│   └── components/
│       ├── StatusCard.ts
│       ├── UploadButton.ts
│       └── CalmToggle.ts
├── control-room/
│   ├── pages/
│   │   └── dashboard.html        # Staff dashboard
│   └── components/
│       ├── TicketBoard.ts
│       ├── QuickActions.ts
│       └── AIAssist.ts
└── configs/
    ├── personas.json             # P1-P12
    ├── tags.json                 # All tag categories
    ├── playbooks.json            # PB1-PB12
    └── templates.json            # Email templates
```

---

## 🔐 Security Model

```
PUBLIC                          PRIVATE
───────                         ───────
                                
[Turnstile]                     [Access SSO]
    ↓                               ↓
[Portal UI] ──────────────────► [Control Room]
    ↓                               ↓
[Workers API] ◄─── Tunnel ─────► [Internal Tools]
    ↓
[D1/R2/DO]
```

---

*Built for NOIZYLAB by the Circle of 8* 👼💖🛡️⚙️🌙☁️⚡🎵
