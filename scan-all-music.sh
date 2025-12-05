#!/bin/bash
# FISH MUSIC INC - COMPLETE MUSIC ARCHIVE SCANNER
# Find ROB's entire 40-year creative output across ALL volumes

set -e

echo ""
echo "🎵 FISH MUSIC INC - COMPLETE MUSIC ARCHIVE SCANNER"
echo "===================================================="
echo ""
echo "Mission: Find ROB's ENTIRE 40 years of creative work"
echo "Searching for: FUEL, McDonald's, Microsoft, Deadwood, Design 2025, all client work"
echo ""

# Output file
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="/Users/m2ultra/CB-01-FISHMUSICINC/scans"
mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="$OUTPUT_DIR/music_archive_scan_${TIMESTAMP}.txt"
JSON_FILE="$OUTPUT_DIR/music_archive_scan_${TIMESTAMP}.json"

echo "Fish Music Inc - Complete Music Archive Scan" > "$OUTPUT_FILE"
echo "Generated: $(date)" >> "$OUTPUT_FILE"
echo "=========================================" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Start JSON
echo "{" > "$JSON_FILE"
echo '  "scan_date": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",' >> "$JSON_FILE"
echo '  "scanner": "Fish Music Inc Archive Scanner v2.0",' >> "$JSON_FILE"
echo '  "volumes": [' >> "$JSON_FILE"

FIRST_VOLUME=true

# Priority search terms
SEARCH_TERMS=(
    "Design"
    "Design 2025"
    "design-2025"
    "FUEL"
    "McDonald"
    "McDonalds"
    "Microsoft"
    "Tinker"
    "Deadwood"
    "Fish Music"
    "FishMusic"
    "stems"
    "sessions"
    "mixes"
    "masters"
    "client"
    "commercial"
    "projects"
    "Gavin"
    "Rogers"
)

# Audio file extensions
AUDIO_EXTS=("*.wav" "*.aif" "*.aiff" "*.mp3" "*.flac" "*.m4a" "*.aac")

