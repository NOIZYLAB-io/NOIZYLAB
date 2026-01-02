#!/usr/bin/env python3
"""
🔍 NoizyFish Master Search System
Unified search interface for all AI tools, agents, and content
"""

import os
import sys
import json
import asyncio
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import argparse

# Add all tool directories to path
current_dir = Path(__file__).parent.parent
sys.path.extend([
    str(current_dir / "01_AI_Code_Assistant"),
    str(current_dir / "02_Audio_Transcription"), 
    str(current_dir / "03_Creative_Writing_Assistant"),
    str(current_dir / "04_Image_Generation"),
    str(current_dir / "05_Voice_Analysis"),
    str(current_dir / "06_AI_Agents")
])

try:
    import openai
    from code_assistant import CodeAssistant
    from audio_transcriber import AudioTranscriber
    from writing_assistant import CreativeWritingAssistant
    from image_generator import ImageGenerator
    from voice_analyzer import VoiceAnalyzer
except ImportError as e:
    print(f"⚠️  Import warning: {e}")
    print("Some tools may not be available. Run setup.sh first.")

class MasterSearchSystem:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Master Search System"""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.client = openai.OpenAI(api_key=self.api_key) if self.api_key else None
        
        # Initialize all tools
        self.tools = {}
        self._initialize_tools()
        
        # Search categories
        self.categories = {
            'code': 'Code analysis, generation, debugging',
            'audio': 'Audio transcription, voice analysis',
            'writing': 'Creative writing, lyrics, documentation',
            'images': 'Image generation, artwork, logos',
            'files': 'File system search and analysis',
            'agents': 'AI agents and autonomous tasks',
            'music': 'Music archive and audio files',
            'all': 'Search everything'
        }
        
        # File type mappings
        self.file_types = {
            'audio': ['.wav', '.mp3', '.m4a', '.flac', '.aif', '.aiff'],
            'code': ['.py', '.js', '.ts', '.html', '.css', '.json', '.md'],
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.txt', '.md', '.pdf', '.doc', '.docx'],
            'data': ['.csv', '.json', '.xml', '.yaml', '.yml']
        }
        
        # Cache for search results
        self.search_cache = {}
        
    def _initialize_tools(self):
        """Initialize all available AI tools"""
        try:
            if self.api_key:
                self.tools['code'] = CodeAssistant(self.api_key)
                self.tools['audio'] = AudioTranscriber(self.api_key)
                self.tools['writing'] = CreativeWritingAssistant(self.api_key)
                self.tools['images'] = ImageGenerator(self.api_key)
                self.tools['voice'] = VoiceAnalyzer(self.api_key)
            else:
                print("⚠️  No API key found. AI features will be limited.")
        except Exception as e:
            print(f"⚠️  Tool initialization error: {e}")
    
    def search_files(self, query: str, file_types: List[str] = None, 
                    directory: str = None) -> List[Dict]:
        """Search for files matching query"""
        if directory is None:
            directory = "/Users/rsp_ms/NoizyFish_Aquarium"
        
        results = []
        search_path = Path(directory)
        
        if not search_path.exists():
            return results
        
        # Determine extensions to search
        extensions = []
        if file_types:
            for ft in file_types:
                extensions.extend(self.file_types.get(ft, []))
        else:
            # Search all known file types
            for ext_list in self.file_types.values():
                extensions.extend(ext_list)
        
        # Search files
        for file_path in search_path.rglob("*"):
            if file_path.is_file():
                # Check extension match
                if extensions and file_path.suffix.lower() not in extensions:
                    continue
                
                # Check name match
                if query.lower() in file_path.name.lower():
                    results.append({
                        'path': str(file_path),
                        'name': file_path.name,
                        'type': self._get_file_type(file_path),
                        'size': file_path.stat().st_size,
                        'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                        'match_type': 'filename'
                    })
        
        return results[:50]  # Limit results
    
    def smart_search(self, query: str, category: str = 'all', 
                    deep_search: bool = False) -> Dict:
        """Intelligent search that combines multiple approaches"""
        search_id = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{hash(query) % 10000}"
        
        results = {
            'search_id': search_id,
            'query': query,
            'category': category,
            'timestamp': datetime.now().isoformat(),
            'file_matches': [],
            'content_matches': [],
            'ai_analysis': {},
            'tool_results': {},
            'suggestions': []
        }
        
        # 1. File name search
        if category in ['all', 'files']:
            file_types = None if category == 'all' else [category]
            results['file_matches'] = self.search_files(query, file_types)
        
        return results
    
    def _get_file_type(self, file_path: Path) -> str:
        """Determine file type category"""
        ext = file_path.suffix.lower()
        for category, extensions in self.file_types.items():
            if ext in extensions:
                return category
        return 'other'

def main():
    parser = argparse.ArgumentParser(description="🔍 NoizyFish Master Search System")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--category", choices=['all', 'code', 'audio', 'music', 'files'], 
                       default="all", help="Search category")
    parser.add_argument("--interactive", action="store_true", help="Interactive search mode")
    
    args = parser.parse_args()
    
    # Initialize search system
    search_system = MasterSearchSystem()
    
    if args.interactive:
        # Interactive mode
        print("🔍 NoizyFish Master Search - Interactive Mode")
        print("Type 'quit' to exit\n")
        
        while True:
            try:
                query = input("Search> ").strip()
                
                if query.lower() == 'quit':
                    break
                
                if not query:
                    continue
                
                print(f"\n🔍 Searching for: '{query}'...")
                results = search_system.smart_search(query, args.category)
                
                # Display results
                print(f"\n{'='*60}")
                print(f"SEARCH RESULTS - {results['search_id']}")
                print(f"{'='*60}")
                
                if results['file_matches']:
                    print(f"\n📁 File Matches ({len(results['file_matches'])}):")
                    for match in results['file_matches'][:10]:
                        print(f"  📄 {match['name']} ({match['type']})")
                        print(f"     {match['path']}")
                else:
                    print(f"\n📁 No file matches found")
                
                print(f"\nSearch ID: {results['search_id']}")
                
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    else:
        # Single search mode
        print(f"🔍 Searching for: '{args.query}' in category '{args.category}'")
        
        results = search_system.smart_search(args.query, args.category)
        
        print(f"\n{'='*60}")
        print(f"SEARCH RESULTS")
        print(f"{'='*60}")
        print(f"Query: {results['query']}")
        print(f"Category: {results['category']}")
        print(f"Search ID: {results['search_id']}")
        
        print(f"\n📊 Summary:")
        print(f"  File matches: {len(results['file_matches'])}")
        
        # Show top results
        if results['file_matches']:
            print(f"\n📁 File Matches:")
            for match in results['file_matches'][:20]:
                print(f"  📄 {match['name']} ({match['type']})")
                print(f"     {match['path']}")
        else:
            print(f"\n📁 No matches found for '{args.query}'")

if __name__ == "__main__":
    main()