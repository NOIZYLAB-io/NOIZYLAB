#!/bin/bash
# Quick setup script for Gmail automation

echo "🤖 Gmail Automation Setup"
echo "========================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

# Install Selenium
echo "📦 Installing Selenium..."
pip3 install selenium

# Check ChromeDriver
if ! command -v chromedriver &> /dev/null; then
    echo ""
    echo "⚠️  ChromeDriver is not installed"
    echo "Install it with:"
    echo "  brew install chromedriver"
    echo ""
    echo "Or download from: https://chromedriver.chromium.org/"
else
    echo "✅ ChromeDriver is installed"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Run the automation with:"
echo "  python3 automate_gmail_setup.py"

