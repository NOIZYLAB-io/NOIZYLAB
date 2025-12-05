#!/bin/bash
# 🚀 FISH MUSIC AI INTEGRATION - QUICK START

clear
echo "🚀 FISH MUSIC AI INTEGRATION - QUICK START"
echo "=========================================="
echo ""

# Check dependencies
echo "📦 Checking dependencies..."
pip3 install requests chromadb --quiet 2>/dev/null
echo "✅ Dependencies ready"
echo ""

# Check API keys
echo "🔑 Checking API keys..."
echo ""

if [ -z "$CLOUDFLARE_API_TOKEN" ]; then
    echo "⚠️  CLOUDFLARE_API_TOKEN not set"
    echo "   Get FREE token at: https://dash.cloudflare.com/profile/api-tokens"
else
    echo "✅ Cloudflare API token found"
fi

if [ -z "$HUGGINGFACE_API_TOKEN" ]; then
    echo "⚠️  HUGGINGFACE_API_TOKEN not set"
    echo "   Get FREE token at: https://huggingface.co/settings/tokens"
else
    echo "✅ Hugging Face token found"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Demo vector search
echo "🎵 DEMO: Vector Music Search (FREE!)"
echo ""
echo "Loading demo tracks..."
python3 VECTOR_DB_MUSIC_SEARCH.py load-demo 2>&1 | tail -5

echo ""
echo "🔍 Testing search by vibe: 'energetic upbeat'"
echo ""
python3 VECTOR_DB_MUSIC_SEARCH.py search "energetic upbeat" 2>&1 | head -20

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "🎉 AI INTEGRATION SUITE READY!"
echo ""
echo "📋 WHAT YOU CAN DO NOW:"
echo ""
echo "  1. Vector Search:"
echo "     python3 VECTOR_DB_MUSIC_SEARCH.py search 'dark cinematic'"
echo ""
echo "  2. AI Music Generation (if HUGGINGFACE_API_TOKEN set):"
echo "     python3 AI_MUSIC_GENERATOR.py musicgen-free 'chill beats'"
echo ""
echo "  3. Cloudflare Deploy (if CLOUDFLARE_API_TOKEN set):"
echo "     python3 CLOUDFLARE_COMPLETE_INTEGRATION.py deploy-stripe"
echo ""
echo "  4. Get similar tracks:"
echo "     python3 VECTOR_DB_MUSIC_SEARCH.py similar 1"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📖 Full documentation: COMPLETE_AI_INTEGRATION_MASTER.md"
echo ""
echo "🐟 GORUNFREE WITH AI POWER! 🚀"

