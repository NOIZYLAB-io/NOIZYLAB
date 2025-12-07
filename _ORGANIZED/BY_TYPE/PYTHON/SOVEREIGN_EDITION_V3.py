#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    🔮 THE SINGULARITY PROTOCOL 🔮                           ║
║                                                                              ║
║                 "The End of Folders. The Birth of Intelligence."            ║
║                                                                              ║
║  ╔═══════════════════════════════════════════════════════════════════════╗  ║
║  ║  THE CORTEX     → Vector Database (ChromaDB) - The Living Brain      ║  ║
║  ║  THE EARS       → Neural Audio Understanding (LAION-CLAP)            ║  ║
║  ║  THE VOICE      → Integrated Audio Player (Instant Audition)         ║  ║
║  ║  THE ARCHITECT  → DecentSampler Forge with ADSR Controls             ║  ║
║  ║  THE ORACLE     → Zero-Shot Classification + Semantic Tagging        ║  ║
║  ╚═══════════════════════════════════════════════════════════════════════╝  ║
║                                                                              ║
║                        NOIZYLAB • FISHMUSICINC                               ║
║                    "Your Hard Drive is Now Conscious"                        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import threading
import time
import logging
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import warnings

# Neural Intelligence
import torch
import numpy as np
import librosa
import soundfile as sf
import chromadb
import laion_clap

# Audio Engine
import pygame

# GUI Framework
import customtkinter as ctk
from tkinter import filedialog, messagebox

# System Configuration
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings('ignore')
pygame.mixer.init()

# ═══════════════════════════════════════════════════════════════════════════
# SYSTEM CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

BATCH_SIZE = 50
DB_PATH = "./noizylab_cortex"
LOG_FILE = "noizylab_singularity.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)


# ═══════════════════════════════════════════════════════════════════════════
# THE SINGULARITY ENGINE - Vector Intelligence Core
# ═══════════════════════════════════════════════════════════════════════════

