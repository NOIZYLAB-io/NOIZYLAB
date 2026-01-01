#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# 🌌 NOIZYLAB UNIVERSAL SYNC SCRIPT
# Synchronizes ALL NOIZYLAB repositories with smart conflict detection
# ═══════════════════════════════════════════════════════════════════════════════

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# NOIZYLAB Repos
REPOS=(
    "/Users/m2ultra/NOIZYLAB/GABRIEL"
    "/Users/m2ultra/NOIZYLAB/NOIZYLAB"
)

# Optional repos (may not exist)
OPTIONAL_REPOS=(
    "/Users/m2ultra/NOIZYLAB/NOIZYLAB_CONSOLE_v3"
)

echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                               ║"
echo "║   🌌 NOIZYLAB UNIVERSAL SYNC                                                  ║"
echo "║   Synchronizing all repositories...                                           ║"
echo "║                                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

sync_repo() {
    local repo_path=$1
    local repo_name=$(basename "$repo_path")
    
    echo -e "\n${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}📂 ${repo_name}${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    if [ ! -d "$repo_path" ]; then
        echo -e "${YELLOW}⚠️  Not found: $repo_path${NC}"
        return 1
    fi
    
    cd "$repo_path"
    
    # Check git status
    echo -e "\n${YELLOW}📋 Checking status...${NC}"
    
    # Get current branch
    branch=$(git branch --show-current)
    echo -e "   Branch: ${GREEN}$branch${NC}"
    
    # Fetch all
    echo -e "\n${YELLOW}📥 Fetching from origin...${NC}"
    git fetch --all --prune
    
    # Check for uncommitted changes
    if [ -n "$(git status --porcelain)" ]; then
        echo -e "\n${YELLOW}⚠️  Uncommitted changes detected:${NC}"
        git status --short
        
        echo -e "\n${YELLOW}Would you like to:${NC}"
        echo "  1. Stash changes and pull"
        echo "  2. Skip this repo"
        echo "  3. Show diff"
        read -p "Choice [1/2/3]: " choice
        
        case $choice in
            1)
                echo -e "${CYAN}Stashing changes...${NC}"
                git stash push -m "Auto-stash before sync $(date +%Y%m%d-%H%M%S)"
                git pull origin "$branch"
                echo -e "${CYAN}Popping stash...${NC}"
                git stash pop || echo -e "${YELLOW}Stash pop had conflicts${NC}"
                ;;
            3)
                git diff
                return 0
                ;;
            *)
                echo -e "${YELLOW}Skipping...${NC}"
                return 0
                ;;
        esac
    else
        # Check if behind
        local_rev=$(git rev-parse HEAD)
        remote_rev=$(git rev-parse "origin/$branch" 2>/dev/null || echo "")
        
        if [ -n "$remote_rev" ] && [ "$local_rev" != "$remote_rev" ]; then
            echo -e "\n${CYAN}📥 Pulling latest changes...${NC}"
            git pull origin "$branch"
            echo -e "${GREEN}✅ Updated!${NC}"
        else
            echo -e "\n${GREEN}✅ Already up to date${NC}"
        fi
    fi
    
    # Show recent commits
    echo -e "\n${YELLOW}📝 Recent commits:${NC}"
    git log --oneline -5
    
    # Show branch info
    echo -e "\n${YELLOW}🌿 Branches:${NC}"
    git branch -vv | head -5
    
    return 0
}

# Summary arrays
declare -a synced_repos
declare -a skipped_repos
declare -a failed_repos

# Sync main repos
for repo in "${REPOS[@]}"; do
    if sync_repo "$repo"; then
        synced_repos+=("$(basename $repo)")
    else
        failed_repos+=("$(basename $repo)")
    fi
done

# Sync optional repos
for repo in "${OPTIONAL_REPOS[@]}"; do
    if [ -d "$repo" ]; then
        if sync_repo "$repo"; then
            synced_repos+=("$(basename $repo)")
        else
            failed_repos+=("$(basename $repo)")
        fi
    else
        skipped_repos+=("$(basename $repo)")
    fi
done

# Summary
echo -e "\n${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════════════════════════╗"
echo "║                           SYNC COMPLETE                                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${GREEN}✅ Synced: ${synced_repos[*]:-none}${NC}"
[ ${#skipped_repos[@]} -gt 0 ] && echo -e "${YELLOW}⏭️  Skipped: ${skipped_repos[*]}${NC}"
[ ${#failed_repos[@]} -gt 0 ] && echo -e "${RED}❌ Failed: ${failed_repos[*]}${NC}"

echo -e "\n${CYAN}🚀 All NOIZYLAB repos synchronized!${NC}\n"
