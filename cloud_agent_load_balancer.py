#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ⚖️  NOIZYLAB CLOUD AGENT LOAD BALANCER                                 ║
║                                                                           ║
║   Enterprise-grade load balancer with multi-region support,             ║
║   health-based routing, and automatic failover                          ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import json
import logging
import time
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import urllib.request
import urllib.error

# ═══════════════════════════════════════════════════════════════════════════
# DATA MODELS
# ═══════════════════════════════════════════════════════════════════════════

class LoadBalancingAlgorithm(Enum):
    """Load balancing algorithms"""
    ROUND_ROBIN = "round_robin"
    LEAST_CONNECTIONS = "least_connections"
    WEIGHTED = "weighted"
    LATENCY_BASED = "latency_based"
    GEOGRAPHIC = "geographic"

class EndpointHealth(Enum):
    """Endpoint health states"""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"

@dataclass
class Endpoint:
    """Load balancer endpoint configuration"""
    url: str
    region: str = "us-east"
    weight: int = 1
    max_connections: int = 100
    priority: int = 1
    api_key: Optional[str] = None
    
    # Runtime state
    health: EndpointHealth = EndpointHealth.UNKNOWN
    current_connections: int = 0
    last_health_check: float = 0
    avg_latency_ms: float = 0
    total_requests: int = 0
    failed_requests: int = 0
    consecutive_failures: int = 0

