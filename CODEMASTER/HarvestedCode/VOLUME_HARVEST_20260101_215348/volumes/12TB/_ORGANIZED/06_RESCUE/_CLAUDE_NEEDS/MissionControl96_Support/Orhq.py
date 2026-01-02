#!/usr/bin/env python3
"""
Example: NoizyFish AI Agents in Action
Demonstrates the agent system with your actual music files
"""

import asyncio
import sys
import os
from pathlib import Path

# Add agent system to path
sys.path.append('/Users/rsp_ms/NoizyFish_Aquarium/🤖 AI_Toolkit/06_AI_Agents')

from agent_system import AgentManager, TaskPriority
from agent_workflows import WorkflowEngine

async def demo_music_analysis():
    """Demo: Analyze music from your archive"""
    
    print("🎵 NoizyFish AI Agents Demo - Music Analysis")
    print("=" * 50)
    
    # Initialize agent system
    manager = AgentManager()
    manager.start()
    
    # Sample audio file from your archive
    audio_file = "/Users/rsp_ms/NoizyFish_Aquarium/🎵 Original_Music_Archive/00_The_FLAP_4.wav"
    
    if not os.path.exists(audio_file):
        print(f"❌ Audio file not found: {audio_file}")
        print("Using placeholder for demo...")
        audio_file = "demo_audio.wav"
    
    try:
        print(f"🔍 Analyzing: {Path(audio_file).name}")
        
        # Create analysis task
        task = manager.create_task(
            name="NoizyFish Audio Analysis",
            description=f"Deep analysis of {Path(audio_file).name}",
            agent_type="audio_transcription",
            parameters={
                "task_type": "analyze_audio",
                "audio_file": audio_file
            },
            priority=TaskPriority.HIGH
        )
        
        print(f"✅ Created task: {task.name}")
        
        # Process the task
        print("🤖 Agent working...")
        await manager.process_tasks()
        
        # Show results
        if manager.completed_tasks:
            result = manager.completed_tasks[-1]
            print(f"\n📊 Analysis Results:")
            print(f"Task: {result.name}")
            print(f"Status: {result.status}")
            
            if result.result and result.result.get("success"):
                print("✅ Analysis completed successfully!")
                analysis = result.result.get("analysis", "No analysis available")
                print(f"\n🎼 Musical Analysis Preview:")
                print(analysis[:200] + "..." if len(analysis) > 200 else analysis)
            else:
                print("❌ Analysis failed")
                if result.result and "error" in result.result:
                    print(f"Error: {result.result['error']}")
        
    except Exception as e:
        print(f"❌ Demo error: {e}")
    
    finally:
        manager.stop()

async def demo_creative_workflow():
    """Demo: Creative workflow for NoizyFish album"""
    
    print("\n🎨 NoizyFish AI Agents Demo - Creative Workflow")
    print("=" * 50)
    
    # Initialize workflow engine
    manager = AgentManager()
    manager.start()
    workflow_engine = WorkflowEngine(manager)
    
    try:
        print("🚀 Starting Album Creation Workflow...")
        
        # Parameters for NoizyFish album
        params = {
            "artist": "NoizyFish",
            "inspiration": "deep ocean soundscapes and underwater technology",
            "audience": "electronic music enthusiasts and ambient music lovers"
        }
        
        # Execute workflow
        results = await workflow_engine.execute_workflow("album_creation_workflow", params)
        
        print(f"\n🎉 Workflow completed!")
        print(f"📊 Generated {len(results)} result categories:")
        
        for category, result in results.items():
            if isinstance(result, dict) and result.get("success"):
                print(f"  ✅ {category}: Success")
                
                # Show preview of some results
                if category == "album_structure" and "album_concept" in result:
                    concept = result["album_concept"]
                    print(f"     Preview: {concept[:100]}...")
                elif category == "track_lyrics":
                    print(f"     Generated lyrics for {len(result)} tracks")
                    
            elif isinstance(result, list):
                print(f"  📋 {category}: {len(result)} items")
            else:
                print(f"  📄 {category}: Generated")
        
        print(f"\n💾 Results saved in workflow_results/ directory")
        
    except Exception as e:
        print(f"❌ Workflow error: {e}")
    
    finally:
        manager.stop()

