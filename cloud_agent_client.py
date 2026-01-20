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
import time
import gzip
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from enum import Enum
import urllib.request
import urllib.error
import urllib.parse
from functools import wraps

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

import os

CLOUD_AGENT_ENDPOINT = os.getenv(
    "CLOUD_AGENT_ENDPOINT", 
    "https://noizylab.rsplowman.workers.dev"
)
DEFAULT_TIMEOUT = int(os.getenv("CLOUD_AGENT_TIMEOUT", "30"))
API_KEY = os.getenv("CLOUD_AGENT_API_KEY", "")

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM EXCEPTIONS
# ═══════════════════════════════════════════════════════════════════════════

class CloudAgentError(Exception):
    """Base exception for cloud agent errors"""
    pass

class AuthenticationError(CloudAgentError):
    """Authentication failed"""
    pass

class RateLimitError(CloudAgentError):
    """Rate limit exceeded"""
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after} seconds.")

class CircuitBreakerOpen(CloudAgentError):
    """Circuit breaker is open"""
    pass

# ═══════════════════════════════════════════════════════════════════════════
# CIRCUIT BREAKER
# ═══════════════════════════════════════════════════════════════════════════

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    """Circuit breaker pattern implementation"""
    
    def __init__(self, failure_threshold: int = 5, timeout: int = 30):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time: Optional[float] = None
        self.state = CircuitState.CLOSED
        self.logger = logging.getLogger("CircuitBreaker")
    
    def call_succeeded(self):
        """Record successful call"""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            self.logger.info("🔄 Circuit breaker CLOSED")
    
    def call_failed(self):
        """Record failed call"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            self.logger.warning(f"⚠️ Circuit breaker OPEN (failures: {self.failure_count})")
    
    def can_attempt(self) -> bool:
        """Check if request can be attempted"""
        if self.state == CircuitState.CLOSED:
            return True
        
        if self.state == CircuitState.OPEN:
            if self.last_failure_time and time.time() - self.last_failure_time >= self.timeout:
                self.state = CircuitState.HALF_OPEN
                self.logger.info("🔄 Circuit breaker HALF_OPEN")
                return True
            return False
        
        # HALF_OPEN state - allow one attempt
        return True
    
    def get_state(self) -> Dict[str, Any]:
        """Get current circuit breaker state"""
        return {
            "state": self.state.value,
            "failure_count": self.failure_count,
            "last_failure_time": self.last_failure_time
        }

# ═══════════════════════════════════════════════════════════════════════════
# RESPONSE CACHE
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class CacheEntry:
    """Cache entry with expiration"""
    data: Any
    expires_at: float

class ResponseCache:
    """Simple in-memory cache with TTL"""
    
    def __init__(self):
        self.cache: Dict[str, CacheEntry] = {}
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired"""
        if key in self.cache:
            entry = self.cache[key]
            if time.time() < entry.expires_at:
                return entry.data
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value: Any, ttl_seconds: int):
        """Set cache value with TTL"""
        self.cache[key] = CacheEntry(
            data=value,
            expires_at=time.time() + ttl_seconds
        )
    
    def clear(self):
        """Clear all cache entries"""
        self.cache.clear()

# ═══════════════════════════════════════════════════════════════════════════
# RETRY DECORATOR
# ═══════════════════════════════════════════════════════════════════════════

