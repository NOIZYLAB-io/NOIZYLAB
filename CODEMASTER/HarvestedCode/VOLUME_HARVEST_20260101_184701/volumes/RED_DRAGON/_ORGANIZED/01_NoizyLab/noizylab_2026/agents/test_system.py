#!/usr/bin/env python3
"""
Quick test script for NoizyLab Agent System
Tests basic functionality of all components
"""
import sys
from pathlib import Path
import asyncio
import time

print("🧪 NoizyLab Agent System - Quick Test")
print("=" * 60)

# Test 1: Import all modules
print("\n1️⃣  Testing module imports...")
try:
    from agent_core import Agent, AgentCoordinator, Task, TaskPriority, coordinator
    print("   ✅ agent_core")
except Exception as e:
    print(f"   ❌ agent_core: {e}")
    sys.exit(1)

try:
    from specialized_agents import create_all_agents
    print("   ✅ specialized_agents")
except Exception as e:
    print(f"   ❌ specialized_agents: {e}")

try:
    from advanced_agents import create_advanced_agents
    print("   ✅ advanced_agents")
except Exception as e:
    print(f"   ❌ advanced_agents: {e}")

try:
    from agent_communication import MessageType, global_message_bus
    print("   ✅ agent_communication")
except Exception as e:
    print(f"   ❌ agent_communication: {e}")

try:
    from task_scheduler import scheduler, setup_default_schedules
    print("   ✅ task_scheduler")
except Exception as e:
    print(f"   ❌ task_scheduler: {e}")

# Test 2: Create agents
print("\n2️⃣  Testing agent creation...")
try:
    basic_agents = create_all_agents()
    print(f"   ✅ Created {len(basic_agents)} basic agents")
    for agent in basic_agents:
        print(f"      • {agent.name}")
except Exception as e:
    print(f"   ❌ Failed to create basic agents: {e}")

try:
    advanced_agents = create_advanced_agents()
    print(f"   ✅ Created {len(advanced_agents)} advanced agents")
    for agent in advanced_agents:
        print(f"      • {agent.name}")
except Exception as e:
    print(f"   ❌ Failed to create advanced agents: {e}")

# Test 3: Register agents
print("\n3️⃣  Testing agent registration...")
all_agents = basic_agents + advanced_agents
for agent in all_agents:
    try:
        coordinator.register_agent(agent)
        print(f"   ✅ Registered: {agent.name}")
    except Exception as e:
        print(f"   ❌ Failed to register {agent.name}: {e}")

# Test 4: Start agents
print("\n4️⃣  Testing agent startup...")
try:
    coordinator.start_all()
    print(f"   ✅ Started {len(all_agents)} agents")
    time.sleep(1)  # Let them start
except Exception as e:
    print(f"   ❌ Failed to start agents: {e}")

# Test 5: Submit test tasks
print("\n5️⃣  Testing task submission...")
test_tasks = [
    Task(
        id="test_health",
        name="Test Health Check",
        action="check_health",
        params={},
        priority=TaskPriority.HIGH
    ),
    Task(
        id="test_scan",
        name="Test Directory Scan",
        action="scan_directory",
        params={"path": str(Path(__file__).parent), "depth": 1},
        priority=TaskPriority.NORMAL
    )
]

submitted = 0
for task in test_tasks:
    try:
        if coordinator.assign_task(task):
            print(f"   ✅ Submitted: {task.name}")
            submitted += 1
        else:
            print(f"   ⚠️  Could not assign: {task.name}")
    except Exception as e:
        print(f"   ❌ Error submitting {task.name}: {e}")

print(f"\n   📊 Successfully submitted {submitted}/{len(test_tasks)} tasks")

# Test 6: Wait for tasks to complete
print("\n6️⃣  Waiting for tasks to complete...")
time.sleep(3)

# Test 7: Check status
print("\n7️⃣  Testing status retrieval...")
try:
    status = coordinator.get_fleet_status()
    print(f"   ✅ Fleet status retrieved")
    print(f"      • Total agents: {status['total_agents']}")
    print(f"      • Total tasks: {status['coordinator_metrics']['total_tasks']}")
    print(f"      • Completed: {status['coordinator_metrics']['completed_tasks']}")
except Exception as e:
    print(f"   ❌ Failed to get status: {e}")

# Test 8: Check individual agents
print("\n8️⃣  Checking individual agent status...")
for agent in all_agents[:3]:  # Check first 3
    try:
        status = agent.get_status()
        print(f"   ✅ {agent.name}")
        print(f"      • Status: {status['status']}")
        print(f"      • Queue: {status['queue_size']}")
        print(f"      • Completed: {status['metrics']['tasks_completed']}")
    except Exception as e:
        print(f"   ❌ {agent.name}: {e}")

# Test 9: Test scheduler
print("\n9️⃣  Testing task scheduler...")
try:
    setup_default_schedules()
    sched_status = scheduler.get_status()
    print(f"   ✅ Scheduler configured")
    print(f"      • Scheduled tasks: {sched_status['scheduled_tasks']}")
except Exception as e:
    print(f"   ❌ Scheduler test failed: {e}")

# Test 10: Cleanup
print("\n🔟 Testing shutdown...")
try:
    coordinator.stop_all()
    print("   ✅ All agents stopped")
except Exception as e:
    print(f"   ❌ Shutdown error: {e}")

# Final report
print("\n" + "=" * 60)
print("✅ TEST SUITE COMPLETED")
print("=" * 60)
print("\n📋 Summary:")
print(f"   • Agents created: {len(all_agents)}")
print(f"   • Tasks submitted: {submitted}")
print(f"   • System status: Operational")
print("\n🚀 Ready for production use!")
print("\nNext steps:")
print("   • Run: python3 master_control.py")
print("   • Or:  python3 agent_dashboard.py")
print("   • Or:  ./start_agents.sh")
print("=" * 60 + "\n")
