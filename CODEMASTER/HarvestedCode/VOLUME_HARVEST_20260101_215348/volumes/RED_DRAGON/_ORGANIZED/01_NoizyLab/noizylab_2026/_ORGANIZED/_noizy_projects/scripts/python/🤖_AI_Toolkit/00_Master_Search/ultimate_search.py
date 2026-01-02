#!/usr/bin/env python3
"""
🔍 ULTIMATE NoizyFish Master Search
Comprehensive search system integrating ALL AI tools and agents
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import argparse

class UltimateMasterSearch:
    def __init__(self):
        """Initialize the Ultimate Master Search system"""
        self.workspace = Path("/Users/rsp_ms/NoizyFish_Aquarium")
        self.ai_toolkit = Path("/Users/rsp_ms/NoizyFish_Aquarium/🤖 AI_Toolkit")
        
        # All searchable locations
        self.search_locations = {
            'music_archive': self.workspace / "🎵 Original_Music_Archive",
            'python_projects': self.workspace / "🐍 Python_Projects", 
            'js_projects': self.workspace / "🌟 JavaScript_Projects",
            'learning_projects': self.workspace / "📚 Learning_Projects",
            'artwork_archive': self.workspace / "🎨 Artwork_Archive",
            'conversations': self.workspace / "🗣️ Conversations_Archive",
            'ai_toolkit': self.ai_toolkit,
            'tools_utilities': self.workspace / "🔧 Tools_And_Utilities"
        }
        
        # AI Tool commands
        self.ai_tools = {
            'code_assistant': f'python "{self.ai_toolkit}/01_AI_Code_Assistant/code_assistant.py"',
            'audio_transcriber': f'python "{self.ai_toolkit}/02_Audio_Transcription/audio_transcriber.py"',
            'writing_assistant': f'python "{self.ai_toolkit}/03_Creative_Writing_Assistant/writing_assistant.py"',
            'image_generator': f'python "{self.ai_toolkit}/04_Image_Generation/image_generator.py"',
            'voice_analyzer': f'python "{self.ai_toolkit}/05_Voice_Analysis/voice_analyzer.py"',
            'ai_agents': f'python "{self.ai_toolkit}/06_AI_Agents/ai_agents.py"'
        }
        
        # File type mappings
        self.file_categories = {
            'audio': ['.wav', '.mp3', '.m4a', '.flac', '.aif', '.aiff'],
            'code': ['.py', '.js', '.ts', '.html', '.css', '.json', '.md'],
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.txt', '.md', '.pdf', '.doc', '.docx'],
            'data': ['.csv', '.json', '.xml', '.yaml', '.yml']
        }
        
        # Search history
        self.search_history = []
    
    def search_everything(self, query: str, category: str = 'all') -> Dict:
        """Search across all locations and tools"""
        search_id = f"search_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        results = {
            'search_id': search_id,
            'query': query,
            'category': category,
            'timestamp': datetime.now().isoformat(),
            'locations_searched': [],
            'file_matches': [],
            'tool_suggestions': [],
            'quick_actions': []
        }
        
        print(f"🔍 ULTIMATE SEARCH: '{query}' (category: {category})")
        print(f"{'='*80}")
        
        # 1. Fast file search using system commands
        results['file_matches'] = self._fast_file_search(query, category)
        
        # 2. Suggest relevant AI tools
        results['tool_suggestions'] = self._suggest_ai_tools(query, results['file_matches'])
        
        # 3. Generate quick actions
        results['quick_actions'] = self._generate_quick_actions(query, results['file_matches'])
        
        # Save to search history
        self.search_history.append(results)
        
        return results
    
    def _fast_file_search(self, query: str, category: str) -> List[Dict]:
        """Fast file search using system find command"""
        matches = []
        
        # Determine search locations based on category
        if category == 'music' or category == 'audio':
            locations = [self.search_locations['music_archive']]
        elif category == 'code':
            locations = [self.search_locations['python_projects'], 
                        self.search_locations['js_projects'],
                        self.search_locations['ai_toolkit']]
        elif category == 'all':
            locations = list(self.search_locations.values())
        else:
            locations = list(self.search_locations.values())
        
        for location_name, location_path in self.search_locations.items():
            if location_path not in locations or not location_path.exists():
                continue
            
            print(f"  🔍 Searching {location_name}...")
            
            try:
                # Use find command for speed
                cmd = ['find', str(location_path), '-name', f'*{query}*', '-type', 'f']
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                
                if result.returncode == 0:
                    for file_path in result.stdout.strip().split('\n'):
                        if file_path:  # Skip empty lines
                            file_info = self._get_file_info(Path(file_path))
                            if file_info:
                                file_info['location'] = location_name
                                matches.append(file_info)
                                
            except (subprocess.TimeoutExpired, Exception) as e:
                print(f"    ⚠️  Error searching {location_name}: {e}")
                continue
        
        # Sort by relevance and modification time
        matches.sort(key=lambda x: (
            query.lower() not in x['name'].lower(),  # Exact matches first
            -x.get('modified_timestamp', 0)  # Then newest
        ))
        
        return matches[:50]  # Limit results
    
    def _get_file_info(self, file_path: Path) -> Optional[Dict]:
        """Get detailed file information"""
        try:
            stat = file_path.stat()
            return {
                'name': file_path.name,
                'path': str(file_path),
                'size': stat.st_size,
                'type': self._get_file_category(file_path),
                'extension': file_path.suffix.lower(),
                'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'modified_timestamp': stat.st_mtime
            }
        except (OSError, PermissionError):
            return None
    
    def _get_file_category(self, file_path: Path) -> str:
        """Categorize file by extension"""
        ext = file_path.suffix.lower()
        for category, extensions in self.file_categories.items():
            if ext in extensions:
                return category
        return 'other'
    
    def _suggest_ai_tools(self, query: str, file_matches: List[Dict]) -> List[Dict]:
        """Suggest relevant AI tools based on search results"""
        suggestions = []
        
        # Analyze what was found
        audio_files = [f for f in file_matches if f['type'] == 'audio']
        code_files = [f for f in file_matches if f['type'] == 'code']
        image_files = [f for f in file_matches if f['type'] == 'images']
        
        # Audio-related suggestions
        if audio_files or 'music' in query.lower() or 'audio' in query.lower():
            suggestions.extend([
                {
                    'tool': 'audio_transcriber',
                    'action': 'Transcribe audio files',
                    'command': f'{self.ai_tools["audio_transcriber"]} --file',
                    'description': f'Transcribe {len(audio_files)} audio files found'
                },
                {
                    'tool': 'voice_analyzer', 
                    'action': 'Analyze voice characteristics',
                    'command': f'{self.ai_tools["voice_analyzer"]} --file',
                    'description': 'Get vocal coaching and performance analysis'
                }
            ])
        
        # Code-related suggestions
        if code_files or 'code' in query.lower() or 'script' in query.lower():
            suggestions.extend([
                {
                    'tool': 'code_assistant',
                    'action': 'Analyze code files',
                    'command': f'{self.ai_tools["code_assistant"]} --mode analyze --file',
                    'description': f'Analyze {len(code_files)} code files found'
                }
            ])
        
        # Creative suggestions
        if 'lyrics' in query.lower() or 'write' in query.lower():
            suggestions.append({
                'tool': 'writing_assistant',
                'action': 'Generate creative content',
                'command': f'{self.ai_tools["writing_assistant"]} --type lyrics --prompt "{query}"',
                'description': 'Create lyrics or written content'
            })
        
        # Image suggestions
        if 'album' in query.lower() or 'art' in query.lower() or 'logo' in query.lower():
            suggestions.append({
                'tool': 'image_generator',
                'action': 'Generate artwork',
                'command': f'{self.ai_tools["image_generator"]} --prompt "{query}"',
                'description': 'Create visual content or artwork'
            })
        
        return suggestions
    
    def _generate_quick_actions(self, query: str, file_matches: List[Dict]) -> List[Dict]:
        """Generate quick actions based on search results"""
        actions = []
        
        if file_matches:
            # Open first match
            first_match = file_matches[0]
            actions.append({
                'action': 'Open first result',
                'command': f'open "{first_match["path"]}"',
                'description': f'Open {first_match["name"]}'
            })
            
            # Show in Finder
            actions.append({
                'action': 'Show in Finder',
                'command': f'open -R "{first_match["path"]}"',
                'description': f'Reveal {first_match["name"]} in Finder'
            })
        
        # Agent suggestions
        actions.extend([
            {
                'action': 'Run daily AI routine',
                'command': f'{self.ai_tools["ai_agents"]} --routine',
                'description': 'Execute daily automated tasks'
            },
            {
                'action': 'Scan music archive',
                'command': f'{self.ai_tools["ai_agents"]} --agent music --task scan_archive',
                'description': 'Analyze your music collection'
            }
        ])
        
        return actions
    
    def execute_action(self, action_command: str) -> Dict:
        """Execute a suggested action"""
        try:
            print(f"🚀 Executing: {action_command}")
            result = subprocess.run(action_command, shell=True, capture_output=True, text=True, timeout=30)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr,
                'command': action_command
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'command': action_command
            }
    
    def format_size(self, size_bytes: int) -> str:
        """Format file size"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"
    
    def export_results(self, search_results: Dict) -> str:
        """Export search results to JSON file"""
        filename = f"search_export_{search_results['search_id']}.json"
        
        with open(filename, 'w') as f:
            json.dump(search_results, f, indent=2)
        
        return filename

