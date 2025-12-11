# Token Management System Documentation

## 🎯 **Overview**

The Token Management System in UnfoldAI is a sophisticated solution designed to handle GPT-4o-mini's 128K token context window efficiently. It uses intelligent priority-based message removal to maintain conversation context while staying within token limits.

## 🏗️ **System Architecture**

### **Core Components**

```
Token Management System
├── Priority Calculator
├── Message Analyzer
├── Token Counter
├── Removal Engine
└── Context Preserver
```

### **Key Functions**

```typescript
// Main entry point
export async function manageTokenCount(
    messages: Message[], 
    chatState: ChatState, 
    promptMaxTokens: number
): Promise<void>

// Priority calculation
const getMessagePriority = (message: Message, index: number): number

// Token counting
export async function numTokensFromMessages(messages: Message[]): Promise<number>
```

## 🧠 **Priority Algorithm**

### **Priority Calculation Logic**

The system uses a **multi-factor priority scoring** approach that considers:

1. **Message Role** (Primary factor)
2. **Message Position** (Recency)
3. **Content Length** (Size penalty)
4. **Content Type** (Code detection)

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
                   message.content.includes('file:') ||
                   message.content.includes('.ts') ||
                   message.content.includes('.js') ||
                   message.content.includes('.py') ||
                   message.content.includes('.json');
    const codeBonus = hasCode ? -2 : 0;
    
    return roleScore + recencyScore + lengthPenalty + codeBonus;
};
```

### **Priority Levels Explained**

| Priority | Message Type | Removal Order | Reasoning |
|----------|-------------|---------------|-----------|
| **0** | System Messages | Never | Essential for AI behavior |
| **1** | Early Setup (first 5) | Last | Important context |
| **2** | User Messages | Second to last | User intent preservation |
| **10** | Assistant Messages | First | Can be regenerated |
| **Variable** | Based on factors | Calculated | Dynamic prioritization |

## 🔄 **Removal Process**

### **Iterative Removal Algorithm**

```typescript
// 1. Calculate priorities for all messages
const messageInfo = await Promise.all(messages.map(async (message, index) => {
    const messageTokens = await numTokensFromMessages([message]);
    return {
        index,
        message,
        tokens: messageTokens,
        priority: getMessagePriority(message, index)
    };
}));

// 2. Sort by priority (ascending) and recency (descending)
messageInfo.sort((a, b) => {
    if (a.priority !== b.priority) {
        return a.priority - b.priority;
    }
    return b.index - a.index; // Remove older messages first
});

// 3. Remove messages iteratively with proper index management
let removedTokens = 0;
const removedIndices: number[] = [];

for (const info of messageInfo) {
    // Never remove system messages (priority 0)
    if (info.priority === 0) continue;
    
    // Check if removing this message would get us under the limit
    if (tokenCount - info.tokens <= promptMaxTokens) {
        break;
    }
    
    // Calculate actual index after previous removals
    const actualIndex = info.index - removedIndices.filter(removedIndex => removedIndex < info.index).length;
    
    // Remove the message
    messages.splice(actualIndex, 1);
    tokenCount -= info.tokens;
    removedTokens += info.tokens;
    removedIndices.push(info.index);
    
    console.log(`Removed message at original index ${info.index} (actual index ${actualIndex}, ${info.tokens} tokens, priority ${info.priority})`);
}
```

### **Index Management**

The system handles **array index shifting** correctly:

```typescript
// Problem: Array indices shift after each removal
// Solution: Track original indices and calculate actual positions

