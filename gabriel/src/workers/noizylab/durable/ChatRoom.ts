// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Chat Room Durable Object
// Real-time chat for Live Help sessions
// ═══════════════════════════════════════════════════════════════════════════

interface Message {
  id: string;
  sender: 'client' | 'staff';
  senderId: string;
  content: string;
  timestamp: string;
  type: 'text' | 'system' | 'file';
  metadata?: Record<string, any>;
}

interface Session {
  clients: Map<WebSocket, { id: string; role: 'client' | 'staff'; name: string }>;
  messages: Message[];
  startedAt: string;
}

export class ChatRoom {
  private state: DurableObjectState;
  private session: Session;
  
  constructor(state: DurableObjectState) {
    this.state = state;
    this.session = {
      clients: new Map(),
      messages: [],
      startedAt: new Date().toISOString(),
    };
    
    // Load persisted messages
    this.state.blockConcurrencyWhile(async () => {
      const stored = await this.state.storage.get<Message[]>('messages');
      if (stored) {
        this.session.messages = stored;
      }
    });
  }
  
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    
    // Handle transcript request
    if (url.pathname === '/transcript') {
      return this.getTranscript();
    }
    
    // Handle WebSocket upgrade
    if (request.headers.get('Upgrade') === 'websocket') {
      return this.handleWebSocket(request);
    }
    
    // Handle REST API
    if (request.method === 'GET') {
      return this.handleGet(request);
    }
    
    if (request.method === 'POST') {
      return this.handlePost(request);
    }
    
    return new Response('Method not allowed', { status: 405 });
  }
  
  private async handleWebSocket(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const role = url.searchParams.get('role') as 'client' | 'staff' || 'client';
    const name = url.searchParams.get('name') || 'Anonymous';
    const id = url.searchParams.get('id') || crypto.randomUUID();
    
    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);
    
    // Accept the WebSocket
    this.state.acceptWebSocket(server);
    
    // Store client info
    this.session.clients.set(server, { id, role, name });
    
    // Send join message
    const joinMessage: Message = {
      id: crypto.randomUUID(),
      sender: 'staff',
      senderId: 'system',
      content: `${name} joined the session`,
      timestamp: new Date().toISOString(),
      type: 'system',
    };
    
    this.broadcast(joinMessage);
    
    // Send message history to new client
    server.send(JSON.stringify({
      type: 'history',
      messages: this.session.messages.slice(-50),
    }));
    
    return new Response(null, {
      status: 101,
      webSocket: client,
    });
  }
  
  async webSocketMessage(ws: WebSocket, message: string | ArrayBuffer) {
    const clientInfo = this.session.clients.get(ws);
    if (!clientInfo) return;
    
    try {
      const data = JSON.parse(message as string);
      
      if (data.type === 'message') {
        const chatMessage: Message = {
          id: crypto.randomUUID(),
          sender: clientInfo.role,
          senderId: clientInfo.id,
          content: data.content,
          timestamp: new Date().toISOString(),
          type: 'text',
          metadata: {
            senderName: clientInfo.name,
          },
        };
        
        // Store message
        this.session.messages.push(chatMessage);
        await this.state.storage.put('messages', this.session.messages);
        
        // Broadcast to all clients
        this.broadcast(chatMessage);
      }
      
      if (data.type === 'typing') {
        // Broadcast typing indicator to others
        this.broadcastExcept(ws, {
          type: 'typing',
          sender: clientInfo.name,
          role: clientInfo.role,
        });
      }
      
    } catch (error) {
      console.error('WebSocket message error:', error);
    }
  }
  
  async webSocketClose(ws: WebSocket, code: number, reason: string) {
    const clientInfo = this.session.clients.get(ws);
    if (clientInfo) {
      const leaveMessage: Message = {
        id: crypto.randomUUID(),
        sender: 'staff',
        senderId: 'system',
        content: `${clientInfo.name} left the session`,
        timestamp: new Date().toISOString(),
        type: 'system',
      };
      
      this.session.clients.delete(ws);
      this.broadcast(leaveMessage);
    }
  }
  
  async webSocketError(ws: WebSocket, error: unknown) {
    console.error('WebSocket error:', error);
    this.session.clients.delete(ws);
  }
  
  private broadcast(message: Message | object) {
    const data = JSON.stringify({ type: 'message', ...message });
    
    for (const ws of this.session.clients.keys()) {
      try {
        ws.send(data);
      } catch (error) {
        // Client disconnected, will be cleaned up
      }
    }
  }
  
  private broadcastExcept(exclude: WebSocket, data: object) {
    const json = JSON.stringify(data);
    
    for (const ws of this.session.clients.keys()) {
      if (ws !== exclude) {
        try {
          ws.send(json);
        } catch (error) {
          // Client disconnected
        }
      }
    }
  }
  
  private async handleGet(request: Request): Promise<Response> {
    return new Response(JSON.stringify({
      clientCount: this.session.clients.size,
      messageCount: this.session.messages.length,
      startedAt: this.session.startedAt,
    }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  private async handlePost(request: Request): Promise<Response> {
    const body = await request.json() as { action: string; content?: string };
    
    if (body.action === 'system-message') {
      const message: Message = {
        id: crypto.randomUUID(),
        sender: 'staff',
        senderId: 'system',
        content: body.content || '',
        timestamp: new Date().toISOString(),
        type: 'system',
      };
      
      this.session.messages.push(message);
      await this.state.storage.put('messages', this.session.messages);
      this.broadcast(message);
      
      return new Response(JSON.stringify({ success: true }));
    }
    
    return new Response('Unknown action', { status: 400 });
  }
  
  private getTranscript(): Response {
    // Build transcript from messages
    const transcript = this.session.messages
      .filter(m => m.type === 'text')
      .map(m => `[${m.sender}] ${m.metadata?.senderName || 'Unknown'}: ${m.content}`)
      .join('\n');
    
    return new Response(JSON.stringify({ transcript }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
