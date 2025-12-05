#!/bin/bash
# 📋 CLIPBOARD SYNC - UNIVERSAL CLIPBOARD ACROSS MACHINES
# Fish Music Inc - CB_01

echo "📋 Starting clipboard sync (GABRIEL ↔ OMEN)..."

# Install clipboard sync daemon
if ! command -v clipnotify >/dev/null 2>&1; then
    echo "[+] Installing clipboard tools..."
    brew install clipnotify >/dev/null 2>&1 || echo "   (Install manually if needed)"
fi

# Start clipboard monitor
cat > /tmp/clipboard_sync.sh << 'EOF'
#!/bin/bash
# Monitor clipboard and sync via Redis

while true; do
    # Get clipboard content
    CLIP=$(pbpaste 2>/dev/null)
    
    # Store in Redis
    if [ ! -z "$CLIP" ]; then
        echo "$CLIP" | redis-cli -x SET clipboard:gabriel >/dev/null 2>&1
    fi
    
    # Get remote clipboard from Redis
    REMOTE=$(redis-cli GET clipboard:omen 2>/dev/null)
    if [ ! -z "$REMOTE" ] && [ "$REMOTE" != "$CLIP" ]; then
        echo "$REMOTE" | pbcopy
    fi
    
    sleep 1
done
EOF

chmod +x /tmp/clipboard_sync.sh
nohup /tmp/clipboard_sync.sh >/dev/null 2>&1 &

echo "✅ Clipboard sync active!"
echo "   Clipboard shared between GABRIEL ↔ OMEN via Redis"
echo ""
