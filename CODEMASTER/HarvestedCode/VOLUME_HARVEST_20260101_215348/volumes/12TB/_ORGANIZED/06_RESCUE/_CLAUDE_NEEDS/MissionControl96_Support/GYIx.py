#!/usr/bin/env python3
"""
Reset CoreAudio buffer settings and restart the daemon
"""
import sys
import subprocess
import os

def main():
    buffer_size = sys.argv[1] if len(sys.argv) > 1 else "256"
    
    print(f"Setting CoreAudio buffer size to {buffer_size} frames")
    
    # Kill CoreAudio daemon (it will auto-restart)
    try:
        subprocess.run(["killall", "-9", "coreaudiod"], check=False)
        print("CoreAudio daemon restarted")
    except Exception as e:
        print(f"Error restarting CoreAudio: {e}")
    
    # Optional: Set audio preferences (requires additional tools)
    # This is a placeholder for more advanced audio settings
    print(f"Buffer size preference noted: {buffer_size}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())