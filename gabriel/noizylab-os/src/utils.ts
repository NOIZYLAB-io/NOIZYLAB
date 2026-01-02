// NoizyLab OS - Utilities

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
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "Content-Type": "application/json", ...headers },
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
