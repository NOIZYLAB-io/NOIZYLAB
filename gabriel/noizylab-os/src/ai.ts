// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - AI Jobs
// Strict: persona(1) + tags(≤3) + question(≤1) + playbook(1) + calm(3 lines)
// ═══════════════════════════════════════════════════════════════════════════

import { PERSONAS, PLAYBOOKS } from './utils';

const TAGS = [
  'PERF-TABS','PERF-STARTUP','PERF-BACKGROUND','PERF-THERMAL','PERF-LOWRAM',
  'STOR-LOWDISK','STOR-DISKERRORS','STOR-EXTERNALDRIVE','FILE-PERMISSIONS','FILE-CORRUPTION',
  'SEC-PUP','SEC-BROWSERHIJACK','SEC-PHISH-ACCOUNT','SEC-AV-CONFLICT',
  'AUTH-APPLEID','AUTH-MICROSOFT','AUTH-GOOGLE','AUTH-MFA','AUTH-PASSWORDRESET',
  'NET-WIFIDROP','NET-DNS','NET-ROUTER','NET-VPN',
  'UPD-OS','UPD-APP','DRV-PRINTER','DRV-USB','DRV-GPU','DRV-AUDIO',
  'SYNC-ICLOUD','SYNC-ONEDRIVE','SYNC-GDRIVE','SYNC-DUPES',
  'HW-SSD','HW-RAM','HW-BATTERY','HW-DUSTFAN','HW-LIQUID',
  'USR-CLICKYES','USR-NOBACKUP','USR-UPDATEAVOID','USR-DOWNLOADSCHAOS','USR-PASSWORDCHAOS'
];

export interface TriageResult {
  persona: string;
  tags: string[];
  next_question: string | null;
  playbook: string;
  calm_message: string;
  confidence: number;
}

export interface SummaryResult {
  summary: string;
  key_points: string[];
  next_steps: string[];
  sentiment: 'positive' | 'neutral' | 'frustrated';
}

export async function triage(ai: Ai, subject: string, desc: string): Promise<TriageResult> {
  const prompt = `Analyze this support ticket. Pick exactly 1 persona (P1-P12), 1-3 tags, 1 playbook (PB1-PB12).

Subject: ${subject}
Description: ${desc}

PERSONAS: ${Object.entries(PERSONAS).map(([k,v])=>`${k}=${v}`).join(', ')}
TAGS: ${TAGS.join(', ')}
PLAYBOOKS: ${Object.entries(PLAYBOOKS).map(([k,v])=>`${k}=${v}`).join(', ')}

JSON only:
{"persona":"P1","tags":["TAG"],"next_question":"one question or null","playbook":"PB1","calm_message":"3 lines max","confidence":0.8}`;

  try {
    const r = await ai.run('@cf/meta/llama-3.1-8b-instruct', { prompt, max_tokens: 400 }) as { response: string };
    const m = r.response.match(/\{[\s\S]*\}/);
    if (!m) return defaultTriage();
    const j = JSON.parse(m[0]);
    return {
      persona: Object.keys(PERSONAS).includes(j.persona) ? j.persona : 'P11',
      tags: (j.tags||[]).filter((t:string) => TAGS.includes(t)).slice(0,3),
      next_question: j.next_question || null,
      playbook: Object.keys(PLAYBOOKS).includes(j.playbook) ? j.playbook : 'PB11',
      calm_message: (j.calm_message||'').split('\n').slice(0,3).join('\n').slice(0,500),
      confidence: Math.min(1, Math.max(0, j.confidence || 0.5))
    };
  } catch { return defaultTriage(); }
}

export async function summarize(ai: Ai, events: Array<{type:string;payload_json:string}>): Promise<SummaryResult> {
  const evts = events.map(e => `[${e.type}] ${e.payload_json}`).join('\n');
  const prompt = `Summarize this support session.

${evts}

JSON: {"summary":"3 sentences","key_points":["≤3"],"next_steps":["≤3"],"sentiment":"neutral"}`;

  try {
    const r = await ai.run('@cf/meta/llama-3.1-8b-instruct', { prompt, max_tokens: 300 }) as { response: string };
    const m = r.response.match(/\{[\s\S]*\}/);
    if (!m) return defaultSummary();
    const j = JSON.parse(m[0]);
    return {
      summary: (j.summary||'').slice(0,500),
      key_points: (j.key_points||[]).slice(0,3),
      next_steps: (j.next_steps||[]).slice(0,3),
      sentiment: ['positive','neutral','frustrated'].includes(j.sentiment) ? j.sentiment : 'neutral'
    };
  } catch { return defaultSummary(); }
}

function defaultTriage(): TriageResult {
  return {
    persona: 'P11', tags: [], next_question: 'Can you tell me more about what changed?',
    playbook: 'PB11', calm_message: "We've received your request.\nA team member will review shortly.\nNo action needed.", confidence: 0.3
  };
}

function defaultSummary(): SummaryResult {
  return { summary: 'Session in progress.', key_points: [], next_steps: ['Review details'], sentiment: 'neutral' };
}