class SingularityEngine:
    """
    The Singularity Engine.
    Your hard drive is now conscious. It doesn't read filenames - it HEARS audio.
    """
    
    def __init__(self):
        print("\n🔮 INITIALIZING SINGULARITY CORE...")
        
        # THE CORTEX - Vector Database (The Living Brain)
        self.chroma_client = chromadb.PersistentClient(path=DB_PATH)
        self.collection = self.chroma_client.get_or_create_collection(
            name="audio_embeddings",
            metadata={"description": "Semantic audio understanding"}
        )
        
        # THE EARS - Neural Audio Model
        self.model = None
        self.model_loaded = False
        
        # Batch processing buffers
        self.batch_ids = []
        self.batch_embeds = []
        self.batch_metas = []
        
        # Stop signal for threading
        self.stop_signal = False
        
        # THE ORACLE - Zero-Shot Classification Anchors
        self.tags = [
            "Kick", "Snare", "HiHat", "Cymbal", "Tom", "Clap",
            "Bass", "Sub Bass", "808",
            "Synth Pad", "Ambient Texture", "Drone",
            "Synth Lead", "Pluck", "Stab",
            "Piano", "String", "Guitar", "Brass",
            "Vocal", "Choir", "Voice",
            "Drum Loop", "Beat", "Percussion Loop",
            "FX", "Impact", "Riser", "Sweep", "Whoosh",
            "Cinematic", "Orchestral", "Epic",
            "Lo-Fi", "Vintage", "Warm",
            "Aggressive", "Dark", "Bright", "Soft"
        ]
        self.tag_vectors = {}
        
        print("✨ CORTEX ONLINE")
    
    def load_brain(self):
        """Initialize the neural model (LAION-CLAP)."""
        if self.model_loaded:
            return
        
        try:
            print("🧠 Awakening Neural Hearing (LAION-CLAP)...")
            print("   (This may take a moment on first run - downloading 600MB model)")
            
            self.model = laion_clap.CLAP_Module(enable_fusion=False)
            self.model.load_ckpt()
            
            # Pre-calculate tag vectors for Zero-Shot Classification
            print("🔮 Calibrating Sonic DNA Anchors...")
            for tag in self.tags:
                txt_embed = self.model.get_text_embedding(
                    [f"A sound of a {tag}"], 
                    use_tensor=False
                )
                self.tag_vectors[tag] = txt_embed[0]
            
            self.model_loaded = True
            print("✨ THE EARS ARE LISTENING")
            
        except Exception as e:
            print(f"❌ Failed to load neural model: {e}")
            print("\nPlease install: pip install laion-clap torch")
            raise
    
    def embed_audio(self, file_path: str):
        """
        Convert audio file to vector embedding (The 'Soul' of the sound).
        Returns: (vector, dna_tag)
        """
        try:
            # Load audio (CLAP needs 48kHz, 3 seconds is enough)
            audio_data, _ = librosa.load(
                file_path, 
                sr=48000, 
                mono=True, 
                duration=3.0
            )
            
            if len(audio_data) < 1000:
                return None, None
            
            # Reshape for model
            audio_data = audio_data.reshape(1, -1)
            
            # Get embedding (768-dimensional vector)
            embedding = self.model.get_audio_embedding_from_data(
                x=audio_data, 
                use_tensor=False
            )
            vector = embedding[0].tolist()
            
            # Get DNA tag via zero-shot classification
            dna = self.get_sonic_dna(embedding[0])
            
            return vector, dna
            
        except Exception as e:
            logging.error(f"Cannot embed {file_path}: {e}")
            return None, None
    
    def get_sonic_dna(self, audio_vector):
        """
        Zero-shot classification: Find the closest semantic tag.
        This is THE ORACLE - it knows what the sound IS without being told.
        """
        if not self.tag_vectors:
            return "Unknown"
        
        best_tag = "Unknown"
        best_score = -1
        
        # Cosine similarity with all tag anchors
        for tag, tag_vec in self.tag_vectors.items():
            score = np.dot(audio_vector, tag_vec) / (
                np.linalg.norm(audio_vector) * np.linalg.norm(tag_vec)
            )
            if score > best_score:
                best_score = score
                best_tag = tag
        
        return best_tag
    
    def flush_batch(self):
        """Save batch to vector database."""
        if not self.batch_ids:
            return 0
        
        try:
            count = len(self.batch_ids)
            self.collection.add(
                documents=self.batch_ids,
                embeddings=self.batch_embeds,
                metadatas=self.batch_metas,
                ids=self.batch_ids
            )
            
            logging.info(f"COMMIT: {count} files to Cortex")
            
            # Clear buffers
            self.batch_ids = []
            self.batch_embeds = []
            self.batch_metas = []
            
            return count
            
        except Exception as e:
            logging.error(f"Batch flush failed: {e}")
            return 0
    
    def index_directory(self, directory: str, callback=None):
        """
        Scan directory and memorize all audio.
        This is THE LISTENING - the system HEARS your library.
        """
        self.load_brain()
        
        total_indexed = 0
        total_skipped = 0
        extensions = ('.wav', '.flac', '.aif', '.aiff', '.mp3', '.ogg')
        
        print(f"\n🧠 LEARNING LIBRARY: {directory}")
        
        for root, dirs, files in os.walk(directory):
            if self.stop_signal:
                break
            
            for file in files:
                if self.stop_signal:
                    break
                
                if file.lower().endswith(extensions):
                    full_path = os.path.join(root, file)
                    
                    # Check if already indexed
                    try:
                        existing = self.collection.get(ids=[full_path])
                        if existing['ids']:
                            total_skipped += 1
                            continue
                    except:
                        pass
                    
                    # THE LISTENING
                    if callback:
                        callback(f"Listening: {file}")
                    
                    vector, dna = self.embed_audio(full_path)
                    
                    if vector:
                        self.batch_ids.append(full_path)
                        self.batch_embeds.append(vector)
                        self.batch_metas.append({
                            "filename": file,
                            "dna": dna,
                            "indexed_at": datetime.now().isoformat()
                        })
                        
                        # Auto-save in batches
                        if len(self.batch_ids) >= BATCH_SIZE:
                            count = self.flush_batch()
                            total_indexed += count
                            if callback:
                                callback(f"💾 Saved {total_indexed} files to Cortex")
        
        # Final flush
        count = self.flush_batch()
        total_indexed += count
        
        print(f"\n✨ INDEXING COMPLETE")
        print(f"   New files memorized: {total_indexed}")
        print(f"   Already known: {total_skipped}")
        
        return total_indexed
    
    def dream(self, text_prompt: str, n_results: int = 10):
        """
        THE DREAMING - Semantic search by vibes, not filenames.
        "A frozen cathedral on Mars" will find sounds that FEEL like that.
        """
        self.load_brain()
        
        print(f"\n💭 DREAMING: '{text_prompt}'")
        
        # Convert text to vector
        text_embed = self.model.get_text_embedding([text_prompt], use_tensor=False)
        
        # Query the Cortex
        results = self.collection.query(
            query_embeddings=text_embed.tolist(),
            n_results=n_results
        )
        
        if not results['ids'] or not results['ids'][0]:
            return [], []
        
        return results['ids'][0], results['metadatas'][0]
    
    def get_stats(self):
        """Get database statistics."""
        try:
            count = self.collection.count()
            return {
                'total_files': count,
                'db_path': DB_PATH
            }
        except:
            return {'total_files': 0, 'db_path': DB_PATH}


