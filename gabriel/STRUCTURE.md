# GABRIEL - Organized Structure

## Root Directory (Active Code)
```
GABRIEL/
├── config/           # Configuration files
├── logs/             # System logs
├── projects/         # Active projects
├── scripts/          # Shell scripts
├── system-scripts/   # System management scripts
├── titanhive/        # TitanHive AI agents + voice.py (MAIN VOICE)
├── tools/            # Utility tools
├── voice_ai/         # Voice AI infrastructure
├── workers/          # Cloudflare workers
├── CODEMASTER/       # Code organization system
└── _ORGANIZED/       # Consolidated modules
```

## Core Files
- `gorunfree` - Main GABRIEL launcher
- `start_gabriel.sh` - Startup script
- `mc96_server.py` - MC96 server
- `PUSH_TO_GITHUB.sh` - Git push script

## _ORGANIZED/ Structure
```
_ORGANIZED/
├── core/             # Core system files
├── voice/            # Voice processing modules
├── scripts/          # Organized scripts
├── system/           # System management
├── tools/            # Organized tools
├── workers/          # Worker scripts
├── projects/         # Consolidated projects
├── golang/           # Go code
├── archive/          # Archives
├── automation/       # Automation scripts
├── business/         # Business docs
├── infrastructure/   # Infra configs
├── hp_omen/          # HP Omen integration
├── PORTAL/           # Portal modules
├── SystemGuardian/   # System guardian
├── TURBO/            # Turbo modules
└── VPN/              # VPN configs
```

## Key Modules

### Voice System (titanhive/voice.py)
- Master Voice Engine: Triple-layered Winston voice
- Jamie Premium + OpenAI Onyx + Edge TTS Thomas
- 3 semitone pitch drop for gruff British sound
- Real-time streaming with progress callbacks

### Commands
```bash
python3 titanhive/voice.py master "text"   # Master voice
python3 titanhive/voice.py realtime "text" # Low latency
./gorunfree                                 # Launch GABRIEL
./start_gabriel.sh                          # Start system
```

## CODEMASTER Structure
```
CODEMASTER/
├── _ORGANIZED/       # Organized code
│   ├── 01_CORE/
│   ├── 02_VOICE/
│   ├── 03_SCRIPTS/
│   ├── 04_MCP/
│   ├── 05_TOOLS/
│   ├── 06_AI/
│   ├── 07_LEGACY/
│   └── 08_KNOWLEDGE/
└── _HARVEST/         # Collected code to organize
```

---
Last Updated: 2024-12-28
