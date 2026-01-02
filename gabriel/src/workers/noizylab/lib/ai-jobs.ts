// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - AI Genius Jobs
// Intelligent automation: triage, summaries, suggestions
// ═══════════════════════════════════════════════════════════════════════════

import type { Env } from '../index';
import { logEvent } from './events';
import { generateUUID } from './utils';

// Import config data (in production, load from R2 or KV)
import personas from '../../configs/personas.json';
import tags from '../../configs/tags.json';
import playbooks from '../../configs/playbooks.json';

// ═══════════════════════════════════════════════════════════════════════════
// Types
// ═══════════════════════════════════════════════════════════════════════════

interface TriageResult {
  persona: string | null;
  tags: string[];
  nextQuestion: string | null;
  suggestedPlaybook: string | null;
  draftMessage: {
    what: string;
    next: string;
    when: string;
  };
  confidence: 'green' | 'yellow' | 'red';
  reasoning: string;
}

interface SessionSummary {
  summary: string[];
  risk: string;
  prevention: string;
  followups: Array<{ days: number; check: string }>;
}

// ═══════════════════════════════════════════════════════════════════════════
// Triage Ticket (Auto on intake)
// ═══════════════════════════════════════════════════════════════════════════

export async function triageTicket(env: Env, ticketId: string, ticketData: any): Promise<TriageResult> {
  const startTime = Date.now();
  
  // Build prompt with context
  const prompt = buildTriagePrompt(ticketData);
  
  try {
    // Call AI Gateway
    const response = await env.AI.run('@cf/anthropic/claude-3-5-sonnet', {
      messages: [
        {
          role: 'system',
          content: getTriageSystemPrompt(),
        },
        {
          role: 'user',
          content: prompt,
        },
      ],
      max_tokens: 1000,
    });
    
    // Parse response
    const result = parseTriageResponse(response);
    
    // Log AI analysis
    await logAIAnalysis(env.DB, {
      ticketId,
      analysisType: 'intake',
      model: 'claude-3-5-sonnet',
      input: prompt,
      output: result,
      confidence: result.confidence,
      processingMs: Date.now() - startTime,
    });
    
    // Update ticket with AI results
    await updateTicketWithTriage(env.DB, ticketId, result);
    
    // Log events
    if (result.persona) {
      await logEvent(env.DB, {
        id: generateUUID(),
        ticketId,
        eventType: 'AUTO_PERSONA',
        actorType: 'ai',
        actorId: 'triage-bot',
        aiModel: 'claude-3-5-sonnet',
        aiConfidence: getConfidenceScore(result.confidence),
        aiReason: result.reasoning,
        data: { persona: result.persona },
      });
    }
    
    if (result.tags.length > 0) {
      await logEvent(env.DB, {
        id: generateUUID(),
        ticketId,
        eventType: 'AUTO_TAGS',
        actorType: 'ai',
        actorId: 'triage-bot',
        aiModel: 'claude-3-5-sonnet',
        aiConfidence: getConfidenceScore(result.confidence),
        data: { tags: result.tags },
      });
    }
    
    if (result.suggestedPlaybook) {
      await logEvent(env.DB, {
        id: generateUUID(),
        ticketId,
        eventType: 'PLAYBOOK_SUGGESTED',
        actorType: 'ai',
        actorId: 'triage-bot',
        aiModel: 'claude-3-5-sonnet',
        aiConfidence: getConfidenceScore(result.confidence),
        data: { playbook: result.suggestedPlaybook },
      });
    }
    
    return result;
    
  } catch (error) {
    console.error('AI triage error:', error);
    
    // Return safe fallback
    return {
      persona: null,
      tags: [],
      nextQuestion: 'What specific issue are you experiencing?',
      suggestedPlaybook: null,
      draftMessage: {
        what: 'Got your request.',
        next: 'A technician will review shortly.',
        when: 'Next update within 2 hours.',
      },
      confidence: 'red',
      reasoning: 'AI analysis unavailable - requires staff review',
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// Session Summary (Auto after live session ends)
// ═══════════════════════════════════════════════════════════════════════════

export async function summarizeSession(
  env: Env,
  ticketId: string,
  sessionId: string,
  transcript: string
): Promise<SessionSummary> {
  const startTime = Date.now();
  
  const prompt = `
Summarize this tech support session:

TRANSCRIPT:
${transcript}

Provide:
1. 5-bullet summary of what was done
2. Main risk/issue that could recur
3. Prevention recommendation
4. Recommended follow-up checks (7 days and/or 30 days)

Respond in JSON format:
{
  "summary": ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5"],
  "risk": "main risk statement",
  "prevention": "prevention recommendation",
  "followups": [{"days": 7, "check": "what to check"}, {"days": 30, "check": "what to check"}]
}
`;

  try {
    const response = await env.AI.run('@cf/anthropic/claude-3-5-sonnet', {
      messages: [
        {
          role: 'system',
          content: 'You are a tech support summarizer. Provide concise, actionable summaries. Always respond in valid JSON.',
        },
        {
          role: 'user',
          content: prompt,
        },
      ],
      max_tokens: 800,
    });
    
    const result = JSON.parse(response.response) as SessionSummary;
    
    // Log AI analysis
    await logAIAnalysis(env.DB, {
      ticketId,
      analysisType: 'session_summary',
      model: 'claude-3-5-sonnet',
      input: prompt,
      output: result,
      confidence: 'green',
      processingMs: Date.now() - startTime,
    });
    
    // Log summary event
    await logEvent(env.DB, {
      id: generateUUID(),
      ticketId,
      eventType: 'AI_SUMMARY',
      actorType: 'ai',
      actorId: 'summary-bot',
      aiModel: 'claude-3-5-sonnet',
      sessionId,
      data: result,
    });
    
    // Schedule follow-ups
    for (const followup of result.followups) {
      await scheduleFollowup(env.DB, ticketId, followup.days, followup.check);
    }
    
    return result;
    
  } catch (error) {
    console.error('Session summary error:', error);
    return {
      summary: ['Session completed', 'Details require staff review'],
      risk: 'Unable to analyze automatically',
      prevention: 'Staff review recommended',
      followups: [{ days: 7, check: 'General follow-up' }],
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// Draft Client Message
// ═══════════════════════════════════════════════════════════════════════════

export async function draftClientMessage(
  env: Env,
  ticketId: string,
  context: {
    status: string;
    persona: string;
    tags: string[];
    lastUpdate: string;
    nextUpdateBy: string;
  }
): Promise<{ what: string; next: string; when: string }> {
  const personaInfo = personas.personas[context.persona as keyof typeof personas.personas];
  
  const prompt = `
Draft a brief client message (3 lines max) for:
- Status: ${context.status}
- Persona: ${context.persona} - ${personaInfo?.name || 'Unknown'}
- Tags: ${context.tags.join(', ')}
- Last update: ${context.lastUpdate}

Use the persona's calm response style. Be empathetic but efficient.

Respond in JSON:
{
  "what": "what we know/found (1 line)",
  "next": "what happens next (1 line)",
  "when": "next update time (1 line)"
}
`;

  try {
    const response = await env.AI.run('@cf/anthropic/claude-3-5-sonnet', {
      messages: [
        {
          role: 'system',
          content: 'You draft brief, calm tech support messages. Never more than 3 lines. Always JSON format.',
        },
        {
          role: 'user',
          content: prompt,
        },
      ],
      max_tokens: 300,
    });
    
    return JSON.parse(response.response);
    
  } catch (error) {
    console.error('Draft message error:', error);
    return {
      what: 'We\'re looking into this.',
      next: 'A technician will follow up.',
      when: `Next update by ${context.nextUpdateBy}`,
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// Helper Functions
// ═══════════════════════════════════════════════════════════════════════════

function getTriageSystemPrompt(): string {
  return `You are an expert IT triage bot for NoizyLab, a tech support service.

Your job is to analyze incoming support requests and:
1. Identify the client PERSONA (P1-P12)
2. Suggest up to 3 TAGS from the allowed list
3. Recommend a PLAYBOOK if applicable
4. Draft a brief, calm response

PERSONAS:
${Object.entries(personas.personas).map(([id, p]) => `${id}: ${p.name} - ${p.description}`).join('\n')}

ALLOWED TAGS:
${tags.allTags.join(', ')}

PLAYBOOKS:
${Object.entries(playbooks.playbooks).map(([id, p]) => `${id}: ${p.name} - ${p.description}`).join('\n')}

CONFIDENCE LEVELS:
- green: High confidence, draft and suggest automatically
- yellow: Medium confidence, ask 1 clarifying question
- red: Low confidence, requires staff review

Always respond in valid JSON format.`;
}

function buildTriagePrompt(ticketData: any): string {
  return `
NEW TICKET:
- Device: ${ticketData.deviceType} ${ticketData.deviceModel || ''} (${ticketData.deviceOs || 'OS unknown'})
- Issue Summary: ${ticketData.issueSummary}
- Description: ${ticketData.issueDescription || 'No additional details'}
- Client: ${ticketData.clientName}

Analyze and provide triage in JSON:
{
  "persona": "P1-P12 or null",
  "tags": ["TAG1", "TAG2", "TAG3"],
  "nextQuestion": "clarifying question if needed, else null",
  "suggestedPlaybook": "PB1-PB12 or null",
  "draftMessage": {
    "what": "acknowledgment",
    "next": "next step",
    "when": "update time"
  },
  "confidence": "green|yellow|red",
  "reasoning": "brief explanation"
}
`;
}

function parseTriageResponse(response: any): TriageResult {
  try {
    const parsed = JSON.parse(response.response);
    return {
      persona: parsed.persona || null,
      tags: Array.isArray(parsed.tags) ? parsed.tags.slice(0, 3) : [],
      nextQuestion: parsed.nextQuestion || null,
      suggestedPlaybook: parsed.suggestedPlaybook || null,
      draftMessage: parsed.draftMessage || {
        what: 'Got your request.',
        next: 'Reviewing now.',
        when: 'Update within 2 hours.',
      },
      confidence: parsed.confidence || 'yellow',
      reasoning: parsed.reasoning || 'No reasoning provided',
    };
  } catch (error) {
    console.error('Failed to parse triage response:', error);
    return {
      persona: null,
      tags: [],
      nextQuestion: 'Could you provide more details about the issue?',
      suggestedPlaybook: null,
      draftMessage: {
        what: 'Got your request.',
        next: 'A technician will review.',
        when: 'Update within 2 hours.',
      },
      confidence: 'red',
      reasoning: 'Failed to parse AI response',
    };
  }
}

function getConfidenceScore(confidence: string): number {
  switch (confidence) {
    case 'green': return 0.9;
    case 'yellow': return 0.6;
    case 'red': return 0.3;
    default: return 0.5;
  }
}

async function updateTicketWithTriage(db: D1Database, ticketId: string, result: TriageResult) {
  await db.prepare(`
    UPDATE tickets SET
      persona = ?,
      tags = ?,
      suggested_playbook = ?,
      ai_confidence = ?,
      updated_at = datetime('now')
    WHERE id = ?
  `).bind(
    result.persona,
    JSON.stringify(result.tags),
    result.suggestedPlaybook,
    result.confidence,
    ticketId
  ).run();
}

async function logAIAnalysis(
  db: D1Database,
  data: {
    ticketId: string;
    analysisType: string;
    model: string;
    input: string;
    output: any;
    confidence: string;
    processingMs: number;
  }
) {
  await db.prepare(`
    INSERT INTO ai_analysis (
      id, ticket_id, analysis_type, model,
      input_text, output_json, confidence, processing_ms
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    generateUUID(),
    data.ticketId,
    data.analysisType,
    data.model,
    data.input,
    JSON.stringify(data.output),
    data.confidence,
    data.processingMs
  ).run();
}

async function scheduleFollowup(
  db: D1Database,
  ticketId: string,
  days: number,
  check: string
) {
  const scheduledFor = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toISOString();
  
  await db.prepare(`
    INSERT INTO followups (
      id, ticket_id, scheduled_for, followup_type,
      check_description, ai_suggested
    ) VALUES (?, ?, ?, ?, ?, 1)
  `).bind(
    generateUUID(),
    ticketId,
    scheduledFor,
    `${days}d`,
    check
  ).run();
  
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'FOLLOWUP_SCHEDULED',
    actorType: 'ai',
    actorId: 'summary-bot',
    data: { days, check, scheduledFor },
  });
}
