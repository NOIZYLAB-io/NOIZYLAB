# Integration Guide for Changelog 3.25.0 Features

## Overview
This guide details the integration of Focus Chain, Auto Compact, and Deep Planning features from copy-from-cline changelog 3.25.0 into cline-main-2.

## Files Added
✅ **Completed:**
1. `/src/shared/FocusChainSettings.ts` - Focus chain configuration interface
2. `/src/shared/focus-chain-utils.ts` - Utility functions for focus chain
3. `/src/core/task/focus-chain/index.ts` - Main FocusChainManager class
4. `/src/core/task/focus-chain/file-utils.ts` - File handling for focus chains
5. `/src/core/task/focus-chain/utils.ts` - Focus chain parsing utilities
6. `/src/core/prompts/contextManagement.ts` - Auto-compact context management
7. Updated `/src/core/prompts/commands.ts` - Added deepPlanningToolResponse
8. Updated `/src/core/slash-commands/index.ts` - Added deep-planning command
9. Updated `/src/core/task/TaskState.ts` - Added focus chain state properties

## Remaining Integration Steps

### 1. Update Task/index.ts
The main task file needs several key integrations:

#### A. Add Focus Chain Manager Import and Initialization
```typescript
// Add to imports
import { FocusChainManager } from "./focus-chain"
import { DEFAULT_FOCUS_CHAIN_SETTINGS } from "@shared/FocusChainSettings"

// In constructor, after this.taskState = new TaskState()
this.focusChainManager = new FocusChainManager({
    taskId: this.taskId,
    taskState: this.taskState,
    mode: this.mode,
    context: this.context,
    cacheService: this.cacheService,
    postStateToWebview: this.postStateToWebview,
    say: this.say.bind(this),
    focusChainSettings: DEFAULT_FOCUS_CHAIN_SETTINGS // Or load from settings
})
```

#### B. Add Focus Chain Instructions to System Prompt
In the method that builds the system prompt, add:
```typescript
if (this.focusChainManager.shouldIncludeFocusChainInstructions()) {
    systemPrompt += this.focusChainManager.generateFocusChainInstructions()
}
```

#### C. Update Tool Response Handler
After processing tool responses, add:
```typescript
// After each tool execution
this.taskState.apiRequestCount++
this.taskState.apiRequestsSinceLastTodoUpdate++

// If tool has task_progress parameter
await this.focusChainManager.updateFCListFromToolResponse(taskProgress)
```

#### D. Add Auto-Compact Logic
When detecting context window issues:
```typescript
import { summarizeTask, continuationPrompt } from "@core/prompts/contextManagement"

// When context window is approaching limit
if (shouldCompactContext) {
    const summaryPrompt = summarizeTask(this.focusChainManager !== undefined)
    // Send summary prompt to model
    // Process response and compact conversation history
}
```

### 2. Update Telemetry Service
Add these methods to `/src/services/posthog/telemetry/TelemetryService.ts`:

```typescript
captureFocusChainListWritten(taskId: string) {
    // Telemetry tracking for focus chain list creation
}

captureFocusChainProgressFirst(taskId: string, totalItems: number) {
    // Track first progress list creation
}

captureFocusChainProgressUpdate(taskId: string, totalItems: number, completedItems: number) {
    // Track progress updates
}

captureFocusChainIncompleteOnCompletion(taskId: string, totalItems: number, completedItems: number, incompleteItems: number) {
    // Track incomplete items when task is marked complete
}
```

### 3. Update Feature Flags Service
Add to `/src/services/posthog/feature-flags/FeatureFlagsService.ts`:

```typescript
async getFocusChainEnabled(): Promise<boolean> {
    // Return feature flag status for focus chain
    return true // Or fetch from PostHog
}
```

### 4. Update WebView Components
The webview needs to handle the new `task_progress` message type:

```typescript
// In message handler
case "task_progress":
    // Display the focus chain checklist in the UI
    break
```

### 5. Settings Integration
Add focus chain settings to the extension settings:

```json
{
    "focusChain.enabled": {
        "type": "boolean",
        "default": true,
        "description": "Enable Focus Chain todo list feature"
    },
    "focusChain.remindInterval": {
        "type": "number",
        "default": 6,
        "description": "Number of messages before reminding about focus chain"
    }
}
```

## Testing Checklist

- [ ] Test `/deep-planning` slash command triggers planning mode
- [ ] Test focus chain todo list creation in Act mode
- [ ] Test todo list file watching and updates
- [ ] Test auto-compact when context window fills
- [ ] Test that existing API key logic remains intact
- [ ] Test that Sixth authentication still works
- [ ] Verify webview-ui displays todo lists correctly
- [ ] Test that hardcoded API key is not exposed

## Important Considerations

1. **Preserve cline-main-2 Logic**: 
   - Keep hardcoded API key implementation
   - Maintain Sixth authentication logic
   - Don't modify existing webview-ui structure

2. **Focus Chain Storage**:
   - Todo lists are stored in `.cline/tasks/[taskId]/focus_chain_taskid_[taskId].md`
   - Files are watched for external edits

3. **Auto Compact**:
   - Triggers when context window approaches limit
   - Preserves important context while removing older messages
   - Integrates with focus chain to maintain todo list state

4. **Deep Planning**:
   - Four-step structured planning process
   - Creates implementation_plan.md document
   - Integrates with focus chain for progress tracking

## Next Steps

1. Complete the Task/index.ts integration (most complex part)
2. Add telemetry methods (can be stubbed initially)
3. Update webview to display todo lists
4. Test all features thoroughly
5. Ensure no conflicts with cline-main-2 specific features

## Notes
- The focus chain manager is designed to be modular and shouldn't interfere with existing logic
- Auto-compact is optional and only triggers when needed
- Deep planning is a slash command that enhances planning mode