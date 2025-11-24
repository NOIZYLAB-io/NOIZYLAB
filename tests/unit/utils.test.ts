/**
 * NOIZYLAB Email System - Utils Unit Tests
 */

import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import {
  generateMessageId,
  generateRequestId,
  generateRandomString,
  normalizeEmail,
  normalizeEmailList,
  isValidEmail,
  safeJsonParse,
  safeJsonStringify,
  sleep,
  retryWithBackoff,
  maskSensitiveData,
  maskEmail,
  truncate,
  deepClone,
  isProduction,
  now,
  getBase64Size,
  validateEnvVars,
  parseCommaSeparated,
  timeout,
} from '../../src/utils';

describe('Utils', () => {
  describe('generateMessageId', () => {
    it('should generate unique IDs', () => {
      const id1 = generateMessageId();
      const id2 = generateMessageId();
      expect(id1).not.toBe(id2);
    });

    it('should have correct prefix', () => {
      const id = generateMessageId();
      expect(id).toMatch(/^noizy_[a-z0-9]+_[a-z0-9]+$/);
    });

    it('should be consistent length', () => {
      const ids = Array.from({ length: 10 }, () => generateMessageId());
      const lengths = ids.map((id) => id.length);
      expect(Math.max(...lengths) - Math.min(...lengths)).toBeLessThanOrEqual(5);
    });
  });

  describe('generateRequestId', () => {
    it('should generate unique IDs', () => {
      const id1 = generateRequestId();
      const id2 = generateRequestId();
      expect(id1).not.toBe(id2);
    });

    it('should have correct prefix', () => {
      const id = generateRequestId();
      expect(id).toMatch(/^req_[a-z0-9]+_[a-z0-9]+$/);
    });
  });

  describe('generateRandomString', () => {
    it('should generate string of correct length', () => {
      const str = generateRandomString(10);
      expect(str).toHaveLength(10);
    });

    it('should only contain lowercase alphanumeric characters', () => {
      const str = generateRandomString(100);
      expect(str).toMatch(/^[a-z0-9]+$/);
    });

    it('should generate different strings', () => {
      const str1 = generateRandomString(20);
      const str2 = generateRandomString(20);
      expect(str1).not.toBe(str2);
    });
  });

  describe('normalizeEmail', () => {
    it('should lowercase email', () => {
      expect(normalizeEmail('Test@Example.COM')).toBe('test@example.com');
    });

    it('should trim whitespace', () => {
      expect(normalizeEmail('  test@example.com  ')).toBe('test@example.com');
    });

    it('should handle both', () => {
      expect(normalizeEmail('  TEST@EXAMPLE.COM  ')).toBe('test@example.com');
    });
  });

  describe('normalizeEmailList', () => {
    it('should handle string input', () => {
      const result = normalizeEmailList('Test@Example.com');
      expect(result).toEqual(['test@example.com']);
    });

    it('should handle array input', () => {
      const result = normalizeEmailList(['Test@Example.com', 'Other@Test.com']);
      expect(result).toEqual(['test@example.com', 'other@test.com']);
    });
  });

  describe('isValidEmail', () => {
    it('should validate correct emails', () => {
      expect(isValidEmail('test@example.com')).toBe(true);
      expect(isValidEmail('user.name@domain.org')).toBe(true);
      expect(isValidEmail('user+tag@example.co.uk')).toBe(true);
    });

    it('should reject invalid emails', () => {
      expect(isValidEmail('invalid')).toBe(false);
      expect(isValidEmail('invalid@')).toBe(false);
      expect(isValidEmail('@domain.com')).toBe(false);
      expect(isValidEmail('no spaces@domain.com')).toBe(false);
    });
  });

  describe('safeJsonParse', () => {
    it('should parse valid JSON', () => {
      expect(safeJsonParse('{"key":"value"}')).toEqual({ key: 'value' });
      expect(safeJsonParse('[1,2,3]')).toEqual([1, 2, 3]);
    });

    it('should return null for invalid JSON', () => {
      expect(safeJsonParse('invalid')).toBeNull();
      expect(safeJsonParse('{broken')).toBeNull();
    });
  });

  describe('safeJsonStringify', () => {
    it('should stringify valid values', () => {
      expect(safeJsonStringify({ key: 'value' })).toBe('{"key":"value"}');
      expect(safeJsonStringify([1, 2, 3])).toBe('[1,2,3]');
    });

    it('should handle circular references', () => {
      const obj: Record<string, unknown> = { a: 1 };
      obj['self'] = obj;
      expect(safeJsonStringify(obj)).toBeNull();
    });
  });

  describe('sleep', () => {
    it('should wait for specified duration', async () => {
      const start = Date.now();
      await sleep(100);
      const duration = Date.now() - start;
      expect(duration).toBeGreaterThanOrEqual(90);
      expect(duration).toBeLessThan(200);
    });
  });

  describe('retryWithBackoff', () => {
    it('should succeed on first try', async () => {
      const fn = vi.fn().mockResolvedValue('success');
      const result = await retryWithBackoff(fn);
      expect(result).toBe('success');
      expect(fn).toHaveBeenCalledTimes(1);
    });

    it('should retry on failure', async () => {
      const fn = vi
        .fn()
        .mockRejectedValueOnce(new Error('fail'))
        .mockResolvedValue('success');

      const result = await retryWithBackoff(fn, {
        maxRetries: 3,
        baseDelayMs: 10,
      });

      expect(result).toBe('success');
      expect(fn).toHaveBeenCalledTimes(2);
    });

    it('should throw after max retries', async () => {
      const fn = vi.fn().mockRejectedValue(new Error('always fails'));

      await expect(
        retryWithBackoff(fn, { maxRetries: 2, baseDelayMs: 10 })
      ).rejects.toThrow('always fails');

      expect(fn).toHaveBeenCalledTimes(3);
    });

    it('should respect shouldRetry predicate', async () => {
      const fn = vi.fn().mockRejectedValue(new Error('do not retry'));

      await expect(
        retryWithBackoff(fn, {
          maxRetries: 3,
          baseDelayMs: 10,
          shouldRetry: () => false,
        })
      ).rejects.toThrow('do not retry');

      expect(fn).toHaveBeenCalledTimes(1);
    });
  });

  describe('maskSensitiveData', () => {
    it('should mask middle characters', () => {
      expect(maskSensitiveData('1234567890')).toBe('1234****7890');
    });

    it('should mask short strings completely', () => {
      expect(maskSensitiveData('abc')).toBe('***');
    });

    it('should respect visibleChars parameter', () => {
      expect(maskSensitiveData('1234567890', 2)).toBe('12******90');
    });
  });

  describe('maskEmail', () => {
    it('should mask local part of email', () => {
      expect(maskEmail('test@example.com')).toBe('t**t@example.com');
    });

    it('should handle short local parts', () => {
      expect(maskEmail('ab@example.com')).toBe('**@example.com');
    });

    it('should handle invalid emails', () => {
      expect(maskEmail('notanemail')).toBe('nota****mail');
    });
  });

  describe('truncate', () => {
    it('should not truncate short strings', () => {
      expect(truncate('hello', 10)).toBe('hello');
    });

    it('should truncate long strings', () => {
      expect(truncate('hello world', 8)).toBe('hello...');
    });

    it('should use custom suffix', () => {
      expect(truncate('hello world', 8, '…')).toBe('hello w…');
    });
  });

  describe('deepClone', () => {
    it('should create independent copy', () => {
      const original = { a: { b: 1 } };
      const clone = deepClone(original);
      clone.a.b = 2;
      expect(original.a.b).toBe(1);
    });

    it('should clone arrays', () => {
      const original = [1, [2, 3]];
      const clone = deepClone(original);
      (clone[1] as number[])[0] = 99;
      expect((original[1] as number[])[0]).toBe(2);
    });
  });

  describe('isProduction', () => {
    it('should return true for production', () => {
      expect(isProduction({ ENVIRONMENT: 'production' })).toBe(true);
    });

    it('should return false for other environments', () => {
      expect(isProduction({ ENVIRONMENT: 'development' })).toBe(false);
      expect(isProduction({ ENVIRONMENT: 'staging' })).toBe(false);
      expect(isProduction({})).toBe(false);
    });
  });

  describe('now', () => {
    it('should return ISO date string', () => {
      const result = now();
      expect(result).toMatch(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z$/);
    });
  });

  describe('getBase64Size', () => {
    it('should calculate correct size', () => {
      // "Hello" in base64 is "SGVsbG8="
      expect(getBase64Size('SGVsbG8=')).toBe(5);
    });

    it('should handle strings without padding', () => {
      // "Hi" in base64 is "SGk="
      expect(getBase64Size('SGk=')).toBe(2);
    });
  });

  describe('validateEnvVars', () => {
    it('should return valid for all present vars', () => {
      const result = validateEnvVars({ A: '1', B: '2' }, ['A', 'B']);
      expect(result.valid).toBe(true);
      expect(result.missing).toEqual([]);
    });

    it('should return missing vars', () => {
      const result = validateEnvVars({ A: '1' }, ['A', 'B', 'C']);
      expect(result.valid).toBe(false);
      expect(result.missing).toEqual(['B', 'C']);
    });

    it('should treat empty strings as missing', () => {
      const result = validateEnvVars({ A: '' }, ['A']);
      expect(result.valid).toBe(false);
      expect(result.missing).toEqual(['A']);
    });
  });

  describe('parseCommaSeparated', () => {
    it('should parse comma-separated string', () => {
      expect(parseCommaSeparated('a, b, c')).toEqual(['a', 'b', 'c']);
    });

    it('should handle empty values', () => {
      expect(parseCommaSeparated('')).toEqual([]);
      expect(parseCommaSeparated(undefined)).toEqual([]);
    });

    it('should trim whitespace', () => {
      expect(parseCommaSeparated('  a  ,  b  ,  c  ')).toEqual(['a', 'b', 'c']);
    });

    it('should filter empty items', () => {
      expect(parseCommaSeparated('a,,b,,c')).toEqual(['a', 'b', 'c']);
    });
  });

  describe('timeout', () => {
    it('should resolve if promise completes in time', async () => {
      const result = await timeout(Promise.resolve('done'), 1000);
      expect(result).toBe('done');
    });

    it('should reject if promise times out', async () => {
      const slowPromise = new Promise((resolve) => setTimeout(resolve, 1000));
      await expect(timeout(slowPromise, 10)).rejects.toThrow('timed out');
    });

    it('should use custom message', async () => {
      const slowPromise = new Promise((resolve) => setTimeout(resolve, 1000));
      await expect(timeout(slowPromise, 10, 'Custom timeout')).rejects.toThrow(
        'Custom timeout'
      );
    });
  });
});
