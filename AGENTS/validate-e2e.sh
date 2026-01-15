#!/bin/bash
# End-to-end validation script for cloud agent delegation
# Tests all components of the implementation

set -e  # Exit on any error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║    NOIZYLAB Cloud Agent Delegation - E2E Validation            ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Test 1: Registry JSON validation
echo "🔍 Test 1: Validating registry.json..."
if python3 -m json.tool registry.json > /dev/null 2>&1; then
  echo "   ✅ registry.json is valid JSON"
else
  echo "   ❌ registry.json has syntax errors"
  exit 1
fi

# Test 2: Python integration tests
echo ""
echo "🔍 Test 2: Running Python integration tests..."
if python3 test_cloud_delegation.py > /dev/null 2>&1; then
  echo "   ✅ All Python integration tests passed"
else
  echo "   ❌ Python integration tests failed"
  exit 1
fi

# Test 3: Shell script syntax
echo ""
echo "🔍 Test 3: Validating launch.sh syntax..."
if bash -n launch.sh; then
  echo "   ✅ launch.sh has valid syntax"
else
  echo "   ❌ launch.sh has syntax errors"
  exit 1
fi

# Test 4: TypeScript compilation
echo ""
echo "🔍 Test 4: Compiling TypeScript worker..."
cd ../workers/noizylab
if npm run build > /dev/null 2>&1; then
  echo "   ✅ TypeScript compiled successfully"
else
  echo "   ❌ TypeScript compilation failed"
  exit 1
fi
cd "$SCRIPT_DIR"

# Test 5: File existence checks
echo ""
echo "🔍 Test 5: Checking required files..."
FILES=(
  "cloud-delegate.py"
  "launch.sh"
  "registry.json"
  "README.md"
  "test_cloud_delegation.py"
  "IMPLEMENTATION_SUMMARY.md"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "   ✅ $file exists"
  else
    echo "   ❌ $file is missing"
    exit 1
  fi
done

# Test 6: Python script help
echo ""
echo "🔍 Test 6: Testing cloud-delegate.py help..."
if python3 cloud-delegate.py --help > /dev/null 2>&1; then
  echo "   ✅ cloud-delegate.py --help works"
else
  echo "   ❌ cloud-delegate.py --help failed"
  exit 1
fi

# Test 7: Launch script list
echo ""
echo "🔍 Test 7: Testing launch.sh list..."
if bash launch.sh list > /dev/null 2>&1; then
  echo "   ✅ launch.sh list works"
else
  echo "   ❌ launch.sh list failed"
  exit 1
fi

# Test 8: Registry structure validation
echo ""
echo "🔍 Test 8: Validating registry structure..."
REQUIRED_KEYS=("version" "updated" "agents" "cloud" "launcher" "storage")
for key in "${REQUIRED_KEYS[@]}"; do
  if python3 -c "import json; data=json.load(open('registry.json')); exit(0 if '$key' in data else 1)"; then
    echo "   ✅ registry.json has '$key' key"
  else
    echo "   ❌ registry.json missing '$key' key"
    exit 1
  fi
done

# Test 9: Cloud configuration validation
echo ""
echo "🔍 Test 9: Validating cloud configuration..."
if python3 -c "import json; data=json.load(open('registry.json')); cloud=data.get('cloud',{}); exit(0 if cloud.get('enabled') and cloud.get('endpoint') else 1)"; then
  echo "   ✅ Cloud configuration is valid"
else
  echo "   ❌ Cloud configuration is invalid"
  exit 1
fi

# Test 10: Agent deployment modes
echo ""
echo "🔍 Test 10: Validating agent deployment modes..."
if python3 -c "import json; data=json.load(open('registry.json')); agents=data.get('agents',[]); exit(0 if all('deployment' in a for a in agents) else 1)"; then
  echo "   ✅ All agents have deployment modes"
else
  echo "   ❌ Some agents missing deployment modes"
  exit 1
fi

# Summary
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   🎉 ALL TESTS PASSED! 🎉                      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Cloud agent delegation is fully validated and ready for use!"
echo ""
echo "Quick start:"
echo "  ./launch.sh list"
echo "  ./launch.sh systemguardian --cloud"
echo "  ./cloud-delegate.py --health"
echo ""
