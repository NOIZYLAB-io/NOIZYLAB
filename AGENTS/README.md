# NOIZYLAB AGENTS

Central registry and launcher for all MC96UNIVERSE agents.

## Quick Start

```bash
# List available agents
./launch.sh list

# Launch GABRIEL
./launch.sh gabriel

# Launch Cloud Agent
./launch.sh cloud-agent

# Check Cloud Agent status
./launch.sh cloud-status

# Launch all agents
./launch.sh all
```

## Agents

| Agent | Description | Type | Status |
|-------|-------------|------|--------|
| GABRIEL | Zero Latency Voice + Control | Local | ✅ Active |
| MC96 | Core Universe Engine | Local | ✅ Active |
| SystemGuardian | System Monitoring | Local | 🔧 Stub |
| CloudAgent | Cloudflare Worker Agent | Remote | ✅ Active |

## Cloud Agent Delegation

The Cloud Agent runs on Cloudflare Workers and provides task delegation capabilities for distributed workloads.

### Features

- **Task Delegation**: Offload tasks to cloud infrastructure
- **Multiple Task Types**: Support for echo, inference, code-analysis, monitoring
- **REST API**: Simple HTTP API for task submission
- **Status Checking**: Query task status and results
- **Health Monitoring**: Built-in health check endpoints

### Usage

#### From Command Line

```bash
# Check cloud agent status
python3 ../cloud_agent_client.py --status

# Delegate a task
python3 ../cloud_agent_client.py --delegate echo "Hello Cloud"

# Interactive mode
python3 ../cloud_agent_client.py --interactive
```

#### From Python Code

```python
from cloud_agent_client import CloudAgentClient

# Create client
client = CloudAgentClient()

# Check health
health = await client.health_check()
print(health)

# Get capabilities
caps = await client.get_capabilities()
print(caps.capabilities)

# Delegate a task
response = await client.delegate_task(
    task_type="echo",
    task_data={"message": "Hello from Python"}
)
print(response.result)
```

#### Integration with Master Orchestrator

```python
from cloud_agent_client import CloudAgentOrchestrator

# Create orchestrator wrapper
cloud_orch = CloudAgentOrchestrator()

# Route task to cloud
result = await cloud_orch.route_task_to_cloud(
    task_type="inference",
    task_data={"model": "claude", "prompt": "Hello"}
)
```

### API Endpoints

The Cloud Agent exposes the following endpoints:

- `GET /health` - Health check
- `GET /api/capabilities` - List available task types
- `POST /api/delegate` - Delegate a task
- `GET /api/status?task_id=<id>` - Get task status

### Task Types

| Type | Description | Input |
|------|-------------|-------|
| `echo` | Echo message back | `{"message": "text"}` |
| `inference` | AI inference task | `{"model": "...", "prompt": "..."}` |
| `code-analysis` | Analyze code files | `{"files": [...]}` |
| `monitoring` | System monitoring | `{}` |

### Deployment

The Cloud Agent is automatically deployed via GitHub Actions when changes are pushed to `main` or `xenodochial-almeida` branches.

```bash
# Manual deployment
cd workers/noizylab
npm install
wrangler deploy
```

### Configuration

Cloud agent endpoint is configured in:
- `AGENTS/registry.json` - Agent registry
- `cloud_agent_client.py` - Python client (CLOUD_AGENT_ENDPOINT)

Default endpoint: `https://noizylab.rsplowman.workers.dev`

## Registry

See `registry.json` for full agent configuration.
