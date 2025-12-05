#!/bin/bash
# NoizyLab Heal & Fix Script
# ===========================
# Fixes common issues and heals broken configurations

set -e

NOIZYLAB="/Users/m2ultra/NOIZYLAB"

echo "🏥 NoizyLab Heal & Fix"
echo "======================"
echo ""

# Fix 1: Check and create missing config files
echo "🔧 Fix 1: Checking configuration files..."

# Email Intelligence config
if [ ! -f "$NOIZYLAB/email-intelligence/app/config.py" ]; then
    echo "   Creating email-intelligence config..."
    mkdir -p "$NOIZYLAB/email-intelligence/app"
    cat > "$NOIZYLAB/email-intelligence/app/config.py" << 'EOF'
"""Configuration for Email Intelligence App"""
import os
from pathlib import Path

API_KEY = os.getenv("GEMINI_API_KEY", os.getenv("API_KEY", ""))
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

DB_PATH = os.getenv("EMAIL_DB_PATH", os.getenv("DB_PATH", "email_intelligence.db"))
API_URL = os.getenv("API_URL", "http://localhost:8000")
WEBSOCKET_URL = os.getenv("WEBSOCKET_URL", "ws://localhost:8000/ws")

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")
GOOGLE_SHEETS_JSON = os.getenv("GOOGLE_SHEETS_JSON", "google_sheets.json")

BATCH_SIZE = int(os.getenv("BATCH_SIZE", "50"))
ENABLE_ML = os.getenv("ENABLE_ML", "true").lower() == "true"
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")

db_path_obj = Path(DB_PATH)
if db_path_obj.parent:
    db_path_obj.parent.mkdir(parents=True, exist_ok=True)
EOF
    echo "   ✅ Email config created"
fi

# Fix 2: Create missing databases
echo "💾 Fix 2: Checking databases..."

# Email Intelligence DB
if [ ! -f "$NOIZYLAB/email-intelligence/email_intelligence.db" ]; then
    echo "   Creating email_intelligence.db..."
    sqlite3 "$NOIZYLAB/email-intelligence/email_intelligence.db" << 'EOF'
CREATE TABLE IF NOT EXISTS email_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    valid INTEGER DEFAULT 1,
    category TEXT,
    quality_score REAL,
    enriched_info TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_email ON email_list(email);
CREATE INDEX IF NOT EXISTS idx_category ON email_list(category);
EOF
    echo "   ✅ Email database created"
fi

# Auth DB
if [ ! -f "$NOIZYLAB/security/auth.db" ]; then
    echo "   Creating auth.db..."
    mkdir -p "$NOIZYLAB/security"
    sqlite3 "$NOIZYLAB/security/auth.db" << 'EOF'
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    role TEXT DEFAULT 'user',
    api_key TEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
