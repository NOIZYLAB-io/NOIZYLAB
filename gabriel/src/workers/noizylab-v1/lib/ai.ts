// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS v1 - AI Jobs
// Strict outputs: persona(1) + tags(≤3) + question(≤1) + playbook(1) + calm(3 lines)
// ═══════════════════════════════════════════════════════════════════════════

import { Env, AITriageResult, AISummaryResult, Persona, Tag, Playbook, PERSONA_NAMES, PLAYBOOK_NAMES } from '../types';

// Workers AI type defs can lag model names; cast the canonical model id once.
const LLAMA_INSTRUCT_MODEL = '@cf/meta/llama-3.1-8b-instruct' as unknown as keyof AiModels;

// ───────────────────────────────────────────────────────────────────────────
// AI Triage - Analyze ticket and assign persona/tags/playbook
// ───────────────────────────────────────────────────────────────────────────
export async function triageTicket(
  ai: Ai,
  subject: string,
  description: string
): Promise<AITriageResult> {
  const prompt = `You are a tech support triage AI for NoizyLab OS. Analyze this support request and classify it.

TICKET:
Subject: ${subject}
Description: ${description}

PERSONAS (pick exactly 1):
P1 Tab Tornado - Too many browser tabs, memory issues
P2 Storage Closet - Disk full, hoarding files, can't find things
P3 Click-Yes Optimizer - Installed junk "optimizer" tools, PUPs
P4 Update Avoider - Refuses updates, running old OS/apps
P5 Password Spiral - Locked out, forgot passwords, no password manager
P6 Wi-Fi Whiplash - Constant connectivity drops, router issues
P7 Peripheral Collector - Too many devices, USB/printer/dock issues
P8 Cloud Sync Tangle - Multiple cloud services fighting, duplicates
P9 Thermal Throttler - Overheating laptop, fan noise, slowdowns
P10 Creative Chaos - Designer/creator with app conflicts, scratch disk full
P11 Fine Yesterday - "Nothing changed" but everything's broken
P12 Hardware Failing Quietly - Actual hardware failure, denial stage

TAGS (pick 1-3 from these exact tags):
Performance: PERF-TABS, PERF-STARTUP, PERF-BACKGROUND, PERF-THERMAL, PERF-LOWRAM
Storage: STOR-LOWDISK, STOR-DISKERRORS, STOR-EXTERNALDRIVE, FILE-PERMISSIONS, FILE-CORRUPTION
Security: SEC-PUP, SEC-BROWSERHIJACK, SEC-PHISH-ACCOUNT, SEC-AV-CONFLICT
Accounts: AUTH-APPLEID, AUTH-MICROSOFT, AUTH-GOOGLE, AUTH-MFA, AUTH-PASSWORDRESET
Network: NET-WIFIDROP, NET-DNS, NET-ROUTER, NET-VPN
Updates: UPD-OS, UPD-APP, DRV-PRINTER, DRV-USB, DRV-GPU, DRV-AUDIO
Cloud: SYNC-ICLOUD, SYNC-ONEDRIVE, SYNC-GDRIVE, SYNC-DUPES
Hardware: HW-SSD, HW-RAM, HW-BATTERY, HW-DUSTFAN, HW-LIQUID
Behavior: USR-CLICKYES, USR-NOBACKUP, USR-UPDATEAVOID, USR-DOWNLOADSCHAOS, USR-PASSWORDCHAOS

PLAYBOOKS (pick exactly 1):
PB1 Browser Diet - tabs/extensions cleanup
PB2 Space Guard - disk/downloads/cache cleanup
PB3 No Snake Oil - PUP/malware removal
PB4 Update Safe-Window - safe update strategy
PB5 Password Cleanroom - account recovery
PB6 Wi-Fi Stabilizer - network troubleshooting
PB7 Peripheral Detox - device cleanup
PB8 Cloud Sync Sanity - sync fix
PB9 Thermal Rescue - cooling/performance
PB10 Creative Workstation Tune - creative app optimization
PB11 Hardware Truth Test - diagnostics
PB12 Backup Bulletproof - backup setup

Respond in this exact JSON format:
{
  "persona": "P1",
  "tags": ["TAG-ONE", "TAG-TWO"],
  "next_question": "One clarifying question or null",
  "playbook": "PB1",
  "calm_message": "3 lines max. Reassuring. Actionable.",
  "confidence": 0.85
}`;

  try {
    const response = await ai.run(LLAMA_INSTRUCT_MODEL, {
      prompt,
      max_tokens: 500,
    }) as { response: string };
    
    // Parse JSON from response
    const jsonMatch = response.response.match(/\{[\s\S]*\}/);
    if (!jsonMatch) {
      return getDefaultTriage();
    }
    
    const result = JSON.parse(jsonMatch[0]);
    
    // Validate and enforce constraints
    return {
      persona: validatePersona(result.persona),
      tags: validateTags(result.tags),
      next_question: result.next_question || null,
      playbook: validatePlaybook(result.playbook),
      calm_message: truncateLines(result.calm_message, 3),
      confidence: Math.min(1, Math.max(0, result.confidence || 0.5)),
    };
  } catch (error) {
    console.error('AI triage error:', error);
    return getDefaultTriage();
  }
}

