#!/usr/bin/env python3
"""
🔊 NOIZYLAB - Folder Keeper
Ensures empty directories have .empty placeholders for git
Fish Music Inc - CB_01
🔥 GORUNFREE! 🎸🔥
"""

import os
from pathlib import Path


class FolderKeeper:
    """Maintain folder structure with .empty placeholders"""

    def enforce(self, path="."):
        """Add .empty to all empty directories"""
        for root, dirs, files in os.walk(path):
            if root.startswith("./.git") or "/.git" in root:
                continue
            if not files and not dirs:
                placeholder = os.path.join(root, ".empty")
                if not os.path.exists(placeholder):
                    open(placeholder, "w").close()
                    print("ENGR: Added placeholder to", root)

    def clean_gitkeep(self, path="."):
        """Replace all .gitkeep with .empty"""
        for root, dirs, files in os.walk(path):
            for f in files:
                if f == ".gitkeep":
                    old = os.path.join(root, f)
                    new = os.path.join(root, ".empty")
                    os.rename(old, new)
                    print("Replaced:", old, "→", new)
        print("✔ All .gitkeep files replaced with .empty")

    def status(self, path="."):
        """Show folder structure status"""
        empty_dirs = []
        placeholder_dirs = []
        
        for root, dirs, files in os.walk(path):
            if "/.git" in root or root.startswith("./.git"):
                continue
            
            has_empty = ".empty" in files or ".gitkeep" in files
            is_empty = len([f for f in files if not f.startswith(".")]) == 0 and not dirs
            
            if has_empty:
                placeholder_dirs.append(root)
            elif is_empty:
                empty_dirs.append(root)
        
        print(f"📁 FOLDER STATUS ({path})")
        print(f"   ✅ With placeholders: {len(placeholder_dirs)}")
        print(f"   ⚠️  Empty (need placeholder): {len(empty_dirs)}")
        
        if empty_dirs:
            print("\n   Missing placeholders:")
            for d in empty_dirs[:10]:
                print(f"      - {d}")
            if len(empty_dirs) > 10:
                print(f"      ... and {len(empty_dirs) - 10} more")
        
        return {"placeholder": placeholder_dirs, "empty": empty_dirs}


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='NOIZYLAB Folder Keeper')
    parser.add_argument('path', nargs='?', default='.', help='Path to scan')
    parser.add_argument('--enforce', action='store_true', help='Add .empty to empty dirs')
    parser.add_argument('--clean', action='store_true', help='Replace .gitkeep with .empty')
    parser.add_argument('--status', action='store_true', help='Show status only')
    args = parser.parse_args()
    
    keeper = FolderKeeper()
    
    if args.clean:
        keeper.clean_gitkeep(args.path)
    elif args.enforce:
        keeper.enforce(args.path)
    else:
        keeper.status(args.path)
    
    print("\n🔥 GORUNFREE! 🎸🔥")


if __name__ == "__main__":
    main()
