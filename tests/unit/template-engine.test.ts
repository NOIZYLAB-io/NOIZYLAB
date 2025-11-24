/**
 * NOIZYLAB Email System - Template Engine Unit Tests
 */

import { describe, it, expect, beforeEach, vi } from 'vitest';
import { env } from 'cloudflare:test';
import { TemplateEngine } from '../../src/services/template-engine';
import { TemplateNotFoundError, TemplateRenderError } from '../../src/errors';

describe('TemplateEngine', () => {
  let engine: TemplateEngine;
  let mockKV: KVNamespace;

  beforeEach(() => {
    mockKV = env.EMAIL_KV;
    engine = new TemplateEngine(mockKV);
  });

  describe('saveTemplate and getTemplate', () => {
    it('should save and retrieve a template', async () => {
      const template = {
        id: 'welcome',
        name: 'Welcome Email',
        subject: 'Welcome to {{appName}}',
        html: '<h1>Hello {{name}}!</h1>',
        text: 'Hello {{name}}!',
      };

      const saved = await engine.saveTemplate(template);

      expect(saved.id).toBe('welcome');
      expect(saved.createdAt).toBeDefined();
      expect(saved.updatedAt).toBeDefined();

      const retrieved = await engine.getTemplate('welcome');
      expect(retrieved.name).toBe('Welcome Email');
      expect(retrieved.subject).toBe('Welcome to {{appName}}');
    });

    it('should throw TemplateNotFoundError for missing template', async () => {
      await expect(engine.getTemplate('nonexistent')).rejects.toThrow(TemplateNotFoundError);
    });

    it('should update existing template', async () => {
      await engine.saveTemplate({
        id: 'test',
        name: 'Original',
        subject: 'Original Subject',
        html: '<p>Original</p>',
      });

      const updated = await engine.saveTemplate({
        id: 'test',
        name: 'Updated',
        subject: 'Updated Subject',
        html: '<p>Updated</p>',
      });

      expect(updated.name).toBe('Updated');
      expect(updated.createdAt).toBeDefined();
    });
  });

  describe('deleteTemplate', () => {
    it('should delete a template', async () => {
      await engine.saveTemplate({
        id: 'to-delete',
        name: 'Delete Me',
        subject: 'Test',
        text: 'Test',
      });

      await engine.deleteTemplate('to-delete');

      await expect(engine.getTemplate('to-delete')).rejects.toThrow(TemplateNotFoundError);
    });
  });

  describe('render', () => {
    it('should render simple variables', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Hello {{name}}',
        html: '<p>Welcome, {{name}}!</p>',
        text: 'Welcome, {{name}}!',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const result = engine.render(template, { name: 'John' });

      expect(result.subject).toBe('Hello John');
      expect(result.html).toBe('<p>Welcome, John!</p>');
      expect(result.text).toBe('Welcome, John!');
    });

    it('should handle default values', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Hello {{name|Guest}}',
        html: '<p>{{greeting|Hello}}</p>',
        text: '{{greeting|Hello}}',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const result = engine.render(template, {});

      expect(result.subject).toBe('Hello Guest');
      expect(result.html).toBe('<p>Hello</p>');
    });

    it('should handle nested properties', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Order for {{user.name}}',
        html: '<p>{{order.item.name}} - ${{order.item.price}}</p>',
        text: '',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const result = engine.render(template, {
        user: { name: 'Alice' },
        order: { item: { name: 'Widget', price: '29.99' } },
      });

      expect(result.subject).toBe('Order for Alice');
      expect(result.html).toBe('<p>Widget - $29.99</p>');
    });

    it('should handle conditionals', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Notification',
        html: '{{#if premium}}<p>Premium feature!</p>{{/if}}',
        text: '',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const withPremium = engine.render(template, { premium: true });
      expect(withPremium.html).toBe('<p>Premium feature!</p>');

      const withoutPremium = engine.render(template, { premium: false });
      expect(withoutPremium.html).toBe('');
    });

    it('should handle loops', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Your Items',
        html: '<ul>{{#each items}}<li>{{name}}</li>{{/each}}</ul>',
        text: '',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const result = engine.render(template, {
        items: [{ name: 'Apple' }, { name: 'Banana' }, { name: 'Cherry' }],
      });

      expect(result.html).toBe('<ul><li>Apple</li><li>Banana</li><li>Cherry</li></ul>');
    });

    it('should provide loop metadata', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Test',
        html: '{{#each items}}{{@index}}:{{name}}{{#if @last}}.{{/if}}{{/each}}',
        text: '',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const result = engine.render(template, {
        items: [{ name: 'A' }, { name: 'B' }, { name: 'C' }],
      });

      expect(result.html).toBe('0:A1:B2:C.');
    });

    it('should escape HTML in variable values', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Test',
        html: '<p>{{content}}</p>',
        text: '',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const result = engine.render(template, {
        content: '<script>alert("xss")</script>',
      });

      expect(result.html).toBe('<p>&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;</p>');
    });

    it('should handle missing variables gracefully', () => {
      const template = {
        id: 'test',
        name: 'Test',
        subject: 'Hello {{name}}',
        html: '<p>{{undefined_var}}</p>',
        text: '',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };

      const result = engine.render(template, {});

      expect(result.subject).toBe('Hello ');
      expect(result.html).toBe('<p></p>');
    });
  });

  describe('validateTemplateSyntax', () => {
    it('should validate correct templates', () => {
      const result = engine.validateTemplateSyntax(
        '{{name}} {{#if active}}Active{{/if}} {{#each items}}{{name}}{{/each}}'
      );
      expect(result.valid).toBe(true);
      expect(result.errors).toHaveLength(0);
    });

    it('should detect unclosed if blocks', () => {
      const result = engine.validateTemplateSyntax('{{#if active}}Active');
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('Mismatched {{#if}}');
    });

    it('should detect unclosed each blocks', () => {
      const result = engine.validateTemplateSyntax('{{#each items}}Item');
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('Mismatched {{#each}}');
    });
  });

  describe('extractVariables', () => {
    it('should extract simple variables', () => {
      const vars = engine.extractVariables('Hello {{name}}, your order {{orderId}} is ready');
      expect(vars).toContain('name');
      expect(vars).toContain('orderId');
    });

    it('should extract variables from conditionals', () => {
      const vars = engine.extractVariables('{{#if premium}}Premium{{/if}}');
      expect(vars).toContain('premium');
    });

    it('should extract variables from loops', () => {
      const vars = engine.extractVariables('{{#each items}}{{name}}{{/each}}');
      expect(vars).toContain('items');
      expect(vars).toContain('name');
    });

    it('should deduplicate variables', () => {
      const vars = engine.extractVariables('{{name}} {{name}} {{name}}');
      expect(vars.filter((v) => v === 'name')).toHaveLength(1);
    });
  });

  describe('listTemplates', () => {
    it('should list all templates', async () => {
      await engine.saveTemplate({
        id: 'template-1',
        name: 'Template 1',
        subject: 'Test',
        text: 'Test',
      });

      await engine.saveTemplate({
        id: 'template-2',
        name: 'Template 2',
        subject: 'Test',
        text: 'Test',
      });

      const { templates } = await engine.listTemplates();
      const ids = templates.map((t) => t.id);

      expect(ids).toContain('template-1');
      expect(ids).toContain('template-2');
    });
  });

  describe('renderById', () => {
    it('should render a template by ID', async () => {
      await engine.saveTemplate({
        id: 'email-template',
        name: 'Email',
        subject: 'Hello {{name}}',
        html: '<p>Hi {{name}}!</p>',
        text: 'Hi {{name}}!',
      });

      const result = await engine.renderById('email-template', { name: 'World' });

      expect(result.subject).toBe('Hello World');
      expect(result.html).toBe('<p>Hi World!</p>');
    });

    it('should throw for non-existent template', async () => {
      await expect(engine.renderById('missing', {})).rejects.toThrow(TemplateNotFoundError);
    });
  });
});
