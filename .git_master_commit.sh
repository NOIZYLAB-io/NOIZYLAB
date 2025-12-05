#!/bin/bash
# ⚡ MASTER GIT COMMIT SCRIPT - Commit all organized NOIZYLAB projects
# ====================================================================

set -e

BASE="/Users/m2ultra/NOIZYLAB"
GITHUB_DIR="/Users/m2ultra/Github"

echo "🚀 MASTER GIT COMMIT - NOIZYLAB Projects"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

commit_project() {
    local project_dir="$1"
    local project_name="$2"
    
    if [ ! -d "$project_dir" ]; then
        echo -e "${YELLOW}⚠️  $project_name: Directory not found${NC}"
        return 1
    fi
    
    cd "$project_dir"
    
    # Check if git repo
    if [ ! -d ".git" ]; then
        echo -e "${BLUE}📦 $project_name: Initializing git...${NC}"
        git init
        git branch -M main 2>/dev/null || true
    fi
    
    # Check for changes
    if git diff --quiet && git diff --cached --quiet; then
        echo -e "${YELLOW}⏭️  $project_name: No changes to commit${NC}"
        return 0
    fi
    
    # Add all files
    echo -e "${BLUE}📝 $project_name: Staging files...${NC}"
    git add -A 2>/dev/null || git add .
    
    # Commit
    echo -e "${BLUE}💾 $project_name: Committing...${NC}"
    git commit -m "✨ Organized structure - All code committed

- Complete project organization
- All files properly structured
- Updated paths and imports
- Ready for production" 2>/dev/null || {
        echo -e "${YELLOW}⚠️  $project_name: Nothing to commit or commit failed${NC}"
        return 1
    }
    
    echo -e "${GREEN}✅ $project_name: Committed successfully${NC}"
    return 0
}

# Commit email-intelligence
echo -e "${BLUE}📧 Processing email-intelligence...${NC}"
commit_project "$BASE/email-intelligence" "email-intelligence"

# Commit other major projects
MAJOR_PROJECTS=(
    "master-dashboard:Master Dashboard"
    "control-panel:Control Panel"
    "ai-aggregator:AI Aggregator"
    "noizylab-knowledge-system:Knowledge System"
    "ultimate-ssh-system:SSH System"
)

for project in "${MAJOR_PROJECTS[@]}"; do
    IFS=':' read -r dir name <<< "$project"
    if [ -d "$BASE/$dir" ]; then
        commit_project "$BASE/$dir" "$name"
    fi
done

echo ""
echo -e "${GREEN}✨ All projects committed!${NC}"
echo ""
echo "📤 To push to remote:"
echo "   cd $BASE/email-intelligence"
echo "   git remote add origin <repo-url>"
echo "   git push -u origin main"