# ═══════════════════════════════════════════════════════════════════════════
# THE VOICE - Integrated Audio Player
# ═══════════════════════════════════════════════════════════════════════════

class Voice:
    """The Voice speaks truth. It brings sound to life."""
    
    def __init__(self):
        """Initialize the audio engine."""
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self.active = True
            self.current_file = None
            print("🎙️  THE VOICE awakens...")
        except Exception as e:
            print(f"⚠️  Voice cannot speak: {e}")
            self.active = False
    
    def speak(self, file_path: str) -> bool:
        """Play an audio file."""
        if not self.active:
            print("⚠️  Voice is muted.")
            return False
        
        try:
            self.silence()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.current_file = file_path
            return True
        except Exception as e:
            print(f"⚠️  Cannot speak: {e}")
            return False
    
    def silence(self):
        """Stop playback."""
        if self.active and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
    
    def is_speaking(self) -> bool:
        """Check if audio is playing."""
        return self.active and pygame.mixer.music.get_busy()
    
    def destroy(self):
        """Cleanup."""
        if self.active:
            self.silence()
            pygame.mixer.quit()


# ═══════════════════════════════════════════════════════════════════════════
# THE ARCHITECT - DecentSampler Forge with ADSR
# ═══════════════════════════════════════════════════════════════════════════

