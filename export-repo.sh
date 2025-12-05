#!/bin/bash
# EXPORT ENTIRE REPO AS TAR.GZ
set -e

VERSION=$(date +%Y%m%d_%H%M%S)
OUTPUT="noizylab-os-${VERSION}.tar.gz"

echo "📦 Creating export: $OUTPUT"

tar -czf "$OUTPUT" \
  --exclude='node_modules' \
  --exclude='.wrangler' \
  --exclude='.git' \
  --exclude='*.log' \
  .

echo "✅ Export created: $OUTPUT"
ls -lh "$OUTPUT"
