#!/bin/bash
# 🧠 RAY CLUSTER - START WORKER NODE
# Fish Music Inc - CB_01
# Run this on HP-OMEN (or any worker machine)

GABRIEL_IP="${1:-192.168.1.100}"

echo "🧠 Starting Ray WORKER node..."
echo "   Connecting to HEAD: $GABRIEL_IP:6379"
echo ""

# Stop existing
ray stop >/dev/null 2>&1

# Start worker
ray start \
    --address="$GABRIEL_IP:6379" \
    --num-cpus=14 \
    --num-gpus=1

echo ""
echo "✅ Ray WORKER connected to HEAD!"
echo ""
echo "📊 Check status on HEAD: ray status"
echo ""
