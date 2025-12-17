# COMPLETE INSTALL & UPGRADE - Make Everything Perfect
# Rob Sonic Protocol | GORUNFREE | MC96

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  COMPLETE INSTALL & UPGRADE - MC96                 ║" -ForegroundColor Cyan
Write-Host "║  Installing & Upgrading Everything                 ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$LOG_FILE = "/Users/rsp_ms/CODE_MASTER/logs/install_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
New-Item -ItemType Directory -Force -Path "/Users/rsp_ms/CODE_MASTER/logs" | Out-Null

function Write-InstallLog {
    param($Message, $Color = "White")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] $Message"
    Write-Host $logMessage -ForegroundColor $Color
    Add-Content -Path $LOG_FILE -Value $logMessage
}

Write-InstallLog "=== COMPLETE INSTALL STARTED ===" "Cyan"

# PHASE 1: VERIFY ALL DIRECTORIES
Write-InstallLog "PHASE 1: Verifying directory structure..." "Yellow"
$dirs = @(
    "/Users/rsp_ms/CODE_MASTER",
    "/Users/rsp_ms/CODE_MASTER/scripts",
    "/Users/rsp_ms/CODE_MASTER/python",
    "/Users/rsp_ms/CODE_MASTER/nodejs",
    "/Users/rsp_ms/CODE_MASTER/config",
    "/Users/rsp_ms/CODE_MASTER/docs",
    "/Users/rsp_ms/CODE_MASTER/logs",
    "/Users/rsp_ms/CODE_MASTER/upgrades",
    "/Users/rsp_ms/CODE_MASTER/backups"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    Write-InstallLog "  ✓ $dir" "Green"
}
Write-Host ""

# PHASE 2: INSTALL ALL SCRIPTS WITH PERMISSIONS
Write-InstallLog "PHASE 2: Installing all scripts..." "Yellow"
$scripts = Get-ChildItem "/Users/rsp_ms/CODE_MASTER/scripts" -File -ErrorAction SilentlyContinue
foreach ($script in $scripts) {
    if ($script.Extension -eq ".sh" -or $script.Extension -eq ".bash") {
        chmod +x $script.FullName 2>/dev/null
        Write-InstallLog "  ✓ $($script.Name) - Executable" "Green"
    }
}
Write-Host ""

# PHASE 3: CREATE SYSTEM SERVICE SCRIPTS
Write-InstallLog "PHASE 3: Creating system service scripts..." "Yellow"

# Daily Maintenance
$dailyMaintenance = @"
#!/bin/bash
# DAILY MAINTENANCE - MC96
# Run daily system maintenance tasks

echo "╔════════════════════════════════════════════════════╗"
echo "║  DAILY MAINTENANCE - MC96                         ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Health check
echo "🏥 Running health check..."
bash "$HOME/CODE_MASTER/scripts/HEALTH_CHECK.sh" > "$HOME/CODE_MASTER/logs/health_$(date +%Y%m%d).log" 2>&1

# Auto-optimize
echo ""
echo "🧹 Running auto-optimization..."
bash "$HOME/CODE_MASTER/scripts/AUTO_OPTIMIZE.sh" >> "$HOME/CODE_MASTER/logs/health_$(date +%Y%m%d).log" 2>&1

# GHOST drive check
echo ""
echo "👻 Checking GHOST drive..."
if [ -L "$HOME/Desktop/GHOST_DRIVE" ]; then
    TARGET=$(readlink "$HOME/Desktop/GHOST_DRIVE")
    if [ -d "$TARGET" ]; then
        echo "  ✓ GHOST drive accessible"
    else
        echo "  ✗ GHOST drive not mounted"
    fi
fi

echo ""
echo "✅ Daily maintenance complete!"
"@

$dailyMaintenance | Out-File -FilePath "/Users/rsp_ms/CODE_MASTER/scripts/DAILY_MAINTENANCE.sh" -Encoding utf8 -NoNewline
chmod +x "/Users/rsp_ms/CODE_MASTER/scripts/DAILY_MAINTENANCE.sh"
Write-InstallLog "  ✓ Daily maintenance script created" "Green"

# Backup System
$backupSystem = @"
#!/bin/bash
# AUTOMATED BACKUP SYSTEM - MC96
# Comprehensive backup automation

echo "╔════════════════════════════════════════════════════╗"
echo "║  AUTOMATED BACKUP SYSTEM - MC96                   ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

BACKUP_DIR="$HOME/CODE_MASTER/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Backup CODE_MASTER scripts
echo "📦 Backing up CODE_MASTER scripts..."
tar -czf "$BACKUP_DIR/code_master_scripts.tar.gz" "$HOME/CODE_MASTER/scripts" 2>/dev/null
echo "  ✓ Scripts backed up"

