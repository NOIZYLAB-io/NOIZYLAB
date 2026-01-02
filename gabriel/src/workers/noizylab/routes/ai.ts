// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - AI Routes
// AI Gateway endpoints for analysis and drafting
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { z } from 'zod';
import { zValidator } from '@hono/zod-validator';
import type { Env } from '../index';
import { triageTicket, draftClientMessage, summarizeSession } from '../lib/ai-jobs';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Manual Triage Request
// ═══════════════════════════════════════════════════════════════════════════

app.post('/triage/:ticketId', async (c) => {
  const ticketId = c.req.param('ticketId');
  
  // Get ticket data
  const ticket = await c.env.DB.prepare(
    'SELECT * FROM tickets WHERE id = ?'
  ).bind(ticketId).first();
  
  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }
  
  try {
    const result = await triageTicket(c.env, ticketId, {
      deviceType: ticket.device_type,
      deviceModel: ticket.device_model,
      deviceOs: ticket.device_os,
      issueSummary: ticket.issue_summary,
      issueDescription: ticket.issue_description,
      clientName: ticket.client_name,
    });
    
    return c.json({
      success: true,
      ticketId,
      triage: result,
    });
    
  } catch (error) {
    console.error('Triage error:', error);
    return c.json({ error: 'AI triage failed' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Draft Client Message
// ═══════════════════════════════════════════════════════════════════════════

const draftSchema = z.object({
  persona: z.string().optional(),
  tags: z.array(z.string()).optional(),
  status: z.string().optional(),
  customContext: z.string().optional(),
});

app.post('/draft/:ticketId', zValidator('json', draftSchema), async (c) => {
  const ticketId = c.req.param('ticketId');
  const body = c.req.valid('json');
  
  // Get ticket data
  const ticket = await c.env.DB.prepare(
    'SELECT * FROM tickets WHERE id = ?'
  ).bind(ticketId).first();
  
  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }
  
  try {
    const draft = await draftClientMessage(c.env, ticketId, {
      status: body.status || ticket.status as string,
      persona: body.persona || ticket.persona as string || 'P11',
      tags: body.tags || (ticket.tags ? JSON.parse(ticket.tags as string) : []),
      lastUpdate: ticket.updated_at as string,
      nextUpdateBy: ticket.next_update_by as string,
    });
    
    return c.json({
      success: true,
      ticketId,
      draft,
    });
    
  } catch (error) {
    console.error('Draft error:', error);
    return c.json({ error: 'AI draft failed' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get AI Analysis History
// ═══════════════════════════════════════════════════════════════════════════

app.get('/analysis/:ticketId', async (c) => {
  const ticketId = c.req.param('ticketId');
  
  try {
    const analyses = await c.env.DB.prepare(`
      SELECT id, analysis_type, model, confidence, confidence_score,
             reasoning, staff_reviewed, staff_approved, created_at, processing_ms
      FROM ai_analysis
      WHERE ticket_id = ?
      ORDER BY created_at DESC
      LIMIT 20
    `).bind(ticketId).all();
    
    return c.json({
      ticketId,
      analyses: analyses.results,
    });
    
  } catch (error) {
    console.error('Error fetching AI history:', error);
    return c.json({ error: 'Failed to fetch AI history' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Staff Review of AI Analysis
// ═══════════════════════════════════════════════════════════════════════════

const reviewSchema = z.object({
  approved: z.boolean(),
  corrections: z.string().optional(),
});

app.post('/analysis/:analysisId/review', zValidator('json', reviewSchema), async (c) => {
  const analysisId = c.req.param('analysisId');
  const body = c.req.valid('json');
  const staffId = c.req.header('X-Staff-Id') || 'unknown';
  
  try {
    await c.env.DB.prepare(`
      UPDATE ai_analysis SET
        staff_reviewed = 1,
        staff_approved = ?,
        staff_corrections = ?
      WHERE id = ?
    `).bind(
      body.approved ? 1 : 0,
      body.corrections || null,
      analysisId
    ).run();
    
    return c.json({
      success: true,
      analysisId,
      approved: body.approved,
    });
    
  } catch (error) {
    console.error('Error reviewing analysis:', error);
    return c.json({ error: 'Failed to review analysis' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get Available Models
// ═══════════════════════════════════════════════════════════════════════════

app.get('/models', (c) => {
  return c.json({
    models: [
      {
        id: '@cf/anthropic/claude-3-5-sonnet',
        name: 'Claude 3.5 Sonnet',
        provider: 'Anthropic',
        capabilities: ['triage', 'summary', 'draft'],
        default: true,
      },
      {
        id: '@cf/meta/llama-3.1-70b-instruct',
        name: 'Llama 3.1 70B',
        provider: 'Meta',
        capabilities: ['triage', 'summary'],
        default: false,
      },
      {
        id: '@cf/mistral/mistral-7b-instruct-v0.2',
        name: 'Mistral 7B',
        provider: 'Mistral',
        capabilities: ['draft'],
        default: false,
      },
    ],
    defaultModel: '@cf/anthropic/claude-3-5-sonnet',
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// Confidence Statistics
// ═══════════════════════════════════════════════════════════════════════════

app.get('/stats', async (c) => {
  try {
    const stats = await c.env.DB.prepare(`
      SELECT 
        confidence,
        COUNT(*) as count,
        AVG(processing_ms) as avg_processing_ms,
        SUM(CASE WHEN staff_approved = 1 THEN 1 ELSE 0 END) as approved_count,
        SUM(CASE WHEN staff_approved = 0 THEN 1 ELSE 0 END) as rejected_count
      FROM ai_analysis
      WHERE created_at > datetime('now', '-30 days')
      GROUP BY confidence
    `).all();
    
    const totalAnalyses = await c.env.DB.prepare(`
      SELECT COUNT(*) as total FROM ai_analysis
      WHERE created_at > datetime('now', '-30 days')
    `).first();
    
    return c.json({
      period: '30 days',
      total: totalAnalyses?.total || 0,
      byConfidence: stats.results,
    });
    
  } catch (error) {
    console.error('Error fetching AI stats:', error);
    return c.json({ error: 'Failed to fetch stats' }, 500);
  }
});

export { app as aiRoutes };
