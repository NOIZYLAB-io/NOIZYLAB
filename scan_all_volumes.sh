#!/bin/bash
# Scan all volumes for ROB's 40 years of music
# Find FUEL, McDonald's, Microsoft, Deadwood, Design stems, etc.

echo ""
echo "🎵 SCANNING ALL VOLUMES FOR MUSIC ARCHIVE"
echo "=========================================="
echo ""

OUTPUT_FILE="volume_scan_results.txt"
echo "Fish Music Inc - Volume Scan Results" > $OUTPUT_FILE
echo "Generated: $(date)" >> $OUTPUT_FILE
echo "=========================================" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Key search terms for ROB's work
SEARCH_TERMS=(
    "FUEL"
    "McDonald"
    "Microsoft"
    "Tinker"
    "Deadwood"
    "Design"
    "Design 2025"
    "Fish Music"
    "stems"
    "sessions"
    "mixes"
    "masters"
    "client"
    "commercial"
)

echo "🔍 Searching for:"
for term in "${SEARCH_TERMS[@]}"; do
    echo "  • $term"
done
echo ""

# Scan each volume
for vol in /Volumes/*; do
    if [ -d "$vol" ]; then
        vol_name=$(basename "$vol")
        echo ""
        echo "📀 Scanning: $vol_name"
        echo "------------------------"
        
        echo "" >> $OUTPUT_FILE
        echo "=== VOLUME: $vol_name ===" >> $OUTPUT_FILE
        echo "" >> $OUTPUT_FILE
        
        # Search for each term
        for term in "${SEARCH_TERMS[@]}"; do
            results=$(find "$vol" -maxdepth 4 -type d -iname "*${term}*" 2>/dev/null)
            if [ ! -z "$results" ]; then
                echo "  ✨ Found '$term' matches:"
                echo "" >> $OUTPUT_FILE
                echo "--- $term ---" >> $OUTPUT_FILE
                echo "$results" | while read dir; do
                    size=$(du -sh "$dir" 2>/dev/null | awk '{print $1}')
                    echo "    • $dir ($size)"
                    echo "$dir ($size)" >> $OUTPUT_FILE
                done
            fi
        done
        
        # Look for audio files
        echo "  🎵 Counting audio files..."
        wav_count=$(find "$vol" -maxdepth 4 -type f -iname "*.wav" 2>/dev/null | wc -l | xargs)
        aif_count=$(find "$vol" -maxdepth 4 -type f -iname "*.aif*" 2>/dev/null | wc -l | xargs)
        mp3_count=$(find "$vol" -maxdepth 4 -type f -iname "*.mp3" 2>/dev/null | wc -l | xargs)
        
        if [ "$wav_count" -gt 0 ] || [ "$aif_count" -gt 0 ] || [ "$mp3_count" -gt 0 ]; then
            echo "    WAV: $wav_count | AIF: $aif_count | MP3: $mp3_count"
            echo "" >> $OUTPUT_FILE
            echo "Audio files: WAV=$wav_count, AIF=$aif_count, MP3=$mp3_count" >> $OUTPUT_FILE
        fi
    fi
done

echo ""
echo "✅ Scan complete!"
echo ""
echo "📄 Full results saved to: $OUTPUT_FILE"
echo ""

# Display summary
echo "📊 SUMMARY"
echo "----------"
cat $OUTPUT_FILE | grep -E "VOLUME:|Audio files:" | head -20
echo ""

