#!/usr/bin/env python3
"""
Master Search System - NoizyFish AI Toolkit
Unified interface to search, access, and coordinate all AI tools and agents
"""

import os
import sys
import json
import asyncio
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
import openai

# Add all tool directories to path
toolkit_dir = Path(__file__).parent.parent
sys.path.extend([
    str(toolkit_dir / "01_AI_Code_Assistant"),
    str(toolkit_dir / "02_Audio_Transcription"),
    str(toolkit_dir / "03_Creative_Writing_Assistant"),
    str(toolkit_dir / "04_Image_Generation"),
    str(toolkit_dir / "05_Voice_Analysis"),
    str(toolkit_dir / "06_AI_Agents")
])

class MasterSearchSystem:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Master Search System"""
        self.client = openai.OpenAI(
            api_key=api_key or os.getenv('OPENAI_API_KEY')
        )
        self.toolkit_dir = toolkit_dir
        self.tools = self._discover_tools()
        self.agents = self._discover_agents()
        self.workspace_info = self._scan_workspace()
        
    def _discover_tools(self) -> Dict[str, Dict]:
        """Discover all available AI tools"""
        tools = {
            "code_assistant": {
                "name": "AI Code Assistant",
                "description": "Code analysis, generation, refactoring, debugging",
                "module": "code_assistant",
                "path": "01_AI_Code_Assistant/code_assistant.py",
                "capabilities": ["analyze", "generate", "refactor", "explain", "debug"],
                "supports": ["python", "javascript", "typescript", "all languages"]
            },
            "audio_transcriber": {
                "name": "Audio Transcription Tool",
                "description": "Audio-to-text, lyric analysis, batch processing",
                "module": "audio_transcriber",
                "path": "02_Audio_Transcription/audio_transcriber.py",
                "capabilities": ["transcribe", "translate", "analyze_lyrics", "batch_process"],
                "supports": ["wav", "mp3", "m4a", "flac", "aif"]
            },
            "writing_assistant": {
                "name": "Creative Writing Assistant",
                "description": "Lyrics, stories, documentation, poetry generation",
                "module": "writing_assistant",
                "path": "03_Creative_Writing_Assistant/writing_assistant.py",
                "capabilities": ["lyrics", "stories", "docs", "poetry", "brainstorm"],
                "supports": ["all_text_types"]
            },
            "image_generator": {
                "name": "Image Generation Tool",
                "description": "DALL-E powered artwork, album covers, logos",
                "module": "image_generator",
                "path": "04_Image_Generation/image_generator.py",
                "capabilities": ["album_covers", "logos", "artwork", "variations"],
                "supports": ["png", "jpg", "high_quality"]
            },
            "voice_analyzer": {
                "name": "Voice Analysis Tool",
                "description": "Vocal performance analysis and coaching",
                "module": "voice_analyzer",
                "path": "05_Voice_Analysis/voice_analyzer.py",
                "capabilities": ["vocal_analysis", "coaching", "emotion_detection", "comparison"],
                "supports": ["wav", "mp3", "audio_analysis"]
            }
        }
        return tools
    
    def _discover_agents(self) -> Dict[str, Dict]:
        """Discover all available AI agents"""
        agents = {
            "music_producer": {
                "name": "Music Producer Agent",
                "description": "Autonomous music production workflow management",
                "specialties": ["track_analysis", "mixing_advice", "arrangement", "sound_design"],
                "tools": ["audio_transcriber", "voice_analyzer", "writing_assistant"]
            },
            "creative_director": {
                "name": "Creative Director Agent", 
                "description": "Visual content and branding coordination",
                "specialties": ["album_artwork", "branding", "visual_concepts", "marketing"],
                "tools": ["image_generator", "writing_assistant"]
            },
            "code_architect": {
                "name": "Code Architect Agent",
                "description": "Software development and automation",
                "specialties": ["system_design", "code_optimization", "automation", "debugging"],
                "tools": ["code_assistant"]
            },
            "content_curator": {
                "name": "Content Curator Agent",
                "description": "Content organization and workflow optimization",
                "specialties": ["file_organization", "metadata", "workflow_design", "automation"],
                "tools": ["all_tools"]
            }
        }
        return agents
    
    def _scan_workspace(self) -> Dict[str, Any]:
        """Scan the NoizyFish workspace for content"""
        workspace_root = Path("/Users/rsp_ms/NoizyFish_Aquarium")
        
        workspace_info = {
            "music_archive": {
                "path": workspace_root / "🎵 Original_Music_Archive",
                "file_count": 0,
                "total_size": 0,
                "formats": set()
            },
            "projects": {
                "python": workspace_root / "🐍 Python_Projects",
                "javascript": workspace_root / "🌟 JavaScript_Projects", 
                "learning": workspace_root / "📚 Learning_Projects",
                "tools": workspace_root / "🔧 Tools_And_Utilities"
            },
            "archives": {
                "conversations": workspace_root / "🗣️ Conversations_Archive",
                "artwork": workspace_root / "🎨 Artwork_Archive"
            }
        }
        
        # Scan music archive
        music_path = workspace_info["music_archive"]["path"]
        if music_path.exists():
            audio_extensions = {'.wav', '.mp3', '.m4a', '.aif', '.aiff', '.flac'}
            for file_path in music_path.rglob('*'):
                if file_path.is_file():
                    workspace_info["music_archive"]["file_count"] += 1
                    workspace_info["music_archive"]["total_size"] += file_path.stat().st_size
                    if file_path.suffix.lower() in audio_extensions:
                        workspace_info["music_archive"]["formats"].add(file_path.suffix.lower())
        
        workspace_info["music_archive"]["formats"] = list(workspace_info["music_archive"]["formats"])
        workspace_info["music_archive"]["total_size_gb"] = workspace_info["music_archive"]["total_size"] / (1024**3)
        
        return workspace_info
    
    def search_tools(self, query: str) -> List[Dict]:
        """Search for relevant tools based on query"""
        results = []
        query_lower = query.lower()
        
        for tool_id, tool_info in self.tools.items():
            score = 0
            
            # Check name and description
            if query_lower in tool_info["name"].lower():
                score += 10
            if query_lower in tool_info["description"].lower():
                score += 5
                
            # Check capabilities
            for capability in tool_info["capabilities"]:
                if query_lower in capability.lower():
                    score += 8
                    
            # Check supported formats
            for support in tool_info["supports"]:
                if query_lower in support.lower():
                    score += 3
                    
            if score > 0:
                results.append({
                    "type": "tool",
                    "id": tool_id,
                    "score": score,
                    **tool_info
                })
        
        # Sort by relevance score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results
    
    def search_agents(self, query: str) -> List[Dict]:
        """Search for relevant agents based on query"""
        results = []
        query_lower = query.lower()
        
        for agent_id, agent_info in self.agents.items():
            score = 0
            
            # Check name and description
            if query_lower in agent_info["name"].lower():
                score += 10
            if query_lower in agent_info["description"].lower():
                score += 5
                
            # Check specialties
            for specialty in agent_info["specialties"]:
                if query_lower in specialty.lower():
                    score += 8
                    
            if score > 0:
                results.append({
                    "type": "agent",
                    "id": agent_id,
                    "score": score,
                    **agent_info
                })
        
        results.sort(key=lambda x: x["score"], reverse=True)
        return results
    
    def search_workspace(self, query: str) -> List[Dict]:
        """Search workspace files and content"""
        results = []
        query_lower = query.lower()
        
        # Search music archive
        music_path = self.workspace_info["music_archive"]["path"]
        if music_path.exists():
            for file_path in music_path.rglob('*'):
                if file_path.is_file() and query_lower in file_path.name.lower():
                    results.append({
                        "type": "file",
                        "path": str(file_path),
                        "name": file_path.name,
                        "size": file_path.stat().st_size,
                        "category": "music",
                        "extension": file_path.suffix
                    })
        
        # Search other project directories
        for proj_name, proj_path in self.workspace_info["projects"].items():
            if proj_path.exists():
                for file_path in proj_path.rglob('*'):
                    if file_path.is_file() and query_lower in file_path.name.lower():
                        results.append({
                            "type": "file",
                            "path": str(file_path),
                            "name": file_path.name,
                            "size": file_path.stat().st_size,
                            "category": proj_name,
                            "extension": file_path.suffix
                        })
        
        return results[:20]  # Limit results
    
    def ai_search(self, query: str) -> str:
        """Use AI to understand search intent and provide recommendations"""
        
        # Get context about available tools and workspace
        context = {
            "tools": list(self.tools.keys()),
            "agents": list(self.agents.keys()),
            "workspace": {
                "music_files": self.workspace_info["music_archive"]["file_count"],
                "music_formats": self.workspace_info["music_archive"]["formats"],
                "total_size_gb": round(self.workspace_info["music_archive"]["total_size_gb"], 2)
            }
        }
        
        prompt = f"""
        You are the Master Search AI for the NoizyFish AI Toolkit. Analyze this search query and provide intelligent recommendations.
        
        Search Query: "{query}"
        
        Available Tools: {', '.join(self.tools.keys())}
        Available Agents: {', '.join(self.agents.keys())}
        
        Workspace Context:
        - Music Archive: {context['workspace']['music_files']} files ({context['workspace']['total_size_gb']} GB)
        - Formats: {', '.join(context['workspace']['music_formats'])}
        
        Provide:
        1. **Intent Analysis**: What is the user trying to accomplish?
        2. **Recommended Tools**: Which tools would be most helpful?
        3. **Suggested Workflow**: Step-by-step approach
        4. **Specific Commands**: Exact commands to run
        5. **Expected Outcomes**: What results to expect
        
        Be specific and actionable. Include exact command examples.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert AI toolkit coordinator and workflow designer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def execute_workflow(self, workflow_name: str, params: Dict = None) -> Dict:
        """Execute predefined workflows"""
        workflows = {
            "music_analysis": self._workflow_music_analysis,
            "album_creation": self._workflow_album_creation,
            "code_project": self._workflow_code_project,
            "content_audit": self._workflow_content_audit
        }
        
        if workflow_name in workflows:
            return workflows[workflow_name](params or {})
        else:
            return {"error": f"Workflow '{workflow_name}' not found"}
    
    def _workflow_music_analysis(self, params: Dict) -> Dict:
        """Analyze music files in the archive"""
        results = {
            "workflow": "music_analysis",
            "timestamp": datetime.now().isoformat(),
            "steps": []
        }
        
        # Step 1: Scan for audio files
        audio_files = []
        music_path = self.workspace_info["music_archive"]["path"]
        audio_extensions = {'.wav', '.mp3', '.m4a', '.aif', '.aiff'}
        
        for file_path in music_path.rglob('*'):
            if file_path.suffix.lower() in audio_extensions:
                audio_files.append(str(file_path))
                
        results["steps"].append({
            "step": "scan_files",
            "found": len(audio_files),
            "sample": audio_files[:5]
        })
        
        # Step 2: Recommend analysis tools
        recommendations = []
        if audio_files:
            recommendations.extend([
                "Use Voice Analyzer for vocal performance analysis",
                "Use Audio Transcriber for lyric extraction",
                "Use Writing Assistant for lyric improvement"
            ])
            
        results["steps"].append({
            "step": "recommendations",
            "tools": recommendations
        })
        
        return results
    
    def _workflow_album_creation(self, params: Dict) -> Dict:
        """Complete album creation workflow"""
        album_name = params.get("album_name", "New Album")
        artist_name = params.get("artist_name", "NoizyFish")
        
        workflow_steps = [
            f"1. Generate album concept with Writing Assistant",
            f"2. Create album artwork with Image Generator",
            f"3. Analyze existing tracks with Voice Analyzer", 
            f"4. Generate promotional content with Writing Assistant",
            f"5. Organize files with Content Curator Agent"
        ]
        
        return {
            "workflow": "album_creation",
            "album": album_name,
            "artist": artist_name,
            "steps": workflow_steps,
            "estimated_time": "2-4 hours",
            "tools_needed": ["writing_assistant", "image_generator", "voice_analyzer"]
        }
    
    def _workflow_code_project(self, params: Dict) -> Dict:
        """Software development workflow"""
        project_type = params.get("type", "general")
        
        return {
            "workflow": "code_project",
            "project_type": project_type,
            "steps": [
                "1. Generate project structure with Code Assistant",
                "2. Create documentation with Writing Assistant",
                "3. Code review and optimization with Code Architect Agent",
                "4. Create README and guides with Writing Assistant"
            ],
            "tools_needed": ["code_assistant", "writing_assistant"]
        }
    
    def _workflow_content_audit(self, params: Dict) -> Dict:
        """Audit and organize workspace content"""
        return {
            "workflow": "content_audit",
            "scope": "full_workspace",
            "steps": [
                "1. Scan all directories for file types and sizes",
                "2. Identify duplicate or unused files",
                "3. Generate organization recommendations",
                "4. Create cleanup scripts with Code Assistant",
                "5. Document findings with Writing Assistant"
            ],
            "estimated_files": self.workspace_info["music_archive"]["file_count"],
            "tools_needed": ["code_assistant", "writing_assistant"]
        }
    
    def get_tool_status(self) -> Dict:
        """Check status of all tools and agents"""
        status = {
            "timestamp": datetime.now().isoformat(),
            "tools": {},
            "agents": {},
            "workspace": self.workspace_info
        }
        
        # Check tool availability
        for tool_id, tool_info in self.tools.items():
            tool_path = self.toolkit_dir / tool_info["path"]
            status["tools"][tool_id] = {
                "available": tool_path.exists(),
                "path": str(tool_path),
                "last_modified": datetime.fromtimestamp(tool_path.stat().st_mtime).isoformat() if tool_path.exists() else None
            }
        
        # Check agent availability  
        for agent_id, agent_info in self.agents.items():
            status["agents"][agent_id] = {
                "available": True,  # Agents are code-based
                "tools_available": [t for t in agent_info["tools"] if t in self.tools or t == "all_tools"]
            }
        
        return status
    
    def search_everything(self, query: str) -> Dict:
        """Comprehensive search across tools, agents, workspace, and AI analysis"""
        
        print(f"🔍 Searching for: {query}")
        
        results = {
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "tools": self.search_tools(query),
            "agents": self.search_agents(query),
            "workspace_files": self.search_workspace(query),
            "ai_analysis": self.ai_search(query)
        }
        
        return results

