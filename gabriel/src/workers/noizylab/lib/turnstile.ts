// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Turnstile Verification
// Bot protection for public endpoints
// ═══════════════════════════════════════════════════════════════════════════

interface TurnstileResponse {
  success: boolean;
  'error-codes'?: string[];
  challenge_ts?: string;
  hostname?: string;
}

export async function verifyTurnstile(
  token: string,
  secretKey: string,
  ip?: string
): Promise<boolean> {
  if (!token || !secretKey) {
    console.warn('Turnstile: Missing token or secret');
    return false;
  }
  
  try {
    const formData = new FormData();
    formData.append('secret', secretKey);
    formData.append('response', token);
    if (ip) {
      formData.append('remoteip', ip);
    }
    
    const response = await fetch(
      'https://challenges.cloudflare.com/turnstile/v0/siteverify',
      {
        method: 'POST',
        body: formData,
      }
    );
    
    const result: TurnstileResponse = await response.json();
    
    if (!result.success) {
      console.warn('Turnstile verification failed:', result['error-codes']);
    }
    
    return result.success;
    
  } catch (error) {
    console.error('Turnstile verification error:', error);
    return false;
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// Middleware for Hono
// ═══════════════════════════════════════════════════════════════════════════

import { Context, Next } from 'hono';

export function turnstileMiddleware(secretKeyEnvName = 'TURNSTILE_SECRET') {
  return async (c: Context, next: Next) => {
    const token = c.req.header('X-Turnstile-Token') || 
                  (await c.req.json().catch(() => ({}))).turnstileToken;
    
    if (!token) {
      return c.json({ error: 'Turnstile token required' }, 401);
    }
    
    const secretKey = (c.env as any)[secretKeyEnvName];
    const ip = c.req.header('CF-Connecting-IP');
    
    const valid = await verifyTurnstile(token, secretKey, ip);
    
    if (!valid) {
      return c.json({ error: 'Bot verification failed' }, 403);
    }
    
    await next();
  };
}
