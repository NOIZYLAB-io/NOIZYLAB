#!/usr/bin/env python3
"""
CLAUDERMT SPEECH INTEGRATION
Voice-controlled speech system for Rob's workflow
"""

import os
import subprocess
import json
from pathlib import Path

class SpeechController:
    """Control macOS speech system via ClaudeRMT voice commands"""
    
    VOICE_PROFILES = {
        'fast': {'voice': 'Alex', 'rate': 300},
        'clear': {'voice': 'Samantha', 'rate': 225},
        'slow': {'voice': 'Samantha', 'rate': 180},
        'british': {'voice': 'Daniel', 'rate': 225},
        'scottish': {'voice': 'Fiona', 'rate': 225},
        'aussie': {'voice': 'Karen', 'rate': 225},
    }
    
    def __init__(self):
        self.current_profile = 'clear'
        self.speaking = False
    
    def speak(self, text, voice=None, rate=None):
        """Speak text with optional voice and rate override"""
        profile = self.VOICE_PROFILES.get(self.current_profile)
        v = voice or profile['voice']
        r = rate or profile['rate']
        
        cmd = ['say', '-v', v, '-r', str(r), text]
        subprocess.Popen(cmd)
        self.speaking = True
        return f"Speaking with {v} at {r} WPM"
    
    def stop(self):
        """Stop all speech"""
        subprocess.run(['killall', 'say'], stderr=subprocess.DEVNULL)
        subprocess.run(['killall', 'speechsynthesisd'], stderr=subprocess.DEVNULL)
        self.speaking = False
        return "Speech stopped"
    
    def read_file(self, filepath):
        """Read a file aloud"""
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            return self.speak(content)
        except Exception as e:
            return f"Error reading file: {e}"
    
    def read_clipboard(self):
        """Read clipboard contents"""
        result = subprocess.run(['pbpaste'], capture_output=True, text=True)
        if result.stdout:
            return self.speak(result.stdout)
        return "Clipboard is empty"
    
    def set_profile(self, profile_name):
        """Change voice profile"""
        if profile_name in self.VOICE_PROFILES:
            self.current_profile = profile_name
            p = self.VOICE_PROFILES[profile_name]
            
            # Update system defaults
            subprocess.run([
                'defaults', 'write', 'com.apple.speech.voice.prefs',
                'SelectedVoiceName', '-string', p['voice']
            ])
            subprocess.run([
                'defaults', 'write', 'com.apple.speech.voice.prefs',
                'Rate', '-float', str(float(p['rate']))
            ])
            
            return f"Profile: {profile_name} ({p['voice']} @ {p['rate']} WPM)"
        return f"Unknown profile: {profile_name}"
    
    def get_status(self):
        """Get current speech status"""
        profile = self.VOICE_PROFILES[self.current_profile]
        return {
            'profile': self.current_profile,
            'voice': profile['voice'],
            'rate': profile['rate'],
            'speaking': self.speaking
        }


class VoiceCommandHandler:
    """Handle voice commands for speech control"""
    
    def __init__(self):
        self.speech = SpeechController()
        self.commands = {
            'read this': self._read_selection,
            'read clipboard': self._read_clipboard,
            'read clip': self._read_clipboard,
            'stop reading': self._stop,
            'stop speech': self._stop,
            'shut up': self._stop,
            'fast mode': self._fast_mode,
            'clear mode': self._clear_mode,
            'slow mode': self._slow_mode,
            'british voice': self._british_mode,
            'scottish voice': self._scottish_mode,
            'aussie voice': self._aussie_mode,
            'speech status': self._status,
            'read file': self._read_file,
        }
    
    def _read_selection(self):
        """Read currently selected text"""
        # Simulate Cmd+C
        subprocess.run(['osascript', '-e', '''
            tell application "System Events"
                keystroke "c" using command down
            end tell
        '''])
        import time
        time.sleep(0.3)
        return self.speech.read_clipboard()
    
    def _read_clipboard(self):
        return self.speech.read_clipboard()
    
    def _stop(self):
        return self.speech.stop()
    
    def _fast_mode(self):
        return self.speech.set_profile('fast')
    
    def _clear_mode(self):
        return self.speech.set_profile('clear')
    
    def _slow_mode(self):
        return self.speech.set_profile('slow')
    
    def _british_mode(self):
        return self.speech.set_profile('british')
    
    def _scottish_mode(self):
        return self.speech.set_profile('scottish')
    
    def _aussie_mode(self):
        return self.speech.set_profile('aussie')
    
    def _status(self):
        status = self.speech.get_status()
        return json.dumps(status, indent=2)
    
    def _read_file(self, filepath=None):
        if not filepath:
            return "Please specify file path"
        return self.speech.read_file(filepath)
    
    def handle(self, command_text, args=None):
        """Handle incoming voice command"""
        command_text = command_text.lower().strip()
        
        for cmd, handler in self.commands.items():
            if cmd in command_text:
                try:
                    if args:
                        return handler(args)
                    else:
                        return handler()
                except TypeError:
                    return handler()
        
        # If no command matched, try to speak the text directly
        if command_text.startswith('speak '):
            text = command_text[6:]
            return self.speech.speak(text)
        
        return f"Unknown command: {command_text}"


def main():
    """Main CLI interface"""
    import sys
    
    handler = VoiceCommandHandler()
    
    if len(sys.argv) < 2:
        print("CLAUDERMT SPEECH INTEGRATION")
        print("\nUsage:")
        print("  speech_control.py 'read this'")
        print("  speech_control.py 'read clipboard'")
        print("  speech_control.py 'stop reading'")
        print("  speech_control.py 'fast mode'")
        print("  speech_control.py 'clear mode'")
        print("  speech_control.py 'slow mode'")
        print("  speech_control.py 'speak hello rob'")
        print("  speech_control.py 'speech status'")
        print("\nAvailable profiles: fast, clear, slow, british, scottish, aussie")
        return
    
    command = ' '.join(sys.argv[1:])
    result = handler.handle(command)
    print(result)


if __name__ == '__main__':
    main()
