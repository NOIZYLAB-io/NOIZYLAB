// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB CLI - HTTP Client
// ═══════════════════════════════════════════════════════════════════════════

import { error } from './util.js';

const API = process.env.NOIZYLAB_API || 'http://localhost:8787';
const STAFF_TOKEN = process.env.STAFF_TOKEN || '';

type Method = 'GET' | 'POST' | 'PATCH' | 'DELETE';

interface ApiResponse<T = any> {
  ok: boolean;
  error?: string;
  [key: string]: any;
}

export async function api<T = any>(
  path: string,
  method: Method = 'GET',
  body?: any,
  headers: Record<string, string> = {}
): Promise<ApiResponse<T>> {
  const url = `${API}${path}`;
  
  const opts: RequestInit = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...(STAFF_TOKEN ? { 'Authorization': `Bearer ${STAFF_TOKEN}` } : {}),
      ...headers,
    },
  };

  if (body && method !== 'GET') {
    opts.body = JSON.stringify(body);
  }

  try {
    const r = await fetch(url, opts);
    const data = await r.json() as ApiResponse<T>;
    return data;
  } catch (e: any) {
    error(`API Error: ${e.message}`);
    return { ok: false, error: e.message };
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// PUBLIC ENDPOINTS
// ─────────────────────────────────────────────────────────────────────────────

export async function createTicket(subject: string, channel = 'cli', turnstileToken = 'cli-bypass') {
  return api('/public/tickets', 'POST', { subject, channel, turnstileToken });
}

export async function getTicketStatus(publicId: string, secret: string) {
  return api(`/public/status/${publicId}?secret=${secret}`);
}

export async function joinLiveByCode(code: string, name = 'CLI User') {
  return api('/public/live/join', 'POST', { code });
}

export async function joinRtkByCode(code: string, name = 'CLI User') {
  return api('/public/rtk/join', 'POST', { code, name });
}

// ─────────────────────────────────────────────────────────────────────────────
// STAFF ENDPOINTS
// ─────────────────────────────────────────────────────────────────────────────

export async function listTickets(status = 'TRIAGE') {
  return api(`/staff/tickets?status=${status}`);
}

export async function setTicketStatus(ticketId: number, status: string) {
  return api(`/staff/tickets/${ticketId}/status`, 'PATCH', { status });
}

export async function createLiveRoom(ticketId?: number) {
  return api('/staff/live/create', 'POST', { ticketId });
}

export async function startRtkSession(ticketId?: number, staffName = 'Staff') {
  return api('/staff/rtk/start', 'POST', { ticketId, staffName });
}

// ─────────────────────────────────────────────────────────────────────────────
// AI ENDPOINTS (Staff)
// ─────────────────────────────────────────────────────────────────────────────

export async function aiTriage(ticketId: number, text: string) {
  return api('/staff/ai/triage', 'POST', { ticketId, text });
}

export async function aiNextQuestion(ticketId: number, context: string) {
  return api('/staff/ai/next-question', 'POST', { ticketId, context });
}

export async function aiLiveNotes(ticketId: number, transcript: string) {
  return api('/staff/ai/live-notes', 'POST', { ticketId, transcript });
}

// ─────────────────────────────────────────────────────────────────────────────
// CONSENT ENDPOINTS (to be wired)
// ─────────────────────────────────────────────────────────────────────────────

export async function grantConsent(ticketId: number, scope: string[]) {
  return api('/staff/consent/grant', 'POST', { ticketId, scope });
}

export async function revokeConsent(ticketId: number) {
  return api('/staff/consent/revoke', 'POST', { ticketId });
}

export async function getConsentStatus(ticketId: number) {
  return api(`/staff/consent/${ticketId}`);
}

// ─────────────────────────────────────────────────────────────────────────────
// RETENTION ENDPOINTS (to be wired)
// ─────────────────────────────────────────────────────────────────────────────

export async function setRetention(ticketId: number, days: number) {
  return api('/staff/retention/set', 'POST', { ticketId, days });
}

export async function deleteTicketData(ticketId: number) {
  return api('/staff/retention/delete', 'POST', { ticketId });
}

// ─────────────────────────────────────────────────────────────────────────────
// ESTIMATE / PAYMENT ENDPOINTS (stubs)
// ─────────────────────────────────────────────────────────────────────────────

export async function sendEstimate(ticketId: number, items: { desc: string; amount: number }[]) {
  return api('/staff/billing/estimate', 'POST', { ticketId, items });
}

export async function approveEstimate(ticketId: number, estimateId: string) {
  return api('/public/billing/approve', 'POST', { ticketId, estimateId });
}

export async function recordPayment(ticketId: number, amount: number, method: string) {
  return api('/staff/billing/payment', 'POST', { ticketId, amount, method });
}

// ─────────────────────────────────────────────────────────────────────────────
// CONTROL LANE ENDPOINTS (stubs)
// ─────────────────────────────────────────────────────────────────────────────

export async function requestControl(ticketId: number, type: 'view' | 'control') {
  return api('/staff/control/request', 'POST', { ticketId, type });
}

export async function grantControlConsent(ticketId: number, type: 'view' | 'control', durationMinutes = 15) {
  return api('/public/control/grant', 'POST', { ticketId, type, durationMinutes });
}

export async function endControl(ticketId: number) {
  return api('/staff/control/end', 'POST', { ticketId });
}

// ─────────────────────────────────────────────────────────────────────────────
// PLAYBOOK ENDPOINTS (to be wired)
// ─────────────────────────────────────────────────────────────────────────────

export async function listPlaybooks() {
  return api('/staff/playbooks');
}

export async function getPlaybook(playbookId: string) {
  return api(`/staff/playbooks/${playbookId}`);
}

export async function applyPlaybook(ticketId: number, playbookId: string) {
  return api('/staff/playbooks/apply', 'POST', { ticketId, playbookId });
}
