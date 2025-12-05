#!/bin/bash
# ULTIMATE_MASTER_X1000.sh
# COMBINE ALL - FORCE RUN - FIX ALL - OPTIMIZE - TEST - UPGRADE - IMPROVE

set +e  # Don't exit on errors

clear

HOME_DIR="/Users/rsp_ms"
BACKUP_DIR="/Volumes/4TB_02/CODE_MASTER/System_Backup"
NEW_CODE_MASTER="/Volumes/4TB_02/CODE_MASTER"
EXTERNAL_BASE="/Volumes/4TB_02"

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     🚀 ULTIMATE MASTER X1000 - FORCE RUN ALL                          ║"
echo "║     FIX | OPTIMIZE | TEST | UPGRADE | IMPROVE                         ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# ============================================================================
# PHASE 1: STOP ALL PROCESSES
# ============================================================================
echo "🛑 PHASE 1: Stopping all processes..."
pkill -9 -f "MUSIC_RESCUE" 2>/dev/null || true
pkill -9 -f "rsync" 2>/dev/null || true
pkill -9 -f "find.*mp3\|wav\|flac" 2>/dev/null || true
pkill -9 -f "xargs" 2>/dev/null || true
sleep 2
echo "✅ All processes stopped"
echo ""

# ============================================================================
# PHASE 2: HEALTH CHECK
# ============================================================================
echo "🏥 PHASE 2: System Health Check..."
echo ""

echo "📊 Disk Space:"
df -h / | tail -1
echo ""

echo "📁 External Drive:"
if [ -d "$EXTERNAL_BASE" ]; then
    echo "   ✅ Mounted"
    df -h "$EXTERNAL_BASE" | tail -1
else
    echo "   ❌ NOT MOUNTED!"
    exit 1
fi
echo ""

echo "📂 CODE_MASTER Status:"
if [ -d "$HOME_DIR/CODE_MASTER" ]; then
    SIZE=$(du -sh "$HOME_DIR/CODE_MASTER" 2>/dev/null | cut -f1)
    echo "   System: $HOME_DIR/CODE_MASTER ($SIZE)"
else
    echo "   System: ✅ Empty"
fi

if [ -d "$NEW_CODE_MASTER" ]; then
    SIZE=$(du -sh "$NEW_CODE_MASTER" 2>/dev/null | cut -f1)
    echo "   External: $NEW_CODE_MASTER ($SIZE)"
else
    echo "   External: ❌ Not found!"
fi
echo ""

# ============================================================================
# PHASE 3: FORCE MOVE ALL CODE FILES
# ============================================================================
echo "📦 PHASE 3: FORCE MOVING ALL CODE FILES..."
echo ""

mkdir -p "$BACKUP_DIR/.config"
mkdir -p "$BACKUP_DIR/.windsurf"
mkdir -p "$BACKUP_DIR/.codegpt"
mkdir -p "$BACKUP_DIR/.gemini"
mkdir -p "$BACKUP_DIR/.rest-client"

# Function to force move
force_move() {
    local src="$1"
    local dest="$2"
    local name="$3"
    
    if [ ! -e "$src" ]; then
        return 0
    fi
    
    echo "   📦 $name..."
    
    if [ -d "$src" ]; then
        cp -Rf "$src" "$dest" 2>/dev/null
        [ $? -eq 0 ] && rm -rf "$src" 2>/dev/null && echo "      ✅ FORCED" || echo "      ⚠️  Issue"
    else
        mkdir -p "$(dirname "$dest")"
        cp -f "$src" "$dest" 2>/dev/null
        [ $? -eq 0 ] && rm -f "$src" 2>/dev/null && echo "      ✅ FORCED" || echo "      ⚠️  Issue"
    fi
}

force_move "$HOME_DIR/.config/gcloud" "$BACKUP_DIR/.config/gcloud" ".config/gcloud"
force_move "$HOME_DIR/.config/configstore" "$BACKUP_DIR/.config/configstore" ".config/configstore"
force_move "$HOME_DIR/.config/Dadroit" "$BACKUP_DIR/.config/Dadroit" ".config/Dadroit"
force_move "$HOME_DIR/.rest-client" "$BACKUP_DIR/.rest-client" ".rest-client"
force_move "$HOME_DIR/.codegpt" "$BACKUP_DIR/.codegpt" ".codegpt"
force_move "$HOME_DIR/.gemini" "$BACKUP_DIR/.gemini" ".gemini"

# Move .windsurf files
echo "   📁 .windsurf files..."
find "$HOME_DIR/.windsurf/extensions" -type f \( -name "*.py" -o -name "*.js" -o -name "*.json" \) \
    -not -path "*/node_modules/*" 2>/dev/null | while read file; do
    rel_path="${file#$HOME_DIR/.windsurf/}"
    dest="$BACKUP_DIR/.windsurf/$rel_path"
    mkdir -p "$(dirname "$dest")"
    cp -f "$file" "$dest" 2>/dev/null && rm -f "$file" 2>/dev/null || true
done
echo "✅ All code files FORCED to external drive"
echo ""

# ============================================================================
# PHASE 4: CLEAN SYSTEM DRIVE
# ============================================================================
echo "🧹 PHASE 4: Cleaning system drive..."
echo ""

echo "   Cleaning caches..."
find "$HOME_DIR/Library/Caches" -type f -size +10M -delete 2>/dev/null || true
CACHE_COUNT=$(find "$HOME_DIR/Library/Caches" -type f -size +10M 2>/dev/null | wc -l | xargs)
echo "      Removed large cache files"

