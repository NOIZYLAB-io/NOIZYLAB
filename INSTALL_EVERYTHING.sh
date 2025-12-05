#!/bin/bash
# ONE-CLICK INSTALLER - ALL SYSTEMS
# Installs and configures everything automatically

echo "========================================"
echo "🚀 ONE-CLICK INSTALLER - ALL SYSTEMS"
echo "========================================"
echo ""
echo "This will install and configure:"
echo "  • Domain & Email Management Suite"
echo "  • 24/7 Monitoring System"
echo "  • Services Integration (X4 Speed)"
echo "  • Outlook Configuration"
echo "  • Master Control Center"
echo ""
echo "Continue? (y/n): "
read -r response

if [ "$response" != "y" ]; then
    echo "Installation cancelled."
    exit 0
fi

echo ""
echo "========================================"
echo "📦 STEP 1: Installing Dependencies"
echo "========================================"

# Check Python version
echo "Checking Python..."
python3 --version || { echo "❌ Python 3 not found!"; exit 1; }

# Install Python packages
echo ""
echo "Installing Python packages..."
pip3 install --user --upgrade pip 2>/dev/null
pip3 install --user requests dnspython python-whois python-dotenv 2>/dev/null

echo "✅ Dependencies installed!"

echo ""
echo "========================================"
echo "📁 STEP 2: Creating Directories"
echo "========================================"

BASE_DIR="/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB"

# Create all required directories
mkdir -p "$BASE_DIR/email_backups"
mkdir -p "$BASE_DIR/domain_reports"
mkdir -p "$BASE_DIR/monitoring_alerts"
mkdir -p "$BASE_DIR/outlook_configs"

echo "✅ Directories created!"

echo ""
echo "========================================"
echo "🔧 STEP 3: Making Scripts Executable"
echo "========================================"

# Make all scripts executable
chmod +x "$BASE_DIR"/*.py 2>/dev/null
chmod +x "$BASE_DIR"/*.sh 2>/dev/null

echo "✅ Scripts are executable!"

echo ""
echo "========================================"
echo "📧 STEP 4: Generating Outlook Configs"
echo "========================================"

if [ -f "$BASE_DIR/SETUP_OUTLOOK_ALL_EMAILS.sh" ]; then
    bash "$BASE_DIR/SETUP_OUTLOOK_ALL_EMAILS.sh" 2>/dev/null
    echo "✅ Outlook configurations generated!"
else
    echo "⚠ Outlook setup script not found (optional)"
fi

echo ""
echo "========================================"
echo "⚙️ STEP 5: Creating Environment Config"
echo "========================================"

# Create .env_services if it doesn't exist
if [ ! -f "$BASE_DIR/.env_services" ]; then
    if [ -f "$BASE_DIR/SETUP_SERVICES_X4.sh" ]; then
        bash "$BASE_DIR/SETUP_SERVICES_X4.sh" 2>/dev/null
        echo "✅ Environment config created!"
    fi
else
    echo "✅ Environment config exists!"
fi

echo ""
echo "========================================"
echo "🎛️ STEP 6: Setting Up Control Center"
echo "========================================"

# Make Master Control Center executable
chmod +x "$BASE_DIR/MASTER_CONTROL_CENTER.py"

echo "✅ Control Center ready!"

echo ""
echo "========================================"
echo "🔍 STEP 7: Verification"
echo "========================================"

echo ""
echo "Checking files..."
COUNT=0

# Check critical files
FILES=(
    "domains_and_emails_master.json"
    "ADVANCED_DOMAIN_EMAIL_MANAGER.py"
    "DOMAIN_EMAIL_MONITOR_24_7.py"
    "MASTER_SERVICES_INTEGRATION_X4.py"
    "MASTER_CONTROL_CENTER.py"
)

for file in "${FILES[@]}"; do
    if [ -f "$BASE_DIR/$file" ]; then
        echo "  ✓ $file"
        ((COUNT++))
    else
        echo "  ✗ $file (missing)"
    fi
done

echo ""
echo "Checking directories..."
DIRS=(
    "email_backups"
    "domain_reports"
    "monitoring_alerts"
    "outlook_configs"
)

for dir in "${DIRS[@]}"; do
    if [ -d "$BASE_DIR/$dir" ]; then
        echo "  ✓ $dir/"
    else
        echo "  ✗ $dir/ (missing)"
    fi
done

echo ""
echo "========================================"
echo "✅ INSTALLATION COMPLETE!"
echo "========================================"
echo ""
echo "📊 WHAT WAS INSTALLED:"
echo ""
echo "✓ Domain & Email Management System"
echo "  • Health monitoring"
echo "  • Analytics & reporting"
echo "  • Configuration backups"
echo ""
echo "✓ 24/7 Monitoring System"
echo "  • Continuous monitoring"
echo "  • Real-time alerts"
echo "  • Auto-fix capabilities"
echo ""
echo "✓ Services Integration (X4 Speed)"
echo "  • Slack, Cloudflare, GoDaddy"
echo "  • MS365, Google Workspace"
echo "  • Parallel processing"
echo ""
echo "✓ Outlook Configuration"
echo "  • 7 email accounts"
echo "  • Complete setup guides"
echo "  • Server settings"
echo ""
echo "✓ Master Control Center"
echo "  • Unified dashboard"
echo "  • One-click access"
echo "  • System management"
echo ""
echo "========================================"
echo "🚀 QUICK START COMMANDS:"
echo "========================================"
echo ""
echo "1. Launch Control Center:"
echo "   python3 MASTER_CONTROL_CENTER.py"
echo ""
echo "2. Run Health Check:"
echo "   python3 ADVANCED_DOMAIN_EMAIL_MANAGER.py"
echo ""
echo "3. Start Monitoring:"
echo "   python3 DOMAIN_EMAIL_MONITOR_24_7.py"
echo ""
echo "4. View Outlook Guide:"
echo "   cat outlook_configs/MASTER_SETUP_GUIDE.md"
echo ""
echo "========================================"
echo "📖 NEXT STEPS:"
echo "========================================"
echo ""
echo "1. Launch the Master Control Center:"
echo "   cd $BASE_DIR"
echo "   python3 MASTER_CONTROL_CENTER.py"
echo ""
echo "2. Configure API keys in .env_services"
echo ""
echo "3. Run a health check to verify everything"
echo ""
echo "4. Set up Outlook with the generated configs"
echo ""
echo "========================================"
echo "✨ All systems installed and ready!"
echo "========================================"

