// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS v1 - Utility Functions
// ═══════════════════════════════════════════════════════════════════════════

// ───────────────────────────────────────────────────────────────────────────
// ID Generation
// ───────────────────────────────────────────────────────────────────────────
export function generateId(): string {
  return crypto.randomUUID();
}

export function generatePublicId(): string {
  // Format: NL-XXXXXX (6 alphanumeric chars)
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // No I,O,0,1 for clarity
  let id = 'NL-';
  for (let i = 0; i < 6; i++) {
    id += chars[Math.floor(Math.random() * chars.length)];
  }
  return id;
}

export function generateSecret(): string {
  // 32-char hex secret
  const bytes = new Uint8Array(16);
  crypto.getRandomValues(bytes);
  return Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('');
}

export function generateJoinCode(): string {
  // 6-digit code for live sessions
  return Math.floor(100000 + Math.random() * 900000).toString();
}

export function generateRoomToken(): string {
  // Short-lived token for WebSocket auth
  const bytes = new Uint8Array(24);
  crypto.getRandomValues(bytes);
  return btoa(String.fromCharCode(...bytes)).replace(/[+/=]/g, '');
}

// ───────────────────────────────────────────────────────────────────────────
// Hashing
// ───────────────────────────────────────────────────────────────────────────
export async function hashSecret(secret: string): Promise<string> {
  const encoder = new TextEncoder();
  const data = encoder.encode(secret);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

export async function verifySecret(secret: string, hash: string): Promise<boolean> {
  const computed = await hashSecret(secret);
  return computed === hash;
}

// ───────────────────────────────────────────────────────────────────────────
// Turnstile Verification
// ───────────────────────────────────────────────────────────────────────────
export async function verifyTurnstile(token: string, secretKey: string, ip?: string): Promise<boolean> {
  const formData = new FormData();
  formData.append('secret', secretKey);
  formData.append('response', token);
  if (ip) formData.append('remoteip', ip);
  
  const response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    method: 'POST',
    body: formData,
  });
  
  const result = await response.json() as { success: boolean };
  return result.success;
}

// ───────────────────────────────────────────────────────────────────────────
// Cloudflare Access Verification
// ───────────────────────────────────────────────────────────────────────────
export async function verifyAccess(request: Request, accessAud: string): Promise<{ valid: boolean; email?: string }> {
  const jwt = request.headers.get('Cf-Access-Jwt-Assertion');
  if (!jwt) return { valid: false };
  
  // Cloudflare Access automatically validates the JWT at the edge
  // We just need to extract the email from the claims
  try {
    const parts = jwt.split('.');
    if (parts.length !== 3) return { valid: false };
    
    const payload = JSON.parse(atob(parts[1]));
    
    // Verify audience matches
    if (payload.aud !== accessAud && !payload.aud?.includes(accessAud)) {
      return { valid: false };
    }
    
    return { valid: true, email: payload.email };
  } catch {
    return { valid: false };
  }
}

// ───────────────────────────────────────────────────────────────────────────
// Time Helpers
// ───────────────────────────────────────────────────────────────────────────
export function now(): string {
  return new Date().toISOString();
}

export function addMinutes(minutes: number): string {
  return new Date(Date.now() + minutes * 60 * 1000).toISOString();
}

export function isExpired(timestamp: string): boolean {
  return new Date(timestamp) < new Date();
}

// ───────────────────────────────────────────────────────────────────────────
// Response Helpers
// ───────────────────────────────────────────────────────────────────────────
export function json<T>(data: T, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    },
  });
}

export function error(message: string, status = 400): Response {
  return json({ error: message }, status);
}

export function notFound(message = 'Not found'): Response {
  return error(message, 404);
}

export function unauthorized(message = 'Unauthorized'): Response {
  return error(message, 401);
}

export function forbidden(message = 'Forbidden'): Response {
  return error(message, 403);
}

// ───────────────────────────────────────────────────────────────────────────
// Input Validation
// ───────────────────────────────────────────────────────────────────────────
export function validateEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export function sanitize(input: string, maxLength = 1000): string {
  // Trim, clamp length, and escape HTML to keep logs/emails safe
  const trimmed = String(input ?? '').trim().slice(0, maxLength);
  return trimmed
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function validatePhone(phone: string): boolean {
  // Basic phone validation (allows various formats)
  return /^[\d\s\-+()]{7,20}$/.test(phone);
}
