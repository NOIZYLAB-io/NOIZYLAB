# UnfoldAI Pure Architecture Documentation

## 🏗️ **System Overview**

UnfoldAI follows a **layered architecture pattern** with clear separation of concerns between frontend (VS Code Extension) and backend (Node.js API), deployed on AWS cloud infrastructure with high availability and scalability.

## 🎯 **Frontend Architecture (VS Code Extension)**

### **Architecture Layers**

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code Extension                        │
├─────────────────────────────────────────────────────────────┤
│  Presentation Layer (UI Components)                         │
│  ├── Sidebar.svelte (Main Chat Interface)                  │
│  ├── Node.svelte (File Tree Component)                     │
│  ├── Confetti.svelte (Success Animations)                  │
│  └── MandatoryUpdateModal.svelte (Update Notifications)    │
├─────────────────────────────────────────────────────────────┤
│  Business Logic Layer (Services)                            │
│  ├── apiKeyManager.ts (API Key Management)                 │
│  ├── codeBaseService.ts (Codebase Operations)              │
│  ├── crossPlatformTerminalService.ts (Terminal Integration)│
│  ├── monitorCodePasteService.ts (Code Paste Monitoring)    │
│  └── monitorTerminalsService.ts (Terminal Monitoring)      │
├─────────────────────────────────────────────────────────────┤
│  State Management Layer (Svelte Stores)                     │
│  ├── userStore (User Authentication State)                 │
│  ├── chatStore (Chat History & State)                      │
│  └── codebaseStore (Codebase Analysis State)               │
├─────────────────────────────────────────────────────────────┤
│  Communication Layer (API Integration)                      │
│  ├── HTTP Client (node-fetch)                              │
│  ├── WebSocket Client (Real-time Updates)                  │
│  └── Error Handling & Retry Logic                          │
├─────────────────────────────────────────────────────────────┤
│  Extension Integration Layer                                │
│  ├── extension.ts (VS Code Extension Entry Point)          │
│  ├── SidebarProvider.ts (Webview Management)               │
│  └── VS Code API Integration                               │
└─────────────────────────────────────────────────────────────┘
```

### **Layer Details**

#### **1. Presentation Layer (UI Components)**
```typescript
// webviews/components/
├── Sidebar.svelte              // Main chat interface
│   ├── Chat Interface          // Message display and input
│   ├── File Tree Integration   // Codebase selection
│   ├── Settings Panel          // User preferences
│   └── Status Indicators       // Loading, error states
├── Node.svelte                 // File tree component
│   ├── File/Folder Display     // Hierarchical view
│   ├── Selection Management    // Checkbox interactions
│   └── Context Menus           // Right-click actions
├── Confetti.svelte             // Success animations
└── MandatoryUpdateModal.svelte // Update notifications
```

#### **2. Business Logic Layer (Services)**
```typescript
// Services/
├── apiKeyManager.ts            // API key management
│   ├── Key Storage             // Secure key persistence
│   ├── Key Validation          // API key verification
│   └── Key Rotation            // Automatic key updates
├── codeBaseService.ts          // Codebase operations
│   ├── File Reading            // VS Code file system access
│   ├── Content Processing      // File content extraction
│   ├── Token Calculation       // Content token estimation
│   └── Filtering Logic         // File selection algorithms
├── crossPlatformTerminalService.ts // Terminal integration
│   ├── Terminal Detection      // Platform-specific terminals
│   ├── Command Execution       // Cross-platform commands
│   └── Output Parsing          // Terminal output analysis
├── monitorCodePasteService.ts  // Code paste monitoring
│   ├── Paste Detection         // Clipboard monitoring
│   ├── Content Analysis        // Code snippet analysis
│   └── Auto-suggestions        // Context-aware suggestions
└── monitorTerminalsService.ts  // Terminal monitoring
    ├── Error Detection         // Real-time error monitoring
    ├── Auto-solve Triggers     // Automatic problem resolution
    └── Context Preservation    // Terminal state management
