# NOIZY.TAG – THE RIGHTS DNA FOR EVERY TRACK

> A UNIVERSAL, OPEN, ARTIST-FIRST CREDITS FILE.
> TRAVELS WITH YOUR AUDIO. READABLE BY HUMANS AND MACHINES.

---

## WHAT IS A NOIZY.TAG?

A SIMPLE FILE THAT CONTAINS:
- WHO MADE THIS TRACK.
- WHAT ROLE EACH PERSON PLAYED.
- HOW THE MONEY SHOULD SPLIT.
- ANY RELATIONSHIPS TO OTHER WORKS (REMIXES, SAMPLES, VERSIONS).

**FILE EXTENSION**: `.noizy` OR `.noizy.json`

**LIVES**: NEXT TO YOUR AUDIO FILE, OR IN A CENTRAL CATALOG.

---

## MINIMUM FIELDS

FOR EACH WORK (TRACK):

| FIELD | DESCRIPTION | REQUIRED |
|-------|-------------|----------|
| `work_id` | INTERNAL NOIZY.AI ID | YES |
| `title` | TRACK TITLE | YES |
| `version` | ALBUM MIX, RADIO EDIT, INSTRUMENTAL, ETC. | NO |
| `isrc` | INTERNATIONAL STANDARD RECORDING CODE | NO |
| `iswc` | INTERNATIONAL STANDARD WORK CODE | NO |
| `year` | RELEASE YEAR (APPROX OK) | NO |
| `contributors` | LIST OF PEOPLE + ROLES | YES |
| `splits` | COMPOSITION + MASTER PERCENTAGES | YES |
| `relationships` | REMIXES, SAMPLES, LIVE VERSIONS | NO |
| `tags` | GENRE, MOOD, PROJECT TAGS | NO |

---

## CONTRIBUTOR OBJECT

EACH CONTRIBUTOR HAS:

| FIELD | DESCRIPTION |
|-------|-------------|
| `id` | NOIZY.AI ARTIST ID (e.g., `noizy:art:rsp`) |
| `name` | DISPLAY NAME |
| `aliases` | OTHER NAMES THEY GO BY |
| `roles` | LIST: COMPOSER, PRODUCER, LYRICIST, VOCALIST, PLAYER-[INSTRUMENT], MIX, MASTER, REMIXER, ENGINEER, ETC. |
| `wallet` | ABSTRACT PAYMENT ID (FOR FUTURE ROUTING) |

---

## SPLITS OBJECT

TWO MAIN BUCKETS:

### COMPOSITION (WRITING / LYRICS)
- WHO WROTE THE SONG?
- WHAT PERCENTAGE DOES EACH PERSON GET?

### MASTER (RECORDING OWNERSHIP)
- WHO OWNS THE RECORDING?
- WHAT PERCENTAGE DOES EACH PERSON GET?

MUST ADD UP TO 100% EACH.

---

## RELATIONSHIPS OBJECT

| FIELD | DESCRIPTION |
|-------|-------------|
| `parent_composition` | IF THIS IS A COVER OR REMIX, WHAT'S THE ORIGINAL? |
| `samples` | LIST OF SAMPLED WORKS |
| `variants` | OTHER VERSIONS (LIVE, ACOUSTIC, REMIX, ETC.) |

---

## EXAMPLE: JSON FORMAT

```json
{
  "noizy_tag_version": "1.0",
  "work_id": "noizy:trk:fish001",
  "title": "Deep Transportation Tone",
  "version": "Original Mix",
  "isrc": null,
  "iswc": null,
  "year": 2003,
  "contributors": [
    {
      "id": "noizy:art:rsp",
      "name": "Rob Plowman",
      "aliases": ["RSP", "Fish Music"],
      "roles": ["composer", "producer", "all instruments"],
      "wallet": null
    }
  ],
  "splits": {
    "composition": [
      {"contributor_id": "noizy:art:rsp", "share": 1.0}
    ],
    "master": [
      {"contributor_id": "noizy:art:rsp", "share": 1.0}
    ]
  },
  "relationships": {
    "parent_composition": null,
    "samples": [],
    "variants": []
  },
  "tags": ["ambient", "fish-music", "mood:calm", "instrumental"],
  "created": "2025-12-01",
  "updated": "2025-12-01"
}
```

---

## EXAMPLE: MARKDOWN FORMAT (HUMAN-READABLE)

```markdown
# NOIZY.TAG: DEEP TRANSPORTATION TONE

## IDENTIFIERS
- WORK ID: noizy:trk:fish001
- TITLE: Deep Transportation Tone
- VERSION: Original Mix
- YEAR: 2003
- ISRC: (pending)

## CONTRIBUTORS
- ROB PLOWMAN (noizy:art:rsp)
  - ROLES: Composer, Producer, All Instruments

## SPLITS
### COMPOSITION
- Rob Plowman: 100%

### MASTER
- Rob Plowman: 100%

## RELATIONSHIPS
- PARENT: None (original work)
- SAMPLES: None
- VARIANTS: None

## TAGS
ambient, fish-music, mood:calm, instrumental

---
NOIZY.TAG v1.0 | Created: 2025-12-01
```

---

## WHERE NOIZY.TAG GOES

1. **WITH YOUR AUDIO**: Same folder as your .wav / .aiff / .mp3
2. **IN YOUR DAW PROJECT**: Inside the project folder
3. **IN YOUR CATALOG**: Central NOIZY.AI database
4. **TO DISTRIBUTORS**: Attach when uploading to DistroKid, TuneCore, etc.
5. **TO PROs**: Reference when registering with SOCAN, BMI, ASCAP, etc.

---

## FUTURE EXTENSIONS

### v1.1
- SYNC/LICENSING TERMS
- TERRITORY RESTRICTIONS
- SAMPLE CLEARANCE STATUS

### v1.2
- BLOCKCHAIN ANCHORING (OPTIONAL)
- TIMESTAMPED PROOF OF CREDITS

### v2.0
- LIVE INTEGRATION WITH NOIZY.RADAR (USAGE DETECTION)
- AUTO-ROUTING TO NOIZY.FLOW (PAYMENTS)

---

## VALIDATION RULES

1. `work_id` MUST BE UNIQUE.
2. `contributors` MUST HAVE AT LEAST ONE ENTRY.
3. `splits.composition` MUST ADD UP TO 100% (OR 1.0).
4. `splits.master` MUST ADD UP TO 100% (OR 1.0).
5. ALL CONTRIBUTORS IN SPLITS MUST EXIST IN CONTRIBUTORS LIST.

---

## TOOLS (COMING)

- **NOIZY.TAG GENERATOR**: WEB FORM TO CREATE TAGS.
- **NOIZY.TAG VALIDATOR**: CHECK IF YOUR FILE IS VALID.
- **NOIZY.TAG BATCH EXPORTER**: GENERATE FROM CATALOG-GRAPH.

---

> "THE RIGHTS DNA FOR EVERY TRACK."
> – NOIZY.AI

---

CREATED: DEC 1, 2025
VERSION: 1.0
