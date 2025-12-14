# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **New Relic CodeStream VS Code Extension** - a sophisticated IDE integration that brings production telemetry, observability, and collaboration capabilities directly into VS Code. It enables developers to view code-level metrics, investigate errors, search logs, execute NRQL queries, and collaborate on code reviews without leaving their IDE.

**Current Version:** 16.1.2
**Min VS Code Version:** 1.73.0
**Repository:** https://github.com/TeamCodeStream/CodeStream

## Common Development Commands

### Setup & Installation
```bash
npm install              # Install dependencies
npm run agent:rebuild    # Build shared agent
npm run webview:build    # Build webview components
npm run build            # Build extension
```

### Development Workflow
```bash
npm run watch               # Watch extension for changes
npm run agent:watch         # Watch shared agent
npm run mwatch             # Watch both in tmux
npm run webview:watch      # Watch webview components
```

### Testing
```bash
npm run test               # Run all tests (agent + webview + vscode)
npm run vscode:test        # Run extension tests only
npm run test:ci            # CI test run with coverage and junit output
```

### Code Quality
```bash
npm run lint               # Run ESLint with auto-fix
npm run pretty             # Format with Prettier
npm run verify:compile     # Check TypeScript compilation
npm run verify:lint        # Verify linting (no auto-fix)
npm run verify:prettier    # Verify formatting
```

### Production Build
```bash
npm run bundle:ci          # Clean and bundle for CI
npm run bundle             # Full production bundle
npm run pack               # Create .vsix package
```

### Single Test Execution
```bash
npx jest __test__/unit/specific-test.spec.ts    # Run specific test file
npx jest --testNamePattern="test name"          # Run specific test by name
```

## Architecture & Structure

### Monorepo Structure
This is part of a larger monorepo at `C:\code\codestream\`:
- `vscode/` - VS Code extension (this directory)
- `jb/` - JetBrains IDE extension
- `vs/` - Visual Studio extension
- `shared/agent/` - Language server agent (CommonJS)
- `shared/ui/` - Shared React webview components
- `shared/util/` - Shared utilities and protocols

### Key Directories

**`src/controllers/`** - Main UI controllers for extension functionality:
- `sidebarController.ts` - Primary sidebar webview with bidirectional IPC
- `editorController.ts` - Editor-level interactions and document handling
- `instrumentableCodeLensController.ts` - Code-level metrics display
- `nrqlCodeLensController.ts` - NRQL query assistance

**`src/providers/`** - VS Code provider implementations:
- `instrumentationCodeLensProvider.ts` - Shows performance metrics inline
- `markerDecorationProvider.ts` - Visual decorations in editor
- `nrqlDocumentSymbolProvider.ts` - NRQL language support

**`src/api/`** - Authentication and session management:
- `session.ts` - Main session management with event emitters
- `tokenManager.ts` - Secure token storage via VS Code keychain

**`src/agent/`** - LSP connection to shared agent:
- `agentConnection.ts` - Primary LSP client (700+ lines, handles 200+ request types)

**`src/webviews/`** - React webview implementations:
- `sidebar/` - Main sidebar React application
- `editor/` - Editor panel React application

### Build System (esbuild)

The project uses esbuild for bundling with three separate builds:
1. **Extension Build** - Main extension code (`src/extension.ts` → `dist/extension.js`)
2. **Sidebar Build** - React webview (`src/webviews/sidebar/` → `dist/webviews/sidebar/`)
3. **Editor Build** - React webview (`src/webviews/editor/` → `dist/webviews/editor/`)

### Communication Architecture

**Extension ↔ Webview (IPC):**
- Message-based communication via `postMessage`
- Bidirectional request/response with message IDs
- Protocols defined in `@codestream/protocols/webview`

**Extension ↔ Agent (LSP):**
- Language Server Protocol over stdio
- Agent runs as separate CommonJS process
- Typed protocol definitions in `@codestream/protocols/agent`

**Agent ↔ API Server:**
- HTTP REST API with token-based authentication
- Real-time subscriptions for data updates
- Default server: `https://codestream-api-v2-us1.service.newrelic.com`

### Dependency Injection

The `Container` class (src/container.ts) manages all singleton services:
- `_agent`: CodeStreamAgentConnection (LSP client)
- `_session`: CodeStreamSession (authentication & data)
- `_sidebar`: SidebarController (main UI)
- Various providers and controllers

Access services via `Container.instance().session` pattern.

### TypeScript Configuration

**Path Aliases:**
- `@codestream/protocols/agent` → `../../shared/util/src/protocol/agent/agent.protocol.ts`
- `@codestream/protocols/api` → `../../shared/util/src/protocol/agent/api.protocol.ts`
- `@codestream/protocols/webview` → `../../shared/ui/ipc/webview.protocol.ts`
- `@codestream/utils/*` → `../../shared/util/src/utils/*`

**Key Settings:**
- Target: ES2020
- Decorators: Experimental decorators enabled
- Strict mode: Enabled
- Source maps: Enabled for debugging

### Extension Lifecycle

**Activation (`src/extension.ts`):**
1. Initialize configuration and logging
2. Load build metadata and Git executable
3. Migrate deprecated settings
4. Create webview sidebar and container
5. Set up protocol handlers for deep linking
6. Register providers and controllers

**Key Components:**
- **Entry Point:** `./dist/extension` (compiled from `src/extension.ts`)
- **Activity Bar View:** "codestream-activitybar"
- **Commands:** 20+ commands (sign in/out, toggle, log search, NRQL execution)
- **Languages:** NRQL language support with grammar and snippets

### Testing Framework

**Jest Configuration:**
- Uses ts-jest preset
- Tests in `__test__/unit/*.spec.ts`
- Global setup disables New Relic telemetry
- Coverage reports to `coverage/` directory

### Key Extension Points

**CodeLens Providers:**
- Show performance metrics inline in code
- NRQL query assistance and execution
- Configurable via `codestream.goldenSignalsInEditor`

**Commands:**
- `codestream.toggle` - Main sidebar toggle (Ctrl+Shift+/ /)
- `codestream.logSearch` - Open log search
- `codestream.nrqlQuery` - Execute NRQL queries

**Configuration Settings:**
- `codestream.serverUrl` - API server endpoint
- `codestream.traceLevel` - Logging level (silent/errors/verbose/debug)
- `codestream.autoSignIn` - Automatic authentication
- `codestream.disableStrictSSL` - SSL certificate validation

### Debugging

**Logging:**
- Output channel: "CodeStream"
- Command: `codestream.debugProtocol` for detailed protocol logging
- Trace levels configurable via settings

**Common Issues:**
- Proxy/SSL: Configure `disableStrictSSL` or `extraCerts`
- Git detection: Requires VS Code Git extension or git in PATH
- Token issues: Uses VS Code keychain with workspace fallbacks

### Important Files

**Core Files:**
- `src/extension.ts` - Extension entry point and activation
- `src/container.ts` - Dependency injection container
- `src/constants.ts` - Extension IDs and built-in commands
- `src/configuration.ts` - Configuration management

**Protocol Files:**
- Protocols are imported from shared utilities
- Agent protocol: Request/response definitions for LSP
- Webview protocol: IPC message definitions
- API protocol: Data structures for REST API

This extension follows VS Code best practices with clear separation between extension host code, webview UI, and the shared language server agent.