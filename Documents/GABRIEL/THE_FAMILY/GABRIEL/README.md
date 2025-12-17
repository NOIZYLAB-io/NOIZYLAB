# GABRIEL File Management Suite

Production-ready intelligent file management system with AI-powered classification, automated organization, and comprehensive monitoring.

---

## ⚠️ IMPORTANT: macOS Shell Configuration Fix

**If you're seeing terminal errors about shell paths or VS Code integration not working:**

Before getting started, apply the macOS shell environment fix:

```bash
# Quick fix (recommended)
bash /Users/rsp_ms/fix_shell.sh

# Then replace VS Code settings
cp /Users/rsp_ms/vscode_settings_fixed.json \
   ~/Library/Application\ Support/Code/User/settings.json
```

📖 **[Read the full fix guide →](GABRIEL_MACOS_FIX_GUIDE.md)**

This resolves:
- ✅ Broken shell paths referencing old user accounts
- ✅ VS Code terminal integration issues
- ✅ Python and Git configuration problems
- ✅ Outdated macOS naming conventions (OSX → osx)

---

## 🎯 Overview

GABRIEL is a modular Python suite consisting of three core components:

- **DeepScan**: Advanced file system crawler with duplicate detection and metadata extraction
- **SenseMaker**: AI-powered semantic tagging and content classification
- **HiveSort**: Intelligent file organization with version control and cloud mirroring

## ✨ Features

- 🔍 **Recursive file crawling** with configurable depth and filters
- 🤖 **AI-powered classification** using local/cloud models
- 🎯 **Semantic tagging** and content analysis
- 📦 **Duplicate detection** using multiple hashing strategies
- 🗂️ **Automated organization** with rule-based sorting
- 📊 **Real-time dashboard** (FastAPI + React/Streamlit)
- ☁️ **Cloud backup** and mirror sync support
- 🔄 **Version control** for organized files
- ⏰ **Scheduled automation** for nightly runs
- 📈 **Comprehensive logging** and monitoring

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+ (for React dashboard)
- Virtual environment tool (venv/conda)

### Installation

```bash
# Clone and navigate to project
cd /Users/rsp_ms/GABRIEL/THE_FAMILY/GABRIEL

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure settings
cp config/config.template.yaml config/config.yaml
# Edit config/config.yaml with your drive paths and preferences

# Initialize database
python src/core/database.py
```

### Basic Usage

```bash
# Run full pipeline
python src/main.py --config config/config.yaml

# Run individual components
python src/deepscan/scanner.py --path /path/to/scan
python src/sensemaker/classifier.py --input scan_results.json
python src/hivesort/organizer.py --input classified_results.json

# Start dashboard
python src/dashboard/api.py  # FastAPI backend on :8000
# or
streamlit run src/dashboard/streamlit_app.py  # Streamlit on :8501
```

## 📁 Project Structure

```
GABRIEL/
├── config/
│   ├── config.template.yaml      # Main configuration template
│   ├── drives.yaml               # Network drive mappings
│   ├── rules.yaml                # Organization rules
│   ├── schedule.yaml             # Automation schedule
│   └── cloud_backup.yaml         # Cloud sync settings
├── src/
│   ├── core/                     # Core utilities
│   │   ├── database.py           # SQLite database manager
│   │   ├── logger.py             # Logging configuration
│   │   └── utils.py              # Helper functions
│   ├── deepscan/                 # File scanning module
│   │   ├── scanner.py            # Main scanner
│   │   ├── duplicate_detector.py # Duplicate finding
│   │   └── metadata_extractor.py # Metadata extraction
│   ├── sensemaker/               # AI classification module
│   │   ├── classifier.py         # Content classifier
│   │   ├── semantic_tagger.py    # Semantic tagging
│   │   └── models.py             # AI model wrappers
│   ├── hivesort/                 # Organization module
│   │   ├── organizer.py          # File organizer
│   │   ├── version_control.py    # Version tracking
│   │   └── cloud_sync.py         # Cloud mirroring
│   ├── dashboard/                # Web interfaces
│   │   ├── api.py                # FastAPI backend
│   │   ├── streamlit_app.py      # Streamlit dashboard
│   │   └── frontend/             # React app
│   ├── automation/               # Scheduling
│   │   ├── scheduler.py          # Task scheduler
│   │   └── notifier.py           # Alert system
│   └── main.py                   # Main orchestrator
├── data/                         # Data storage
│   ├── database/                 # SQLite databases
│   ├── logs/                     # Application logs
│   └── cache/                    # Temporary cache
├── tests/                        # Test suite
├── docker/                       # Docker configs
├── docs/                         # Documentation
├── requirements.txt              # Python dependencies
└── .env.example                  # Environment variables
```

