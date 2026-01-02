#!/usr/bin/env python3
"""
🔍 NoizyFish Ultimate Search
The master search system that finds everything and suggests AI tools
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path
import json

def search_h3000():
    """Quick search for H3000 files"""
    print("🔍 Searching for H3000 files...")
    
    music_path = "/Users/rsp_ms/NoizyFish_Aquarium/🎵 Original_Music_Archive"
    
    try:
        # Use find command
        cmd = ['find', music_path, '-name', '*H3000*', '-type', 'f']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            files = [f for f in result.stdout.strip().split('\n') if f]
            
            print(f"\n📊 Found {len(files)} H3000 files:")
            print("="*60)
            
            for i, file_path in enumerate(files, 1):
                file_name = Path(file_path).name
                try:
                    size = Path(file_path).stat().st_size
                    size_mb = size / (1024 * 1024)
                    print(f"{i:2d}. 🎵 {file_name}")
                    print(f"    💾 {size_mb:.1f} MB")
                    print(f"    📂 {file_path}")
                    print()
                except:
                    print(f"{i:2d}. 🎵 {file_name}")
                    print(f"    📂 {file_path}")
                    print()
            
            print("🤖 AI Tool Suggestions:")
            print("-"*40)
            print("1. 🎤 Transcribe audio files:")
            print("   python 02_Audio_Transcription/audio_transcriber.py --file '[filename]'")
            print()
            print("2. 🔍 Analyze voice characteristics:")
            print("   python 05_Voice_Analysis/voice_analyzer.py --file '[filename]'")
            print()
            print("3. ✍️  Generate lyrics inspired by H3000:")
            print("   python 03_Creative_Writing_Assistant/writing_assistant.py --type lyrics --prompt 'H3000 harmonizer effects'")
            print()
            print("4. 🤖 Run AI agents to organize music:")
            print("   python 06_AI_Agents/ai_agents.py --agent music --task scan_archive")
            
        else:
            print("❌ Search failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def search_anything(query, category='all'):
    """Search for anything in the workspace"""
    print(f"🔍 Searching for '{query}' (category: {category})")
    print("="*60)
    
    # Define search locations
    locations = {
        'music': "/Users/rsp_ms/NoizyFish_Aquarium/🎵 Original_Music_Archive",
        'code': "/Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects",
        'js': "/Users/rsp_ms/NoizyFish_Aquarium/🌟 JavaScript_Projects",
        'tools': "/Users/rsp_ms/NoizyFish_Aquarium/🔧 Tools_And_Utilities",
        'ai': "/Users/rsp_ms/NoizyFish_Aquarium/🤖 AI_Toolkit"
    }
    
    if category == 'audio' or category == 'music':
        search_paths = [locations['music']]
    elif category == 'code':
        search_paths = [locations['code'], locations['js'], locations['ai']]
    else:
        search_paths = list(locations.values())
    
    all_matches = []
    
    for location_name, location_path in locations.items():
        if location_path in search_paths and Path(location_path).exists():
            print(f"  🔍 Searching {location_name}...")
            
            try:
                cmd = ['find', location_path, '-name', f'*{query}*', '-type', 'f']
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
                
                if result.returncode == 0:
                    matches = [f for f in result.stdout.strip().split('\n') if f]
                    for match in matches:
                        all_matches.append({'path': match, 'location': location_name})
                        
            except Exception as e:
                print(f"    ⚠️  Error in {location_name}: {e}")
    
    # Display results
    print(f"\n📊 Found {len(all_matches)} files matching '{query}':")
    print("-"*60)
    
    for i, match in enumerate(all_matches[:20], 1):  # Show first 20
        file_path = Path(match['path'])
        print(f"{i:2d}. 📄 {file_path.name}")
        print(f"    📂 {match['location']} | {match['path']}")
        print()
    
    if len(all_matches) > 20:
        print(f"    ... and {len(all_matches) - 20} more files")
    
    return all_matches

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="🔍 NoizyFish Ultimate Search")
    parser.add_argument("query", nargs='?', default="H3000", help="Search query")
    parser.add_argument("--category", choices=['all', 'audio', 'music', 'code'], 
                       default='all', help="Category to search")
    
    args = parser.parse_args()
    
    print("🔍 NoizyFish Ultimate Master Search")
    print("="*60)
    print("🤖 AI Toolkit Integration | 🎵 Music Archive | 🐍 Code Projects")
    print()
    
    if args.query.lower() == 'h3000':
        search_h3000()
    else:
        matches = search_anything(args.query, args.category)
        
        # Suggest AI tools based on what was found
        audio_files = [m for m in matches if any(m['path'].endswith(ext) for ext in ['.wav', '.mp3', '.m4a'])]
        code_files = [m for m in matches if any(m['path'].endswith(ext) for ext in ['.py', '.js', '.ts'])]
        
        print("\n🤖 AI Tool Suggestions:")
        print("-"*40)
        
        if audio_files:
            print("🎵 Audio files found - Try:")
            print(f"  • Transcribe: python 02_Audio_Transcription/audio_transcriber.py --file '[filename]'")
            print(f"  • Analyze: python 05_Voice_Analysis/voice_analyzer.py --file '[filename]'")
        
        if code_files:
            print("💻 Code files found - Try:")
            print(f"  • Analyze: python 01_AI_Code_Assistant/code_assistant.py --mode analyze --file '[filename]'")
            print(f"  • Debug: python 01_AI_Code_Assistant/code_assistant.py --mode debug --file '[filename]'")
        
        print(f"✍️  Creative content - Try:")
        print(f"  • Generate: python 03_Creative_Writing_Assistant/writing_assistant.py --type lyrics --prompt '{args.query}'")
        print(f"  • Images: python 04_Image_Generation/image_generator.py --prompt '{args.query}'")
        
        print(f"🤖 Run AI agents:")
        print(f"  • Daily routine: python 06_AI_Agents/ai_agents.py --routine")

if __name__ == "__main__":
    main()