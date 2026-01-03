#!/bin/bash
###############################################################################
# 🎣 FISHNET - CATCH ALL FISH MUSIC COLLECTION!
# Scours EVERYWHERE for music, loops, SFX
# Rebuilds clean structure for VST & plugins!
# MAXIMUM VELOCITY! GORUNFREE!!!
###############################################################################

echo "🎣🔥 FISHNET - COMPLETE FISH MUSIC COLLECTION! 🔥🎣"
echo "Scouring all volumes! Finding EVERYTHING!"
echo ""

MASTER_BASE="/Volumes/6TB/FISH_MUSIC_COMPLETE"

# Clean rebuild structure
echo "📁 Creating clean VST/Plugin structure..."
mkdir -p "$MASTER_BASE"/{MUSIC_ORIGINALS,LOOPS,SFX_SAMPLES,VST_READY,PLUGIN_PRESETS,STEMS}
mkdir -p "$MASTER_BASE/LOOPS"/{DRUMS,BASS,MELODY,FX,PERCUSSION}
mkdir -p "$MASTER_BASE/SFX_SAMPLES"/{IMPACTS,TRANSITIONS,ATMOSPHERES,FOLEY,RISERS}
mkdir -p "$MASTER_BASE/MUSIC_ORIGINALS"/{VOCALS,INSTRUMENTALS,DEMOS,MASTERS}

echo "✅ Structure created!"
echo ""

echo "🔍 FISHNET SCAN - Finding ALL Fish Music Collection..."
echo ""

# FISHNET all volumes for Fish Music content
find /Volumes/SIDNEY /Volumes/"4TB Lacie" /Volumes/6TB /Volumes/4TBSG /Volumes/"MAG 4TB" \
  -type f \( -iname "*fish*" -o -iname "*noizy*" \) \
  \( -iname "*.wav" -o -iname "*.mp3" -o -iname "*.flac" -o -iname "*.aiff" \) \
  2>/dev/null | tee /tmp/fishnet_found.txt

FOUND=$(wc -l < /tmp/fishnet_found.txt)

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🎣 FISHNET CAUGHT: $FOUND files!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Categorize and copy
echo "⚡ Organizing by type..."
echo ""

MUSIC_COUNT=0
LOOP_COUNT=0
SFX_COUNT=0

while IFS= read -r file; do
    if [ ! -f "$file" ]; then continue; fi
    
    filename=$(basename "$file")
    path_lower=$(echo "$file" | tr '[:upper:]' '[:lower:]')
    
    # Categorize
    if [[ "$path_lower" == *"loop"* ]] || [[ "$path_lower" == *"128bpm"* ]] || [[ "$path_lower" == *"bpm"* ]]; then
        # LOOP
        if [[ "$path_lower" == *"drum"* ]]; then
            cp "$file" "$MASTER_BASE/LOOPS/DRUMS/" 2>/dev/null
        elif [[ "$path_lower" == *"bass"* ]]; then
            cp "$file" "$MASTER_BASE/LOOPS/BASS/" 2>/dev/null
        else
            cp "$file" "$MASTER_BASE/LOOPS/MELODY/" 2>/dev/null
        fi
        LOOP_COUNT=$((LOOP_COUNT + 1))
        
    elif [[ "$path_lower" == *"sfx"* ]] || [[ "$path_lower" == *"sample"* ]] || [[ "$path_lower" == *"one"*"shot"* ]]; then
        # SFX
        if [[ "$path_lower" == *"impact"* ]] || [[ "$path_lower" == *"hit"* ]]; then
            cp "$file" "$MASTER_BASE/SFX_SAMPLES/IMPACTS/" 2>/dev/null
        elif [[ "$path_lower" == *"riser"* ]] || [[ "$path_lower" == *"sweep"* ]]; then
            cp "$file" "$MASTER_BASE/SFX_SAMPLES/RISERS/" 2>/dev/null
        else
            cp "$file" "$MASTER_BASE/SFX_SAMPLES/ATMOSPHERES/" 2>/dev/null
        fi
        SFX_COUNT=$((SFX_COUNT + 1))
        
    else
        # MUSIC
        if [[ "$path_lower" == *"vocal"* ]] || [[ "$path_lower" == *"vox"* ]]; then
            cp "$file" "$MASTER_BASE/MUSIC_ORIGINALS/VOCALS/" 2>/dev/null
        elif [[ "$path_lower" == *"master"* ]]; then
            cp "$file" "$MASTER_BASE/MUSIC_ORIGINALS/MASTERS/" 2>/dev/null
        elif [[ "$path_lower" == *"instrumental"* ]] || [[ "$path_lower" == *"inst"* ]]; then
            cp "$file" "$MASTER_BASE/MUSIC_ORIGINALS/INSTRUMENTALS/" 2>/dev/null
        else
            cp "$file" "$MASTER_BASE/MUSIC_ORIGINALS/DEMOS/" 2>/dev/null
        fi
        MUSIC_COUNT=$((MUSIC_COUNT + 1))
    fi
    
    # Progress
    TOTAL=$((MUSIC_COUNT + LOOP_COUNT + SFX_COUNT))
    if [ $((TOTAL % 50)) -eq 0 ]; then
        echo "  ⚡ Organized: $TOTAL files..."
    fi
    
done < /tmp/fishnet_found.txt

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ FISHNET COMPLETE!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎵 Music: $MUSIC_COUNT"
echo "🔁 Loops: $LOOP_COUNT"  
echo "🔊 SFX: $SFX_COUNT"
echo "📂 Total: $TOTAL"
echo ""
echo "📍 Location: /Volumes/6TB/FISH_MUSIC_COMPLETE/"
echo ""
echo "🎯 VST & PLUGIN READY!"
echo "🚀 GORUNFREE!!!"

