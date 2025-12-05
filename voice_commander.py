#!/usr/bin/env python3
"""
🎙️ NOIZYLAB VOICE COMMANDER
Hands-free control for your digital symphony
"""

import speech_recognition as sr
import subprocess
import os
from pathlib import Path

class VoiceCommander:
    """Voice control for NOIZYLAB operations"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.commands = {
            'turbo': self.run_turbo,
            'status': self.show_status,
            'optimize': self.run_optimizer,
            'sync': self.sync_repos,
            'commit': self.commit_all,
            'fire': self.fire_all,
            'organize': self.organize_files,
            'disk': self.show_disk,
        }
    
    def listen(self):
        """Listen for voice command"""
        with sr.Microphone() as source:
            print("🎙️  Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5)
        
        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"Heard: {command}")
            return command
        except:
            return None
    
    def run_turbo(self):
        subprocess.run(['python3', 'scripts/turbo.py'])
    
    def show_status(self):
        subprocess.run(['./noizylab', 'status'])
    
    def run_optimizer(self):
        subprocess.run(['python3', 'scripts/optimizer.py'])
    
    def sync_repos(self):
        subprocess.run(['python3', 'scripts/turbo.py', '--sync'])
    
    def commit_all(self):
        subprocess.run(['git', 'add', '-A'])
        subprocess.run(['git', 'commit', '-m', 'voice-commit'])
    
    def fire_all(self):
        self.run_turbo()
        self.run_optimizer()
    
    def organize_files(self):
        subprocess.run(['python3', 'ai/orchestrator.py'])
    
    def show_disk(self):
        subprocess.run(['df', '-h'])
    
    def execute(self, command_text: str):
        """Execute voice command"""
        for keyword, func in self.commands.items():
            if keyword in command_text:
                print(f"🔥 Executing: {keyword}")
                func()
                return True
        
        print("❓ Command not recognized")
        return False
    
    def run(self):
        """Main voice control loop"""
        print("🎙️  NOIZYLAB VOICE COMMANDER")
        print("Say: turbo, status, optimize, sync, commit, fire, organize, disk")
        print("Say 'quit' to exit\n")
        
        while True:
            command = self.listen()
            
            if command:
                if 'quit' in command or 'exit' in command:
                    print("👋 Goodbye!")
                    break
                
                self.execute(command)


if __name__ == "__main__":
    # Check dependencies
    try:
        import speech_recognition
        commander = VoiceCommander()
        commander.run()
    except ImportError:
        print("⚠️  Install: pip3 install SpeechRecognition pyaudio")
        print("Then run: python3 ai/voice_commander.py")
