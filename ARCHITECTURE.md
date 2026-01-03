# 🏗️ NOIZYLAB Architecture

## System Overview

NOIZYLAB is a unified integration platform that orchestrates multiple systems across macOS, Windows, and Cloudflare Workers environments.

```
┌─────────────────────────────────────────────────────────────────┐
│                     NOIZYLAB Platform                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐      ┌──────────────────┐                │
│  │   Core Layer     │      │  Integration     │                │
│  │                  │      │     Layer        │                │
│  │ • Orchestrator   │◄────►│ • Auth System    │                │
│  │ • Cluster Mgmt   │      │ • File Sync      │                │
│  │ • Event Bus      │      │ • gRPC Bridge    │                │
│  │                  │      │ • Remote Display │                │
│  └──────────────────┘      │ • Metrics        │                │
│                            └──────────────────┘                │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Cloudflare Workers Layer                     │  │
│  │  • NOIZYLAB Worker  • AEON Workers  • Tunnel Workers     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Directory Structure

```
NOIZYLAB/
├── src/                           # Source code
│   ├── core/                      # Core orchestration
│   │   ├── master_orchestrator.py
│   │   └── cluster_launcher.py
│   └── integrations/              # System integrations
│       ├── unified_auth_system.py
│       ├── unified_file_sync.py
│       ├── unified_integration_bridge.py
│       ├── noizylab_grpc_bridge.py
│       ├── secure_transport_layer.py
│       ├── unified_remote_display.py
│       └── unified_performance_metrics.py
│
├── workers/                       # Cloudflare Workers
│   └── noizylab/                  # Main NOIZYLAB worker
│
├── scripts/                       # Utility scripts
├── docs/                          # Documentation
│   ├── guides/                    # Implementation guides
│   ├── setup/                     # Setup instructions
│   ├── plans/                     # Planning documents
│   └── quizzes/                   # Knowledge checks
│
├── gabriel/                       # Gabriel subsystem
├── PROJECTS/                      # Project workspace
├── data/                          # Data files
└── ui/                            # UI components

```

## Core Components

### 1. Master Orchestrator (`src/core/master_orchestrator.py`)
- Central coordination point for all systems
- Event bus for pub/sub messaging
- Node registry and health monitoring
- Workflow execution engine

### 2. Integration Bridge (`src/integrations/unified_integration_bridge.py`)
- Unified interface for all integrated systems
- AEON, RepairRob, 10CC, Tunnel, Ingestion orchestration
- Health reporting and status monitoring

### 3. Authentication System (`src/integrations/unified_auth_system.py`)
- Keychain integration (macOS/Windows)
- API key management
- OAuth2 token handling
- Credential rotation

### 4. File Synchronization (`src/integrations/unified_file_sync.py`)
- Bidirectional file sync
- 5 conflict resolution strategies
- Real-time change detection
- Clipboard sync support

### 5. Secure Transport (`src/integrations/secure_transport_layer.py`)
- SSH tunneling with fallback
- VPN integration
- Network health monitoring
- Bandwidth testing

### 6. Remote Display (`src/integrations/unified_remote_display.py`)
- Multiple codec support (H.264, VP9, H.265, JPEG)
- Window sharing
- Remote input handling
- Annotation support

### 7. Performance Metrics (`src/integrations/unified_performance_metrics.py`)
- System metrics collection
- Network metrics tracking
- Bandwidth throttling
- Prometheus export

### 8. gRPC Bridge (`src/integrations/noizylab_grpc_bridge.py`)
- Cross-platform RPC
- AI task orchestration
- Node discovery
- Health checks

## Data Flow

```
User Request
    ↓
Master Orchestrator
    ↓
Integration Bridge
    ↓
┌─────────┬─────────┬─────────┬─────────┐
│  Auth   │  Sync   │ Network │ Display │
└─────────┴─────────┴─────────┴─────────┘
    ↓
gRPC / REST API
    ↓
Remote Systems / Workers
```

## Technology Stack

- **Python 3.12+**: Core backend
- **TypeScript**: Cloudflare Workers
- **gRPC**: Inter-node communication
- **WebSockets**: Real-time updates
- **Cloudflare Workers**: Edge computing
- **D1**: SQLite at the edge

## Security

- Keychain integration for credential storage
- SSH tunneling for secure transport
- Token rotation for API keys
- Environment-based configuration
- No hardcoded credentials

## Getting Started

See [QUICK_START_EXAMPLES.py](/QUICK_START_EXAMPLES.py) for runnable examples.

## Additional Resources

- [Integration Completion Report](/docs/guides/INTEGRATION_COMPLETION_REPORT.md)
- [Setup Guides](/docs/setup/)
- [API Documentation](/docs/DOCUMENTATION_INDEX.md)
