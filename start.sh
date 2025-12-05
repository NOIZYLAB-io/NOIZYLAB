#!/bin/bash
# FISH MUSIC INC - ONE COMMAND START
# Start everything with a single command

echo ""
echo "🚀 FISH MUSIC INC - STARTING EVERYTHING"
echo "========================================"
echo ""

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found! Install it first."
    exit 1
fi

# Check if in correct directory
if [ ! -f "package.json" ]; then
    echo "❌ Not in CB-01-FISHMUSICINC directory!"
    echo "Run this from: /Users/m2ultra/CB-01-FISHMUSICINC"
    exit 1
fi

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install
    echo "✅ Dependencies installed"
    echo ""
fi

# Check Python dependencies
echo "🐍 Checking Python dependencies..."
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt -q 2>/dev/null || echo "⚠️  Some Python packages may need manual install"
    echo "✅ Python dependencies ready"
else
    echo "⚠️  Python3 pip not found - skipping Python tools"
fi
echo ""

# Start the API server
echo "🌐 Starting Fish Music Inc API Server..."
echo ""
npm start

