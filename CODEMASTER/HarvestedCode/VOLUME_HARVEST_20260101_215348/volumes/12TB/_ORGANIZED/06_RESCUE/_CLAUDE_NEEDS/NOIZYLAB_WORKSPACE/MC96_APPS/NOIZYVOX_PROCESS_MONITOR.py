#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        📊 NOIZYVOX PROCESS MONITOR 📊                                    ║
║                                                                           ║
║  Real-Time System Monitoring Dashboard                                   ║
║  GORUNFREE! BITW 1000X                                                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from pathlib import Path
import json
import threading
import time
from datetime import datetime
import os


class NoizyVoxProcessMonitor:
    """Real-time process monitoring dashboard."""

    def __init__(self, root):
        self.root = root
        self.root.title("📊 NOIZYVOX PROCESS MONITOR - GORUNFREE!")
        self.root.geometry("1600x1000")
        self.root.configure(bg="#0a0a0a")

        # Paths
        self.noizyvox_path = Path("/Volumes/12TB 1/NOIZYVOX")
        self.catalog_file = self.noizyvox_path / "VOICE_CATALOG.json"
        self.models_catalog = self.noizyvox_path / "VOICES" / "MODELS" / "MODEL_CATALOG.json"

        # Monitoring state
        self.running = True
        self.stats = {
            "voices_found": 0,
            "voices_processed": 0,
            "models_created": 0,
            "total_size": 0,
            "categories": {},
            "recent_files": []
        }

        # Create UI
        self.create_ui()

        # Start monitoring
        self.start_monitoring()

    def create_ui(self):
        """Create the monitoring dashboard UI."""

        # Main header
        header = tk.Frame(self.root, bg="#1a1a2e", height=100)
        header.pack(fill=tk.X, padx=10, pady=10)

        title = tk.Label(
            header,
            text="📊 NOIZYVOX LIVE PROCESS MONITOR",
            font=("Arial Black", 32, "bold"),
            bg="#1a1a2e",
            fg="#00ff88"
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            header,
            text="Real-Time Voice Harvesting & Model Creation Monitoring",
            font=("Arial", 14, "bold"),
            bg="#1a1a2e",
            fg="#00d4ff"
        )
        subtitle.pack()

        # Time display
        self.time_label = tk.Label(
            header,
            text="",
            font=("Courier", 12, "bold"),
            bg="#1a1a2e",
            fg="#ffaa00"
        )
        self.time_label.pack(pady=5)

        # Main container
        main_container = tk.Frame(self.root, bg="#0a0a0a")
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Top stats panel
        stats_panel = tk.Frame(main_container, bg="#16213e", height=200)
        stats_panel.pack(fill=tk.X, pady=(0, 10))

        # Stats boxes
        stats_container = tk.Frame(stats_panel, bg="#16213e")
        stats_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create stat boxes
        self.create_stat_box(stats_container, "🎙️ VOICES FOUND", "0", "voices_found", 0, 0)
        self.create_stat_box(stats_container, "✅ PROCESSED", "0", "processed", 0, 1)
        self.create_stat_box(stats_container, "🤖 AI MODELS", "0", "models", 0, 2)
        self.create_stat_box(stats_container, "💾 TOTAL SIZE", "0 MB", "size", 0, 3)

        # Middle section - split into categories and recent activity
        middle_container = tk.Frame(main_container, bg="#0a0a0a")
        middle_container.pack(fill=tk.BOTH, expand=True)

        # Left - Categories breakdown
        left_panel = tk.Frame(middle_container, bg="#16213e", width=600)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

        categories_label = tk.Label(
            left_panel,
            text="📂 VOICE CATEGORIES",
            font=("Arial", 16, "bold"),
            bg="#16213e",
            fg="#00d4ff"
        )
        categories_label.pack(pady=10)

        self.categories_display = scrolledtext.ScrolledText(
            left_panel,
            bg="#0f3460",
            fg="#ffffff",
            font=("Courier", 11),
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.categories_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Right - Recent activity
        right_panel = tk.Frame(middle_container, bg="#16213e")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

        activity_label = tk.Label(
            right_panel,
            text="⚡ RECENT ACTIVITY",
            font=("Arial", 16, "bold"),
            bg="#16213e",
            fg="#00ff88"
        )
        activity_label.pack(pady=10)

        self.activity_display = scrolledtext.ScrolledText(
            right_panel,
            bg="#0f3460",
            fg="#ffffff",
            font=("Courier", 10),
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.activity_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Configure text tags for activity
        self.activity_display.tag_config("new", foreground="#00ff88", font=("Courier", 10, "bold"))
        self.activity_display.tag_config("process", foreground="#00d4ff")
        self.activity_display.tag_config("model", foreground="#ffaa00")
        self.activity_display.tag_config("error", foreground="#ff4444")

        # Bottom - Models status
        bottom_panel = tk.Frame(main_container, bg="#16213e", height=200)
        bottom_panel.pack(fill=tk.X, pady=(10, 0))

        models_label = tk.Label(
            bottom_panel,
            text="🤖 AI VOICE MODELS STATUS",
            font=("Arial", 16, "bold"),
            bg="#16213e",
            fg="#ffaa00"
        )
        models_label.pack(pady=10)

        self.models_display = scrolledtext.ScrolledText(
            bottom_panel,
            bg="#0f3460",
            fg="#ffffff",
            font=("Courier", 10),
            wrap=tk.WORD,
            state=tk.DISABLED,
            height=8
        )
        self.models_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="🟢 MONITORING ACTIVE - Refreshing every 2 seconds",
            font=("Arial", 11, "bold"),
            bg="#0f3460",
            fg="#00ff88",
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=5)

    def create_stat_box(self, parent, title, value, key, row, col):
        """Create a stat display box."""
        box = tk.Frame(parent, bg="#0f3460", relief=tk.RAISED, borderwidth=2)
        box.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        parent.grid_columnconfigure(col, weight=1)

        title_label = tk.Label(
            box,
            text=title,
            font=("Arial", 12, "bold"),
            bg="#0f3460",
            fg="#00d4ff"
        )
        title_label.pack(pady=(10, 5))

        value_label = tk.Label(
            box,
            text=value,
            font=("Arial Black", 24, "bold"),
            bg="#0f3460",
            fg="#00ff88"
        )
        value_label.pack(pady=(5, 10))

        # Store reference
        setattr(self, f"{key}_label", value_label)

    def start_monitoring(self):
        """Start monitoring threads."""
        # Update time
        threading.Thread(target=self.update_time_thread, daemon=True).start()

        # Monitor catalogs
        threading.Thread(target=self.monitor_catalogs_thread, daemon=True).start()

        # Monitor filesystem
        threading.Thread(target=self.monitor_filesystem_thread, daemon=True).start()

    def update_time_thread(self):
        """Update time display."""
        while self.running:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.root.after(0, self.time_label.config, {"text": f"🕐 {current_time}"})
            time.sleep(1)

    def monitor_catalogs_thread(self):
        """Monitor catalog files for changes."""
        last_voice_count = 0
        last_model_count = 0

        while self.running:
            try:
                # Check voice catalog
                if self.catalog_file.exists():
                    with open(self.catalog_file, 'r') as f:
                        catalog = json.load(f)
                        voices = catalog.get("voices", [])
                        voice_count = len(voices)

                        if voice_count != last_voice_count:
                            self.stats["voices_found"] = voice_count
                            self.root.after(0, self.voices_found_label.config,
                                          {"text": f"{voice_count:,}"})

                            # Add to recent activity
                            if voice_count > last_voice_count:
                                new_count = voice_count - last_voice_count
                                self.add_activity(
                                    f"[HARVEST] Found {new_count} new voice file(s)! Total: {voice_count:,}",
                                    "new"
                                )
                            last_voice_count = voice_count

                        # Update categories
                        categories = {}
                        for voice in voices:
                            cat = voice.get("category", "unknown")
                            categories[cat] = categories.get(cat, 0) + 1

                        self.stats["categories"] = categories
                        self.root.after(0, self.update_categories_display)

                        # Calculate total size
                        total_size = sum(voice.get("file_size", 0) for voice in voices)
                        self.stats["total_size"] = total_size
                        size_mb = total_size / (1024 * 1024)
                        self.root.after(0, self.size_label.config,
                                      {"text": f"{size_mb:.1f} MB"})

                # Check models catalog
                if self.models_catalog.exists():
                    with open(self.models_catalog, 'r') as f:
                        models_cat = json.load(f)
                        models = models_cat.get("models", [])
                        model_count = len(models)

                        if model_count != last_model_count:
                            self.stats["models_created"] = model_count
                            self.root.after(0, self.models_label.config,
                                          {"text": f"{model_count}"})

                            if model_count > last_model_count:
                                self.add_activity(
                                    f"[MODEL] New AI voice model created! Total: {model_count}",
                                    "model"
                                )
                            last_model_count = model_count

                        # Update models display
                        self.root.after(0, self.update_models_display, models)

            except Exception as e:
                self.add_activity(f"[ERROR] Monitoring error: {str(e)}", "error")

            time.sleep(2)

    def monitor_filesystem_thread(self):
        """Monitor filesystem for new files."""
        while self.running:
            try:
                # Count processed files
                processed_count = 0
                if (self.noizyvox_path / "VOICES" / "PROCESSED").exists():
                    processed_files = list((self.noizyvox_path / "VOICES" / "PROCESSED").rglob("*.wav"))
                    processed_count = len(processed_files)

                if processed_count != self.stats.get("voices_processed", 0):
                    self.stats["voices_processed"] = processed_count
                    self.root.after(0, self.processed_label.config,
                                  {"text": f"{processed_count:,}"})

            except Exception as e:
                pass

            time.sleep(3)

    def update_categories_display(self):
        """Update categories display."""
        self.categories_display.config(state=tk.NORMAL)
        self.categories_display.delete("1.0", tk.END)

        if not self.stats["categories"]:
            self.categories_display.insert("1.0", "\n   No categories yet...\n   Waiting for voice harvest...\n")
        else:
            categories_text = "\n"
            categories_text += "  Category                    Count\n"
            categories_text += "  " + "="*45 + "\n\n"

            # Sort by count
            sorted_cats = sorted(self.stats["categories"].items(), key=lambda x: x[1], reverse=True)

            for category, count in sorted_cats:
                cat_display = category.replace("_", " ").title()
                bar_length = int((count / max(self.stats["categories"].values())) * 20)
                bar = "█" * bar_length
                categories_text += f"  {cat_display:25} {count:5,} {bar}\n"

            self.categories_display.insert("1.0", categories_text)

        self.categories_display.config(state=tk.DISABLED)

    def update_models_display(self, models):
        """Update models display."""
        self.models_display.config(state=tk.NORMAL)
        self.models_display.delete("1.0", tk.END)

        if not models:
            self.models_display.insert("1.0", "\n   No AI models created yet...\n   Run ai_voice_model_trainer.py to create models!\n")
        else:
            models_text = "\n"
            models_text += f"  {'Character':25} {'Quality':10} {'Framework':12} {'Status':10}\n"
            models_text += "  " + "="*75 + "\n\n"

            for model in models:
                name = model['character_name'][:24]
                quality = f"{model['overall_quality_score']}/100"
                framework = model['framework'][:11]
                status = "✅ Deployed" if model['is_deployed'] else "⏳ Ready"
                models_text += f"  {name:25} {quality:10} {framework:12} {status:10}\n"

            self.models_display.insert("1.0", models_text)

        self.models_display.config(state=tk.DISABLED)

    def add_activity(self, message, tag="process"):
        """Add activity message."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"

        self.activity_display.config(state=tk.NORMAL)
        self.activity_display.insert("1.0", full_message, tag)

        # Keep only last 100 lines
        lines = int(self.activity_display.index('end-1c').split('.')[0])
        if lines > 100:
            self.activity_display.delete("100.0", tk.END)

        self.activity_display.config(state=tk.DISABLED)

    def on_closing(self):
        """Handle window closing."""
        self.running = False
        self.root.destroy()


def main():
    """Main entry point."""
    root = tk.Tk()
    app = NoizyVoxProcessMonitor(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
