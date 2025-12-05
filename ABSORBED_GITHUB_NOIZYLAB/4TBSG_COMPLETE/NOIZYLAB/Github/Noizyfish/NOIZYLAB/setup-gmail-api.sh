#!/bin/bash
# Gmail API Setup Helper
# ======================

echo "📧 Gmail API Setup for NoizyLab CORE v3.0"
echo "=========================================="
echo ""

cd ~/NOIZYLAB/email-intelligence

# Check if credentials file exists
if [ -f "config/gmail_credentials.json" ]; then
    echo "✅ Gmail credentials file found!"
    echo ""
    echo "To complete setup:"
    echo "1. Run: python3 main.py"
    echo "2. Select option 2 (Inbox Scanner)"
    echo "3. Browser will open for authentication"
    echo "4. Grant permissions"
    echo ""
else
    echo "⚠️  Gmail credentials file not found."
    echo ""
    echo "📋 Setup Steps:"
    echo ""
    echo "1. Go to Google Cloud Console:"
    echo "   https://console.cloud.google.com/"
    echo ""
    echo "2. Create a new project (or select existing)"
    echo ""
    echo "3. Enable Gmail API:"
    echo "   - Go to 'APIs & Services' > 'Library'"
    echo "   - Search for 'Gmail API'"
    echo "   - Click 'Enable'"
    echo ""
    echo "4. Create OAuth 2.0 Credentials:"
    echo "   - Go to 'APIs & Services' > 'Credentials'"
    echo "   - Click 'Create Credentials' > 'OAuth client ID'"
    echo "   - Application type: 'Desktop app'"
    echo "   - Name: 'NoizyLab Email Intelligence'"
    echo "   - Click 'Create'"
    echo ""
    echo "5. Download credentials:"
    echo "   - Click 'Download JSON'"
    echo "   - Save as: config/gmail_credentials.json"
    echo ""
    echo "6. Run this script again or launch the app!"
    echo ""
fi

echo "💡 Quick Setup (if you have credentials):"
echo "   cp /path/to/credentials.json config/gmail_credentials.json"
echo ""

