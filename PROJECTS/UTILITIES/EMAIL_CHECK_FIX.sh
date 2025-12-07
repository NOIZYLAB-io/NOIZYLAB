#!/bin/bash
# ============================================
# EMAIL CHECK & FIX - GORUNFREE
# Run on GOD or DaFixer
# ============================================

echo "=========================================="
echo "EMAIL DIAGNOSTIC - $(date)"
echo "=========================================="

DOMAINS=("noizyfish.com" "noizylab.ca" "fishmusicinc.com")

for DOMAIN in "${DOMAINS[@]}"; do
    echo ""
    echo "==========> $DOMAIN <=========="
    
    echo ""
    echo "[MX RECORDS]"
    MX=$(dig +short MX $DOMAIN 2>/dev/null)
    if [ -z "$MX" ]; then
        echo "  ❌ NO MX RECORDS - EMAIL BROKEN"
    else
        echo "$MX" | while read line; do echo "  $line"; done
    fi
    
    echo ""
    echo "[NAMESERVERS]"
    NS=$(dig +short NS $DOMAIN 2>/dev/null)
    if [ -z "$NS" ]; then
        echo "  ❌ NO NS RECORDS - DOMAIN NOT RESOLVING"
    else
        echo "$NS" | while read line; do echo "  $line"; done
        
        # Check if Cloudflare
        if echo "$NS" | grep -q "cloudflare"; then
            echo "  ✅ Using Cloudflare DNS"
        else
            echo "  ⚠️  NOT on Cloudflare - move DNS to CF for email routing"
        fi
    fi
    
    echo ""
    echo "[SPF RECORD]"
    SPF=$(dig +short TXT $DOMAIN 2>/dev/null | grep "v=spf1")
    if [ -z "$SPF" ]; then
        echo "  ❌ NO SPF - emails may go to spam"
    else
        echo "  $SPF"
    fi
    
    echo ""
    echo "[A RECORD]"
    A=$(dig +short A $DOMAIN 2>/dev/null)
    if [ -z "$A" ]; then
        echo "  ❌ NO A RECORD"
    else
        echo "  $A"
    fi
    
done

echo ""
echo "=========================================="
echo "DIAGNOSIS & FIX INSTRUCTIONS"
echo "=========================================="
echo ""
echo "FOR CLOUDFLARE EMAIL ROUTING TO WORK:"
echo ""
echo "1. Domain must use Cloudflare nameservers"
echo "2. Add these MX records in Cloudflare DNS:"
echo "   Priority 5  -> route1.mx.cloudflare.net"
echo "   Priority 10 -> route2.mx.cloudflare.net"
echo "   Priority 20 -> route3.mx.cloudflare.net"
echo ""
echo "3. Add SPF TXT record:"
echo "   v=spf1 include:_spf.mx.cloudflare.net ~all"
echo ""
echo "4. In Cloudflare Dashboard -> Email -> Email Routing:"
echo "   - Enable Email Routing"
echo "   - Add destination: rsplowman@icloud.com"
echo "   - Create routing rules for each address"
echo ""
echo "=========================================="
echo "QUICK GMAIL CHECK"
echo "=========================================="
echo ""
echo "For rsplowman@gmail.com issues:"
echo "1. Check spam folder"
echo "2. Check Promotions/Updates tabs"
echo "3. Go to: https://accounts.google.com/signin/recovery"
echo ""
echo "=========================================="