const actualIndex = info.index - removedIndices.filter(removedIndex => removedIndex < info.index).length;
```

**Example:**
```
Original: [A, B, C, D, E] (indices: 0,1,2,3,4)
Remove B (index 1): [A, C, D, E] (indices: 0,1,2,3)
Remove D (original index 3, actual index 2): [A, C, E] (indices: 0,1,2)
```

## 📊 **Token Counting**

### **Conservative Estimation**

```typescript
export async function numTokensFromMessages(messages: Message[], model: string = "gpt-4o-mini"): Promise<number> {
    let totalTokens = 0;
    
    for (const message of messages) {
        // Conservative estimate: 4 characters per token
        const estimatedTokens = Math.ceil(message.content.length / 4);
        totalTokens += estimatedTokens;
        
        // Add overhead for message structure
        totalTokens += 4; // Role, content, etc.
    }
    
    return totalTokens;
}
```

### **Token Limits**

```typescript
// Constants for token management
export const MODEL_MAX_TOKENS_GPT4_MINI_128K = 128000;
export const MAX_TOKENS_REQUEST = 80000;
export const MAX_TOKENS_RESPONSE = 4000;

// Calculate available tokens for prompt
const maxTokensAllowed = MODEL_MAX_TOKENS_GPT4_MINI_128K - modelMaxTokensResponse;
```

## 🛡️ **Safety Mechanisms**

### **1. Emergency Fallback**

```typescript
// If token management fails, use emergency reduction
if (messages.length > 2) {
    console.warn('Attempting emergency message reduction...');
    const systemMessage = messages.find((m: Message) => m.role === 'system');
    const lastUserMessage = messages.filter((m: Message) => m.role === 'user').pop();
    
    if (systemMessage && lastUserMessage) {
        messages.length = 0; // Clear array
        messages.push(systemMessage, lastUserMessage);
        console.log('Emergency reduction: keeping only system and last user message');
    }
}
```

### **2. Final Verification**

```typescript
// Verify we're under the limit after all reductions
const finalTokenCount = await numTokensFromMessages(messages);
if (finalTokenCount > promptMaxTokens) {
    console.error(`CRITICAL: Token count still exceeds limit after all reductions: ${finalTokenCount}/${promptMaxTokens}`);
    throw new Error(`Token count exceeds maximum allowed: ${finalTokenCount}/${promptMaxTokens}`);
}
```

### **3. Context Length Exceeded Handling**

```typescript
try {
    const response = await axios.post('https://api.openai.com/v1/chat/completions', data, { headers });
    return response;
} catch (error) {
    if (error.response?.status === 400 && error.response?.data?.error?.code === 'context_length_exceeded') {
        console.error('Context length exceeded even after token management');
        throw new Error('Request too large even after optimization. Please try with a shorter message or smaller codebase.');
    }
    throw error;
}
```

## 📈 **Performance Optimization**

### **1. Parallel Token Counting**

```typescript
// Calculate tokens for all messages in parallel
const messageInfo = await Promise.all(messages.map(async (message, index) => {
    const messageTokens = await numTokensFromMessages([message]);
    return {
        index,
        message,
        tokens: messageTokens,
        priority: getMessagePriority(message, index)
    };
}));
```

### **2. Early Termination**

```typescript
// Stop processing if already under limit
if (tokenCount <= promptMaxTokens) {
    console.log(`Token count within limits: ${tokenCount}/${promptMaxTokens}`);
    return;
}
```

### **3. Efficient Sorting**

```typescript
// Sort by priority first, then by index for same priority
messageInfo.sort((a, b) => {
    if (a.priority !== b.priority) {
        return a.priority - b.priority;
    }
    return b.index - a.index; // Remove older messages first
});
```

## 🔍 **Debugging & Monitoring**

### **1. Detailed Logging**

```typescript
console.log(`Initial token count: ${tokenCount}`);
console.log(`Need to reduce by ${tokensToReduce} tokens`);
console.log(`Removed message at original index ${info.index} (actual index ${actualIndex}, ${info.tokens} tokens, priority ${info.priority})`);
console.log(`Final token count: ${finalTokenCount}/${promptMaxTokens}`);
console.log(`Total tokens removed: ${removedTokens}`);
console.log(`Removed message indices: ${removedIndices.join(', ')}`);
```

### **2. Performance Metrics**

```typescript
// Track performance metrics
const startTime = Date.now();
await manageTokenCount(messages, chatState, maxTokensAllowed);
const processingTime = Date.now() - startTime;