def retry_on_failure(max_retries: int = 3, backoff_base: float = 1.0):
    """Decorator for retrying failed operations with exponential backoff"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except (urllib.error.URLError, ConnectionError, TimeoutError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        delay = backoff_base * (2 ** attempt)
                        logging.getLogger("RetryDecorator").warning(
                            f"Attempt {attempt + 1} failed, retrying in {delay}s: {e}"
                        )
                        await asyncio.sleep(delay)
                    else:
                        logging.getLogger("RetryDecorator").error(
                            f"All {max_retries} attempts failed"
                        )
            raise last_exception
        return wrapper
    return decorator

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
    
    Features:
    - Retry logic with exponential backoff
    - Circuit breaker pattern
    - Response caching
    - Request compression
    - API key authentication
    - Rate limit handling
    
    Usage:
        client = CloudAgentClient(api_key="your-key")
        response = await client.delegate_task("echo", {"message": "Hello"})
        print(response.result)
    """
    
    def __init__(
        self, 
        endpoint: str = CLOUD_AGENT_ENDPOINT, 
        timeout: int = DEFAULT_TIMEOUT,
        api_key: str = API_KEY
    ):
        self.endpoint = endpoint.rstrip('/')
        self.timeout = timeout
        self.api_key = api_key
        self.logger = logging.getLogger("CloudAgentClient")
        self._loop = None
        self._executor = None
        
        # Advanced features
        self.circuit_breaker = CircuitBreaker()
        self.cache = ResponseCache()
    
    def _get_executor(self):
        """Get or create thread pool executor for sync operations"""
        if self._executor is None:
            import concurrent.futures
            self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        return self._executor
    
    def _compress_data(self, data: bytes) -> bytes:
        """Compress data using gzip"""
        return gzip.compress(data)
    
    def _decompress_data(self, data: bytes) -> bytes:
        """Decompress gzip data"""
        return gzip.decompress(data)
    
    @retry_on_failure(max_retries=3, backoff_base=1.0)
    async def _make_request_async(
        self,
        path: str,
        method: str = "GET",
        data: Optional[Dict] = None
    ) -> Dict:
        """Make async HTTP request to cloud agent with retry logic"""
        # Check circuit breaker
        if not self.circuit_breaker.can_attempt():
            raise CircuitBreakerOpen("Circuit breaker is open, requests blocked")
        
        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                self._get_executor(),
                self._make_request_sync,
                path,
                method,
                data
            )
            self.circuit_breaker.call_succeeded()
            return result
        except Exception as e:
            self.circuit_breaker.call_failed()
            raise
    
    def _make_request_sync(
        self,
        path: str,
        method: str = "GET",
        data: Optional[Dict] = None
    ) -> Dict:
        """Make synchronous HTTP request to cloud agent"""
        url = f"{self.endpoint}{path}"
        headers = {"Content-Type": "application/json"}
        
        # Add API key header if configured
        if self.api_key:
            headers["X-API-Key"] = self.api_key
        
        try:
            if method == "POST" and data:
                req_data = json.dumps(data).encode('utf-8')
                
                # Compress large payloads
                if len(req_data) > 1024:
                    req_data = self._compress_data(req_data)
                    headers["Content-Encoding"] = "gzip"
                
                request = urllib.request.Request(url, data=req_data, headers=headers, method=method)
            else:
                request = urllib.request.Request(url, headers=headers, method=method)
            
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                response_data = response.read()
                
                # Check if response is compressed
                if response.headers.get("Content-Encoding") == "gzip":
                    response_data = self._decompress_data(response_data)
                
                return json.loads(response_data.decode('utf-8'))
        
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            
            # Handle rate limiting
            if e.code == 429:
                retry_after = int(e.headers.get("Retry-After", 60))
                raise RateLimitError(retry_after)
            
            # Handle authentication errors
            if e.code == 401:
                raise AuthenticationError("API key authentication failed")
            
            try:
                error_data = json.loads(error_body)
                if 'error' in error_data:
                    raise CloudAgentError(f"HTTP {e.code}: {error_data['error']}")
                return error_data
            except json.JSONDecodeError:
                raise CloudAgentError(f"HTTP {e.code}: {error_body}")
        
        except urllib.error.URLError as e:
            raise CloudAgentError(f"Connection error: {e.reason}")
        
        except Exception as e:
            raise CloudAgentError(f"Request failed: {str(e)}")
    
    async def health_check(self) -> Dict[str, Any]:
        """Check cloud agent health (cached for 1 minute)"""
        cache_key = "health_check"
        cached = self.cache.get(cache_key)
        if cached:
            self.logger.debug("🔄 Using cached health check")
            return cached
        
        self.logger.info(f"🔍 Checking cloud agent health at {self.endpoint}...")
        result = await self._make_request_async("/health")
        self.cache.set(cache_key, result, ttl_seconds=60)
        return result
    
    async def get_capabilities(self) -> AgentCapabilities:
        """Get cloud agent capabilities (cached for 5 minutes)"""
        cache_key = "capabilities"
        cached = self.cache.get(cache_key)
        if cached:
            self.logger.debug("🔄 Using cached capabilities")
            return AgentCapabilities.from_dict(cached)
        
        self.logger.info("📋 Fetching cloud agent capabilities...")
        data = await self._make_request_async("/api/capabilities")
        self.cache.set(cache_key, data, ttl_seconds=300)
        return AgentCapabilities.from_dict(data)
    
    async def get_metrics(self) -> Dict[str, Any]:
        """Get cloud agent metrics"""
        self.logger.info("📊 Fetching cloud agent metrics...")
        return await self._make_request_async("/api/metrics")
    
    async def delegate_task(
        self,
        task_type: str,
        task_data: Dict[str, Any],
        task_id: Optional[str] = None,
        priority: str = "normal",
        webhook_url: Optional[str] = None
    ) -> TaskResponse:
        """
        Delegate a task to the cloud agent
        
        Args:
            task_type: Type of task (e.g., "echo", "inference", "code-analysis")
            task_data: Task-specific data
            task_id: Optional task ID (generated if not provided)
            priority: Task priority ("low", "normal", "high")
            webhook_url: Optional webhook URL for async notification
        
        Returns:
            TaskResponse with task result or error
        """
        request = TaskRequest(
            task_type=task_type,
            task_data=task_data,
            task_id=task_id,
            priority=priority
        )
        
        request_dict = request.to_dict()
        if webhook_url:
            request_dict["webhook_url"] = webhook_url
        
        self.logger.info(f"🚀 Delegating task: {task_type} (ID: {request.task_id or 'auto'})")
        
        try:
            data = await self._make_request_async("/api/delegate", method="POST", data=request_dict)
            response = TaskResponse.from_dict(data)
            
            if response.status == "completed":
                self.logger.info(f"✅ Task completed: {response.task_id}")
            elif response.status == "failed":
                self.logger.error(f"❌ Task failed: {response.error}")
            else:
                self.logger.info(f"⏳ Task status: {response.status}")
            
            return response
        
        except RateLimitError as e:
            self.logger.warning(f"⚠️ Rate limit exceeded. Retry after {e.retry_after}s")
            return TaskResponse(
                task_id=request.task_id or "error",
                status="failed",
                error=str(e)
            )
        
        except CircuitBreakerOpen as e:
            self.logger.error(f"⚠️ Circuit breaker open: {e}")
            return TaskResponse(
                task_id=request.task_id or "error",
                status="failed",
                error=str(e)
            )
        
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
        """Delegate multiple tasks using batch endpoint"""
        self.logger.info(f"🚀 Delegating {len(tasks)} tasks in batch...")
        
        # Use new batch endpoint
        try:
            batch_data = {
                "tasks": [t.to_dict() for t in tasks]
            }
            
            result = await self._make_request_async("/api/batch", method="POST", data=batch_data)
            
            if "results" in result:
                responses = [TaskResponse.from_dict(r) for r in result["results"]]
                self.logger.info(f"✅ Batch completed: {len(responses)} tasks")
                return responses
            else:
                raise CloudAgentError("Invalid batch response format")
        
        except Exception as e:
            self.logger.error(f"❌ Batch delegation failed: {e}")
            # Fallback to sequential processing
            self.logger.info("🔄 Falling back to sequential processing...")
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
    
    def get_circuit_breaker_state(self) -> Dict[str, Any]:
        """Get current circuit breaker state"""
        return self.circuit_breaker.get_state()
    
    def reset_circuit_breaker(self):
        """Manually reset circuit breaker"""
        self.circuit_breaker.failure_count = 0
        self.circuit_breaker.state = CircuitState.CLOSED
        self.logger.info("🔄 Circuit breaker manually reset")
    
    def clear_cache(self):
        """Clear response cache"""
        self.cache.clear()
        self.logger.info("🗑️ Cache cleared")