```

#### **3. State Management Layer (Svelte Stores)**
```typescript
// stores/
├── userStore.ts                // User authentication state
│   ├── User Data               // User profile information
│   ├── Authentication Status   // Login/logout state
│   ├── Premium Status          // Subscription information
│   └── API Keys                // User API keys
├── chatStore.ts                // Chat history & state
│   ├── Message History         // Conversation messages
│   ├── Chat Tabs               // Multiple chat sessions
│   ├── Chat State              // Context flags and metadata
│   └── Token Management        // Conversation token tracking
└── codebaseStore.ts            // Codebase analysis state
    ├── File Selection          // Selected files for analysis
    ├── Analysis History        // Previous analysis results
    ├── Filtering State         // File filtering preferences
    └── Training Status         // Model training progress
```

#### **4. Communication Layer (API Integration)**
```typescript
// Communication/
├── HTTP Client (node-fetch)    // REST API communication
│   ├── Request Builder         // API request construction
│   ├── Response Handler        // Response processing
│   ├── Error Handling          // Network error management
│   └── Retry Logic             // Automatic retry mechanisms
├── WebSocket Client            // Real-time updates
│   ├── Connection Management   // WebSocket lifecycle
│   ├── Event Handling          // Real-time event processing
│   ├── Reconnection Logic      // Automatic reconnection
│   └── Message Queuing         // Offline message handling
└── API Integration Layer       // Backend communication
    ├── Authentication          // JWT token management
    ├── Rate Limiting           // Request throttling
    ├── Caching                 // Response caching
    └── Offline Support         // Offline functionality
```

#### **5. Extension Integration Layer**
```typescript
// Extension Core/
├── extension.ts                // VS Code Extension Entry Point
│   ├── Extension Activation    // Extension startup logic
│   ├── Command Registration    // VS Code command registration
│   ├── Event Handlers          // VS Code event processing
│   ├── Webview Management      // Webview panel lifecycle
│   └── Resource Management     // Extension resource cleanup
├── SidebarProvider.ts          // Webview Management
│   ├── Webview Creation        // Webview panel instantiation
│   ├── Message Passing         // Extension ↔ Webview communication
│   ├── State Synchronization   // Extension state management
│   ├── Error Handling          // Webview error management
│   └── Resource Cleanup        // Memory and resource management
└── VS Code API Integration     // VS Code Platform Integration
    ├── File System Access      // VS Code file system operations
    ├── Terminal Integration    // VS Code terminal access
    ├── Workspace Management    // Workspace state and settings
    ├── Extension API           // VS Code extension API usage
    └── Platform Detection      // OS and platform detection
