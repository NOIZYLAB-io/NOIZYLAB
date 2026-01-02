#!/usr/bin/env python3
"""
Device Sync Helper for Mission Control 96
Helps sync Apple Certification Audio to iPhone and iPad
"""

import os
import subprocess
import json
from pathlib import Path

def find_connected_devices():
    """Find connected iOS devices"""
    try:
        # Try to find connected devices using system_profiler
        result = subprocess.run(
            ["system_profiler", "SPUSBDataType", "-json"],
            capture_output=True,
            text=True
        )
        
        devices = []
        if result.returncode == 0:
            data = json.loads(result.stdout)
            # Parse USB data to find iOS devices
            # This is a simplified version - you might need to adjust based on your system
            for item in data.get("SPUSBDataType", []):
                if "iPhone" in str(item) or "iPad" in str(item):
                    devices.append({
                        "name": "iOS Device Found",
                        "type": "iPhone/iPad",
                        "status": "connected"
                    })
        
        return devices
    except Exception:
        return []

def create_sync_folder():
    """Create a sync folder on Desktop for easy transfer"""
    sync_folder = Path.home() / "Desktop" / "Mission_Control_Sync"
    sync_folder.mkdir(exist_ok=True)
    
    # Create device-specific folders
    (sync_folder / "iPhone_Playlist").mkdir(exist_ok=True)
    (sync_folder / "iPad_Playlist").mkdir(exist_ok=True)
    
    return sync_folder

def copy_audio_files_for_device(device_type, max_size_mb=50):
    """Copy audio files to sync folder for specific device"""
    audio_library = Path.home() / "Desktop" / "Apple_Certification_Audio"
    sync_folder = create_sync_folder()
    device_folder = sync_folder / f"{device_type}_Playlist"
    
    # Clear existing files
    for file in device_folder.glob("*"):
        if file.is_file():
            file.unlink()
    
    copied_files = []
    total_size = 0
    
    # Copy files from each chapter
    for chapter_dir in audio_library.glob("Chapter_*"):
        chapter_name = chapter_dir.name
        chapter_sync_dir = device_folder / chapter_name
        chapter_sync_dir.mkdir(exist_ok=True)
        
        for audio_file in chapter_dir.glob("*.{mp3,wav,m4a,aac}"):
            file_size_mb = audio_file.stat().st_size / (1024 * 1024)
            
            if file_size_mb <= max_size_mb:
                dest_file = chapter_sync_dir / audio_file.name
                dest_file.write_bytes(audio_file.read_bytes())
                copied_files.append({
                    "file": audio_file.name,
                    "chapter": chapter_name,
                    "size_mb": round(file_size_mb, 2)
                })
                total_size += file_size_mb
    
    # Create playlist files
    create_m3u_playlist(device_folder, copied_files, device_type)
    
    return {
        "device": device_type,
        "sync_folder": str(device_folder),
        "files_copied": len(copied_files),
        "total_size_mb": round(total_size, 2),
        "files": copied_files
    }

def create_m3u_playlist(folder, files, device_type):
    """Create M3U playlist file"""
    playlist_file = folder / f"Apple_Certification_{device_type}.m3u"
    
    with open(playlist_file, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        f.write(f"#PLAYLIST:Apple Certification - {device_type}\n\n")
        
        for file_info in files:
            f.write(f"#EXTINF:-1,{file_info['chapter']} - {file_info['file']}\n")
            f.write(f"{file_info['chapter']}/{file_info['file']}\n\n")

def generate_sync_instructions():
    """Generate sync instructions"""
    return """
📱 SYNC INSTRUCTIONS FOR iPhone/iPad

Method 1: AirDrop (Recommended)
1. Open Finder and navigate to ~/Desktop/Mission_Control_Sync/
2. Select the iPhone_Playlist or iPad_Playlist folder
3. Right-click and select "Share" > "AirDrop"
4. Choose your device and accept on your iPhone/iPad

Method 2: iTunes/Music App Sync
1. Connect your device via USB
2. Open Music app (or iTunes on older macOS)
3. Drag the playlist folder to your device
4. Click "Sync" to transfer files

Method 3: iCloud Drive
1. Copy playlist folder to iCloud Drive
2. Open Files app on your device
3. Download files from iCloud Drive to local storage

Method 4: Third-party Apps
- Use apps like VLC, Documents by Readdle, or GoodReader
- These can handle various audio formats and playlists

🎯 Recommended App: VLC for Mobile
- Supports all audio formats
- Can import M3U playlists
- Works offline once downloaded
"""

def main():
    print("📱 Mission Control 96 - Device Sync Helper")
    print("=" * 50)
    
    # Check for connected devices
    devices = find_connected_devices()
    if devices:
        print(f"✅ Found {len(devices)} connected device(s)")
        for device in devices:
            print(f"   📱 {device['name']} - {device['status']}")
    else:
        print("⚠️  No iOS devices detected (you can still prepare sync folders)")
    
    print("\n🎯 Preparing sync folders...")
    
    # Prepare iPhone playlist
    print("\n📱 Preparing iPhone playlist...")
    iphone_result = copy_audio_files_for_device("iPhone", max_size_mb=50)
    print(f"   ✅ {iphone_result['files_copied']} files ({iphone_result['total_size_mb']} MB)")
    
    # Prepare iPad playlist  
    print("\n📱 Preparing iPad playlist...")
    ipad_result = copy_audio_files_for_device("iPad", max_size_mb=100)
    print(f"   ✅ {ipad_result['files_copied']} files ({ipad_result['total_size_mb']} MB)")
    
    print("\n📁 Sync folders created:")
    print(f"   iPhone: {iphone_result['sync_folder']}")
    print(f"   iPad: {ipad_result['sync_folder']}")
    
    print("\n" + generate_sync_instructions())
    
    # Open sync folder in Finder
    sync_folder = create_sync_folder()
    subprocess.run(["open", str(sync_folder)])
    print(f"📂 Opened sync folder in Finder: {sync_folder}")

if __name__ == "__main__":
    main()