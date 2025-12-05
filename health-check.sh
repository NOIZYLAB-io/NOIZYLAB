#!/bin/bash
# NoizyLab Health Check

echo "🏥 NoizyLab Health Check"
echo "========================"
echo ""

# Check services
echo "📡 Services:"
curl -s http://localhost:8000/ >/dev/null && echo "   ✅ V4 API: Running" || echo "   ❌ V4 API: Not running"
curl -s http://localhost:8001/docs >/dev/null && echo "   ✅ Webhook Hub: Running" || echo "   ❌ Webhook Hub: Not running"
curl -s http://localhost:8002/mobile/health >/dev/null && echo "   ✅ Mobile API: Running" || echo "   ❌ Mobile API: Not running"
lsof -i :8501 >/dev/null && echo "   ✅ Dashboard: Running" || echo "   ❌ Dashboard: Not running"

echo ""
echo "💾 Databases:"
[ -f "email-intelligence/email_intelligence.db" ] && echo "   ✅ Email DB: Exists" || echo "   ❌ Email DB: Missing"
[ -f "security/auth.db" ] && echo "   ✅ Auth DB: Exists" || echo "   ❌ Auth DB: Missing"
[ -f "integrations/webhooks.db" ] && echo "   ✅ Webhook DB: Exists" || echo "   ❌ Webhook DB: Missing"

echo ""
echo "📁 Structure:"
[ -d "email-intelligence" ] && echo "   ✅ Email Intelligence" || echo "   ❌ Email Intelligence"
[ -d "universal-blocker" ] && echo "   ✅ Universal Blocker" || echo "   ❌ Universal Blocker"
[ -d "imessage-spam-filter" ] && echo "   ✅ iMessage Filter" || echo "   ❌ iMessage Filter"

echo ""
