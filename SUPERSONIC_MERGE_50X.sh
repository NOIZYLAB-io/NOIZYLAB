#!/bin/bash
# 🚀 SUPERSONIC MERGE - 50X FASTER CODE ABSORPTION
# Merges ALL code into Github/Noizyfish/NOIZYLAB safely

set -e

echo "🚀 SUPERSONIC MERGE STARTING..."
echo "================================================"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

TARGET="/Users/m2ultra/Github/Noizyfish/NOIZYLAB"
SOURCE1="/Users/m2ultra/NOIZYLAB"
SOURCE2="/Users/m2ultra/Github/noizylab"

echo -e "${BLUE}📊 PHASE 1: Setup Git LFS for Large Files${NC}"
cd "$TARGET"
git lfs install 2>/dev/null || true

# Track large file types with Git LFS
git lfs track "*.mp4" "*.MP4" "*.dmg" "*.zip" "*.tar.gz" "*.nkx" "*.wav" "*.CAF" 2>/dev/null || true
git add .gitattributes 2>/dev/null || true

echo -e "${BLUE}📦 PHASE 2: Commit Current Target State${NC}"
cd "$TARGET"
git add -A 2>/dev/null || echo "No changes to add"
git commit -m "🔄 Pre-merge snapshot: Current NOIZYLAB state" 2>/dev/null || echo "Nothing to commit"

echo -e "${BLUE}🔥 PHASE 3: Copy Code from SOURCE1 (/NOIZYLAB)${NC}"
# Copy only code files, exclude large media
rsync -av --progress \
  --include='*.py' --include='*.js' --include='*.ts' --include='*.tsx' \
  --include='*.json' --include='*.md' --include='*.sh' --include='*.yml' \
  --include='*.yaml' --include='*.toml' --include='*.html' --include='*.css' \
  --include='*/' \
  --exclude='*.mp4' --exclude='*.MP4' --exclude='*.dmg' --exclude='*.zip' \
  --exclude='*.tar.gz' --exclude='*.nkx' --exclude='*.wav' --exclude='*.CAF' \
  --exclude='.git' --exclude='node_modules' --exclude='__pycache__' \
  "$SOURCE1/" "$TARGET/"

echo -e "${BLUE}💫 PHASE 4: Copy Code from SOURCE2 (/noizylab)${NC}"
rsync -av --progress \
  --include='*.py' --include='*.js' --include='*.ts' --include='*.tsx' \
  --include='*.json' --include='*.md' --include='*.sh' --include='*.yml' \
  --include='*.yaml' --include='*.toml' --include='*.html' --include='*.css' \
  --include='*/' \
  --exclude='*.mp4' --exclude='*.MP4' --exclude='*.dmg' --exclude='*.zip' \
  --exclude='*.tar.gz' --exclude='*.nkx' --exclude='*.wav' --exclude='*.CAF' \
  --exclude='.git' --exclude='node_modules' --exclude='__pycache__' \
  "$SOURCE2/" "$TARGET/"

echo -e "${BLUE}✅ PHASE 5: Stage All New Code${NC}"
cd "$TARGET"
git add -A

echo -e "${BLUE}💾 PHASE 6: Create Massive Commit${NC}"
git commit -m "🚀 SUPERSONIC MERGE: Absorbed ALL code from everywhere

Sources merged:
- /Users/m2ultra/NOIZYLAB (425GB → code only)
- /Users/m2ultra/Github/noizylab (974MB → code only)

Strategy:
- Code files: Python, JavaScript, TypeScript, configs
- Large media: Excluded (handled separately with LFS)
- Result: Clean, fast, code-focused repository

Date: $(date)
Velocity: MAXIMUM 🔥
" || echo "No changes to commit"

echo -e "${GREEN}✨ PHASE 7: Summary${NC}"
cd "$TARGET"
echo "================================================"
echo "📊 Git Status:"
git status --short | head -20
echo ""
echo "📈 Repository Size:"
du -sh "$TARGET"
echo ""
echo -e "${GREEN}🎉 SUPERSONIC MERGE COMPLETE!${NC}"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Review changes: cd $TARGET && git log"
echo "2. Push to remote: git push origin main"
echo "3. Clean up sources (optional): Run DELETE script"
