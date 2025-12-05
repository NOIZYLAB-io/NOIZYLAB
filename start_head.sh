#!/bin/bash
# 🧠 RAY CLUSTER - START HEAD NODE
# Fish Music Inc - CB_01

echo "🧠 Starting Ray cluster HEAD node on GABRIEL..."

# Stop existing cluster if running
ray stop >/dev/null 2>&1

# Start head node
ray start \
    --head \
    --port=6379 \
    --dashboard-host=0.0.0.0 \
    --dashboard-port=8265 \
    --num-cpus=20 \
    --num-gpus=1

echo ""
echo "✅ Ray HEAD node online!"
echo ""
echo "📊 Dashboard: http://localhost:8265"
echo "🔗 Connect workers with:"
echo "   ray start --address='<GABRIEL-IP>:6379'"
echo ""
