#!/bin/bash
# 🐟 GLOBAL FISHNET - NOIZYFISH CODE HARVESTER
# Harvests ALL code from M2Ultra + All Volumes
# Created: January 2, 2026 - ANTHROPIC FELLOWS DEADLINE: Jan 12, 2026

HARVEST_DIR="/Users/m2ultra/NOIZYLAB/GLOBAL_HARVEST_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$HARVEST_DIR"/{python,javascript,typescript,rust,cpp,swift,shell,sql,config}

echo "🐟 GLOBAL FISHNET ACTIVATED"
echo "=========================="
echo "Target: $HARVEST_DIR"

harvest_local() {
    local src="$1"
    local name="$2"
    echo "🎣 Harvesting: $name"
    
    find "$src" -maxdepth 8 -type f \( \
        -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx" \
        -o -name "*.jsx" -o -name "*.rs" -o -name "*.cpp" -o -name "*.swift" \
        -o -name "*.sh" -o -name "*.sql" -o -name "*.ipynb" \) \
        ! -path "*/node_modules/*" ! -path "*/.git/*" ! -path "*/venv/*" \
        ! -path "*/__pycache__/*" ! -path "*/dist/*" \
        -size -1M 2>/dev/null | head -3000 | while read -r file; do
        
        ext="${file##*.}"
        base=$(basename "$file")
        hash=$(echo "$file" | md5 | cut -c1-8)
        
        case "$ext" in
            py|ipynb) cp "$file" "$HARVEST_DIR/python/${name}__${hash}__${base}" 2>/dev/null ;;
            js) cp "$file" "$HARVEST_DIR/javascript/${name}__${hash}__${base}" 2>/dev/null ;;
            ts|tsx) cp "$file" "$HARVEST_DIR/typescript/${name}__${hash}__${base}" 2>/dev/null ;;
            rs) cp "$file" "$HARVEST_DIR/rust/${name}__${hash}__${base}" 2>/dev/null ;;
            cpp|c|h) cp "$file" "$HARVEST_DIR/cpp/${name}__${hash}__${base}" 2>/dev/null ;;
            swift) cp "$file" "$HARVEST_DIR/swift/${name}__${hash}__${base}" 2>/dev/null ;;
            sh|bash|zsh) cp "$file" "$HARVEST_DIR/shell/${name}__${hash}__${base}" 2>/dev/null ;;
            sql) cp "$file" "$HARVEST_DIR/sql/${name}__${hash}__${base}" 2>/dev/null ;;
            *) cp "$file" "$HARVEST_DIR/config/${name}__${hash}__${base}" 2>/dev/null ;;
        esac
    done
    echo "   ✅ $name done"
}

echo "📍 PHASE 1: M2ULTRA LOCAL"
harvest_local "/Users/m2ultra/NOIZYLAB" "NOIZYLAB"
harvest_local "/Users/m2ultra/PROJECTS" "PROJECTS"
harvest_local "/Users/m2ultra/GITHUB_HARVEST" "GITHUB"
harvest_local "/Users/m2ultra/NOIZY.AI" "NOIZY_AI"
harvest_local "/Users/m2ultra/noizyhive" "NOIZYHIVE"

echo "💾 PHASE 2: EXTERNAL VOLUMES"
for vol in "/Volumes/4TBSG" "/Volumes/4TB Lacie" "/Volumes/RED DRAGON" "/Volumes/JOE" "/Volumes/4TB BLK" "/Volumes/12TB" "/Volumes/6TB"; do
    [ -d "$vol" ] && harvest_local "$vol" "$(basename "$vol" | tr ' ' '_')"
done

echo ""
echo "📊 HARVEST COMPLETE!"
echo "Python: $(ls "$HARVEST_DIR/python" 2>/dev/null | wc -l)"
echo "JavaScript: $(ls "$HARVEST_DIR/javascript" 2>/dev/null | wc -l)"
echo "TypeScript: $(ls "$HARVEST_DIR/typescript" 2>/dev/null | wc -l)"
echo "Shell: $(ls "$HARVEST_DIR/shell" 2>/dev/null | wc -l)"
echo "Location: $HARVEST_DIR"
