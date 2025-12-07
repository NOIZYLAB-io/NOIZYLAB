#!/usr/bin/env python3
"""
EXS24 Master Library - Master Index Generator
Creates a comprehensive HTML index of all instruments
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class MasterIndexGenerator:
    def __init__(self, scan_data_file=None):
        if scan_data_file is None:
            scan_data_file = Path(__file__).parent / "SCAN_DATA.json"
        self.scan_data_file = Path(scan_data_file)
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load scan data"""
        if not self.scan_data_file.exists():
            print(f"⚠️  Scan data not found: {self.scan_data_file}")
            print("   Run SCAN_AND_ORGANIZE.py first to generate scan data.")
            return False
        
        try:
            with open(self.scan_data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            print(f"✅ Loaded scan data ({len(self.data.get('exs_files', []))} files)")
            return True
        except Exception as e:
            print(f"⚠️  Error loading scan data: {e}")
            return False
    
    def generate_html_index(self):
        """Generate comprehensive HTML index"""
        if not self.data:
            return None
        
        files = self.data.get('exs_files_detailed', [])
        collections = defaultdict(list)
        
        # Organize by collection
        for file_info in files:
            collection = file_info.get('collection', 'UNKNOWN')
            collections[collection].append(file_info)
        
        # Sort collections
        sorted_collections = sorted(collections.items(), key=lambda x: len(x[1]), reverse=True)
        
        html = []
        html.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EXS24 Master Library - Master Index</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #1a1a1a;
            color: #e0e0e0;
            line-height: 1.6;
            padding: 20px;
        }
        .container { max-width: 1400px; margin: 0 auto; }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        h1 { color: white; font-size: 2.5em; margin-bottom: 10px; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        .stat-value { font-size: 2em; font-weight: bold; color: #667eea; }
        .stat-label { color: #aaa; margin-top: 5px; }
        .collection {
            background: #2a2a2a;
            margin-bottom: 20px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .collection-header {
            background: #333;
            padding: 15px 20px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background 0.3s;
        }
        .collection-header:hover { background: #3a3a3a; }
        .collection-title { font-size: 1.3em; font-weight: bold; color: #667eea; }
        .collection-count { color: #aaa; }
        .collection-content {
            padding: 20px;
            display: none;
        }
        .collection-content.active { display: block; }
        .file-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 10px;
        }
        .file-item {
            background: #1e1e1e;
            padding: 10px;
            border-radius: 5px;
            border-left: 3px solid #667eea;
            font-size: 0.9em;
        }
        .file-name { color: #fff; font-weight: bold; margin-bottom: 5px; }
        .file-path { color: #888; font-size: 0.85em; word-break: break-all; }
        .file-size { color: #667eea; font-size: 0.85em; margin-top: 5px; }
        .search-box {
            background: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        #searchInput {
            width: 100%;
            padding: 12px;
            background: #1a1a1a;
            border: 2px solid #667eea;
            border-radius: 5px;
            color: #fff;
            font-size: 1em;
        }
        #searchInput:focus { outline: none; border-color: #764ba2; }
        .hidden { display: none !important; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎹 EXS24 Master Library</h1>
            <p style="color: rgba(255,255,255,0.9);">Comprehensive Index of All Instruments</p>
            <p style="color: rgba(255,255,255,0.7); margin-top: 10px;">Generated: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
        </header>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">""" + f"{len(files):,}" + """</div>
                <div class="stat-label">Total Instruments</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">""" + f"{len(sorted_collections):,}" + """</div>
                <div class="stat-label">Collections</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">""" + f"{self.data.get('total_dirs', 0):,}" + """</div>
                <div class="stat-label">Directories</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">""" + f"{self.data.get('file_sizes', {}).get('total', 0) / (1024*1024):,.1f}" + """ MB</div>
                <div class="stat-label">Total Size</div>
            </div>
        </div>
        
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="🔍 Search instruments by name, collection, or path...">
        </div>
        
        <div id="collections">""")
        
        # Generate collection sections
        for collection, files in sorted_collections:
            collection_id = collection.replace(' ', '_').replace('/', '_').replace('\\', '_')
            html.append(f"""
        <div class="collection" data-collection="{collection.lower()}">
            <div class="collection-header" onclick="toggleCollection('{collection_id}')">
                <span class="collection-title">{collection}</span>
                <span class="collection-count">{len(files):,} files</span>
            </div>
            <div class="collection-content" id="{collection_id}">
                <div class="file-list">""")
            
            # Sort files by name
            sorted_files = sorted(files, key=lambda x: x.get('name', '').lower())
            
            for file_info in sorted_files:
                file_name = file_info.get('name', '')
                file_path = file_info.get('path', '')
                file_size_kb = file_info.get('size', 0) / 1024
                
                # Escape HTML
                file_name = file_name.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                file_path = file_path.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                
                html.append(f"""
                    <div class="file-item" data-name="{file_name.lower()}" data-path="{file_path.lower()}">
                        <div class="file-name">{file_name}</div>
                        <div class="file-path">{file_path}</div>
                        <div class="file-size">{file_size_kb:.2f} KB</div>
                    </div>""")
            
            html.append("""
                </div>
            </div>
        </div>""")
        
        html.append("""
        </div>
    </div>
    
    <script>
        function toggleCollection(id) {
            const content = document.getElementById(id);
            content.classList.toggle('active');
        }
        
        // Expand all by default
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.collection-content').forEach(el => {
                el.classList.add('active');
            });
        });
        
        // Search functionality
        document.getElementById('searchInput').addEventListener('input', function(e) {
            const query = e.target.value.toLowerCase();
            const fileItems = document.querySelectorAll('.file-item');
            const collections = document.querySelectorAll('.collection');
            
            fileItems.forEach(item => {
                const name = item.getAttribute('data-name');
                const path = item.getAttribute('data-path');
                
                if (name.includes(query) || path.includes(query)) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
            
            // Show/hide collections based on visible items
            collections.forEach(collection => {
                const visibleItems = collection.querySelectorAll('.file-item:not(.hidden)');
                if (visibleItems.length === 0 && query !== '') {
                    collection.classList.add('hidden');
                } else {
                    collection.classList.remove('hidden');
                }
            });
        });
    </script>
</body>
</html>""")
        
        return '\n'.join(html)
    
    def save_html(self, output_file="MASTER_INDEX.html"):
        """Save HTML index to file"""
        html = self.generate_html_index()
        if not html:
            return None
        
        output_path = Path(__file__).parent / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ HTML index saved to: {output_path}")
        return output_path


def main():
    generator = MasterIndexGenerator()
    if generator.data:
        generator.save_html()
        print("\n✨ Master index generated! Open MASTER_INDEX.html in your browser.")


if __name__ == "__main__":
    main()