# ═══════════════════════════════════════════════════════════════════════════
# ORCHESTRATOR INTEGRATION
# ═══════════════════════════════════════════════════════════════════════════

class CloudAgentOrchestrator:
    """
    Wrapper for integrating CloudAgentClient with master_orchestrator.py
    
    Features:
    - Intelligent task routing
    - Fallback to local execution
    - Task priority queue
    - Load balancing
    """
    
    def __init__(self, endpoint: str = CLOUD_AGENT_ENDPOINT, api_key: str = API_KEY):
        self.client = CloudAgentClient(endpoint, api_key=api_key)
        self.logger = logging.getLogger("CloudAgentOrchestrator")
        self.task_queue: List[tuple] = []  # (priority, task_data)
        
        # Task routing configuration
        self.cloud_task_types = set()
        self.local_fallback_enabled = True
    
    async def initialize(self):
        """Initialize orchestrator and fetch capabilities"""
        try:
            caps = await self.client.get_capabilities()
            self.cloud_task_types = set(caps.capabilities)
            self.logger.info(f"✅ Orchestrator initialized with {len(self.cloud_task_types)} cloud capabilities")
        except Exception as e:
            self.logger.warning(f"⚠️ Could not fetch cloud capabilities: {e}")
            self.local_fallback_enabled = True
    
    async def is_cloud_healthy(self) -> bool:
        """Check if cloud agent is healthy"""
        try:
            health = await self.client.health_check()
            return health.get("status") == "ok"
        except Exception:
            return False
    
    async def route_task_to_cloud(
        self,
        task_type: str,
        task_data: Dict[str, Any],
        priority: str = "normal"
    ) -> Dict[str, Any]:
        """
        Route a task from the master orchestrator to the cloud agent
        
        This method is designed to be called from master_orchestrator.execute_task()
        """
        self.logger.info(f"🌐 Routing task to cloud: {task_type}")
        
        # Check if cloud agent is healthy
        if not await self.is_cloud_healthy():
            if self.local_fallback_enabled:
                self.logger.warning("⚠️ Cloud agent unhealthy, falling back to local execution")
                raise CloudAgentError("Cloud agent unavailable, use local fallback")
            else:
                raise CloudAgentError("Cloud agent unavailable")
        
        # Check if cloud agent supports this task type
        if task_type not in self.cloud_task_types:
            if self.local_fallback_enabled:
                self.logger.warning(f"⚠️ Cloud agent does not support '{task_type}', using local fallback")
                raise CloudAgentError(f"Task type '{task_type}' not supported by cloud agent")
            else:
                raise ValueError(
                    f"Cloud agent does not support task type '{task_type}'. "
                    f"Available: {', '.join(self.cloud_task_types)}"
                )
        
        # Delegate to cloud
        response = await self.client.delegate_task(task_type, task_data, priority=priority)
        
        if response.status == "failed":
            raise CloudAgentError(f"Cloud task failed: {response.error}")
        
        return {
            "task_id": response.task_id,
            "status": response.status,
            "result": response.result,
            "delegated_to": "cloud-agent",
            "timestamp": response.timestamp
        }
    
    async def should_route_to_cloud(self, task_type: str, task_data: Dict[str, Any]) -> bool:
        """
        Decide if task should be routed to cloud based on task properties
        
        Routes to cloud if:
        - Task is computationally expensive
        - Cloud agent is healthy
        - Task type is supported
        """
        # Check if cloud supports this task
        if task_type not in self.cloud_task_types:
            return False
        
        # Check cloud health
        if not await self.is_cloud_healthy():
            return False
        
        # Route computationally expensive tasks to cloud
        expensive_tasks = {"inference", "code-analysis", "data-transform", "file-processing"}
        if task_type in expensive_tasks:
            return True
        
        # Route large payloads to cloud
        if isinstance(task_data, dict):
            data_size = len(json.dumps(task_data))
            if data_size > 10000:  # 10KB threshold
                return True
        
        return False
    
    async def execute_with_priority(
        self,
        task_type: str,
        task_data: Dict[str, Any],
        priority: int = 0
    ) -> Dict[str, Any]:
        """
        Execute task with priority
        
        Higher priority tasks execute first
        Priority: 0 (normal), 1 (high), -1 (low)
        """
        self.task_queue.append((priority, task_type, task_data))
        self.task_queue.sort(key=lambda x: -x[0])  # Sort by priority descending
        
        # Execute highest priority task
        _, t_type, t_data = self.task_queue.pop(0)
        
        return await self.route_task_to_cloud(
            t_type,
            t_data,
            priority="high" if priority > 0 else "normal"
        )
    
    async def get_status(self) -> Dict[str, Any]:
        """Get orchestrator status"""
        try:
            health = await self.client.health_check()
            metrics = await self.client.get_metrics()
            circuit_state = self.client.get_circuit_breaker_state()
            
            return {
                "cloud_agent": {
                    "healthy": health.get("status") == "ok",
                    "version": health.get("version"),
                    "endpoint": self.client.endpoint
                },
                "circuit_breaker": circuit_state,
                "metrics": metrics,
                "capabilities": list(self.cloud_task_types),
                "queue_size": len(self.task_queue),
                "local_fallback_enabled": self.local_fallback_enabled
            }
        except Exception as e:
            return {
                "cloud_agent": {
                    "healthy": False,
                    "error": str(e)
                },
                "circuit_breaker": self.client.get_circuit_breaker_state(),
                "queue_size": len(self.task_queue),
                "local_fallback_enabled": self.local_fallback_enabled
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
