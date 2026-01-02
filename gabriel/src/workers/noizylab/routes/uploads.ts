// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Upload Routes
// R2 presigned URL generation and upload tracking
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { z } from 'zod';
import { zValidator } from '@hono/zod-validator';
import type { Env } from '../index';
import { verifyTurnstile } from '../lib/turnstile';
import { logUpload } from '../lib/events';
import { generateUUID, generateR2Key, sanitizeFilename } from '../lib/utils';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Validation Schemas
// ═══════════════════════════════════════════════════════════════════════════

const requestUploadSchema = z.object({
  ticketId: z.string(),
  filename: z.string().max(255),
  contentType: z.string(),
  uploadType: z.enum(['photo', 'screenshot', 'log', 'receipt', 'document']),
  turnstileToken: z.string(),
});

// ═══════════════════════════════════════════════════════════════════════════
// Request Presigned Upload URL
// ═══════════════════════════════════════════════════════════════════════════

app.post('/request', zValidator('json', requestUploadSchema), async (c) => {
  const body = c.req.valid('json');
  
  // Verify Turnstile
  const turnstileValid = await verifyTurnstile(body.turnstileToken, c.env.TURNSTILE_SECRET);
  if (!turnstileValid) {
    return c.json({ error: 'Bot verification failed' }, 403);
  }
  
  // Verify ticket exists
  const ticket = await c.env.DB.prepare(
    'SELECT id FROM tickets WHERE id = ?'
  ).bind(body.ticketId).first();
  
  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }
  
  // Generate R2 key
  const safeFilename = sanitizeFilename(body.filename);
  const r2Key = generateR2Key(body.ticketId, safeFilename);
  const uploadId = generateUUID();
  
  // Create presigned URL
  // Note: R2 presigned URLs require the Cloudflare API
  // For now, we'll use direct upload through the worker
  
  try {
    // Store pending upload record
    await c.env.DB.prepare(`
      INSERT INTO uploads (
        id, ticket_id, r2_key, filename, content_type, 
        upload_type, size_bytes, uploaded_by, presigned_url_expires
      ) VALUES (?, ?, ?, ?, ?, ?, 0, 'client', datetime('now', '+1 hour'))
    `).bind(
      uploadId,
      body.ticketId,
      r2Key,
      safeFilename,
      body.contentType,
      body.uploadType
    ).run();
    
    return c.json({
      success: true,
      uploadId,
      r2Key,
      uploadUrl: `/api/uploads/${uploadId}/complete`,
      expiresIn: 3600,
      maxSize: 10 * 1024 * 1024, // 10MB
    });
    
  } catch (error) {
    console.error('Error creating upload request:', error);
    return c.json({ error: 'Failed to create upload request' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Complete Upload (receive file)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/:uploadId/complete', async (c) => {
  const uploadId = c.req.param('uploadId');
  
  // Get pending upload record
  const upload = await c.env.DB.prepare(
    'SELECT * FROM uploads WHERE id = ? AND size_bytes = 0'
  ).bind(uploadId).first();
  
  if (!upload) {
    return c.json({ error: 'Upload not found or already completed' }, 404);
  }
  
  // Check if expired
  if (upload.presigned_url_expires && new Date(upload.presigned_url_expires as string) < new Date()) {
    return c.json({ error: 'Upload URL expired' }, 410);
  }
  
  try {
    // Get file from request body
    const contentType = c.req.header('Content-Type') || 'application/octet-stream';
    const body = await c.req.arrayBuffer();
    
    // Size check (10MB)
    if (body.byteLength > 10 * 1024 * 1024) {
      return c.json({ error: 'File too large (max 10MB)' }, 413);
    }
    
    // Upload to R2
    await c.env.UPLOADS.put(upload.r2_key as string, body, {
      httpMetadata: {
        contentType,
      },
      customMetadata: {
        ticketId: upload.ticket_id as string,
        uploadId,
        uploadType: upload.upload_type as string,
      },
    });
    
    // Update upload record
    await c.env.DB.prepare(`
      UPDATE uploads SET 
        size_bytes = ?,
        content_type = ?,
        presigned_url_expires = NULL
      WHERE id = ?
    `).bind(body.byteLength, contentType, uploadId).run();
    
    // Log event
    await logUpload(
      c.env.DB,
      upload.ticket_id as string,
      'client',
      'client',
      upload.r2_key as string,
      upload.filename as string,
      upload.upload_type as string
    );
    
    return c.json({
      success: true,
      uploadId,
      size: body.byteLength,
      ticketId: upload.ticket_id,
    });
    
  } catch (error) {
    console.error('Error completing upload:', error);
    return c.json({ error: 'Failed to complete upload' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get Upload (serve file)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/:uploadId', async (c) => {
  const uploadId = c.req.param('uploadId');
  
  // Get upload record
  const upload = await c.env.DB.prepare(
    'SELECT * FROM uploads WHERE id = ?'
  ).bind(uploadId).first();
  
  if (!upload || upload.size_bytes === 0) {
    return c.json({ error: 'Upload not found' }, 404);
  }
  
  try {
    // Get from R2
    const object = await c.env.UPLOADS.get(upload.r2_key as string);
    
    if (!object) {
      return c.json({ error: 'File not found in storage' }, 404);
    }
    
    // Return file
    return new Response(object.body, {
      headers: {
        'Content-Type': upload.content_type as string,
        'Content-Disposition': `inline; filename="${upload.filename}"`,
        'Cache-Control': 'private, max-age=3600',
      },
    });
    
  } catch (error) {
    console.error('Error serving upload:', error);
    return c.json({ error: 'Failed to retrieve file' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// List Uploads for Ticket (Staff)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/ticket/:ticketId', async (c) => {
  const ticketId = c.req.param('ticketId');
  
  try {
    const uploads = await c.env.DB.prepare(`
      SELECT id, filename, content_type, size_bytes, upload_type, uploaded_at
      FROM uploads 
      WHERE ticket_id = ? AND size_bytes > 0
      ORDER BY uploaded_at DESC
    `).bind(ticketId).all();
    
    return c.json({
      ticketId,
      uploads: uploads.results,
      count: uploads.results.length,
    });
    
  } catch (error) {
    console.error('Error listing uploads:', error);
    return c.json({ error: 'Failed to list uploads' }, 500);
  }
});

export { app as uploadRoutes };
