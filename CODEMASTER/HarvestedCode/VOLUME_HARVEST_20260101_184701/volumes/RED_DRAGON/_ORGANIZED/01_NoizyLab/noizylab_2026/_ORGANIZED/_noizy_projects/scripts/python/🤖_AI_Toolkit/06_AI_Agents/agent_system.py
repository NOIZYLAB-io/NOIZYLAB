#!/usr/bin/env python3
"""
NoizyFish AI Agent System
Autonomous AI agents that can perform complex tasks and workflows
"""

import os
import json
import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, asdict
from enum import Enum
import openai
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AgentStatus(Enum):
    IDLE = "idle"
    WORKING = "working"
    COMPLETED = "completed"
    ERROR = "error"
    PAUSED = "paused"

class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

@dataclass
class Task:
    id: str
    name: str
    description: str
    priority: TaskPriority
    agent_type: str
    parameters: Dict[str, Any]
    created_at: datetime
    deadline: Optional[datetime] = None
    dependencies: List[str] = None
    status: str = "pending"
    result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None

class BaseAgent:
    """Base class for all AI agents"""
    
    def __init__(self, agent_id: str, name: str, description: str, 
                 capabilities: List[str], api_key: Optional[str] = None):
        self.agent_id = agent_id
        self.name = name
        self.description = description
        self.capabilities = capabilities
        self.status = AgentStatus.IDLE
        self.current_task = None
        self.task_history = []
        self.client = openai.OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        
    async def execute_task(self, task: Task) -> Dict[str, Any]:
        """Execute a task - to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement execute_task")
    
    def can_handle_task(self, task: Task) -> bool:
        """Check if this agent can handle the given task"""
        return task.agent_type in self.capabilities
    
    async def process_task(self, task: Task) -> Dict[str, Any]:
        """Process a task with error handling and logging"""
        try:
            self.status = AgentStatus.WORKING
            self.current_task = task
            
            logger.info(f"Agent {self.name} starting task: {task.name}")
            
            result = await self.execute_task(task)
            
            self.status = AgentStatus.COMPLETED
            self.task_history.append(task)
            
            logger.info(f"Agent {self.name} completed task: {task.name}")
            
            return result
            
        except Exception as e:
            self.status = AgentStatus.ERROR
            error_msg = f"Error in agent {self.name}: {str(e)}"
            logger.error(error_msg)
            
            return {
                "success": False,
                "error": error_msg,
                "task_id": task.id
            }
        finally:
            self.current_task = None

class MusicProductionAgent(BaseAgent):
    """Agent specialized in music production tasks"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(
            agent_id="music_producer",
            name="Music Production Agent",
            description="Handles music analysis, transcription, and production tasks",
            capabilities=["audio_transcription", "music_analysis", "beat_generation", "lyrics_creation"],
            api_key=api_key
        )
    
    async def execute_task(self, task: Task) -> Dict[str, Any]:
        """Execute music production tasks"""
        task_type = task.parameters.get("task_type")
        
        if task_type == "analyze_audio":
            return await self._analyze_audio(task.parameters)
        elif task_type == "transcribe_vocals":
            return await self._transcribe_vocals(task.parameters)
        elif task_type == "generate_lyrics":
            return await self._generate_lyrics(task.parameters)
        elif task_type == "create_beat_pattern":
            return await self._create_beat_pattern(task.parameters)
        else:
            raise ValueError(f"Unknown music task type: {task_type}")
    
    async def _analyze_audio(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze audio file characteristics"""
        audio_file = params.get("audio_file")
        
        # This would integrate with your Voice Analysis tool
        analysis_prompt = f"""
        Analyze this audio file for music production:
        File: {audio_file}
        
        Provide analysis for:
        1. BPM and tempo
        2. Key signature
        3. Musical style/genre
        4. Instrumentation
        5. Mix quality
        6. Suggestions for improvement
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert music producer and audio engineer."},
                {"role": "user", "content": analysis_prompt}
            ],
            temperature=0.3
        )
        
        return {
            "success": True,
            "analysis": response.choices[0].message.content,
            "file": audio_file,
            "timestamp": datetime.now().isoformat()
        }
    
    async def _transcribe_vocals(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Transcribe vocal content from audio"""
        audio_file = params.get("audio_file")
        
        try:
            with open(audio_file, 'rb') as audio:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio,
                    response_format="verbose_json"
                )
            
            return {
                "success": True,
                "transcription": transcript.text,
                "language": transcript.language,
                "duration": transcript.duration,
                "file": audio_file
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Transcription failed: {str(e)}"
            }
    
    async def _generate_lyrics(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate song lyrics"""
        theme = params.get("theme", "general")
        genre = params.get("genre", "pop")
        mood = params.get("mood", "upbeat")
        
        prompt = f"""
        Write song lyrics with these specifications:
        - Theme: {theme}
        - Genre: {genre}
        - Mood: {mood}
        
        Create engaging, memorable lyrics with proper song structure.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional songwriter."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return {
            "success": True,
            "lyrics": response.choices[0].message.content,
            "theme": theme,
            "genre": genre,
            "mood": mood
        }
    
    async def _create_beat_pattern(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Create beat patterns and drum sequences"""
        bpm = params.get("bpm", 120)
        style = params.get("style", "hip-hop")
        
        prompt = f"""
        Create a {style} drum pattern at {bpm} BPM.
        
        Provide:
        1. Kick drum pattern (16th note grid)
        2. Snare/clap pattern
        3. Hi-hat pattern
        4. Any additional percussion
        5. Groove description
        6. Programming tips
        
        Format as both text description and pattern notation.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert drummer and beat programmer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        
        return {
            "success": True,
            "beat_pattern": response.choices[0].message.content,
            "bpm": bpm,
            "style": style
        }

class CreativeAgent(BaseAgent):
    """Agent for creative tasks like writing and visual content"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(
            agent_id="creative_assistant",
            name="Creative Agent",
            description="Handles creative writing, brainstorming, and content generation",
            capabilities=["writing", "brainstorming", "image_generation", "creative_concepts"],
            api_key=api_key
        )
    
    async def execute_task(self, task: Task) -> Dict[str, Any]:
        """Execute creative tasks"""
        task_type = task.parameters.get("task_type")
        
        if task_type == "brainstorm_ideas":
            return await self._brainstorm_ideas(task.parameters)
        elif task_type == "write_content":
            return await self._write_content(task.parameters)
        elif task_type == "generate_concepts":
            return await self._generate_concepts(task.parameters)
        elif task_type == "create_album_concept":
            return await self._create_album_concept(task.parameters)
        else:
            raise ValueError(f"Unknown creative task type: {task_type}")
    
    async def _brainstorm_ideas(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Brainstorm creative ideas"""
        topic = params.get("topic")
        count = params.get("count", 10)
        category = params.get("category", "general")
        
        prompt = f"""
        Brainstorm {count} creative ideas for {category} about: {topic}
        
        Make each idea:
        - Unique and innovative
        - Actionable and specific
        - Inspiring and memorable
        - Diverse in approach
        
        Format as numbered list with brief descriptions.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative director and innovation expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        
        return {
            "success": True,
            "ideas": response.choices[0].message.content,
            "topic": topic,
            "category": category,
            "count": count
        }
    
    async def _write_content(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Write various types of content"""
        content_type = params.get("content_type", "general")
        prompt_text = params.get("prompt")
        tone = params.get("tone", "professional")
        length = params.get("length", "medium")
        
        prompt = f"""
        Write {content_type} content with these specifications:
        - Topic/Prompt: {prompt_text}
        - Tone: {tone}
        - Length: {length}
        
        Create engaging, well-structured content that serves its purpose effectively.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an expert {content_type} writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        
        return {
            "success": True,
            "content": response.choices[0].message.content,
            "content_type": content_type,
            "tone": tone,
            "length": length
        }
    
    async def _generate_concepts(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate creative concepts and themes"""
        project_type = params.get("project_type")
        style = params.get("style", "modern")
        inspiration = params.get("inspiration", "")
        
        prompt = f"""
        Generate creative concepts for a {project_type} project:
        
        Style: {style}
        Inspiration: {inspiration}
        
        Provide:
        1. 3-5 unique concept directions
        2. Visual/aesthetic descriptions
        3. Mood and atmosphere
        4. Key elements and themes
        5. Implementation suggestions
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative concept designer and art director."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return {
            "success": True,
            "concepts": response.choices[0].message.content,
            "project_type": project_type,
            "style": style
        }
    
    async def _create_album_concept(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Create comprehensive album concepts"""
        album_theme = params.get("theme")
        genre = params.get("genre")
        artist_name = params.get("artist", "NoizyFish")
        
        prompt = f"""
        Create a complete album concept for {artist_name}:
        
        Theme: {album_theme}
        Genre: {genre}
        
        Provide:
        1. Album title and subtitle
        2. Track list with song titles (10-12 tracks)
        3. Overall narrative/story arc
        4. Visual aesthetic description
        5. Marketing angle and target audience
        6. Key singles and their concepts
        7. Album artwork direction
        8. Production style notes
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a music industry A&R executive and creative director."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return {
            "success": True,
            "album_concept": response.choices[0].message.content,
            "theme": album_theme,
            "genre": genre,
            "artist": artist_name
        }

class TechnicalAgent(BaseAgent):
    """Agent for technical and development tasks"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(
            agent_id="technical_assistant",
            name="Technical Agent",
            description="Handles coding, debugging, and technical analysis",
            capabilities=["code_analysis", "debugging", "system_optimization", "documentation"],
            api_key=api_key
        )
    
    async def execute_task(self, task: Task) -> Dict[str, Any]:
        """Execute technical tasks"""
        task_type = task.parameters.get("task_type")
        
        if task_type == "analyze_code":
            return await self._analyze_code(task.parameters)
        elif task_type == "debug_issue":
            return await self._debug_issue(task.parameters)
        elif task_type == "optimize_performance":
            return await self._optimize_performance(task.parameters)
        elif task_type == "generate_documentation":
            return await self._generate_documentation(task.parameters)
        else:
            raise ValueError(f"Unknown technical task type: {task_type}")
    
    async def _analyze_code(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze code for quality and improvements"""
        code = params.get("code")
        language = params.get("language", "python")
        
        prompt = f"""
        Analyze this {language} code for:
        
        1. Code quality and best practices
        2. Potential bugs or issues
        3. Performance improvements
        4. Security considerations
        5. Maintainability suggestions
        
        Code:
        ```{language}
        {code}
        ```
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior software engineer and code reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return {
            "success": True,
            "analysis": response.choices[0].message.content,
            "language": language,
            "timestamp": datetime.now().isoformat()
        }
    
    async def _debug_issue(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Debug code issues and provide solutions"""
        code = params.get("code")
        error_message = params.get("error_message")
        language = params.get("language", "python")
        
        prompt = f"""
        Debug this {language} code error:
        
        Error: {error_message}
        
        Code:
        ```{language}
        {code}
        ```
        
        Provide:
        1. Root cause analysis
        2. Fixed code
        3. Explanation of the fix
        4. Prevention strategies
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert debugger and problem solver."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return {
            "success": True,
            "debug_solution": response.choices[0].message.content,
            "language": language,
            "error": error_message
        }
    
    async def _optimize_performance(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize code or system performance"""
        code = params.get("code")
        performance_issue = params.get("issue", "general optimization")
        language = params.get("language", "python")
        
        prompt = f"""
        Optimize this {language} code for better performance:
        
        Performance issue: {performance_issue}
        
        Code:
        ```{language}
        {code}
        ```
        
        Provide:
        1. Optimized version
        2. Performance improvements explanation
        3. Benchmarking suggestions
        4. Alternative approaches
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a performance optimization expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return {
            "success": True,
            "optimization": response.choices[0].message.content,
            "language": language,
            "issue": performance_issue
        }
    
    async def _generate_documentation(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate technical documentation"""
        code = params.get("code")
        doc_type = params.get("doc_type", "API documentation")
        language = params.get("language", "python")
        
        prompt = f"""
        Generate {doc_type} for this {language} code:
        
        ```{language}
        {code}
        ```
        
        Include:
        1. Clear descriptions
        2. Parameter explanations
        3. Usage examples
        4. Return value documentation
        5. Error handling notes
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a technical documentation specialist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return {
            "success": True,
            "documentation": response.choices[0].message.content,
            "doc_type": doc_type,
            "language": language
        }

class AgentManager:
    """Manages multiple AI agents and task distribution"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.agents: Dict[str, BaseAgent] = {}
        self.task_queue: List[Task] = []
        self.completed_tasks: List[Task] = []
        self.running = False
        
        # Initialize default agents
        self._initialize_agents()
    
    def _initialize_agents(self):
        """Initialize the default set of agents"""
        self.agents = {
            "music_producer": MusicProductionAgent(self.api_key),
            "creative_assistant": CreativeAgent(self.api_key),
            "technical_assistant": TechnicalAgent(self.api_key)
        }
        
        logger.info(f"Initialized {len(self.agents)} agents")
    
    def add_agent(self, agent: BaseAgent):
        """Add a new agent to the system"""
        self.agents[agent.agent_id] = agent
        logger.info(f"Added agent: {agent.name}")
    
    def create_task(self, name: str, description: str, agent_type: str,
                   parameters: Dict[str, Any], priority: TaskPriority = TaskPriority.MEDIUM,
                   deadline: Optional[datetime] = None) -> Task:
        """Create a new task"""
        task = Task(
            id=f"task_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.task_queue)}",
            name=name,
            description=description,
            priority=priority,
            agent_type=agent_type,
            parameters=parameters,
            created_at=datetime.now(),
            deadline=deadline
        )
        
        self.task_queue.append(task)
        self.task_queue.sort(key=lambda t: t.priority.value, reverse=True)
        
        logger.info(f"Created task: {task.name} (Priority: {task.priority.name})")
        
        return task
    
    async def assign_task(self, task: Task) -> Optional[BaseAgent]:
        """Assign a task to an appropriate agent"""
        available_agents = [
            agent for agent in self.agents.values()
            if agent.status == AgentStatus.IDLE and agent.can_handle_task(task)
        ]
        
        if not available_agents:
            logger.warning(f"No available agents for task: {task.name}")
            return None
        
        # Simple assignment - first available agent
        selected_agent = available_agents[0]
        logger.info(f"Assigned task {task.name} to agent {selected_agent.name}")
        
        return selected_agent
    
    async def process_tasks(self):
        """Process tasks in the queue"""
        while self.task_queue and self.running:
            task = self.task_queue.pop(0)
            
            agent = await self.assign_task(task)
            if agent:
                task.status = "assigned"
                
                # Process task asynchronously
                result = await agent.process_task(task)
                
                task.result = result
                task.status = "completed" if result.get("success") else "failed"
                
                self.completed_tasks.append(task)
                
                # Save task result
                await self._save_task_result(task)
            else:
                # Put task back in queue if no agent available
                self.task_queue.append(task)
                await asyncio.sleep(1)  # Wait before retrying
    
    async def _save_task_result(self, task: Task):
        """Save task results to file"""
        results_dir = Path("agent_results")
        results_dir.mkdir(exist_ok=True)
        
        filename = f"{task.id}_{task.name.replace(' ', '_')}.json"
        filepath = results_dir / filename
        
        task_data = asdict(task)
        task_data['created_at'] = task_data['created_at'].isoformat()
        if task_data['deadline']:
            task_data['deadline'] = task_data['deadline'].isoformat()
        
        with open(filepath, 'w') as f:
            json.dump(task_data, f, indent=2, default=str)
        
        logger.info(f"Saved task result: {filepath}")
    
    def start(self):
        """Start the agent manager"""
        self.running = True
        logger.info("Agent Manager started")
    
    def stop(self):
        """Stop the agent manager"""
        self.running = False
        logger.info("Agent Manager stopped")
    
    def get_status(self) -> Dict[str, Any]:
        """Get system status"""
        return {
            "agents": {
                agent_id: {
                    "name": agent.name,
                    "status": agent.status.value,
                    "current_task": agent.current_task.name if agent.current_task else None,
                    "completed_tasks": len(agent.task_history)
                }
                for agent_id, agent in self.agents.items()
            },
            "queue_size": len(self.task_queue),
            "completed_tasks": len(self.completed_tasks),
            "running": self.running
        }

# Example usage and testing
async def main():
    """Example usage of the agent system"""
    
    # Initialize agent manager
    manager = AgentManager()
    manager.start()
    
    # Create some example tasks
    tasks = [
        manager.create_task(
            name="Analyze NoizyFish Audio",
            description="Analyze audio files from the music archive",
            agent_type="music_producer",
            parameters={
                "task_type": "analyze_audio",
                "audio_file": "/Users/rsp_ms/NoizyFish_Aquarium/🎵 Original_Music_Archive/00_The_FLAP_4.wav"
            },
            priority=TaskPriority.HIGH
        ),
        
        manager.create_task(
            name="Create Underwater Beat",
            description="Generate lyrics about underwater music studio",
            agent_type="music_producer",
            parameters={
                "task_type": "generate_lyrics",
                "theme": "underwater music studio where fish create beats",
                "genre": "electronic",
                "mood": "dreamy"
            },
            priority=TaskPriority.MEDIUM
        ),
        
        manager.create_task(
            name="Album Concept Development",
            description="Create a complete album concept for NoizyFish",
            agent_type="creative_assistant",
            parameters={
                "task_type": "create_album_concept",
                "theme": "Deep Sea Sound Laboratory",
                "genre": "Electronic Ambient",
                "artist": "NoizyFish"
            },
            priority=TaskPriority.HIGH
        )
    ]
    
    # Process tasks
    await manager.process_tasks()
    
    # Print status
    status = manager.get_status()
    print(json.dumps(status, indent=2))
    
    manager.stop()

if __name__ == "__main__":
    asyncio.run(main())
    