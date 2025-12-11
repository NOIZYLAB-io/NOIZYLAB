# NOIZY.AI v1 – PRODUCT SPEC (BATTLE SPEC)

> BECOME THE PLACE WHERE AN ARTIST CAN SAY:
> "THIS IS MY CATALOG. THESE ARE MY PEOPLE. THESE ARE OUR SPLITS."

---

## CREED

> NOIZY.AI REMEMBERS EVERY NAME, FOLLOWS EVERY PLAY IT CAN FIND, AND PUSHES EVERY DOLLAR IT CAN ROUTE BACK TO THE PEOPLE WHO MADE THE SOUND.

---

## THE NOIZY.AI STACK

| Component | Name | What It Does | v1 Status |
|-----------|------|--------------|-----------|
| 🧠 | **NOIZY.BRAIN** | The credits graph – who did what on every track | ✅ CORE |
| 🧬 | **NOIZY.TAG** | Portable rights DNA file – travels with the music | ✅ CORE |
| 📡 | **NOIZY.RADAR** | Usage detection & logs | 🟡 BABY VERSION |
| 💸 | **NOIZY.FLOW** | Money routing + statements | 🔴 LATER |

**v1 = BRAIN + TAG, baby RADAR, manual FLOW.**

---

## v1 GOAL (SUPER CLEAR)

**Truthful credits, in one place, in a machine-readable format.**

No global ingestion. No giant deals.
Just: YOUR catalog. YOUR people. YOUR splits. LOCKED.

---

## v1 USER FLOW – ARTIST SIDE

### STEP 1: SIGN UP / CREATE PROFILE

Artist creates a NOIZY.AI profile:

```
- Name (legal + display)
- Aliases (stage names, producer tags)
- Email
- Primary roles: [writer, producer, performer, engineer, etc.]
- Optional: PRO affiliation, publisher info
```

### STEP 2: ADD WORKS (TRACKS)

For each track:

```
- Title
- Version (Album Mix, Radio Edit, etc.)
- Year
- ISRC (if available)
- Album / Project (optional)
```

**Add contributors:**

```
For each person on the track:
- Name
- Role(s): [composer, lyricist, producer, performer, engineer, mixer, etc.]
- Email / handle (optional)
- Their NOIZY.AI ID (if they have one)
```

### STEP 3: DEFINE SPLITS

**Two buckets (v1):**

| Bucket | Who Gets Paid |
|--------|---------------|
| **COMPOSITION** | Songwriters, lyricists, composers |
| **MASTER** | Recording owners (artist, label, producer points) |

**Rules:**
- Must add up to 100%
- Visual guardrails ("You have 15% unassigned")
- Lock when confirmed by all parties (future)

**Future buckets (v2+):**
- Producer points
- Sample clearance splits
- Neighboring rights

### STEP 4: EXPORT NOIZY.TAG

When a track is "locked":

**NOIZY.AI generates:**
- `.noizy.json` file with all credits + splits
- Human-readable summary (PDF or Markdown)
- CSV export for spreadsheet lovers

**Artist can:**
- Download and store with masters
- Send to distributors / labels / PROs
- Attach to uploads

### STEP 5: USAGE NOTIFICATIONS (BABY RADAR)

**v1 sources:**
- Manual inputs ("I got played on X radio")
- Artist's own platforms (YouTube channel, Bandcamp logs)
- Basic web mentions (future)

**What gets logged:**
```
- Date
- Track
- Where it was used (platform, show, etc.)
- Type: stream / download / broadcast / sync / live
- Value: $X or "exposure-only"
```

**Outcome:** Central log of "this song showed up here, here, here."

---

## v1 FEATURES SUMMARY

| Feature | Description | Priority |
|---------|-------------|----------|
| Artist Profile | Name, aliases, roles, contact | ✅ MUST |
| Track Entry | Title, year, ISRC, version | ✅ MUST |
| Contributor Management | Add people + roles | ✅ MUST |
| Split Calculator | Composition + Master splits | ✅ MUST |
| NOIZY.TAG Export | JSON file per track | ✅ MUST |
| Human-Readable Export | PDF/Markdown summary | ✅ MUST |
| Usage Log (Manual) | Track where music appears | 🟡 NICE |
| Collaborator Invites | Email contributors to confirm | 🟡 NICE |
| Dispute Resolution | Flag conflicts | 🔴 LATER |
| Payment Routing | Actually move money | 🔴 LATER |

---

## v1 DATA MODEL (SIMPLIFIED)

```
ARTIST
├── id
├── name
├── aliases[]
├── email
├── roles[]
└── works[]

WORK (TRACK)
├── id
├── title
├── version
├── year
├── isrc
├── contributors[]
│   ├── artist_id
│   ├── roles[]
│   └── confirmed: bool
├── splits
│   ├── composition[]
│   │   └── {artist_id, share}
│   └── master[]
│       └── {artist_id, share}
└── usages[]
    ├── date
    ├── platform
    ├── type
    └── value
```

---

## v1 TECH STACK (MINIMAL)

| Layer | Tool | Why |
|-------|------|-----|
| Data Store | Markdown files → SQLite/JSON | Start simple, scale later |
| Frontend | Static site / simple React | Artist dashboard |
| Backend | Cloudflare Workers / FastAPI | API for CRUD + export |
| Export | JSON + PDF generation | NOIZY.TAG files |
| Auth | Magic links / Passkeys | Simple, secure |

---

## SUCCESS METRICS (v1)

| Metric | Target |
|--------|--------|
| Artists with profiles | 10 |
| Tracks in NOIZY.BRAIN | 100 |
| NOIZY.TAGs generated | 50 |
| Paid Credit Cleanup clients | 3 |

---

## WHAT v1 IS NOT

- ❌ Global music database
- ❌ Streaming platform
- ❌ PRO replacement
- ❌ Payment processor
- ❌ Label services

**v1 IS:**
- ✅ Your catalog, organized
- ✅ Your credits, locked
- ✅ Your splits, documented
- ✅ Your future-proof file

---

```
NOIZY.AI v1
UNIVERSAL CREDIT. DIRECT REVENUE. ARTIST FIRST.
```