## ⚙️ Configuration

### Main Configuration (`config/config.yaml`)

```yaml
scanning:
  root_paths:
    - /Users/rsp_ms/GABRIEL
    - /Volumes/NetworkDrive
  exclude_patterns:
    - "*.tmp"
    - ".git"
  max_depth: 10
  parallel_workers: 4

classification:
  model_provider: "openai"  # openai, anthropic, local
  model_name: "gpt-4"
  enable_semantic_search: true
  confidence_threshold: 0.7

organization:
  destination_root: /Users/rsp_ms/GABRIEL/Organized
  create_structure: true
  version_control: true
  dry_run: false
```

### Network Drives (`config/drives.yaml`)

```yaml
drives:
  - name: "Production NAS"
    path: "/Volumes/ProductionNAS"
    type: "smb"
    enabled: true
  - name: "Backup Drive"
    path: "/Volumes/BackupDrive"
    type: "local"
    enabled: true
```

### Cloud Backup (`config/cloud_backup.yaml`)

```yaml
providers:
  - name: "aws_s3"
    bucket: "gabriel-backups"
    region: "us-east-1"
    enabled: true
  - name: "google_drive"
    folder_id: "xxxxx"
    enabled: false
```

## 🤖 Automation

### Nightly Scheduled Run

```bash
# Install as cron job (Unix/macOS)
python src/automation/scheduler.py --install

# Or use the scheduler daemon
python src/automation/scheduler.py --daemon
```

### Manual Scheduling (`config/schedule.yaml`)

```yaml
schedules:
  - name: "nightly_scan"
    cron: "0 2 * * *"  # 2 AM daily
    tasks:
      - deepscan
      - sensemaker
      - hivesort
      - cloud_sync
  - name: "weekly_deep_clean"
    cron: "0 3 * * 0"  # 3 AM Sunday
    tasks:
      - duplicate_cleanup
      - version_cleanup
```

## 📊 Dashboard

### FastAPI + React Dashboard

```bash
# Start backend
cd src/dashboard
python api.py

# Start frontend (new terminal)
cd src/dashboard/frontend
npm install
npm start
```

Access at `http://localhost:3000`

### Streamlit Dashboard

```bash
streamlit run src/dashboard/streamlit_app.py
```

Access at `http://localhost:8501`

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific module tests
pytest tests/test_deepscan.py
pytest tests/test_sensemaker.py
pytest tests/test_hivesort.py

# Run with coverage
pytest --cov=src tests/
```

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or use individual containers
docker build -t gabriel-suite .
docker run -v /your/data:/data gabriel-suite
```

## 📈 Monitoring

- **Logs**: `data/logs/gabriel.log`
- **Dashboard**: Real-time stats and progress
- **Notifications**: Email/Slack alerts on completion/errors
- **Database**: SQLite at `data/database/gabriel.db`

## 🔧 Advanced Usage

### Custom Classification Rules

Edit `config/rules.yaml`:

```yaml
rules:
  - pattern: "*.pdf"
    category: "documents"
    destination: "Documents/PDFs"
  - pattern: "IMG_*.jpg"
    category: "photos"
    destination: "Photos/{year}/{month}"
  - semantic: "contains invoice"
    category: "financial"
    destination: "Finance/Invoices"
```

### API Integration

```python
from src.deepscan.scanner import FileScanner
from src.sensemaker.classifier import AIClassifier
from src.hivesort.organizer import FileOrganizer

# Scan files
scanner = FileScanner(root_path="/path/to/scan")
results = scanner.scan()

# Classify
classifier = AIClassifier()
classified = classifier.classify(results)

# Organize
organizer = FileOrganizer()
organizer.organize(classified)
```

## 🤝 Contributing

See `docs/CONTRIBUTING.md` for development guidelines.

## 📄 License

MIT License - See LICENSE file

## 🆘 Troubleshooting

See `docs/TROUBLESHOOTING.md` for common issues and solutions.

## 📞 Support

- Issues: GitHub Issues
- Documentation: `docs/`
- Examples: `examples/`

✅ FIX APPLIED!
