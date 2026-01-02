#!/usr/bin/env python3
"""
🚀 NoizyFish AI Toolkit Launcher
Quick access to all your AI tools
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    print("🚀 NoizyFish AI Toolkit Launcher")
    print("="*60)
    print("🤖 All your AI tools in one place")
    print()

def show_tools():
    """Display all available tools"""
    tools = {
        '1': ('🔍 Master Search', 'python master_search.py'),
        '2': ('💻 Code Assistant', 'python 01_AI_Code_Assistant/code_assistant.py'),
        '3': ('🎤 Audio Transcription', 'python 02_Audio_Transcription/audio_transcriber.py'),
        '4': ('✍️  Creative Writing', 'python 03_Creative_Writing_Assistant/writing_assistant.py'),
        '5': ('🎨 Image Generation', 'python 04_Image_Generation/image_generator.py'),
        '6': ('🗣️ Voice Analysis', 'python 05_Voice_Analysis/voice_analyzer.py'),
        '7': ('🤖 AI Agents', 'python 06_AI_Agents/ai_agents.py'),
        '8': ('⚙️  Setup/Config', 'bash setup.sh'),
        '9': ('📋 Quick Actions', 'show_quick_actions'),
    }
    
    print("Available AI Tools:")
    print("-"*40)
    for key, (name, cmd) in tools.items():
        print(f"{key}. {name}")
    print("0. Exit")
    print()
    
    return tools

def show_quick_actions():
    """Show common quick actions"""
    print("📋 Quick Actions:")
    print("-"*30)
    print("1. Search for H3000 files")
    print("2. Transcribe latest audio")
    print("3. Generate album cover")
    print("4. Analyze voice samples")
    print("5. Create song lyrics")
    print("6. Run music archive agent")
    print("7. Backup workspace")
    print("8. System health check")
    print()

def run_command(cmd):
    """Run a command in the toolkit directory"""
    toolkit_dir = Path(__file__).parent
    os.chdir(toolkit_dir)
    
    try:
        if cmd == 'show_quick_actions':
            show_quick_actions()
            return
            
        print(f"🚀 Running: {cmd}")
        print("-"*40)
        result = subprocess.run(cmd, shell=True)
        print()
        print(f"✅ Command completed with status: {result.returncode}")
        
    except KeyboardInterrupt:
        print("\n⚠️  Command interrupted by user")
    except Exception as e:
        print(f"❌ Error running command: {e}")

def main():
    print_header()
    
    while True:
        tools = show_tools()
        
        try:
            choice = input("Select a tool (0-9): ").strip()
            
            if choice == '0':
                print("👋 Goodbye!")
                break
            elif choice in tools:
                name, cmd = tools[choice]
                print(f"\n🚀 Launching {name}...")
                run_command(cmd)
                print("\nPress Enter to continue...")
                input()
                print_header()
            else:
                print("❌ Invalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()