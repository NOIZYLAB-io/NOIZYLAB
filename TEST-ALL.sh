#!/bin/bash
# SYSTEM TEST & VERIFICATION
# Tests all components and reports status
# GORUNFREEX1000 Quality Assurance

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PASS=0
FAIL=0
WARN=0

echo "🧪 SYSTEM TEST & VERIFICATION"
echo "=============================="
echo ""

# Test 1: Node.js files syntax
echo -e "${BLUE}Test 1: JavaScript Syntax${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for JS_FILE in *.js; do
    if [ -f "$JS_FILE" ]; then
        if node --check "$JS_FILE" 2>/dev/null; then
            echo -e "${GREEN}  ✓ $JS_FILE${NC}"
            ((PASS++))
        else
            echo -e "${RED}  ✗ $JS_FILE - SYNTAX ERROR${NC}"
            node --check "$JS_FILE" 2>&1 | head -3
            ((FAIL++))
        fi
    fi
done
echo ""

# Test 2: JSON files validity
echo -e "${BLUE}Test 2: JSON Validity${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for JSON_FILE in *.json; do
    if [ -f "$JSON_FILE" ]; then
        if python3 -m json.tool "$JSON_FILE" > /dev/null 2>&1; then
            echo -e "${GREEN}  ✓ $JSON_FILE${NC}"
            ((PASS++))
        else
            echo -e "${RED}  ✗ $JSON_FILE - INVALID JSON${NC}"
            ((FAIL++))
        fi
    fi
done
echo ""

# Test 3: Shell scripts syntax
echo -e "${BLUE}Test 3: Shell Script Syntax${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for SH_FILE in *.sh; do
    if [ -f "$SH_FILE" ]; then
        if bash -n "$SH_FILE" 2>/dev/null; then
            echo -e "${GREEN}  ✓ $SH_FILE${NC}"
            ((PASS++))
        else
            echo -e "${RED}  ✗ $SH_FILE - SYNTAX ERROR${NC}"
            ((FAIL++))
        fi
    fi
done
echo ""

# Test 4: Executability
echo -e "${BLUE}Test 4: File Permissions${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

SHOULD_BE_EXECUTABLE=(*.sh *.js)
for FILE in "${SHOULD_BE_EXECUTABLE[@]}"; do
    if [ -f "$FILE" ]; then
        if [ -x "$FILE" ]; then
            echo -e "${GREEN}  ✓ $FILE executable${NC}"
            ((PASS++))
        else
            echo -e "${YELLOW}  ⚠ $FILE not executable (fixing...)${NC}"
            chmod +x "$FILE"
            ((WARN++))
        fi
    fi
done
echo ""

# Test 5: Required dependencies
echo -e "${BLUE}Test 5: Dependencies${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

DEPS=("node" "npm" "python3" "curl" "jq")
for DEP in "${DEPS[@]}"; do
    if command -v $DEP &> /dev/null; then
        VERSION=$($DEP --version 2>&1 | head -1)
        echo -e "${GREEN}  ✓ $DEP found${NC} ($VERSION)"
        ((PASS++))
    else
        echo -e "${YELLOW}  ⚠ $DEP not found${NC}"
        ((WARN++))
    fi
done
echo ""

# Test 6: Port availability
echo -e "${BLUE}Test 6: Port Availability${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

PORTS=(7777 8888 9999)
for PORT in "${PORTS[@]}"; do
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "${GREEN}  ✓ Port $PORT in use (service running)${NC}"
        ((PASS++))
    else
        echo -e "${YELLOW}  ⚠ Port $PORT available (service not running)${NC}"
        ((WARN++))
    fi
done
echo ""

# Test 7: API Keys
echo -e "${BLUE}Test 7: API Keys${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

KEYS=("anthropic_api_key" "google_api_key" "together_api_key")
for KEY in "${KEYS[@]}"; do
    if security find-generic-password -a $USER -s "$KEY" -w 2>/dev/null >/dev/null; then
        echo -e "${GREEN}  ✓ $KEY configured${NC}"
        ((PASS++))
    else
        echo -e "${YELLOW}  ⚠ $KEY not found${NC}"
        ((WARN++))
    fi
done
echo ""

# Test 8: API Endpoint Tests
echo -e "${BLUE}Test 8: API Endpoints${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if lsof -Pi :8888 -sTCP:LISTEN -t >/dev/null 2>&1; then
    # Test /api/config
    if curl -s http://localhost:8888/api/config > /dev/null 2>&1; then
        echo -e "${GREEN}  ✓ GET /api/config${NC}"
        ((PASS++))
    else
        echo -e "${RED}  ✗ GET /api/config failed${NC}"
        ((FAIL++))
    fi
    
    # Test /api/models
    if curl -s http://localhost:8888/api/models > /dev/null 2>&1; then
        echo -e "${GREEN}  ✓ GET /api/models${NC}"
        ((PASS++))
    else
        echo -e "${RED}  ✗ GET /api/models failed${NC}"
        ((FAIL++))
    fi
else
    echo -e "${YELLOW}  ⚠ AI GENIUS not running (start with ./START-ALL.sh)${NC}"
    ((WARN++))
fi
echo ""

# Test 9: File structure
echo -e "${BLUE}Test 9: File Structure${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

REQUIRED_FILES=(
    "ai-genius.js"
    "ai-genius-config.js"
    "ai-models-list.json"
    "START-ALL.sh"
    "stop-all.sh"
)

for FILE in "${REQUIRED_FILES[@]}"; do
    if [ -f "$FILE" ]; then
        SIZE=$(du -h "$FILE" | cut -f1)
        echo -e "${GREEN}  ✓ $FILE ($SIZE)${NC}"
        ((PASS++))
    else
        echo -e "${RED}  ✗ $FILE missing${NC}"
        ((FAIL++))
    fi
done
echo ""

# Test 10: Documentation
echo -e "${BLUE}Test 10: Documentation${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

DOCS=(
    "AI-GENIUS-GUIDE.md"
    "AI-GENIUS-QUICK-START.md"
    "README.md"
)

for DOC in "${DOCS[@]}"; do
    if [ -f "$DOC" ]; then
        LINES=$(wc -l < "$DOC")
        echo -e "${GREEN}  ✓ $DOC ($LINES lines)${NC}"
        ((PASS++))
    else
        echo -e "${YELLOW}  ⚠ $DOC missing${NC}"
        ((WARN++))
    fi
done
echo ""

# Summary
echo "=============================="
echo "TEST SUMMARY"
echo "=============================="
echo ""
echo -e "${GREEN}Passed:  $PASS${NC}"
echo -e "${YELLOW}Warnings: $WARN${NC}"
echo -e "${RED}Failed:  $FAIL${NC}"
echo ""

TOTAL=$((PASS + WARN + FAIL))
SCORE=$(echo "scale=2; ($PASS * 100) / $TOTAL" | bc)

if [ $FAIL -eq 0 ]; then
    echo -e "${GREEN}✓ SYSTEM READY - Score: $SCORE%${NC}"
    echo ""
    echo "Start all services:"
    echo "  ./START-ALL.sh"
    exit 0
else
    echo -e "${RED}✗ SYSTEM NEEDS ATTENTION - Score: $SCORE%${NC}"
    echo ""
    echo "Review errors above and run:"
    echo "  ./HEAL-ALL.sh"
    exit 1
fi