def main():
    parser = argparse.ArgumentParser(description="🔍 Ultimate NoizyFish Master Search")
    parser.add_argument("query", help="What to search for")
    parser.add_argument("--category", choices=['all', 'music', 'audio', 'code', 'images'], 
                       default='all', help="Category to search")
    parser.add_argument("--execute", type=int, help="Execute quick action by number")
    parser.add_argument("--export", action="store_true", help="Export results to JSON")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    
    args = parser.parse_args()
    
    search_system = UltimateMasterSearch()
    
    if args.interactive:
        print("🔍 Ultimate NoizyFish Master Search - Interactive Mode")
        print("Commands: search <query>, tools, history, quit")
        print("="*60)
        
        while True:
            try:
                user_input = input("\n🔍 > ").strip()
                
                if user_input.lower() == 'quit':
                    break
                elif user_input.lower() == 'tools':
                    print("\n🤖 Available AI Tools:")
                    for tool_name in search_system.ai_tools:
                        print(f"  - {tool_name}")
                elif user_input.lower() == 'history':
                    print(f"\n📚 Search History ({len(search_system.search_history)} searches):")
                    for i, search in enumerate(search_system.search_history[-5:], 1):
                        print(f"  {i}. '{search['query']}' - {search['timestamp']}")
                elif user_input.startswith('search '):
                    query = user_input[7:]
                    results = search_system.search_everything(query)
                    
                    # Display results (same as below)
                    print(f"\n📊 Found {len(results['file_matches'])} files")
                    
                    for i, match in enumerate(results['file_matches'][:10], 1):
                        size_str = search_system.format_size(match['size'])
                        print(f"{i:2d}. 📄 {match['name']} ({size_str})")
                        print(f"    📂 {match['location']} | {match['type']} | {match['modified']}")
                    
                    if results['tool_suggestions']:
                        print(f"\n🤖 AI Tool Suggestions:")
                        for i, suggestion in enumerate(results['tool_suggestions'], 1):
                            print(f"{i:2d}. {suggestion['action']} - {suggestion['description']}")
                
                else:
                    print("Unknown command. Try: search <query>, tools, history, quit")
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break
    
    else:
        # Single search mode
        results = search_system.search_everything(args.query, args.category)
        
        print(f"\n📊 SEARCH SUMMARY")
        print(f"{'='*60}")
        print(f"Query: '{results['query']}'")
        print(f"Category: {results['category']}")
        print(f"Files found: {len(results['file_matches'])}")
        print(f"Search ID: {results['search_id']}")
        
        # Show file matches
        if results['file_matches']:
            print(f"\n📁 FILE MATCHES:")
            print(f"{'-'*60}")
            
            total_size = 0
            for i, match in enumerate(results['file_matches'][:20], 1):
                size_str = search_system.format_size(match['size'])
                total_size += match['size']
                
                print(f"{i:2d}. 📄 {match['name']}")
                print(f"    📂 {match['location']} | {match['type']} | {size_str}")
                print(f"    📅 {match['modified']} | {match['path']}")
                print()
            
            if len(results['file_matches']) > 20:
                remaining = len(results['file_matches']) - 20
                print(f"    ... and {remaining} more files")
            
            print(f"Total size: {search_system.format_size(total_size)}")
        
        # Show AI tool suggestions
        if results['tool_suggestions']:
            print(f"\n🤖 AI TOOL SUGGESTIONS:")
            print(f"{'-'*60}")
            
            for i, suggestion in enumerate(results['tool_suggestions'], 1):
                print(f"{i:2d}. {suggestion['action']}")
                print(f"    {suggestion['description']}")
                print(f"    Command: {suggestion['command']}")
                print()
        
        # Show quick actions
        if results['quick_actions']:
            print(f"\n⚡ QUICK ACTIONS:")
            print(f"{'-'*60}")
            
            for i, action in enumerate(results['quick_actions'], 1):
                print(f"{i:2d}. {action['action']}")
                print(f"    {action['description']}")
                print(f"    Command: {action['command']}")
                print()
        
        # Execute action if requested
        if args.execute and results['quick_actions']:
            if 1 <= args.execute <= len(results['quick_actions']):
                action = results['quick_actions'][args.execute - 1]
                print(f"\n🚀 EXECUTING ACTION {args.execute}:")
                execution_result = search_system.execute_action(action['command'])
                
                if execution_result['success']:
                    print(f"✅ Success!")
                    if execution_result['output']:
                        print(execution_result['output'])
                else:
                    print(f"❌ Error: {execution_result['error']}")
        
        # Export if requested
        if args.export:
            filename = search_system.export_results(results)
            print(f"\n💾 Results exported to: {filename}")

if __name__ == "__main__":
    main()