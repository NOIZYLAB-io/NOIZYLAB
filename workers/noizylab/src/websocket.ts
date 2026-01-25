/**
 * ╔═══════════════════════════════════════════════════════════════════════════╗
 * ║                                                                           ║
 * ║   🔌 NOIZYLAB CLOUD AGENT - WEBSOCKET HANDLER                           ║
 * ║                                                                           ║
 * ║   Real-time bidirectional communication for streaming task results       ║
 * ║   Enterprise-grade WebSocket implementation with health checks           ║
 * ║                                                                           ║
 * ╚═══════════════════════════════════════════════════════════════════════════╝
 */

interface WebSocketMessage {
  type: "ping" | "pong" | "task" | "result" | "error" | "subscribe" | "unsubscribe";
  task_id?: string;
  task_type?: string;
  task_data?: Record<string, any>;
  result?: any;
  error?: string;
  channel?: string;
  timestamp: string;
}

interface WebSocketSession {
  id: string;
  connected_at: number;
  last_activity: number;
  subscriptions: Set<string>;
}

export class WebSocketHandler {
  private sessions: Map<string, WebSocketSession> = new Map();
  private taskHandlers: Record<string, (data: any) => Promise<any>>;
  
  constructor(taskHandlers: Record<string, (data: any) => Promise<any>>) {
    this.taskHandlers = taskHandlers;
  }
  
  /**
   * Handle WebSocket upgrade request
   */
  async handleUpgrade(request: Request): Promise<Response> {
    const upgradeHeader = request.headers.get("Upgrade");
    
    if (!upgradeHeader || upgradeHeader !== "websocket") {
      return new Response("Expected Upgrade: websocket", { status: 426 });
    }
    
    const webSocketPair = new WebSocketPair();
    const [client, server] = Object.values(webSocketPair);
    
    const sessionId = crypto.randomUUID();
    const session: WebSocketSession = {
      id: sessionId,
      connected_at: Date.now(),
      last_activity: Date.now(),
      subscriptions: new Set()
    };
    
    this.sessions.set(sessionId, session);
    
    server.accept();
    
    // Setup message handler
    server.addEventListener("message", async (event: MessageEvent) => {
      try {
        const message: WebSocketMessage = JSON.parse(event.data as string);
        await this.handleMessage(server, session, message);
      } catch (error) {
        this.sendError(server, "Invalid message format", error);
      }
    });
    
    // Setup close handler
    server.addEventListener("close", () => {
      this.sessions.delete(sessionId);
    });
    
    // Setup error handler
    server.addEventListener("error", (error: Event) => {
      console.error(`WebSocket error for session ${sessionId}:`, error);
      this.sessions.delete(sessionId);
    });
    
    // Send welcome message
    this.send(server, {
      type: "pong",
      result: {
        session_id: sessionId,
        message: "Connected to NOIZYLAB Cloud Agent WebSocket"
      },
      timestamp: new Date().toISOString()
    });
    
    // Start heartbeat
    this.startHeartbeat(server, session);
    
    return new Response(null, {
      status: 101,
      webSocket: client
    });
  }
  
  /**
   * Handle incoming WebSocket message
   */
  private async handleMessage(
    socket: WebSocket,
    session: WebSocketSession,
    message: WebSocketMessage
  ): Promise<void> {
    session.last_activity = Date.now();
    
    switch (message.type) {
      case "ping":
        this.send(socket, {
          type: "pong",
          timestamp: new Date().toISOString()
        });
        break;
        
      case "subscribe":
        if (message.channel) {
          session.subscriptions.add(message.channel);
          this.send(socket, {
            type: "result",
            result: { subscribed: message.channel },
            timestamp: new Date().toISOString()
          });
        }
        break;
        
      case "unsubscribe":
        if (message.channel) {
          session.subscriptions.delete(message.channel);
          this.send(socket, {
            type: "result",
            result: { unsubscribed: message.channel },
            timestamp: new Date().toISOString()
          });
        }
        break;
        
      case "task":
        if (!message.task_type || !message.task_data) {
          this.sendError(socket, "task_type and task_data required");
          return;
        }
        
        await this.handleTask(socket, message);
        break;
        
      default:
        this.sendError(socket, `Unknown message type: ${message.type}`);
    }
  }
  
