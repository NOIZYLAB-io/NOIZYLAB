# UnfoldAI Architecture Overview

## 🏗️ **System Architecture**

UnfoldAI is built as a **client-server architecture** with a VS Code extension frontend and a Node.js/TypeScript backend. The frontend communicates with the backend via REST APIs, and the backend handles all third-party service integrations including OpenAI API.

```
┌─────────────────┐    HTTP/WebSocket    ┌─────────────────┐
│   VS Code       │ ◄──────────────────► │   Backend API   │
│   Extension     │                      │   (Node.js)     │
│   (Svelte)      │                      │                 │
└─────────────────┘                      └─────────────────┘
                                                │
                                                │
                                                ▼
                                    ┌─────────────────┐
                                    │   Third-Party   │
                                    │   Services      │
                                    │                 │
                                    │ ┌─────────────┐ │
                                    │ │   OpenAI    │ │
                                    │ │   API       │ │
                                    │ └─────────────┘ │
                                    │                 │
                                    │ ┌─────────────┐ │
                                    │ │  Database   │ │
                                    │ │(PostgreSQL) │ │
                                    │ └─────────────┘ │
                                    │                 │
                                    │ ┌─────────────┐ │
                                    │ │  Logflare   │ │
                                    │ │  Logging    │ │
                                    │ └─────────────┘ │
                                    └─────────────────┘
```

## 🎯 **Core Components**

### **1. Frontend (VS Code Extension)**

#### **Technology Stack**
- **Framework**: Svelte 3.x
- **Language**: TypeScript
- **Build Tool**: Rollup
- **UI**: Custom components with Tailwind CSS
- **State Management**: Svelte stores
- **Extension API**: VS Code Extension API

#### **Key Components**
```typescript
// Main extension entry point
extension.ts
├── SidebarProvider.ts          // VS Code sidebar integration
├── webviews/
│   ├── components/
│   │   ├── Sidebar.svelte      // Main chat interface
│   │   ├── Node.svelte         // File tree component
│   │   └── Confetti.svelte     // Success animations
│   └── pages/
│       └── sidebar.ts          // Page routing
└── Services/
    ├── apiKeyManager.ts        // API key management
    ├── codeBaseService.ts      // Codebase operations
    └── monitorTerminalsService.ts // Terminal monitoring
```

### **2. Backend (Node.js API)**

#### **Technology Stack**
- **Runtime**: Node.js 18+
- **Framework**: Express.js
- **Language**: TypeScript
- **Database**: PostgreSQL
- **Authentication**: JWT
- **Logging**: Winston + Logflare
- **Third-Party APIs**: OpenAI API, MailerLite, etc.

#### **Key Components**
```typescript
// Main application structure
src/
├── index.ts                    // Express server setup
├── helpers/
│   ├── openai.ts              // OpenAI integration & token management
│   ├── codebaseFiltering.ts   // Intelligent file filtering
│   ├── auth.ts                // Authentication middleware
│   ├── mailerLite.ts          // Email service integration
│   └── middleware.ts          // Request processing
├── entities/
│   └── User.ts                // User data model
└── types/
    └── custom-logflare-transport.d.ts
```

## 🔄 **Data Flow Architecture**

### **1. Chat Request Flow**

```
User Input → Frontend Processing → Backend API → OpenAI API → Backend Processing → Frontend Display
     │              │                   │           │              │              │
     ▼              ▼                   ▼           ▼              ▼              ▼
1. Message        2. API Request       3. Backend  4. AI          5. Response    6. UI
   Creation         Preparation          Processing  Processing     Processing     Update
```

#### **Detailed Flow:**

1. **Frontend Processing**
   ```typescript
   // Sidebar.svelte
   async function sendMessage(message: string) {
       // 1. Add message to chat tab
       chatTabs[activeChat].messages.push({
           role: 'user',
           content: message,
           fullContent: message
       });
       
       // 2. Prepare API request to backend
       const requestBody = {
           prompt: message,
           messages: filterMessagesForAPI(chatTabs[activeChat].messages),
           codeSnippet: currentCodeSnippet,
           chatState: chatTabs[activeChat].state
       };
   }
   ```

2. **Backend Processing**
   ```typescript
   // index.ts - /Unfold/New/solution
   app.post('/Unfold/New/solution', async (req, res) => {
       // 1. Validate request and authenticate user
       const { prompt, messages, codeSnippet, chatState } = req.body;
       
       // 2. Manage token count
       await manageTokenCount(messages, chatState, maxTokensAllowed);
       
       // 3. Send to OpenAI API (backend handles this)
       const response = await sendOpenAIRequest(model, messages, apiKey, isPremium, chatState);
       
       // 4. Process OpenAI response and return to frontend
       res.json({
           data: response.data.choices[0].message.content,
           chatHistory: messages, // Full conversation context
           chatState: updatedChatState
       });
   });
   ```