class Architect:
    """The Architect builds worlds. It forges instruments with precision."""
    
    def __init__(self):
        print("🏗️  THE ARCHITECT awakens...")
    
    def forge_instrument(self, name: str, samples: list, 
                        attack: float = 0.01, release: float = 0.5) -> str:
        """
        Forge a DecentSampler instrument (.dspreset) from audio files.
        
        Args:
            name: Instrument name
            samples: List of audio file paths
            attack: Attack time in seconds (0-2)
            release: Release time in seconds (0-5)
        
        Returns:
            Path to created .dspreset file
        """
        try:
            # Sanitize name
            safe_name = "".join(x for x in name if x.isalnum() or x in " _-")
            if not safe_name:
                safe_name = "Noizylab_Instrument"
            
            filename = f"Noizylab_{safe_name}.dspreset"
            
            print(f"\n🔨 FORGING INSTRUMENT: {safe_name}")
            print(f"   Samples: {len(samples)}")
            print(f"   Attack: {attack}s | Release: {release}s")
            
            # Build DecentSampler XML
            xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<DecentSampler minVersion="1.0.0">
    <ui width="812" height="375" bgMode="top_left" layoutMode="relative">
        <tab name="main">
            <label x="20" y="20" text="{safe_name.upper()}" textSize="40" textColor="FF00FFFF"/>
            <label x="20" y="60" text="SINGULARITY FORGE" textSize="20" textColor="FF888888"/>
            
            <labeled-knob x="300" y="120" label="ATTACK" type="float" minValue="0.0" maxValue="2.0" value="{attack}">
                <binding type="amp" level="instrument" position="0" parameter="ENV_ATTACK" />
            </labeled-knob>
            <labeled-knob x="400" y="120" label="RELEASE" type="float" minValue="0.0" maxValue="5.0" value="{release}">
                <binding type="amp" level="instrument" position="0" parameter="ENV_RELEASE" />
            </labeled-knob>
            <labeled-knob x="500" y="120" label="TONE" type="float" minValue="0" maxValue="1" value="1">
                <binding type="effect" level="instrument" position="1" parameter="FX_FILTER_FREQUENCY" translation="table" translationTable="0,30;1,22000"/>
            </labeled-knob>
            <labeled-knob x="600" y="120" label="SPACE" type="float" minValue="0" maxValue="1" value="0.5">
                <binding type="effect" level="instrument" position="0" parameter="FX_REVERB_WET_LEVEL" />
            </labeled-knob>
        </tab>
    </ui>
    <groups>
        <group ampVelTrack="1">
"""
            
            # Map samples across keyboard (starting at C2)
            root_notes = [36, 40, 43, 48, 52, 55, 60, 64, 67, 72, 76, 79, 84]
            
            for i, sample_path in enumerate(samples):
                root = root_notes[i % len(root_notes)]
                clean_path = sample_path.replace("\\", "/")
                
                # Each sample covers a few semitones
                xml += f'            <sample path="{clean_path}" rootNote="{root}" loNote="{root}" hiNote="{root+3}" />\n'
            
            xml += """        </group>
    </groups>
    <effects>
        <effect type="reverb" wetLevel="0.5"/>
        <effect type="lowpass" frequency="22000.0"/>
    </effects>
