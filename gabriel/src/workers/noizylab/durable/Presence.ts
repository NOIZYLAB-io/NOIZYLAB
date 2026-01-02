// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Presence Durable Object
// Track who's online and their status
// ═══════════════════════════════════════════════════════════════════════════

interface User {
  id: string;
  name: string;
  role: 'client' | 'staff';
  status: 'online' | 'away' | 'busy';
  lastSeen: string;
  currentTicket?: string;
}

export class Presence {
  private state: DurableObjectState;
  private users: Map<string, User>;
  private connections: Map<WebSocket, string>;
  
  constructor(state: DurableObjectState) {
    this.state = state;
    this.users = new Map();
    this.connections = new Map();
    
    // Load persisted users (for staff presence)
    this.state.blockConcurrencyWhile(async () => {
      const stored = await this.state.storage.get<[string, User][]>('users');
      if (stored) {
        this.users = new Map(stored);
      }
    });
  }
  
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    
    // Handle WebSocket upgrade
    if (request.headers.get('Upgrade') === 'websocket') {
      return this.handleWebSocket(request);
    }
    
    // REST API
    switch (url.pathname) {
      case '/online':
        return this.getOnlineUsers();
      case '/staff':
        return this.getStaffStatus();
      case '/heartbeat':
        return this.handleHeartbeat(request);
      default:
        return new Response('Not found', { status: 404 });
    }
  }
  
  private async handleWebSocket(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const userId = url.searchParams.get('userId') || crypto.randomUUID();
    const name = url.searchParams.get('name') || 'Anonymous';
    const role = url.searchParams.get('role') as 'client' | 'staff' || 'client';
    
    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);
    
    this.state.acceptWebSocket(server);
    
    // Register user
    const user: User = {
      id: userId,
      name,
      role,
      status: 'online',
      lastSeen: new Date().toISOString(),
    };
    
    this.users.set(userId, user);
    this.connections.set(server, userId);
    
    // Persist staff users
    if (role === 'staff') {
      await this.persistUsers();
    }
    
    // Broadcast presence update
    this.broadcastPresence();
    
    // Send current presence to new user
    server.send(JSON.stringify({
      type: 'presence',
      users: this.getOnlineUsersList(),
    }));
    
    return new Response(null, {
      status: 101,
      webSocket: client,
    });
  }
  
  async webSocketMessage(ws: WebSocket, message: string | ArrayBuffer) {
    const userId = this.connections.get(ws);
    if (!userId) return;
    
    try {
      const data = JSON.parse(message as string);
      
      if (data.type === 'status') {
        const user = this.users.get(userId);
        if (user) {
          user.status = data.status;
          user.lastSeen = new Date().toISOString();
          this.users.set(userId, user);
          this.broadcastPresence();
        }
      }
      
      if (data.type === 'viewing') {
        const user = this.users.get(userId);
        if (user) {
          user.currentTicket = data.ticketId;
          this.users.set(userId, user);
          this.broadcastPresence();
        }
      }
      
      if (data.type === 'ping') {
        ws.send(JSON.stringify({ type: 'pong' }));
        const user = this.users.get(userId);
        if (user) {
          user.lastSeen = new Date().toISOString();
          this.users.set(userId, user);
        }
      }
      
    } catch (error) {
      console.error('Presence message error:', error);
    }
  }
  
  async webSocketClose(ws: WebSocket) {
    const userId = this.connections.get(ws);
    if (userId) {
      const user = this.users.get(userId);
      if (user) {
        // Keep staff in the list but mark as offline
        if (user.role === 'staff') {
          user.status = 'away';
          user.lastSeen = new Date().toISOString();
          this.users.set(userId, user);
          await this.persistUsers();
        } else {
          // Remove clients completely
          this.users.delete(userId);
        }
      }
      this.connections.delete(ws);
      this.broadcastPresence();
    }
  }
  
  async webSocketError(ws: WebSocket, error: unknown) {
    console.error('Presence WebSocket error:', error);
    this.webSocketClose(ws);
  }
  
  private broadcastPresence() {
    const presenceData = JSON.stringify({
      type: 'presence',
      users: this.getOnlineUsersList(),
    });
    
    for (const ws of this.connections.keys()) {
      try {
        ws.send(presenceData);
      } catch (error) {
        // Will be cleaned up on close
      }
    }
  }
  
  private getOnlineUsersList(): User[] {
    return Array.from(this.users.values())
      .filter(u => u.status !== 'away' || u.role === 'staff')
      .sort((a, b) => {
        // Staff first, then by name
        if (a.role !== b.role) return a.role === 'staff' ? -1 : 1;
        return a.name.localeCompare(b.name);
      });
  }
  
  private async persistUsers() {
    const staffUsers = Array.from(this.users.entries())
      .filter(([_, user]) => user.role === 'staff');
    await this.state.storage.put('users', staffUsers);
  }
  
  private getOnlineUsers(): Response {
    return new Response(JSON.stringify({
      users: this.getOnlineUsersList(),
      count: this.users.size,
    }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  private getStaffStatus(): Response {
    const staff = Array.from(this.users.values())
      .filter(u => u.role === 'staff');
    
    return new Response(JSON.stringify({
      staff,
      available: staff.filter(s => s.status === 'online').length,
      total: staff.length,
    }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  private async handleHeartbeat(request: Request): Promise<Response> {
    const { userId, status } = await request.json() as { userId: string; status?: string };
    
    const user = this.users.get(userId);
    if (user) {
      user.lastSeen = new Date().toISOString();
      if (status) user.status = status as 'online' | 'away' | 'busy';
      this.users.set(userId, user);
      
      if (user.role === 'staff') {
        await this.persistUsers();
      }
      
      return new Response(JSON.stringify({ success: true }));
    }
    
    return new Response(JSON.stringify({ success: false, error: 'User not found' }), {
      status: 404,
    });
  }
}
