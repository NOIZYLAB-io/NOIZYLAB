#!/usr/bin/env python3
"""
Volume Management and Audio Extraction System for Noizy Fishes Empire
Performs integrity checks and audio file extraction from mounted drives.
"""

import shutil
from pathlib import Path
import subprocess


class VolumeManager:
    def __init__(self):
        self.volumes = self.get_mounted_volumes()
        self.temp_folder = Path("/Users/rsp_ms/Desktop/Noizy_Temp")
        self.audio_extensions = ['.wav', '.mp3', '.flac', '.aiff', '.m4a', '.ogg']
        
    def get_mounted_volumes(self):
        """Get all mounted volumes with numeric selection"""
        volumes = []
        volume_path = Path("/Volumes")
        
        if volume_path.exists():
            for item in volume_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    volumes.append({
                        'id': len(volumes) + 1,
                        'name': item.name,
                        'path': str(item),
                        'size': self.get_directory_size(item)
                    })
        
        # Add Mission Control (root)
        volumes.append({
            'id': len(volumes) + 1,
            'name': 'Mission Control',
            'path': '/',
            'size': self.get_directory_size(Path('/'))
        })
        
        return volumes
    
    def get_directory_size(self, path):
        """Get directory size in a human-readable format"""
        try:
            result = subprocess.run(['du', '-sh', str(path)], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return result.stdout.split('\t')[0]
        except Exception:
            pass
        return "Unknown"
    
    def display_volumes(self):
        """Display all volumes with numeric selection"""
        print("\n" + "="*60)
        print("MOUNTED VOLUMES - NOIZY FISHES EMPIRE")
        print("="*60)
        
        for vol in self.volumes:
            print(f"{vol['id']:2}. {vol['name']:<20} | {vol['size']:>10} | {vol['path']}")
        
        print("="*60)
        return self.volumes
    
    def perform_integrity_check(self, volume_path):
        """Perform basic integrity check on a volume"""
        print(f"\nPerforming integrity check on: {volume_path}")
        
        try:
            # Check if path exists and is accessible
            path = Path(volume_path)
            if not path.exists():
                return {"status": "error", "message": "Path does not exist"}
            
            # Count files and directories
            file_count = 0
            dir_count = 0
            audio_count = 0
            
            for item in path.rglob('*'):
                if item.is_file():
                    file_count += 1
                    if item.suffix.lower() in self.audio_extensions:
                        audio_count += 1
                elif item.is_dir():
                    dir_count += 1
            
            return {
                "status": "success",
                "files": file_count,
                "directories": dir_count,
                "audio_files": audio_count,
                "readable": True
            }
            
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def extract_audio_files(self, volume_path, volume_name):
        """Extract and organize audio files by name"""
        print(f"\nExtracting audio files from: {volume_name}")
        
        source_path = Path(volume_path)
        dest_folder = self.temp_folder / "Audio_Extractions" / volume_name.replace(" ", "_")
        dest_folder.mkdir(parents=True, exist_ok=True)
        
        extracted_files = []
        
        try:
            for audio_file in source_path.rglob('*'):
                if audio_file.is_file() and audio_file.suffix.lower() in self.audio_extensions:
                    try:
                        # Create organized filename
                        new_name = f"{audio_file.stem}{audio_file.suffix}"
                        dest_file = dest_folder / new_name
                        
                        # Handle duplicates
                        counter = 1
                        while dest_file.exists():
                            new_name = f"{audio_file.stem}_{counter}{audio_file.suffix}"
                            dest_file = dest_folder / new_name
                            counter += 1
                        
                        # Copy file
                        shutil.copy2(audio_file, dest_file)
                        extracted_files.append(str(dest_file))
                        
                    except Exception as e:
                        print(f"Error copying {audio_file}: {e}")
                        continue
            
            print(f"Extracted {len(extracted_files)} audio files to {dest_folder}")
            return extracted_files
            
        except Exception as e:
            print(f"Error extracting from {volume_name}: {e}")
            return []
    
    def process_selected_volume(self, volume_id):
        """Process a selected volume with integrity check and audio extraction"""
        try:
            volume = next(v for v in self.volumes if v['id'] == volume_id)
        except StopIteration:
            print(f"Volume ID {volume_id} not found")
            return
        
        print(f"\nProcessing: {volume['name']}")
        print("-" * 40)
        
        # Integrity check
        integrity = self.perform_integrity_check(volume['path'])
        print(f"Integrity Check: {integrity}")
        
        if integrity['status'] == 'success':
            # Audio extraction
            extracted = self.extract_audio_files(volume['path'], volume['name'])
            print(f"Audio files extracted: {len(extracted)}")
        else:
            print("Skipping audio extraction due to integrity issues")
    
    def process_all_volumes(self):
        """Process all volumes"""
        for volume in self.volumes:
            self.process_selected_volume(volume['id'])
            print("\n" + "="*60)

def main():
    vm = VolumeManager()
    
    while True:
        volumes = vm.display_volumes()
        print("\nOptions:")
        print("  Enter volume number to process")
        print("  'all' to process all volumes")
        print("  'quit' to exit")
        
        choice = input("\nEnter your choice: ").strip().lower()
        
        if choice == 'quit':
            break
        elif choice == 'all':
            vm.process_all_volumes()
        else:
            try:
                volume_id = int(choice)
                vm.process_selected_volume(volume_id)
            except ValueError:
                print("Invalid selection. Please enter a number, 'all', or 'quit'.")

if __name__ == "__main__":
    main()