# NOIZYLAB Cleanup & Organization Plan

## 🎯 Your Agents Found

1. **🟣 GABRIEL** - `/Users/m2ultra/NOIZYLAB/gabriel-cli.mjs`
   - Local-first command interface
   - Commands: scan, heal, organize, workflow, daemon

2. **🔵 MC96** - `/Users/m2ultra/NOIZYLAB/mc96-cli.mjs`
   - Super-cursor scaffold tool
   - Commands: init, generate, agent, migrate, deploy

## 🚀 Quick Actions (FAST - No Heavy Scanning)

### Option 1: Run FAST_CLEANUP.sh (Recommended)
```bash
cd /Users/m2ultra/NOIZYLAB
./FAST_CLEANUP.sh
```
This will:
- ✅ Move all scripts to `scripts/` folder
- ✅ Move docs to `docs/` folder  
- ✅ Archive old versioned scripts
- ✅ Clean .DS_Store files
- ⚡ **FAST** - No heavy scanning

### Option 2: Run Python Organizer
```bash
cd /Users/m2ultra/NOIZYLAB
python3 QUICK_ORGANIZE.py
```

## 📊 Check What's Running (If System is Slow)

```bash
cd /Users/m2ultra/NOIZYLAB
python3 CHECK_AGENTS.py
```

This shows:
- Running agent processes
- Python processes consuming resources
- System resource usage

## 🔍 Why /Users/m2ultra Might Be 260GB

Common culprits:
1. **Library/Caches** - Browser, app caches
2. **Library/CloudStorage** - iCloud sync files
3. **node_modules** - Multiple projects with dependencies
4. **Media files** - Photos, videos, downloads
5. **Backups** - Time Machine or app backups

### To Analyze Disk Usage:

**Option A: Use the analyzer**
```bash
cd /Users/m2ultra/NOIZYLAB
python3 disk_usage_analyzer.py
```

**Option B: Quick terminal check**
```bash
du -sh ~/Library/Caches
du -sh ~/Library/CloudStorage
du -sh ~/Downloads
du -sh ~/NOIZYLAB
```

## 📁 Recommended NOIZYLAB Structure

```
NOIZYLAB/
├── scripts/              # All .sh and .py scripts
├── docs/                 # All .md documentation
├── .archive/            # Old versions, backups
│   └── old-versions/    # Versioned scripts
├── gabriel-cli.mjs      # GABRIEL agent (keep in root)
├── mc96-cli.mjs         # MC96 agent (keep in root)
├── media_offload.sh     # Media mover (keep in root)
├── README.md            # Main readme
└── [projects]/          # Your actual projects
```

## 🎬 For Large Media Files

If you have large media files consuming space:

```bash
cd /Users/m2ultra/NOIZYLAB
./media_offload.sh --audit "/Users/m2ultra" "/Volumes/12TB"
```

This will:
- Audit all media files
- Show what can be moved
- Optionally move to external drive

## ✅ Files Created

1. **FAST_CLEANUP.sh** - Quick bash cleanup script
2. **QUICK_ORGANIZE.py** - Quick Python organizer
3. **CHECK_AGENTS.py** - Check running processes
4. **disk_usage_analyzer.py** - Analyze disk usage
5. **MASTER_CLEANUP_ORGANIZER.sh** - Comprehensive cleanup (slower)
6. **media_offload.sh** - Media file mover

## 🎯 Recommended Order

1. **First**: Run `./FAST_CLEANUP.sh` (organizes files)
2. **Then**: Run `python3 CHECK_AGENTS.py` (check if agents are slowing things)
3. **Finally**: If still slow, run `python3 disk_usage_analyzer.py` (find what's big)

---

**Next Steps**: Run `./FAST_CLEANUP.sh` to organize everything quickly!