### **2. Codebase Analysis Flow**

```
File Selection → Frontend Filtering Request → Backend Processing → File Content → Analysis → Training → Chat Context
      │                    │                       │               │           │           │           │
      ▼                    ▼                       ▼               ▼           ▼           ▼           ▼
1. Tree Node      2. API Request to      3. Intelligent   4. Frontend    5. Backend    6. Context   7. Future
   Collection      Backend                Filtering       File Reading   OpenAI Call   Storage      Queries
```

#### **Detailed Flow:**

1. **File Selection (Frontend)**
   ```typescript
   // Sidebar.svelte
   function collectFileNames(node: NewTreeItem, fileNames: string[]) {
       if (node.checked) {
           if (node.type === 'file') {
               fileNames.push(node.path);
           } else if (node.children) {
               node.children.forEach(child => collectFileNames(child, fileNames));
           }
       }
   }
   ```

2. **Backend Filtering**
   ```typescript
   // Backend: codebaseFiltering.ts
   export async function intelligentFileFiltering(filePaths: string[], maxTokens: number) {
       // 1. Analyze files with content
       const fileAnalysis = await analyzeFilesWithContent(filePaths, 'development-focused');
       
       // 2. Process large files through semantic chunking
       const processedFiles = await processLargeFiles(fileAnalysis, maxTokens);
       
       // 3. Calculate universal relevance scores
       const filesWithScores = await calculateAdvancedRelevanceScores(processedFiles);
       
       // 4. Select optimal files with advanced strategies
       return await selectFilesWithAdvancedStrategies(filesWithScores, maxTokens);
   }
   ```

3. **Frontend File Reading**
   ```typescript
   // Frontend: codeBaseService.ts
   async function extractFileContents(filePaths: string[]) {
       const fileContents = [];
       for (const path of filePaths) {
           try {
               const content = await vscode.workspace.fs.readFile(vscode.Uri.file(path));
               fileContents.push({
                   path,
                   content: content.toString()
               });
           } catch (error) {
               console.error(`Error reading file ${path}:`, error);
           }
       }
       return fileContents;
   }
   ```

## 🧠 **Intelligent Systems**

### **1. Token Management System**

