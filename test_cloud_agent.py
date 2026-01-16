#!/usr/bin/env python3
"""
Test script for cloud agent delegation functionality.

This script should be run after the Cloudflare Worker is deployed
to verify that the cloud agent delegation system works correctly.
"""

import asyncio
import sys
from cloud_agent_client import CloudAgentClient, CloudAgentOrchestrator

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

async def main():
    """Run all tests"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + " "*20 + "CLOUD AGENT TEST SUITE" + " "*26 + "║")
    print("╚" + "="*68 + "╝")
    
    tests = [
        test_health,
        test_capabilities,
        test_echo_task,
        test_inference_task,
        test_monitoring_task,
        test_orchestrator_integration,
        test_invalid_task,
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
    
    if passed == total:
        print("\n✅ ALL TESTS PASSED")
        print("\n" + "="*70 + "\n")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED")
        print("\n" + "="*70 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
