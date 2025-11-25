# METABEAST_CC Changelog

All notable changes to METABEAST_CC - The Audio Canon Command Center.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-25

### Added

#### Core Catalog System
- `data/catalog.yaml` - Master catalog with 75+ audio production items
- `data/index.json` - Dashboard-ready JSON export for MissionControl96
- Schema definition with required/optional fields
- Item ID auto-generation by type (daw-XXX, plug-XXX, inst-XXX, ai-XXX)

#### Manifests
- `manifests/DAW/DAW_MANIFEST.yaml` - 25 DAWs with full specifications
  - Tier classification (Industry Standard, Professional, Specialized, Free)
  - Pricing, features, stock plugins, strengths/weaknesses
- `manifests/Plugins/PLUGIN_MANIFEST.yaml` - Complete plugin registry
  - Categories: EQ, Compressors, Reverbs, Delays, Saturation, Limiters
  - Ratings, pricing, feature highlights
- `manifests/Instruments/INSTRUMENT_MANIFEST.yaml` - Virtual instruments
  - Synths (Wavetable, Analog, Hybrid), Samplers, Orchestral, Drums
  - Kontakt Quick Load organization guide
- `manifests/Repair_Tools/REPAIR_AI_MANIFEST.yaml` - Repair tools & workflows
  - 7 complete repair workflows with step-by-step guides
  - Tool recommendations per task
- `manifests/AI_Models/AI_MODELS_MANIFEST.yaml` - 50+ AI models
  - Transcription: Whisper, AssemblyAI, Deepgram, Vosk
  - Stem Separation: Demucs, LALAL.AI, Spleeter
  - Video AI: Topaz, DaVinci, Runway
  - Voice Synthesis: ElevenLabs, Descript, Resemble AI
  - Music Generation: Suno, Udio, Stable Audio

#### CLI Tools
- `tools/audiocat` - Main CLI with commands:
  - `init` - Initialize registry structure
  - `add` - Add items to catalog
  - `search` - Search catalog
  - `list` - List with filters
  - `audit` - Run catalog audit
  - `export` - Export to JSON/CSV
  - `guide` - AI repair workflow guide
- `tools/ai_host_guide.py` - Interactive repair workflow assistant
- `tools/validate_schema.py` - Schema validation with strict mode
- `tools/snapshot.py` - Backup/restore manager with MD5 checksums
- `tools/audit/run_audit.py` - Comprehensive audit reporting
- `tools/ingest/add_items.py` - CSV import and interactive add
- `tools/export/export_index.py` - Multi-format export

#### Integrations
- `integrations/missioncontrol96_dashboard.yaml` - Full dashboard config
  - 6 pages: Overview, Catalog, Developers, Timeline, Repair, Audit
  - Accessibility: Voice, gaze, switch control, keyboard shortcuts
  - Dark/light themes
- `integrations/homeassistant.yaml` - Home Assistant integration
  - REST sensors for catalog stats
  - Template sensors for calculated values
  - Automations: Monthly audit, health alerts, weekly backup
  - Shell commands and scripts
- `integrations/nodered_flows.json` - Node-RED automation
  - Monthly audit trigger (1st @ 3AM)
  - Weekly export (Sunday @ 4AM)
  - Daily backup (2AM)
  - REST API endpoints
  - Health monitoring

#### Templates
- `templates/kontakt_quickload/` - Kontakt library organization guide

#### Configuration
- `requirements.txt` - Python dependencies
- `setup.py` - Package installer
- `.env.example` - Environment configuration template
- `data/sample_import.csv` - Sample CSV for testing imports

### Features
- Accessibility-first design (WCAG AA, voice/gaze/switch control)
- MD5 checksums on all exports
- Health scoring system (0-100)
- Developer constellation mapping
- Decade timeline visualization
- Multi-platform support (macOS, Windows, Linux)

---

## [Unreleased]

### Planned
- Web dashboard UI
- Docker containerization
- GitHub Actions CI/CD
- Unit test suite
- CLAP format tracking
- Dolby Atmos readiness flags
- MPE support tagging
- License management (perpetual vs subscription)
- Mobile companion app
- Voice command interface

---

## Version History

| Version | Date | Highlights |
|---------|------|------------|
| 1.0.0 | 2025-11-25 | Initial release - METABEAST_CC |

---

*Fish Music Inc. / MissionControl96 / NOIZYLAB*
