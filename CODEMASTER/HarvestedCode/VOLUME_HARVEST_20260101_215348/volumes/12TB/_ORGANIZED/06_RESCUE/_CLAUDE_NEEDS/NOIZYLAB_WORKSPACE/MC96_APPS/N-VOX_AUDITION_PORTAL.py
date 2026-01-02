#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎙️ N-VOX AUDITION PORTAL 🎙️                                     ║
║                                                                           ║
║  Interactive Voice Chat & Audition System                                ║
║  GORUNFREE! BITW 1000X Quality                                           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from pathlib import Path
import subprocess
import json
from datetime import datetime
import threading


class NVOXAuditionPortal:
    """Interactive desktop voice chat and audition portal."""

    def __init__(self, root):
        self.root = root
        self.root.title("🎙️ N-VOX AUDITION PORTAL - GORUNFREE!")
        self.root.geometry("1400x900")
        self.root.configure(bg="#1a1a2e")

        # Paths
        self.noizyvox_path = Path("/Volumes/12TB 1/NOIZYVOX")
        self.models_path = self.noizyvox_path / "VOICES" / "MODELS"
        self.catalog_path = self.models_path / "MODEL_CATALOG.json"

        # Load models
        self.models = self.load_models()
        self.current_model = None
        self.current_audio_process = None

        # Chat history
        self.chat_history = []

        # Create UI
        self.create_ui()

        # Load models list
        self.refresh_models()

    def load_models(self):
        """Load voice models from catalog."""
        if self.catalog_path.exists():
            with open(self.catalog_path, 'r') as f:
                catalog = json.load(f)
                return catalog.get("models", [])
        return []

    def create_ui(self):
        """Create the user interface."""

        # Header
        header = tk.Frame(self.root, bg="#0f3460", height=80)
        header.pack(fill=tk.X, padx=10, pady=10)

        title = tk.Label(
            header,
            text="🎙️ N-VOX AUDITION PORTAL",
            font=("Arial", 28, "bold"),
            bg="#0f3460",
            fg="#00d4ff"
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            header,
            text="FULL INTERACTIVE VOICE CHAT - Talk With Each Character!",
            font=("Arial", 13, "bold"),
            bg="#0f3460",
            fg="#00ff88"
        )
        subtitle.pack()

        # Main container
        main_container = tk.Frame(self.root, bg="#1a1a2e")
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left panel - Models list
        left_panel = tk.Frame(main_container, bg="#16213e", width=280)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))

        models_label = tk.Label(
            left_panel,
            text="🎭 VOICE MODELS",
            font=("Arial", 14, "bold"),
            bg="#16213e",
            fg="#00d4ff"
        )
        models_label.pack(pady=10)

        # Models listbox
        self.models_listbox = tk.Listbox(
            left_panel,
            bg="#0f3460",
            fg="#ffffff",
            font=("Arial", 11),
            selectbackground="#00d4ff",
            selectforeground="#000000",
            height=25
        )
        self.models_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.models_listbox.bind("<<ListboxSelect>>", self.on_model_select)

        # Refresh button
        refresh_btn = tk.Button(
            left_panel,
            text="🔄 Refresh Models",
            command=self.refresh_models,
            bg="#00d4ff",
            fg="#000000",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        refresh_btn.pack(pady=10, padx=10, fill=tk.X)

        # Load audio button
        load_btn = tk.Button(
            left_panel,
            text="📂 Load Audio File",
            command=self.load_and_play_audio,
            bg="#ff8800",
            fg="#000000",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        load_btn.pack(pady=10, padx=10, fill=tk.X)

        # Right panel - Chat interface
        right_panel = tk.Frame(main_container, bg="#16213e")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Character info header
        self.char_info_label = tk.Label(
            right_panel,
            text="Select a character to begin chatting",
            font=("Arial", 16, "bold"),
            bg="#16213e",
            fg="#00d4ff",
            height=2
        )
        self.char_info_label.pack(pady=10, fill=tk.X)

        # Chat display
        chat_frame = tk.Frame(right_panel, bg="#16213e")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        chat_label = tk.Label(
            chat_frame,
            text="💬 INTERACTIVE CHAT",
            font=("Arial", 14, "bold"),
            bg="#16213e",
            fg="#00d4ff"
        )
        chat_label.pack(pady=(0, 10))

        # Chat history
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            bg="#0f3460",
            fg="#ffffff",
            font=("Arial", 12),
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)

        # Configure text tags for styling
        self.chat_display.tag_config("user", foreground="#00ff88", font=("Arial", 12, "bold"))
        self.chat_display.tag_config("character", foreground="#00d4ff", font=("Arial", 12, "bold"))
        self.chat_display.tag_config("system", foreground="#ffaa00", font=("Arial", 11, "italic"))

        # Input frame
        input_frame = tk.Frame(right_panel, bg="#16213e")
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        input_label = tk.Label(
            input_frame,
            text="📝 Type your message (character will respond with voice):",
            font=("Arial", 11, "bold"),
            bg="#16213e",
            fg="#00d4ff"
        )
        input_label.pack(pady=(0, 5))

        # Input text box
        self.input_text = tk.Text(
            input_frame,
            bg="#0f3460",
            fg="#ffffff",
            font=("Arial", 12),
            height=3,
            wrap=tk.WORD
        )
        self.input_text.pack(fill=tk.X, pady=5)
        self.input_text.bind("<Return>", self.on_enter_key)

        # Send button
        self.send_btn = tk.Button(
            input_frame,
            text="🎤 SEND & SPEAK",
            command=self.send_message,
            bg="#00ff88",
            fg="#000000",
            font=("Arial", 14, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            height=2,
            state=tk.DISABLED
        )
        self.send_btn.pack(fill=tk.X, pady=5)

        # Quick phrase buttons
        quick_frame = tk.Frame(input_frame, bg="#16213e")
        quick_frame.pack(fill=tk.X, pady=10)

        quick_label = tk.Label(
            quick_frame,
            text="⚡ Quick Phrases:",
            font=("Arial", 10, "bold"),
            bg="#16213e",
            fg="#ffaa00"
        )
        quick_label.pack(side=tk.LEFT, padx=5)

        quick_phrases = [
            "Hello! How are you?",
            "Tell me about yourself",
            "What can you teach me?",
            "Let's have fun!",
            "Goodbye!"
        ]

        for phrase in quick_phrases:
            btn = tk.Button(
                quick_frame,
                text=phrase,
                command=lambda p=phrase: self.quick_phrase(p),
                bg="#0f3460",
                fg="#ffffff",
                font=("Arial", 9),
                relief=tk.FLAT,
                cursor="hand2"
            )
            btn.pack(side=tk.LEFT, padx=3)

        # Control buttons
        control_frame = tk.Frame(right_panel, bg="#16213e")
        control_frame.pack(fill=tk.X, padx=10, pady=5)

        self.stop_btn = tk.Button(
            control_frame,
            text="⏹️ Stop",
            command=self.stop_audio,
            bg="#ff4444",
            fg="#ffffff",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = tk.Button(
            control_frame,
            text="🗑️ Clear Chat",
            command=self.clear_chat,
            bg="#666666",
            fg="#ffffff",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)

        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready - Select a voice model to begin interactive chat",
            font=("Arial", 11),
            bg="#0f3460",
            fg="#00d4ff",
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=5)

    def refresh_models(self):
        """Refresh models list."""
        self.models = self.load_models()
        self.models_listbox.delete(0, tk.END)

        if not self.models:
            self.models_listbox.insert(tk.END, "No models found")
            self.update_status("No voice models found in catalog", "warning")
            return

        # Group by type
        fishy_models = [m for m in self.models if m['character_name'] in
                       ['Captain Finn', 'Bubbles', 'Professor Scales', 'Marina Melody', 'Reef Explorer', 'Grandma Pearl']]
        musi_models = [m for m in self.models if m not in fishy_models]

        if fishy_models:
            self.models_listbox.insert(tk.END, "🐠 FISHY STORYS:")
            for model in fishy_models:
                display_name = f"   {model['character_name']}"
                self.models_listbox.insert(tk.END, display_name)

        if musi_models:
            self.models_listbox.insert(tk.END, "")
            self.models_listbox.insert(tk.END, "🏝️ MUSI TEACHERS:")
            for model in musi_models:
                display_name = f"   {model['character_name']}"
                self.models_listbox.insert(tk.END, display_name)

        self.update_status(f"Loaded {len(self.models)} voice models", "success")

    def on_model_select(self, event):
        """Handle model selection."""
        selection = self.models_listbox.curselection()
        if not selection:
            return

        index = selection[0]
        selected_text = self.models_listbox.get(index)

        # Skip headers
        if selected_text.startswith("🐠") or selected_text.startswith("🏝️") or not selected_text.strip():
            return

        # Find model by name
        character_name = selected_text.strip()
        for model in self.models:
            if model['character_name'] == character_name:
                self.current_model = model
                self.activate_character()
                break

    def activate_character(self):
        """Activate selected character for chat."""
        if not self.current_model:
            return

        # Update header
        self.char_info_label.config(
            text=f"🎭 Chatting with: {self.current_model['character_name']} "
                 f"(Quality: {self.current_model['overall_quality_score']}/100)"
        )

        # Enable send button
        self.send_btn.config(state=tk.NORMAL)

        # Add system message
        self.add_chat_message(
            "system",
            f"\n{'='*60}\nConnected to {self.current_model['character_name']}!\n"
            f"Framework: {self.current_model['framework']} | "
            f"Training: {self.current_model['training_words']:,} words\n{'='*60}\n"
        )

        self.update_status(f"Ready to chat with {self.current_model['character_name']}", "success")

    def add_chat_message(self, speaker, message):
        """Add message to chat display."""
        self.chat_display.config(state=tk.NORMAL)

        if speaker == "user":
            self.chat_display.insert(tk.END, "\nYou: ", "user")
            self.chat_display.insert(tk.END, f"{message}\n")
        elif speaker == "character":
            char_name = self.current_model['character_name'] if self.current_model else "Character"
            self.chat_display.insert(tk.END, f"\n{char_name}: ", "character")
            self.chat_display.insert(tk.END, f"{message}\n")
        elif speaker == "system":
            self.chat_display.insert(tk.END, message, "system")

        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def send_message(self):
        """Send user message and get voice response."""
        if not self.current_model:
            self.update_status("Please select a character first", "error")
            return

        user_message = self.input_text.get("1.0", tk.END).strip()
        if not user_message:
            self.update_status("Please type a message", "error")
            return

        # Add user message to chat
        self.add_chat_message("user", user_message)

        # Clear input
        self.input_text.delete("1.0", tk.END)

        # Generate character response (in production, would use AI/TTS)
        self.generate_response(user_message)

    def generate_response(self, user_message):
        """Generate character voice response."""
        # For now, echo with character personality
        # In production, this would use AI to generate response + TTS to speak it

        responses = {
            "Captain Finn": "Ahoy there! That's a fine question, matey. In my many years at sea...",
            "Bubbles": "Ooh ooh! I love that! Let me tell you something super fun!",
            "Professor Scales": "Excellent inquiry! Let me explain this from a scientific perspective...",
            "Marina Melody": "How wonderful! Music and joy are what life is all about!",
            "Reef Explorer": "Awesome! That reminds me of an adventure I had last week!",
            "Grandma Pearl": "Oh my dear, what a sweet thing to say! Let me share some wisdom...",
            "Maestro Melody": "Magnificent! Music is the language of the soul, you know...",
            "Rhythm Ray": "Yeah! Let's get that beat going! Feel the rhythm!",
            "Harmony Hana": "Beautiful! Harmony is when everything comes together perfectly...",
            "Tempo Tim": "Quick! Keep the pace! Time is everything in music!",
            "Note Nancy": "Let's read those notes carefully! Each one tells a story...",
            "Scale Sam": "Scales are the foundation! Let's practice together!",
            "Dynamics Dana": "Listen to the volume! Sometimes soft, sometimes loud!",
            "Instrument Izzy": "Every instrument has its own voice! Let me show you!"
        }

        char_name = self.current_model['character_name']
        response = responses.get(char_name, "Thank you for chatting with me!")

        # Add character response
        self.add_chat_message("character", response)

        # "Speak" the response (placeholder - would use TTS in production)
        self.update_status(f"{char_name} is speaking...", "info")

        # Simulate speaking
        threading.Thread(target=self._speak_thread, args=(response,), daemon=True).start()

    def _speak_thread(self, text):
        """Background speech thread."""
        # Placeholder - in production would synthesize speech with TTS
        import time
        time.sleep(2)  # Simulate speaking duration
        self.root.after(0, self.update_status, "Ready for next message", "success")

    def quick_phrase(self, phrase):
        """Insert quick phrase."""
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert("1.0", phrase)

    def on_enter_key(self, event):
        """Handle Enter key."""
        if event.state & 0x1:  # Shift+Enter = new line
            return
        else:  # Just Enter = send
            self.send_message()
            return "break"

    def load_and_play_audio(self):
        """Load and play an audio file."""
        file_path = filedialog.askopenfilename(
            title="Select Audio File",
            initialdir=self.noizyvox_path,
            filetypes=[
                ("Audio Files", "*.wav *.mp3 *.m4a *.aiff *.flac"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        self.add_chat_message("system", f"\n▶️ Playing audio file: {Path(file_path).name}\n")
        self.update_status(f"Playing: {Path(file_path).name}", "info")

        # Play audio
        threading.Thread(target=self._play_audio_thread, args=(file_path,), daemon=True).start()

    def _play_audio_thread(self, file_path):
        """Background audio playback thread."""
        try:
            self.current_audio_process = subprocess.Popen(["afplay", file_path])
            self.root.after(0, lambda: self.stop_btn.config(state=tk.NORMAL))
            self.current_audio_process.wait()
            self.root.after(0, lambda: self.stop_btn.config(state=tk.DISABLED))
            self.root.after(0, self.update_status, "Playback complete", "success")
        except Exception as e:
            self.root.after(0, self.update_status, f"Playback error: {str(e)}", "error")
            self.root.after(0, lambda: self.stop_btn.config(state=tk.DISABLED))

    def stop_audio(self):
        """Stop current audio playback."""
        if self.current_audio_process:
            self.current_audio_process.terminate()
            self.current_audio_process = None
            self.stop_btn.config(state=tk.DISABLED)
            self.update_status("Audio stopped", "info")

    def clear_chat(self):
        """Clear chat history."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete("1.0", tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_history = []
        self.update_status("Chat cleared", "info")

    def update_status(self, message, status_type="info"):
        """Update status bar."""
        colors = {
            "info": "#00d4ff",
            "success": "#00ff88",
            "warning": "#ffaa00",
            "error": "#ff4444"
        }

        icons = {
            "info": "ℹ️",
            "success": "✅",
            "warning": "⚠️",
            "error": "❌"
        }

        self.status_bar.config(
            text=f"{icons.get(status_type, 'ℹ️')} {message}",
            fg=colors.get(status_type, "#00d4ff")
        )


def main():
    """Main entry point."""
    root = tk.Tk()
    app = NVOXAuditionPortal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
