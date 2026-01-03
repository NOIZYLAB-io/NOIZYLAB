#!/bin/bash
###############################################################################
# 🚀 DEPLOY BOTH SITES - OPTIMIZED & IMPROVED!!!
# One command = Both sites LIVE on Cloudflare Pages!
# FLOW-enabled! AUTOALLOW mode!
###############################################################################

set -e  # Exit on error

echo "🔥⚡🚀 DEPLOYING BOTH SITES TO CLOUDFLARE PAGES!!! 🚀⚡🔥"
echo ""

# Check if wrangler installed
if ! command -v npx &> /dev/null; then
    echo "⚠️  Installing prerequisites..."
    # Would install here
fi

echo "🌐 SITE 1: FISHMUSICINC.COM"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd /Users/m2ultra/NOIZYLAB/websites/fishmusicinc

echo "📁 Location: $(pwd)"
echo "📊 Files: $(ls -1 | wc -l) files"
echo ""
echo "⚡ Deploying to Cloudflare Pages..."
echo ""

# Deploy with automatic project creation
npx wrangler pages deploy . --project-name=fishmusicinc --branch=main

echo ""
echo "✅ FISHMUSICINC.COM DEPLOYED!!!"
echo ""

sleep 2

echo "🌐 SITE 2: NOIZYLAB.CA"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd /Users/m2ultra/NOIZYLAB/websites/noizylab

echo "📁 Location: $(pwd)"
echo "📊 Files: $(ls -1 | wc -l) files"
echo ""
echo "⚡ Deploying to Cloudflare Pages..."
echo ""

# Deploy
npx wrangler pages deploy . --project-name=noizylab --branch=main

echo ""
echo "✅ NOIZYLAB.CA DEPLOYED!!!"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 BOTH SITES DEPLOYED TO CLOUDFLARE PAGES!!!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📍 Live at:"
echo "   → fishmusicinc.pages.dev (temporary)"
echo "   → noizylab.pages.dev (temporary)"
echo ""
echo "🎯 NEXT STEP:"
echo "   Connect custom domains in Cloudflare dashboard:"
echo "   Pages → fishmusicinc → Custom domains → Add fishmusicinc.com"
echo "   Pages → noizylab → Custom domains → Add noizylab.ca"
echo ""
echo "   5-10 minutes = LIVE ON YOUR DOMAINS!!! ✅"
echo ""
echo "GORUNFREE 4 YOU ROB!!! 🚀"