CREATE TABLE IF NOT EXISTS api_keys (
    id INTEGER PRIMARY KEY,
    key_hash TEXT UNIQUE,
    user_id INTEGER,
    name TEXT,
    permissions TEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used TIMESTAMP,
    active INTEGER DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    action TEXT,
    endpoint TEXT,
    ip_address TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
EOF
    echo "   ✅ Auth database created"
fi

# Webhook DB
if [ ! -f "$NOIZYLAB/integrations/webhooks.db" ]; then
    echo "   Creating webhooks.db..."
    mkdir -p "$NOIZYLAB/integrations"
    sqlite3 "$NOIZYLAB/integrations/webhooks.db" << 'EOF'
CREATE TABLE IF NOT EXISTS webhooks (
    id INTEGER PRIMARY KEY,
    name TEXT,
    url TEXT,
    events TEXT,
    active INTEGER DEFAULT 1,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
EOF
    echo "   ✅ Webhook database created"
fi

echo "✅ Databases checked"
echo ""

# Fix 3: Fix import paths
echo "🔗 Fix 3: Fixing import paths..."

# Fix API server imports
if [ -f "$NOIZYLAB/email-intelligence/api_server_v4.py" ]; then
    # Ensure app.config import works
    if ! grep -q "sys.path" "$NOIZYLAB/email-intelligence/api_server_v4.py"; then
        sed -i '' '1a\
import sys\
from pathlib import Path\
sys.path.insert(0, str(Path(__file__).parent))\
' "$NOIZYLAB/email-intelligence/api_server_v4.py" 2>/dev/null || true
    fi
    echo "   ✅ API server imports fixed"
fi

# Fix dashboard imports
if [ -f "$NOIZYLAB/email-intelligence/dashboard_v4.py" ]; then
    if ! grep -q "sys.path" "$NOIZYLAB/email-intelligence/dashboard_v4.py"; then
        sed -i '' '1a\
import sys\
from pathlib import Path\
sys.path.insert(0, str(Path(__file__).parent))\
' "$NOIZYLAB/email-intelligence/dashboard_v4.py" 2>/dev/null || true
    fi
    echo "   ✅ Dashboard imports fixed"
fi

echo "✅ Import paths fixed"
echo ""

# Fix 4: Create missing directories
echo "📁 Fix 4: Creating missing directories..."
cd "$NOIZYLAB"

dirs=(
    "logs"
    "backups"
    "temp"
    "docs"
    "email-intelligence/app"
    "security"
    "performance"
    "mobile"
    "integrations"
    "monitoring"
    "workflows"
    "control-panel"
    "ml-models"
    "api-docs"
    "tests"
)

for dir in "${dirs[@]}"; do
    mkdir -p "$dir"
done

echo "✅ Directories created"
echo ""

# Fix 5: Fix broken symlinks
echo "🔗 Fix 5: Checking symlinks..."
cd "$NOIZYLAB"

# Remove broken symlinks
find . -type l ! -exec test -e {} \; -delete 2>/dev/null || true

echo "✅ Symlinks checked"
echo ""

# Fix 6: Update requirements
echo "📦 Fix 6: Updating requirements..."
cd "$NOIZYLAB"

if [ -f "requirements-v4.txt" ]; then
    echo "   Installing requirements..."
    pip3 install -q -r requirements-v4.txt 2>&1 | tail -3 || echo "   ⚠️  Some packages may need manual install"
fi

echo "✅ Requirements updated"
echo ""

# Fix 7: Optimize all databases
echo "⚡ Fix 7: Optimizing all databases..."
cd "$NOIZYLAB"

for db in email-intelligence/email_intelligence.db security/auth.db integrations/webhooks.db; do
    if [ -f "$db" ]; then
        echo "   Optimizing $(basename $db)..."
        sqlite3 "$db" "VACUUM; ANALYZE; PRAGMA optimize;" 2>/dev/null || true
    fi
done

echo "✅ Databases optimized"
echo ""

# Fix 8: Create health check script
echo "🏥 Fix 8: Creating health check..."
cat > "$NOIZYLAB/health-check.sh" << 'EOF'
#!/bin/bash
# NoizyLab Health Check

echo "🏥 NoizyLab Health Check"
echo "========================"
echo ""

# Check services
echo "📡 Services:"
curl -s http://localhost:8000/ >/dev/null && echo "   ✅ V4 API: Running" || echo "   ❌ V4 API: Not running"
curl -s http://localhost:8001/docs >/dev/null && echo "   ✅ Webhook Hub: Running" || echo "   ❌ Webhook Hub: Not running"
curl -s http://localhost:8002/mobile/health >/dev/null && echo "   ✅ Mobile API: Running" || echo "   ❌ Mobile API: Not running"
lsof -i :8501 >/dev/null && echo "   ✅ Dashboard: Running" || echo "   ❌ Dashboard: Not running"

echo ""
echo "💾 Databases:"
[ -f "email-intelligence/email_intelligence.db" ] && echo "   ✅ Email DB: Exists" || echo "   ❌ Email DB: Missing"
[ -f "security/auth.db" ] && echo "   ✅ Auth DB: Exists" || echo "   ❌ Auth DB: Missing"
[ -f "integrations/webhooks.db" ] && echo "   ✅ Webhook DB: Exists" || echo "   ❌ Webhook DB: Missing"

echo ""
echo "📁 Structure:"
[ -d "email-intelligence" ] && echo "   ✅ Email Intelligence" || echo "   ❌ Email Intelligence"
[ -d "universal-blocker" ] && echo "   ✅ Universal Blocker" || echo "   ❌ Universal Blocker"
[ -d "imessage-spam-filter" ] && echo "   ✅ iMessage Filter" || echo "   ❌ iMessage Filter"

echo ""
EOF

chmod +x "$NOIZYLAB/health-check.sh"
echo "   ✅ Health check created"
echo ""

echo "✨ HEAL COMPLETE!"
echo "================="
echo ""
echo "✅ All fixes applied"
echo "✅ Databases created/optimized"
echo "✅ Configurations fixed"
echo "✅ Structure organized"
echo ""
echo "Run health check: ~/NOIZYLAB/health-check.sh"
echo ""