@dataclass
class LoadBalancerStats:
    """Load balancer statistics"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_latency_ms: float = 0
    endpoint_stats: Dict[str, Dict[str, Any]] = field(default_factory=dict)

# ═══════════════════════════════════════════════════════════════════════════
# LOAD BALANCER
# ═══════════════════════════════════════════════════════════════════════════

class CloudAgentLoadBalancer:
    """
    Intelligent load balancer for distributing tasks across multiple
    cloud agent endpoints with health checks and automatic failover.
    """
    
    def __init__(
        self,
        endpoints: List[Endpoint],
        algorithm: LoadBalancingAlgorithm = LoadBalancingAlgorithm.LEAST_CONNECTIONS,
        health_check_interval: int = 30,
        failure_threshold: int = 3,
        recovery_threshold: int = 2
    ):
        """
        Initialize load balancer.
        
        Args:
            endpoints: List of backend endpoints
            algorithm: Load balancing algorithm to use
            health_check_interval: Seconds between health checks
            failure_threshold: Consecutive failures before marking unhealthy
            recovery_threshold: Consecutive successes before marking healthy
        """
        self.endpoints = endpoints
        self.algorithm = algorithm
        self.health_check_interval = health_check_interval
        self.failure_threshold = failure_threshold
        self.recovery_threshold = recovery_threshold
        
        self.current_index = 0
        self.stats = LoadBalancerStats()
        self.logger = logging.getLogger("CloudAgentLoadBalancer")
        
        # Start health check background task
        self._health_check_task: Optional[asyncio.Task] = None
        
        self.logger.info(f"⚖️ Load balancer initialized with {len(endpoints)} endpoints")
        self.logger.info(f"   Algorithm: {algorithm.value}")
    
    async def start(self):
        """Start background health checking"""
        if self._health_check_task is None:
            self._health_check_task = asyncio.create_task(self._health_check_loop())
            self.logger.info("🏥 Health check loop started")
    
    async def stop(self):
        """Stop background health checking"""
        if self._health_check_task:
            self._health_check_task.cancel()
            try:
                await self._health_check_task
            except asyncio.CancelledError:
                pass
            self._health_check_task = None
            self.logger.info("🛑 Health check loop stopped")
    
    def select_endpoint(
        self,
        client_region: Optional[str] = None,
        task_priority: str = "normal"
    ) -> Optional[Endpoint]:
        """
        Select best endpoint based on configured algorithm.
        
        Args:
            client_region: Client's geographic region for geographic routing
            task_priority: Task priority (may affect selection)
        
        Returns:
            Selected endpoint or None if no healthy endpoints
        """
        # Filter to healthy or degraded endpoints
        available = [
            ep for ep in self.endpoints
            if ep.health in (EndpointHealth.HEALTHY, EndpointHealth.DEGRADED)
            and ep.current_connections < ep.max_connections
        ]
        
        if not available:
            self.logger.warning("⚠️ No healthy endpoints available!")
            return None
        
        if self.algorithm == LoadBalancingAlgorithm.ROUND_ROBIN:
            return self._select_round_robin(available)
        
        elif self.algorithm == LoadBalancingAlgorithm.LEAST_CONNECTIONS:
            return self._select_least_connections(available)
        
        elif self.algorithm == LoadBalancingAlgorithm.WEIGHTED:
            return self._select_weighted(available)
        
        elif self.algorithm == LoadBalancingAlgorithm.LATENCY_BASED:
            return self._select_latency_based(available)
        
        elif self.algorithm == LoadBalancingAlgorithm.GEOGRAPHIC:
            return self._select_geographic(available, client_region)
        
        return available[0]
    
    def _select_round_robin(self, endpoints: List[Endpoint]) -> Endpoint:
        """Round-robin selection"""
        if not endpoints:
            return None
        
        endpoint = endpoints[self.current_index % len(endpoints)]
        self.current_index += 1
        return endpoint
    
    def _select_least_connections(self, endpoints: List[Endpoint]) -> Endpoint:
        """Select endpoint with fewest active connections"""
        return min(endpoints, key=lambda ep: ep.current_connections)
    
    def _select_weighted(self, endpoints: List[Endpoint]) -> Endpoint:
        """Weighted random selection"""
        import random
        
        # Filter by health - prefer HEALTHY over DEGRADED
        healthy = [ep for ep in endpoints if ep.health == EndpointHealth.HEALTHY]
        pool = healthy if healthy else endpoints
        
        total_weight = sum(ep.weight for ep in pool)
        if total_weight == 0:
            return pool[0]
        
        r = random.uniform(0, total_weight)
        cumulative = 0
        
        for ep in pool:
            cumulative += ep.weight
            if r <= cumulative:
                return ep
        
        return pool[-1]
    
    def _select_latency_based(self, endpoints: List[Endpoint]) -> Endpoint:
        """Select endpoint with lowest average latency"""
        # Only consider endpoints that have been tested
        tested = [ep for ep in endpoints if ep.avg_latency_ms > 0]
        if not tested:
            return endpoints[0]
        
        return min(tested, key=lambda ep: ep.avg_latency_ms)
    
    def _select_geographic(
        self,
        endpoints: List[Endpoint],
        client_region: Optional[str]
    ) -> Endpoint:
        """Select endpoint closest to client region"""
        if client_region:
            # Try to find endpoint in same region
            same_region = [ep for ep in endpoints if ep.region == client_region]
            if same_region:
                return self._select_least_connections(same_region)
        
        # Fallback to least connections
        return self._select_least_connections(endpoints)
    
    async def execute_task(
        self,
        task_type: str,
        task_data: Dict[str, Any],
        client_region: Optional[str] = None,
        priority: str = "normal",
        timeout: int = 30
    ) -> Dict[str, Any]:
        """
        Execute task on selected endpoint with automatic failover.
        
        Args:
            task_type: Type of task to execute
            task_data: Task payload data
            client_region: Client's region for geographic routing
            priority: Task priority
            timeout: Request timeout in seconds
        
        Returns:
            Task result from endpoint
        
        Raises:
            Exception: If all endpoints fail
        """
        attempts = 0
        max_attempts = min(3, len(self.endpoints))
        last_error = None
        
        while attempts < max_attempts:
            endpoint = self.select_endpoint(client_region, priority)
            
            if endpoint is None:
                raise Exception("No healthy endpoints available")
            
            try:
                endpoint.current_connections += 1
                start_time = time.time()
                
                result = await self._send_request(
                    endpoint,
                    task_type,
                    task_data,
                    timeout
                )
                
                latency = (time.time() - start_time) * 1000
                
                # Update endpoint stats
                endpoint.total_requests += 1
                endpoint.avg_latency_ms = (
                    endpoint.avg_latency_ms * (endpoint.total_requests - 1) + latency
                ) / endpoint.total_requests
                endpoint.consecutive_failures = 0
                
                # Update global stats
                self.stats.total_requests += 1
                self.stats.successful_requests += 1
                self.stats.total_latency_ms += latency
                
                return result
                
            except Exception as e:
                last_error = e
                endpoint.failed_requests += 1
                endpoint.consecutive_failures += 1
                
                self.logger.warning(
                    f"⚠️ Request to {endpoint.url} failed: {e}"
                )
                
                # Mark as unhealthy if threshold reached
                if endpoint.consecutive_failures >= self.failure_threshold:
                    endpoint.health = EndpointHealth.UNHEALTHY
                    self.logger.error(
                        f"❌ Endpoint {endpoint.url} marked UNHEALTHY "
                        f"({endpoint.consecutive_failures} consecutive failures)"
                    )
                
                self.stats.failed_requests += 1
                attempts += 1
                
            finally:
                endpoint.current_connections = max(0, endpoint.current_connections - 1)
        
        raise Exception(
            f"All {max_attempts} attempts failed. Last error: {last_error}"
        )
    
    async def _send_request(
        self,
        endpoint: Endpoint,
        task_type: str,
        task_data: Dict[str, Any],
        timeout: int
    ) -> Dict[str, Any]:
        """Send request to specific endpoint"""
        url = f"{endpoint.url}/api/delegate"
        
        headers = {
            "Content-Type": "application/json"
        }
        
        if endpoint.api_key:
            headers["X-API-Key"] = endpoint.api_key
        
        payload = json.dumps({
            "task_type": task_type,
            "task_data": task_data
        }).encode()
        
        request = urllib.request.Request(
            url,
            data=payload,
            headers=headers,
            method="POST"
        )
        
        try:
            response = urllib.request.urlopen(request, timeout=timeout)
            data = json.loads(response.read().decode())
            
            if data.get("status") == "failed":
                raise Exception(data.get("error", "Task failed"))
            
            return data
            
        except urllib.error.HTTPError as e:
            error_data = e.read().decode() if e.code else "Unknown error"
            raise Exception(f"HTTP {e.code}: {error_data}")
        
        except urllib.error.URLError as e:
            raise Exception(f"Network error: {e.reason}")
    
    async def _health_check_loop(self):
        """Background loop for periodic health checks"""
        while True:
            try:
                await asyncio.sleep(self.health_check_interval)
                await self._check_all_endpoints()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Health check error: {e}")
    
    async def _check_all_endpoints(self):
        """Check health of all endpoints"""
        tasks = [self._check_endpoint_health(ep) for ep in self.endpoints]
        await asyncio.gather(*tasks, return_exceptions=True)
    
    async def _check_endpoint_health(self, endpoint: Endpoint):
        """Check health of single endpoint"""
        url = f"{endpoint.url}/health"
        
        headers = {}
        if endpoint.api_key:
            headers["X-API-Key"] = endpoint.api_key
        
        try:
            start_time = time.time()
            
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request, timeout=5)
            
            latency = (time.time() - start_time) * 1000
            data = json.loads(response.read().decode())
            
            endpoint.last_health_check = time.time()
            
            # Update health status
            if response.status == 200 and data.get("status") == "healthy":
                if endpoint.health == EndpointHealth.UNHEALTHY:
                    # Recovering - need consecutive successes
                    endpoint.consecutive_failures = 0
                    if endpoint.total_requests - endpoint.failed_requests >= self.recovery_threshold:
                        endpoint.health = EndpointHealth.HEALTHY
                        self.logger.info(f"✅ Endpoint {endpoint.url} recovered to HEALTHY")
                else:
                    endpoint.health = EndpointHealth.HEALTHY
                
                # Update latency with health check result
                if endpoint.avg_latency_ms == 0:
                    endpoint.avg_latency_ms = latency
                else:
                    endpoint.avg_latency_ms = (endpoint.avg_latency_ms * 0.9 + latency * 0.1)
            else:
                endpoint.health = EndpointHealth.DEGRADED
                
        except Exception as e:
            endpoint.consecutive_failures += 1
            
            if endpoint.consecutive_failures >= self.failure_threshold:
                if endpoint.health != EndpointHealth.UNHEALTHY:
                    endpoint.health = EndpointHealth.UNHEALTHY
                    self.logger.error(
                        f"❌ Endpoint {endpoint.url} marked UNHEALTHY: {e}"
                    )
            else:
                endpoint.health = EndpointHealth.DEGRADED
    
    def get_stats(self) -> Dict[str, Any]:
        """Get load balancer statistics"""
        healthy = sum(1 for ep in self.endpoints if ep.health == EndpointHealth.HEALTHY)
        degraded = sum(1 for ep in self.endpoints if ep.health == EndpointHealth.DEGRADED)
        unhealthy = sum(1 for ep in self.endpoints if ep.health == EndpointHealth.UNHEALTHY)
        
        avg_latency = (
            self.stats.total_latency_ms / self.stats.successful_requests
            if self.stats.successful_requests > 0
            else 0
        )
        
        endpoint_details = []
        for ep in self.endpoints:
            endpoint_details.append({
                "url": ep.url,
                "region": ep.region,
                "health": ep.health.value,
                "weight": ep.weight,
                "current_connections": ep.current_connections,
                "total_requests": ep.total_requests,
                "failed_requests": ep.failed_requests,
                "success_rate": (
                    (ep.total_requests - ep.failed_requests) / ep.total_requests * 100
                    if ep.total_requests > 0 else 0
                ),
                "avg_latency_ms": round(ep.avg_latency_ms, 2),
                "last_health_check": ep.last_health_check
            })
        
        return {
            "algorithm": self.algorithm.value,
            "total_endpoints": len(self.endpoints),
            "healthy_endpoints": healthy,
            "degraded_endpoints": degraded,
            "unhealthy_endpoints": unhealthy,
            "total_requests": self.stats.total_requests,
            "successful_requests": self.stats.successful_requests,
            "failed_requests": self.stats.failed_requests,
            "success_rate": (
                self.stats.successful_requests / self.stats.total_requests * 100
                if self.stats.total_requests > 0 else 0
            ),
            "avg_latency_ms": round(avg_latency, 2),
            "endpoints": endpoint_details
        }
    
    def print_status(self):
        """Print load balancer status to console"""
        stats = self.get_stats()
        
        print("\n" + "="*70)
        print("⚖️  LOAD BALANCER STATUS")
        print("="*70)
        print(f"Algorithm: {stats['algorithm']}")
        print(f"Total Endpoints: {stats['total_endpoints']}")
        print(f"  ✅ Healthy: {stats['healthy_endpoints']}")
        print(f"  ⚠️  Degraded: {stats['degraded_endpoints']}")
        print(f"  ❌ Unhealthy: {stats['unhealthy_endpoints']}")
        print(f"\nRequests: {stats['total_requests']}")
        print(f"  Success: {stats['successful_requests']} ({stats['success_rate']:.1f}%)")
        print(f"  Failed: {stats['failed_requests']}")
        print(f"  Avg Latency: {stats['avg_latency_ms']:.2f}ms")
        
        print(f"\nEndpoint Details:")
        for ep in stats['endpoints']:
            health_icon = {
                "healthy": "✅",
                "degraded": "⚠️",
                "unhealthy": "❌",
                "unknown": "❓"
            }.get(ep['health'], "❓")
            
            print(f"  {health_icon} {ep['url']}")
            print(f"     Region: {ep['region']} | Weight: {ep['weight']}")
            print(f"     Requests: {ep['total_requests']} | Success: {ep['success_rate']:.1f}%")
            print(f"     Latency: {ep['avg_latency_ms']:.2f}ms | Connections: {ep['current_connections']}")


# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE USAGE
# ═══════════════════════════════════════════════════════════════════════════

async def main():
    """Demo load balancer usage"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    # Configure endpoints
    endpoints = [
        Endpoint(
            url="https://noizylab.rsplowman.workers.dev",
            region="us-east",
            weight=3,
            api_key="your-api-key-1"
        ),
        Endpoint(
            url="https://noizylab-eu.workers.dev",
            region="eu-west",
            weight=2,
            api_key="your-api-key-2"
        ),
        Endpoint(
            url="https://noizylab-asia.workers.dev",
            region="asia-east",
            weight=1,
            api_key="your-api-key-3"
        )
    ]
    
    # Create load balancer
    lb = CloudAgentLoadBalancer(
        endpoints=endpoints,
        algorithm=LoadBalancingAlgorithm.LEAST_CONNECTIONS,
        health_check_interval=30
    )
    
    await lb.start()
    
    # Simulate some requests
    print("🚀 Executing tasks through load balancer...")
    
    for i in range(10):
        try:
            result = await lb.execute_task(
                task_type="echo",
                task_data={"message": f"Hello from request {i}"},
                client_region="us-east",
                priority="normal"
            )
            print(f"  ✅ Request {i}: {result.get('status')}")
        except Exception as e:
            print(f"  ❌ Request {i} failed: {e}")
        
        await asyncio.sleep(0.5)
    
    # Print status
    lb.print_status()
    
    await lb.stop()


if __name__ == "__main__":
    asyncio.run(main())
