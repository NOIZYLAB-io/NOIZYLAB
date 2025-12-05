#!/bin/bash
# Setup Google Account Emails for NoizyLab
# ========================================

BASE="/Users/m2ultra/NOIZYLAB/email-intelligence"

echo "📧 Setting Up Google Account Emails"
echo "===================================="
echo ""

cd "$BASE"

# Import emails
echo "📥 Importing emails..."
python3 google-account-manager.py

echo ""
echo "✅ Google Account emails setup complete!"
echo ""
echo "📋 Next Steps:"
echo "   1. Review imported emails"
echo "   2. Configure email sending for each address"
echo "   3. Set up email routing (Cloudflare)"
echo "   4. Integrate with email intelligence system"
echo ""

