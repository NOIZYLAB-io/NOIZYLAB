#!/bin/bash

# =============================================================================
# Email Functionality Test Script
# Tests email send/receive capabilities
# =============================================================================

echo "📧 EMAIL FUNCTIONALITY TEST"
echo "==========================="
echo ""
echo "This script tests email connectivity and configuration"
echo ""

# Check if required tools are installed
check_tool() {
    if ! command -v $1 &> /dev/null; then
        echo "⚠️  $1 not found. Install with: brew install $1"
        return 1
    fi
    return 0
}

echo "Checking required tools..."
check_tool "telnet" || echo "  (telnet optional for connectivity test)"
check_tool "curl" || echo "  (curl optional for web tests)"
echo ""

# Test SMTP connectivity
test_smtp() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📤 Testing SMTP (Outgoing Email) Connectivity"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    echo "Testing smtp.gmail.com:587 (STARTTLS)..."
    if timeout 5 bash -c "echo > /dev/tcp/smtp.gmail.com/587" 2>/dev/null; then
        echo "✅ Port 587 is accessible"
    else
        echo "❌ Cannot connect to port 587"
        echo "   Check firewall settings"
    fi
    
    echo ""
    echo "Testing smtp.gmail.com:465 (SSL)..."
    if timeout 5 bash -c "echo > /dev/tcp/smtp.gmail.com/465" 2>/dev/null; then
        echo "✅ Port 465 is accessible"
    else
        echo "❌ Cannot connect to port 465"
    fi
    
    echo ""
}

# Test IMAP connectivity
test_imap() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📥 Testing IMAP (Incoming Email) Connectivity"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    echo "Testing imap.gmail.com:993 (SSL)..."
    if timeout 5 bash -c "echo > /dev/tcp/imap.gmail.com/993" 2>/dev/null; then
        echo "✅ Port 993 is accessible"
    else
        echo "❌ Cannot connect to port 993"
        echo "   Check firewall settings"
    fi
    
    echo ""
}

# Test DNS resolution
test_dns() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🌐 Testing DNS Resolution"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    echo "Testing smtp.gmail.com..."
    if host smtp.gmail.com &>/dev/null; then
        echo "✅ smtp.gmail.com resolves"
        host smtp.gmail.com | head -1
    else
        echo "❌ Cannot resolve smtp.gmail.com"
    fi
    
    echo ""
    echo "Testing imap.gmail.com..."
    if host imap.gmail.com &>/dev/null; then
        echo "✅ imap.gmail.com resolves"
        host imap.gmail.com | head -1
    else
        echo "❌ Cannot resolve imap.gmail.com"
    fi
    
    echo ""
}

# Manual test instructions
manual_tests() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📝 Manual Email Tests Required"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Please perform these manual tests:"
    echo ""
    echo "1. SEND TEST EMAIL:"
    echo "   - From: rsp@noizylab.ca"
    echo "   - To: Your personal email (Gmail, Outlook, etc.)"
    echo "   - Subject: Test Email from noizylab.ca"
    echo "   - Check: Email arrives in inbox"
    echo "   - Check: In Gmail, click 'Show original' → Verify SPF/DKIM/DMARC pass"
    echo ""
    echo "2. SEND TEST EMAIL:"
    echo "   - From: rp@fishmusicinc.com"
    echo "   - To: Your personal email"
    echo "   - Subject: Test Email from fishmusicinc.com"
    echo "   - Check: Email arrives in inbox"
    echo "   - Check: Authentication passes"
    echo ""
    echo "3. RECEIVE TEST EMAIL:"
    echo "   - Send email TO: rsp@noizylab.ca"
    echo "   - From: Your personal email"
    echo "   - Check: Email arrives in inbox on all devices"
    echo ""
    echo "4. RECEIVE TEST EMAIL:"
    echo "   - Send email TO: rp@fishmusicinc.com"
    echo "   - From: Your personal email"
    echo "   - Check: Email arrives in inbox on all devices"
    echo ""
    echo "5. TEST ON ALL DEVICES:"
    echo "   - iPhone: Send/receive test"
    echo "   - iPad: Send/receive test"
    echo "   - macOS: Send/receive test"
    echo "   - Other devices: Send/receive test"
    echo ""
}

# Run tests
test_dns
test_smtp
test_imap
manual_tests

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Connectivity tests complete"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Next: Perform manual email tests above"
echo ""

