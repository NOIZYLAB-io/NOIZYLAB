# UnfoldAI Tech Stack Documentation

## 🏗️ **Technology Overview**

UnfoldAI is built using modern, production-ready technologies with a clear separation between frontend (VS Code Extension) and backend (Node.js API) components. This document provides a comprehensive overview of all technologies, libraries, and tools used in the project.

## 🎯 **Frontend Tech Stack (VS Code Extension)**

### **Core Technologies**

#### **1. Extension Framework**
- **Platform**: Visual Studio Code Extension
- **Language**: TypeScript 4.7
- **Extension API**: VS Code Extension API v1.74+
- **Package Manager**: npm

#### **2. UI Framework**
- **Framework**: Svelte 3.31.0
- **Build Tool**: Rollup 2.30
- **Preprocessor**: Svelte Preprocess 4.6.1
- **Type Checking**: Svelte Check 1.1.23

#### **3. Development Tools**
- **Linting**: ESLint 8.28.0
- **Type Checking**: TypeScript ESLint 5.45.0
- **Testing**: Mocha 10.1.0
- **Build Tools**: Webpack, Rollup

### **Actual Dependencies**

#### **Core Dependencies**
```json
{
  "dependencies": {
    "@rollup/plugin-commonjs": "^17.0.0",
    "@rollup/plugin-node-resolve": "^11.0.1",
    "@types/glob": "^7.1.3",
    "@types/polka": "^0.5.1",
    "@types/vscode": "^1.52.0",
    "concurrently": "^5.3.0",
    "highlight.js": "^11.8.0",
    "lodash": "^4.17.21",
    "node-fetch": "^3.3.2",
    "polka": "^0.5.2",
    "rollup": "2.30",
    "svelte": "^3.31.0",
    "svelte-check": "^1.1.23",
    "svelte-preprocess": "^4.6.1",
    "ts-loader": "^9.4.2",
    "typescript": "4.7",
    "uuid": "^9.0.0"
  }
}
```

#### **Development Dependencies**
```json
{
  "devDependencies": {
    "@rollup/plugin-typescript": "^11.1.2",
    "@tsconfig/svelte": "^3.0.0",
    "@types/lodash": "^4.14.198",
    "@types/mocha": "^8.0.4",
    "@types/uuid": "^9.0.2",
    "@typescript-eslint/eslint-plugin": "^5.45.0",
    "@typescript-eslint/parser": "^5.45.0",
    "@vscode/test-electron": "^2.2.0",
    "eslint": "^8.28.0",
    "glob": "^8.0.3",
    "mocha": "^10.1.0",
    "rollup-plugin-svelte": "^6.1.1",
    "rollup-plugin-terser": "^7.0.2",
    "rollup-plugin-typescript2": "^0.34.1",
    "svelte-highlight": "^7.3.0",
    "tslib": "^2.4.1"
  }
}
```

### **Frontend Architecture Components**

#### **1. Extension Entry Point**
```typescript
// extension.ts
- Extension activation and deactivation
- Command registration
- Webview panel management
- Sidebar provider integration
```

#### **2. Webview Components**
```typescript
// webviews/components/
├── Sidebar.svelte          // Main chat interface
├── Node.svelte             // File tree component
├── Confetti.svelte         // Success animations
├── MandatoryUpdateModal.svelte // Update notifications
└── sidebar/
    └── Sidebar.svelte      // Sidebar-specific components
```

#### **3. Services Layer**
```typescript
// Services/
├── apiKeyManager.ts        // API key management
├── codeBaseService.ts      // Codebase operations
├── crossPlatformTerminalService.ts // Terminal integration
├── monitorCodePasteService.ts // Code paste monitoring
└── monitorTerminalsService.ts // Terminal monitoring
```

#### **4. Authentication**
```typescript
// Auth/
├── AuthEmail.js           // Email authentication
├── authenticate.ts        // Authentication logic
├── AuthManager.ts         // Auth state management
└── TokenManager.ts        // JWT token handling
```

## 🔧 **Backend Tech Stack (Node.js API)**

### **Core Technologies**