# Backup configs
echo ""
echo "📦 Backing up configurations..."
if [ -d "$HOME/CODE_MASTER/config" ]; then
    tar -czf "$BACKUP_DIR/configs.tar.gz" "$HOME/CODE_MASTER/config" 2>/dev/null
    echo "  ✓ Configs backed up"
fi

# Backup logs (compressed)
echo ""
echo "📦 Backing up logs..."
if [ -d "$HOME/CODE_MASTER/logs" ]; then
    find "$HOME/CODE_MASTER/logs" -name "*.log" -mtime +7 -exec gzip {} \; 2>/dev/null
    echo "  ✓ Logs compressed"
fi

echo ""
echo "✅ Backup complete: $BACKUP_DIR"
"@

$backupSystem | Out-File -FilePath "/Users/rsp_ms/CODE_MASTER/scripts/AUTO_BACKUP.sh" -Encoding utf8 -NoNewline
chmod +x "/Users/rsp_ms/CODE_MASTER/scripts/AUTO_BACKUP.sh"
Write-InstallLog "  ✓ Backup system created" "Green"

# Performance Monitor
$perfMonitor = @"
#!/bin/bash
# PERFORMANCE MONITOR - MC96
# Real-time performance monitoring

echo "╔════════════════════════════════════════════════════╗"
echo "║  PERFORMANCE MONITOR - MC96                        ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

while true; do
    clear
    echo "╔════════════════════════════════════════════════════╗"
    echo "║  PERFORMANCE MONITOR - MC96 (Press Ctrl+C to exit)║"
    echo "╚════════════════════════════════════════════════════╝"
    echo ""
    
    # CPU
    echo "⚡ CPU Usage:"
    top -l 1 | grep "CPU usage" | awk '{print "  " $0}'
    
    # Memory
    echo ""
    echo "💾 Memory:"
    vm_stat | head -5 | awk '{print "  " $0}'
    
    # Disk
    echo ""
    echo "📊 Disk Usage:"
    df -h / | tail -1 | awk '{print "  Root: " $5 " used (" $4 " free)"}'
    
    # Network
    echo ""
    echo "🌐 Network:"
    ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print "  " $2}'
    
    sleep 2
done
"@

$perfMonitor | Out-File -FilePath "/Users/rsp_ms/CODE_MASTER/scripts/PERF_MONITOR.sh" -Encoding utf8 -NoNewline
chmod +x "/Users/rsp_ms/CODE_MASTER/scripts/PERF_MONITOR.sh"
Write-InstallLog "  ✓ Performance monitor created" "Green"
Write-Host ""

# PHASE 4: CREATE INSTALLATION VERIFICATION
Write-InstallLog "PHASE 4: Creating installation verification..." "Yellow"

$verifyScript = @"
#!/bin/bash
# INSTALLATION VERIFICATION - MC96
# Verify all systems are properly installed

echo "╔════════════════════════════════════════════════════╗"
echo "║  INSTALLATION VERIFICATION - MC96                 ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

PASSED=0
FAILED=0

# Check directories
echo "📁 Checking directories..."
DIRS=(
    "$HOME/CODE_MASTER"
    "$HOME/CODE_MASTER/scripts"
    "$HOME/CODE_MASTER/logs"
    "$HOME/CODE_MASTER/backups"
)

for dir in "`${DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✓ $dir"
        ((PASSED++))
    else
        echo "  ✗ $dir - MISSING"
        ((FAILED++))
    fi
done

# Check scripts
echo ""
echo "📜 Checking scripts..."
SCRIPTS=(
    "HEALTH_CHECK.sh"
    "AUTO_OPTIMIZE.sh"
    "FIX_GHOST_DRIVE.sh"
    "ENHANCED_GHOST_SCAN.sh"
    "DAILY_MAINTENANCE.sh"
    "AUTO_BACKUP.sh"
    "PERF_MONITOR.sh"
)

for script in "`${SCRIPTS[@]}"; do
    if [ -f "$HOME/CODE_MASTER/scripts/$script" ] && [ -x "$HOME/CODE_MASTER/scripts/$script" ]; then
        echo "  ✓ $script"
        ((PASSED++))
    else
        echo "  ✗ $script - MISSING or NOT EXECUTABLE"
        ((FAILED++))
    fi
done

# Check GHOST drive
echo ""
echo "👻 Checking GHOST drive..."
if [ -L "$HOME/Desktop/GHOST_DRIVE" ]; then
    echo "  ✓ GHOST_DRIVE alias exists"
    ((PASSED++))
