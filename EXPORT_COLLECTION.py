#!/usr/bin/env python3
"""
EXS24 Master Library - Collection Exporter
Export specific collections or all instruments to a new location
"""

import json
import shutil
from pathlib import Path
from datetime import datetime

class CollectionExporter:
    def __init__(self, scan_data_file=None):
        if scan_data_file is None:
            scan_data_file = Path(__file__).parent / "SCAN_DATA.json"
        self.scan_data_file = Path(scan_data_file)
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load scan data"""
        if not self.scan_data_file.exists():
            print("⚠️  No scan data found. Run SCAN_AND_ORGANIZE.py first.")
            return False
        
        try:
            with open(self.scan_data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except Exception as e:
            print(f"⚠️  Error loading data: {e}")
            return False
    
    def export_collection(self, collection_name, output_dir, preserve_structure=True):
        """Export a specific collection"""
        if not self.data:
            return False
        
        files = self.data.get('exs_files_detailed', [])
        collection_files = [f for f in files if f.get('collection', '').upper() == collection_name.upper()]
        
        if not collection_files:
            print(f"⚠️  Collection '{collection_name}' not found")
            return False
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        exported = 0
        errors = []
        
        print(f"📦 Exporting '{collection_name}' ({len(collection_files)} files)...")
        
        for file_info in collection_files:
            source_path = Path(__file__).parent / file_info['path']
            
            if preserve_structure:
                # Preserve relative path structure
                rel_path = Path(file_info['path'])
                dest_path = output_path / rel_path.name
            else:
                # Flatten to single directory
                dest_path = output_path / file_info['name']
            
            try:
                if source_path.exists():
                    shutil.copy2(source_path, dest_path)
                    exported += 1
                else:
                    errors.append(f"Source not found: {source_path}")
            except Exception as e:
                errors.append(f"Error copying {source_path}: {e}")
        
        print(f"✅ Exported {exported}/{len(collection_files)} files")
        if errors:
            print(f"⚠️  {len(errors)} errors occurred")
        
        return exported > 0
    
    def export_all(self, output_dir, by_collection=True):
        """Export all instruments"""
        if not self.data:
            return False
        
        files = self.data.get('exs_files_detailed', [])
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        exported = 0
        errors = []
        
        print(f"📦 Exporting all instruments ({len(files)} files)...")
        
        if by_collection:
            # Organize by collection
            collections = {}
            for file_info in files:
                collection = file_info.get('collection', 'UNKNOWN')
                if collection not in collections:
                    collections[collection] = []
                collections[collection].append(file_info)
            
            for collection, collection_files in collections.items():
                collection_dir = output_path / collection
                collection_dir.mkdir(exist_ok=True)
                
                for file_info in collection_files:
                    source_path = Path(__file__).parent / file_info['path']
                    dest_path = collection_dir / file_info['name']
                    
                    try:
                        if source_path.exists():
                            shutil.copy2(source_path, dest_path)
                            exported += 1
                        else:
                            errors.append(f"Source not found: {source_path}")
                    except Exception as e:
                        errors.append(f"Error copying {source_path}: {e}")
        else:
            # Flatten all files
            for file_info in files:
                source_path = Path(__file__).parent / file_info['path']
                dest_path = output_path / file_info['name']
                
                try:
                    if source_path.exists():
                        shutil.copy2(source_path, dest_path)
                        exported += 1
                    else:
                        errors.append(f"Source not found: {source_path}")
                except Exception as e:
                    errors.append(f"Error copying {source_path}: {e}")
        
        print(f"✅ Exported {exported}/{len(files)} files")
        if errors:
            print(f"⚠️  {len(errors)} errors occurred")
        
        return exported > 0


def main():
    import sys
    
    exporter = CollectionExporter()
    
    if not exporter.data:
        return
    
    if len(sys.argv) < 3:
        print("EXS24 Collection Exporter")
        print()
        print("Usage:")
        print("  python3 EXPORT_COLLECTION.py <collection_name> <output_dir>")
        print("  python3 EXPORT_COLLECTION.py --all <output_dir>")
        print()
        print("Examples:")
        print("  python3 EXPORT_COLLECTION.py 'BASS LEGENDS' ./exported")
        print("  python3 EXPORT_COLLECTION.py --all ./all_instruments")
        return
    
    if sys.argv[1] == '--all':
        output_dir = sys.argv[2]
        exporter.export_all(output_dir)
    else:
        collection_name = sys.argv[1]
        output_dir = sys.argv[2]
        exporter.export_collection(collection_name, output_dir)


if __name__ == "__main__":
    main()




