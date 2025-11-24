/**
 * NOIZYLAB Email System - Template Engine Service
 * Handles email template storage, retrieval, and rendering
 */

import type { EmailTemplate } from '../types';
import { TemplateNotFoundError, TemplateRenderError, ValidationError } from '../errors';
import { now } from '../utils';

/**
 * Template variable pattern: {{variableName}} or {{variableName|default}}
 */
const VARIABLE_PATTERN = /\{\{([^{}|]+)(?:\|([^{}]*))?\}\}/g;

/**
 * Conditional pattern: {{#if condition}}...{{/if}}
 */
const CONDITIONAL_PATTERN = /\{\{#if\s+([^{}]+)\}\}([\s\S]*?)\{\{\/if\}\}/g;

/**
 * Loop pattern: {{#each items}}...{{/each}}
 */
const LOOP_PATTERN = /\{\{#each\s+([^{}]+)\}\}([\s\S]*?)\{\{\/each\}\}/g;

/**
 * Template engine for email rendering
 */
export class TemplateEngine {
  private readonly kv: KVNamespace;
  private readonly keyPrefix: string;
  private readonly cache: Map<string, EmailTemplate>;
  private readonly cacheMaxAge: number;
  private readonly cacheTimestamps: Map<string, number>;

  constructor(kv: KVNamespace, options: { keyPrefix?: string; cacheMaxAge?: number } = {}) {
    this.kv = kv;
    this.keyPrefix = options.keyPrefix ?? 'template';
    this.cache = new Map();
    this.cacheMaxAge = options.cacheMaxAge ?? 300000; // 5 minutes default
    this.cacheTimestamps = new Map();
  }

  /**
   * Get a template by ID
   */
  async getTemplate(templateId: string): Promise<EmailTemplate> {
    // Check cache first
    const cached = this.getCached(templateId);
    if (cached !== null) {
      return cached;
    }

    // Fetch from KV
    const key = this.buildKey(templateId);
    const stored = await this.kv.get(key, 'json');

    if (stored === null) {
      throw new TemplateNotFoundError(templateId);
    }

    const template = stored as EmailTemplate;
    this.setCache(templateId, template);

    return template;
  }

  /**
   * Save a template
   */
  async saveTemplate(template: Omit<EmailTemplate, 'createdAt' | 'updatedAt'>): Promise<EmailTemplate> {
    const existing = await this.kv.get(this.buildKey(template.id), 'json');
    const timestamp = now();

    const fullTemplate: EmailTemplate = {
      ...template,
      createdAt: existing !== null ? (existing as EmailTemplate).createdAt : timestamp,
      updatedAt: timestamp,
    };

    await this.kv.put(this.buildKey(template.id), JSON.stringify(fullTemplate));
    this.setCache(template.id, fullTemplate);

    return fullTemplate;
  }

  /**
   * Delete a template
   */
  async deleteTemplate(templateId: string): Promise<void> {
    await this.kv.delete(this.buildKey(templateId));
    this.cache.delete(templateId);
    this.cacheTimestamps.delete(templateId);
  }

  /**
   * List all templates
   */
  async listTemplates(options: { limit?: number; cursor?: string } = {}): Promise<{
    templates: EmailTemplate[];
    cursor?: string;
  }> {
    const { limit = 100, cursor } = options;
    const listResult = await this.kv.list({
      prefix: `${this.keyPrefix}:`,
      limit,
      cursor,
    });

    const templates: EmailTemplate[] = [];
    for (const key of listResult.keys) {
      const template = await this.kv.get(key.name, 'json');
      if (template !== null) {
        templates.push(template as EmailTemplate);
      }
    }

    return {
      templates,
      cursor: listResult.list_complete ? undefined : listResult.cursor,
    };
  }

  /**
   * Render a template with provided data
   */
  render(template: EmailTemplate, data: Record<string, unknown>): { subject: string; html?: string; text?: string } {
    try {
      const subject = this.renderString(template.subject, data);
      const html = template.html !== undefined ? this.renderString(template.html, data) : undefined;
      const text = template.text !== undefined ? this.renderString(template.text, data) : undefined;

      return { subject, html, text };
    } catch (error) {
      if (error instanceof Error) {
        throw new TemplateRenderError(template.id, error.message);
      }
      throw new TemplateRenderError(template.id, 'Unknown render error');
    }
  }

  /**
   * Render a template by ID with provided data
   */
  async renderById(templateId: string, data: Record<string, unknown>): Promise<{ subject: string; html?: string; text?: string }> {
    const template = await this.getTemplate(templateId);
    return this.render(template, data);
  }

  /**
   * Validate template syntax
   */
  validateTemplateSyntax(content: string): { valid: boolean; errors: string[] } {
    const errors: string[] = [];

    // Check for unclosed conditionals
    const ifOpens = (content.match(/\{\{#if\s+[^{}]+\}\}/g) ?? []).length;
    const ifCloses = (content.match(/\{\{\/if\}\}/g) ?? []).length;
    if (ifOpens !== ifCloses) {
      errors.push(`Mismatched {{#if}} tags: ${ifOpens} opens, ${ifCloses} closes`);
    }

    // Check for unclosed loops
    const eachOpens = (content.match(/\{\{#each\s+[^{}]+\}\}/g) ?? []).length;
    const eachCloses = (content.match(/\{\{\/each\}\}/g) ?? []).length;
    if (eachOpens !== eachCloses) {
      errors.push(`Mismatched {{#each}} tags: ${eachOpens} opens, ${eachCloses} closes`);
    }

    // Check for invalid variable syntax
    const invalidVars = content.match(/\{\{[^{}]*\{[^{}]*\}\}/g);
    if (invalidVars !== null) {
      errors.push(`Invalid nested braces in template: ${invalidVars.join(', ')}`);
    }

    return {
      valid: errors.length === 0,
      errors,
    };
  }

  /**
   * Extract variables from template content
   */
  extractVariables(content: string): string[] {
    const variables = new Set<string>();

    // Extract from variable patterns
    let match;
    while ((match = VARIABLE_PATTERN.exec(content)) !== null) {
      const varName = match[1];
      if (varName !== undefined) {
        variables.add(varName.trim());
      }
    }

    // Reset regex state
    VARIABLE_PATTERN.lastIndex = 0;

    // Extract from conditionals
    while ((match = CONDITIONAL_PATTERN.exec(content)) !== null) {
      const condition = match[1];
      if (condition !== undefined) {
        variables.add(condition.trim());
      }
    }

    // Reset regex state
    CONDITIONAL_PATTERN.lastIndex = 0;

    // Extract from loops
    while ((match = LOOP_PATTERN.exec(content)) !== null) {
      const loopVar = match[1];
      if (loopVar !== undefined) {
        variables.add(loopVar.trim());
      }
    }

    // Reset regex state
    LOOP_PATTERN.lastIndex = 0;

    return Array.from(variables);
  }

  /**
   * Render a string with variable substitution
   */
  private renderString(content: string, data: Record<string, unknown>): string {
    let result = content;

    // Process loops first
    result = this.processLoops(result, data);

    // Process conditionals
    result = this.processConditionals(result, data);

    // Process variables
    result = this.processVariables(result, data);

    return result;
  }

  /**
   * Process loop patterns
   */
  private processLoops(content: string, data: Record<string, unknown>): string {
    return content.replace(LOOP_PATTERN, (_match, loopVar: string, loopContent: string) => {
      const items = this.getValue(data, loopVar.trim());

      if (!Array.isArray(items)) {
        return '';
      }

      return items
        .map((item, index) => {
          const itemData: Record<string, unknown> = {
            ...data,
            '@index': index,
            '@first': index === 0,
            '@last': index === items.length - 1,
          };

          if (typeof item === 'object' && item !== null) {
            Object.assign(itemData, item);
          } else {
            itemData['this'] = item;
          }

          return this.renderString(loopContent, itemData);
        })
        .join('');
    });
  }

  /**
   * Process conditional patterns
   */
  private processConditionals(content: string, data: Record<string, unknown>): string {
    return content.replace(CONDITIONAL_PATTERN, (_match, condition: string, conditionalContent: string) => {
      const value = this.getValue(data, condition.trim());
      const isTruthy = this.isTruthy(value);

      return isTruthy ? this.renderString(conditionalContent, data) : '';
    });
  }

  /**
   * Process variable patterns
   */
  private processVariables(content: string, data: Record<string, unknown>): string {
    return content.replace(VARIABLE_PATTERN, (_match, varName: string, defaultValue?: string) => {
      const value = this.getValue(data, varName.trim());

      if (value === undefined || value === null) {
        return defaultValue ?? '';
      }

      return this.escapeHtml(String(value));
    });
  }

  /**
   * Get a value from data object using dot notation
   */
  private getValue(data: Record<string, unknown>, path: string): unknown {
    const parts = path.split('.');
    let current: unknown = data;

    for (const part of parts) {
      if (current === null || current === undefined) {
        return undefined;
      }
      if (typeof current !== 'object') {
        return undefined;
      }
      current = (current as Record<string, unknown>)[part];
    }

    return current;
  }

  /**
   * Check if a value is truthy for conditionals
   */
  private isTruthy(value: unknown): boolean {
    if (value === null || value === undefined) {
      return false;
    }
    if (typeof value === 'boolean') {
      return value;
    }
    if (typeof value === 'number') {
      return value !== 0;
    }
    if (typeof value === 'string') {
      return value !== '';
    }
    if (Array.isArray(value)) {
      return value.length > 0;
    }
    return true;
  }

  /**
   * Escape HTML special characters
   */
  private escapeHtml(str: string): string {
    const htmlEscapes: Record<string, string> = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#x27;',
    };
    return str.replace(/[&<>"']/g, (char) => htmlEscapes[char] ?? char);
  }

  private buildKey(templateId: string): string {
    return `${this.keyPrefix}:${templateId}`;
  }

  private getCached(templateId: string): EmailTemplate | null {
    const timestamp = this.cacheTimestamps.get(templateId);
    if (timestamp === undefined || Date.now() - timestamp > this.cacheMaxAge) {
      this.cache.delete(templateId);
      this.cacheTimestamps.delete(templateId);
      return null;
    }
    return this.cache.get(templateId) ?? null;
  }

  private setCache(templateId: string, template: EmailTemplate): void {
    this.cache.set(templateId, template);
    this.cacheTimestamps.set(templateId, Date.now());
  }
}

/**
 * Create template engine from environment
 */
export function createTemplateEngine(kv: KVNamespace): TemplateEngine {
  return new TemplateEngine(kv);
}
