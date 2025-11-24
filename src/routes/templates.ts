/**
 * NOIZYLAB Email System - Template Routes
 * API endpoints for email template management
 */

import { Hono } from 'hono';
import { z } from 'zod';
import type { EmailTemplate } from '../types';
import {
  isNoizylabError,
  toNoizylabError,
  ValidationError,
  TemplateNotFoundError,
} from '../errors';
import { generateRequestId, now } from '../utils';

/**
 * Template creation schema
 */
const CreateTemplateSchema = z.object({
  id: z.string().min(1).max(100),
  name: z.string().min(1).max(255),
  subject: z.string().min(1).max(998),
  html: z.string().max(10_000_000).optional(),
  text: z.string().max(10_000_000).optional(),
  variables: z.array(z.string()).optional(),
}).refine(
  (data) => data.html !== undefined || data.text !== undefined,
  { message: 'Either html or text must be provided' }
);

/**
 * Template update schema
 */
const UpdateTemplateSchema = z.object({
  name: z.string().min(1).max(255).optional(),
  subject: z.string().min(1).max(998).optional(),
  html: z.string().max(10_000_000).optional(),
  text: z.string().max(10_000_000).optional(),
  variables: z.array(z.string()).optional(),
});

/**
 * Template preview schema
 */
const PreviewTemplateSchema = z.object({
  data: z.record(z.unknown()).optional(),
});

/**
 * Context type with template engine
 */
interface TemplateContext {
  Variables: {
    templateEngine: import('../services/template-engine').TemplateEngine;
    requestId: string;
  };
}

const templateRoutes = new Hono<TemplateContext>();

/**
 * POST /templates - Create a new template
 */
templateRoutes.post('/', async (c) => {
  const requestId = c.get('requestId');
  const templateEngine = c.get('templateEngine');

  try {
    const body = await c.req.json();
    const validation = CreateTemplateSchema.safeParse(body);

    if (!validation.success) {
      throw new ValidationError('Invalid template data', {
        errors: validation.error.errors.map((e) => ({
          path: e.path.join('.'),
          message: e.message,
        })),
      });
    }

    const templateData = validation.data;

    // Validate template syntax
    if (templateData.html !== undefined) {
      const htmlValidation = templateEngine.validateTemplateSyntax(templateData.html);
      if (!htmlValidation.valid) {
        throw new ValidationError('Invalid HTML template syntax', {
          errors: htmlValidation.errors,
        });
      }
    }

    if (templateData.text !== undefined) {
      const textValidation = templateEngine.validateTemplateSyntax(templateData.text);
      if (!textValidation.valid) {
        throw new ValidationError('Invalid text template syntax', {
          errors: textValidation.errors,
        });
      }
    }

    // Extract variables if not provided
    const variables = templateData.variables ?? [
      ...templateEngine.extractVariables(templateData.subject),
      ...(templateData.html !== undefined ? templateEngine.extractVariables(templateData.html) : []),
      ...(templateData.text !== undefined ? templateEngine.extractVariables(templateData.text) : []),
    ];

    const template = await templateEngine.saveTemplate({
      ...templateData,
      variables: [...new Set(variables)],
    });

    return c.json(
      {
        success: true,
        data: template,
        meta: { requestId, timestamp: now() },
      },
      201
    );
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

/**
 * GET /templates - List all templates
 */
templateRoutes.get('/', async (c) => {
  const requestId = c.get('requestId');
  const templateEngine = c.get('templateEngine');

  const limit = parseInt(c.req.query('limit') ?? '100', 10);
  const cursor = c.req.query('cursor');

  try {
    const { templates, cursor: nextCursor } = await templateEngine.listTemplates({
      limit: Math.min(limit, 100),
      cursor,
    });

    return c.json({
      success: true,
      data: templates.map((t) => ({
        id: t.id,
        name: t.name,
        subject: t.subject,
        variables: t.variables,
        createdAt: t.createdAt,
        updatedAt: t.updatedAt,
      })),
      meta: {
        requestId,
        timestamp: now(),
        pagination: {
          cursor: nextCursor,
          hasMore: nextCursor !== undefined,
        },
      },
    });
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

/**
 * GET /templates/:id - Get a template by ID
 */
templateRoutes.get('/:id', async (c) => {
  const requestId = c.get('requestId');
  const templateEngine = c.get('templateEngine');
  const templateId = c.req.param('id');

  try {
    const template = await templateEngine.getTemplate(templateId);

    return c.json({
      success: true,
      data: template,
      meta: { requestId, timestamp: now() },
    });
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

/**
 * PUT /templates/:id - Update a template
 */
templateRoutes.put('/:id', async (c) => {
  const requestId = c.get('requestId');
  const templateEngine = c.get('templateEngine');
  const templateId = c.req.param('id');

  try {
    // Get existing template
    const existing = await templateEngine.getTemplate(templateId);

    const body = await c.req.json();
    const validation = UpdateTemplateSchema.safeParse(body);

    if (!validation.success) {
      throw new ValidationError('Invalid template data', {
        errors: validation.error.errors.map((e) => ({
          path: e.path.join('.'),
          message: e.message,
        })),
      });
    }

    const updates = validation.data;

    // Validate template syntax
    if (updates.html !== undefined) {
      const htmlValidation = templateEngine.validateTemplateSyntax(updates.html);
      if (!htmlValidation.valid) {
        throw new ValidationError('Invalid HTML template syntax', {
          errors: htmlValidation.errors,
        });
      }
    }

    if (updates.text !== undefined) {
      const textValidation = templateEngine.validateTemplateSyntax(updates.text);
      if (!textValidation.valid) {
        throw new ValidationError('Invalid text template syntax', {
          errors: textValidation.errors,
        });
      }
    }

    const template = await templateEngine.saveTemplate({
      ...existing,
      ...updates,
      id: templateId,
    });

    return c.json({
      success: true,
      data: template,
      meta: { requestId, timestamp: now() },
    });
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

/**
 * DELETE /templates/:id - Delete a template
 */
templateRoutes.delete('/:id', async (c) => {
  const requestId = c.get('requestId');
  const templateEngine = c.get('templateEngine');
  const templateId = c.req.param('id');

  try {
    // Verify template exists
    await templateEngine.getTemplate(templateId);

    await templateEngine.deleteTemplate(templateId);

    return c.json({
      success: true,
      data: { deleted: true },
      meta: { requestId, timestamp: now() },
    });
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

/**
 * POST /templates/:id/preview - Preview a rendered template
 */
templateRoutes.post('/:id/preview', async (c) => {
  const requestId = c.get('requestId');
  const templateEngine = c.get('templateEngine');
  const templateId = c.req.param('id');

  try {
    const body = await c.req.json();
    const validation = PreviewTemplateSchema.safeParse(body);

    if (!validation.success) {
      throw new ValidationError('Invalid preview data', {
        errors: validation.error.errors.map((e) => ({
          path: e.path.join('.'),
          message: e.message,
        })),
      });
    }

    const rendered = await templateEngine.renderById(templateId, validation.data.data ?? {});

    return c.json({
      success: true,
      data: {
        subject: rendered.subject,
        html: rendered.html,
        text: rendered.text,
      },
      meta: { requestId, timestamp: now() },
    });
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

export { templateRoutes };