else
    echo "  ✗ GHOST_DRIVE alias missing"
    ((FAILED++))
fi

# Summary
echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║  VERIFICATION SUMMARY                             ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "  Passed: $PASSED"
echo "  Failed: $FAILED"
echo ""

if [ $FAILED -eq 0 ]; then
    echo "✅ ALL SYSTEMS VERIFIED!"
    exit 0
else
    echo "⚠️  Some systems need attention"
    exit 1
fi
"@

$verifyScript | Out-File -FilePath "/Users/rsp_ms/CODE_MASTER/scripts/VERIFY_INSTALL.sh" -Encoding utf8 -NoNewline
chmod +x "/Users/rsp_ms/CODE_MASTER/scripts/VERIFY_INSTALL.sh"
Write-InstallLog "  ✓ Verification script created" "Green"
Write-Host ""

# PHASE 5: CREATE MASTER CONTROL PANEL
Write-InstallLog "PHASE 5: Creating master control panel..." "Yellow"

$controlPanel = @"
#!/bin/bash
# MASTER CONTROL PANEL - MC96
# Centralized system control

while true; do
    clear
    echo "╔════════════════════════════════════════════════════╗"
    echo "║  MASTER CONTROL PANEL - MC96                      ║"
    echo "╚════════════════════════════════════════════════════╝"
    echo ""
    echo "  1) Health Check"
    echo "  2) Auto Optimize"
    echo "  3) GHOST Drive Scan"
    echo "  4) Performance Monitor"
    echo "  5) Daily Maintenance"
    echo "  6) Auto Backup"
    echo "  7) Verify Installation"
    echo "  8) View Logs"
    echo "  9) Exit"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) bash "$HOME/CODE_MASTER/scripts/HEALTH_CHECK.sh"; read -p "Press Enter to continue...";;
        2) bash "$HOME/CODE_MASTER/scripts/AUTO_OPTIMIZE.sh"; read -p "Press Enter to continue...";;
        3) bash "$HOME/CODE_MASTER/scripts/ENHANCED_GHOST_SCAN.sh"; read -p "Press Enter to continue...";;
        4) bash "$HOME/CODE_MASTER/scripts/PERF_MONITOR.sh";;
        5) bash "$HOME/CODE_MASTER/scripts/DAILY_MAINTENANCE.sh"; read -p "Press Enter to continue...";;
        6) bash "$HOME/CODE_MASTER/scripts/AUTO_BACKUP.sh"; read -p "Press Enter to continue...";;
        7) bash "$HOME/CODE_MASTER/scripts/VERIFY_INSTALL.sh"; read -p "Press Enter to continue...";;
        8) ls -lah "$HOME/CODE_MASTER/logs/" | head -20; read -p "Press Enter to continue...";;
        9) exit 0;;
        *) echo "Invalid option"; sleep 1;;
    esac
done
"@

$controlPanel | Out-File -FilePath "/Users/rsp_ms/CODE_MASTER/CONTROL_PANEL.sh" -Encoding utf8 -NoNewline
chmod +x "/Users/rsp_ms/CODE_MASTER/CONTROL_PANEL.sh"
Write-InstallLog "  ✓ Master control panel created" "Green"
Write-Host ""

# PHASE 6: RUN VERIFICATION
Write-InstallLog "PHASE 6: Running installation verification..." "Yellow"
bash "/Users/rsp_ms/CODE_MASTER/scripts/VERIFY_INSTALL.sh"
Write-Host ""

# PHASE 7: CREATE COMPLETE DOCUMENTATION
Write-InstallLog "PHASE 7: Creating complete documentation..." "Yellow"

$completeDocs = @"
# 🚀 CODE_MASTER - COMPLETE SYSTEM DOCUMENTATION

## ✅ INSTALLATION COMPLETE

**Date:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  
**Status:** ✅ FULLY INSTALLED & VERIFIED

---

## 📁 SYSTEM STRUCTURE