async def demo_interactive_session():
    """Demo: Interactive session with agents"""
    
    print("\n🤖 NoizyFish AI Agents Demo - Interactive Session")
    print("=" * 50)
    
    manager = AgentManager()
    manager.start()
    
    try:
        # Create a variety of tasks
        tasks = [
            # Music task
            manager.create_task(
                name="Generate Underwater Beats",
                description="Create beat patterns for underwater theme",
                agent_type="beat_generation",
                parameters={
                    "task_type": "create_beat_pattern",
                    "bpm": 120,
                    "style": "underwater ambient"
                },
                priority=TaskPriority.HIGH
            ),
            
            # Creative task
            manager.create_task(
                name="Brainstorm NoizyFish Ideas",
                description="Generate creative ideas for NoizyFish brand",
                agent_type="brainstorming",
                parameters={
                    "task_type": "brainstorm_ideas",
                    "topic": "NoizyFish brand development and music concepts",
                    "category": "music branding",
                    "count": 10
                },
                priority=TaskPriority.MEDIUM
            ),
            
            # Lyrics task
            manager.create_task(
                name="Ocean Laboratory Lyrics",
                description="Create lyrics about underwater music laboratory",
                agent_type="lyrics_creation",
                parameters={
                    "task_type": "generate_lyrics",
                    "theme": "scientific underwater music laboratory where fish conduct experiments",
                    "genre": "electronic experimental",
                    "mood": "mysterious and innovative"
                },
                priority=TaskPriority.HIGH
            )
        ]
        
        print(f"📋 Created {len(tasks)} tasks for agents to process")
        print("🤖 Agents working on tasks...")
        
        # Process all tasks
        await manager.process_tasks()
        
        # Show results summary
        print(f"\n📊 Task Results Summary:")
        print("-" * 30)
        
        for task in manager.completed_tasks:
            print(f"\n🎯 {task.name}")
            print(f"   Status: {task.status}")
            
            if task.result and task.result.get("success"):
                print("   ✅ Completed successfully")
                
                # Show specific result previews
                result = task.result
                if "beat_pattern" in result:
                    print("   🥁 Beat pattern generated")
                elif "ideas" in result:
                    print("   💡 Creative ideas generated")
                elif "lyrics" in result:
                    print("   🎵 Lyrics created")
                    lyrics = result["lyrics"]
                    print(f"   Preview: {lyrics[:100]}...")
            else:
                print("   ❌ Task failed")
                if task.result and "error" in task.result:
                    print(f"   Error: {task.result['error']}")
        
        # Show agent status
        print(f"\n🤖 Agent Status:")
        status = manager.get_status()
        
        for agent_id, agent_info in status["agents"].items():
            print(f"   {agent_info['name']}: {agent_info['status']}")
            print(f"      Completed: {agent_info['completed_tasks']} tasks")
        
    except Exception as e:
        print(f"❌ Interactive demo error: {e}")
    
    finally:
        manager.stop()

async def main():
    """Run all demos"""
    
    print("🐠 Welcome to NoizyFish AI Agents Demo!")
    print("This demo shows how AI agents can help with music production,")
    print("creative work, and workflow automation.")
    print("\n" + "=" * 60)
    
    # Run demos
    await demo_music_analysis()
    await demo_creative_workflow()
    await demo_interactive_session()
    
    print("\n" + "=" * 60)
    print("🎉 Demo completed!")
    print("\nTo use the agents interactively:")
    print("  python agent_cli.py --mode interactive")
    print("\nTo run workflows:")
    print("  python agent_workflows.py --workflow album_creation_workflow --theme 'Deep Ocean'")
    print("\n🐠 Happy creating with NoizyFish AI Agents!")

if __name__ == "__main__":
    asyncio.run(main())