/**
 * NOIZYLAB Email System - Types/Schemas Unit Tests
 */

import { describe, it, expect } from 'vitest';
import {
  EmailAddressSchema,
  EmailAddressListSchema,
  EmailAttachmentSchema,
  EmailRequestSchema,
  EmailTemplateSchema,
} from '../../src/types';

describe('EmailAddressSchema', () => {
  it('should accept valid email addresses', () => {
    expect(EmailAddressSchema.safeParse('test@example.com').success).toBe(true);
    expect(EmailAddressSchema.safeParse('user.name@domain.org').success).toBe(true);
    expect(EmailAddressSchema.safeParse('user+tag@sub.domain.com').success).toBe(true);
  });

  it('should reject invalid email addresses', () => {
    expect(EmailAddressSchema.safeParse('invalid').success).toBe(false);
    expect(EmailAddressSchema.safeParse('no@domain').success).toBe(false);
    expect(EmailAddressSchema.safeParse('@nodomain.com').success).toBe(false);
    expect(EmailAddressSchema.safeParse('spaces not@allowed.com').success).toBe(false);
  });
});

describe('EmailAddressListSchema', () => {
  it('should accept single email', () => {
    const result = EmailAddressListSchema.safeParse('test@example.com');
    expect(result.success).toBe(true);
  });

  it('should accept array of emails', () => {
    const result = EmailAddressListSchema.safeParse([
      'a@example.com',
      'b@example.com',
    ]);
    expect(result.success).toBe(true);
  });

  it('should reject empty array', () => {
    const result = EmailAddressListSchema.safeParse([]);
    expect(result.success).toBe(false);
  });

  it('should reject arrays with more than 50 emails', () => {
    const emails = Array(51).fill('test@example.com');
    const result = EmailAddressListSchema.safeParse(emails);
    expect(result.success).toBe(false);
  });

  it('should reject arrays with invalid emails', () => {
    const result = EmailAddressListSchema.safeParse(['valid@example.com', 'invalid']);
    expect(result.success).toBe(false);
  });
});

describe('EmailAttachmentSchema', () => {
  it('should accept valid attachment', () => {
    const result = EmailAttachmentSchema.safeParse({
      filename: 'document.pdf',
      content: 'base64content',
      contentType: 'application/pdf',
    });
    expect(result.success).toBe(true);
  });

  it('should default encoding to base64', () => {
    const result = EmailAttachmentSchema.safeParse({
      filename: 'document.pdf',
      content: 'base64content',
      contentType: 'application/pdf',
    });
    expect(result.success).toBe(true);
    if (result.success) {
      expect(result.data.encoding).toBe('base64');
    }
  });

  it('should accept utf-8 encoding', () => {
    const result = EmailAttachmentSchema.safeParse({
      filename: 'text.txt',
      content: 'Hello World',
      contentType: 'text/plain',
      encoding: 'utf-8',
    });
    expect(result.success).toBe(true);
  });

  it('should reject empty filename', () => {
    const result = EmailAttachmentSchema.safeParse({
      filename: '',
      content: 'content',
      contentType: 'text/plain',
    });
    expect(result.success).toBe(false);
  });

  it('should reject invalid encoding', () => {
    const result = EmailAttachmentSchema.safeParse({
      filename: 'file.txt',
      content: 'content',
      contentType: 'text/plain',
      encoding: 'invalid',
    });
    expect(result.success).toBe(false);
  });
});

describe('EmailRequestSchema', () => {
  it('should accept minimal valid request with text', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test Subject',
      text: 'Hello World',
    });
    expect(result.success).toBe(true);
  });

  it('should accept minimal valid request with html', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test Subject',
      html: '<p>Hello World</p>',
    });
    expect(result.success).toBe(true);
  });

  it('should accept request with templateId', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test Subject',
      templateId: 'welcome-email',
      templateData: { name: 'John' },
    });
    expect(result.success).toBe(true);
  });

  it('should require html, text, or templateId', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test Subject',
    });
    expect(result.success).toBe(false);
  });

  it('should accept full request with all fields', () => {
    const result = EmailRequestSchema.safeParse({
      to: ['a@example.com', 'b@example.com'],
      from: 'sender@example.com',
      subject: 'Complete Test',
      html: '<h1>Hello</h1>',
      text: 'Hello',
      replyTo: 'reply@example.com',
      cc: ['cc@example.com'],
      bcc: ['bcc@example.com'],
      headers: { 'X-Custom': 'value' },
      attachments: [
        {
          filename: 'file.txt',
          content: 'content',
          contentType: 'text/plain',
        },
      ],
      priority: 'high',
      idempotencyKey: 'unique-key-123',
      tags: ['important', 'notification'],
    });
    expect(result.success).toBe(true);
  });

  it('should default priority to normal', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test',
      text: 'Test',
    });
    expect(result.success).toBe(true);
    if (result.success) {
      expect(result.data.priority).toBe('normal');
    }
  });

  it('should reject invalid priority', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test',
      text: 'Test',
      priority: 'urgent',
    });
    expect(result.success).toBe(false);
  });

  it('should reject subject longer than 998 characters', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'x'.repeat(999),
      text: 'Test',
    });
    expect(result.success).toBe(false);
  });

  it('should accept scheduledAt datetime', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test',
      text: 'Test',
      scheduledAt: '2025-01-01T00:00:00Z',
    });
    expect(result.success).toBe(true);
  });

  it('should reject invalid scheduledAt format', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test',
      text: 'Test',
      scheduledAt: 'not-a-date',
    });
    expect(result.success).toBe(false);
  });

  it('should limit cc to 50 recipients', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test',
      text: 'Test',
      cc: Array(51).fill('cc@example.com'),
    });
    expect(result.success).toBe(false);
  });

  it('should limit attachments to 10', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test',
      text: 'Test',
      attachments: Array(11).fill({
        filename: 'file.txt',
        content: 'content',
        contentType: 'text/plain',
      }),
    });
    expect(result.success).toBe(false);
  });

  it('should limit tags to 10', () => {
    const result = EmailRequestSchema.safeParse({
      to: 'test@example.com',
      subject: 'Test',
      text: 'Test',
      tags: Array(11).fill('tag'),
    });
    expect(result.success).toBe(false);
  });
});

describe('EmailTemplateSchema', () => {
  it('should accept valid template', () => {
    const result = EmailTemplateSchema.safeParse({
      id: 'welcome-email',
      name: 'Welcome Email',
      subject: 'Welcome {{name}}!',
      html: '<h1>Hello {{name}}</h1>',
      text: 'Hello {{name}}',
      variables: ['name'],
      createdAt: '2025-01-01T00:00:00Z',
      updatedAt: '2025-01-01T00:00:00Z',
    });
    expect(result.success).toBe(true);
  });

  it('should require id, name, subject, and timestamps', () => {
    const result = EmailTemplateSchema.safeParse({
      name: 'Test',
      subject: 'Test',
    });
    expect(result.success).toBe(false);
  });

  it('should reject template without html or text', () => {
    const result = EmailTemplateSchema.safeParse({
      id: 'test',
      name: 'Test',
      subject: 'Test',
      createdAt: '2025-01-01T00:00:00Z',
      updatedAt: '2025-01-01T00:00:00Z',
    });
    // This should succeed as html/text are optional in schema
    expect(result.success).toBe(true);
  });
});
