// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Webhook Routes
// Inbound webhooks for email, payments, etc.
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import type { Env } from '../index';
import { logEvent, logBillingPaid } from '../lib/events';
import { generateUUID, parseSubjectDNA } from '../lib/utils';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Email Webhook (from Gmail/Cloudflare Email Workers)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/email', async (c) => {
  const signature = c.req.header('X-Webhook-Signature');
  // In production, verify webhook signature
  
  try {
    const email = await c.req.json();
    
    const {
      from,
      to,
      subject,
      body,
      threadId,
      messageId,
    } = email;
    
    // Parse subject for ticket ID
    const subjectDNA = parseSubjectDNA(subject);
    
    if (subjectDNA.ticketId) {
      // Existing ticket - log as event
      await logEvent(c.env.DB, {
        id: generateUUID(),
        ticketId: subjectDNA.ticketId,
        eventType: 'INFO_REQUESTED', // or create EMAIL_RECEIVED type
        actorType: 'client',
        actorId: from,
        data: {
          subject,
          preview: body.substring(0, 200),
          threadId,
          messageId,
        },
      });
      
      // Update ticket
      await c.env.DB.prepare(`
        UPDATE tickets SET 
          status = CASE 
            WHEN status = '1-WAITING-CLIENT' THEN '0-TRIAGE'
            ELSE status 
          END,
          updated_at = datetime('now'),
          gmail_thread_id = COALESCE(gmail_thread_id, ?)
        WHERE id = ?
      `).bind(threadId, subjectDNA.ticketId).run();
      
    } else {
      // New ticket from email - create one
      // This would parse the email body and create a ticket
      // For MVP, just log and let staff handle manually
      console.log('New email without ticket ID:', subject);
    }
    
    return c.json({ success: true });
    
  } catch (error) {
    console.error('Email webhook error:', error);
    return c.json({ error: 'Failed to process email' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Payment Webhook (Stripe/e-Transfer notification)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/payment', async (c) => {
  const signature = c.req.header('Stripe-Signature');
  // In production, verify Stripe webhook signature
  
  try {
    const event = await c.req.json();
    
    if (event.type === 'payment_intent.succeeded') {
      const paymentIntent = event.data.object;
      const ticketId = paymentIntent.metadata?.ticketId;
      
      if (ticketId) {
        // Update billing record
        await c.env.DB.prepare(`
          UPDATE billing SET
            status = 'paid',
            payment_method = ?,
            paid_at = datetime('now')
          WHERE ticket_id = ?
        `).bind(paymentIntent.payment_method_types[0], ticketId).run();
        
        // Log event
        await logBillingPaid(
          c.env.DB,
          ticketId,
          paymentIntent.amount / 100,
          paymentIntent.payment_method_types[0]
        );
      }
    }
    
    return c.json({ received: true });
    
  } catch (error) {
    console.error('Payment webhook error:', error);
    return c.json({ error: 'Failed to process payment' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Follow-up Reminder Webhook (from scheduled job)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/followup-check', async (c) => {
  try {
    // Get due follow-ups
    const dueFollowups = await c.env.DB.prepare(`
      SELECT f.*, t.client_email, t.client_name
      FROM followups f
      JOIN tickets t ON f.ticket_id = t.id
      WHERE f.status = 'pending'
      AND datetime(f.scheduled_for) <= datetime('now')
      LIMIT 50
    `).all();
    
    const processed: string[] = [];
    
    for (const followup of dueFollowups.results) {
      // Log that follow-up is due
      await logEvent(c.env.DB, {
        id: generateUUID(),
        ticketId: followup.ticket_id as string,
        eventType: 'FOLLOWUP_SCHEDULED',
        actorType: 'system',
        actorId: 'followup-scheduler',
        data: {
          followupId: followup.id,
          check: followup.check_description,
          originalSchedule: followup.scheduled_for,
          status: 'due',
        },
      });
      
      processed.push(followup.id as string);
      
      // In production, send email reminder here
    }
    
    return c.json({
      success: true,
      processed: processed.length,
      followupIds: processed,
    });
    
  } catch (error) {
    console.error('Follow-up check error:', error);
    return c.json({ error: 'Failed to process follow-ups' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Health/Status Webhook (for monitoring)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/health-ping', async (c) => {
  const timestamp = new Date().toISOString();
  
  // Could store in KV for uptime tracking
  await c.env.CACHE.put('last-health-ping', timestamp, { expirationTtl: 300 });
  
  return c.json({
    status: 'healthy',
    timestamp,
    version: '1.0.0',
  });
});

export { app as webhookRoutes };
