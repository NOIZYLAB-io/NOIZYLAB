#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ☁️  NOIZYLAB CLOUD AGENT CLIENT                                        ║
║                                                                           ║
║   Python client for delegating tasks to the Cloudflare Worker agent      ║
║   Integrates with master_orchestrator.py and cluster_launcher.py         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import json
import logging
import sys
import uuid
from typing import Dict, Any, Optional, List
from datetime import datetime
from dataclasses import dataclass, asdict
import urllib.request
import urllib.error
import urllib.parse

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

import os

CLOUD_AGENT_ENDPOINT = os.getenv(
    "CLOUD_AGENT_ENDPOINT", 
    "https://noizylab.rsplowman.workers.dev"
)
DEFAULT_TIMEOUT = int(os.getenv("CLOUD_AGENT_TIMEOUT", "30"))

# ═══════════════════════════════════════════════════════════════════════════
# DATA MODELS
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class TaskRequest:
    """Task delegation request"""
    task_type: str
    task_data: Dict[str, Any]
    task_id: Optional[str] = None
    priority: str = "normal"
    
    def to_dict(self) -> Dict:
        return {
            "task_id": self.task_id or str(uuid.uuid4()),
            "task_type": self.task_type,
            "task_data": self.task_data,
            "priority": self.priority
        }

@dataclass
class TaskResponse:
    """Task delegation response"""
    task_id: str
    status: str
    result: Optional[Any] = None
    error: Optional[str] = None
    timestamp: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TaskResponse':
        return cls(
            task_id=data.get("task_id", "unknown"),
            status=data.get("status", "unknown"),
            result=data.get("result"),
            error=data.get("error"),
            timestamp=data.get("timestamp")
        )

@dataclass
class AgentCapabilities:
    """Cloud agent capabilities"""
    agent_id: str
    capabilities: List[str]
    status: str
    timestamp: str
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentCapabilities':
        return cls(
            agent_id=data.get("agent_id", "unknown"),
            capabilities=data.get("capabilities", []),
            status=data.get("status", "unknown"),
            timestamp=data.get("timestamp", "")
        )

# ═══════════════════════════════════════════════════════════════════════════
# CLOUD AGENT CLIENT
# ═══════════════════════════════════════════════════════════════════════════

