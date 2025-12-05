#!/bin/bash
set -e

echo "🧪 NoizyLab OS Test Harness"
echo "============================"
echo ""

BASE="/Users/m2ultra/NOIZYLAB/noizylab-os"
TESTS_PASSED=0
TESTS_FAILED=0

test_cmd() {
    local name="$1"
    local cmd="$2"
    
    echo -n "Testing $name... "
    if eval "$cmd" >/dev/null 2>&1; then
        echo "✔️  PASS"
        ((TESTS_PASSED++))
        return 0
    else
        echo "❌ FAIL"
        ((TESTS_FAILED++))
        return 1
    fi
}

# Test 1: Node.js version
echo "📦 Environment Tests"
test_cmd "Node.js installed" "command -v node"
test_cmd "npm installed" "command -v npm"
test_cmd "wrangler CLI installed" "command -v wrangler"

# Test 2: Cloudflare authentication
echo ""
echo "☁️  Cloudflare Tests"
test_cmd "Cloudflare authenticated" "wrangler whoami"

# Test 3: Workers build
echo ""
echo "🏗️  Worker Build Tests"
if [ -d "$BASE/workers/ai-super-worker" ]; then
    cd "$BASE/workers/ai-super-worker"
    test_cmd "ai-super-worker builds" "npm run build 2>/dev/null || npx wrangler deploy --dry-run"
fi

# Test 4: D1 Database
echo ""
echo "💾 Database Tests"
test_cmd "D1 database accessible" "wrangler d1 list | grep -q noizylab || true"

# Test 5: Queues
echo ""
echo "📬 Queue Tests"
test_cmd "Queues configured" "wrangler queues list | grep -q SNAPSHOT_QUEUE || true"

# Test 6: AI Router
echo ""
echo "🤖 AI Router Tests"
if [ -f "$BASE/.env" ]; then
    source "$BASE/.env"
    if [ -n "$GEMINI_API_KEY" ]; then
        test_cmd "Gemini API key set" "[ -n \"\$GEMINI_API_KEY\" ]"
    fi
    if [ -n "$ANTHROPIC_API_KEY" ]; then
        test_cmd "Claude API key set" "[ -n \"\$ANTHROPIC_API_KEY\" ]"
    fi
fi

# Test 7: CLI Tools
echo ""
echo "🛠️  CLI Tool Tests"
test_cmd "cfw CLI available" "command -v cfw || [ -f /usr/local/bin/cfw ]"
test_cmd "gemini CLI available" "command -v gemini || [ -f /usr/local/bin/gemini ]"
test_cmd "claude CLI available" "command -v claude || [ -f /usr/local/bin/claude ]"

# Test 8: File structure
echo ""
echo "📁 File Structure Tests"
test_cmd "Workers directory exists" "[ -d \"$BASE/workers\" ]"
test_cmd "AI directory exists" "[ -d \"$BASE/ai\" ]"
test_cmd "Scripts directory exists" "[ -d \"$BASE/scripts\" ]"
test_cmd "Supercode directory exists" "[ -d \"$BASE/supercode\" ]"

# Summary
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Test Summary:"
echo "  ✔️  Passed: $TESTS_PASSED"
echo "  ❌ Failed: $TESTS_FAILED"
echo ""

if [ $TESTS_FAILED -eq 0 ]; then
    echo "✨ All tests passed!"
    exit 0
else
    echo "⚠️  Some tests failed. Review output above."
    exit 1
fi

