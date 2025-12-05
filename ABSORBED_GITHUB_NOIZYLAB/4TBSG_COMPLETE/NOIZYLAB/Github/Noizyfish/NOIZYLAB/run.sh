#!/bin/bash
# Quick start script for IT Genius

cd "$(dirname "$0")"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import psutil" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Run IT Genius
python3 it_genius.py

