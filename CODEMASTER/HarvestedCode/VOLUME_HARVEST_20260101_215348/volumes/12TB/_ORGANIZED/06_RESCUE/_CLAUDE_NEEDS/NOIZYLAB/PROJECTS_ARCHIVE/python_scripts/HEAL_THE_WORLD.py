#!/usr/bin/env python3
"""
HEAL THE WORLD - Comprehensive System Cleanup & Organization
Cleans and organizes the entire Mac system while preserving custom folders
"""

import os
import shutil
import json
import hashlib
import datetime
from pathlib import Path
import subprocess

# ============= CONFIGURATION =============
HOME = Path.home()
PROTECTED_FOLDERS = {
    "Documents/_CUSTOM_FOLDERS",
    "Applications",
    "Applications (Parallels)",
    "Library",
    "System",
    ".Trash",
}

# Organization Structure
ORGANIZATION_MAP = {
    # Development Projects
    "DEVELOPMENT": {
        "path": HOME / "Documents" / "DEVELOPMENT",
        "patterns": [
            "*.py",
            "*.js",
            "*.ts",
            "*.swift",
            "*.go",
            "*.java",
            "*.cpp",
            "*.c",
        ],
        "folders": ["src", "app", "core", "lib", "api", "backend", "frontend"],
    },
    # NoizyLab Projects
    "NOIZYLAB_PROJECTS": {
        "path": HOME / "Documents" / "NOIZYLAB_PROJECTS",
        "patterns": ["noizylab*", "mission*", "dgs*", "mc96*", "fleet*"],
        "folders": ["noizylab*", "MissionControl*", "DGS*", "MC96*"],
    },
    # Scripts & Automation
    "SCRIPTS_AUTOMATION": {
        "path": HOME / "Documents" / "SCRIPTS_AUTOMATION",
        "patterns": ["*.sh", "*.ps1", "*.bat", "*script*", "*automation*"],
        "folders": ["scripts", "Scripts", "PowerShell", "WindowsPowerShell"],
    },
    # Configuration Files
    "CONFIGURATIONS": {
        "path": HOME / "Documents" / "CONFIGURATIONS",
        "patterns": ["*.json", "*.yaml", "*.yml", "*.ini", "*.cfg", "*.conf"],
        "folders": ["config", "configs", ".vscode", ".config"],
    },
    # Archives & Backups
    "ARCHIVES": {
        "path": HOME / "Documents" / "ARCHIVES",
        "patterns": ["*backup*", "*archive*", "*old*", "*_old", "*_bak"],
        "folders": ["Archives", "Backup*", "*_backup", "*_archive"],
    },
    # Media & Assets
    "MEDIA_ASSETS": {
        "path": HOME / "Documents" / "MEDIA_ASSETS",
        "patterns": ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.svg", "*.ico"],
        "folders": ["assets", "images", "Pictures", "PIX", "00_images*"],
    },
    # Documentation
    "DOCUMENTATION": {
        "path": HOME / "Documents" / "DOCUMENTATION",
        "patterns": ["*.md", "*.txt", "*.rtf", "*.pdf", "README*"],
        "folders": ["docs", "Documentation", "README*"],
    },
}