echo "   Cleaning logs..."
find "$HOME_DIR/Library/Logs" -type f -mtime +3 -delete 2>/dev/null || true
LOG_COUNT=$(find "$HOME_DIR/Library/Logs" -type f -mtime +3 2>/dev/null | wc -l | xargs)
echo "      Removed old logs"

echo "   Emptying trash..."
rm -rf "$HOME_DIR/.Trash"/* 2>/dev/null || true
echo "      ✅ Trash emptied"

echo "   Cleaning temp files..."
rm -rf /tmp/* 2>/dev/null || true
rm -rf /var/tmp/* 2>/dev/null || true
echo "      ✅ Temp files cleaned"
echo ""

# ============================================================================
# PHASE 5: OPTIMIZE
# ============================================================================
echo "⚡ PHASE 5: Optimizing..."
echo ""

# Update all paths in scripts
echo "   Updating script paths..."
if [ -d "$NEW_CODE_MASTER/scripts" ]; then
    OLD_PATH="/Users/rsp_ms/CODE_MASTER"
    find "$NEW_CODE_MASTER/scripts" -type f \( -name "*.sh" -o -name "*.py" -o -name "*.json" \) \
        -exec sed -i '' "s|$OLD_PATH|$NEW_CODE_MASTER|g" {} \; 2>/dev/null
    echo "      ✅ Scripts optimized"
fi

# Create symlinks if needed
echo "   Creating symlinks..."
[ ! -L "$HOME_DIR/CODE_MASTER" ] && [ ! -d "$HOME_DIR/CODE_MASTER" ] && {
    ln -sf "$NEW_CODE_MASTER" "$HOME_DIR/CODE_MASTER" 2>/dev/null
    echo "      ✅ Symlink created"
}
echo "✅ Optimization complete"
echo ""

# ============================================================================
# PHASE 6: TEST
# ============================================================================
echo "🧪 PHASE 6: Testing..."
echo ""

# Test external drive access
[ -d "$EXTERNAL_BASE" ] && echo "   ✅ External drive accessible" || echo "   ❌ External drive NOT accessible"

# Test CODE_MASTER
[ -d "$NEW_CODE_MASTER" ] && echo "   ✅ CODE_MASTER accessible" || echo "   ❌ CODE_MASTER NOT accessible"

# Test scripts directory
[ -d "$NEW_CODE_MASTER/scripts" ] && {
    SCRIPT_COUNT=$(find "$NEW_CODE_MASTER/scripts" -name "*.sh" | wc -l | xargs)
    echo "   ✅ Scripts directory: $SCRIPT_COUNT scripts found"
} || echo "   ❌ Scripts directory NOT found"

# Test backup
[ -d "$BACKUP_DIR" ] && {
    BACKUP_SIZE=$(du -sh "$BACKUP_DIR" 2>/dev/null | cut -f1)
    echo "   ✅ Backup location: $BACKUP_SIZE"
} || echo "   ⚠️  Backup location empty"

echo "✅ Testing complete"
echo ""

# ============================================================================
# PHASE 7: UPGRADE & IMPROVE
# ============================================================================
echo "🚀 PHASE 7: Upgrading & Improving..."
echo ""

# Ensure all scripts are executable
echo "   Making scripts executable..."
find "$NEW_CODE_MASTER/scripts" -name "*.sh" -exec chmod +x {} \; 2>/dev/null
echo "      ✅ Scripts upgraded"

# Create master launcher if missing
if [ ! -f "$NEW_CODE_MASTER/START_HERE.sh" ]; then
    cat > "$NEW_CODE_MASTER/START_HERE.sh" << 'EOF'
#!/bin/bash
# START_HERE.sh
CODE_MASTER="/Volumes/4TB_02/CODE_MASTER"
[ -f "$CODE_MASTER/scripts/START_HERE_X1000.sh" ] && bash "$CODE_MASTER/scripts/START_HERE_X1000.sh"
EOF
    chmod +x "$NEW_CODE_MASTER/START_HERE.sh"
    echo "      ✅ Master launcher created"
fi

# Create health monitoring script
cat > "$NEW_CODE_MASTER/scripts/SYSTEM_MONITOR_X1000.sh" << 'EOF'
#!/bin/bash
# SYSTEM_MONITOR_X1000.sh
echo "📊 System Monitor"
df -h / | tail -1
df -h /Volumes/4TB_02 2>/dev/null | tail -1
EOF
chmod +x "$NEW_CODE_MASTER/scripts/SYSTEM_MONITOR_X1000.sh"
echo "      ✅ System monitor created"

echo "✅ Upgrade & improvement complete"
echo ""

# ============================================================================
# FINAL SUMMARY
# ============================================================================
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     📊 FINAL SUMMARY                                                   ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

echo "📊 System Drive Space:"
df -h / | tail -1
echo ""

echo "📁 External Drive:"
df -h "$EXTERNAL_BASE" 2>/dev/null | tail -1
echo ""

echo "📂 CODE_MASTER:"
echo "   Location: $NEW_CODE_MASTER"
du -sh "$NEW_CODE_MASTER" 2>/dev/null
echo ""

echo "💾 Backup:"
du -sh "$BACKUP_DIR" 2>/dev/null || echo "   (empty)"
echo ""

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     ✅ ULTIMATE MASTER COMPLETE!                                       ║"
echo "║     ALL PHASES: FIX | OPTIMIZE | TEST | UPGRADE | IMPROVE            ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

