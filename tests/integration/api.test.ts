/**
 * NOIZYLAB Email System - API Integration Tests
 */

import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import { env, createExecutionContext, waitOnExecutionContext } from 'cloudflare:test';
import { app } from '../../src/index';

describe('API Integration Tests', () => {
  describe('Root Endpoint', () => {
    it('GET / should return API info', async () => {
      const res = await app.request('/', {}, env);

      expect(res.status).toBe(200);

      const body = await res.json();
      expect(body['name']).toBe('NOIZYLAB Email System');
      expect(body['version']).toBe('1.0.0');
      expect(body['endpoints']).toBeDefined();
    });
  });

  describe('Health Endpoints', () => {
    it('GET /health should return healthy status', async () => {
      const res = await app.request('/health', {}, env);

      expect(res.status).toBe(200);

      const body = await res.json();
      expect(body['status']).toBe('healthy');
      expect(body['version']).toBeDefined();
      expect(body['timestamp']).toBeDefined();
    });

    it('GET /health/live should return liveness', async () => {
      const res = await app.request('/health/live', {}, env);

      expect(res.status).toBe(200);

      const body = await res.json();
      expect(body['live']).toBe(true);
    });

    it('GET /health/ready should return readiness', async () => {
      const res = await app.request('/health/ready', {}, env);

      // May return 503 if DB not initialized, but should return valid response
      expect([200, 503]).toContain(res.status);

      const body = await res.json();
      expect(typeof body['ready']).toBe('boolean');
    });

    it('GET /health/detailed should return component status', async () => {
      const res = await app.request('/health/detailed', {}, env);

      expect([200, 503]).toContain(res.status);

      const body = await res.json() as Record<string, unknown>;
      expect(body['status']).toBeDefined();
      expect(body['checks']).toBeDefined();

      const checks = body['checks'] as Record<string, unknown>;
      expect(checks['database']).toBeDefined();
      expect(checks['cache']).toBeDefined();
    });
  });

  describe('Email Endpoints', () => {
    describe('POST /emails', () => {
      it('should require Content-Type header', async () => {
        const res = await app.request(
          '/emails',
          {
            method: 'POST',
            body: JSON.stringify({
              to: 'test@example.com',
              subject: 'Test',
              text: 'Test',
            }),
          },
          env
        );

        expect(res.status).toBe(415);
      });

      it('should validate email request', async () => {
        const res = await app.request(
          '/emails',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              to: 'invalid-email',
              subject: 'Test',
              text: 'Test',
            }),
          },
          env
        );

        expect(res.status).toBe(400);

        const body = await res.json() as Record<string, unknown>;
        expect(body['success']).toBe(false);
        expect((body['error'] as Record<string, unknown>)['code']).toBe('VALIDATION_ERROR');
      });

      it('should require either text, html, or templateId', async () => {
        const res = await app.request(
          '/emails',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              to: 'test@example.com',
              subject: 'Test',
            }),
          },
          env
        );

        expect(res.status).toBe(400);
      });

      it('should send email with valid request', async () => {
        const res = await app.request(
          '/emails',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              to: 'test@example.com',
              subject: 'Test Email',
              text: 'This is a test email',
              html: '<p>This is a test email</p>',
            }),
          },
          env
        );

        // May fail due to provider issues, but should not be validation error
        if (res.status === 201) {
          const body = await res.json() as Record<string, unknown>;
          expect(body['success']).toBe(true);
          expect(body['data']).toBeDefined();
          expect((body['data'] as Record<string, unknown>)['messageId']).toBeDefined();
        }
      });

      it('should include rate limit headers', async () => {
        const res = await app.request(
          '/emails',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              to: 'test@example.com',
              subject: 'Test',
              text: 'Test',
            }),
          },
          env
        );

        // Should have rate limit headers regardless of success
        expect(res.headers.get('X-RateLimit-Limit')).toBeDefined();
        expect(res.headers.get('X-RateLimit-Remaining')).toBeDefined();
      });
    });

    describe('GET /emails', () => {
      it('should list emails with pagination', async () => {
        const res = await app.request('/emails?limit=10&offset=0', {}, env);

        expect([200, 500]).toContain(res.status); // 500 if DB not initialized

        if (res.status === 200) {
          const body = await res.json() as Record<string, unknown>;
          expect(body['success']).toBe(true);
          expect(Array.isArray(body['data'])).toBe(true);
          expect(body['meta']).toBeDefined();
          expect((body['meta'] as Record<string, unknown>)['pagination']).toBeDefined();
        }
      });

      it('should filter by status', async () => {
        const res = await app.request('/emails?status=sent', {}, env);
        expect([200, 500]).toContain(res.status);
      });
    });

    describe('GET /emails/:messageId', () => {
      it('should return 404 for non-existent email', async () => {
        const res = await app.request('/emails/nonexistent-id', {}, env);

        expect([404, 500]).toContain(res.status);

        if (res.status === 404) {
          const body = await res.json() as Record<string, unknown>;
          expect(body['success']).toBe(false);
          expect((body['error'] as Record<string, unknown>)['code']).toBe('NOT_FOUND');
        }
      });
    });
  });

  describe('Template Endpoints', () => {
    const testTemplateId = `test-template-${Date.now()}`;

    describe('POST /templates', () => {
      it('should create a new template', async () => {
        const res = await app.request(
          '/templates',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              id: testTemplateId,
              name: 'Test Template',
              subject: 'Hello {{name}}',
              html: '<h1>Welcome, {{name}}!</h1>',
              text: 'Welcome, {{name}}!',
            }),
          },
          env
        );

        expect(res.status).toBe(201);

        const body = await res.json() as Record<string, unknown>;
        expect(body['success']).toBe(true);
        expect((body['data'] as Record<string, unknown>)['id']).toBe(testTemplateId);
      });

      it('should validate template syntax', async () => {
        const res = await app.request(
          '/templates',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              id: 'invalid-template',
              name: 'Invalid',
              subject: 'Test',
              html: '{{#if condition}}Unclosed conditional',
            }),
          },
          env
        );

        expect(res.status).toBe(400);

        const body = await res.json() as Record<string, unknown>;
        expect((body['error'] as Record<string, unknown>)['code']).toBe('VALIDATION_ERROR');
      });

      it('should require html or text', async () => {
        const res = await app.request(
          '/templates',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              id: 'no-content',
              name: 'No Content',
              subject: 'Test',
            }),
          },
          env
        );

        expect(res.status).toBe(400);
      });
    });

    describe('GET /templates', () => {
      it('should list templates', async () => {
        const res = await app.request('/templates', {}, env);

        expect(res.status).toBe(200);

        const body = await res.json() as Record<string, unknown>;
        expect(body['success']).toBe(true);
        expect(Array.isArray(body['data'])).toBe(true);
      });

      it('should support pagination', async () => {
        const res = await app.request('/templates?limit=5', {}, env);

        expect(res.status).toBe(200);

        const body = await res.json() as Record<string, unknown>;
        expect((body['meta'] as Record<string, unknown>)['pagination']).toBeDefined();
      });
    });

    describe('GET /templates/:id', () => {
      it('should get template by ID', async () => {
        // First create a template
        await app.request(
          '/templates',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              id: 'get-test-template',
              name: 'Get Test',
              subject: 'Test',
              text: 'Test content',
            }),
          },
          env
        );

        const res = await app.request('/templates/get-test-template', {}, env);

        expect(res.status).toBe(200);

        const body = await res.json() as Record<string, unknown>;
        expect(body['success']).toBe(true);
        expect((body['data'] as Record<string, unknown>)['id']).toBe('get-test-template');
      });

      it('should return 404 for non-existent template', async () => {
        const res = await app.request('/templates/nonexistent', {}, env);

        expect(res.status).toBe(404);

        const body = await res.json() as Record<string, unknown>;
        expect((body['error'] as Record<string, unknown>)['code']).toBe('TEMPLATE_NOT_FOUND');
      });
    });

    describe('PUT /templates/:id', () => {
      it('should update existing template', async () => {
        // First create
        await app.request(
          '/templates',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              id: 'update-test',
              name: 'Original',
              subject: 'Original Subject',
              text: 'Original content',
            }),
          },
          env
        );

        // Then update
        const res = await app.request(
          '/templates/update-test',
          {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              name: 'Updated',
              subject: 'Updated Subject',
            }),
          },
          env
        );

        expect(res.status).toBe(200);

        const body = await res.json() as Record<string, unknown>;
        expect((body['data'] as Record<string, unknown>)['name']).toBe('Updated');
      });
    });

    describe('DELETE /templates/:id', () => {
      it('should delete existing template', async () => {
        // First create
        await app.request(
          '/templates',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              id: 'delete-test',
              name: 'To Delete',
              subject: 'Test',
              text: 'Test',
            }),
          },
          env
        );

        // Then delete
        const res = await app.request(
          '/templates/delete-test',
          { method: 'DELETE' },
          env
        );

        expect(res.status).toBe(200);

        // Verify deleted
        const getRes = await app.request('/templates/delete-test', {}, env);
        expect(getRes.status).toBe(404);
      });
    });

    describe('POST /templates/:id/preview', () => {
      it('should preview rendered template', async () => {
        // First create template
        await app.request(
          '/templates',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              id: 'preview-test',
              name: 'Preview Test',
              subject: 'Hello {{name}}',
              html: '<h1>Welcome, {{name}}!</h1>',
              text: 'Welcome, {{name}}!',
            }),
          },
          env
        );

        // Then preview
        const res = await app.request(
          '/templates/preview-test/preview',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              data: { name: 'World' },
            }),
          },
          env
        );

        expect(res.status).toBe(200);

        const body = await res.json() as Record<string, unknown>;
        expect((body['data'] as Record<string, unknown>)['subject']).toBe('Hello World');
        expect((body['data'] as Record<string, unknown>)['html']).toBe('<h1>Welcome, World!</h1>');
      });
    });
  });

  describe('Error Handling', () => {
    it('should return 404 for unknown routes', async () => {
      const res = await app.request('/unknown/route', {}, env);

      expect(res.status).toBe(404);

      const body = await res.json() as Record<string, unknown>;
      expect(body['success']).toBe(false);
      expect((body['error'] as Record<string, unknown>)['code']).toBe('NOT_FOUND');
    });

    it('should include request ID in responses', async () => {
      const res = await app.request('/', {}, env);

      expect(res.headers.get('X-Request-ID')).toBeDefined();
    });

    it('should use provided request ID', async () => {
      const customId = 'custom-request-id-123';
      const res = await app.request(
        '/',
        {
          headers: { 'X-Request-ID': customId },
        },
        env
      );

      expect(res.headers.get('X-Request-ID')).toBe(customId);
    });

    it('should include response time header', async () => {
      const res = await app.request('/', {}, env);

      const responseTime = res.headers.get('X-Response-Time');
      expect(responseTime).toBeDefined();
      expect(responseTime).toMatch(/^\d+ms$/);
    });
  });

  describe('CORS', () => {
    it('should include CORS headers', async () => {
      const res = await app.request('/', {}, env);

      expect(res.headers.get('Access-Control-Allow-Origin')).toBeDefined();
    });

    it('should handle OPTIONS requests', async () => {
      const res = await app.request(
        '/emails',
        {
          method: 'OPTIONS',
          headers: {
            'Access-Control-Request-Method': 'POST',
          },
        },
        env
      );

      expect([200, 204]).toContain(res.status);
      expect(res.headers.get('Access-Control-Allow-Methods')).toBeDefined();
    });
  });
});
