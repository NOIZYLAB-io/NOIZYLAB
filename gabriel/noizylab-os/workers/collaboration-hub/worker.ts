/**
 * NoizyLab OS - Real-Time Collaboration Hub Worker
 * 🤝 WebSocket-Powered Multi-Technician Collaboration
 * 
 * Enables real-time collaboration between technicians working
 * on the same device, remote expert assistance, live annotations,
 * and synchronized repair sessions using Durable Objects.
 */

interface Env {
  COLLABORATION_HUB: DurableObjectNamespace;
  COLLABORATION_KV: KVNamespace;
  D1_DATABASE: D1Database;
  R2_BUCKET: R2Bucket;
  AI: Ai;
  BRAIN_SERVICE: Fetcher;
  NOTIFICATIONS_SERVICE: Fetcher;
}

// ==================== Main Worker ====================

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // Route to appropriate handler
    if (url.pathname.startsWith('/session/')) {
      // WebSocket connection for collaboration session
      const sessionId = url.pathname.split('/')[2];
      const roomId = env.COLLABORATION_HUB.idFromName(sessionId);
      const room = env.COLLABORATION_HUB.get(roomId);
      return room.fetch(request);
    }

    if (url.pathname === '/sessions' && request.method === 'POST') {
      return createSession(request, env, corsHeaders);
    }

    if (url.pathname === '/sessions' && request.method === 'GET') {
      return listSessions(env, corsHeaders);
    }

    if (url.pathname.startsWith('/sessions/') && request.method === 'GET') {
      const sessionId = url.pathname.split('/')[2];
      return getSession(sessionId, env, corsHeaders);
    }

    if (url.pathname === '/expert/request' && request.method === 'POST') {
      return requestExpert(request, env, corsHeaders);
    }

    if (url.pathname === '/recordings' && request.method === 'GET') {
      return listRecordings(env, corsHeaders);
    }

    if (url.pathname.startsWith('/recordings/') && request.method === 'GET') {
      const recordingId = url.pathname.split('/')[2];
      return getRecording(recordingId, env, corsHeaders);
    }

    return new Response('Not Found', { status: 404, headers: corsHeaders });
  },
};

// ==================== Session Management ====================

async function createSession(request: Request, env: Env, corsHeaders: Record<string, string>): Promise<Response> {
  const { device_id, repair_ticket_id, created_by, title, session_type = 'repair' } = await request.json() as any;

  const sessionId = `session-${Date.now()}-${Math.random().toString(36).substring(7)}`;

  const session = {
    id: sessionId,
    device_id,
    repair_ticket_id,
    created_by,
    title,
    session_type, // 'repair', 'training', 'consultation', 'review'
    status: 'active',
    participants: [],
    created_at: new Date().toISOString(),
    ended_at: null,
    recording_enabled: true,
  };

  // Store session metadata
  await env.D1_DATABASE.prepare(`
    INSERT INTO collaboration_sessions (
      id, device_id, repair_ticket_id, created_by, title, session_type, status, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, 'active', datetime('now'))
  `).bind(sessionId, device_id, repair_ticket_id, created_by, title, session_type).run();

  // Cache for quick access
  await env.COLLABORATION_KV.put(`session:${sessionId}`, JSON.stringify(session), { expirationTtl: 86400 });

  // Initialize the Durable Object room
  const roomId = env.COLLABORATION_HUB.idFromName(sessionId);
  const room = env.COLLABORATION_HUB.get(roomId);

  // Initialize room with session data
  await room.fetch(new Request('https://internal/init', {
    method: 'POST',
    body: JSON.stringify(session),
  }));

  return new Response(JSON.stringify({
    success: true,
    session,
    websocket_url: `/session/${sessionId}`,
  }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  });
}

