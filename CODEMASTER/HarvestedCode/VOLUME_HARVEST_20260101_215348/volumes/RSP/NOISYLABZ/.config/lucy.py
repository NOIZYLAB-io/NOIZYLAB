"""
LUCY - Intelligent Voice Assistant for NOISYLABZ
A sophisticated AI voice assistant that reads code updates and provides expert guidance
on music production, film, VS Code, and AI development.

Features:
- Real-time code change narration
- Expert knowledge across music, film, code, AI
- British accent with French elegance
- Natural, conversational tone
- Contextual code explanations
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Optional

class LucyVoiceAssistant:
    """Main Lucy assistant class"""
    
    def __init__(self, voice_provider: str = "system"):
        """
        Initialize Lucy with voice settings
        
        Args:
            voice_provider: 'system' (macOS), 'azure', or 'google'
        """
        self.voice_provider = voice_provider
        self.config = self._load_config()
        self.voice = self._select_voice()
        
    def _load_config(self) -> dict:
        """Load Lucy configuration"""
        config_path = Path(__file__).parent / "lucy_config.json"
        if config_path.exists():
            with open(config_path) as f:
                return json.load(f)
        return self._default_config()
    
    def _default_config(self) -> dict:
        """Return default Lucy configuration"""
        return {
            "name": "Lucy",
            "personality": "sophisticated",
            "expertise": [
                "music_production",
                "film_production", 
                "vscode",
                "ai_development",
                "universal_knowledge"
            ],
            "accent": "british_french",
            "gender": "female",
            "age_persona": "45",
            "education": "ridiculously_well_schooled"
        }
    
    def _select_voice(self) -> str:
        """Select the best available voice"""
        if self.voice_provider == "system":
            return self._get_macos_voice()
        elif self.voice_provider == "azure":
            return "en-GB-LibbyNeural"  # British female voice
        elif self.voice_provider == "google":
            return "en-GB-Neural2-C"  # Google's British female voice
        return "Victoria"  # Fallback
    
    def _get_macos_voice(self) -> str:
        """Get best macOS voice available"""
        voices = {
            "Victoria": 169,  # British English - ideal
            "Daniel": 169,    # British English
            "Moira": 169,     # British English  
            "Samantha": 168,  # Eloquent alternative
        }
        # Check available voices
        try:
            result = subprocess.run(
                ["say", "-v", "?"],
                capture_output=True,
                text=True
            )
            for voice in voices.keys():
                if voice in result.stdout:
                    return voice
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        return "Victoria"  # Best British female option
    
    def speak(self, text: str, speed: float = 0.85) -> None:
        """
        Speak using Lucy's voice
        
        Args:
            text: Text to speak
            speed: Speaking rate (0.5-2.0)
        """
        if self.voice_provider == "system":
            self._speak_macos(text, speed)
        else:
            self._speak_cloud(text)
    
    def _speak_macos(self, text: str, speed: float) -> None:
        """Speak on macOS using 'say' command"""
        rate = int(speed * 200)  # Convert to WPM
        subprocess.run([
            "say",
            "-v", self.voice,
            "-r", str(rate),
            text
        ])
    
    def _speak_cloud(self, text: str) -> None:
        """Speak using cloud provider (Azure/Google)"""
        # Implementation for cloud providers
        print(f"[{self.voice}]: {text}")
    
    def narrate_code_change(self, old_code: str, new_code: str, minimal: bool = True) -> None:
        """Narrate what changed in code - minimal mode by default"""
        summary = self._summarize_changes(old_code, new_code, minimal)
        if summary:
            self.speak(summary)
    
    def _summarize_changes(self, old_code: str, new_code: str, minimal: bool = True) -> str:
        """Summarize what changed between versions - minimal mode"""
        # Simple diff analysis
        old_lines = set(old_code.split('\n'))
        new_lines = set(new_code.split('\n'))
        
        added = len(new_lines - old_lines)
        removed = len(old_lines - new_lines)
        
        if minimal:
            # Minimal mode: only mention if significant changes
            if added > 10 or removed > 10:
                return f"{added} lines added, {removed} removed."
            elif added > 3:
                return "Code updated."
            elif removed > 3:
                return "Lines removed."
            return ""  # Don't narrate tiny changes
        
        # Verbose mode (if needed)
        if added > 0 and removed > 0:
            return f"Added {added} lines, removed {removed} lines."
        elif added > 0:
            return f"Added {added} new lines."
        elif removed > 0:
            return f"Removed {removed} lines."
        return "Code has been modified."
    
    def explain_code(self, code: str, context: str = "") -> None:
        """Explain code in detail"""
        explanation = f"Here's what this code does: {context}"
        self.speak(explanation)
    
    def answer_question(self, question: str) -> None:
        """Answer any question about music, film, code, AI, etc."""
        # Would integrate with Claude API for intelligent answers
        response = f"Regarding {question}: [Expert response would be here]"
        self.speak(response)
    
    def read_bullet_points(self, bullets: list) -> None:
        """Read bullet points from VS Code window"""
        for i, bullet in enumerate(bullets, 1):
            text = f"Point {i}: {bullet}"
            self.speak(text)


# Alternative: Use Azure Cognitive Services for more realistic voice
class LucyAzure(LucyVoiceAssistant):
    """Lucy using Azure Text-to-Speech"""
    
    def __init__(self, api_key: str, region: str = "eastus"):
        """Initialize with Azure credentials"""
        self.api_key = api_key
        self.region = region
        super().__init__(voice_provider="azure")
    
    def _speak_cloud(self, text: str) -> None:
        """Speak using Azure Cognitive Services"""
        import requests
        
        # Azure TTS endpoint
        url = f"https://{self.region}.tts.speech.microsoft.com/cognitiveservices/v1"
        
        headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3"
        }
        
        # SSML with British female voice
        ssml = f"""
        <speak version='1.0' xml:lang='en-GB'>
            <voice xml:lang='en-GB' name='en-GB-LibbyNeural'>
                <prosody rate='0.9' pitch='+5%'>
                    {text}
                </prosody>
            </voice>
        </speak>
        """
        
        try:
            response = requests.post(url, headers=headers, data=ssml)
            if response.status_code == 200:
                # Play audio
                with open("lucy_audio.mp3", "wb") as f:
                    f.write(response.content)
                subprocess.run(["afplay", "lucy_audio.mp3"])
        except Exception as e:
            print(f"Azure TTS error: {e}")


# Quick start
if __name__ == "__main__":
    # Initialize Lucy
    lucy = LucyVoiceAssistant(voice_provider="system")
    
    # Example usage
    lucy.speak("Hello, I'm Lucy. I'm here to help you with your code, music production, film work, and anything else you might need.")
    lucy.speak("I notice you're working on the NOISYLABZ workspace configuration.")
    
    # Read bullet points example
    bullets = [
        "VS Code workspace initialized",
        "Tab limit set to 1 for focused development",
        "Auto-save enabled on focus change",
        "Backup automation configured"
    ]
    lucy.read_bullet_points(bullets)
