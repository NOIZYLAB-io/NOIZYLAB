/**
 * NoizyBridge API Endpoints
 * =========================
 * Centralized endpoint definitions.
 */

export const ENDPOINTS = {
  // Memory
  MEMORY_RECALL: (email) => `/memory/recall/${email}`,
  MEMORY_REMEMBER: "/memory/remember",
  
  // Client
  CLIENT_LOGIN: "/client/login",
  CLIENT_REGISTER: "/client/register",
  CLIENT_SESSIONS: (email) => `/client/sessions/${email}`,
  
  // Device / Omen
  OMEN_LIVE: "/remote/omen/live",
  OMEN_HEALTH: "/remote/omen/health",
  
  // AI Assistant
  ASSISTANT_LIVE: "/assistant/live",
  AI_EMOTION: "/ai/emotion",
  AI_PERSONA: (email) => `/ai/persona/${email}`,
  
  // Voice
  VOICE_TRANSCRIBE: "/voice/transcribe",
  VOICE_STATUS: "/voice/status",
  
  // Grid
  GRID_NODES: "/grid/nodes",
  GRID_HEALTH: "/grid/health",
  GRID_RUN: "/grid/run",
  
  // Sync
  SYNC_FLOW: "/sync/flow",
  SYNC_EMERGENCY: "/sync/emergency",
  
  // Shield
  SHIELD_ANALYZE: "/shield/analyze",
  
  // Deploy
  VERSION: "/deploy/version",
  CHECK_UPDATE: (version) => `/deploy/check/${version}`,
  
  // WebSocket
  WS_SYNC: "/ws/sync"
};

