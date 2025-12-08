#!/bin/bash
# Setup All Email Clients - Complete Email Setup
# ==============================================

BASE="/Users/m2ultra/NOIZYLAB/email-intelligence"

echo "📧 Setting Up All Email Clients"
echo "================================"
echo ""

cd "$BASE"

# 1. Generate iOS configs
echo "📱 Step 1: Generating iOS configurations..."
python3 setup-ios-emails.py
echo "✅ iOS configs ready"
echo ""

# 2. Generate MacMail scripts
echo "💻 Step 2: Generating MacMail scripts..."
python3 setup-macmail.py
echo "✅ MacMail scripts ready"
echo ""

# 3. Generate Outlook configs
echo "📮 Step 3: Generating Outlook configurations..."
python3 setup-outlook.py
echo "✅ Outlook configs ready"
echo ""

# 4. Setup Xcode
echo "🔧 Step 4: Setting up Xcode..."
./setup-xcode-ios.sh
echo "✅ Xcode ready"
echo ""

echo "✨ ALL EMAIL CLIENTS SETUP COMPLETE!"
echo "===================================="
echo ""
echo "📋 Available Configurations:"
echo "   • iOS: ios-configs/"
echo "   • MacMail: macmail-scripts/"
echo "   • Outlook: outlook-configs/"
echo ""
echo "🚀 Ready to configure all your email clients!"

