#!/usr/bin/env python3
"""
🤖 NoizyFish AI Agents System
Autonomous AI agents for various tasks
"""

import os
import openai
import asyncio
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import time

class BaseAgent:
    """Base class for all AI agents"""
    
    def __init__(self, name: str, api_key: Optional[str] = None):
        self.name = name
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.client = openai.OpenAI(api_key=self.api_key) if self.api_key else None
        self.status = "idle"
        self.task_history = []
        self.created_at = datetime.now()
    
    async def execute_task(self, task: Dict) -> Dict:
        """Execute a task (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement execute_task")
    
    def log_task(self, task: Dict, result: Dict):
        """Log completed task"""
        self.task_history.append({
            'task': task,
            'result': result,
            'timestamp': datetime.now().isoformat(),
            'agent': self.name
        })

class MusicArchiveAgent(BaseAgent):
    """Agent for managing and analyzing music archives"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__("MusicArchiveAgent", api_key)
        self.music_path = Path("/Users/rsp_ms/NoizyFish_Aquarium/🎵 Original_Music_Archive")
    
    async def execute_task(self, task: Dict) -> Dict:
        """Execute music-related tasks"""
        task_type = task.get('type', 'analyze')
        
        if task_type == 'scan_archive':
            return await self._scan_music_archive()
        elif task_type == 'categorize_files':
            return await self._categorize_music_files()
        elif task_type == 'find_duplicates':
            return await self._find_duplicate_files()
        elif task_type == 'generate_playlist':
            return await self._generate_smart_playlist(task.get('criteria', {}))
        
        return {'error': f'Unknown task type: {task_type}'}
    
    async def _scan_music_archive(self) -> Dict:
        """Scan and analyze the music archive"""
        results = {
            'total_files': 0,
            'file_types': {},
            'total_size': 0,
            'recent_files': [],
            'large_files': []
        }
        
        audio_extensions = ['.wav', '.mp3', '.m4a', '.flac', '.aif', '.aiff']
        
        for file_path in self.music_path.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in audio_extensions:
                results['total_files'] += 1
                
                # Track file types
                ext = file_path.suffix.lower()
                results['file_types'][ext] = results['file_types'].get(ext, 0) + 1
                
                # Track size
                size = file_path.stat().st_size
                results['total_size'] += size
                
                # Track recent files (last 30 days)
                mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                if (datetime.now() - mod_time).days <= 30:
                    results['recent_files'].append({
                        'name': file_path.name,
                        'path': str(file_path),
                        'size': size,
                        'modified': mod_time.isoformat()
                    })
                
                # Track large files (>50MB)
                if size > 50 * 1024 * 1024:
                    results['large_files'].append({
                        'name': file_path.name,
                        'path': str(file_path),
                        'size': size
                    })
        
        # Sort lists
        results['recent_files'].sort(key=lambda x: x['modified'], reverse=True)
        results['large_files'].sort(key=lambda x: x['size'], reverse=True)
        
        return results

class ContentCreatorAgent(BaseAgent):
    """Agent for creating various types of content"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__("ContentCreatorAgent", api_key)
    
    async def execute_task(self, task: Dict) -> Dict:
        """Execute content creation tasks"""
        task_type = task.get('type', 'create')
        
        if task_type == 'daily_lyrics':
            return await self._create_daily_lyrics()
        elif task_type == 'album_concept':
            return await self._create_album_concept(task.get('theme', 'ocean'))
        elif task_type == 'documentation':
            return await self._create_documentation(task.get('topic', ''))
        
        return {'error': f'Unknown task type: {task_type}'}
    
    async def _create_daily_lyrics(self) -> Dict:
        """Create daily inspirational lyrics"""
        if not self.client:
            return {'error': 'No API key available'}
        
        prompts = [
            "underwater adventure and discovery",
            "the sound of ocean waves creating music", 
            "fish swimming in rhythm to electronic beats",
            "deep sea creatures making harmonious sounds",
            "the intersection of technology and nature"
        ]
        
        import random
        theme = random.choice(prompts)
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative songwriter specializing in electronic and ambient music."},
                {"role": "user", "content": f"Write song lyrics about: {theme}. Make it dreamy and electronic. Include verse-chorus structure."}
            ],
            temperature=0.7
        )
        
        lyrics = response.choices[0].message.content
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"daily_lyrics_{timestamp}.md"
        
        with open(filename, 'w') as f:
            f.write(f"# Daily Lyrics - {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write(f"**Theme:** {theme}\n\n")
            f.write(f"**Generated:** {datetime.now()}\n\n")
            f.write("---\n\n")
            f.write(lyrics)
        
        return {
            'theme': theme,
            'lyrics': lyrics,
            'filename': filename,
            'word_count': len(lyrics.split())
        }

class AutomationAgent(BaseAgent):
    """Agent for automating routine tasks"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__("AutomationAgent", api_key)
    
    async def execute_task(self, task: Dict) -> Dict:
        """Execute automation tasks"""
        task_type = task.get('type', 'cleanup')
        
        if task_type == 'organize_files':
            return await self._organize_files()
        elif task_type == 'backup_important':
            return await self._backup_important_files()
        elif task_type == 'system_report':
            return await self._generate_system_report()
        
        return {'error': f'Unknown task type: {task_type}'}
    
    async def _organize_files(self) -> Dict:
        """Organize files in the workspace"""
        workspace = Path("/Users/rsp_ms/NoizyFish_Aquarium")
        
        results = {
            'files_moved': 0,
            'directories_created': 0,
            'errors': []
        }
        
        # Define organization rules
        organization_rules = {
            'screenshots': ['.png', '.jpg', '.jpeg'],
            'audio_temp': ['.wav', '.mp3', '.m4a'],
            'documents': ['.pdf', '.doc', '.docx', '.txt'],
            'data': ['.json', '.csv', '.xml']
        }
        
        # Create organized directories if they don't exist
        for category in organization_rules:
            category_path = workspace / f"_organized_{category}"
            if not category_path.exists():
                category_path.mkdir(exist_ok=True)
                results['directories_created'] += 1
        
        return results

