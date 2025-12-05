#!/usr/bin/env bash
# ==============================================================================
# 🚀 MASTER UPGRADE & IMPROVE ALL - NOIZYLAB ULTIMATE UPGRADE
# ==============================================================================
# Upgrades, improves, and optimizes EVERYTHING in NOIZYLAB
# ==============================================================================

set -euo pipefail

NOIZYLAB="/Users/m2ultra/NOIZYLAB"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG="$NOIZYLAB/logs/upgrade-${TIMESTAMP}.log"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

mkdir -p "$NOIZYLAB/logs"

log() {
    echo -e "${CYAN}${1}${NC}" | tee -a "$LOG"
}

log_header() {
    echo "" | tee -a "$LOG"
    echo -e "${BOLD}${GREEN}═══════════════════════════════════════════════════════════${NC}" | tee -a "$LOG"
    echo -e "${BOLD}${CYAN}${1}${NC}" | tee -a "$LOG"
    echo -e "${BOLD}${GREEN}═══════════════════════════════════════════════════════════${NC}" | tee -a "$LOG"
}

# ==============================================================================
# STEP 1: ORGANIZE EVERYTHING
# ==============================================================================

organize_all() {
    log_header "📦 STEP 1: ORGANIZING ALL FILES"
    
    mkdir -p "$NOIZYLAB/scripts" "$NOIZYLAB/docs" "$NOIZYLAB/.archive/old-versions" "$NOIZYLAB/config"
    
    local moved=0
    
    # Move all scripts
    for f in "$NOIZYLAB"/*.{sh,py,js,mjs}; do
        if [ -f "$f" ]; then
            basename=$(basename "$f")
            # Keep main agents and current script in root
            if [[ ! "$basename" =~ ^(gabriel-cli|mc96-cli|MASTER_UPGRADE_ALL|UPGRADE_ALL|START|launch)\.(mjs|sh|py)$ ]]; then
                mv "$f" "$NOIZYLAB/scripts/" 2>/dev/null && log "  ✓ Moved: $basename → scripts/" && moved=$((moved + 1)) || true
            fi
        fi
    done
    
    # Move docs (keep README.md)
    for f in "$NOIZYLAB"/*.md; do
        if [ -f "$f" ] && [ "$(basename "$f")" != "README.md" ]; then
            mv "$f" "$NOIZYLAB/docs/" 2>/dev/null && log "  ✓ Moved: $(basename "$f") → docs/" && moved=$((moved + 1)) || true
        fi
    done
    
    # Archive versioned files
    for f in "$NOIZYLAB"/*_V*.{sh,py,md} "$NOIZYLAB"/*_v*.{sh,py,md}; do
        if [ -f "$f" ]; then
            mv "$f" "$NOIZYLAB/.archive/old-versions/" 2>/dev/null && log "  ✓ Archived: $(basename "$f")" && moved=$((moved + 1)) || true
        fi
    done
    
    log "✅ Organized $moved files"
}

# ==============================================================================
# STEP 2: UPGRADE SCRIPTS WITH IMPROVEMENTS
# ==============================================================================

upgrade_scripts() {
    log_header "⚡ STEP 2: UPGRADING SCRIPTS"
    
    # Make all scripts executable
    find "$NOIZYLAB" -type f \( -name "*.sh" -o -name "*.py" \) -exec chmod +x {} \; 2>/dev/null
    log "  ✓ Made all scripts executable"
    
    # Add shebangs to Python scripts missing them
    find "$NOIZYLAB" -type f -name "*.py" -exec grep -L "^#!/usr/bin/env python" {} \; 2>/dev/null | while read -r file; do
        if [ -f "$file" ]; then
            sed -i '' '1i\
#!/usr/bin/env python3
' "$file" 2>/dev/null || true
            log "  ✓ Added shebang to: $(basename "$file")"
        fi
    done
    
    log "✅ Scripts upgraded"
}

# ==============================================================================
# STEP 3: CLEAN TEMPORARY FILES
# ==============================================================================

clean_temp_files() {
    log_header "🧹 STEP 3: CLEANING TEMPORARY FILES"
    
    local cleaned=0
    
    # Python cache
    local pycache=$(find "$NOIZYLAB" -type d -name "__pycache__" 2>/dev/null | wc -l | tr -d ' ')
    if [ "$pycache" -gt 0 ]; then
        find "$NOIZYLAB" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
        find "$NOIZYLAB" -name "*.pyc" -delete 2>/dev/null || true
        log "  ✓ Removed Python cache files"
    fi
    
    # .DS_Store
    find "$NOIZYLAB" -name ".DS_Store" -delete 2>/dev/null || true
    log "  ✓ Removed .DS_Store files"
    
    # Temp files
    find "$NOIZYLAB" -name "*.tmp" -delete 2>/dev/null || true
    find "$NOIZYLAB" -name "*.swp" -delete 2>/dev/null || true
    find "$NOIZYLAB" -name "*~" -delete 2>/dev/null || true
    log "  ✓ Removed temporary files"
    
    log "✅ Cleanup complete"
}

# ==============================================================================
# STEP 4: OPTIMIZE DATABASES
# ==============================================================================

optimize_databases() {
    log_header "💾 STEP 4: OPTIMIZING DATABASES"
    
    # Optimize SQLite databases
    for db in "$NOIZYLAB"/*.db; do
        if [ -f "$db" ]; then
            sqlite3 "$db" "VACUUM; ANALYZE; REINDEX;" 2>/dev/null && log "  ✓ Optimized: $(basename "$db")" || true
        fi
    done
    
    # Find databases in subdirectories
    find "$NOIZYLAB" -name "*.db" -type f 2>/dev/null | while read -r db; do
        sqlite3 "$db" "VACUUM; ANALYZE; REINDEX;" 2>/dev/null && log "  ✓ Optimized: $(basename "$db")" || true
    done
    
    log "✅ Databases optimized"
}

# ==============================================================================
# STEP 5: CREATE IMPROVED STRUCTURE
# ==============================================================================

create_structure() {
    log_header "🏗️  STEP 5: CREATING IMPROVED STRUCTURE"
    
    # Create essential directories
    mkdir -p "$NOIZYLAB"/{scripts,docs,config,logs,backups,temp,workflows,automation}
    mkdir -p "$NOIZYLAB/.archive"/{old-versions,deprecated,backups}
    
    log "  ✓ Created directory structure"
    
    # Create .gitignore if missing
    if [ ! -f "$NOIZYLAB/.gitignore" ]; then
        cat > "$NOIZYLAB/.gitignore" << 'EOF'
# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Logs
*.log
logs/

# Databases
*.db
*.sqlite
*.sqlite3

# Archives
*.tar.gz
*.zip
*.rar

# Temporary
*.tmp
*.swp
*~
temp/
EOF
        log "  ✓ Created .gitignore"
    fi
    
    log "✅ Structure created"
}

# ==============================================================================
# STEP 6: CREATE QUICK REFERENCE
# ==============================================================================

create_quick_reference() {
    log_header "📚 STEP 6: CREATING QUICK REFERENCE"
    
    cat > "$NOIZYLAB/QUICK_REFERENCE.md" << 'EOF'
# 🚀 NOIZYLAB Quick Reference

## Your Agents

### 🟣 GABRIEL
```bash
node gabriel-cli.mjs scan
node gabriel-cli.mjs heal
node gabriel-cli.mjs organize
node gabriel-cli.mjs workflow
node gabriel-cli.mjs status
```

### 🔵 MC96
```bash
node mc96-cli.mjs agent <Name> --kind modern --mods text,vision
node mc96-cli.mjs migrate
node mc96-cli.mjs deploy --env production
```

## Quick Commands

### Cleanup & Organize
```bash
./MASTER_UPGRADE_ALL.sh          # Upgrade everything
./FAST_CLEANUP.sh                 # Quick cleanup
python3 QUICK_ORGANIZE.py         # Organize files
```

### Analysis
```bash
python3 CHECK_AGENTS.py           # Check running processes
python3 disk_usage_analyzer.py    # Analyze disk usage
./media_offload.sh --audit        # Audit media files
```

### Start Services
```bash
./START_EVERYTHING.sh             # Start all services
./launch-v3                       # Master launcher
```

## Directory Structure

```
NOIZYLAB/
├── scripts/          # All scripts
├── docs/             # Documentation
├── config/           # Configuration files
├── logs/             # Log files
├── backups/          # Backups
├── .archive/         # Archived files
└── [projects]/       # Your projects
```

## Performance Tips

1. **If slow**: Run `python3 CHECK_AGENTS.py` to find heavy processes
2. **Large files**: Use `./media_offload.sh --audit` to find media
3. **Cleanup**: Run `./FAST_CLEANUP.sh` regularly

## Key Files

- `gabriel-cli.mjs` - GABRIEL agent
- `mc96-cli.mjs` - MC96 agent
- `MASTER_UPGRADE_ALL.sh` - Master upgrade script
- `QUICK_REFERENCE.md` - This file

---
Last updated: $(date)
EOF
    
    log "  ✓ Created QUICK_REFERENCE.md"
    log "✅ Documentation created"
}

# ==============================================================================
# STEP 7: CREATE PERFORMANCE MONITOR
# ==============================================================================

create_performance_monitor() {
    log_header "⚡ STEP 7: CREATING PERFORMANCE MONITOR"
    
    cat > "$NOIZYLAB/PERFORMANCE_MONITOR.py" << 'PERFMON'
#!/usr/bin/env python3
"""
Performance Monitor - Quick system health check
"""

import subprocess
import sys
from datetime import datetime

def check_cpu():
    """Check CPU usage"""
    try:
        result = subprocess.run(['top', '-l', '1', '-n', '10'], 
                              capture_output=True, text=True, timeout=3)
        lines = result.stdout.split('\n')
        cpu_line = [l for l in lines if 'CPU usage' in l]
        if cpu_line:
            print(f"💻 CPU: {cpu_line[0]}")
    except:
        print("💻 CPU: Could not check")

def check_memory():
    """Check memory usage"""
    try:
        result = subprocess.run(['vm_stat'], capture_output=True, text=True, timeout=3)
        print("💾 Memory Stats:")
        for line in result.stdout.split('\n')[:5]:
            if ':' in line:
                print(f"   {line.strip()}")
    except:
        print("💾 Memory: Could not check")

def check_processes():
    """Check top processes"""
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=3)
        lines = sorted(result.stdout.split('\n'), 
                      key=lambda x: float(x.split()[2]) if len(x.split()) > 2 and x.split()[2].replace('.', '').isdigit() else 0,
                      reverse=True)
        print("\n🔥 Top CPU Processes:")
        for line in lines[1:6]:
            if line.strip():
                parts = line.split()
                if len(parts) > 10:
                    cpu = parts[2]
                    cmd = ' '.join(parts[10:])
                    print(f"   {cpu:>5}%  {cmd[:60]}...")
    except:
        print("🔥 Processes: Could not check")

def main():
    print("=" * 70)
    print(" " * 20 + "PERFORMANCE MONITOR")
    print("=" * 70)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    check_cpu()
    print()
    check_memory()
    check_processes()
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
PERFMON
    
    chmod +x "$NOIZYLAB/PERFORMANCE_MONITOR.py"
    log "  ✓ Created PERFORMANCE_MONITOR.py"
    log "✅ Performance monitor created"
}

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

main() {
    echo -e "${BOLD}${GREEN}"
    echo "═══════════════════════════════════════════════════════════"
    echo "   🚀 MASTER UPGRADE & IMPROVE ALL - NOIZYLAB ULTIMATE"
    echo "═══════════════════════════════════════════════════════════"
    echo -e "${NC}"
    
    log "Started at: $(date)"
    log "Log file: $LOG"
    echo ""
    
    organize_all
    upgrade_scripts
    clean_temp_files
    optimize_databases
    create_structure
    create_quick_reference
    create_performance_monitor
    
    log_header "✅ UPGRADE COMPLETE!"
    
    echo -e "${GREEN}"
    echo "═══════════════════════════════════════════════════════════"
    echo "   ✨ ALL SYSTEMS UPGRADED & IMPROVED!"
    echo "═══════════════════════════════════════════════════════════"
    echo -e "${NC}"
    
    log ""
    log "📚 Next steps:"
    log "  1. Review: cat QUICK_REFERENCE.md"
    log "  2. Check performance: python3 PERFORMANCE_MONITOR.py"
    log "  3. Check agents: python3 CHECK_AGENTS.py"
    log ""
    log "Completed at: $(date)"
}

main

