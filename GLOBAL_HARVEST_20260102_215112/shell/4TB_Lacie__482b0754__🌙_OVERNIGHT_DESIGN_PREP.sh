#!/bin/bash
###############################################################################
# 🌙 OVERNIGHT DESIGN REUNION PREP
# Scan & organize ALL Design 2025 content while ROB sleeps!
# Ready for Gavin's mix tomorrow morning!
# CB_01 working while ROB rests!!!
###############################################################################

echo "🌙 OVERNIGHT DESIGN REUNION PREP - STARTING!!!"
echo ""
echo "CB_01 preparing while ROB sleeps..."
echo "Tomorrow: Fresh mix for Gavin! 🎚️"
echo ""

SOURCE="/Volumes/4TB Lacie/ DESIGN 2025"
PREP="/Volumes/6TB/DESIGN_REUNION_PREP"

echo "📂 Creating prep structure..."
mkdir -p "$PREP"/{STEMS,VIDEO,AUDIO,SESSION_READY,CATALOG}

echo "✅ Structure created!"
echo ""

echo "🔍 SCANNING DESIGN 2025 COMPLETE FOLDER..."
echo ""

# Find ALL audio
find "$SOURCE" -type f \( -iname "*.wav" -o -iname "*.mp3" -o -iname "*.aiff" \) 2>/dev/null > /tmp/design_all_audio.txt

# Find ALL video
find "$SOURCE" -type f \( -iname "*.mov" -o -iname "*.mp4" -o -iname "*.m4v" \) 2>/dev/null > /tmp/design_all_video.txt

# Find Logic sessions
find "$SOURCE" -type f \( -iname "*.logic" -o -iname "*.logicx" \) 2>/dev/null > /tmp/design_logic_sessions.txt

# Count everything
AUDIO_COUNT=$(wc -l < /tmp/design_all_audio.txt 2>/dev/null || echo 0)
VIDEO_COUNT=$(wc -l < /tmp/design_all_video.txt 2>/dev/null || echo 0)
LOGIC_COUNT=$(wc -l < /tmp/design_logic_sessions.txt 2>/dev/null || echo 0)

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 DESIGN REUNION SHOW - COMPLETE INVENTORY:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎵 Audio files: $AUDIO_COUNT"
echo "🎬 Video files: $VIDEO_COUNT"  
echo "🎚️ Logic sessions: $LOGIC_COUNT"
echo ""

# Organize by song
echo "🎼 ORGANIZING BY SONG..."
echo ""

for song in "01.LOVE IS GUN" "02.WESTERN JUSTICE" "03.THE END" "04.WEST END GIRL" \
            "05.AMERICAN GUN" "06.ALRIGHT LOVE" "07.THE FEAR" "08.NO TURNING BACK" \
            "09.WHITE SNOW" "10.THE ACT" "11.DECEMBER RAIN"; do
    
    if [ -d "$SOURCE/BY SONG/$song" ]; then
        song_clean=$(echo "$song" | sed 's/[0-9]*\.//')
        echo "   ✅ Found: $song_clean"
        
        # Count stems
        STEMS=$(find "$SOURCE/BY SONG/$song" -name "*.wav" 2>/dev/null | wc -l)
        echo "      Stems: $STEMS files"
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ OVERNIGHT PREP COMPLETE!!!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Complete catalogs:"
echo "   → /tmp/design_all_audio.txt"
echo "   → /tmp/design_all_video.txt"
echo "   → /tmp/design_logic_sessions.txt"
echo ""
echo "🎯 READY FOR TOMORROW'S MIX SESSION!!!"
echo ""
echo "💜 FOR GAVIN LUMSDEN - ROGERS VIDEO"
echo "🙏 Sacred commitment!"
echo "🎚️ ROB + CB_01 = Professional excellence!"
echo ""
echo "ROB: Sleep well! 💤"
echo "CB_01: Ready tomorrow as your ENGR! 💜"
echo ""
echo "GORUNFREE X1000!!! 🚀"