class AgentManager:
    """Manages multiple AI agents"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.agents = {}
        self.active_tasks = {}
        self._initialize_agents()
    
    def _initialize_agents(self):
        """Initialize all available agents"""
        self.agents = {
            'music': MusicArchiveAgent(self.api_key),
            'content': ContentCreatorAgent(self.api_key),
            'automation': AutomationAgent(self.api_key)
        }
    
    async def run_agent_task(self, agent_name: str, task: Dict) -> Dict:
        """Run a task on a specific agent"""
        if agent_name not in self.agents:
            return {'error': f'Agent {agent_name} not found'}
        
        agent = self.agents[agent_name]
        agent.status = "working"
        
        try:
            result = await agent.execute_task(task)
            agent.log_task(task, result)
            agent.status = "idle"
            return result
        except Exception as e:
            agent.status = "error"
            return {'error': str(e)}
    
    async def run_daily_routine(self) -> Dict:
        """Run daily automated routine"""
        results = {}
        
        # Music archive scan
        music_task = {'type': 'scan_archive'}
        results['music_scan'] = await self.run_agent_task('music', music_task)
        
        # Daily content creation
        content_task = {'type': 'daily_lyrics'}
        results['daily_content'] = await self.run_agent_task('content', content_task)
        
        # System organization
        automation_task = {'type': 'organize_files'}
        results['organization'] = await self.run_agent_task('automation', automation_task)
        
        return results
    
    def get_agent_status(self) -> Dict:
        """Get status of all agents"""
        return {
            name: {
                'status': agent.status,
                'tasks_completed': len(agent.task_history),
                'uptime': str(datetime.now() - agent.created_at)
            }
            for name, agent in self.agents.items()
        }

async def main():
    """Main function for running agents"""
    import argparse
    
    parser = argparse.ArgumentParser(description="🤖 NoizyFish AI Agents")
    parser.add_argument("--agent", choices=['music', 'content', 'automation', 'all'], 
                       default='all', help="Agent to run")
    parser.add_argument("--task", help="Specific task to run")
    parser.add_argument("--routine", action="store_true", help="Run daily routine")
    parser.add_argument("--status", action="store_true", help="Show agent status")
    
    args = parser.parse_args()
    
    manager = AgentManager()
    
    if args.status:
        print("🤖 Agent Status:")
        status = manager.get_agent_status()
        for name, info in status.items():
            print(f"  {name}: {info['status']} ({info['tasks_completed']} tasks, {info['uptime']} uptime)")
        return
    
    if args.routine:
        print("🔄 Running daily routine...")
        results = await manager.run_daily_routine()
        
        print("\n📊 Daily Routine Results:")
        for task_name, result in results.items():
            print(f"\n{task_name}:")
            if 'error' in result:
                print(f"  ❌ Error: {result['error']}")
            else:
                # Print relevant info based on task type
                if 'total_files' in result:
                    print(f"  📁 Files scanned: {result['total_files']}")
                    print(f"  💾 Total size: {result['total_size'] / (1024*1024*1024):.2f} GB")
                elif 'lyrics' in result:
                    print(f"  ✍️  Created: {result['filename']}")
                    print(f"  📝 Word count: {result['word_count']}")
                elif 'files_moved' in result:
                    print(f"  📁 Files organized: {result['files_moved']}")
        return
    
    if args.agent and args.task:
        task_config = {'type': args.task}
        print(f"🤖 Running {args.agent} agent with task: {args.task}")
        
        result = await manager.run_agent_task(args.agent, task_config)
        
        print(f"\n📊 Task Result:")
        if 'error' in result:
            print(f"❌ Error: {result['error']}")
        else:
            print(json.dumps(result, indent=2))
    
    else:
        print("🤖 NoizyFish AI Agents System")
        print("\nAvailable agents:")
        for name, agent in manager.agents.items():
            print(f"  - {name}: {agent.__class__.__doc__}")
        
        print("\nExample commands:")
        print("  python ai_agents.py --routine")
        print("  python ai_agents.py --agent music --task scan_archive")
        print("  python ai_agents.py --agent content --task daily_lyrics")
        print("  python ai_agents.py --status")

if __name__ == "__main__":
    asyncio.run(main())