#### **1. Runtime & Framework**
- **Runtime**: Node.js
- **Framework**: Express.js 4.17.1
- **Language**: TypeScript 4.9.5
- **Package Manager**: npm

#### **2. Database & ORM**
- **Database**: PostgreSQL
- **ORM**: TypeORM 0.2.45
- **Connection**: pg 8.5.1

#### **3. Authentication & Security**
- **JWT**: jsonwebtoken 8.5.1
- **Password Hashing**: bcryptjs 3.0.2
- **OAuth**: Passport with GitHub and Google OAuth
- **CORS**: cors 2.8.5

#### **4. Logging & Monitoring**
- **Logging**: Winston 3.14.2
- **External Logging**: winston-logflare 0.1.1
- **File Rotation**: winston-daily-rotate-file 5.0.0

### **Actual Dependencies**

#### **Core Backend Libraries**
```json
{
  "dependencies": {
    "axios": "^1.10.0",
    "axios-retry": "^3.5.1",
    "bcryptjs": "^3.0.2",
    "body-parser": "^1.20.2",
    "cors": "^2.8.5",
    "crypto": "^1.0.1",
    "dotenv": "^16.4.5",
    "express": "^4.17.1",
    "jsonwebtoken": "^8.5.1",
    "passport": "^0.4.1",
    "passport-github": "^1.1.0",
    "passport-google-oauth20": "^2.0.0",
    "pg": "^8.5.1",
    "reflect-metadata": "^0.1.14",
    "tiktoken": "^1.0.16",
    "typeorm": "^0.2.45",
    "winston": "^3.14.2",
    "winston-daily-rotate-file": "^5.0.0",
    "winston-logflare": "^0.1.1",
    "winston-transport": "^4.7.1"
  }
}
```

#### **Development Dependencies**
```json
{
  "devDependencies": {
    "@types/axios": "^0.14.4",
    "@types/bcrypt": "^5.0.0",
    "@types/cors": "^2.8.9",
    "@types/express": "^4.17.9",
    "@types/jsonwebtoken": "^8.5.9",
    "@types/node": "^14.14.14",
    "@types/passport": "^1.0.11",
    "@types/passport-github": "^1.1.7",
    "@types/passport-google-oauth20": "^2.0.11",
    "@types/winston": "^2.4.4",
    "dotenv-safe": "^8.2.0",
    "nodemon": "^2.0.6",
    "typescript": "^4.9.5"
  }
}
```

### **Backend Architecture Components**

#### **1. Server Setup**
```typescript
// index.ts
- Express server configuration
- Middleware setup
- Route registration
- Error handling
- Database connection
```

#### **2. Helper Modules**
```typescript
// helpers/
├── openai.ts              // OpenAI API integration
├── codebaseFiltering.ts   // File filtering logic
├── auth.ts                // Authentication middleware
├── mailerLite.ts          // Email service
├── middleware.ts          // Custom middleware
├── types.ts               // Type definitions
└── userManagement.ts      // User operations
```

#### **3. Data Models**
```typescript
// entities/
└── User.ts                // User data model
```

#### **4. Type Definitions**
```typescript
// types/
├── custom-logflare-transport.d.ts
├── env.d.ts
└── winston-logflare.d.ts
```

## 🔗 **Third-Party Integrations**

### **1. AI Services**
- **OpenAI API**: GPT-4o-mini for chat completions
- **Model**: gpt-4o-mini (128K context window)
- **Integration**: Direct API calls via axios
- **Token Counting**: tiktoken for accurate token estimation

### **2. Authentication Services**
- **JWT**: Stateless authentication with jsonwebtoken
- **OAuth Providers**: GitHub and Google OAuth via Passport
- **Password Security**: bcryptjs for password hashing
- **Session Management**: Server-side session tracking

### **3. Logging Services**
- **Logflare**: Centralized logging and monitoring
- **Winston**: Structured logging framework
- **Custom Transport**: Winston transport for Logflare
- **File Rotation**: Daily log file rotation

### **4. Database**
- **PostgreSQL**: Primary database
- **TypeORM**: Object-relational mapping
- **Connection Pooling**: Built-in PostgreSQL pooling