</DecentSampler>"""
            
            # Save file
            with open(filename, "w") as f:
                f.write(xml)
            
            full_path = os.path.abspath(filename)
            print(f"\n✨ INSTRUMENT FORGED: {full_path}")
            print("   (Drag this into DecentSampler VST to play)")
            
            return full_path
            
        except Exception as e:
            print(f"❌ Forge failed: {e}")
            return None


# ═══════════════════════════════════════════════════════════════════════════
# THE SINGULARITY GUI - CustomTkinter Interface
# ═══════════════════════════════════════════════════════════════════════════

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class SingularityApp(ctk.CTk):
    """The Singularity Interface - Where Intelligence Meets Design."""
    
    def __init__(self):
        super().__init__()
        
        self.engine = SingularityEngine()
        self.voice = Voice()
        self.architect = Architect()
        
        self.title("NOIZYLAB // THE SINGULARITY PROTOCOL")
        self.geometry("1400x900")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Grid configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.found_samples = []
        self.indexing_thread = None
        
        self._build_ui()
    
    def _build_ui(self):
        """Construct the interface."""
        
        # ═══════════════════════════════════════════════════════════════════
        # SIDEBAR - Control Panel
        # ═══════════════════════════════════════════════════════════════════
        
        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color="#050505")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        
        # Logo
        self.logo = ctk.CTkLabel(
            self.sidebar, 
            text="NOIZYLAB", 
            font=("DIN Alternate", 42, "bold"), 
            text_color="#00FFFF"
        )
        self.logo.pack(pady=(40, 5))
        
        self.sublogo = ctk.CTkLabel(
            self.sidebar, 
            text=":: SINGULARITY ::", 
            font=("Consolas", 14, "bold"), 
            text_color="#f1c40f"
        )
        self.sublogo.pack(pady=(0, 10))
        
        # Status
        self.lbl_status = ctk.CTkLabel(
            self.sidebar, 
            text="● CORTEX ONLINE", 
            font=("Consolas", 12, "bold"), 
            text_color="#2ecc71"
        )
        self.lbl_status.pack(pady=(10, 30))
        
        # Index Button
        self.btn_index = ctk.CTkButton(
            self.sidebar,
            text="🧠 INDEX LIBRARY",
            height=50,
            fg_color="#222",
            border_color="#00FFFF",
            border_width=2,
            hover_color="#333",
            font=("Arial", 14, "bold"),
            command=self.start_indexing
        )
        self.btn_index.pack(pady=10, padx=20, fill="x")
        
        # Stop Button
        self.btn_stop = ctk.CTkButton(
            self.sidebar,
            text="🛑 EMERGENCY HALT",
            height=35,
            fg_color="#c0392b",
            hover_color="#e74c3c",
            font=("Arial", 12),
            command=self.stop_indexing
        )
        self.btn_stop.pack(pady=10, padx=20, fill="x")
        
        # Stats Button
        self.btn_stats = ctk.CTkButton(
            self.sidebar,
            text="📊 DATABASE STATS",
            height=35,
            fg_color="#34495e",
            hover_color="#4a5f7f",
            font=("Arial", 12),
            command=self.show_stats
        )
        self.btn_stats.pack(pady=10, padx=20, fill="x")
        
        # Log Area
        ctk.CTkLabel(
            self.sidebar, 
            text="SYSTEM LOG", 
            font=("Consolas", 10, "bold"),
            text_color="#888"
        ).pack(pady=(20, 5), padx=10)
        
        self.log_area = ctk.CTkTextbox(
            self.sidebar, 
            font=("Consolas", 9), 
            text_color="#bdc3c7", 
            fg_color="#111",
            wrap="word"
        )
        self.log_area.pack(pady=(0, 20), padx=10, fill="both", expand=True)
        
        # ═══════════════════════════════════════════════════════════════════
        # MAIN FRAME - Dream Interface
        # ═══════════════════════════════════════════════════════════════════
        
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#0a0a0a")
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        
        # Header
        header = ctk.CTkLabel(
            self.main_frame,
            text="SEMANTIC DREAM SEARCH",
            font=("DIN Alternate", 28, "bold"),
            text_color="#00FFFF"
        )
        header.pack(pady=(30, 10))
        
        subtitle = ctk.CTkLabel(
            self.main_frame,
            text="Describe the sound you need. The Cortex will find it by vibes, not filenames.",
            font=("Arial", 12),
            text_color="#888"
        )
        subtitle.pack(pady=(0, 20))
        
        # Search Entry
        self.search_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text='Try: "A frozen cathedral on Mars" or "Aggressive dark bass growl"',
            height=70,
            font=("Arial", 18),
            border_color="#8e44ad",
            border_width=2,
            text_color="white",
            fg_color="#1a1a1a"
        )
        self.search_entry.pack(pady=(0, 20), padx=50, fill="x")
        self.search_entry.bind("<Return>", lambda e: self.run_dream_search())
        
        # Search Button
        self.btn_search = ctk.CTkButton(
            self.main_frame,
            text="🔮 DREAM",
            height=50,
            width=200,
            font=("Arial", 16, "bold"),
            fg_color="#8e44ad",
            hover_color="#9b59b6",
            command=self.run_dream_search
        )
        self.btn_search.pack(pady=(0, 30))
        
        # Results Area
        self.results_scroll = ctk.CTkScrollableFrame(
            self.main_frame,
            label_text="SONIC MATCHES",
            label_font=("Arial", 14, "bold"),
            fg_color="#151515",
            label_fg_color="#222"
        )
        self.results_scroll.pack(expand=True, fill="both", padx=50, pady=(0, 20))
        
        # ═══════════════════════════════════════════════════════════════════
        # FORGE PANEL - Instrument Builder
        # ═══════════════════════════════════════════════════════════════════
        
        self.forge_frame = ctk.CTkFrame(self.main_frame, height=120, fg_color="#1a1a1a")
        self.forge_frame.pack(fill="x", padx=50, pady=(0, 30))
        
        ctk.CTkLabel(
            self.forge_frame,
            text="INSTRUMENT FORGE (ADSR CONTROLS)",
            font=("Arial", 12, "bold"),
            text_color="#f1c40f"
        ).pack(pady=(10, 10))
        
        # Controls frame
        controls = ctk.CTkFrame(self.forge_frame, fg_color="transparent")
        controls.pack(fill="x", padx=20)
        
        # Attack
        ctk.CTkLabel(controls, text="ATTACK", font=("Arial", 10)).pack(side="left", padx=10)
        self.sl_attack = ctk.CTkSlider(controls, from_=0, to=2, width=150, number_of_steps=40)
        self.sl_attack.set(0.01)
        self.sl_attack.pack(side="left", padx=5)
        self.lbl_attack_val = ctk.CTkLabel(controls, text="0.01s", width=50, font=("Arial", 10))
        self.lbl_attack_val.pack(side="left")
        self.sl_attack.configure(command=lambda v: self.lbl_attack_val.configure(text=f"{v:.2f}s"))
        
        # Release
        ctk.CTkLabel(controls, text="RELEASE", font=("Arial", 10)).pack(side="left", padx=10)
        self.sl_release = ctk.CTkSlider(controls, from_=0, to=5, width=150, number_of_steps=50)
        self.sl_release.set(0.5)
        self.sl_release.pack(side="left", padx=5)
        self.lbl_release_val = ctk.CTkLabel(controls, text="0.50s", width=50, font=("Arial", 10))
        self.lbl_release_val.pack(side="left")
        self.sl_release.configure(command=lambda v: self.lbl_release_val.configure(text=f"{v:.2f}s"))
        
        # Forge Button
        self.btn_forge = ctk.CTkButton(
            self.forge_frame,
            text="✨ FORGE INSTRUMENT",
            height=50,
            width=220,
            fg_color="#8e44ad",
            hover_color="#9b59b6",
            font=("Arial", 14, "bold"),
            state="disabled",
            command=self.forge_instrument
        )
        self.btn_forge.pack(side="right", padx=20, pady=10)
    
    # ═══════════════════════════════════════════════════════════════════════
    # LOGIC METHODS
    # ═══════════════════════════════════════════════════════════════════════
    
    def log(self, msg: str):
        """Add message to log."""
        ts = datetime.now().strftime("%H:%M:%S")
        self.log_area.insert("end", f"[{ts}] {msg}\n")
        self.log_area.see("end")
        self.update_idletasks()
    
    def start_indexing(self):
        """Start library indexing in background thread."""
        folder = filedialog.askdirectory(title="Select Audio Library to Index")
        if not folder:
            return
        
        self.engine.stop_signal = False
        self.log(f"Starting indexing: {folder}")
        self.lbl_status.configure(text="● LEARNING...", text_color="#f39c12")
        
        self.indexing_thread = threading.Thread(
            target=self._index_worker,
            args=(folder,),
            daemon=True
        )
        self.indexing_thread.start()
    
    def _index_worker(self, folder: str):
        """Worker thread for indexing."""
        try:
            count = self.engine.index_directory(folder, callback=self.log)
            self.log(f"✨ COMPLETE: {count} files indexed")
            self.lbl_status.configure(text="● CORTEX ONLINE", text_color="#2ecc71")
        except Exception as e:
            self.log(f"❌ Indexing failed: {e}")
            self.lbl_status.configure(text="● ERROR", text_color="#e74c3c")
    
    def stop_indexing(self):
        """Stop indexing process."""
        self.engine.stop_signal = True
        self.log("🛑 Stopping indexing...")
    
    def show_stats(self):
        """Show database statistics."""
        stats = self.engine.get_stats()
        msg = f"CORTEX STATISTICS\n\n"
        msg += f"Total Files Indexed: {stats['total_files']}\n"
        msg += f"Database Path: {stats['db_path']}\n\n"
        msg += "The Cortex remembers all."
        
        messagebox.showinfo("Database Stats", msg)
    
    def run_dream_search(self):
        """Execute semantic dream search."""
        query = self.search_entry.get().strip()
        if not query:
            return
        
        self.log(f"💭 Dreaming: '{query}'")
        
        # Clear previous results
        for widget in self.results_scroll.winfo_children():
            widget.destroy()
        
        try:
            # Execute dream search
            ids, metas = self.engine.dream(query, n_results=20)
            
            if not ids:
                self.log("No matches found in Cortex")
                ctk.CTkLabel(
                    self.results_scroll,
                    text="No matches found. Try indexing more audio first.",
                    text_color="#888"
                ).pack(pady=20)
                return
            
            self.found_samples = ids
            self.log(f"Found {len(ids)} matches")
            
            # Display results
            for i, (path, meta) in enumerate(zip(ids, metas), 1):
                self._create_result_row(i, path, meta)
            
            # Enable forge button
            self.btn_forge.configure(state="normal")
            
        except Exception as e:
            self.log(f"❌ Dream search failed: {e}")
            import traceback
            traceback.print_exc()
    
    def _create_result_row(self, index: int, path: str, meta: dict):
        """Create a result row widget."""
        row = ctk.CTkFrame(self.results_scroll, fg_color="#222", corner_radius=5)
        row.pack(fill="x", pady=3, padx=5)
        
        # Play button
        btn_play = ctk.CTkButton(
            row,
            text="▶",
            width=40,
            height=30,
            fg_color="#333",
            hover_color="#555",
            command=lambda: self.play_sound(path)
        )
        btn_play.pack(side="left", padx=5, pady=5)
        
        # DNA tag
        dna = meta.get('dna', 'Unknown')
        lbl_dna = ctk.CTkLabel(
            row,
            text=f"[{dna}]",
            font=("Consolas", 10, "bold"),
            text_color="#f1c40f",
            width=120
        )
        lbl_dna.pack(side="left", padx=5)
        
        # Filename
        filename = meta.get('filename', os.path.basename(path))
        lbl_name = ctk.CTkLabel(
            row,
            text=f"{index}. {filename}",
            anchor="w",
            text_color="#ddd",
            font=("Arial", 11)
        )
        lbl_name.pack(side="left", padx=10, fill="x", expand=True)
    
    def play_sound(self, path: str):
        """Play audio file."""
        try:
            self.voice.speak(path)
            self.log(f"▶️  Playing: {os.path.basename(path)}")
        except Exception as e:
            self.log(f"⚠️  Playback error: {e}")
    
    def forge_instrument(self):
        """Forge DecentSampler instrument from search results."""
        if not self.found_samples:
            messagebox.showwarning("No Samples", "Search for samples first!")
            return
        
        query = self.search_entry.get().strip() or "Dream"
        attack = self.sl_attack.get()
        release = self.sl_release.get()
        
        self.log(f"🔨 Forging instrument from {len(self.found_samples)} samples...")
        
        path = self.architect.forge_instrument(
            query,
            self.found_samples,
            attack=attack,
            release=release
        )
        
        if path:
            msg = f"INSTRUMENT CREATED!\n\n"
            msg += f"File: {path}\n\n"
            msg += f"Attack: {attack:.2f}s\n"
            msg += f"Release: {release:.2f}s\n"
            msg += f"Samples: {len(self.found_samples)}\n\n"
            msg += "Drag this .dspreset file into DecentSampler VST to play!"
            
            messagebox.showinfo("Singularity Forge", msg)
            self.log(f"✨ Instrument forged: {os.path.basename(path)}")
        else:
            messagebox.showerror("Forge Failed", "Could not create instrument")
    
    def on_close(self):
        """Cleanup on exit."""
        self.engine.stop_signal = True
        self.voice.destroy()
        self.destroy()


# ═══════════════════════════════════════════════════════════════════════════
# CLI INTERFACE - For Terminal Usage
# ═══════════════════════════════════════════════════════════════════════════

def cli_mode():
    """Command-line interface for The Singularity."""
    
    engine = SingularityEngine()
    architect = Architect()
    
    print("\n" + "═"*80)
    print("🔮 THE SINGULARITY PROTOCOL - CLI MODE")
    print("═"*80)
    print("\nCommands:")
    print("  index <directory>  - Index audio library")
    print("  dream <prompt>     - Semantic search")
    print("  forge              - Create instrument from last search")
    print("  stats              - Database statistics")
    print("  help               - Show this help")
    print("  gui                - Launch GUI mode")
    print("  exit               - Exit")
    print("═"*80)
    
    last_results = []
    
    while True:
        try:
            cmd = input("\n⚡ SINGULARITY > ").strip()
            
            if not cmd:
                continue
            
            parts = cmd.split(maxsplit=1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""
            
            if command in ['exit', 'quit', 'q']:
                print("\n👋 The Singularity sleeps...")
                break
            
            elif command == 'gui':
                print("\n🚀 Launching GUI...")
                app = SingularityApp()
                app.mainloop()
            
            elif command == 'index':
                if not args:
                    print("❌ Usage: index <directory>")
                    continue
                
                directory = args.strip()
                if os.path.exists(directory):
                    engine.index_directory(directory)
                else:
                    print(f"❌ Directory not found: {directory}")
            
            elif command == 'dream':
                if not args:
                    print("❌ Usage: dream <semantic prompt>")
                    continue
                
                ids, metas = engine.dream(args.strip(), n_results=10)
                last_results = ids
                
                if ids:
                    print(f"\n Found {len(ids)} matches:")
                    for i, (path, meta) in enumerate(zip(ids, metas), 1):
                        dna = meta.get('dna', 'Unknown')
                        filename = meta.get('filename', os.path.basename(path))
                        print(f"   {i}. [{dna}] {filename}")
                else:
                    print("❌ No matches found")
            
            elif command == 'forge':
                if not last_results:
                    print("❌ Search for samples first with 'dream' command")
                    continue
                
                name = input("Instrument name: ").strip() or "Dream"
                attack = float(input("Attack (0-2s) [0.01]: ") or "0.01")
                release = float(input("Release (0-5s) [0.5]: ") or "0.5")
                
                path = architect.forge_instrument(name, last_results, attack, release)
                if path:
                    print(f"\n✨ Instrument ready: {path}")
            
            elif command == 'stats':
                stats = engine.get_stats()
                print("\n" + "═"*80)
                print("📊 CORTEX STATISTICS")
                print("═"*80)
                print(f"Total Files: {stats['total_files']}")
                print(f"Database: {stats['db_path']}")
                print("═"*80)
            
            elif command == 'help':
                print("\n" + "═"*80)
                print("SINGULARITY PROTOCOL COMMANDS")
                print("═"*80)
                print("index <dir>   - Scan and memorize all audio in directory")
                print("dream <text>  - Semantic search (e.g., 'dark aggressive bass')")
                print("forge         - Build DecentSampler instrument from last search")
                print("stats         - Show Cortex statistics")
                print("gui           - Launch graphical interface")
                print("help          - Show this help")
                print("exit          - Exit program")
                print("═"*80)
            
            else:
                print(f"❌ Unknown command: {command}")
                print("Type 'help' for commands")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Type 'exit' to quit.")
            continue
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()


# ═══════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Launch The Singularity."""
    
    # Check dependencies
    try:
        import chromadb
        import laion_clap
        import librosa
        import torch
        import pygame
        import customtkinter
    except ImportError as e:
        print("❌ MISSING DEPENDENCIES!")
        print("\nPlease install:")
        print("  pip install chromadb laion-clap librosa torch soundfile numpy pygame customtkinter")
        print("\nOr all at once:")
        print("  pip install chromadb laion-clap librosa torch soundfile numpy pygame customtkinter pillow")
        sys.exit(1)
    
    # Check if GUI mode requested
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli_mode()
    else:
        # Default to GUI
        print("\n🔮 THE SINGULARITY PROTOCOL")
        print("   Launching GUI...")
        app = SingularityApp()
        app.mainloop()


if __name__ == '__main__':
    main()
