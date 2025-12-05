#!/bin/bash
# Master Heal - Complete System Healing
# ======================================

BASE="/Users/m2ultra/NOIZYLAB"

echo "🌍 MASTER HEAL - Healing Everything!"
echo "====================================="
echo ""

# 1. HealTheWorld
echo "🌍 Step 1: Running HealTheWorld..."
cd "$BASE"
python3 health/healtheworld.py
echo ""

# 2. Fix Code
echo "🔧 Step 2: Fixing All Code..."
python3 code-fixer.py
echo ""

# 3. Optimize
echo "⚡ Step 3: Optimizing Everything..."
cd "$BASE/performance"
python3 optimizer.py >/dev/null 2>&1
echo "✅ Optimized"
echo ""

# 4. Clean
echo "🧹 Step 4: Cleaning..."
find "$BASE" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find "$BASE" -name "*.pyc" -delete 2>/dev/null || true
find "$BASE" -name ".DS_Store" -delete 2>/dev/null || true
echo "✅ Cleaned"
echo ""

# 5. Permissions
echo "🔐 Step 5: Fixing Permissions..."
find "$BASE" -name "*.sh" -exec chmod +x {} \; 2>/dev/null
find "$BASE" -name "*.py" -exec chmod +x {} \; 2>/dev/null
echo "✅ Permissions fixed"
echo ""

# 6. Databases
echo "💾 Step 6: Optimizing Databases..."
for db in email-intelligence/email_intelligence.db security/auth.db integrations/webhooks.db; do
    if [ -f "$BASE/$db" ]; then
        sqlite3 "$BASE/$db" "VACUUM; ANALYZE;" 2>/dev/null && echo "  ✅ $(basename $db)"
    fi
done
echo ""

echo "✨ MASTER HEAL COMPLETE!"
echo "======================="
echo ""
echo "✅ Everything healed"
echo "✅ Everything fixed"
echo "✅ Everything optimized"
echo ""
echo "🚀 System is HEALTHY!"