```

## 🔧 **Backend Architecture (Node.js API)**

### **Architecture Layers**

```
┌─────────────────────────────────────────────────────────────┐
│                    Node.js Backend API                      │
├─────────────────────────────────────────────────────────────┤
│  API Gateway Layer (Express.js)                             │
│  ├── Route Management (REST Endpoints)                      │
│  ├── Middleware Stack (Authentication, CORS, etc.)          │
│  ├── Request Validation (Input Sanitization)                │
│  └── Response Formatting (JSON, Error Handling)             │
├─────────────────────────────────────────────────────────────┤
│  Business Logic Layer (Services)                             │
│  ├── OpenAI Service (AI Integration)                        │
│  ├── Codebase Filtering Service (File Processing)           │
│  ├── Authentication Service (JWT, OAuth)                    │
│  ├── User Management Service (User Operations)              │
│  └── Email Service (MailerLite Integration)                 │
├─────────────────────────────────────────────────────────────┤
│  Data Access Layer (Database)                                │
│  ├── TypeORM (Object-Relational Mapping)                    │
│  ├── PostgreSQL (Primary Database)                          │
│  ├── Connection Pooling (Database Connections)              │
│  └── Migration Management (Schema Updates)                  │
├─────────────────────────────────────────────────────────────┤
│  External Services Layer (Third-Party APIs)                 │
│  ├── OpenAI API (GPT-4o-mini Integration)                   │
│  ├── Logflare API (Logging Service)                         │
│  ├── MailerLite API (Email Service)                         │
│  └── OAuth Providers (GitHub, Google)                       │
├─────────────────────────────────────────────────────────────┤
│  Infrastructure Layer (System Services)                     │
│  ├── Logging Service (Winston + Logflare)                   │
│  ├── Configuration Management (Environment Variables)       │
│  ├── Health Monitoring (Health Checks)                      │
│  └── Error Handling (Global Error Management)               │
└─────────────────────────────────────────────────────────────┘
```

### **Layer Details**

#### **1. API Gateway Layer (Express.js)**
```typescript
// index.ts - Main Application Entry Point
├── Express Server Setup        // Server configuration
│   ├── Middleware Registration // CORS, body-parser, etc.
│   ├── Route Registration      // API endpoint registration
│   ├── Error Handling          // Global error middleware
│   └── Health Checks           // Application health endpoints
├── Route Management            // REST API endpoints
│   ├── /Unfold/New/solution    // Main chat endpoint
│   ├── /Unfold/new/codebase-filter // File filtering endpoint
│   ├── /auth/*                 // Authentication endpoints
│   └── /user/*                 // User management endpoints
├── Middleware Stack            // Request processing pipeline
│   ├── Authentication          // JWT token validation
│   ├── Rate Limiting           // Request throttling
│   ├── Request Validation      // Input sanitization
│   ├── CORS Handling           // Cross-origin requests
│   └── Logging                 // Request/response logging
└── Response Management         // Response handling
    ├── JSON Formatting         // Response serialization
    ├── Error Responses         // Standardized error format
    ├── Status Codes            // HTTP status code management
    └── Headers                 // Response header management
```

#### **2. Business Logic Layer (Services)**
```typescript
// helpers/ - Core Business Logic
├── openai.ts                   // OpenAI Integration Service
│   ├── API Communication       // OpenAI API calls
│   ├── Token Management        // Context window management
│   ├── Response Processing     // AI response handling
│   ├── Error Handling          // API error management
│   └── Retry Logic             // Automatic retry mechanisms
├── codebaseFiltering.ts        // File Filtering Service
│   ├── File Analysis           // File content analysis
│   ├── Semantic Chunking       // Intelligent file chunking
│   ├── Relevance Scoring       // File importance calculation
│   ├── Selection Algorithms    // File selection strategies
│   └── Token Optimization      // Token limit management
├── auth.ts                     // Authentication Service
│   ├── JWT Management          // Token generation/validation
│   ├── OAuth Integration       // GitHub/Google OAuth
│   ├── Password Security       // bcryptjs hashing
│   ├── Session Management      // User session handling
│   └── Permission Control      // Role-based access control
├── userManagement.ts           // User Management Service
│   ├── User CRUD Operations    // User data management
│   ├── Profile Management      // User profile operations
│   ├── Subscription Handling   // Premium status management
│   ├── Usage Tracking          // API usage monitoring
│   └── Analytics               // User behavior analytics
└── mailerLite.ts               // Email Service
    ├── Email Templates         // Email content templates
    ├── Campaign Management     // Email campaign handling
    ├── Subscription Management // Email list management
    ├── Analytics               // Email performance tracking
    └── Automation              // Automated email workflows
```

#### **3. Data Access Layer (Database)**
```typescript
// Database Layer
├── TypeORM Configuration       // Database connection setup
│   ├── Connection Pooling      // Database connection management
│   ├── Migration System        // Schema version control
│   ├── Entity Management       // Data model definitions
│   └── Query Optimization      // Database query optimization
├── Entities                    // Data Models
│   ├── User.ts                 // User entity
│   │   ├── User Profile        // User information
│   │   ├── Authentication      // Auth-related fields
│   │   ├── Subscription        // Premium status
│   │   └── Usage Metrics       // API usage tracking
│   ├── Chat.ts                 // Chat entity
│   │   ├── Message History     // Conversation messages
│   │   ├── Context State       // Chat context flags
│   │   ├── Token Usage         // Token consumption
│   │   └── Metadata            // Chat metadata
│   └── CodebaseAnalysis.ts     // Codebase analysis entity
│       ├── File Selection      // Selected files
│       ├── Analysis Results    // Analysis output
│       ├── Training Status     // Model training state
│       └── Performance Metrics // Analysis performance
├── Repositories                // Data Access Objects
│   ├── UserRepository          // User data operations
│   ├── ChatRepository          // Chat data operations
│   └── CodebaseRepository      // Codebase data operations
└── Database Operations         // Database interactions
    ├── CRUD Operations         // Create, Read, Update, Delete
    ├── Complex Queries         // Advanced database queries
    ├── Transactions            // Database transaction management
    └── Performance Monitoring  // Query performance tracking
```

#### **4. External Services Layer (Third-Party APIs)**
```typescript
// External API Integrations
├── OpenAI API Integration      // AI Service Integration
│   ├── GPT-4o-mini Access      // Model API calls
│   ├── Token Counting          // tiktoken integration
│   ├── Context Management      // Conversation context
│   ├── Response Processing     // AI response handling
│   └── Error Recovery          // API failure handling
├── Logflare Integration        // Logging Service
│   ├── Structured Logging      // Winston integration
│   ├── Custom Transport        // Logflare transport
│   ├── Log Rotation            // Daily log rotation
│   ├── Real-time Monitoring    // Live log streaming
│   └── Analytics               // Log analytics
├── OAuth Providers             // Authentication Providers
│   ├── GitHub OAuth            // GitHub authentication
│   ├── Google OAuth            // Google authentication
│   ├── Token Management        // OAuth token handling
│   ├── User Profile Sync       // Profile synchronization
│   └── Permission Scopes       // OAuth permission management
└── Email Service Integration   // Email Marketing
    ├── MailerLite API          // Email service API
    ├── Campaign Management     // Email campaign handling
    ├── List Management         // Email list operations
    ├── Template Management     // Email template handling
    └── Analytics               // Email performance tracking
```

#### **5. Infrastructure Layer (System Services)**
```typescript
// Infrastructure Services
├── Logging Service             // Application Logging
│   ├── Winston Configuration   // Logging framework setup
│   ├── Log Levels              // Debug, Info, Warn, Error
│   ├── Structured Logging      // JSON log format
│   ├── Log Rotation            // File rotation management
│   └── External Logging        // Logflare integration
├── Configuration Management    // Environment Configuration
│   ├── Environment Variables   // Configuration variables
│   ├── Secret Management       // Sensitive data handling
│   ├── Feature Flags           // Feature toggle management
│   ├── API Keys                // External API credentials
│   └── Database Configuration  // Database connection settings
├── Health Monitoring           // System Health Checks
│   ├── Application Health      // Service health endpoints
│   ├── Database Health         // Database connectivity checks
│   ├── External API Health     // Third-party service checks
│   ├── Performance Metrics     // System performance monitoring
│   └── Alerting                // Health alert notifications
└── Error Handling              // Global Error Management
    ├── Error Classification     // Error type categorization
    ├── Error Logging           // Error logging and tracking
    ├── Error Recovery          // Automatic error recovery
    ├── User Notifications      // User-friendly error messages
    └── Error Analytics         // Error pattern analysis
```

## ☁️ **Cloud Infrastructure Architecture (AWS)**

### **High-Level Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                        AWS Cloud Infrastructure              │
├─────────────────────────────────────────────────────────────┤
│  Global Load Balancing & DNS                                 │
│  ├── Route 53 (DNS Management)                              │
│  ├── Application Load Balancer (ALB)                        │
│  ├── SSL/TLS Termination                                     │
│  └── Health Checks & Failover                                │
├─────────────────────────────────────────────────────────────┤
│  Container Orchestration                                     │
│  ├── Amazon ECS (Container Service)                          │
│  ├── ECR (Container Registry)                                │
│  ├── ARM64 Docker Builds                                     │
│  └── Auto Scaling Groups                                      │
├─────────────────────────────────────────────────────────────┤
│  Data Layer                                                  │
│  ├── RDS PostgreSQL (Primary Database)                       │
│  ├── Read Replicas (Performance)                             │
│  ├── Multi-AZ Deployment (High Availability)                 │
│  └── Automated Backups                                       │
├─────────────────────────────────────────────────────────────┤
│  Security & Secrets Management                               │
│  ├── AWS Secrets Manager                                     │
│  ├── IAM Roles & Policies                                     │
│  ├── VPC & Security Groups                                    │
│  └── WAF (Web Application Firewall)                          │
├─────────────────────────────────────────────────────────────┤
│  Monitoring & Observability                                  │
│  ├── CloudWatch (Metrics & Logs)                             │
│  ├── CloudWatch Alarms                                       │
│  ├── X-Ray (Distributed Tracing)                             │
│  └── SNS (Notifications)                                     │
├─────────────────────────────────────────────────────────────┤
│  CI/CD Pipeline                                              │
│  ├── CodeBuild (Build Process)                               │
│  ├── CodePipeline (Deployment Pipeline)                      │
│  ├── Blue-Green Deployment                                   │
│  └── Rollback Mechanisms                                      │
└─────────────────────────────────────────────────────────────┘
```

### **Detailed Infrastructure Components**

#### **1. Global Load Balancing & DNS**
```yaml
# Route 53 Configuration
Route53:
  Domain: unfoldai.com
  Health Checks:
    - Path: /health
    - Interval: 30s
    - Timeout: 5s
    - Failure Threshold: 3
  Failover:
    - Primary: us-east-1
    - Secondary: us-west-2
  SSL/TLS:
    - Certificate: ACM managed
    - Protocol: TLS 1.2+
    - Cipher Suite: Modern

# Application Load Balancer
ALB:
  Type: Application Load Balancer
  Protocol: HTTPS (443)
  Target Groups:
    - Backend API (Port 3002)
    - Health Check Path: /health
  Security Groups:
    - Inbound: HTTPS (443) from 0.0.0.0/0
    - Outbound: All traffic
  Features:
    - SSL/TLS Termination
    - Sticky Sessions
    - Access Logs
    - WAF Integration
```

#### **2. Container Orchestration**
```yaml
# Amazon ECS Configuration
ECS:
  Cluster: unfoldai-cluster
  Service: unfoldai-backend
  Task Definition:
    Family: unfoldai-backend
    Network Mode: awsvpc
    CPU: 1024 (1 vCPU)
    Memory: 2048 MB
    Container:
      Name: unfoldai-api
      Image: unfoldai/backend:latest
      Port: 3002
      Environment:
        - NODE_ENV=production
        - DATABASE_URL=${DATABASE_URL}
        - OPENAI_API_KEY=${OPENAI_API_KEY}
      Secrets:
        - JWT_SECRET: secretsmanager:jwt-secret
        - LOGFLARE_TOKEN: secretsmanager:logflare-token
      Health Check:
        Command: ["CMD-SHELL", "curl -f http://localhost:3002/health || exit 1"]
        Interval: 30s
        Timeout: 5s
        Retries: 3

# ECR Repository
ECR:
  Repository: unfoldai/backend
  Image Tagging: latest, v1.5.1
  Lifecycle Policy:
    - Keep last 10 images
    - Delete images older than 30 days
  Cross-Region Replication:
    - Source: us-east-1
    - Destination: us-west-2

# ARM64 Docker Build
Dockerfile:
  Platform: linux/arm64
  Base Image: node:18-alpine
  Multi-stage Build:
    - Build Stage: Dependencies installation
    - Production Stage: Optimized runtime
  Build Arguments:
    - NODE_ENV=production
    - TARGETPLATFORM=linux/arm64
```

#### **3. Data Layer**
```yaml
# RDS PostgreSQL Configuration
RDS:
  Engine: PostgreSQL 14
  Instance Class: db.t4g.micro (ARM64)
  Storage:
    Type: gp3
    Size: 20 GB
    IOPS: 3000
    Throughput: 125 MB/s
  Multi-AZ: true
  Backup:
    Retention: 7 days
    Window: 03:00-04:00 UTC
    Maintenance Window: Sun 04:00-05:00 UTC
  Security:
    Encryption: Enabled (AES-256)
    Publicly Accessible: false
    VPC Security Groups: Database SG
  Monitoring:
    Enhanced Monitoring: Enabled
    Performance Insights: Enabled
    Log Exports: CloudWatch Logs

# Read Replicas
ReadReplicas:
  - Region: us-east-1
    Instance Class: db.t4g.micro
    Auto Scaling: Enabled
  - Region: us-west-2
    Instance Class: db.t4g.micro
    Auto Scaling: Enabled
```

#### **4. Security & Secrets Management**
```yaml
# AWS Secrets Manager
SecretsManager:
  Secrets:
    - jwt-secret:
        Description: JWT signing secret
        Rotation: 90 days
        Auto Rotation: Enabled
    - logflare-token:
        Description: Logflare API token
        Rotation: 365 days
        Auto Rotation: Disabled
    - database-credentials:
        Description: RDS database credentials
        Rotation: 90 days
        Auto Rotation: Enabled
    - openai-api-key:
        Description: OpenAI API key
        Rotation: Manual
        Auto Rotation: Disabled

# IAM Roles & Policies
IAM:
  ECS Task Role:
    - SecretsManagerReadWrite
    - CloudWatchLogsFullAccess
    - ECSTaskExecutionRole
  ECS Execution Role:
    - ECR Pull Access
    - CloudWatch Logs
    - Secrets Manager Read
  ALB Role:
    - ALB Full Access
    - CloudWatch Logs
```

#### **5. Monitoring & Observability**
```yaml
# CloudWatch Configuration
CloudWatch:
  Metrics:
    - ECS Service Metrics
    - RDS Database Metrics
    - ALB Metrics
    - Custom Application Metrics
  Logs:
    - Application Logs (Winston)
    - Access Logs (ALB)
    - Database Logs (RDS)
    - Container Logs (ECS)
  Alarms:
    - High CPU Usage (>80% for 5 minutes)
    - High Memory Usage (>85% for 5 minutes)
    - Database Connections (>80% for 5 minutes)
    - 5xx Errors (>5% for 2 minutes)
    - Response Time (>2s for 5 minutes)
  Dashboards:
    - Application Performance
    - Infrastructure Health
    - Business Metrics
    - Error Rates

# X-Ray Distributed Tracing
XRay:
  Enabled: true
  Sampling: 10%
  Segments:
    - API Gateway
    - ECS Tasks
    - RDS Queries
    - External APIs
```

#### **6. CI/CD Pipeline**
```yaml
# CodePipeline Configuration
CodePipeline:
  Stages:
    - Source:
        Provider: GitHub
        Repository: codemachine8/Unfold-AI
        Branch: main
        Webhook: Enabled
    - Build:
        Provider: CodeBuild
        Buildspec: buildspec.yml
        Environment:
          Type: ARM_CONTAINER
          Image: aws/codebuild/amazonlinux2-aarch64-standard:2.0
    - Deploy:
        Provider: ECS
        Cluster: unfoldai-cluster
        Service: unfoldai-backend
        Blue-Green: Enabled

# CodeBuild Configuration
CodeBuild:
  Buildspec:
    Version: 0.2
    Phases:
      - Pre-build:
          - Login to ECR
          - Install dependencies
      - Build:
          - Build Docker image
          - Run tests
          - Security scan
      - Post-build:
          - Push to ECR
          - Update ECS service
    Artifacts:
      - Docker image
      - Test results
      - Security scan results

# Blue-Green Deployment
BlueGreen:
  Strategy:
    - Blue: Current production
    - Green: New deployment
    - Switch: Traffic shifting
    - Rollback: Automatic on failure
  Health Checks:
    - Application health
    - Database connectivity
    - External API connectivity
  Rollback Triggers:
    - High error rate (>5%)
    - High response time (>2s)
    - Health check failures
```

### **High Availability & Disaster Recovery**

#### **Multi-Region Deployment**
```yaml
# Primary Region: us-east-1
PrimaryRegion:
  - ECS Cluster
  - RDS Primary
  - ALB
  - Route 53 Primary

# Secondary Region: us-west-2
SecondaryRegion:
  - ECS Cluster (Standby)
  - RDS Read Replica
  - ALB (Standby)
  - Route 53 Secondary

# Failover Configuration
Failover:
  - Automatic: Health check failures
  - Manual: Admin-initiated
  - Data Sync: RDS cross-region replication
  - DNS Failover: Route 53 health checks
```

#### **Backup & Recovery**
```yaml
# Backup Strategy
Backup:
  Database:
    - Automated: Daily snapshots
    - Manual: On-demand snapshots
    - Cross-region: Replication
    - Retention: 30 days
  Application:
    - ECR Images: Versioned
    - Configuration: Parameter Store
    - Secrets: Secrets Manager
    - Logs: CloudWatch Logs

# Recovery Procedures
Recovery:
  RTO (Recovery Time Objective): 15 minutes
  RPO (Recovery Point Objective): 5 minutes
  Procedures:
    - Database: Point-in-time recovery
    - Application: Blue-green deployment
    - DNS: Route 53 failover
    - Monitoring: CloudWatch alarms
```

This comprehensive architecture provides a scalable, secure, and highly available foundation for the UnfoldAI application with proper separation of concerns, monitoring, and disaster recovery capabilities. 