// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS v1 - Live Room Durable Object
// WebSocket room with video → audio → chat fallback
// Zero dead ends: always falls back to a working mode
// ═══════════════════════════════════════════════════════════════════════════

import { WSClientMessage, WSServerMessage, LiveMode } from './types';

interface Session {
  ws: WebSocket;
  role: 'client' | 'staff';
  joined_at: string;
}

interface RoomState {
  ticket_id: string;
  mode: LiveMode;
  created_at: string;
  messages: Array<{ from: string; text: string; ts: string }>;
}

export class LiveRoom {
  private state: DurableObjectState;
  private sessions: Map<string, Session> = new Map();
  private roomState: RoomState | null = null;
  
  constructor(state: DurableObjectState) {
    this.state = state;
  }
  
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    
    // Initialize room state if needed
    if (!this.roomState) {
      const stored = await this.state.storage.get<RoomState>('room');
      if (stored) {
        this.roomState = stored;
      } else {
        // New room - extract ticket_id from query
        const ticketId = url.searchParams.get('ticket_id') || 'unknown';
        this.roomState = {
          ticket_id: ticketId,
          mode: 'video',
          created_at: new Date().toISOString(),
          messages: [],
        };
        await this.state.storage.put('room', this.roomState);
      }
    }
    
    // Handle WebSocket upgrade
    if (request.headers.get('Upgrade') === 'websocket') {
      return this.handleWebSocket(request);
    }
    
    // REST endpoints for room management
    if (url.pathname.endsWith('/mode')) {
      return this.handleModeChange(request);
    }
    
    if (url.pathname.endsWith('/close')) {
      return this.handleClose();
    }
    
    if (url.pathname.endsWith('/status')) {
      return this.handleStatus();
    }
    