console.log(`Token management completed in ${processingTime}ms`);
```

### **3. Token Usage Analytics**

```typescript
// Log token usage patterns
logger.info(`Total Tokens Used: ${totalTokensUsed}, UserId ${userId}`, {
    timestamp: new Date().toISOString(),
    userId,
    totalTokensUsed,
    messageCount: messages.length,
    averageTokensPerMessage: totalTokensUsed / messages.length
});
```

## 🎯 **Use Cases**

### **1. Long Conversations**

**Scenario**: User has been chatting for hours, accumulated 200+ messages
**Solution**: System intelligently removes older assistant messages while preserving user intent and recent context

### **2. Code-Heavy Discussions**

**Scenario**: User sharing large code snippets and getting detailed explanations
**Solution**: Code-containing messages get priority boost, ensuring important code context is preserved

### **3. Mixed Content Types**

**Scenario**: Combination of text, code, and system instructions
**Solution**: Priority system balances different content types appropriately

### **4. System Message Preservation**

**Scenario**: Complex system prompts with multiple instructions
**Solution**: System messages are never removed, ensuring AI behavior consistency

## 🚀 **Future Enhancements**

### **1. Semantic Chunking**

```typescript
// Future: Intelligent message chunking
async function chunkLargeMessage(message: Message): Promise<Message[]> {
    if (message.content.length < 4000) return [message];
    
    // Split by logical boundaries (paragraphs, code blocks)
    const chunks = splitByLogicalBoundaries(message.content);
    return chunks.map(chunk => ({
        ...message,
        content: chunk,
        isChunk: true,
        chunkIndex: chunks.indexOf(chunk)
    }));
}
```

### **2. Dynamic Priority Adjustment**

```typescript
// Future: Context-aware priority adjustment
function adjustPriorityBasedOnContext(message: Message, conversationContext: ConversationContext): number {
    let priority = getMessagePriority(message, message.index);
    
    // Boost messages related to current topic
    if (conversationContext.currentTopic && message.content.includes(conversationContext.currentTopic)) {
        priority -= 5;
    }
    
    // Boost messages with recent references
    if (conversationContext.recentReferences.some(ref => message.content.includes(ref))) {
        priority -= 3;
    }
    
    return Math.max(0, priority);
}
```

### **3. Predictive Token Management**

```typescript
// Future: Predict token usage before sending
async function predictTokenUsage(messages: Message[], newMessage: string): Promise<number> {
    const estimatedNewTokens = Math.ceil(newMessage.length / 4);
    const currentTokens = await numTokensFromMessages(messages);
    
    return currentTokens + estimatedNewTokens;
}
```

## 📋 **Best Practices**

### **1. Priority Design**

- **Never remove system messages**: Essential for AI behavior
- **Preserve user intent**: User messages have high priority
- **Balance recency and importance**: Recent messages matter more
- **Consider content type**: Code and configuration get priority

### **2. Error Handling**

- **Graceful degradation**: Emergency fallback mechanisms
- **Clear error messages**: Help users understand limitations
- **Logging**: Comprehensive logging for debugging
- **Validation**: Verify results after processing

### **3. Performance**

- **Parallel processing**: Use Promise.all for efficiency
- **Early termination**: Stop when limits are met
- **Efficient algorithms**: Optimize sorting and removal
- **Memory management**: Clean up temporary data

### **4. Monitoring**

- **Token usage tracking**: Monitor consumption patterns
- **Performance metrics**: Track processing times
- **Error rates**: Monitor failure frequencies
- **User feedback**: Collect user satisfaction data

This token management system provides a robust, efficient, and intelligent solution for handling large conversations while maintaining context quality and system performance. 