  /**
   * Handle task execution
   */
  private async handleTask(socket: WebSocket, message: WebSocketMessage): Promise<void> {
    const taskId = message.task_id || crypto.randomUUID();
    const taskType = message.task_type!;
    const taskData = message.task_data!;
    
    try {
      // Send acknowledgment
      this.send(socket, {
        type: "result",
        task_id: taskId,
        result: { status: "processing" },
        timestamp: new Date().toISOString()
      });
      
      // Check if handler exists
      if (!this.taskHandlers[taskType]) {
        throw new Error(`Unknown task type: ${taskType}`);
      }
      
      // Execute task with streaming support
      const handler = this.taskHandlers[taskType];
      
      // For streaming tasks, we can send progress updates
      if (taskData.stream) {
        await this.handleStreamingTask(socket, taskId, handler, taskData);
      } else {
        const result = await handler(taskData);
        
        this.send(socket, {
          type: "result",
          task_id: taskId,
          result: { status: "completed", data: result },
          timestamp: new Date().toISOString()
        });
      }
    } catch (error) {
      this.send(socket, {
        type: "error",
        task_id: taskId,
        error: error instanceof Error ? error.message : "Task execution failed",
        timestamp: new Date().toISOString()
      });
    }
  }
  
  /**
   * Handle streaming task with progress updates
   */
  private async handleStreamingTask(
    socket: WebSocket,
    taskId: string,
    handler: (data: any) => Promise<any>,
    taskData: any
  ): Promise<void> {
    // Simulate streaming by sending progress updates
    const progressSteps = taskData.progress_steps || 5;
    
    for (let i = 1; i <= progressSteps; i++) {
      this.send(socket, {
        type: "result",
        task_id: taskId,
        result: {
          status: "streaming",
          progress: (i / progressSteps) * 100,
          step: i,
          total: progressSteps
        },
        timestamp: new Date().toISOString()
      });
      
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    
    // Execute final task
    const result = await handler(taskData);
    
    this.send(socket, {
      type: "result",
      task_id: taskId,
      result: { status: "completed", data: result },
      timestamp: new Date().toISOString()
    });
  }
  
  /**
   * Send message to WebSocket
   */
  private send(socket: WebSocket, message: Partial<WebSocketMessage>): void {
    try {
      socket.send(JSON.stringify(message));
    } catch (error) {
      console.error("Failed to send WebSocket message:", error);
    }
  }
  
  /**
   * Send error message
   */
  private sendError(socket: WebSocket, error: string, details?: any): void {
    this.send(socket, {
      type: "error",
      error,
      result: details ? { details: String(details) } : undefined,
      timestamp: new Date().toISOString()
    });
  }
  
  /**
   * Start heartbeat to keep connection alive
   */
  private startHeartbeat(socket: WebSocket, session: WebSocketSession): void {
    const heartbeatInterval = setInterval(() => {
      const now = Date.now();
      const idleTime = now - session.last_activity;
      
      // Close if idle for more than 5 minutes
      if (idleTime > 5 * 60 * 1000) {
        clearInterval(heartbeatInterval);
        socket.close(1000, "Idle timeout");
        this.sessions.delete(session.id);
        return;
      }
      
      // Send ping
      this.send(socket, {
        type: "ping",
        timestamp: new Date().toISOString()
      });
    }, 30000); // Every 30 seconds
  }
  
  /**
   * Broadcast message to all subscribed sessions
   */
  broadcast(channel: string, message: Partial<WebSocketMessage>): void {
    for (const [sessionId, session] of this.sessions) {
      if (session.subscriptions.has(channel)) {
        // Note: In production, you'd need to maintain socket references
        console.log(`Broadcasting to session ${sessionId} on channel ${channel}`);
      }
    }
  }
  
  /**
   * Get active session count
   */
  getSessionCount(): number {
    return this.sessions.size;
  }
  
  /**
   * Get session statistics
   */
  getStats(): {
    total_sessions: number;
    active_sessions: number;
    total_subscriptions: number;
  } {
    let totalSubscriptions = 0;
    let activeSessions = 0;
    const now = Date.now();
    
    for (const session of this.sessions.values()) {
      totalSubscriptions += session.subscriptions.size;
      if (now - session.last_activity < 60000) { // Active in last minute
        activeSessions++;
      }
    }
    
    return {
      total_sessions: this.sessions.size,
      active_sessions: activeSessions,
      total_subscriptions: totalSubscriptions
    };
  }
}

export default WebSocketHandler;