## 🛠️ **Development Tools**

### **1. Build Tools**
- **Frontend**: Rollup for Svelte bundling
- **Backend**: TypeScript compiler
- **Asset Management**: Webpack for static assets
- **Code Highlighting**: highlight.js for syntax highlighting

### **2. Code Quality**
- **Linting**: ESLint with TypeScript support
- **Type Checking**: TypeScript strict mode
- **Testing**: Mocha for testing
- **Git Hooks**: Pre-commit hooks for code quality

### **3. Development Environment**
- **Hot Reload**: Nodemon for backend
- **Live Reload**: Rollup watch mode for frontend
- **Environment Management**: dotenv for configuration
- **Debugging**: VS Code debugger integration

## 📦 **Deployment & Infrastructure**

### **1. Containerization**
- **Docker**: Containerized deployment
- **Docker Compose**: Multi-service orchestration
- **Dockerfile**: Optimized production images

### **2. Environment Management**
- **Development**: Local development setup
- **Staging**: Staging environment configuration
- **Production**: Production deployment setup
- **Environment Variables**: dotenv-safe for required env vars

### **3. Monitoring & Observability**
- **Health Checks**: Application health endpoints
- **Logging**: Structured logging with Winston and Logflare
- **Error Tracking**: Error reporting and alerting

## 🔒 **Security Considerations**

### **1. Authentication & Authorization**
- **JWT Tokens**: Secure token-based authentication
- **OAuth Integration**: GitHub and Google OAuth
- **Password Security**: bcryptjs hashing
- **CORS**: Cross-origin resource sharing

### **2. Data Protection**
- **Environment Variables**: Secure configuration management
- **API Keys**: Secure API key storage
- **Database Security**: PostgreSQL security best practices
- **Input Validation**: Request validation and sanitization

### **3. Network Security**
- **HTTPS**: Secure communication
- **Request Validation**: Input sanitization
- **Rate Limiting**: API usage control

## 📊 **Performance Optimization**

### **1. Frontend Optimization**
- **Code Splitting**: Dynamic imports
- **Tree Shaking**: Unused code elimination
- **Asset Optimization**: Compressed assets
- **Caching**: Browser caching strategies

### **2. Backend Optimization**
- **Database Indexing**: Optimized queries
- **Connection Pooling**: Efficient database connections
- **Caching**: Response caching
- **Compression**: Response compression

### **3. API Optimization**
- **Pagination**: Large dataset handling
- **Filtering**: Efficient data filtering
- **Rate Limiting**: API usage control
- **Response Optimization**: Minimal response payloads

## 🚀 **Future Technology Considerations**

### **1. Planned Upgrades**
- **Node.js**: Upgrade to latest LTS version
- **TypeScript**: Latest TypeScript features
- **Svelte**: Svelte 4+ features
- **Database**: Advanced PostgreSQL features

### **2. Potential Additions**
- **Redis**: Caching layer
- **GraphQL**: Alternative to REST
- **WebSockets**: Real-time features
- **Microservices**: Service decomposition

### **3. Monitoring Enhancements**
- **APM**: Application performance monitoring
- **Distributed Tracing**: Request tracing
- **Metrics**: Custom metrics collection
- **Alerting**: Automated alerting system

## 📋 **Technology Selection Rationale**

### **1. Frontend Choices**
- **Svelte**: Lightweight, fast, and developer-friendly
- **VS Code Extension**: Native IDE integration
- **TypeScript**: Type safety and better developer experience
- **Rollup**: Efficient bundling for extensions

### **2. Backend Choices**
- **Node.js**: JavaScript ecosystem consistency
- **Express.js**: Mature, well-documented framework
- **PostgreSQL**: Reliable, feature-rich database
- **TypeORM**: Type-safe database operations

### **3. Third-Party Services**
- **OpenAI**: Leading AI model provider
- **Logflare**: Modern logging solution
- **Passport**: Flexible authentication framework
- **JWT**: Stateless authentication standard

This tech stack provides a solid foundation for a scalable, maintainable, and feature-rich coding assistant that can handle the diverse needs of developers across all technologies and domains. 