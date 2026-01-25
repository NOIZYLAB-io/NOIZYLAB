# NOIZYLAB AGENTS

Central registry and launcher for all MC96UNIVERSE agents with cloud delegation support.

## Quick Start

```bash
# List available agents
./launch.sh list

# Launch GABRIEL locally
./launch.sh gabriel

# Delegate to cloud GABRIEL
./launch.sh gabriel --cloud

# Launch SystemGuardian (cloud only)
./launch.sh systemguardian --cloud

# Check cloud health
./launch.sh cloud-health

# List cloud agents
./launch.sh cloud-list
```

## Agents

| Agent | Description | Local | Cloud | Status |
|-------|-------------|-------|-------|--------|
| GABRIEL | Zero Latency Voice + Control | ✅ | ✅ | Active |
| MC96 | Core Universe Engine | ✅ | ✅ | Active |
| SystemGuardian | System Monitoring | ❌ | ✅ | Active |

## Cloud Delegation

NOIZYLAB agents can now run in the cloud via Cloudflare Workers, enabling:
- 🌍 **Global availability** - Run agents from anywhere
- ⚡ **Zero latency** - Edge network deployment
- 🔒 **Secure** - HTTPS-only communication
- 📊 **Scalable** - Automatic scaling

### Cloud Architecture

```
Local Request → AGENTS/cloud-delegate.py → Cloudflare Worker
                                          ↓
                                    Cloud Agent (gabriel/mc96/systemGuardian)
                                          ↓
                                       Response
```

### Using Cloud Delegation

#### Python API
```python
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from cloud_delegate import delegate_to_cloud, list_cloud_agents, check_cloud_health

# Check cloud health
health = check_cloud_health()
print(health)

# List available agents
agents = list_cloud_agents()
print(agents)

# Delegate to SystemGuardian
result = delegate_to_cloud('systemGuardian', 'status')
print(result)

# Delegate with parameters
result = delegate_to_cloud('mc96', 'organize', {'path': '/data'})
print(result)
```

#### Command Line
```bash
# Check cloud health
./cloud-delegate.py --health

# List available agents
./cloud-delegate.py --list

# Delegate to agent
./cloud-delegate.py --agent systemGuardian --action status

# Delegate with parameters
./cloud-delegate.py --agent mc96 --action organize --params '{"path": "/data"}'
```

#### Shell Launcher
```bash
# Run locally
./launch.sh gabriel

# Delegate to cloud
./launch.sh gabriel --cloud

# SystemGuardian (cloud only)
./launch.sh systemguardian --cloud
```

## Configuration

Cloud settings are stored in `registry.json`:

```json
{
  "cloud": {
    "enabled": true,
    "endpoint": "https://noizylab.rsplowman.workers.dev",
    "endpoints": {
      "health": "/health",
      "list": "/agent/list",
      "delegate": "/agent/delegate"
    }
  }
}
```

## Deployment

Each agent specifies its deployment modes in the registry:

- `["local"]` - Only available locally
- `["cloud"]` - Only available in cloud
- `["local", "cloud"]` - Available in both modes

## Registry

See `registry.json` for full agent configuration including cloud deployment settings.