#### **Priority-Based Message Removal**
```typescript
const getMessagePriority = (message: Message, index: number): number => {
    // System messages: Never removed (priority 0)
    if (message.role === 'system') return 0;
    
    // Early setup messages: High priority (priority 1)
    if (index < 5) return 1;
    
    // User messages: Higher priority than assistant (priority 2)
    const roleScore = message.role === 'user' ? 2 : 10;
    
    // Recency bonus: Newer messages get higher priority
    const recencyScore = Math.max(0, messages.length - index);
    
    // Length penalty: Very long messages get lower priority
    const lengthPenalty = Math.floor(message.content.length / 2000) * 3;
    
    // Code content bonus: Messages with code get priority boost
    const hasCode = message.content.includes('```') || 
                   message.content.includes('.ts') ||
                   message.content.includes('.js');
    const codeBonus = hasCode ? -2 : 0;
    
    return roleScore + recencyScore + lengthPenalty + codeBonus;
};
```

#### **Iterative Removal Process**
```typescript
// Process removals in priority order, handling index shifting correctly
for (const info of messageInfo) {
    if (info.priority === 0) continue; // Never remove system messages
    
    // Calculate actual index after previous removals
    const actualIndex = info.index - removedIndices.filter(removedIndex => removedIndex < info.index).length;
    
    // Remove the message
    messages.splice(actualIndex, 1);
    tokenCount -= info.tokens;
    removedIndices.push(info.index);
}
```

### **2. Universal File Filtering System**

#### **Multi-Strategy Selection**
```typescript
export async function selectFilesWithAdvancedStrategies(filesWithScores: FileWithScore[], maxTokens: number) {
    const sortedFiles = filesWithScores.sort((a, b) => b.relevanceScore - a.relevanceScore);
    
    // Strategy 1: Try to fit files within token limit
    let selectedFiles: FileWithScore[] = [];
    let currentTokens = 0;
    
    for (const file of sortedFiles) {
        if (currentTokens + file.estimatedTokens <= maxTokens) {
            selectedFiles.push(file);
            currentTokens += file.estimatedTokens;
        } else {
            // Strategy 2: For large files, try summary + key chunks
            if (file.isLargeFile && file.summary) {
                const summaryTokens = 200;
                const keyChunks = file.chunks?.slice(0, 2) || [];
                const chunksTokens = keyChunks.reduce((sum, chunk) => sum + chunk.tokens, 0);
                
                if (currentTokens + summaryTokens + chunksTokens <= maxTokens * 1.2) {
                    selectedFiles.push({
                        ...file,
                        estimatedTokens: summaryTokens + chunksTokens,
                        selectedChunks: keyChunks,
                        processingStrategy: 'summary-with-chunks'
                    });
                    currentTokens += summaryTokens + chunksTokens;
                    continue;
                }
            }
            
            // Strategy 3: Important file override (30% overage allowed)
            if (file.relevanceScore > 85) {
                const overage = (currentTokens + file.estimatedTokens - maxTokens) / maxTokens;
                if (overage <= 0.3) {
                    selectedFiles.push({
                        ...file,
                        processingStrategy: 'important-file-override'
                    });
                    currentTokens += file.estimatedTokens;
                    break;
                }
            }
        }
    }
    
    // Strategy 4: Emergency fallback
    if (selectedFiles.length === 0) {
        const topFile = sortedFiles[0];
        selectedFiles.push({
            ...topFile,
            processingStrategy: 'emergency-minimal'
        });
    }
    
    return selectedFiles;
}
```

## 🔐 **Security & Authentication**

### **1. JWT Authentication**
```typescript
// auth.ts
export function authenticateToken(req: Request, res: Response, next: NextFunction) {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    
    if (!token) {
        return res.sendStatus(401);
    }
    
    jwt.verify(token, JWT_SECRET, (err: any, user: any) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
}
```

### **2. Rate Limiting**
```typescript
// middleware.ts
export function addRequestTimeout(timeoutMs: number) {
    return (req: Request, res: Response, next: NextFunction) => {
        const timeout = setTimeout(() => {
            res.status(408).json({ error: 'Request timeout' });
        }, timeoutMs);
        
        res.on('finish', () => clearTimeout(timeout));
        next();
    };
}
```

## 📊 **Performance Optimization**

### **1. Caching Strategy**
- **File Content Caching**: Cache processed file content to avoid re-processing
- **Token Count Caching**: Cache token calculations for repeated content
- **Filter Results Caching**: Cache filtering results for similar file sets

### **2. Async Processing**
```typescript
// Parallel processing for better performance
const fileAnalysis = await Promise.all(
    filePaths.map(async (path) => {
        const content = await getFileContent(path);
        return analyzeFile(path, content);
    })
);
```

### **3. Memory Management**
- **Streaming**: Process large files in chunks
- **Garbage Collection**: Proper cleanup of temporary objects
- **Memory Limits**: Enforce memory limits for large operations

## 🔧 **Error Handling**

### **1. Graceful Degradation**
```typescript
try {
    await manageTokenCount(messages, chatState, maxTokensAllowed);
} catch (error) {
    console.error('Token management failed:', error.message);
    // Emergency fallback: keep only system and last user message
    if (messages.length > 2) {
        const systemMessage = messages.find((m: Message) => m.role === 'system');
        const lastUserMessage = messages.filter((m: Message) => m.role === 'user').pop();
        
        if (systemMessage && lastUserMessage) {
            messages.length = 0;
            messages.push(systemMessage, lastUserMessage);
        }
    }
}
```

### **2. Retry Logic**
```typescript
// Exponential backoff for API calls
async function retryWithBackoff<T>(fn: () => Promise<T>, maxRetries: number = 3): Promise<T> {
    for (let i = 0; i < maxRetries; i++) {
        try {
            return await fn();
        } catch (error) {
            if (i === maxRetries - 1) throw error;
            await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000));
        }
    }
    throw new Error('Max retries exceeded');
}
```

## 🚀 **Scalability Considerations**

### **1. Horizontal Scaling**
- **Stateless Design**: Backend is stateless for easy scaling
- **Load Balancing**: Ready for load balancer integration
- **Database Connection Pooling**: Efficient database connections

### **2. Vertical Scaling**
- **Memory Optimization**: Efficient memory usage patterns
- **CPU Optimization**: Parallel processing where possible
- **I/O Optimization**: Async operations and streaming

### **3. Future Enhancements**
- **Microservices**: Ready for service decomposition
- **Event-Driven**: Event-driven architecture for better scalability
- **Caching Layer**: Redis integration for better performance

## 📈 **Monitoring & Observability**

### **1. Structured Logging**
```typescript
logger.info(`[NewSolution] Request received`, {
    userId,
    clientIP,
    model,
    promptLength: prompt.length,
    messagesCount: messages.length,
    isCodebaseAnalysis,
    isPremium
});
```

### **2. Performance Metrics**
- **Response Times**: Track API response times
- **Token Usage**: Monitor token consumption patterns
- **Error Rates**: Track error frequencies and types
- **User Activity**: Monitor user engagement patterns

### **3. Health Checks**
```typescript
app.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        uptime: process.uptime(),
        memory: process.memoryUsage()
    });
});
```

This architecture provides a solid foundation for a scalable, maintainable, and feature-rich coding assistant that can handle the diverse needs of developers across all technologies and domains. 