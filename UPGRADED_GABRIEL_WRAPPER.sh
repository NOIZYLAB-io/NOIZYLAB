#!/usr/bin/env bash
# Enhanced GABRIEL Wrapper with error handling and performance monitoring

NOIZYLAB="/Users/m2ultra/NOIZYLAB"
GABRIEL="$NOIZYLAB/gabriel-cli.mjs"

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    exit 1
fi

# Check if GABRIEL exists
if [ ! -f "$GABRIEL" ]; then
    echo "❌ GABRIEL not found at: $GABRIEL"
    exit 1
fi

# Run with performance monitoring
echo "🟣 Starting GABRIEL..."
echo "Command: node $GABRIEL $@"
echo ""

# Track execution time
START_TIME=$(date +%s)

# Run GABRIEL with error handling
if node "$GABRIEL" "$@"; then
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    echo ""
    echo "✅ GABRIEL completed in ${DURATION}s"
else
    echo ""
    echo "❌ GABRIEL encountered an error"
    exit 1
fi

