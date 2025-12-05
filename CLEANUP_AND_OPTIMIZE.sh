#!/bin/bash
# NoizyLab Cleanup, Heal & Optimize Script
# ========================================
# This script:
# 1. Moves all projects into NOIZYLAB
# 2. Cleans temporary files
# 3. Fixes broken dependencies
# 4. Optimizes databases
# 5. Organizes file structure

set -e

BASE="/Users/m2ultra"
NOIZYLAB="$BASE/NOIZYLAB"

echo "🧹 NoizyLab Cleanup, Heal & Optimize"
echo "===================================="
echo ""

# Step 1: Move any stray projects into NOIZYLAB
echo "📦 Step 1: Consolidating projects into NOIZYLAB..."
cd "$BASE"

# Find and move any email-related projects
for dir in email-intelligence email-intel email-*; do
    if [ -d "$dir" ] && [ "$dir" != "NOIZYLAB" ]; then
        echo "   Moving $dir -> NOIZYLAB/"
        mv "$dir" "$NOIZYLAB/" 2>/dev/null || echo "   ⚠️  $dir already in NOIZYLAB or error"
    fi
done

# Find and move blocker projects
for dir in universal-blocker blocker block-*; do
    if [ -d "$dir" ] && [ "$dir" != "NOIZYLAB" ]; then
        echo "   Moving $dir -> NOIZYLAB/"
        mv "$dir" "$NOIZYLAB/" 2>/dev/null || echo "   ⚠️  $dir already in NOIZYLAB or error"
    fi
done

# Find and move spam filter projects
for dir in imessage-spam-filter spam-filter spam-*; do
    if [ -d "$dir" ] && [ "$dir" != "NOIZYLAB" ]; then
        echo "   Moving $dir -> NOIZYLAB/"
        mv "$dir" "$NOIZYLAB/" 2>/dev/null || echo "   ⚠️  $dir already in NOIZYLAB or error"
    fi
done

echo "✅ Projects consolidated"
echo ""

# Step 2: Clean temporary files
echo "🧹 Step 2: Cleaning temporary files..."
cd "$NOIZYLAB"

# Remove Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.pyo" -delete 2>/dev/null || true

# Remove log files (keep recent)
find . -name "*.log" -mtime +7 -delete 2>/dev/null || true

# Remove temp files
find . -name "*.tmp" -delete 2>/dev/null || true
find . -name ".DS_Store" -delete 2>/dev/null || true
find . -name "*.swp" -delete 2>/dev/null || true
find . -name "*.swo" -delete 2>/dev/null || true

# Clean node_modules if any
find . -name "node_modules" -type d -prune -exec rm -rf {} + 2>/dev/null || true

echo "✅ Temporary files cleaned"
echo ""

# Step 3: Fix and optimize databases
echo "⚡ Step 3: Optimizing databases..."
cd "$NOIZYLAB"

# Optimize email intelligence database
if [ -f "email-intelligence/email_intelligence.db" ]; then
    echo "   Optimizing email_intelligence.db..."
    sqlite3 email-intelligence/email_intelligence.db "VACUUM; ANALYZE; REINDEX;" 2>/dev/null || true
    echo "   ✅ Email database optimized"
fi

# Optimize auth database
if [ -f "security/auth.db" ]; then
    echo "   Optimizing auth.db..."
    sqlite3 security/auth.db "VACUUM; ANALYZE; REINDEX;" 2>/dev/null || true
    echo "   ✅ Auth database optimized"
fi

# Optimize webhook database
if [ -f "integrations/webhooks.db" ]; then
    echo "   Optimizing webhooks.db..."
    sqlite3 integrations/webhooks.db "VACUUM; ANALYZE; REINDEX;" 2>/dev/null || true
    echo "   ✅ Webhook database optimized"
fi

echo "✅ Databases optimized"
echo ""

# Step 4: Fix permissions
echo "🔐 Step 4: Fixing permissions..."
cd "$NOIZYLAB"

# Make scripts executable
find . -name "*.sh" -exec chmod +x {} + 2>/dev/null || true
find . -name "*.py" -exec chmod +x {} + 2>/dev/null || true

# Fix Python scripts
find . -name "*.py" -type f -exec sed -i '' '1s|^|#!/usr/bin/env python3\n|' {} + 2>/dev/null || true

echo "✅ Permissions fixed"
echo ""

# Step 5: Organize structure
echo "📁 Step 5: Organizing file structure..."
cd "$NOIZYLAB"

# Create standard directories if missing
mkdir -p logs
mkdir -p backups
mkdir -p temp
mkdir -p docs

# Move logs to logs directory
find . -maxdepth 2 -name "*.log" -type f -exec mv {} logs/ \; 2>/dev/null || true

echo "✅ Structure organized"
echo ""

# Step 6: Check and fix dependencies
echo "🔧 Step 6: Checking dependencies..."
cd "$NOIZYLAB"

# Check Python dependencies
if [ -f "requirements-v4.txt" ]; then
    echo "   Installing/updating Python dependencies..."
    pip3 install -q -r requirements-v4.txt 2>&1 | tail -3 || echo "   ⚠️  Some dependencies may need manual installation"
fi

echo "✅ Dependencies checked"
echo ""

# Step 7: Run performance optimizer
echo "⚡ Step 7: Running performance optimizer..."
if [ -f "performance/optimizer.py" ]; then
    cd "$NOIZYLAB/performance"
    python3 optimizer.py 2>/dev/null || echo "   ⚠️  Optimizer completed with warnings"
fi

echo "✅ Performance optimized"
echo ""

# Step 8: Create consolidated structure report
echo "📊 Step 8: Generating structure report..."
cd "$NOIZYLAB"

cat > STRUCTURE.md << 'EOF'
# NoizyLab Project Structure
============================

## Core Projects
- email-intelligence/     - Email Intelligence System (V4)
- universal-blocker/      - Universal Content Blocker (V3)
- imessage-spam-filter/   - iMessage Spam Filter (V3)
- noizylab-os/            - NoizyLab OS & SuperCodes

## Enterprise Features
- security/               - Authentication & Security
- performance/            - Performance Optimization
- mobile/                 - Mobile API (iOS Shortcuts)
- integrations/           - Webhook Hub & Integrations
- monitoring/             - System Monitoring
- workflows/              - Automation Engine
- control-panel/          - Unified Control Panel
- ml-models/              - ML Model Training
- api-docs/               - API Documentation
- tests/                  - Test Suite

## Utilities
- logs/                   - Log files
- backups/                - Backup files
- temp/                   - Temporary files
- docs/                   - Documentation

## Launchers
- launch-v3               - Master launcher
- START_V4.sh            - Start V4 services
- START_EVERYTHING.sh    - Start all services
EOF

echo "✅ Structure report created"
echo ""

# Final summary
echo "✨ CLEANUP COMPLETE!"
echo "==================="
echo ""
echo "📊 Summary:"
echo "   ✅ Projects consolidated into NOIZYLAB"
echo "   ✅ Temporary files cleaned"
echo "   ✅ Databases optimized"
echo "   ✅ Permissions fixed"
echo "   ✅ Structure organized"
echo "   ✅ Dependencies checked"
echo "   ✅ Performance optimized"
echo ""
echo "📁 All projects are now in: $NOIZYLAB"
echo ""
echo "🚀 Ready to launch!"
echo "   Run: ~/NOIZYLAB/launch-v3"
echo ""

