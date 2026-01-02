#!/usr/bin/env python3
"""
Agent Web Dashboard - Real-time monitoring and control interface
"""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
from pathlib import Path
import sys

# Add parent directory to path to import agent modules
sys.path.insert(0, str(Path(__file__).parent))

from agent_core import coordinator, Task, TaskPriority

app = Flask(__name__)
CORS(app)

# Store for real-time updates
status_log = []

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/status')
def get_status():
    """Get current fleet status"""
    status = coordinator.get_fleet_status()
    return jsonify(status)

@app.route('/api/agents')
def get_agents():
    """Get list of all agents"""
    agents = []
    for agent_id, agent in coordinator.agents.items():
        agents.append({
            'id': agent_id,
            'name': agent.name,
            'status': agent.status.value,
            'capabilities': list(agent.capabilities.keys()),
            'queue_size': agent.task_queue.qsize(),
            'metrics': agent.metrics
        })
    return jsonify(agents)

@app.route('/api/agents/<agent_id>')
def get_agent(agent_id):
    """Get detailed info about specific agent"""
    if agent_id in coordinator.agents:
        agent = coordinator.agents[agent_id]
        return jsonify(agent.get_status())
    return jsonify({'error': 'Agent not found'}), 404

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    """Handle task operations"""
    if request.method == 'POST':
        data = request.json
        
        # Create new task
        task = Task(
            id=data.get('id', f"web_task_{int(datetime.now().timestamp())}"),
            name=data.get('name', 'Unnamed Task'),
            action=data.get('action'),
            params=data.get('params', {}),
            priority=TaskPriority[data.get('priority', 'NORMAL')]
        )
        
        success = coordinator.assign_task(task)
        
        return jsonify({
            'success': success,
            'task_id': task.id,
            'assigned_to': task.assigned_to
        })
    
    else:
        # Get task history
        tasks = []
        for agent in coordinator.agents.values():
            for task in agent.completed_tasks[-10:]:  # Last 10 tasks
                tasks.append({
                    'id': task.id,
                    'name': task.name,
                    'action': task.action,
                    'status': task.status,
                    'agent': agent.name,
                    'result': str(task.result)[:100] if task.result else None
                })
        return jsonify(tasks)

@app.route('/api/metrics')
def get_metrics():
    """Get aggregated metrics"""
    metrics = {
        'total_agents': len(coordinator.agents),
        'active_agents': sum(1 for a in coordinator.agents.values() if a.status.value == 'active'),
        'total_tasks': coordinator.metrics['total_tasks'],
        'completed_tasks': sum(a.metrics['tasks_completed'] for a in coordinator.agents.values()),
        'failed_tasks': sum(a.metrics['tasks_failed'] for a in coordinator.agents.values()),
        'avg_task_time': sum(a.metrics['avg_task_time'] for a in coordinator.agents.values()) / max(len(coordinator.agents), 1)
    }
    return jsonify(metrics)

@app.route('/api/submit_demo')
def submit_demo():
    """Submit demo tasks"""
    demo_tasks = [
        Task(
            id=f"demo_{int(datetime.now().timestamp())}",
            name="System Health Check",
            action="check_health",
            params={},
            priority=TaskPriority.HIGH
        ),
        Task(
            id=f"demo_{int(datetime.now().timestamp()) + 1}",
            name="Monitor Resources",
            action="monitor_resources",
            params={},
            priority=TaskPriority.NORMAL
        )
    ]
    
    results = []
    for task in demo_tasks:
        success = coordinator.assign_task(task)
        results.append({'task': task.name, 'success': success})
    
    return jsonify({'submitted': len(results), 'results': results})

@app.route('/api/control/<action>')
def control(action):
    """Control fleet operations"""
    if action == 'start':
        coordinator.start_all()
        return jsonify({'success': True, 'message': 'Fleet started'})
    elif action == 'stop':
        coordinator.stop_all()
        return jsonify({'success': True, 'message': 'Fleet stopped'})
    else:
        return jsonify({'success': False, 'message': 'Unknown action'}), 400