// ───────────────────────────────────────────────────────────────────────────
// AI Summarize - Generate session/ticket summary
// ───────────────────────────────────────────────────────────────────────────
export async function summarizeSession(
  ai: Ai,
  events: Array<{ type: string; payload_json: string; created_at: string }>
): Promise<AISummaryResult> {
  const eventSummary = events.map(e => {
    const payload = JSON.parse(e.payload_json);
    return `[${e.type}] ${JSON.stringify(payload)}`;
  }).join('\n');
  
  const prompt = `Summarize this tech support session for NoizyLab OS.

EVENTS:
${eventSummary}

Respond in this exact JSON format:
{
  "summary": "3 sentences max describing what happened",
  "key_points": ["point 1", "point 2", "point 3"],
  "next_steps": ["step 1", "step 2", "step 3"],
  "sentiment": "positive|neutral|frustrated"
}`;

  try {
    const response = await ai.run(LLAMA_INSTRUCT_MODEL, {
      prompt,
      max_tokens: 400,
    }) as { response: string };
    
    const jsonMatch = response.response.match(/\{[\s\S]*\}/);
    if (!jsonMatch) {
      return getDefaultSummary();
    }
    
    const result = JSON.parse(jsonMatch[0]);
    
    return {
      summary: truncateLines(result.summary, 3),
      key_points: (result.key_points || []).slice(0, 3),
      next_steps: (result.next_steps || []).slice(0, 3),
      sentiment: ['positive', 'neutral', 'frustrated'].includes(result.sentiment) 
        ? result.sentiment 
        : 'neutral',
    };
  } catch (error) {
    console.error('AI summarize error:', error);
    return getDefaultSummary();
  }
}

// ───────────────────────────────────────────────────────────────────────────
// Validation Helpers
// ───────────────────────────────────────────────────────────────────────────
const VALID_PERSONAS: Persona[] = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12'];
const VALID_PLAYBOOKS: Playbook[] = ['PB1','PB2','PB3','PB4','PB5','PB6','PB7','PB8','PB9','PB10','PB11','PB12'];
const VALID_TAGS: Tag[] = [
  'PERF-TABS','PERF-STARTUP','PERF-BACKGROUND','PERF-THERMAL','PERF-LOWRAM',
  'STOR-LOWDISK','STOR-DISKERRORS','STOR-EXTERNALDRIVE','FILE-PERMISSIONS','FILE-CORRUPTION',
  'SEC-PUP','SEC-BROWSERHIJACK','SEC-PHISH-ACCOUNT','SEC-AV-CONFLICT',
  'AUTH-APPLEID','AUTH-MICROSOFT','AUTH-GOOGLE','AUTH-MFA','AUTH-PASSWORDRESET',
  'NET-WIFIDROP','NET-DNS','NET-ROUTER','NET-VPN',
  'UPD-OS','UPD-APP','DRV-PRINTER','DRV-USB','DRV-GPU','DRV-AUDIO',
  'SYNC-ICLOUD','SYNC-ONEDRIVE','SYNC-GDRIVE','SYNC-DUPES',
  'HW-SSD','HW-RAM','HW-BATTERY','HW-DUSTFAN','HW-LIQUID',
  'USR-CLICKYES','USR-NOBACKUP','USR-UPDATEAVOID','USR-DOWNLOADSCHAOS','USR-PASSWORDCHAOS',
];

function validatePersona(p: string): Persona {
  return VALID_PERSONAS.includes(p as Persona) ? p as Persona : 'P11';
}

function validatePlaybook(pb: string): Playbook {
  return VALID_PLAYBOOKS.includes(pb as Playbook) ? pb as Playbook : 'PB11';
}

function validateTags(tags: string[]): Tag[] {
  if (!Array.isArray(tags)) return [];
  return tags
    .filter(t => VALID_TAGS.includes(t as Tag))
    .slice(0, 3) as Tag[];
}

function truncateLines(text: string, maxLines: number): string {
  if (!text) return '';
  const lines = text.split('\n').slice(0, maxLines);
  return lines.join('\n').slice(0, 500);
}

function getDefaultTriage(): AITriageResult {
  return {
    persona: 'P11',
    tags: [],
    next_question: 'Can you tell me more about what changed recently?',
    playbook: 'PB11',
    calm_message: "We've received your request and are reviewing it.\nA team member will be in touch shortly.\nNo action needed from you right now.",
    confidence: 0.3,
  };
}

function getDefaultSummary(): AISummaryResult {
  return {
    summary: 'Session in progress. Details being collected.',
    key_points: [],
    next_steps: ['Review ticket details'],
    sentiment: 'neutral',
  };
}
