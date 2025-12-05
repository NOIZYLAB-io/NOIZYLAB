#!/bin/bash

echo "$(date): 🔇 Purging voice daemons"
pkill -f "say|VoiceOver|speechsynthesisd"

echo "$(date): 📸 Creating healing snapshot"
SNAP="remoteheal-$(date +%Y%m%d-%H%M)"
prlctl snapshot NOIZYWIN --name "$SNAP" --description "Remote healing snapshot"

echo "$(date): 🔁 Restarting NOIZYWIN"
prlctl stop NOIZYWIN && sleep 3 && prlctl start NOIZYWIN
