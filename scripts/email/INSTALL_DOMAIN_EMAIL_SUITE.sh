#!/bin/bash
# INSTALL ADVANCED DOMAIN & EMAIL MANAGEMENT SUITE

echo "=========================================="
echo "🚀 INSTALLING DOMAIN & EMAIL SUITE"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

# Install required Python packages
echo ""
echo "Installing Python dependencies..."
pip3 install --upgrade pip

pip3 install requests
pip3 install dnspython
pip3 install python-whois
pip3 install python-dotenv

echo ""
echo "✅ Dependencies installed!"
echo ""

# Make scripts executable
echo "Making scripts executable..."
chmod +x "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/ADVANCED_DOMAIN_EMAIL_MANAGER.py"
chmod +x "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/DOMAIN_EMAIL_MONITOR_24_7.py"
chmod +x "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/MASTER_SERVICES_INTEGRATION_X4.py"

echo "✅ Scripts are executable!"
echo ""

# Create required directories
echo "Creating directories..."
mkdir -p "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/email_backups"
mkdir -p "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/domain_reports"
mkdir -p "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/monitoring_alerts"

echo "✅ Directories created!"
echo ""

echo "=========================================="
echo "✅ INSTALLATION COMPLETE!"
echo "=========================================="
echo ""
echo "📚 AVAILABLE COMMANDS:"
echo ""
echo "1. Advanced Domain & Email Manager:"
echo "   python3 ADVANCED_DOMAIN_EMAIL_MANAGER.py"
echo ""
echo "2. 24/7 Monitoring (Quick Check):"
echo "   python3 DOMAIN_EMAIL_MONITOR_24_7.py"
echo ""
echo "3. 24/7 Continuous Monitoring (24 hours):"
echo "   python3 DOMAIN_EMAIL_MONITOR_24_7.py continuous 24"
echo ""
echo "4. Master Services Integration (X4 Speed):"
echo "   source .env_services"
echo "   python3 MASTER_SERVICES_INTEGRATION_X4.py"
echo ""
echo "=========================================="
echo "🎯 Ready to manage your domains & emails!"
echo "=========================================="

