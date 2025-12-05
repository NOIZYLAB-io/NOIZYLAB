#!/usr/bin/env bash
# Enhanced MC96 Wrapper with error handling and performance monitoring

NOIZYLAB="/Users/m2ultra/NOIZYLAB"
MC96="$NOIZYLAB/mc96-cli.mjs"

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    exit 1
fi

# Check if MC96 exists
if [ ! -f "$MC96" ]; then
    echo "❌ MC96 not found at: $MC96"
    exit 1
fi

# Run with performance monitoring
echo "🔵 Starting MC96..."
echo "Command: node $MC96 $@"
echo ""

# Track execution time
START_TIME=$(date +%s)

# Run MC96 with error handling
if node "$MC96" "$@"; then
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    echo ""
    echo "✅ MC96 completed in ${DURATION}s"
else
    echo ""
    echo "❌ MC96 encountered an error"
    exit 1
fi

