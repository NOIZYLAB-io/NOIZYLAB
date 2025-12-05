#!/bin/bash
# Start Email Intelligence Dashboard System
# =========================================

set -e

BASE="/Users/m2ultra/NOIZYLAB/email-intelligence"

echo "🚀 Starting Email Intelligence Dashboard System..."
echo ""

# Check if API is running
if ! curl -s http://localhost:8000 >/dev/null 2>&1; then
    echo "📡 Starting API server..."
    cd "$BASE"
    python3 api_server.py &
    API_PID=$!
    echo "   API server started (PID: $API_PID)"
    sleep 2
else
    echo "✅ API server already running"
fi

# Start dashboard
echo ""
echo "📊 Starting Streamlit dashboard..."
cd "$BASE"
streamlit run dashboard.py --server.port 8501 --server.address 0.0.0.0

echo ""
echo "✨ Dashboard available at: http://localhost:8501"
echo "📡 API available at: http://localhost:8000"