    return new Response('Not found', { status: 404 });
  }
  
  // ─────────────────────────────────────────────────────────────────────────
  // WebSocket Connection Handler
  // ─────────────────────────────────────────────────────────────────────────
  private async handleWebSocket(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const token = url.searchParams.get('token');
    const role = url.searchParams.get('role') as 'client' | 'staff';
    
    if (!token || !role) {
      return new Response('Missing token or role', { status: 400 });
    }
    
    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);
    
    this.state.acceptWebSocket(server);
    
    const sessionId = token;
    this.sessions.set(sessionId, {
      ws: server,
      role,
      joined_at: new Date().toISOString(),
    });
    
    // Notify others
    this.broadcast({
      type: 'user_joined',
      role,
    }, sessionId);
    
    // Send current room state to new user
    server.send(JSON.stringify({
      type: 'mode_changed',
      mode: this.roomState!.mode,
      reason: 'Current room mode',
    }));
    
    // Send chat history
    for (const msg of this.roomState!.messages.slice(-50)) {
      server.send(JSON.stringify({
        type: 'chat',
        from: msg.from,
        text: msg.text,
        ts: msg.ts,
      }));
    }
    
    return new Response(null, {
      status: 101,
      webSocket: client,
    });
  }
  
  // ─────────────────────────────────────────────────────────────────────────
  // WebSocket Message Handler
  // ─────────────────────────────────────────────────────────────────────────
  async webSocketMessage(ws: WebSocket, message: string | ArrayBuffer) {
    const sessionId = this.findSessionId(ws);
    if (!sessionId) return;
    
    const session = this.sessions.get(sessionId);
    if (!session) return;
    
    try {
      const data = JSON.parse(message as string) as WSClientMessage;
      
      switch (data.type) {
        case 'chat':
          await this.handleChat(sessionId, session, data.text);
          break;
          
        case 'mode_request':
          // Only staff can change mode
          if (session.role === 'staff') {
            await this.changeMode(data.mode, 'Staff requested mode change');
          }
          break;
          
        case 'signal':
          // WebRTC signaling - relay to other party
          this.relaySignal(sessionId, data);
          break;
          
        case 'ping':
          ws.send(JSON.stringify({ type: 'pong' }));
          break;
      }
    } catch (error) {
      ws.send(JSON.stringify({ type: 'error', message: 'Invalid message format' }));
    }
  }
  
  async webSocketClose(ws: WebSocket) {
    const sessionId = this.findSessionId(ws);
    if (!sessionId) return;
    
    const session = this.sessions.get(sessionId);
    if (session) {
      this.broadcast({
        type: 'user_left',
        role: session.role,
      }, sessionId);
      
      this.sessions.delete(sessionId);
    }
  }
  
  async webSocketError(ws: WebSocket, error: unknown) {
    console.error('WebSocket error:', error);
    this.webSocketClose(ws);
  }
  
  // ─────────────────────────────────────────────────────────────────────────
  // Chat Handler
  // ─────────────────────────────────────────────────────────────────────────
  private async handleChat(sessionId: string, session: Session, text: string) {
    const msg = {
      from: session.role,
      text: text.slice(0, 2000), // Limit message length
      ts: new Date().toISOString(),
    };
    
    // Store message
    this.roomState!.messages.push(msg);
    if (this.roomState!.messages.length > 500) {
      this.roomState!.messages = this.roomState!.messages.slice(-500);
    }
    await this.state.storage.put('room', this.roomState);
    
    // Broadcast to all
    this.broadcast({
      type: 'chat',
      from: msg.from,
      text: msg.text,
      ts: msg.ts,
    });
  }
  
  // ─────────────────────────────────────────────────────────────────────────
  // Mode Change (Fallback: video → audio → chat)
  // ─────────────────────────────────────────────────────────────────────────
  private async changeMode(newMode: LiveMode, reason: string) {
    const fallbackOrder: LiveMode[] = ['video', 'audio', 'chat'];
    const currentIndex = fallbackOrder.indexOf(this.roomState!.mode);
    const newIndex = fallbackOrder.indexOf(newMode);
    
    // Can only go down the fallback chain (or stay same)
    // video → audio → chat, never back up
    if (newIndex < currentIndex) {
      // Trying to go back up - not allowed
      return;
    }
    
    this.roomState!.mode = newMode;
    await this.state.storage.put('room', this.roomState);
    
    this.broadcast({
      type: 'mode_changed',
      mode: newMode,
      reason,
    });
  }
  
  // Auto-fallback when connection issues detected
  async triggerFallback(reason: string) {
    const fallbackOrder: LiveMode[] = ['video', 'audio', 'chat'];
    const currentIndex = fallbackOrder.indexOf(this.roomState!.mode);
    
    if (currentIndex < fallbackOrder.length - 1) {
      const nextMode = fallbackOrder[currentIndex + 1];
      await this.changeMode(nextMode, reason);
    }
  }
  
  // ─────────────────────────────────────────────────────────────────────────
  // WebRTC Signaling Relay
  // ─────────────────────────────────────────────────────────────────────────
  private relaySignal(fromSessionId: string, signal: { sdp?: string; ice?: string }) {
    // Relay to the other party
    for (const [id, session] of this.sessions) {
      if (id !== fromSessionId) {
        try {
          session.ws.send(JSON.stringify({
            type: 'signal',
            sdp: signal.sdp,
            ice: signal.ice,
          }));
        } catch {
          // Connection might be closed
        }
      }
    }
  }
  
  // ─────────────────────────────────────────────────────────────────────────
  // REST Handlers
  // ─────────────────────────────────────────────────────────────────────────
  private async handleModeChange(request: Request): Promise<Response> {
    const { mode, reason } = await request.json() as { mode: LiveMode; reason: string };
    await this.changeMode(mode, reason || 'Mode changed by staff');
    return new Response(JSON.stringify({ success: true, mode }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  private async handleClose(): Promise<Response> {
    this.broadcast({
      type: 'room_closed',
      reason: 'Session ended by staff',
    });
    
    // Close all connections
    for (const session of this.sessions.values()) {
      try {
        session.ws.close(1000, 'Room closed');
      } catch {
        // Already closed
      }
    }
    this.sessions.clear();
    
    return new Response(JSON.stringify({ success: true }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  private handleStatus(): Response {
    return new Response(JSON.stringify({
      mode: this.roomState?.mode,
      participants: Array.from(this.sessions.values()).map(s => ({
        role: s.role,
        joined_at: s.joined_at,
      })),
      message_count: this.roomState?.messages.length || 0,
    }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  // ─────────────────────────────────────────────────────────────────────────
  // Helpers
  // ─────────────────────────────────────────────────────────────────────────
  private broadcast(message: WSServerMessage, excludeSessionId?: string) {
    const payload = JSON.stringify(message);
    for (const [id, session] of this.sessions) {
      if (id !== excludeSessionId) {
        try {
          session.ws.send(payload);
        } catch {
          // Connection might be closed, will be cleaned up
        }
      }
    }
  }
  
  private findSessionId(ws: WebSocket): string | null {
    for (const [id, session] of this.sessions) {
      if (session.ws === ws) {
        return id;
      }
    }
    return null;
  }
}
