#!/bin/bash

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "🔍 Checking LogicInstaller project structure...\n"

BASE="$HOME/Documents/THE_NEW_WORLD/LogicInstaller"

# Required files
REQUIRED=(
  "$BASE/payload/LogicVoiceCommands.plist"
  "$BASE/postinstall"
  "$BASE/build.sh"
)

MISSING=0

# Check required files
for ITEM in "${REQUIRED[@]}"; do
  if [ -e "$ITEM" ]; then
    echo -e "✅ ${GREEN}Found:${NC} $ITEM"
  else
    echo -e "❌ ${RED}Missing:${NC} $ITEM"
    MISSING=$((MISSING+1))
  fi
done

# Validate LogicVoiceCommands.plist
if [ -f "$BASE/payload/LogicVoiceCommands.plist" ]; then
  echo -e "\n🔎 Validating LogicVoiceCommands.plist..."
  plutil -lint "$BASE/payload/LogicVoiceCommands.plist"
fi

# Validate system VoiceCommands.plist
VC_FILE="$HOME/Library/Application Support/com.apple.speech.recognition.AppleSpeechRecognition.prefs/VoiceCommands.plist"
if [ -f "$VC_FILE" ]; then
  echo -e "\n🔎 Validating system VoiceCommands.plist..."
  plutil -lint "$VC_FILE"
else
  echo -e "\nℹ️ ${YELLOW}No system VoiceCommands.plist yet${NC} (that’s fine if you haven’t created any custom commands)."
fi

# Final status
echo
if [ $MISSING -eq 0 ]; then
  echo -e "🎉 ${GREEN}All required project files are present!${NC}"
else
  echo -e "⚠️ ${YELLOW}$MISSING item(s) missing.${NC} Please add them before building."
fi