def create_dashboard_html():
    """Create the HTML dashboard"""
    html_dir = Path(__file__).parent / 'templates'
    html_dir.mkdir(exist_ok=True)
    
    dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 NoizyLab Agent Fleet Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            padding: 20px;
        }
        .container { max-width: 1400px; margin: 0 auto; }
        h1 { text-align: center; margin-bottom: 30px; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .metric-card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .metric-value { font-size: 2.5em; font-weight: bold; margin: 10px 0; }
        .metric-label { font-size: 0.9em; opacity: 0.9; }
        .agents-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .agent-card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .agent-name { font-size: 1.3em; font-weight: bold; margin-bottom: 10px; }
        .agent-status {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8em;
            margin: 10px 0;
        }
        .status-active { background: #4ade80; color: #000; }
        .status-idle { background: #fbbf24; color: #000; }
        .status-busy { background: #f87171; color: #fff; }
        .capabilities { margin-top: 15px; }
        .capability-tag {
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 5px 10px;
            border-radius: 10px;
            margin: 3px;
            font-size: 0.8em;
        }
        .controls {
            text-align: center;
            margin: 30px 0;
        }
        .btn {
            background: rgba(255,255,255,0.2);
            border: 2px solid #fff;
            color: #fff;
            padding: 12px 30px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            margin: 0 10px;
            transition: all 0.3s;
        }
        .btn:hover {
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
        }
        .refresh-indicator {
            text-align: center;
            margin: 20px 0;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 NoizyLab Agent Fleet Dashboard</h1>
        
        <div class="refresh-indicator">
            <p>🔄 Auto-refreshing every 3 seconds</p>
        </div>
        
        <div class="metrics" id="metrics">
            <!-- Metrics will be populated here -->
        </div>
        
        <div class="controls">
            <button class="btn" onclick="submitDemo()">📋 Submit Demo Tasks</button>
            <button class="btn" onclick="refreshNow()">🔄 Refresh Now</button>
        </div>
        
        <h2 style="margin: 30px 0 20px 0;">Active Agents</h2>
        <div class="agents-grid" id="agents">
            <!-- Agents will be populated here -->
        </div>
    </div>

    <script>
        async function fetchMetrics() {
            const response = await fetch('/api/metrics');
            const data = await response.json();
            
            document.getElementById('metrics').innerHTML = `
                <div class="metric-card">
                    <div class="metric-label">Total Agents</div>
                    <div class="metric-value">${data.total_agents}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Active Agents</div>
                    <div class="metric-value">${data.active_agents}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Total Tasks</div>
                    <div class="metric-value">${data.total_tasks}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Completed</div>
                    <div class="metric-value">${data.completed_tasks}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Failed</div>
                    <div class="metric-value">${data.failed_tasks}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Avg Task Time</div>
                    <div class="metric-value">${data.avg_task_time.toFixed(2)}s</div>
                </div>
            `;
        }
        
        async function fetchAgents() {
            const response = await fetch('/api/agents');
            const agents = await response.json();
            
            const agentsHTML = agents.map(agent => `
                <div class="agent-card">
                    <div class="agent-name">${agent.name}</div>
                    <div class="agent-status status-${agent.status}">${agent.status.toUpperCase()}</div>
                    <p style="margin: 10px 0;">Queue: ${agent.queue_size} tasks</p>
                    <p>Completed: ${agent.metrics.tasks_completed} | Failed: ${agent.metrics.tasks_failed}</p>
                    <div class="capabilities">
                        ${agent.capabilities.slice(0, 5).map(cap => 
                            `<span class="capability-tag">${cap}</span>`
                        ).join('')}
                        ${agent.capabilities.length > 5 ? `<span class="capability-tag">+${agent.capabilities.length - 5} more</span>` : ''}
                    </div>
                </div>
            `).join('');
            
            document.getElementById('agents').innerHTML = agentsHTML;
        }
        
        async function submitDemo() {
            const response = await fetch('/api/submit_demo');
            const data = await response.json();
            alert(`Submitted ${data.submitted} demo tasks!`);
            refreshNow();
        }
        
        function refreshNow() {
            fetchMetrics();
            fetchAgents();
        }
        
        // Initial load
        refreshNow();
        
        // Auto-refresh every 3 seconds
        setInterval(refreshNow, 3000);
    </script>
</body>
</html>"""
    
    (html_dir / 'dashboard.html').write_text(dashboard_html)

if __name__ == "__main__":
    print("🌐 Starting Agent Dashboard Web Server")
    print("=" * 60)
    
    # Create dashboard HTML
    create_dashboard_html()
    
    # Import and initialize agents
    from specialized_agents import create_all_agents
    agents = create_all_agents()
    for agent in agents:
        coordinator.register_agent(agent)
        agent.start()
    
    print(f"✅ {len(agents)} agents registered and started")
    print("=" * 60)
    print("🌐 Dashboard available at: http://localhost:5000")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
