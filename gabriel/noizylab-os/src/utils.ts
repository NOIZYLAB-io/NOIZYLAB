// NoizyLab OS - Utilities

export const PERSONAS: Record<string, string> = {
  P1: 'Frustrated Tech-Savvy',
  P2: 'Confused Beginner',
  P3: 'Impatient Executive',
  P4: 'Methodical Engineer',
  P5: 'Anxious First-Timer',
  P6: 'Demanding Power User',
  P7: 'Friendly Collaborator',
  P8: 'Silent Lurker',
  P9: 'Repeat Caller',
  P10: 'Escalation Risk',
  P11: 'Unknown',
  P12: 'VIP'
};

export const PLAYBOOKS: Record<string, string> = {
  PB1: 'Quick Fix',
  PB2: 'Deep Dive',
  PB3: 'Escalate',
  PB4: 'Document & Close',
  PB5: 'Follow-up Required',
  PB6: 'Training Opportunity',
  PB7: 'Hardware Replacement',
  PB8: 'Software Reinstall',
  PB9: 'Account Recovery',
  PB10: 'Security Incident',
  PB11: 'General Support',
  PB12: 'VIP Handling'
};

export function nowISO() {
  return new Date().toISOString();
}

export function randCode(len = 6) {
  const chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  let out = "";
  for (let i = 0; i < len; i++) out += chars[Math.floor(Math.random() * chars.length)];
  return out;
}

export async function sha256Hex(input: string): Promise<string> {
  const data = new TextEncoder().encode(input);
  const hash = await crypto.subtle.digest("SHA-256", data);
  return [...new Uint8Array(hash)].map(b => b.toString(16).padStart(2, "0")).join("");
}

export function json(data: any, status = 200, headers: Record<string, string> = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 
      "Content-Type": "application/json",
      "Cache-Control": "no-store",
      ...headers 
    },
  });
}

export function bad(status: number, message: string) {
  return json({ ok: false, error: message }, status);
}

export async function readJson(req: Request) {
  try { return await req.json(); } catch { return null; }
}

export async function verifyTurnstile(secret: string, token: string, ip?: string) {
  const body = new URLSearchParams();
  body.set("secret", secret);
  body.set("response", token);
  if (ip) body.set("remoteip", ip);

  const r = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
    method: "POST",
    body,
  });
  return (await r.json()) as { success: boolean; "error-codes"?: string[] };
}

export function getIP(req: Request) {
  return req.headers.get("CF-Connecting-IP") ?? undefined;
}
