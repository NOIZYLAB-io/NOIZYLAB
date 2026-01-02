// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Staff Routes
// Control Room API for staff operations
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { z } from 'zod';
import { zValidator } from '@hono/zod-validator';
import type { Env } from '../index';
import { logEvent, logPlaybookApplied, logStatusChange } from '../lib/events';
import { generateUUID, replaceTemplateVars, formatNextUpdateTime } from '../lib/utils';
import playbooks from '../../configs/playbooks.json';
import templates from '../../configs/gmail-ops.json';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Dashboard Data (Ticket Board)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/dashboard', async (c) => {
  try {
    // Get ticket counts by status
    const ticketCounts = await c.env.DB.prepare(`
      SELECT status, COUNT(*) as count 
      FROM tickets 
      WHERE status != '5-DONE'
      GROUP BY status
      ORDER BY status
    `).all();
    
    // Get active tickets
    const activeTickets = await c.env.DB.prepare(`
      SELECT t.*, 
             (SELECT COUNT(*) FROM events WHERE ticket_id = t.id) as event_count,
             (SELECT COUNT(*) FROM uploads WHERE ticket_id = t.id) as upload_count
      FROM tickets t
      WHERE t.status != '5-DONE'
      ORDER BY 
        CASE t.status 
          WHEN '4-IN-PROGRESS' THEN 1
          WHEN '0-TRIAGE' THEN 2
          WHEN '3-SCHEDULED' THEN 3
          WHEN '1-WAITING-CLIENT' THEN 4
          WHEN '2-WAITING-PARTS' THEN 5
          ELSE 6
        END,
        t.updated_at DESC
      LIMIT 50
    `).all();
    
    // Get today's follow-ups
    const followups = await c.env.DB.prepare(`
      SELECT f.*, t.client_name, t.device_type, t.issue_summary
      FROM followups f
      JOIN tickets t ON f.ticket_id = t.id
      WHERE f.status = 'pending'
      AND date(f.scheduled_for) <= date('now')
      ORDER BY f.scheduled_for
      LIMIT 20
    `).all();
    
    // Get recent AI suggestions needing review
    const pendingReviews = await c.env.DB.prepare(`
      SELECT a.*, t.id as ticket_id, t.client_name
      FROM ai_analysis a
      JOIN tickets t ON a.ticket_id = t.id
      WHERE a.staff_reviewed = 0 AND a.confidence = 'red'
      ORDER BY a.created_at DESC
      LIMIT 10
    `).all();
    
    return c.json({
      ticketCounts: ticketCounts.results,
      activeTickets: activeTickets.results,
      todayFollowups: followups.results,
      pendingReviews: pendingReviews.results,
      timestamp: new Date().toISOString(),
    });
    
  } catch (error) {
    console.error('Dashboard error:', error);
    return c.json({ error: 'Failed to load dashboard' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Apply Playbook
// ═══════════════════════════════════════════════════════════════════════════

const applyPlaybookSchema = z.object({
  playbookId: z.string(),
  notes: z.string().optional(),
});

app.post('/tickets/:ticketId/playbook', zValidator('json', applyPlaybookSchema), async (c) => {
  const ticketId = c.req.param('ticketId');
  const body = c.req.valid('json');
  const staffId = c.req.header('X-Staff-Id') || 'unknown';
  
  const playbook = playbooks.playbooks[body.playbookId as keyof typeof playbooks.playbooks];
  if (!playbook) {
    return c.json({ error: 'Playbook not found' }, 404);
  }
  
  try {
    // Create playbook application record
    const applicationId = generateUUID();
    
    await c.env.DB.prepare(`
      INSERT INTO playbook_applications (
        id, ticket_id, playbook_id, applied_by, notes
      ) VALUES (?, ?, ?, ?, ?)
    `).bind(applicationId, ticketId, body.playbookId, staffId, body.notes || null).run();
    
    // Log event
    await logPlaybookApplied(c.env.DB, ticketId, staffId, body.playbookId, playbook.name);
    
    // Update ticket
    await c.env.DB.prepare(`
      UPDATE tickets SET 
        suggested_playbook = ?,
        updated_at = datetime('now')
      WHERE id = ?
    `).bind(body.playbookId, ticketId).run();
    
    return c.json({
      success: true,
      applicationId,
      playbook: {
        id: playbook.id,
        name: playbook.name,
        fixSteps: playbook.fix.steps,
        preventSteps: playbook.prevent.steps,
        followup: playbook.followup,
      },
    });
    
  } catch (error) {
    console.error('Apply playbook error:', error);
    return c.json({ error: 'Failed to apply playbook' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Complete Playbook Step
// ═══════════════════════════════════════════════════════════════════════════

const completeStepSchema = z.object({
  stepId: z.string(),
  notes: z.string().optional(),
});

app.post('/playbook-applications/:applicationId/step', zValidator('json', completeStepSchema), async (c) => {
  const applicationId = c.req.param('applicationId');
  const body = c.req.valid('json');
  
  try {
    // Get current application
    const app = await c.env.DB.prepare(
      'SELECT * FROM playbook_applications WHERE id = ?'
    ).bind(applicationId).first();
    
    if (!app) {
      return c.json({ error: 'Playbook application not found' }, 404);
    }
    
    // Update completed steps
    let completedSteps: string[] = [];
    if (app.steps_completed) {
      try {
        completedSteps = JSON.parse(app.steps_completed as string);
      } catch (e) {}
    }
    
    if (!completedSteps.includes(body.stepId)) {
      completedSteps.push(body.stepId);
    }
    
    await c.env.DB.prepare(`
      UPDATE playbook_applications SET 
        steps_completed = ?
      WHERE id = ?
    `).bind(JSON.stringify(completedSteps), applicationId).run();
    
    return c.json({
      success: true,
      completedSteps,
    });
    
  } catch (error) {
    console.error('Complete step error:', error);
    return c.json({ error: 'Failed to complete step' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Send Calm Update
// ═══════════════════════════════════════════════════════════════════════════

const sendUpdateSchema = z.object({
  templateId: z.string(),
  variables: z.record(z.string()).optional(),
  nextUpdateHours: z.number().optional(),
});

app.post('/tickets/:ticketId/update', zValidator('json', sendUpdateSchema), async (c) => {
  const ticketId = c.req.param('ticketId');
  const body = c.req.valid('json');
  const staffId = c.req.header('X-Staff-Id') || 'unknown';
  
  const template = templates.templates[body.templateId as keyof typeof templates.templates];
  if (!template) {
    return c.json({ error: 'Template not found' }, 404);
  }
  
  // Get ticket for default variables
  const ticket = await c.env.DB.prepare(
    'SELECT * FROM tickets WHERE id = ?'
  ).bind(ticketId).first();
  
  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }
  
  // Build variables
  const nextUpdateTime = formatNextUpdateTime(body.nextUpdateHours || 2);
  const vars: Record<string, string> = {
    TICKET_ID: ticketId,
    LASTNAME: (ticket.client_name as string).split(' ').pop() || '',
    DEVICE: ticket.device_type as string,
    ISSUE: ticket.issue_summary as string,
    NEXT_UPDATE_TIME: nextUpdateTime,
    ...body.variables,
  };
  
  // Generate message
  const subject = replaceTemplateVars(template.subject, vars);
  const messageBody = replaceTemplateVars(template.body, vars);
  
  try {
    // Log event
    await logEvent(c.env.DB, {
      id: generateUUID(),
      ticketId,
      eventType: 'INFO_REQUESTED',
      actorType: 'staff',
      actorId: staffId,
      data: {
        templateId: body.templateId,
        subject,
        now: messageBody.split('\n')[0],
        next: messageBody.split('\n')[1] || '',
      },
    });
    
    // Update next_update_by
    const nextUpdateBy = new Date(Date.now() + (body.nextUpdateHours || 2) * 60 * 60 * 1000).toISOString();
    await c.env.DB.prepare(`
      UPDATE tickets SET 
        next_update_by = ?,
        updated_at = datetime('now')
      WHERE id = ?
    `).bind(nextUpdateBy, ticketId).run();
    
    return c.json({
      success: true,
      subject,
      body: messageBody,
      nextUpdateBy,
      // In production, this would actually send the email
      // For now, return the draft for manual sending
    });
    
  } catch (error) {
    console.error('Send update error:', error);
    return c.json({ error: 'Failed to send update' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Quick Status Change
// ═══════════════════════════════════════════════════════════════════════════

const statusChangeSchema = z.object({
  status: z.enum([
    '0-TRIAGE', '1-WAITING-CLIENT', '2-WAITING-PARTS',
    '3-SCHEDULED', '4-IN-PROGRESS', '5-DONE', '9-BILLING'
  ]),
  note: z.string().optional(),
});

app.post('/tickets/:ticketId/status', zValidator('json', statusChangeSchema), async (c) => {
  const ticketId = c.req.param('ticketId');
  const body = c.req.valid('json');
  const staffId = c.req.header('X-Staff-Id') || 'unknown';
  
  const ticket = await c.env.DB.prepare(
    'SELECT status FROM tickets WHERE id = ?'
  ).bind(ticketId).first();
  
  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }
  
  const oldStatus = ticket.status as string;
  
  try {
    await c.env.DB.prepare(`
      UPDATE tickets SET 
        status = ?,
        updated_at = datetime('now'),
        closed_at = CASE WHEN ? = '5-DONE' THEN datetime('now') ELSE closed_at END
      WHERE id = ?
    `).bind(body.status, body.status, ticketId).run();
    
    await logStatusChange(c.env.DB, ticketId, staffId, 'staff', oldStatus, body.status, body.note);
    
    return c.json({
      success: true,
      previousStatus: oldStatus,
      newStatus: body.status,
    });
    
  } catch (error) {
    console.error('Status change error:', error);
    return c.json({ error: 'Failed to change status' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Request Photo/Log from Client
// ═══════════════════════════════════════════════════════════════════════════

app.post('/tickets/:ticketId/request-info', async (c) => {
  const ticketId = c.req.param('ticketId');
  const { infoType, customMessage } = await c.req.json();
  const staffId = c.req.header('X-Staff-Id') || 'unknown';
  
  const infoTypes: Record<string, string> = {
    photo: 'Please send a photo of the issue.',
    screenshot: 'Please send a screenshot showing the error.',
    log: 'Please send the system log file.',
    model: 'Please send your device model number.',
  };
  
  const message = customMessage || infoTypes[infoType] || 'Please send the requested information.';
  
  try {
    await logEvent(c.env.DB, {
      id: generateUUID(),
      ticketId,
      eventType: 'INFO_REQUESTED',
      actorType: 'staff',
      actorId: staffId,
      data: { infoType, message },
    });
    
    // Update status to waiting
    await c.env.DB.prepare(`
      UPDATE tickets SET 
        status = '1-WAITING-CLIENT',
        updated_at = datetime('now')
      WHERE id = ?
    `).bind(ticketId).run();
    
    return c.json({
      success: true,
      message,
      status: '1-WAITING-CLIENT',
    });
    
  } catch (error) {
    console.error('Request info error:', error);
    return c.json({ error: 'Failed to request info' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get All Playbooks
// ═══════════════════════════════════════════════════════════════════════════

app.get('/playbooks', (c) => {
  const playbookList = Object.values(playbooks.playbooks).map(pb => ({
    id: pb.id,
    name: pb.name,
    emoji: pb.emoji,
    targetPersona: pb.targetPersona,
    description: pb.description,
    estimatedTime: pb.estimatedTime,
    fixStepCount: pb.fix.steps.length,
    preventStepCount: pb.prevent.steps.length,
    followupDays: pb.followup.days,
  }));
  
  return c.json({ playbooks: playbookList });
});

// ═══════════════════════════════════════════════════════════════════════════
// Get All Templates
// ═══════════════════════════════════════════════════════════════════════════

app.get('/templates', (c) => {
  const templateList = Object.values(templates.templates).map(t => ({
    id: t.id,
    name: t.name,
    variables: t.variables,
  }));
  
  return c.json({ templates: templateList });
});

export { app as staffRoutes };
