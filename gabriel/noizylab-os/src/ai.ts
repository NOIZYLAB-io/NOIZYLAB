// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - AI Jobs
// Strict: persona(1) + tags(≤3) + question(≤1) + playbook(1) + calm(3 lines)
// ═══════════════════════════════════════════════════════════════════════════

import { PERSONAS, PLAYBOOKS, json } from './utils';

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
  question: string | null;
  playbook: string;
  calmMessage: string | string[];
  confidence: number;
}

type Env = {
  AI_BASE_URL?: string;
  AI_API_KEY?: string;
  AI?: Ai;
};

const SYSTEM_PROMPT = `You are a support triage AI. Analyze tickets and return JSON only.
Pick exactly 1 persona (P1-P12), 1-3 tags, 1 playbook (PB1-PB12).
PERSONAS: ${Object.entries(PERSONAS).map(([k,v])=>`${k}=${v}`).join(', ')}
TAGS: ${TAGS.join(', ')}
PLAYBOOKS: ${Object.entries(PLAYBOOKS).map(([k,v])=>`${k}=${v}`).join(', ')}
Respond with JSON: {"persona":"P1","tags":["TAG"],"question":"one question or null","playbook":"PB1","calmMessage":"3 lines max","confidence":0.8}`;

export async function aiTriage(env: Env, text: string): Promise<TriageResult> {
  // Try external AI API first (OpenAI-compatible)
  if (env.AI_BASE_URL && env.AI_API_KEY) {
    try {
      const r = await fetch(`${env.AI_BASE_URL}/chat/completions`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${env.AI_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'gpt-4o-mini',
          messages: [
            { role: 'system', content: SYSTEM_PROMPT },
            { role: 'user', content: text }
          ],
          max_tokens: 400,
          temperature: 0.3,
        }),
      });
      const data = await r.json() as any;
      const content = data?.choices?.[0]?.message?.content ?? '';
      return parseTriageResponse(content);
    } catch { /* fall through to Workers AI or default */ }
  }

  // Fallback to Workers AI binding
  if (env.AI) {
    try {
      const prompt = `${SYSTEM_PROMPT}\n\nTicket: ${text}`;
      const r = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', { prompt, max_tokens: 400 }) as { response: string };
      return parseTriageResponse(r.response);
    } catch { /* fall through to default */ }
  }

  return defaultTriage();
}

function parseTriageResponse(response: string): TriageResult {
  try {
    const m = response.match(/\{[\s\S]*\}/);
    if (!m) return defaultTriage();
    const j = JSON.parse(m[0]);
    return {
      persona: Object.keys(PERSONAS).includes(j.persona) ? j.persona : 'P11',
      tags: (j.tags || []).filter((t: string) => TAGS.includes(t)).slice(0, 3),
      question: j.question || j.next_question || null,
      playbook: Object.keys(PLAYBOOKS).includes(j.playbook) ? j.playbook : 'PB11',
      calmMessage: j.calmMessage || j.calm_message || 'We received your request.',
      confidence: Math.min(1, Math.max(0, j.confidence || 0.5))
    };
  } catch {
    return defaultTriage();
  }
}

function defaultTriage(): TriageResult {
  return {
    persona: 'P11',
    tags: [],
    question: 'Can you tell me more about what changed?',
    playbook: 'PB11',
    calmMessage: "We've received your request.\nA team member will review shortly.\nNo action needed.",
    confidence: 0.3
  };
}

export function aiOk(result: TriageResult) {
  return json({
    ok: true,
    persona: result.persona,
    tags: result.tags,
    question: result.question,
    playbook: result.playbook,
    calmMessage: result.calmMessage,
    confidence: result.confidence,
  });
}