def main():
    parser = argparse.ArgumentParser(description="NoizyFish Master Search System")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--mode", choices=["search", "workflow", "status"], default="search", help="Operation mode")
    parser.add_argument("--workflow", help="Workflow to execute")
    parser.add_argument("--params", help="Parameters as JSON string")
    parser.add_argument("--output", help="Output file for results")
    
    args = parser.parse_args()
    
    try:
        master_search = MasterSearchSystem()
        
        if args.mode == "search":
            results = master_search.search_everything(args.query)
            
            print(f"\n{'='*80}")
            print(f"MASTER SEARCH RESULTS")
            print(f"{'='*80}")
            
            # Tools
            if results["tools"]:
                print(f"\n🔧 RELEVANT TOOLS ({len(results['tools'])} found):")
                for tool in results["tools"][:3]:
                    print(f"  • {tool['name']} (Score: {tool['score']})")
                    print(f"    {tool['description']}")
                    print(f"    Path: {tool['path']}")
            
            # Agents
            if results["agents"]:
                print(f"\n🤖 RELEVANT AGENTS ({len(results['agents'])} found):")
                for agent in results["agents"][:3]:
                    print(f"  • {agent['name']} (Score: {agent['score']})")
                    print(f"    {agent['description']}")
            
            # Workspace Files
            if results["workspace_files"]:
                print(f"\n📁 WORKSPACE FILES ({len(results['workspace_files'])} found):")
                for file_info in results["workspace_files"][:5]:
                    size_mb = file_info['size'] / (1024*1024)
                    print(f"  • {file_info['name']} ({size_mb:.1f} MB)")
                    print(f"    Category: {file_info['category']} | Path: {file_info['path']}")
            
            # AI Analysis
            print(f"\n🧠 AI ANALYSIS & RECOMMENDATIONS:")
            print(results["ai_analysis"])
            
            # Save results
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(results, f, indent=2, default=str)
                print(f"\n💾 Results saved to: {args.output}")
        
        elif args.mode == "workflow":
            if not args.workflow:
                print("Available workflows: music_analysis, album_creation, code_project, content_audit")
                return
                
            params = json.loads(args.params) if args.params else {}
            result = master_search.execute_workflow(args.workflow, params)
            
            print(f"\n{'='*80}")
            print(f"WORKFLOW: {result.get('workflow', args.workflow).upper()}")
            print(f"{'='*80}")
            print(json.dumps(result, indent=2, default=str))
        
        elif args.mode == "status":
            status = master_search.get_tool_status()
            
            print(f"\n{'='*80}")
            print(f"AI TOOLKIT STATUS")
            print(f"{'='*80}")
            
            print(f"\n🔧 TOOLS:")
            for tool_id, tool_status in status["tools"].items():
                status_icon = "✅" if tool_status["available"] else "❌"
                print(f"  {status_icon} {tool_id}")
            
            print(f"\n🤖 AGENTS:")
            for agent_id, agent_status in status["agents"].items():
                print(f"  ✅ {agent_id}")
            
            print(f"\n📊 WORKSPACE:")
            music_info = status["workspace"]["music_archive"]
            print(f"  • Music files: {music_info['file_count']}")
            print(f"  • Total size: {music_info['total_size_gb']:.2f} GB")
            print(f"  • Formats: {', '.join(music_info['formats'])}")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())