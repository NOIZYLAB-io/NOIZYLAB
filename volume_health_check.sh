#!/bin/bash
# MC96 VOLUME HEALTH CHECK
# Checks disk space, organization status

echo "📊 MC96 VOLUME HEALTH CHECK"
echo "==========================="
echo "Date: $(date)"
echo ""

VOLUMES=(
    "6TB"
    "4TB_Utility"
    "4TB Big Fish"
    "4TB Blue Fish"
    "4TBSG"
    "4TB Lacie"
    "MAG 4TB"
    "12TB"
    "4TB_02"
    "RED DRAGON"
    "SAMPLE_MASTER"
    "SIDNEY"
    "EW"
)

echo "| Volume | Used | Free | Status |"
echo "|--------|------|------|--------|"

for vol in "${VOLUMES[@]}"; do
    if [ -d "/Volumes/$vol" ]; then
        info=$(df -h "/Volumes/$vol" 2>/dev/null | tail -1)
        used=$(echo "$info" | awk '{print $3}')
        free=$(echo "$info" | awk '{print $4}')
        cap=$(echo "$info" | awk '{print $5}' | tr -d '%')
        
        if [ "$cap" -gt 90 ]; then
            status="🔴 CRITICAL"
        elif [ "$cap" -gt 80 ]; then
            status="🟡 WARNING"
        else
            status="🟢 OK"
        fi
        
        echo "| $vol | $used | $free | $status |"
    else
        echo "| $vol | - | - | ❌ NOT MOUNTED |"
    fi
done

echo ""
echo "🎉 Health check complete!"