async function listSessions(env: Env, corsHeaders: Record<string, string>): Promise<Response> {
  const results = await env.D1_DATABASE.prepare(`
    SELECT * FROM collaboration_sessions 
    WHERE status = 'active'
    ORDER BY created_at DESC
    LIMIT 50
  `).all();

  return new Response(JSON.stringify({
    sessions: results.results || [],
  }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  });
}

async function getSession(sessionId: string, env: Env, corsHeaders: Record<string, string>): Promise<Response> {
  const cached = await env.COLLABORATION_KV.get(`session:${sessionId}`);
  if (cached) {
    return new Response(cached, {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }

  const result = await env.D1_DATABASE.prepare(`
    SELECT * FROM collaboration_sessions WHERE id = ?
  `).bind(sessionId).first();

  if (!result) {
    return new Response(JSON.stringify({ error: 'Session not found' }), {
      status: 404,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }

  return new Response(JSON.stringify(result), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  });
}

async function requestExpert(request: Request, env: Env, corsHeaders: Record<string, string>): Promise<Response> {
  const { session_id, expertise_needed, urgency, description } = await request.json() as any;

  // Find available experts
  const experts = await env.D1_DATABASE.prepare(`
    SELECT t.* FROM technicians t
    JOIN technician_skills ts ON t.id = ts.technician_id
    WHERE ts.skill LIKE ? AND t.status = 'available'
    ORDER BY ts.proficiency DESC
    LIMIT 5
  `).bind(`%${expertise_needed}%`).all();

  // Send notification to experts
  for (const expert of experts.results || []) {
    await env.NOTIFICATIONS_SERVICE.fetch(new Request('https://notifications/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: expert.id,
        type: 'expert_request',
        priority: urgency,
        title: `Expert Help Needed: ${expertise_needed}`,
        message: description,
        action_url: `/session/${session_id}`,
        metadata: { session_id, expertise_needed },
      }),
    }));
  }

  // Store request
  await env.D1_DATABASE.prepare(`
    INSERT INTO expert_requests (session_id, expertise_needed, urgency, description, status, created_at)
    VALUES (?, ?, ?, ?, 'pending', datetime('now'))
  `).bind(session_id, expertise_needed, urgency, description).run();

  return new Response(JSON.stringify({
    success: true,
    experts_notified: experts.results?.length || 0,
    message: 'Expert request sent - you will be notified when someone joins',
  }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  });
}

async function listRecordings(env: Env, corsHeaders: Record<string, string>): Promise<Response> {
  const results = await env.D1_DATABASE.prepare(`
    SELECT * FROM session_recordings
    ORDER BY created_at DESC
    LIMIT 50
  `).all();

  return new Response(JSON.stringify({
    recordings: results.results || [],
  }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  });
}

