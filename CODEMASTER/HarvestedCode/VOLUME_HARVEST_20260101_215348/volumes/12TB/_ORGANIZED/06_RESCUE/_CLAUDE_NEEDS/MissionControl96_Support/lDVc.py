#!/usr/bin/env python3
"""
NoizyFish Agent Workflows - Predefined workflows for common tasks
Combines multiple agents to complete complex multi-step processes
"""

import asyncio
import json
from datetime import datetime
from typing import Dict, List, Any
from agent_system import AgentManager, TaskPriority

class WorkflowEngine:
    """Manages and executes complex multi-agent workflows"""
    
    def __init__(self, manager: AgentManager):
        self.manager = manager
        self.workflows = {}
        self._register_workflows()
    
    def _register_workflows(self):
        """Register available workflows"""
        self.workflows = {
            "music_production_pipeline": self.music_production_pipeline,
            "album_creation_workflow": self.album_creation_workflow,
            "content_creation_suite": self.content_creation_suite,
            "audio_analysis_deep_dive": self.audio_analysis_deep_dive,
            "creative_brainstorm_session": self.creative_brainstorm_session
        }
    
    async def execute_workflow(self, workflow_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a named workflow"""
        if workflow_name not in self.workflows:
            raise ValueError(f"Unknown workflow: {workflow_name}")
        
        print(f"🚀 Starting workflow: {workflow_name}")
        
        workflow_func = self.workflows[workflow_name]
        result = await workflow_func(parameters)
        
        print(f"✅ Completed workflow: {workflow_name}")
        
        return result
    
    async def music_production_pipeline(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Complete music production pipeline:
        1. Analyze existing audio files
        2. Transcribe vocals if present
        3. Generate improvement suggestions
        4. Create new lyrics based on analysis
        5. Design album artwork concept
        """
        audio_files = params.get("audio_files", [])
        album_theme = params.get("album_theme", "Deep Ocean Sounds")
        genre = params.get("genre", "Electronic Ambient")
        
        results = {}
        
        print("🎵 Step 1: Analyzing audio files...")
        # Analyze each audio file
        analysis_tasks = []
        for audio_file in audio_files:
            task = self.manager.create_task(
                name=f"Analyze: {audio_file}",
                description=f"Deep analysis of {audio_file}",
                agent_type="audio_transcription",
                parameters={
                    "task_type": "analyze_audio",
                    "audio_file": audio_file
                },
                priority=TaskPriority.HIGH
            )
            analysis_tasks.append(task)
        
        # Process analysis tasks
        await self.manager.process_tasks()
        
        # Collect analysis results
        audio_analyses = []
        for task in self.manager.completed_tasks[-len(analysis_tasks):]:
            if task.result and task.result.get("success"):
                audio_analyses.append(task.result)
        
        results["audio_analysis"] = audio_analyses
        
        print("🎤 Step 2: Transcribing vocals...")
        # Transcribe vocals from audio files
        transcription_tasks = []
        for audio_file in audio_files:
            task = self.manager.create_task(
                name=f"Transcribe: {audio_file}",
                description=f"Extract vocals from {audio_file}",
                agent_type="audio_transcription",
                parameters={
                    "task_type": "transcribe_vocals",
                    "audio_file": audio_file
                },
                priority=TaskPriority.HIGH
            )
            transcription_tasks.append(task)
        
        await self.manager.process_tasks()
        
        # Collect transcriptions
        transcriptions = []
        for task in self.manager.completed_tasks[-len(transcription_tasks):]:
            if task.result and task.result.get("success"):
                transcriptions.append(task.result)
        
        results["transcriptions"] = transcriptions
        
        print("✍️ Step 3: Creating new lyrics...")
        # Generate new lyrics based on theme
        lyrics_task = self.manager.create_task(
            name="Generate Album Lyrics",
            description=f"Create lyrics for {album_theme} album",
            agent_type="lyrics_creation",
            parameters={
                "task_type": "generate_lyrics",
                "theme": album_theme,
                "genre": genre,
                "mood": "atmospheric"
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        
        if self.manager.completed_tasks[-1].result.get("success"):
            results["new_lyrics"] = self.manager.completed_tasks[-1].result
        
        print("🎨 Step 4: Designing album concept...")
        # Create album concept
        concept_task = self.manager.create_task(
            name="Album Concept Design",
            description=f"Complete concept for {album_theme}",
            agent_type="creative_concepts",
            parameters={
                "task_type": "create_album_concept",
                "theme": album_theme,
                "genre": genre,
                "artist": "NoizyFish"
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        
        if self.manager.completed_tasks[-1].result.get("success"):
            results["album_concept"] = self.manager.completed_tasks[-1].result
        
        print("🎯 Step 5: Production recommendations...")
        # Generate production recommendations
        production_task = self.manager.create_task(
            name="Production Recommendations",
            description="Create production guide based on analysis",
            agent_type="creative_concepts",
            parameters={
                "task_type": "write_content",
                "content_type": "production guide",
                "prompt": f"Production recommendations for {album_theme} {genre} album based on audio analysis",
                "tone": "professional",
                "length": "detailed"
            },
            priority=TaskPriority.MEDIUM
        )
        
        await self.manager.process_tasks()
        
        if self.manager.completed_tasks[-1].result.get("success"):
            results["production_guide"] = self.manager.completed_tasks[-1].result
        
        # Save workflow results
        await self._save_workflow_results("music_production_pipeline", results)
        
        return results
    
    async def album_creation_workflow(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Complete album creation workflow:
        1. Brainstorm album concepts
        2. Create track listing
        3. Generate lyrics for key tracks
        4. Design visual concepts
        5. Plan marketing strategy
        """
        artist_name = params.get("artist", "NoizyFish")
        style_inspiration = params.get("inspiration", "underwater soundscapes")
        target_audience = params.get("audience", "electronic music enthusiasts")
        
        results = {}
        
        print("💡 Step 1: Brainstorming album concepts...")
        concept_task = self.manager.create_task(
            name="Album Concept Brainstorm",
            description="Generate multiple album concept ideas",
            agent_type="brainstorming",
            parameters={
                "task_type": "brainstorm_ideas",
                "topic": f"album concepts for {artist_name} inspired by {style_inspiration}",
                "category": "music album",
                "count": 8
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        results["concept_ideas"] = self.manager.completed_tasks[-1].result
        
        print("📋 Step 2: Creating album structure...")
        structure_task = self.manager.create_task(
            name="Album Structure Design",
            description="Create detailed album concept and track listing",
            agent_type="creative_concepts",
            parameters={
                "task_type": "create_album_concept",
                "theme": style_inspiration,
                "genre": "electronic ambient",
                "artist": artist_name
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        results["album_structure"] = self.manager.completed_tasks[-1].result
        
        print("🎵 Step 3: Writing signature tracks...")
        # Generate lyrics for 3 key tracks
        key_tracks = ["Opening Track", "Title Track", "Closing Track"]
        track_lyrics = {}
        
        for track in key_tracks:
            lyrics_task = self.manager.create_task(
                name=f"Lyrics: {track}",
                description=f"Write lyrics for {track}",
                agent_type="lyrics_creation",
                parameters={
                    "task_type": "generate_lyrics",
                    "theme": f"{style_inspiration} - {track}",
                    "genre": "electronic ambient",
                    "mood": "ethereal"
                },
                priority=TaskPriority.MEDIUM
            )
        
        await self.manager.process_tasks()
        
        # Collect lyrics for the 3 tracks
        for i, track in enumerate(key_tracks):
            task_result = self.manager.completed_tasks[-(len(key_tracks)-i)]
            if task_result.result.get("success"):
                track_lyrics[track] = task_result.result
        
        results["track_lyrics"] = track_lyrics
        
        print("🎨 Step 4: Visual concept development...")
        visual_task = self.manager.create_task(
            name="Visual Concept Design",
            description="Create visual concepts for album",
            agent_type="creative_concepts",
            parameters={
                "task_type": "generate_concepts",
                "project_type": "album visual identity",
                "style": "underwater electronic",
                "inspiration": style_inspiration
            },
            priority=TaskPriority.MEDIUM
        )
        
        await self.manager.process_tasks()
        results["visual_concepts"] = self.manager.completed_tasks[-1].result
        
        print("📢 Step 5: Marketing strategy...")
        marketing_task = self.manager.create_task(
            name="Marketing Strategy",
            description="Develop marketing approach",
            agent_type="creative_concepts",
            parameters={
                "task_type": "write_content",
                "content_type": "marketing strategy",
                "prompt": f"Marketing strategy for {artist_name} album targeting {target_audience}",
                "tone": "strategic",
                "length": "comprehensive"
            },
            priority=TaskPriority.LOW
        )
        
        await self.manager.process_tasks()
        results["marketing_strategy"] = self.manager.completed_tasks[-1].result
        
        await self._save_workflow_results("album_creation_workflow", results)
        
        return results
    
    async def content_creation_suite(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Content creation workflow:
        1. Brainstorm content ideas
        2. Create blog posts/articles
        3. Generate social media content
        4. Design promotional materials
        """
        topic = params.get("topic", "AI in music production")
        target_platform = params.get("platform", "general")
        content_goals = params.get("goals", "education and engagement")
        
        results = {}
        
        print("💭 Step 1: Content ideation...")
        ideas_task = self.manager.create_task(
            name="Content Ideas",
            description=f"Brainstorm content ideas for {topic}",
            agent_type="brainstorming",
            parameters={
                "task_type": "brainstorm_ideas",
                "topic": topic,
                "category": "content marketing",
                "count": 12
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        results["content_ideas"] = self.manager.completed_tasks[-1].result
        
        print("📝 Step 2: Article creation...")
        article_task = self.manager.create_task(
            name="Main Article",
            description=f"Write comprehensive article about {topic}",
            agent_type="writing",
            parameters={
                "task_type": "write_content",
                "content_type": "educational article",
                "prompt": f"Comprehensive guide to {topic} for {target_platform}",
                "tone": "informative and engaging",
                "length": "long-form"
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        results["main_article"] = self.manager.completed_tasks[-1].result
        
        print("📱 Step 3: Social media content...")
        social_task = self.manager.create_task(
            name="Social Media Content",
            description="Create social media posts",
            agent_type="writing",
            parameters={
                "task_type": "write_content",
                "content_type": "social media posts",
                "prompt": f"Engaging social media content about {topic}",
                "tone": "casual and engaging",
                "length": "short"
            },
            priority=TaskPriority.MEDIUM
        )
        
        await self.manager.process_tasks()
        results["social_content"] = self.manager.completed_tasks[-1].result
        
        print("🎯 Step 4: Content strategy...")
        strategy_task = self.manager.create_task(
            name="Content Strategy",
            description="Develop content distribution strategy",
            agent_type="creative_concepts",
            parameters={
                "task_type": "write_content",
                "content_type": "content strategy",
                "prompt": f"Content distribution strategy for {topic} to achieve {content_goals}",
                "tone": "strategic",
                "length": "detailed"
            },
            priority=TaskPriority.LOW
        )
        
        await self.manager.process_tasks()
        results["content_strategy"] = self.manager.completed_tasks[-1].result
        
        await self._save_workflow_results("content_creation_suite", results)
        
        return results
    
    async def audio_analysis_deep_dive(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deep audio analysis workflow:
        1. Technical audio analysis
        2. Vocal transcription and analysis
        3. Musical structure analysis
        4. Improvement recommendations
        5. Genre and style classification
        """
        audio_files = params.get("audio_files", [])
        analysis_focus = params.get("focus", "comprehensive")
        
        results = {}
        
        print("🔬 Step 1: Technical analysis...")
        for audio_file in audio_files:
            # Technical analysis
            tech_task = self.manager.create_task(
                name=f"Technical Analysis: {audio_file}",
                description=f"Deep technical analysis of {audio_file}",
                agent_type="audio_transcription",
                parameters={
                    "task_type": "analyze_audio",
                    "audio_file": audio_file
                },
                priority=TaskPriority.HIGH
            )
        
        await self.manager.process_tasks()
        
        print("🎤 Step 2: Vocal analysis...")
        for audio_file in audio_files:
            # Vocal transcription
            vocal_task = self.manager.create_task(
                name=f"Vocal Analysis: {audio_file}",
                description=f"Transcribe and analyze vocals in {audio_file}",
                agent_type="audio_transcription",
                parameters={
                    "task_type": "transcribe_vocals",
                    "audio_file": audio_file
                },
                priority=TaskPriority.HIGH
            )
        
        await self.manager.process_tasks()
        
        print("🎼 Step 3: Musical structure analysis...")
        structure_task = self.manager.create_task(
            name="Musical Structure Analysis",
            description="Analyze musical structure and composition",
            agent_type="creative_concepts",
            parameters={
                "task_type": "write_content",
                "content_type": "musical analysis",
                "prompt": f"Analyze musical structure and composition techniques in the provided audio files",
                "tone": "analytical",
                "length": "detailed"
            },
            priority=TaskPriority.MEDIUM
        )
        
        await self.manager.process_tasks()
        
        print("💡 Step 4: Improvement recommendations...")
        improvement_task = self.manager.create_task(
            name="Improvement Recommendations",
            description="Generate specific improvement suggestions",
            agent_type="creative_concepts",
            parameters={
                "task_type": "write_content",
                "content_type": "improvement guide",
                "prompt": "Specific recommendations for improving the analyzed audio tracks",
                "tone": "constructive",
                "length": "detailed"
            },
            priority=TaskPriority.MEDIUM
        )
        
        await self.manager.process_tasks()
        
        # Collect all results
        recent_tasks = self.manager.completed_tasks[-(len(audio_files) * 2 + 2):]
        
        results["analysis"] = {
            "technical": [t.result for t in recent_tasks if "Technical Analysis" in t.name],
            "vocal": [t.result for t in recent_tasks if "Vocal Analysis" in t.name],
            "structure": recent_tasks[-2].result,
            "improvements": recent_tasks[-1].result
        }
        
        await self._save_workflow_results("audio_analysis_deep_dive", results)
        
        return results
    
    async def creative_brainstorm_session(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creative brainstorming workflow:
        1. Generate initial ideas
        2. Expand on promising concepts
        3. Create detailed concepts
        4. Develop implementation plans
        """
        topic = params.get("topic", "innovative music technology")
        session_goal = params.get("goal", "product development")
        creative_constraints = params.get("constraints", "none specified")
        
        results = {}
        
        print("🌟 Step 1: Initial ideation...")
        initial_ideas_task = self.manager.create_task(
            name="Initial Ideas Generation",
            description=f"Generate diverse ideas for {topic}",
            agent_type="brainstorming",
            parameters={
                "task_type": "brainstorm_ideas",
                "topic": topic,
                "category": session_goal,
                "count": 15
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        results["initial_ideas"] = self.manager.completed_tasks[-1].result
        
        print("🔍 Step 2: Concept expansion...")
        expansion_task = self.manager.create_task(
            name="Concept Expansion",
            description="Expand on the most promising ideas",
            agent_type="creative_concepts",
            parameters={
                "task_type": "generate_concepts",
                "project_type": session_goal,
                "style": "innovative",
                "inspiration": topic
            },
            priority=TaskPriority.HIGH
        )
        
        await self.manager.process_tasks()
        results["expanded_concepts"] = self.manager.completed_tasks[-1].result
        
        print("📋 Step 3: Detailed development...")
        detailed_task = self.manager.create_task(
            name="Detailed Concept Development",
            description="Create detailed concepts with specifications",
            agent_type="creative_concepts",
            parameters={
                "task_type": "write_content",
                "content_type": "concept documentation",
                "prompt": f"Detailed concept development for {topic} considering {creative_constraints}",
                "tone": "innovative",
                "length": "comprehensive"
            },
            priority=TaskPriority.MEDIUM
        )
        
        await self.manager.process_tasks()
        results["detailed_concepts"] = self.manager.completed_tasks[-1].result
        
        print("🛠️ Step 4: Implementation planning...")
        implementation_task = self.manager.create_task(
            name="Implementation Strategy",
            description="Create implementation roadmap",
            agent_type="creative_concepts",
            parameters={
                "task_type": "write_content",
                "content_type": "implementation plan",
                "prompt": f"Implementation roadmap for the developed {topic} concepts",
                "tone": "strategic",
                "length": "detailed"
            },
            priority=TaskPriority.MEDIUM
        )
        
        await self.manager.process_tasks()
        results["implementation_plan"] = self.manager.completed_tasks[-1].result
        
        await self._save_workflow_results("creative_brainstorm_session", results)
        
        return results
    
    async def _save_workflow_results(self, workflow_name: str, results: Dict[str, Any]):
        """Save workflow results to file"""
        workflow_dir = Path("workflow_results")
        workflow_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{workflow_name}_{timestamp}.json"
        filepath = workflow_dir / filename
        
        workflow_data = {
            "workflow": workflow_name,
            "timestamp": datetime.now().isoformat(),
            "results": results
        }
        
        with open(filepath, 'w') as f:
            json.dump(workflow_data, f, indent=2, default=str)
        
        print(f"💾 Saved workflow results: {filepath}")

# CLI for workflows
async def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="NoizyFish Workflow Engine")
    parser.add_argument("--workflow", required=True, 
                       choices=["music_production_pipeline", "album_creation_workflow", 
                               "content_creation_suite", "audio_analysis_deep_dive", 
                               "creative_brainstorm_session"],
                       help="Workflow to execute")
    parser.add_argument("--audio-files", nargs='+', help="Audio files to process")
    parser.add_argument("--theme", help="Album or content theme")
    parser.add_argument("--genre", default="electronic", help="Music genre")
    parser.add_argument("--topic", help="Topic for content or brainstorming")
    parser.add_argument("--artist", default="NoizyFish", help="Artist name")
    
    args = parser.parse_args()
    
    # Initialize workflow engine
    manager = AgentManager()
    manager.start()
    workflow_engine = WorkflowEngine(manager)
    
    # Prepare parameters
    params = {}
    if args.audio_files:
        params["audio_files"] = args.audio_files
    if args.theme:
        params["album_theme"] = args.theme
        params["inspiration"] = args.theme
    if args.genre:
        params["genre"] = args.genre
    if args.topic:
        params["topic"] = args.topic
    if args.artist:
        params["artist"] = args.artist
    
    # Execute workflow
    try:
        results = await workflow_engine.execute_workflow(args.workflow, params)
        
        print(f"\n🎉 Workflow '{args.workflow}' completed successfully!")
        print(f"📊 Generated {len(results)} result categories")
        
        # Show summary
        for category, result in results.items():
            if isinstance(result, dict) and result.get("success"):
                print(f"  ✅ {category}: Success")
            elif isinstance(result, list):
                print(f"  📋 {category}: {len(result)} items")
            else:
                print(f"  📄 {category}: Generated")
        
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
    finally:
        manager.stop()

if __name__ == "__main__":
    asyncio.run(main())