# Scan each volume
for VOLUME in /Volumes/*; do
    if [ ! -d "$VOLUME" ]; then
        continue
    fi
    
    VOLUME_NAME=$(basename "$VOLUME")
    echo ""
    echo "=================================================="
    echo "📀 SCANNING: $VOLUME_NAME"
    echo "=================================================="
    
    # Add comma for JSON if not first
    if [ "$FIRST_VOLUME" = false ]; then
        echo "    }," >> "$JSON_FILE"
    fi
    FIRST_VOLUME=false
    
    # JSON volume start
    echo "    {" >> "$JSON_FILE"
    echo '      "name": "'$VOLUME_NAME'",' >> "$JSON_FILE"
    echo '      "path": "'$VOLUME'",' >> "$JSON_FILE"
    
    # Log to text file
    echo "" >> "$OUTPUT_FILE"
    echo "=== VOLUME: $VOLUME_NAME ===" >> "$OUTPUT_FILE"
    echo "Path: $VOLUME" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    # Get volume size
    VOLUME_SIZE=$(df -h "$VOLUME" 2>/dev/null | tail -1 | awk '{print $2}')
    echo "  📊 Size: $VOLUME_SIZE"
    echo "Size: $VOLUME_SIZE" >> "$OUTPUT_FILE"
    echo '      "size": "'$VOLUME_SIZE'",' >> "$JSON_FILE"
    
    # Search for priority terms
    echo ""
    echo "  🔍 Searching for project folders..."
    echo "" >> "$OUTPUT_FILE"
    echo "--- PROJECT FOLDERS ---" >> "$OUTPUT_FILE"
    
    FOUND_PROJECTS=()
    for TERM in "${SEARCH_TERMS[@]}"; do
        RESULTS=$(find "$VOLUME" -maxdepth 5 -type d -iname "*${TERM}*" 2>/dev/null || true)
        if [ ! -z "$RESULTS" ]; then
            echo "  ✨ Found '$TERM' matches:"
            echo "$RESULTS" | while read DIR; do
                if [ ! -z "$DIR" ]; then
                    SIZE=$(du -sh "$DIR" 2>/dev/null | awk '{print $1}')
                    echo "     • $DIR ($SIZE)"
                    echo "$DIR ($SIZE)" >> "$OUTPUT_FILE"
                    FOUND_PROJECTS+=("$DIR")
                fi
            done
        fi
    done
    
    # Count audio files by type
    echo ""
    echo "  🎵 Counting audio files..."
    echo "" >> "$OUTPUT_FILE"
    echo "--- AUDIO FILES ---" >> "$OUTPUT_FILE"
    
    TOTAL_AUDIO=0
    echo '      "audio_files": {' >> "$JSON_FILE"
    
    for EXT in "${AUDIO_EXTS[@]}"; do
        EXT_NAME=${EXT#*.}
        COUNT=$(find "$VOLUME" -type f -iname "$EXT" 2>/dev/null | wc -l | xargs)
        if [ $COUNT -gt 0 ]; then
            echo "     ${EXT_NAME^^}: $COUNT files"
            echo "${EXT_NAME^^}: $COUNT" >> "$OUTPUT_FILE"
            TOTAL_AUDIO=$((TOTAL_AUDIO + COUNT))
            echo '        "'${EXT_NAME}'": '$COUNT',' >> "$JSON_FILE"
        fi
    done
    
    echo '        "total": '$TOTAL_AUDIO >> "$JSON_FILE"
    echo '      },' >> "$JSON_FILE"
    
    echo ""
    echo "  📊 Total Audio Files: $TOTAL_AUDIO"
    echo "Total: $TOTAL_AUDIO" >> "$OUTPUT_FILE"
    
    # Look for Pro Tools sessions
    echo ""
    echo "  🎛️  Checking for DAW sessions..."
    PTX_COUNT=$(find "$VOLUME" -type f -iname "*.ptx" 2>/dev/null | wc -l | xargs)
    LOGIC_COUNT=$(find "$VOLUME" -type d -iname "*.logic" 2>/dev/null | wc -l | xargs)
    
    if [ $PTX_COUNT -gt 0 ] || [ $LOGIC_COUNT -gt 0 ]; then
        echo "     Pro Tools: $PTX_COUNT sessions"
        echo "     Logic Pro: $LOGIC_COUNT projects"
        echo "" >> "$OUTPUT_FILE"
        echo "--- DAW SESSIONS ---" >> "$OUTPUT_FILE"
        echo "Pro Tools: $PTX_COUNT" >> "$OUTPUT_FILE"
        echo "Logic Pro: $LOGIC_COUNT" >> "$OUTPUT_FILE"
    fi
    
    # Check for 4TB Lacie (Design 2025 stems!)
    if [[ "$VOLUME_NAME" == *"4TB"* ]] || [[ "$VOLUME_NAME" == *"Lacie"* ]] || [[ "$VOLUME_NAME" == *"LaCie"* ]]; then
        echo ""
        echo "  🎸 FOUND 4TB LACIE DRIVE!"
        echo "  🔍 Searching for Design 2025 stems..."
        DESIGN_STEMS=$(find "$VOLUME" -maxdepth 4 -type d -iname "*design*2025*" -o -iname "*design*stems*" 2>/dev/null || true)
        if [ ! -z "$DESIGN_STEMS" ]; then
            echo "  ✅ FOUND DESIGN 2025 STEMS:"
            echo "$DESIGN_STEMS" | while read DIR; do
                echo "     🎯 $DIR"
            done
        fi
    fi
    
    echo '      "scanned": true' >> "$JSON_FILE"
done

# Close JSON
echo "    }" >> "$JSON_FILE"
echo "  ]" >> "$JSON_FILE"
echo "}" >> "$JSON_FILE"

# Final summary
echo ""
echo "=================================================="
echo "✅ SCAN COMPLETE!"
echo "=================================================="
echo ""
echo "📄 Results saved to:"
echo "   Text: $OUTPUT_FILE"
echo "   JSON: $JSON_FILE"
echo ""
echo "📊 Quick Stats:"
cat "$OUTPUT_FILE" | grep -E "VOLUME:|Total:|Size:" | head -20
echo ""
echo "🚀 GORUNFREE!"
echo ""