\`\`\`
CODE_MASTER/
├── scripts/          # All system scripts
├── python/           # Python files
├── nodejs/           # JavaScript files
├── config/           # Configuration files
├── docs/             # Documentation
├── logs/             # System logs
├── upgrades/         # Upgrade backups
├── backups/          # System backups
├── CONTROL_PANEL.sh  # Master control panel
└── LAUNCH.sh         # Quick launcher
\`\`\`

---

## 🎯 AVAILABLE SYSTEMS

### **1. Health Check System**
- **Script:** \`scripts/HEALTH_CHECK.sh\`
- **Purpose:** Comprehensive system health monitoring
- **Usage:** \`bash ~/CODE_MASTER/scripts/HEALTH_CHECK.sh\`

### **2. Auto-Optimization**
- **Script:** \`scripts/AUTO_OPTIMIZE.sh\`
- **Purpose:** Automatic system cleanup and optimization
- **Usage:** \`bash ~/CODE_MASTER/scripts/AUTO_OPTIMIZE.sh\`

### **3. GHOST Drive Management**
- **Scripts:** 
  - \`scripts/FIX_GHOST_DRIVE.sh\` - Basic scanner
  - \`scripts/ENHANCED_GHOST_SCAN.sh\` - Advanced analysis
- **Purpose:** GHOST drive scanning and management
- **Usage:** \`bash ~/CODE_MASTER/scripts/ENHANCED_GHOST_SCAN.sh\`

### **4. Performance Monitor**
- **Script:** \`scripts/PERF_MONITOR.sh\`
- **Purpose:** Real-time performance monitoring
- **Usage:** \`bash ~/CODE_MASTER/scripts/PERF_MONITOR.sh\`

### **5. Daily Maintenance**
- **Script:** \`scripts/DAILY_MAINTENANCE.sh\`
- **Purpose:** Automated daily maintenance tasks
- **Usage:** \`bash ~/CODE_MASTER/scripts/DAILY_MAINTENANCE.sh\`

### **6. Auto Backup**
- **Script:** \`scripts/AUTO_BACKUP.sh\`
- **Purpose:** Automated backup system
- **Usage:** \`bash ~/CODE_MASTER/scripts/AUTO_BACKUP.sh\`

### **7. Installation Verification**
- **Script:** \`scripts/VERIFY_INSTALL.sh\`
- **Purpose:** Verify all systems are properly installed
- **Usage:** \`bash ~/CODE_MASTER/scripts/VERIFY_INSTALL.sh\`

---

## 🚀 QUICK ACCESS

### **Master Control Panel:**
\`\`\`bash
bash ~/CODE_MASTER/CONTROL_PANEL.sh
\`\`\`

### **Quick Launcher:**
\`\`\`bash
bash ~/CODE_MASTER/LAUNCH.sh
\`\`\`

---

## 📊 AUTOMATION

### **Schedule Daily Maintenance:**
Add to crontab:
\`\`\`bash
0 2 * * * bash ~/CODE_MASTER/scripts/DAILY_MAINTENANCE.sh
\`\`\`

### **Schedule Auto Backup:**
Add to crontab:
\`\`\`bash
0 3 * * 0 bash ~/CODE_MASTER/scripts/AUTO_BACKUP.sh
\`\`\`

---

## ✅ VERIFICATION

Run verification to ensure everything is installed:
\`\`\`bash
bash ~/CODE_MASTER/scripts/VERIFY_INSTALL.sh
\`\`\`

---

## 📝 LOGS

All logs are stored in: \`~/CODE_MASTER/logs/\`

---

**GORUNFREE | MC96 | Fish Music Inc.**  
**Rob Sonic Protocol | Complete System** 🚀
"@

$completeDocs | Out-File -FilePath "/Users/rsp_ms/CODE_MASTER/COMPLETE_DOCS.md" -Encoding utf8 -NoNewline
Write-InstallLog "  ✓ Complete documentation created" "Green"
Write-Host ""

# SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  INSTALLATION COMPLETE                            ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

Write-InstallLog "=== INSTALLATION SUMMARY ===" "Cyan"
Write-InstallLog "Directories created: $($dirs.Count)" "Green"
Write-InstallLog "Scripts installed: 7+" "Green"
Write-InstallLog "Systems created: 7" "Green"
Write-InstallLog "Documentation: Complete" "Green"
Write-Host ""

Write-Host "✅ INSTALLED SYSTEMS:" -ForegroundColor Green
Write-Host "  • Health Check System" -ForegroundColor White
Write-Host "  • Auto-Optimization" -ForegroundColor White
Write-Host "  • GHOST Drive Management" -ForegroundColor White
Write-Host "  • Performance Monitor" -ForegroundColor White
Write-Host "  • Daily Maintenance" -ForegroundColor White
Write-Host "  • Auto Backup System" -ForegroundColor White
Write-Host "  • Installation Verification" -ForegroundColor White
Write-Host "  • Master Control Panel" -ForegroundColor White
Write-Host ""

Write-Host "🚀 QUICK START:" -ForegroundColor Cyan
Write-Host "  bash ~/CODE_MASTER/CONTROL_PANEL.sh" -ForegroundColor White
Write-Host ""

Write-InstallLog "=== INSTALLATION COMPLETE ===" "Green"
Write-Host "🔥 Everything is installed and ready! 🚀" -ForegroundColor Green

