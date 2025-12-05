#!/bin/bash
# 💾 REDIS - SHARED MEMORY POOL
# Fish Music Inc - CB_01

echo "💾 Starting Redis server..."

# Stop existing
redis-cli shutdown >/dev/null 2>&1

# Start Redis
redis-server \
    --daemonize yes \
    --bind 0.0.0.0 \
    --port 6379 \
    --maxmemory 4gb \
    --maxmemory-policy allkeys-lru \
    --save 60 1000 \
    --dir /tmp

sleep 1

# Verify
if redis-cli ping >/dev/null 2>&1; then
    echo "✅ Redis online (port 6379)"
    echo "   Max memory: 4GB"
    echo "   Persistence: Enabled"
else
    echo "❌ Redis failed to start"
    exit 1
fi
