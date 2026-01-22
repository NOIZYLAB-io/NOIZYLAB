# NOIZYLAB Source Code

Core Python modules for the NOIZYLAB unified integration platform.

## Structure

```
src/
├── core/              # Core orchestration modules
│   ├── master_orchestrator.py
│   └── cluster_launcher.py
└── integrations/      # System integration modules
    ├── unified_auth_system.py
    ├── unified_auth_manager.py
    ├── unified_file_sync.py
    ├── unified_integration_bridge.py
    ├── noizylab_grpc_bridge.py
    ├── secure_transport_layer.py
    ├── unified_remote_display.py
    └── unified_performance_metrics.py
```

## Core Modules

### `core/master_orchestrator.py`
Master orchestration layer connecting all systems. Provides:
- Event bus for pub/sub messaging
- Node registry and health monitoring
- Workflow execution engine
- Cross-system coordination

### `core/cluster_launcher.py`
Cluster launch and management utilities:
- Multi-node cluster initialization
- Configuration management
- Health checks and monitoring

## Integration Modules

### `integrations/unified_integration_bridge.py`
Unified interface for all integrated systems (AEON, RepairRob, 10CC, etc.):
- System orchestration
- Health reporting
- Configuration management

### `integrations/unified_auth_system.py` & `unified_auth_manager.py`
Authentication and credential management:
- Keychain integration (macOS/Windows)
- API key management
- OAuth2 token handling
- Credential rotation

### `integrations/unified_file_sync.py`
Bidirectional file synchronization:
- Real-time change detection
- 5 conflict resolution strategies
- Clipboard sync support

### `integrations/secure_transport_layer.py`
Secure network transport:
- SSH tunneling with fallback
- VPN integration
- Network health monitoring
- Bandwidth testing

### `integrations/unified_remote_display.py`
Remote display capabilities:
- Multiple codec support (H.264, VP9, H.265, JPEG)
- Window sharing
- Remote input handling
- Annotation support

### `integrations/unified_performance_metrics.py`
Performance monitoring and metrics:
- System metrics collection
- Network metrics tracking
- Bandwidth throttling
- Prometheus export

### `integrations/noizylab_grpc_bridge.py`
gRPC bridge for cross-platform communication:
- Inter-node RPC
- AI task orchestration
- Node discovery
- Health checks

## Usage

Import modules from the package structure:

```python
from src.integrations.unified_integration_bridge import UnifiedIntegrationBridge
from src.core.master_orchestrator import MasterOrchestrator

bridge = UnifiedIntegrationBridge()
await bridge.initialize_all()
```

## Development

### Code Style

- **Formatter**: Black
- **Linter**: Ruff
- **Type Checking**: MyPy (when available)

Run formatting:
```bash
black src/
```

Run linting:
```bash
ruff check src/
```

### Testing

Tests should be added to a `tests/` directory at the repository root:

```bash
pytest tests/
```

## Requirements

See `/requirements.txt` for Python dependencies.

Key dependencies:
- Python 3.12+
- asyncio for async operations
- aiohttp for HTTP client
- websockets for WebSocket support
