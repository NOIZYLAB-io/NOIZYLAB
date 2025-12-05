#!/bin/bash

# AI Aggregator Quick Start Script
# This script activates the virtual environment and starts the application

cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run ./setup.sh first"
    exit 1
fi

# Activate virtual environment
echo "🚀 Starting AI Engine Aggregator..."
source venv/bin/activate

# Check if config.json exists
if [ ! -f "config.json" ]; then
    echo "⚠️  config.json not found. Creating default config..."
    python3 -c "
import json
config = {
    'openai': {'api_key': '', 'enabled': True, 'display_name': 'ChatGPT (GPT-4)'},
    'anthropic': {'api_key': '', 'enabled': True, 'display_name': 'Claude (Anthropic)'},
    'google': {'api_key': '', 'enabled': True, 'display_name': 'Gemini (Google)'}
}
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)
"
fi

# Start the application
echo ""
echo "✅ Starting server..."
echo "📱 Open your browser: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py

