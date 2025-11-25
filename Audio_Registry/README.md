# THE LIBRARIAN - Audio Canon Registry

```
███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗
████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗
██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝
██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗
██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝
╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝
```

**Fish Music Inc. / MissionControl96 / NOIZYLAB**

---

## Overview

THE LIBRARIAN is a comprehensive registry and catalog system for audio production tools:
- **DAWs** (Digital Audio Workstations)
- **Plugins** (Effects, Processors, Utilities)
- **Instruments** (Synths, Samplers, Orchestral Libraries)
- **AI Models** (Repair, Enhancement, Separation)

Designed for integration with **MissionControl96** dashboards and third-party AI assistants.

---

## Directory Structure

```
Audio_Registry/
├── data/
│   ├── catalog.yaml      # Master catalog (75+ items)
│   └── index.json        # Dashboard-ready JSON export
├── manifests/
│   ├── DAW/              # DAW-specific manifests
│   ├── Plugins/          # Plugin category manifests
│   ├── Instruments/      # Instrument library manifests
│   ├── AI_Models/        # AI model registry
│   └── Repair_Tools/     # Audio/video repair tools & workflows
├── checksums/
│   └── *.md5             # File integrity checksums
└── tools/
    ├── audiocat          # Main CLI tool
    ├── ai_host_guide.py  # Interactive repair workflow assistant
    ├── audit/            # Catalog audit scripts
    ├── ingest/           # Item import scripts
    └── export/           # Export utilities
```

---

## Quick Start

### Initialize Registry
```bash
./tools/audiocat init --root "./Audio_Registry"
```

### Add an Item
```bash
./tools/audiocat add \
  --name "Serum" \
  --type plugin \
  --category synth \
  --developer "Xfer Records" \
  --format VST3 AU \
  --os macOS Windows \
  --releaseYear 2014 \
  --tags wavetable modulation
```

### Run Audit
```bash
./tools/audiocat audit
# or
python3 tools/audit/run_audit.py --json audit_report.json
```

### Export to JSON
```bash
./tools/audiocat export --output index.json
# or
python3 tools/export/export_index.py --format all
```

### AI Host Guide (Interactive)
```bash
python3 tools/ai_host_guide.py --interactive

# Or start a specific workflow
python3 tools/ai_host_guide.py --workflow dialogue_repair
```

---

## Catalog Schema

### Required Fields
| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Product name |
| `type` | enum | `daw`, `plugin`, `instrument`, `ai_model` |
| `category` | enum | Category (synth, eq, reverb, etc.) |
| `developer` | string | Developer/company name |

### Optional Fields
| Field | Type | Description |
|-------|------|-------------|
| `itemId` | string | Auto-generated unique ID |
| `format` | array | `[VST2, VST3, AU, AAX, CLAP, Standalone]` |
| `os` | array | `[macOS, Windows, Linux]` |
| `releaseYear` | number | Year of initial release |
| `status` | enum | `active`, `legacy`, `discontinued` |
| `tags` | array | Descriptive tags |
| `urls` | object | `{home: string, docs: string}` |
| `notes` | string | Additional notes |

---

## Categories

### DAWs
- Ableton Live, Logic Pro, Pro Tools, Cubase, Studio One, FL Studio, Bitwig, Reaper, Reason, Luna, Digital Performer, Nuendo

### Synths & Instruments
- **Wavetable**: Serum, Vital, Pigments, Phase Plant
- **Analog Modeling**: Diva, Repro, V Collection, TAL-U-NO-LX
- **Hybrid**: Omnisphere, Zebra, Massive X
- **Samplers**: Kontakt, Falcon, HALion
- **Orchestral**: BBC Symphony, Berlin Series, Hollywood Orchestra, Synchron

### Effects
- **EQ**: FabFilter Pro-Q, Equilibrium, SlickEQ
- **Compressors**: Pro-C, Kotelnikov, 1176, LA-2A
- **Reverbs**: Valhalla Room/VintageVerb, Pro-R, Altiverb
- **Delays**: EchoBoy, Valhalla Delay, Timeless
- **Saturation**: Decapitator, Saturn, Tape

### Repair & AI Tools
- **Suites**: iZotope RX, SpectraLayers, Acoustica
- **AI Models**: LALAL.AI, Demucs, Spleeter, Whisper
- **Video**: Topaz Video AI, DaVinci Resolve Neural Engine

---

## AI Host Guide

Interactive assistant for audio/video repair workflows:

```bash
python3 tools/ai_host_guide.py -i
```

### Available Workflows
| Workflow | Description |
|----------|-------------|
| `noise_reduction` | Remove background noise, hiss, hum |
| `dialogue_repair` | Complete dialogue cleanup chain |
| `stem_separation` | AI-powered source separation |
| `video_restoration` | Video upscaling and repair |
| `clipping_repair` | Fix digital/analog clipping |
| `reverb_removal` | Remove unwanted room sound |

### Example Session
```
ai-host> list
ai-host> start dialogue_repair
ai-host> next
ai-host> next
ai-host> recommend noise
ai-host> api lalal_ai
ai-host> export stem_separation workflow.json
```

---

## Integration

### MissionControl96
`index.json` provides dashboard-ready data with:
- Item counts by type/category/developer
- Filter options
- Health metrics
- Developer constellations

### Home Assistant
Expose sensors via the audit tool:
```yaml
sensor.audio_catalog_total_items
sensor.audio_catalog_active_count
sensor.audio_catalog_health_score
```

### Node-RED
Trigger flows for:
- Monthly audits
- Timeline renders
- Snapshot archival

---

## Workflows

### Monthly Ingest
1. Add cornerstone items (50+ per decade)
2. Normalize fields (types, categories, formats)
3. Attach URLs for verification
4. Run audit for completeness

### Audit Checklist
- [ ] Required fields present
- [ ] Format/OS coverage
- [ ] Release year populated
- [ ] URLs verified
- [ ] Status accurate

### Export Pipeline
```bash
# Full export
python3 tools/export/export_index.py --format all

# Generates:
# - data/index.json (dashboard)
# - data/catalog.csv (bulk edit)
# - data/developers.json (constellations)
# - checksums/*.md5
```

---

## Policies

### Naming
- Always capitalize **NOIZY**
- Use full legal product names
- Developer names as officially styled

### Accessibility
- Large-tile touch-friendly dashboards
- Voice/gaze/switch control compatible
- WCAG AA color contrast

### Auditability
- Idempotent CLI commands
- MD5 checksums on exports
- Git version control

---

## Future Extensions

- [ ] **CLAP tracking** - Adoption status per plugin
- [ ] **Atmos readiness** - DAW/plugin support flags
- [ ] **MPE support** - Tag MPE-compatible instruments
- [ ] **AI features** - Track AI-assisted capabilities
- [ ] **License tracking** - Perpetual vs subscription

---

## Stats (Current)

| Metric | Count |
|--------|-------|
| Total Items | 75+ |
| DAWs | 12 |
| Instruments | 20+ |
| Plugins | 43+ |
| AI Models | 15+ |
| Repair Workflows | 7 |

---

## License

Proprietary - Fish Music Inc. / NOIZYLAB

---

*THE LIBRARIAN - Curating the Audio Canon*