class HealTheWorld:
    def __init__(self):
        self.log_file = HOME / "HEAL_THE_WORLD_LOG.txt"
        self.duplicates_found = []
        self.moves_made = []
        self.errors = []

    def log(self, message):
        """Log messages to both console and file"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)

        with open(self.log_file, "a") as f:
            f.write(log_entry + "\n")

    def is_protected(self, path):
        """Check if path is in protected folders"""
        path_str = str(path)
        for protected in PROTECTED_FOLDERS:
            if protected in path_str:
                return True
        return False

    def get_file_hash(self, filepath):
        """Get MD5 hash of file for duplicate detection"""
        try:
            with open(filepath, "rb") as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return None

    def find_duplicates(self, directory):
        """Find duplicate files in directory"""
        self.log(f"🔍 Scanning for duplicates in {directory}")

        file_hashes = {}
        duplicates = []

        for root, dirs, files in os.walk(directory):
            # Skip protected folders
            if self.is_protected(Path(root)):
                continue

            for file in files:
                if file.startswith("."):
                    continue

                filepath = Path(root) / file
                file_hash = self.get_file_hash(filepath)

                if file_hash:
                    if file_hash in file_hashes:
                        duplicates.append(
                            {"original": file_hashes[file_hash], "duplicate": filepath}
                        )
                    else:
                        file_hashes[file_hash] = filepath

        return duplicates

    def create_organization_structure(self):
        """Create the organized folder structure"""
        self.log("🏗️ Creating organization structure...")

        for category, config in ORGANIZATION_MAP.items():
            target_path = config["path"]
            target_path.mkdir(parents=True, exist_ok=True)
            self.log(f"✅ Created {target_path}")

    def should_move_to_category(self, path, category_config):
        """Check if item should be moved to this category"""
        path_name = path.name.lower()

        # Check file patterns
        for pattern in category_config.get("patterns", []):
            if path.is_file() and path_name.endswith(pattern.replace("*", "")):
                return True
            if "*" in pattern and pattern.replace("*", "") in path_name:
                return True

        # Check folder patterns
        for folder_pattern in category_config.get("folders", []):
            if path.is_dir():
                if "*" in folder_pattern:
                    if folder_pattern.replace("*", "") in path_name:
                        return True
                elif path_name == folder_pattern.lower():
                    return True

        return False

    def organize_items(self, source_dir):
        """Organize items from source directory"""
        self.log(f"📁 Organizing items from {source_dir}")

        if not Path(source_dir).exists():
            return

        for item in Path(source_dir).iterdir():
            if item.name.startswith("."):
                continue

            if self.is_protected(item):
                self.log(f"⚠️ Skipping protected: {item}")
                continue

            # Find best category for this item
            best_category = None
            for category, config in ORGANIZATION_MAP.items():
                if self.should_move_to_category(item, config):
                    best_category = category
                    break

            if best_category:
                self.move_to_category(item, best_category)

    def move_to_category(self, source_path, category):
        """Move item to appropriate category folder"""
        config = ORGANIZATION_MAP[category]
        target_dir = config["path"]
        target_path = target_dir / source_path.name

        try:
            # Handle name conflicts
            counter = 1
            while target_path.exists():
                name_parts = source_path.name.rsplit(".", 1)
                if len(name_parts) == 2:
                    new_name = f"{name_parts[0]}_{counter}.{name_parts[1]}"
                else:
                    new_name = f"{source_path.name}_{counter}"
                target_path = target_dir / new_name
                counter += 1

            shutil.move(str(source_path), str(target_path))
            self.moves_made.append(f"{source_path} → {target_path}")
            self.log(f"✅ Moved: {source_path.name} → {category}")

        except Exception as e:
            error_msg = f"❌ Error moving {source_path}: {str(e)}"
            self.errors.append(error_msg)
            self.log(error_msg)

    def remove_duplicates(self, directory):
        """Remove duplicate files"""
        duplicates = self.find_duplicates(directory)

        if not duplicates:
            self.log("✅ No duplicates found")
            return

        self.log(f"🗑️ Found {len(duplicates)} duplicates")

        for dup in duplicates:
            try:
                # Keep the file in a more organized location
                if "Documents" in str(dup["original"]) and "Desktop" in str(
                    dup["duplicate"]
                ):
                    os.remove(dup["duplicate"])
                    self.log(f"🗑️ Removed duplicate: {dup['duplicate']}")
                else:
                    # Remove the one with longer path (likely less organized)
                    if len(str(dup["duplicate"])) > len(str(dup["original"])):
                        os.remove(dup["duplicate"])
                        self.log(f"🗑️ Removed duplicate: {dup['duplicate']}")
                    else:
                        os.remove(dup["original"])
                        self.log(f"🗑️ Removed duplicate: {dup['original']}")

                self.duplicates_found.append(dup)

            except Exception as e:
                error_msg = f"❌ Error removing duplicate {dup['duplicate']}: {str(e)}"
                self.errors.append(error_msg)
                self.log(error_msg)

    def clean_empty_folders(self, directory):
        """Remove empty folders"""
        self.log(f"🧹 Cleaning empty folders in {directory}")

        for root, dirs, files in os.walk(directory, topdown=False):
            if self.is_protected(Path(root)):
                continue

            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                try:
                    if not any(dir_path.iterdir()):
                        dir_path.rmdir()
                        self.log(f"🗑️ Removed empty folder: {dir_path}")
                except:
                    pass

    def generate_report(self):
        """Generate cleanup report"""
        report_path = HOME / "HEAL_THE_WORLD_REPORT.txt"

        with open(report_path, "w") as f:
            f.write("=" * 60 + "\n")
            f.write("HEAL THE WORLD - CLEANUP REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Generated: {datetime.datetime.now()}\n\n")

            f.write(f"📊 SUMMARY:\n")
            f.write(f"- Files moved: {len(self.moves_made)}\n")
            f.write(f"- Duplicates removed: {len(self.duplicates_found)}\n")
            f.write(f"- Errors: {len(self.errors)}\n\n")

            if self.moves_made:
                f.write("📁 FILES MOVED:\n")
                for move in self.moves_made:
                    f.write(f"  {move}\n")
                f.write("\n")

            if self.duplicates_found:
                f.write("🗑️ DUPLICATES REMOVED:\n")
                for dup in self.duplicates_found:
                    f.write(f"  {dup['duplicate']}\n")
                f.write("\n")

            if self.errors:
                f.write("❌ ERRORS:\n")
                for error in self.errors:
                    f.write(f"  {error}\n")

        self.log(f"📋 Report generated: {report_path}")

    def heal_the_world(self):
        """Main healing process"""
        self.log("🌍 HEAL THE WORLD - Starting global cleanup...")

        # Create organization structure
        self.create_organization_structure()

        # Organize main directories
        directories_to_organize = [
            HOME / "Desktop",
            HOME / "Downloads",
            HOME / "Documents" / "noizylab_2026_projects",
            HOME / "NoizyLab_2026_Projects",
        ]

        for directory in directories_to_organize:
            if directory.exists():
                self.organize_items(directory)
                self.remove_duplicates(directory)
                self.clean_empty_folders(directory)

        # Generate final report
        self.generate_report()

        self.log("🌍 HEAL THE WORLD - Complete! The world is healed! ✨")


if __name__ == "__main__":
    healer = HealTheWorld()
    healer.heal_the_world()
