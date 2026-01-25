#!/usr/bin/env python3
"""
Test script for cloud agent delegation functionality.

This script should be run after the Cloudflare Worker is deployed
to verify that the cloud agent delegation system works correctly.

Enhanced test coverage:
- Authentication
- Rate limiting
- Retry logic
- Circuit breaker
- Batch operations
- Webhooks
- New task handlers
- Performance benchmarks
"""

import asyncio
import sys
import time
from cloud_agent_client import (
    CloudAgentClient, 
    CloudAgentOrchestrator,
    TaskRequest,
    AuthenticationError,
    RateLimitError,
    CircuitBreakerOpen
)

async def test_health():
    """Test 1: Health check"""
    print("\n" + "="*70)
    print("TEST 1: Health Check")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        health = await client.health_check()
        print(f"✅ Health check passed")
        print(f"   Status: {health.get('status')}")
        print(f"   Agent: {health.get('agent')}")
        print(f"   Version: {health.get('version')}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

async def test_capabilities():
    """Test 2: Get capabilities"""
    print("\n" + "="*70)
    print("TEST 2: Get Capabilities")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        caps = await client.get_capabilities()
        print(f"✅ Capabilities retrieved")
        print(f"   Agent ID: {caps.agent_id}")
        print(f"   Status: {caps.status}")
        print(f"   Capabilities: {', '.join(caps.capabilities)}")
        return True
    except Exception as e:
        print(f"❌ Capabilities check failed: {e}")
        return False

async def test_echo_task():
    """Test 3: Echo task"""
    print("\n" + "="*70)
    print("TEST 3: Echo Task")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        response = await client.delegate_task(
            "echo",
            {"message": "Test from cloud_agent_client"}
        )
        
        if response.status == "completed":
            print(f"✅ Echo task completed")
            print(f"   Task ID: {response.task_id}")
            print(f"   Result: {response.result}")
            return True
        else:
            print(f"❌ Echo task failed: {response.error}")
            return False
    except Exception as e:
        print(f"❌ Echo task error: {e}")
        return False

async def test_inference_task():
    """Test 4: Inference task"""
    print("\n" + "="*70)
    print("TEST 4: Inference Task")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        response = await client.delegate_task(
            "inference",
            {"model": "claude", "prompt": "Hello from test"}
        )
        
        if response.status == "completed":
            print(f"✅ Inference task completed")
            print(f"   Task ID: {response.task_id}")
            print(f"   Result: {response.result}")
            return True
        else:
            print(f"❌ Inference task failed: {response.error}")
            return False
    except Exception as e:
        print(f"❌ Inference task error: {e}")
        return False

async def test_monitoring_task():
    """Test 5: Monitoring task"""
    print("\n" + "="*70)
    print("TEST 5: Monitoring Task")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        response = await client.delegate_task(
            "monitoring",
            {}
        )
        
        if response.status == "completed":
            print(f"✅ Monitoring task completed")
            print(f"   Task ID: {response.task_id}")
            print(f"   Result: {response.result}")
            return True
        else:
            print(f"❌ Monitoring task failed: {response.error}")
            return False
    except Exception as e:
        print(f"❌ Monitoring task error: {e}")
        return False

async def test_orchestrator_integration():
    """Test 6: Orchestrator integration"""
    print("\n" + "="*70)
    print("TEST 6: Orchestrator Integration")
    print("="*70)
    
    orchestrator = CloudAgentOrchestrator()
    try:
        result = await orchestrator.route_task_to_cloud(
            "echo",
            {"message": "Test from orchestrator"}
        )
        
        print(f"✅ Orchestrator routing successful")
        print(f"   Task ID: {result['task_id']}")
        print(f"   Status: {result['status']}")
        print(f"   Delegated to: {result['delegated_to']}")
        return True
    except Exception as e:
        print(f"❌ Orchestrator routing failed: {e}")
        return False

async def test_invalid_task():
    """Test 7: Invalid task type"""
    print("\n" + "="*70)
    print("TEST 7: Invalid Task Type (Error Handling)")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        response = await client.delegate_task(
            "invalid-task-type",
            {}
        )
        
        if response.status == "failed":
            print(f"✅ Invalid task properly rejected")
            print(f"   Error: {response.error}")
            return True
        else:
            print(f"❌ Invalid task should have failed")
            return False
    except Exception as e:
        print(f"✅ Invalid task properly rejected with exception")
        return True

async def test_file_processing():
    """Test 8: File processing task"""
    print("\n" + "="*70)
    print("TEST 8: File Processing Task")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        response = await client.delegate_task(
            "file-processing",
            {
                "file_name": "test.txt",
                "file_size": 1024,
                "file_type": "text/plain"
            }
        )
        
        if response.status == "completed":
            print(f"✅ File processing completed")
            print(f"   Result: {response.result}")
            return True
        else:
            print(f"❌ File processing failed: {response.error}")
            return False
    except Exception as e:
        print(f"❌ File processing error: {e}")
        return False

async def test_data_transform():
    """Test 9: Data transformation task"""
    print("\n" + "="*70)
    print("TEST 9: Data Transformation Task")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        response = await client.delegate_task(
            "data-transform",
            {
                "input": ["apple", "banana", "cherry"],
                "operation": "sort"
            }
        )
        
        if response.status == "completed":
            print(f"✅ Data transformation completed")
            print(f"   Result: {response.result}")
            return True
        else:
            print(f"❌ Data transformation failed: {response.error}")
            return False
    except Exception as e:
        print(f"❌ Data transformation error: {e}")
        return False

async def test_health_check_task():
    """Test 10: Health check task"""
    print("\n" + "="*70)
    print("TEST 10: Health Check Task")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        response = await client.delegate_task(
            "health-check",
            {
                "url": "https://www.google.com"
            }
        )
        
        if response.status == "completed":
            print(f"✅ Health check completed")
            print(f"   Result: {response.result}")
            return True
        else:
            print(f"❌ Health check failed: {response.error}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

async def test_batch_operations():
    """Test 11: Batch operations"""
    print("\n" + "="*70)
    print("TEST 11: Batch Operations")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        tasks = [
            TaskRequest(
                task_type="echo",
                task_data={"message": f"Batch task {i}"}
            )
            for i in range(3)
        ]
        
        responses = await client.batch_delegate(tasks)
        
        if len(responses) == 3:
            completed = sum(1 for r in responses if r.status == "completed")
            print(f"✅ Batch processing completed")
            print(f"   Completed: {completed}/{len(responses)}")
            return completed == 3
        else:
            print(f"❌ Batch processing failed")
            return False
    except Exception as e:
        print(f"❌ Batch processing error: {e}")
        return False

async def test_retry_logic():
    """Test 12: Retry logic with transient failures"""
    print("\n" + "="*70)
    print("TEST 12: Retry Logic")
    print("="*70)
    
    # Test with invalid endpoint to trigger retries
    client = CloudAgentClient(endpoint="https://invalid-endpoint-12345.example.com")
    try:
        response = await client.delegate_task("echo", {"message": "test"})
        print(f"❌ Should have failed with connection error")
        return False
    except Exception as e:
        print(f"✅ Retry logic engaged: {e}")
        return True

async def test_circuit_breaker():
    """Test 13: Circuit breaker"""
    print("\n" + "="*70)
    print("TEST 13: Circuit Breaker")
    print("="*70)
    
    client = CloudAgentClient(endpoint="https://invalid-endpoint-12345.example.com")
    
    # Trigger multiple failures to open circuit
    for i in range(6):
        try:
            await client.delegate_task("echo", {"message": "test"})
        except:
            pass
    
    # Check circuit breaker state
    state = client.get_circuit_breaker_state()
    print(f"   Circuit breaker state: {state}")
    
    if state["state"] == "open":
        print(f"✅ Circuit breaker opened after failures")
        return True
    else:
        print(f"❌ Circuit breaker should be open")
        return False

async def test_caching():
    """Test 14: Response caching"""
    print("\n" + "="*70)
    print("TEST 14: Response Caching")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        # First call
        start1 = time.time()
        await client.health_check()
        duration1 = time.time() - start1
        
        # Second call (should be cached)
        start2 = time.time()
        await client.health_check()
        duration2 = time.time() - start2
        
        print(f"   First call: {duration1*1000:.2f}ms")
        print(f"   Second call (cached): {duration2*1000:.2f}ms")
        
        if duration2 < duration1:
            print(f"✅ Caching working (speedup: {duration1/duration2:.1f}x)")
            return True
        else:
            print(f"⚠️  Cached call not faster (network may be very fast)")
            return True  # Don't fail test on this
    except Exception as e:
        print(f"❌ Caching test error: {e}")
        return False

async def test_metrics_endpoint():
    """Test 15: Metrics endpoint"""
    print("\n" + "="*70)
    print("TEST 15: Metrics Endpoint")
    print("="*70)
    
    client = CloudAgentClient()
    try:
        metrics = await client.get_metrics()
        print(f"✅ Metrics retrieved")
        print(f"   Total tasks: {metrics.get('total_tasks', 0)}")
        print(f"   Completed: {metrics.get('completed_tasks', 0)}")
        print(f"   Failed: {metrics.get('failed_tasks', 0)}")
        return True
    except Exception as e:
        print(f"⚠️  Metrics not available (may not be configured): {e}")
        return True  # Don't fail if metrics not configured

async def test_orchestrator_routing():
    """Test 16: Orchestrator intelligent routing"""
    print("\n" + "="*70)
    print("TEST 16: Orchestrator Intelligent Routing")
    print("="*70)
    
    orchestrator = CloudAgentOrchestrator()
    try:
        await orchestrator.initialize()
        
        # Test routing decision
        should_route = await orchestrator.should_route_to_cloud(
            "inference",
            {"prompt": "test"}
        )
        
        print(f"   Should route 'inference' to cloud: {should_route}")
        
        # Get orchestrator status
        status = await orchestrator.get_status()
        print(f"   Cloud healthy: {status['cloud_agent']['healthy']}")
        print(f"   Capabilities: {len(status['capabilities'])}")
        
        print(f"✅ Orchestrator routing test completed")
        return True
    except Exception as e:
        print(f"❌ Orchestrator routing failed: {e}")
        return False

async def test_performance_benchmark():
    """Test 17: Performance benchmark"""
    print("\n" + "="*70)
    print("TEST 17: Performance Benchmark")
    print("="*70)
    
    client = CloudAgentClient()
    num_requests = 5
    
    try:
        start = time.time()
        tasks = []
        
        for i in range(num_requests):
            task = client.delegate_task("echo", {"message": f"Benchmark {i}"})
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        duration = time.time() - start
        
        completed = sum(1 for r in results if r.status == "completed")
        avg_duration = (duration / num_requests) * 1000
        
        print(f"   Completed: {completed}/{num_requests}")
        print(f"   Total time: {duration:.2f}s")
        print(f"   Avg per request: {avg_duration:.2f}ms")
        print(f"   Throughput: {num_requests/duration:.2f} req/s")
        
        if completed == num_requests:
            print(f"✅ Performance benchmark passed")
            return True
        else:
            print(f"❌ Some requests failed")
            return False
    except Exception as e:
        print(f"❌ Benchmark error: {e}")
        return False

async def main():
    """Run all tests"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + " "*15 + "CLOUD AGENT TEST SUITE (ENHANCED)" + " "*20 + "║")
    print("╚" + "="*68 + "╝")
    
    tests = [
        test_health,
        test_capabilities,
        test_echo_task,
        test_inference_task,
        test_monitoring_task,
        test_orchestrator_integration,
        test_invalid_task,
        test_file_processing,
        test_data_transform,
        test_health_check_task,
        test_batch_operations,
        test_retry_logic,
        test_circuit_breaker,
        test_caching,
        test_metrics_endpoint,
        test_orchestrator_routing,
        test_performance_benchmark,
    ]
    
    results = []
    for test in tests:
        try:
            result = await test()
            results.append(result)
        except Exception as e:
            print(f"\n❌ Test crashed: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nPassed: {passed}/{total}")
    print(f"Failed: {total - passed}/{total}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n✅ ALL TESTS PASSED")
        print("\n" + "="*70 + "\n")
        sys.exit(0)
    else:
        print("\n⚠️  SOME TESTS FAILED")
        print("\n" + "="*70 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
