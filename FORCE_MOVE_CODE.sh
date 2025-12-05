#!/bin/bash
# FORCE_MOVE_CODE.sh
# Force copy all code files then delete from system drive

HOME_DIR="/Users/rsp_ms"
BACKUP_DIR="/Volumes/4TB_02/CODE_MASTER/System_Backup"

echo "🚨 FORCE COPY AND DELETE - Moving all code files"
echo ""

# Create backup directories
mkdir -p "$BACKUP_DIR/.config"
mkdir -p "$BACKUP_DIR/.windsurf"
mkdir -p "$BACKUP_DIR/.codegpt"
mkdir -p "$BACKUP_DIR/.gemini"
mkdir -p "$BACKUP_DIR/.rest-client"

# Function to copy and delete
copy_and_delete() {
    local src="$1"
    local dest="$2"
    local name="$3"
    
    if [ ! -e "$src" ]; then
        echo "⏭️  $name: Not found"
        return 0
    fi
    
    echo "📦 $name..."
    
    if [ -d "$src" ]; then
        cp -R "$src" "$dest" 2>/dev/null
        if [ $? -eq 0 ]; then
            rm -rf "$src" 2>/dev/null
            echo "   ✅ Copied and deleted"
        else
            echo "   ❌ Copy failed"
        fi
    else
        mkdir -p "$(dirname "$dest")"
        cp -f "$src" "$dest" 2>/dev/null
        if [ $? -eq 0 ]; then
            rm -f "$src" 2>/dev/null
            echo "   ✅ Copied and deleted"
        else
            echo "   ❌ Copy failed"
        fi
    fi
}

# Move directories
copy_and_delete "$HOME_DIR/.config/gcloud" "$BACKUP_DIR/.config/gcloud" ".config/gcloud"
copy_and_delete "$HOME_DIR/.config/configstore" "$BACKUP_DIR/.config/configstore" ".config/configstore"
copy_and_delete "$HOME_DIR/.config/Dadroit" "$BACKUP_DIR/.config/Dadroit" ".config/Dadroit"
copy_and_delete "$HOME_DIR/.rest-client" "$BACKUP_DIR/.rest-client" ".rest-client"
copy_and_delete "$HOME_DIR/.codegpt" "$BACKUP_DIR/.codegpt" ".codegpt"
copy_and_delete "$HOME_DIR/.gemini" "$BACKUP_DIR/.gemini" ".gemini"

# Move .windsurf Python files
echo "📁 .windsurf Python files..."
find "$HOME_DIR/.windsurf/extensions" -type f \( -name "*.py" -o -name "*.js" -o -name "*.json" \) \
    -not -path "*/node_modules/*" 2>/dev/null | while read file; do
    rel_path="${file#$HOME_DIR/.windsurf/}"
    dest="$BACKUP_DIR/.windsurf/$rel_path"
    mkdir -p "$(dirname "$dest")"
    cp -f "$file" "$dest" 2>/dev/null && rm -f "$file" 2>/dev/null && echo "   ✅ $(basename "$file")" || true
done

echo ""
echo "📊 Summary:"
du -sh "$BACKUP_DIR" 2>/dev/null
echo ""
echo "✅ Force copy and delete complete!"