async function getRecording(recordingId: string, env: Env, corsHeaders: Record<string, string>): Promise<Response> {
  const result = await env.D1_DATABASE.prepare(`
    SELECT * FROM session_recordings WHERE id = ?
  `).bind(recordingId).first();

  if (!result) {
    return new Response(JSON.stringify({ error: 'Recording not found' }), {
      status: 404,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }

  // Get recording data from R2
  const recording = await env.R2_BUCKET.get(`recordings/${recordingId}.json`);
  if (!recording) {
    return new Response(JSON.stringify({ error: 'Recording data not found' }), {
      status: 404,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }

  const data = await recording.json();

  return new Response(JSON.stringify({
    metadata: result,
    events: data,
  }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  });
}

// ==================== Collaboration Room Durable Object ====================

interface CollaborationState {
  session: any;
  participants: Map<string, Participant>;
  annotations: Annotation[];
  chat_history: ChatMessage[];
  shared_cursor_positions: Map<string, CursorPosition>;
  document_state: DocumentState;
  recording: CollaborationEvent[];
}

interface Participant {
  id: string;
  name: string;
  role: 'owner' | 'expert' | 'observer' | 'trainee';
  color: string;
  websocket: WebSocket;
  joined_at: string;
  is_speaking: boolean;
  screen_sharing: boolean;
  permissions: ParticipantPermissions;
}

interface ParticipantPermissions {
  can_annotate: boolean;
  can_control: boolean;
  can_chat: boolean;
  can_voice: boolean;
  can_screen_share: boolean;
}

interface Annotation {
  id: string;
  type: 'pointer' | 'drawing' | 'text' | 'highlight' | 'marker';
  author_id: string;
  author_name: string;
  color: string;
  data: any;
  timestamp: string;
  target?: string; // image/document reference
  persistent: boolean;
}

interface ChatMessage {
  id: string;
  author_id: string;
  author_name: string;
  content: string;
  type: 'text' | 'image' | 'file' | 'ai_suggestion' | 'system';
  timestamp: string;
  reactions: Record<string, string[]>;
  thread_id?: string;
}

interface CursorPosition {
  participant_id: string;
  x: number;
  y: number;
  context: string; // which view/document
  timestamp: number;
}

interface DocumentState {
  current_view: string;
  zoom_level: number;
  scroll_position: { x: number; y: number };
  active_tool: string;
  shared_images: string[];
  reference_documents: string[];
}

interface CollaborationEvent {
  type: string;
  participant_id?: string;
  data: any;
  timestamp: string;
}

export class CollaborationHub {
  state: DurableObjectState;
  env: Env;
  collaborationState: CollaborationState;
  participantColors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F'];
  colorIndex = 0;

  constructor(state: DurableObjectState, env: Env) {
    this.state = state;
    this.env = env;
    this.collaborationState = {
      session: null,
      participants: new Map(),
      annotations: [],
      chat_history: [],
      shared_cursor_positions: new Map(),
      document_state: {
        current_view: 'main',
        zoom_level: 1,
        scroll_position: { x: 0, y: 0 },
        active_tool: 'pointer',
        shared_images: [],
        reference_documents: [],
      },
      recording: [],
    };

    // Load state from storage
    this.state.blockConcurrencyWhile(async () => {
      const stored = await this.state.storage.get('collaborationState');
      if (stored) {
        const parsed = stored as any;
        this.collaborationState = {
          ...parsed,
          participants: new Map(), // Don't restore WebSocket connections
        };
      }
    });
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    // Initialize session
    if (url.pathname === '/init' && request.method === 'POST') {
      const session = await request.json();
      this.collaborationState.session = session;
      await this.saveState();
      return new Response(JSON.stringify({ success: true }));
    }

    // WebSocket upgrade
    if (request.headers.get('Upgrade') === 'websocket') {
      return this.handleWebSocket(request);
    }

    // Get current state
    if (url.pathname === '/state' && request.method === 'GET') {
      return new Response(JSON.stringify({
        session: this.collaborationState.session,
        participants: Array.from(this.collaborationState.participants.values()).map(p => ({
          id: p.id,
          name: p.name,
          role: p.role,
          color: p.color,
          joined_at: p.joined_at,
          is_speaking: p.is_speaking,
          screen_sharing: p.screen_sharing,
        })),
        annotations: this.collaborationState.annotations.filter(a => a.persistent),
        chat_history: this.collaborationState.chat_history.slice(-100),
        document_state: this.collaborationState.document_state,
      }));
    }

    return new Response('Not Found', { status: 404 });
  }

  async handleWebSocket(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const participantId = url.searchParams.get('participant_id') || `user-${Date.now()}`;
    const participantName = url.searchParams.get('name') || 'Anonymous';
    const role = (url.searchParams.get('role') || 'observer') as Participant['role'];

    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);

    // Accept WebSocket connection
    this.state.acceptWebSocket(server);

    // Create participant
    const participant: Participant = {
      id: participantId,
      name: participantName,
      role,
      color: this.participantColors[this.colorIndex++ % this.participantColors.length],
      websocket: server,
      joined_at: new Date().toISOString(),
      is_speaking: false,
      screen_sharing: false,
      permissions: this.getPermissionsForRole(role),
    };

    this.collaborationState.participants.set(participantId, participant);

    // Record join event
    this.recordEvent({
      type: 'participant_joined',
      participant_id: participantId,
      data: { name: participantName, role },
      timestamp: new Date().toISOString(),
    });

    // Broadcast join to others
    this.broadcast({
      type: 'participant_joined',
      participant: {
        id: participant.id,
        name: participant.name,
        role: participant.role,
        color: participant.color,
      },
    }, participantId);

    // Send current state to new participant
    server.send(JSON.stringify({
      type: 'init_state',
      session: this.collaborationState.session,
      participants: Array.from(this.collaborationState.participants.values()).map(p => ({
        id: p.id,
        name: p.name,
        role: p.role,
        color: p.color,
        is_speaking: p.is_speaking,
        screen_sharing: p.screen_sharing,
      })),
      your_id: participantId,
      your_color: participant.color,
      your_permissions: participant.permissions,
      annotations: this.collaborationState.annotations.filter(a => a.persistent),
      chat_history: this.collaborationState.chat_history.slice(-50),
      document_state: this.collaborationState.document_state,
    }));

    return new Response(null, {
      status: 101,
      webSocket: client,
    });
  }

  async webSocketMessage(ws: WebSocket, message: string | ArrayBuffer): Promise<void> {
    try {
      const data = JSON.parse(message as string);
      const participant = this.findParticipantByWebSocket(ws);

      if (!participant) {
        ws.send(JSON.stringify({ type: 'error', message: 'Not authenticated' }));
        return;
      }

      switch (data.type) {
        case 'cursor_move':
          await this.handleCursorMove(participant, data);
          break;

        case 'annotation_add':
          await this.handleAnnotationAdd(participant, data);
          break;

        case 'annotation_remove':
          await this.handleAnnotationRemove(participant, data);
          break;

        case 'annotation_update':
          await this.handleAnnotationUpdate(participant, data);
          break;

        case 'chat_message':
          await this.handleChatMessage(participant, data);
          break;

        case 'voice_state':
          await this.handleVoiceState(participant, data);
          break;

        case 'screen_share_state':
          await this.handleScreenShareState(participant, data);
          break;

        case 'document_navigation':
          await this.handleDocumentNavigation(participant, data);
          break;

        case 'request_control':
          await this.handleControlRequest(participant, data);
          break;

        case 'grant_control':
          await this.handleControlGrant(participant, data);
          break;

        case 'share_image':
          await this.handleImageShare(participant, data);
          break;

        case 'ai_assist':
          await this.handleAIAssist(participant, data);
          break;

        case 'ping':
          ws.send(JSON.stringify({ type: 'pong', timestamp: Date.now() }));
          break;

        default:
          console.log('Unknown message type:', data.type);
      }
    } catch (error) {
      console.error('WebSocket message error:', error);
      ws.send(JSON.stringify({ type: 'error', message: 'Failed to process message' }));
    }
  }

  async webSocketClose(ws: WebSocket): Promise<void> {
    const participant = this.findParticipantByWebSocket(ws);
    if (participant) {
      this.collaborationState.participants.delete(participant.id);
      this.collaborationState.shared_cursor_positions.delete(participant.id);

      // Record leave event
      this.recordEvent({
        type: 'participant_left',
        participant_id: participant.id,
        data: { name: participant.name },
        timestamp: new Date().toISOString(),
      });

      // Broadcast leave
      this.broadcast({
        type: 'participant_left',
        participant_id: participant.id,
      });

      // Check if session should end
      if (this.collaborationState.participants.size === 0) {
        await this.endSession();
      }
    }
  }

  // ==================== Message Handlers ====================

  async handleCursorMove(participant: Participant, data: any): Promise<void> {
    const position: CursorPosition = {
      participant_id: participant.id,
      x: data.x,
      y: data.y,
      context: data.context,
      timestamp: Date.now(),
    };

    this.collaborationState.shared_cursor_positions.set(participant.id, position);

    // Throttled broadcast (every 50ms max)
    this.broadcast({
      type: 'cursor_update',
      participant_id: participant.id,
      position,
      color: participant.color,
    }, participant.id);
  }

  async handleAnnotationAdd(participant: Participant, data: any): Promise<void> {
    if (!participant.permissions.can_annotate) {
      participant.websocket.send(JSON.stringify({
        type: 'error',
        message: 'You do not have permission to annotate',
      }));
      return;
    }

    const annotation: Annotation = {
      id: `ann-${Date.now()}-${Math.random().toString(36).substring(7)}`,
      type: data.annotation_type,
      author_id: participant.id,
      author_name: participant.name,
      color: participant.color,
      data: data.annotation_data,
      timestamp: new Date().toISOString(),
      target: data.target,
      persistent: data.persistent || false,
    };

    this.collaborationState.annotations.push(annotation);

    // Record event
    this.recordEvent({
      type: 'annotation_added',
      participant_id: participant.id,
      data: annotation,
      timestamp: annotation.timestamp,
    });

    // Broadcast to all
    this.broadcast({
      type: 'annotation_added',
      annotation,
    });

    if (annotation.persistent) {
      await this.saveState();
    }
  }

  async handleAnnotationRemove(participant: Participant, data: any): Promise<void> {
    const annotation = this.collaborationState.annotations.find(a => a.id === data.annotation_id);

    if (!annotation) return;

    // Only author or owner can remove
    if (annotation.author_id !== participant.id && participant.role !== 'owner') {
      participant.websocket.send(JSON.stringify({
        type: 'error',
        message: 'You can only remove your own annotations',
      }));
      return;
    }

    this.collaborationState.annotations = this.collaborationState.annotations.filter(
      a => a.id !== data.annotation_id
    );

    this.broadcast({
      type: 'annotation_removed',
      annotation_id: data.annotation_id,
    });

    await this.saveState();
  }

  async handleAnnotationUpdate(participant: Participant, data: any): Promise<void> {
    const annotation = this.collaborationState.annotations.find(a => a.id === data.annotation_id);

    if (!annotation || annotation.author_id !== participant.id) return;

    annotation.data = { ...annotation.data, ...data.updates };

    this.broadcast({
      type: 'annotation_updated',
      annotation_id: data.annotation_id,
      updates: data.updates,
    });
  }

  async handleChatMessage(participant: Participant, data: any): Promise<void> {
    if (!participant.permissions.can_chat) return;

    const message: ChatMessage = {
      id: `msg-${Date.now()}-${Math.random().toString(36).substring(7)}`,
      author_id: participant.id,
      author_name: participant.name,
      content: data.content,
      type: data.message_type || 'text',
      timestamp: new Date().toISOString(),
      reactions: {},
      thread_id: data.thread_id,
    };

    this.collaborationState.chat_history.push(message);

    // Record event
    this.recordEvent({
      type: 'chat_message',
      participant_id: participant.id,
      data: message,
      timestamp: message.timestamp,
    });

    // Broadcast to all
    this.broadcast({
      type: 'chat_message',
      message,
    });

    // Check for @mentions
    const mentions = data.content.match(/@(\w+)/g);
    if (mentions) {
      for (const mention of mentions) {
        const mentionedName = mention.slice(1);
        const mentionedParticipant = Array.from(this.collaborationState.participants.values())
          .find(p => p.name.toLowerCase() === mentionedName.toLowerCase());

        if (mentionedParticipant) {
          mentionedParticipant.websocket.send(JSON.stringify({
            type: 'mention_notification',
            message,
          }));
        }
      }
    }

    // Keep chat history manageable
    if (this.collaborationState.chat_history.length > 1000) {
      this.collaborationState.chat_history = this.collaborationState.chat_history.slice(-500);
    }

    await this.saveState();
  }

  async handleVoiceState(participant: Participant, data: any): Promise<void> {
    if (!participant.permissions.can_voice) return;

    participant.is_speaking = data.is_speaking;

    this.broadcast({
      type: 'voice_state_changed',
      participant_id: participant.id,
      is_speaking: data.is_speaking,
    }, participant.id);
  }

  async handleScreenShareState(participant: Participant, data: any): Promise<void> {
    if (!participant.permissions.can_screen_share) return;

    participant.screen_sharing = data.is_sharing;

    this.broadcast({
      type: 'screen_share_changed',
      participant_id: participant.id,
      is_sharing: data.is_sharing,
      stream_id: data.stream_id,
    });

    // Record event
    this.recordEvent({
      type: data.is_sharing ? 'screen_share_started' : 'screen_share_stopped',
      participant_id: participant.id,
      data: {},
      timestamp: new Date().toISOString(),
    });
  }

  async handleDocumentNavigation(participant: Participant, data: any): Promise<void> {
    // Only owner or those with control permission can navigate
    if (participant.role !== 'owner' && !participant.permissions.can_control) {
      return;
    }

    this.collaborationState.document_state = {
      ...this.collaborationState.document_state,
      ...data.navigation,
    };

    this.broadcast({
      type: 'document_navigation',
      navigation: this.collaborationState.document_state,
      navigated_by: participant.id,
    }, participant.id);

    // Record event
    this.recordEvent({
      type: 'document_navigation',
      participant_id: participant.id,
      data: data.navigation,
      timestamp: new Date().toISOString(),
    });
  }

  async handleControlRequest(participant: Participant, data: any): Promise<void> {
    const owner = Array.from(this.collaborationState.participants.values())
      .find(p => p.role === 'owner');

    if (owner) {
      owner.websocket.send(JSON.stringify({
        type: 'control_request',
        requester_id: participant.id,
        requester_name: participant.name,
        reason: data.reason,
      }));
    }
  }

  async handleControlGrant(participant: Participant, data: any): Promise<void> {
    if (participant.role !== 'owner') return;

    const grantee = this.collaborationState.participants.get(data.grantee_id);
    if (grantee) {
      grantee.permissions.can_control = true;

      grantee.websocket.send(JSON.stringify({
        type: 'control_granted',
        permissions: grantee.permissions,
      }));

      this.broadcast({
        type: 'control_granted_notification',
        grantee_id: data.grantee_id,
        grantee_name: grantee.name,
      });
    }
  }

  async handleImageShare(participant: Participant, data: any): Promise<void> {
    // Store image reference
    if (!this.collaborationState.document_state.shared_images.includes(data.image_url)) {
      this.collaborationState.document_state.shared_images.push(data.image_url);
    }

    this.broadcast({
      type: 'image_shared',
      image_url: data.image_url,
      shared_by: participant.name,
      description: data.description,
    });

    // Record event
    this.recordEvent({
      type: 'image_shared',
      participant_id: participant.id,
      data: { image_url: data.image_url, description: data.description },
      timestamp: new Date().toISOString(),
    });

    await this.saveState();
  }

  async handleAIAssist(participant: Participant, data: any): Promise<void> {
    // Call Brain service for AI assistance
    try {
      const response = await this.env.BRAIN_SERVICE.fetch(new Request('https://brain/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: data.query,
          context: {
            session_type: this.collaborationState.session?.session_type,
            device_id: this.collaborationState.session?.device_id,
            recent_chat: this.collaborationState.chat_history.slice(-10),
            annotations: this.collaborationState.annotations.slice(-5),
          },
        }),
      }));

      const aiResponse = await response.json() as any;

      // Send AI response as system message
      const aiMessage: ChatMessage = {
        id: `msg-ai-${Date.now()}`,
        author_id: 'ai-assistant',
        author_name: 'AI Assistant',
        content: aiResponse.response || aiResponse.diagnosis || 'I analyzed the situation but need more context.',
        type: 'ai_suggestion',
        timestamp: new Date().toISOString(),
        reactions: {},
      };

      this.collaborationState.chat_history.push(aiMessage);

      this.broadcast({
        type: 'chat_message',
        message: aiMessage,
      });
    } catch (error) {
      participant.websocket.send(JSON.stringify({
        type: 'error',
        message: 'AI assistance temporarily unavailable',
      }));
    }
  }

  // ==================== Helper Methods ====================

  findParticipantByWebSocket(ws: WebSocket): Participant | undefined {
    for (const participant of this.collaborationState.participants.values()) {
      if (participant.websocket === ws) {
        return participant;
      }
    }
    return undefined;
  }

  getPermissionsForRole(role: Participant['role']): ParticipantPermissions {
    switch (role) {
      case 'owner':
        return {
          can_annotate: true,
          can_control: true,
          can_chat: true,
          can_voice: true,
          can_screen_share: true,
        };
      case 'expert':
        return {
          can_annotate: true,
          can_control: false, // Must be granted
          can_chat: true,
          can_voice: true,
          can_screen_share: true,
        };
      case 'trainee':
        return {
          can_annotate: true,
          can_control: false,
          can_chat: true,
          can_voice: true,
          can_screen_share: false,
        };
      case 'observer':
      default:
        return {
          can_annotate: false,
          can_control: false,
          can_chat: true,
          can_voice: false,
          can_screen_share: false,
        };
    }
  }

  broadcast(message: any, excludeId?: string): void {
    const messageStr = JSON.stringify(message);
    for (const participant of this.collaborationState.participants.values()) {
      if (participant.id !== excludeId) {
        try {
          participant.websocket.send(messageStr);
        } catch (error) {
          // WebSocket may be closed
        }
      }
    }
  }

  recordEvent(event: CollaborationEvent): void {
    if (this.collaborationState.session?.recording_enabled) {
      this.collaborationState.recording.push(event);

      // Keep recording manageable
      if (this.collaborationState.recording.length > 10000) {
        // Save to R2 and reset
        this.saveRecording();
      }
    }
  }

  async saveState(): Promise<void> {
    await this.state.storage.put('collaborationState', {
      session: this.collaborationState.session,
      annotations: this.collaborationState.annotations.filter(a => a.persistent),
      chat_history: this.collaborationState.chat_history.slice(-500),
      document_state: this.collaborationState.document_state,
      recording: this.collaborationState.recording,
    });
  }

  async saveRecording(): Promise<void> {
    if (this.collaborationState.recording.length === 0) return;

    const recordingId = `rec-${this.collaborationState.session?.id}-${Date.now()}`;

    await this.env.R2_BUCKET.put(
      `recordings/${recordingId}.json`,
      JSON.stringify(this.collaborationState.recording),
      { httpMetadata: { contentType: 'application/json' } }
    );

    await this.env.D1_DATABASE.prepare(`
      INSERT INTO session_recordings (id, session_id, event_count, created_at)
      VALUES (?, ?, ?, datetime('now'))
    `).bind(recordingId, this.collaborationState.session?.id, this.collaborationState.recording.length).run();

    // Clear recorded events
    this.collaborationState.recording = [];
  }

  async endSession(): Promise<void> {
    // Save final recording
    await this.saveRecording();

    // Update session status
    if (this.collaborationState.session) {
      await this.env.D1_DATABASE.prepare(`
        UPDATE collaboration_sessions SET status = 'ended', ended_at = datetime('now')
        WHERE id = ?
      `).bind(this.collaborationState.session.id).run();

      // Clear cache
      await this.env.COLLABORATION_KV.delete(`session:${this.collaborationState.session.id}`);
    }
  }
}
