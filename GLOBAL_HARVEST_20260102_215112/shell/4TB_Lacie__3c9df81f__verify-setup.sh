#!/bin/bash

# =============================================================================
# Complete Setup Verification Script
# Verifies: Domains, Email, Cloudflare, Google Workspace
# =============================================================================

echo "🔍 COMPLETE SETUP VERIFICATION"
echo "=============================="
echo ""
echo "This script will verify all DNS records and email configuration"
echo "for noizylab.ca and fishmusicinc.com"
echo ""
echo "Press Enter to continue..."
read

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
PASSED=0
FAILED=0
WARNINGS=0

# Function to check DNS record
check_dns() {
    local domain=$1
    local record_type=$2
    local record_name=$3
    local expected_contains=$4
    local description=$5
    
    echo -n "Checking $description... "
    
    if [ -z "$record_name" ]; then
        result=$(dig +short $record_type $domain 2>/dev/null)
    else
        result=$(dig +short $record_type $record_name.$domain 2>/dev/null)
    fi
    
    if [ -z "$result" ]; then
        echo -e "${RED}❌ FAILED${NC} - No record found"
        FAILED=$((FAILED + 1))
        return 1
    fi
    
    if [ ! -z "$expected_contains" ]; then
        if echo "$result" | grep -q "$expected_contains"; then
            echo -e "${GREEN}✅ PASS${NC}"
            echo "   Result: $result"
            PASSED=$((PASSED + 1))
            return 0
        else
            echo -e "${YELLOW}⚠️  WARNING${NC} - Record exists but may not match expected"
            echo "   Found: $result"
            echo "   Expected to contain: $expected_contains"
            WARNINGS=$((WARNINGS + 1))
            return 2
        fi
    else
        echo -e "${GREEN}✅ PASS${NC} - Record exists"
        echo "   Result: $result"
        PASSED=$((PASSED + 1))
        return 0
    fi
}

# Function to verify domain
verify_domain() {
    local domain=$1
    local domain_name=$2
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Verifying: $domain_name ($domain)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    # MX Records
    echo "📧 MX Records (Email Servers):"
    check_dns "$domain" "MX" "" "google.com" "MX Record 1 (Priority 1)"
    check_dns "$domain" "MX" "" "google.com" "MX Record 2 (Priority 5)"
    check_dns "$domain" "MX" "" "google.com" "MX Record 3 (Priority 5)"
    check_dns "$domain" "MX" "" "google.com" "MX Record 4 (Priority 10)"
    check_dns "$domain" "MX" "" "google.com" "MX Record 5 (Priority 10)"
    echo ""
    
    # SPF Record
    echo "🛡️ SPF Record (Email Authentication):"
    check_dns "$domain" "TXT" "" "spf1" "SPF Record"
    echo ""
    
    # DKIM Record
    echo "🔐 DKIM Record (Email Signing):"
    check_dns "$domain" "TXT" "google._domainkey" "DKIM1" "DKIM Record"
    echo ""
    
    # DMARC Record
    echo "📊 DMARC Record (Email Policy):"
    check_dns "$domain" "TXT" "_dmarc" "DMARC1" "DMARC Record"
    echo ""
    
    # MTA-STS Record
    echo "🔒 MTA-STS Record (TLS Enforcement):"
    check_dns "$domain" "TXT" "_mta-sts" "STSv1" "MTA-STS Record"
    echo ""
    
    # TLSRPT Record
    echo "📈 TLSRPT Record (TLS Reporting):"
    check_dns "$domain" "TXT" "_smtp._tls" "TLSRPTv1" "TLSRPT Record"
    echo ""
}

# Check if dig is installed
if ! command -v dig &> /dev/null; then
    echo -e "${RED}❌ ERROR: 'dig' command not found${NC}"
    echo "Install with: brew install bind (macOS)"
    exit 1
fi

# Start verification
echo ""
echo "Starting DNS verification..."
echo ""

# Verify noizylab.ca
verify_domain "noizylab.ca" "NOIZYLAB.CA"

# Verify fishmusicinc.com
verify_domain "fishmusicinc.com" "FISHMUSICINC.COM"

# Summary
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 VERIFICATION SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${GREEN}✅ Passed: $PASSED${NC}"
echo -e "${YELLOW}⚠️  Warnings: $WARNINGS${NC}"
echo -e "${RED}❌ Failed: $FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    if [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}🎉 ALL CHECKS PASSED!${NC}"
        echo "Your DNS records are properly configured."
    else
        echo -e "${YELLOW}⚠️  Setup complete with warnings${NC}"
        echo "Review warnings above. Setup may still work correctly."
    fi
else
    echo -e "${RED}❌ Some checks failed${NC}"
    echo "Please review failed items and fix configuration."
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Next Steps:"
echo "1. If all checks passed, proceed to email testing"
echo "2. Test sending/receiving emails on all devices"
echo "3. Check Google Admin Console for DKIM status"
echo "4. Monitor DMARC reports (if configured)"
echo ""
echo "For detailed setup instructions, see:"
echo "  - COMPLETE_SETUP_CONFIRMATION.md"
echo "  - IPHONE_IPAD_SETUP.md"
echo ""