class CloudAgentClient:
    """
    Client for communicating with the NOIZYLAB Cloudflare Worker agent.
    
    Usage:
        client = CloudAgentClient()
        response = await client.delegate_task("echo", {"message": "Hello"})
        print(response.result)
    """
    
    def __init__(self, endpoint: str = CLOUD_AGENT_ENDPOINT, timeout: int = DEFAULT_TIMEOUT):
        self.endpoint = endpoint.rstrip('/')
        self.timeout = timeout
        self.logger = logging.getLogger("CloudAgentClient")
        self._loop = None
        self._executor = None
    
    def _get_executor(self):
        """Get or create thread pool executor for sync operations"""
        if self._executor is None:
            import concurrent.futures
            self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        return self._executor
    
    async def _make_request_async(
        self,
        path: str,
        method: str = "GET",
        data: Optional[Dict] = None
    ) -> Dict:
        """Make async HTTP request to cloud agent"""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self._get_executor(),
            self._make_request_sync,
            path,
            method,
            data
        )
    
    def _make_request_sync(
        self,
        path: str,
        method: str = "GET",
        data: Optional[Dict] = None
    ) -> Dict:
        """Make synchronous HTTP request to cloud agent"""
        url = f"{self.endpoint}{path}"
        headers = {"Content-Type": "application/json"}
        
        try:
            if method == "POST" and data:
                req_data = json.dumps(data).encode('utf-8')
                request = urllib.request.Request(url, data=req_data, headers=headers, method=method)
            else:
                request = urllib.request.Request(url, headers=headers, method=method)
            
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode('utf-8'))
        
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            try:
                error_data = json.loads(error_body)
                return error_data
            except json.JSONDecodeError:
                raise Exception(f"HTTP {e.code}: {error_body}")
        
        except urllib.error.URLError as e:
            raise Exception(f"Connection error: {e.reason}")
        
        except Exception as e:
            raise Exception(f"Request failed: {str(e)}")
    
    async def health_check(self) -> Dict[str, Any]:
        """Check cloud agent health"""
        self.logger.info(f"🔍 Checking cloud agent health at {self.endpoint}...")
        return await self._make_request_async("/health")
    
    async def get_capabilities(self) -> AgentCapabilities:
        """Get cloud agent capabilities"""
        self.logger.info("📋 Fetching cloud agent capabilities...")
        data = await self._make_request_async("/api/capabilities")
        return AgentCapabilities.from_dict(data)
    
    async def delegate_task(
        self,
        task_type: str,
        task_data: Dict[str, Any],
        task_id: Optional[str] = None,
        priority: str = "normal"
    ) -> TaskResponse:
        """
        Delegate a task to the cloud agent
        
        Args:
            task_type: Type of task (e.g., "echo", "inference", "code-analysis")
            task_data: Task-specific data
            task_id: Optional task ID (generated if not provided)
            priority: Task priority ("low", "normal", "high")
        
        Returns:
            TaskResponse with task result or error
        """
        request = TaskRequest(
            task_type=task_type,
            task_data=task_data,
            task_id=task_id,
            priority=priority
        )
        
        self.logger.info(f"🚀 Delegating task: {task_type} (ID: {request.task_id or 'auto'})")
        
        try:
            data = await self._make_request_async("/api/delegate", method="POST", data=request.to_dict())
            response = TaskResponse.from_dict(data)
            
            if response.status == "completed":
                self.logger.info(f"✅ Task completed: {response.task_id}")
            elif response.status == "failed":
                self.logger.error(f"❌ Task failed: {response.error}")
            else:
                self.logger.info(f"⏳ Task status: {response.status}")
            
            return response
        
        except Exception as e:
            self.logger.error(f"❌ Task delegation failed: {e}")
            return TaskResponse(
                task_id=request.task_id or "error",
                status="failed",
                error=str(e)
            )
    
    async def get_task_status(self, task_id: str) -> TaskResponse:
        """Get status of a previously submitted task"""
        self.logger.info(f"🔍 Checking status of task: {task_id}")
        data = await self._make_request_async(f"/api/status?task_id={task_id}")
        return TaskResponse.from_dict(data)
    
    async def batch_delegate(self, tasks: List[TaskRequest]) -> List[TaskResponse]:
        """Delegate multiple tasks"""
        self.logger.info(f"🚀 Delegating {len(tasks)} tasks...")
        
        responses = []
        for task in tasks:
            response = await self.delegate_task(
                task.task_type,
                task.task_data,
                task.task_id,
                task.priority
            )
            responses.append(response)
        
        return responses

# ═══════════════════════════════════════════════════════════════════════════
# ORCHESTRATOR INTEGRATION
# ═══════════════════════════════════════════════════════════════════════════

