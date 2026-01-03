#!/bin/bash

# Mac Pro IP over Thunderbolt Bridge
MACPRO_IP="192.168.2.2"

# Launch Screen Sharing
echo "🖥️ Connecting to Mac Pro via Thunderbolt Bridge..."
open "vnc://$MACPRO_IP"

# Optional voice feedback
say "Opening slab link to Mac Pro. Screen sharing initiated."