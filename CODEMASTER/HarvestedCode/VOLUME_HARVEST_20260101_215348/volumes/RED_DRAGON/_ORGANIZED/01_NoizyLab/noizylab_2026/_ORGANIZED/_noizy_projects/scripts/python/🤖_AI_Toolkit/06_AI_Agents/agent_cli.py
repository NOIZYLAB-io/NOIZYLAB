#!/usr/bin/env python3
"""
NoizyFish Agent CLI - Command Line Interface for AI Agents
Easy-to-use interface for managing and interacting with AI agents
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from agent_system import AgentManager, TaskPriority

class AgentCLI:
    def __init__(self):
        self.manager = AgentManager()
        
    async def start_agents(self):
        """Start the agent system"""
        self.manager.start()
        print("🤖 NoizyFish AI Agents started!")
        
        # Show available agents
        print("\n📋 Available Agents:")
        for agent_id, agent in self.manager.agents.items():
            print(f"  • {agent.name}: {agent.description}")
            print(f"    Capabilities: {', '.join(agent.capabilities)}")
        
        return self.manager
    
    async def create_music_task(self, audio_file: str, task_type: str = "analyze_audio"):
        """Create a music production task"""
        task = self.manager.create_task(
            name=f"Music: {task_type}",
            description=f"Process audio file: {audio_file}",
            agent_type="audio_transcription",
            parameters={
                "task_type": task_type,
                "audio_file": audio_file
            },
            priority=TaskPriority.HIGH
        )
        
        print(f"✅ Created music task: {task.name}")
        return task
    
    async def create_lyrics_task(self, theme: str, genre: str = "electronic", mood: str = "upbeat"):
        """Create a lyrics generation task"""
        task = self.manager.create_task(
            name="Generate Lyrics",
            description=f"Create lyrics: {theme}",
            agent_type="lyrics_creation",
            parameters={
                "task_type": "generate_lyrics",
                "theme": theme,
                "genre": genre,
                "mood": mood
            },
            priority=TaskPriority.MEDIUM
        )
        
        print(f"✅ Created lyrics task: {task.name}")
        return task
    
    async def create_creative_task(self, task_type: str, prompt: str, **kwargs):
        """Create a creative task"""
        task = self.manager.create_task(
            name=f"Creative: {task_type}",
            description=f"Creative work: {prompt}",
            agent_type="creative_concepts",
            parameters={
                "task_type": task_type,
                "prompt": prompt,
                **kwargs
            },
            priority=TaskPriority.MEDIUM
        )
        
        print(f"✅ Created creative task: {task.name}")
        return task
    
    async def create_tech_task(self, task_type: str, code: str = "", **kwargs):
        """Create a technical task"""
        task = self.manager.create_task(
            name=f"Tech: {task_type}",
            description=f"Technical work: {task_type}",
            agent_type="code_analysis",
            parameters={
                "task_type": task_type,
                "code": code,
                **kwargs
            },
            priority=TaskPriority.LOW
        )
        
        print(f"✅ Created technical task: {task.name}")
        return task
    
    async def process_and_wait(self):
        """Process all tasks and wait for completion"""
        if not self.manager.task_queue:
            print("📝 No tasks in queue")
            return
        
        print(f"\n🔄 Processing {len(self.manager.task_queue)} tasks...")
        
        # Process tasks
        await self.manager.process_tasks()
        
        # Show results
        print(f"\n✅ Completed {len(self.manager.completed_tasks)} tasks")
        
        for task in self.manager.completed_tasks:
            print(f"\n📋 Task: {task.name}")
            print(f"   Status: {task.status}")
            if task.result and task.result.get("success"):
                print("   ✅ Success")
                # Show brief result
                result = task.result
                if "analysis" in result:
                    print(f"   📊 Analysis available")
                if "lyrics" in result:
                    print(f"   🎵 Lyrics generated")
                if "content" in result:
                    print(f"   📝 Content created")
            else:
                print("   ❌ Failed")
                if task.result and "error" in task.result:
                    print(f"   Error: {task.result['error']}")
    
    async def show_status(self):
        """Show system status"""
        status = self.manager.get_status()
        
        print("\n🤖 Agent System Status")
        print("=" * 40)
        
        for agent_id, agent_info in status["agents"].items():
            print(f"\n{agent_info['name']}:")
            print(f"  Status: {agent_info['status']}")
            print(f"  Current Task: {agent_info['current_task'] or 'None'}")
            print(f"  Completed: {agent_info['completed_tasks']} tasks")
        
        print(f"\nQueue: {status['queue_size']} tasks")
        print(f"Completed: {status['completed_tasks']} tasks")
        print(f"Running: {status['running']}")
    
    async def interactive_mode(self):
        """Interactive mode for creating and managing tasks"""
        await self.start_agents()
        
        print("\n🎛️  Interactive Agent Mode")
        print("Commands: music, lyrics, creative, tech, status, process, quit")
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                
                if command == "quit":
                    break
                elif command == "status":
                    await self.show_status()
                elif command == "process":
                    await self.process_and_wait()
                elif command == "music":
                    audio_file = input("Audio file path: ").strip()
                    if audio_file:
                        await self.create_music_task(audio_file)
                elif command == "lyrics":
                    theme = input("Lyrics theme: ").strip()
                    genre = input("Genre (default: electronic): ").strip() or "electronic"
                    mood = input("Mood (default: upbeat): ").strip() or "upbeat"
                    if theme:
                        await self.create_lyrics_task(theme, genre, mood)
                elif command == "creative":
                    task_type = input("Creative task type (brainstorm_ideas/write_content/create_album_concept): ").strip()
                    prompt = input("Prompt/topic: ").strip()
                    if task_type and prompt:
                        await self.create_creative_task(task_type, prompt)
                elif command == "tech":
                    task_type = input("Tech task type (analyze_code/debug_issue/optimize_performance): ").strip()
                    if task_type:
                        if task_type in ["analyze_code", "debug_issue", "optimize_performance"]:
                            code = input("Code to analyze (or file path): ").strip()
                            await self.create_tech_task(task_type, code)
                        else:
                            await self.create_tech_task(task_type)
                else:
                    print("Unknown command. Available: music, lyrics, creative, tech, status, process, quit")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
        
        self.manager.stop()
        print("\n👋 Goodbye!")

async def main():
    parser = argparse.ArgumentParser(description="NoizyFish AI Agent CLI")
    parser.add_argument("--mode", choices=["interactive", "batch"], default="interactive", 
                       help="Interaction mode")
    parser.add_argument("--music", help="Audio file to analyze")
    parser.add_argument("--lyrics", help="Theme for lyrics generation")
    parser.add_argument("--genre", default="electronic", help="Music genre")
    parser.add_argument("--mood", default="upbeat", help="Mood/emotion")
    parser.add_argument("--creative", help="Creative task prompt")
    parser.add_argument("--creative-type", default="brainstorm_ideas", 
                       help="Type of creative task")
    parser.add_argument("--code", help="Code to analyze")
    parser.add_argument("--tech-task", default="analyze_code", 
                       help="Type of technical task")
    
    args = parser.parse_args()
    
    cli = AgentCLI()
    
    if args.mode == "interactive":
        await cli.interactive_mode()
    else:
        # Batch mode
        await cli.start_agents()
        
        # Create tasks based on arguments
        if args.music:
            await cli.create_music_task(args.music)
        
        if args.lyrics:
            await cli.create_lyrics_task(args.lyrics, args.genre, args.mood)
        
        if args.creative:
            await cli.create_creative_task(args.creative_type, args.creative)
        
        if args.code:
            await cli.create_tech_task(args.tech_task, args.code)
        
        # Process all tasks
        await cli.process_and_wait()
        
        # Show final status
        await cli.show_status()
        
        cli.manager.stop()

if __name__ == "__main__":
    asyncio.run(main())