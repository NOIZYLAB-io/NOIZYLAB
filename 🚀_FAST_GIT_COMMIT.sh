#!/bin/bash
################################################################################
# 🚀 FAST GIT COMMIT - CURSE_BEAST_02 🚀
################################################################################
# Commits all NoizyLab code to git FAST!
################################################################################

set -e

echo "🔥🔥🔥 CURSE_BEAST_02 - FAST GIT COMMIT! 🔥🔥🔥"
echo "⚡ EATING CODE AND COMMITTING TO GIT!"
echo ""

cd /Users/m2ultra/NOIZYLAB

# Initialize if needed
if [ ! -d ".git" ]; then
    echo "🔧 Initializing git..."
    git init
    echo "✅ Git initialized!"
fi

# Add gitignore if needed
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.db
*.sqlite
*.log
*.pid
.DS_Store
.env
node_modules/
dist/
venv/
env/
EOF
    echo "✅ .gitignore created"
fi

# Add all files
echo "🔥 Adding all files..."
git add -A

# Commit
echo "💾 Committing..."
git commit -m "🔥 CURSE_BEAST_02: Complete NoizyLab system - All features (145+), TypeScript+Python unified, MC96 Universe, Jumbo Frames, AI systems, Complete automation" || echo "ℹ️  Nothing to commit or already committed"

echo ""
echo "✅ GIT COMMIT COMPLETE!"
echo ""
echo "📋 To push to GitHub:"
echo "   1. Create repo: github.com/noizylab/noizylab-portal"
echo "   2. Run: git remote add origin https://github.com/noizylab/noizylab-portal.git"
echo "   3. Run: git branch -M main"
echo "   4. Run: git push -u origin main"
echo ""
echo "🔥 CODE EATEN AND COMMITTED BY CURSE_BEAST_02! 🔥"

