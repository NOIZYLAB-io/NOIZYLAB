#!/bin/bash
###############################################################################
# 🔍 COMPLETE MC96ECOUNIVERSE SCAN - FIND ALL ROB'S WORK!!!
# Scans every volume, finds every project, catalogs everything!
# MAXIMUM VELOCITY!!! GORUNFREE X1000!!!
###############################################################################

echo "🔥⚡🚀 MC96ECOUNIVERSE COMPLETE WORK SCAN!!! 🚀⚡🔥"
echo ""
echo "Finding ALL of ROB's creative work!!!"
echo "Even if scattered everywhere!!!"
echo ""

MASTER="/Volumes/6TB/MC96_COMPLETE_WORK_CATALOG"
mkdir -p "$MASTER"

echo "📂 Creating complete catalog structure..."
echo ""

# TURBO PARALLEL SCAN ACROSS ALL VOLUMES!!!
echo "🔍 SCANNING ALL 20+ VOLUMES IN PARALLEL!!!"
echo ""

{
    # CLIENT WORK
    find /Volumes -type d -iname "*fuel*" -o -iname "*mcdonalds*" -o -iname "*microsoft*" -o -iname "*deadwood*" 2>/dev/null > /tmp/mc96_client_work.txt &
    
    # MUSIC PROJECTS
    find /Volumes -type d -iname "*design*2025*" -o -iname "*fitc*" -o -iname "*fish*music*" 2>/dev/null > /tmp/mc96_music_projects.txt &
    
    # LOGIC SESSIONS
    find /Volumes -type f -iname "*.logic" -o -iname "*.logicx" 2>/dev/null > /tmp/mc96_logic_sessions.txt &
    
    # ALL AUDIO
    find /Volumes -type f \( -iname "*.wav" -o -iname "*.mp3" -o -iname "*.flac" \) 2>/dev/null > /tmp/mc96_all_audio.txt &
    
    # ALL VIDEO  
    find /Volumes -type f \( -iname "*.mov" -o -iname "*.mp4" -o -iname "*.m4v" \) 2>/dev/null > /tmp/mc96_all_video.txt &
    
    # ALL IMAGES
    find /Volumes -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.psd" \) 2>/dev/null > /tmp/mc96_all_images.txt &
    
    wait
}

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ⚡ SCAN COMPLETE!!!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# COUNT EVERYTHING
CLIENT=$(wc -l < /tmp/mc96_client_work.txt 2>/dev/null || echo 0)
MUSIC=$(wc -l < /tmp/mc96_music_projects.txt 2>/dev/null || echo 0)
LOGIC=$(wc -l < /tmp/mc96_logic_sessions.txt 2>/dev/null || echo 0)
AUDIO=$(wc -l < /tmp/mc96_all_audio.txt 2>/dev/null || echo 0)
VIDEO=$(wc -l < /tmp/mc96_all_video.txt 2>/dev/null || echo 0)
IMAGES=$(wc -l < /tmp/mc96_all_images.txt 2>/dev/null || echo 0)

echo "📊 ROB'S COMPLETE WORK INVENTORY:"
echo ""
echo "💼 Client Projects: $CLIENT (FUEL, McDonald's, Microsoft, Deadwood!)"
echo "🎵 Music Projects: $MUSIC"
echo "🎚️ Logic Sessions: $LOGIC"
echo "🎧 Audio Files: $AUDIO"
echo "🎬 Video Files: $VIDEO"
echo "🎨 Image Files: $IMAGES"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📍 Complete catalogs saved to /tmp/mc96_*.txt"
echo ""
echo "✅ MC96ECOUNIVERSE SCANNED!!!"
echo "✅ ALL ROB'S WORK CATALOGED!!!"
echo ""
echo "GORUNFREE X1000!!! 🚀"