class CloudAgentOrchestrator:
    """
    Wrapper for integrating CloudAgentClient with master_orchestrator.py
    """
    
    def __init__(self, endpoint: str = CLOUD_AGENT_ENDPOINT):
        self.client = CloudAgentClient(endpoint)
        self.logger = logging.getLogger("CloudAgentOrchestrator")
    
    async def route_task_to_cloud(
        self,
        task_type: str,
        task_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Route a task from the master orchestrator to the cloud agent
        
        This method is designed to be called from master_orchestrator.execute_task()
        """
        self.logger.info(f"🌐 Routing task to cloud: {task_type}")
        
        # Check if cloud agent supports this task type
        capabilities = await self.client.get_capabilities()
        
        if task_type not in capabilities.capabilities:
            raise ValueError(
                f"Cloud agent does not support task type '{task_type}'. "
                f"Available: {', '.join(capabilities.capabilities)}"
            )
        
        # Delegate to cloud
        response = await self.client.delegate_task(task_type, task_data)
        
        if response.status == "failed":
            raise Exception(f"Cloud task failed: {response.error}")
        
        return {
            "task_id": response.task_id,
            "status": response.status,
            "result": response.result,
            "delegated_to": "cloud-agent",
            "timestamp": response.timestamp
        }

# ═══════════════════════════════════════════════════════════════════════════
# CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════

async def cmd_status():
    """Check cloud agent status"""
    client = CloudAgentClient()
    
    print("\n" + "="*70)
    print("☁️  NOIZYLAB CLOUD AGENT STATUS")
    print("="*70 + "\n")
    
    try:
        # Health check
        health = await client.health_check()
        print(f"🟢 Agent Status: {health.get('status', 'unknown').upper()}")
        print(f"📍 Endpoint: {CLOUD_AGENT_ENDPOINT}")
        print(f"🌍 Environment: {health.get('env', 'unknown')}")
        print(f"🤖 Agent: {health.get('agent', 'unknown')}")
        print(f"📦 Version: {health.get('version', 'unknown')}")
        
        # Capabilities
        print("\n" + "-"*70)
        capabilities = await client.get_capabilities()
        print(f"\n📋 Capabilities ({len(capabilities.capabilities)} available):")
        for cap in capabilities.capabilities:
            print(f"   • {cap}")
        
        print(f"\n⏰ Last Update: {capabilities.timestamp}")
        print("\n" + "="*70)
        print("✅ Cloud agent is operational\n")
        
    except Exception as e:
        print(f"❌ Cloud agent unreachable: {e}\n")
        sys.exit(1)

async def cmd_delegate(task_type: str, message: str = "Hello from CLI"):
    """Delegate a test task"""
    client = CloudAgentClient()
    
    print(f"\n🚀 Delegating {task_type} task to cloud agent...\n")
    
    task_data = {"message": message} if task_type == "echo" else {"prompt": message}
    
    try:
        response = await client.delegate_task(task_type, task_data)
        
        print(f"Task ID: {response.task_id}")
        print(f"Status: {response.status}")
        
        if response.result:
            print(f"Result: {json.dumps(response.result, indent=2)}")
        
        if response.error:
            print(f"Error: {response.error}")
        
        print(f"Timestamp: {response.timestamp}\n")
        
    except Exception as e:
        print(f"❌ Error: {e}\n")
        sys.exit(1)

async def cmd_interactive():
    """Interactive mode"""
    client = CloudAgentClient()
    
    print("\n" + "="*70)
    print("☁️  NOIZYLAB CLOUD AGENT - Interactive Mode")
    print("="*70)
    print("\nCommands:")
    print("  status         - Check agent status")
    print("  capabilities   - List capabilities")
    print("  echo <msg>     - Send echo task")
    print("  inference <p>  - Send inference task")
    print("  quit           - Exit")
    print("")
    
    while True:
        try:
            cmd = input("cloud> ").strip()
            
            if not cmd:
                continue
            
            if cmd == "quit" or cmd == "exit":
                print("👋 Goodbye!\n")
                break
            
            elif cmd == "status":
                health = await client.health_check()
                print(f"Status: {health.get('status')} | Env: {health.get('env')}")
            
            elif cmd == "capabilities":
                caps = await client.get_capabilities()
                print(f"Capabilities: {', '.join(caps.capabilities)}")
            
            elif cmd.startswith("echo "):
                msg = cmd[5:]
                response = await client.delegate_task("echo", {"message": msg})
                print(f"Result: {response.result}")
            
            elif cmd.startswith("inference "):
                prompt = cmd[10:]
                response = await client.delegate_task("inference", {"prompt": prompt, "model": "claude"})
                print(f"Result: {response.result}")
            
            else:
                print(f"Unknown command: {cmd}")
        
        except KeyboardInterrupt:
            print("\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"Error: {e}")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
    )
    
    if len(sys.argv) < 2:
        await cmd_interactive()
        return
    
    cmd = sys.argv[1]
    
    if cmd == "--status" or cmd == "status":
        await cmd_status()
    
    elif cmd == "--delegate" or cmd == "delegate":
        task_type = sys.argv[2] if len(sys.argv) > 2 else "echo"
        message = sys.argv[3] if len(sys.argv) > 3 else "Hello from CLI"
        await cmd_delegate(task_type, message)
    
    elif cmd == "--interactive" or cmd == "-i":
        await cmd_interactive()
    
    else:
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ☁️  NOIZYLAB CLOUD AGENT CLIENT                                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Usage:
  python3 cloud_agent_client.py                    # Interactive mode
  python3 cloud_agent_client.py --status           # Check status
  python3 cloud_agent_client.py --delegate <type> <msg>  # Delegate task
  python3 cloud_agent_client.py --interactive      # Interactive mode

Examples:
  python3 cloud_agent_client.py --status
  python3 cloud_agent_client.py --delegate echo "Hello Cloud"
  python3 cloud_agent_client.py --delegate inference "Analyze this"

Task Types:
  - echo           : Echo message back
  - inference      : AI inference task
  - code-analysis  : Analyze code
  - monitoring     : System monitoring
        """)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
