#!/usr/bin/env python3
"""
Quick Lucy Test - Verify voice is working
"""

import subprocess
import sys

def test_voice():
    """Test if system voice works"""
    print("🎙️ Testing Lucy voice...")
    
    try:
        # Test basic speech
        subprocess.run([
            "say",
            "-v", "Victoria",
            "Hello. This is Lucy. Voice test successful."
        ], check=True)
        
        print("✅ Lucy voice is working!")
        return True
    except FileNotFoundError:
        print("❌ macOS 'say' command not found")
        return False
    except subprocess.CalledProcessError:
        print("❌ Voice test failed")
        return False

if __name__ == "__main__":
    success = test_voice()
    sys.exit(0 if success else 1)
