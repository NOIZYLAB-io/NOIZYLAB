#!/usr/bin/env python3
"""
🎯 NOIZYLAB AGENT SYSTEM - QUICK REFERENCE GUIDE
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║                  🤖 NOIZYLAB AGENT SYSTEM                            ║
║                    Quick Reference Guide                             ║
╚══════════════════════════════════════════════════════════════════════╝

📦 INSTALLATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  $ cd /Volumes/RED\\ DRAGON/noizylab_2026/agents
  $ pip3 install -r requirements.txt

🚀 QUICK START
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Option 1 (Recommended): Master Control
  $ python3 master_control.py

  Option 2: Web Dashboard
  $ python3 agent_dashboard.py
  → Open http://localhost:5000

  Option 3: Simple Fleet Controller
  $ python3 fleet_controller.py

  Option 4: Quick Start Script
  $ ./start_agents.sh

📊 AGENTS AVAILABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ FileSystemAgent       - File operations, scanning, organization
  ✓ CodeAnalysisAgent     - Code analysis, TODO finding, metrics
  ✓ SystemMonitorAgent    - Health checks, resource monitoring
  ✓ DataProcessingAgent   - JSON processing, data transformation
  ✓ AudioProcessingAgent  - Audio library management, duplicates
  ✓ ProjectManagementAgent- DAW project tracking, backups

🎯 COMMON TASKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Scan Audio Library:
    action="scan_audio_library"
    params={"path": "/path/to/audio"}

  Find Duplicates:
    action="find_duplicates"
    params={"path": "/path/to/check"}

  System Health Check:
    action="check_health"
    params={}

  Scan Projects:
    action="scan_projects"
    params={"path": "/path/to/projects"}

  Find TODOs:
    action="find_todos"
    params={"path": "/path/to/code"}

📈 PROGRAMMATIC USAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  from agent_core import Task, TaskPriority, coordinator
  
  task = Task(
      id="my_task",
      name="My Task",
      action="scan_directory",
      params={"path": "/some/path", "depth": 2},
      priority=TaskPriority.HIGH
  )
  
  coordinator.assign_task(task)

📅 SCHEDULING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  from task_scheduler import scheduler
  
  scheduler.schedule(
      name="my_recurring_task",
      action="check_health",
      params={},
      interval_seconds=300  # Every 5 minutes
  )

📡 INTER-AGENT COMMUNICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  from agent_communication import get_communicator, MessageType
  
  comm = get_communicator("agent_id")
  await comm.send_message(
      recipient="other_agent",
      msg_type=MessageType.TASK_REQUEST,
      payload={"data": "value"}
  )

🔍 MONITORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Get Status:
    status = coordinator.get_fleet_status()

  Agent Metrics:
    agent_status = agent.get_status()
    
  Performance Analysis:
    from performance_analyzer import PerformanceAnalyzer
    analyzer = PerformanceAnalyzer()
    analyzer.take_snapshot()

🚦 PRIORITY LEVELS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TaskPriority.CRITICAL    (0) - Immediate execution
  TaskPriority.HIGH        (1) - High priority
  TaskPriority.NORMAL      (2) - Default priority
  TaskPriority.LOW         (3) - Low priority
  TaskPriority.BACKGROUND  (4) - Background processing

🛠️ CONFIGURATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Environment Variables:
    export UAP_WS_PORT=8123
    export NOIZY_BIND=127.0.0.1
    export MESH_SHARED_SECRET=your_secret

📝 FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  agent_core.py              - Core framework
  specialized_agents.py      - Basic agents
  advanced_agents.py         - Audio/Project agents
  agent_communication.py     - Messaging system
  task_scheduler.py          - Cron scheduler
  fleet_controller.py        - CLI controller
  agent_dashboard.py         - Web interface
  master_control.py          - Main orchestrator ⭐
  performance_analyzer.py    - Performance tools
  fleet_heartbeat.py         - Mesh integration

📚 DOCUMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  README.md           - Main documentation
  SYSTEM_INDEX.md     - Complete file index
  QUICK_REFERENCE.py  - This guide

🧪 TESTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  $ python3 test_system.py

🆘 TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Problem: Module not found
  Solution: pip3 install -r requirements.txt

  Problem: Agent not responding
  Solution: Check agent.status and logs

  Problem: Tasks not completing
  Solution: Check queue size and agent metrics

  Problem: High failure rate
  Solution: Review task parameters and error logs

🌐 WEB DASHBOARD ENDPOINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  GET  /api/status          - Fleet status
  GET  /api/agents          - List all agents
  GET  /api/agents/<id>     - Specific agent
  GET  /api/metrics         - Aggregated metrics
  POST /api/tasks           - Submit task
  GET  /api/submit_demo     - Run demo tasks
  GET  /api/control/<action>- Control fleet

📞 SUPPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Version: 1.0.0
  Created: November 25, 2025
  Status: Production Ready ✅

╔══════════════════════════════════════════════════════════════════════╗
║  🚀 Ready to deploy! Start with: python3 master_control.py          ║
╚══════════════════════════════════════════════════════════════════════╝
""")
