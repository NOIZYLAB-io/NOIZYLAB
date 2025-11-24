/**
 * NOIZYLAB Email System - Utility Functions
 * Common utility functions used across the application
 */

/**
 * Generate a unique message ID
 * Format: noizy_{timestamp}_{random}
 */
export function generateMessageId(): string {
  const timestamp = Date.now().toString(36);
  const random = generateRandomString(12);
  return `noizy_${timestamp}_${random}`;
}

/**
 * Generate a unique request ID
 * Format: req_{timestamp}_{random}
 */
export function generateRequestId(): string {
  const timestamp = Date.now().toString(36);
  const random = generateRandomString(8);
  return `req_${timestamp}_${random}`;
}

/**
 * Generate a cryptographically secure random string
 */
export function generateRandomString(length: number): string {
  const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
  const array = new Uint8Array(length);
  crypto.getRandomValues(array);
  return Array.from(array, (byte) => chars[byte % chars.length]).join('');
}

/**
 * Normalize email address to lowercase and trim whitespace
 */
export function normalizeEmail(email: string): string {
  return email.toLowerCase().trim();
}

/**
 * Normalize a list of email addresses
 */
export function normalizeEmailList(emails: string | string[]): string[] {
  const list = Array.isArray(emails) ? emails : [emails];
  return list.map(normalizeEmail);
}

/**
 * Check if a string is a valid email address
 */
export function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Safely parse JSON with error handling
 */
export function safeJsonParse<T>(json: string): T | null {
  try {
    return JSON.parse(json) as T;
  } catch {
    return null;
  }
}

/**
 * Safely stringify JSON with error handling
 */
export function safeJsonStringify(value: unknown): string | null {
  try {
    return JSON.stringify(value);
  } catch {
    return null;
  }
}

/**
 * Sleep for a specified number of milliseconds
 */
export function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Retry a function with exponential backoff
 */
export async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  options: {
    maxRetries?: number;
    baseDelayMs?: number;
    maxDelayMs?: number;
    shouldRetry?: (error: unknown) => boolean;
  } = {}
): Promise<T> {
  const {
    maxRetries = 3,
    baseDelayMs = 1000,
    maxDelayMs = 30000,
    shouldRetry = () => true,
  } = options;

  let lastError: unknown;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error;

      if (attempt === maxRetries || !shouldRetry(error)) {
        throw error;
      }

      const delay = Math.min(baseDelayMs * Math.pow(2, attempt), maxDelayMs);
      const jitter = Math.random() * delay * 0.1;
      await sleep(delay + jitter);
    }
  }

  throw lastError;
}

/**
 * Calculate hash of a string using SHA-256
 */
export async function sha256(message: string): Promise<string> {
  const encoder = new TextEncoder();
  const data = encoder.encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map((b) => b.toString(16).padStart(2, '0')).join('');
}

/**
 * Mask sensitive data for logging
 */
export function maskSensitiveData(data: string, visibleChars: number = 4): string {
  if (data.length <= visibleChars * 2) {
    return '*'.repeat(data.length);
  }
  const start = data.slice(0, visibleChars);
  const end = data.slice(-visibleChars);
  const masked = '*'.repeat(Math.min(data.length - visibleChars * 2, 8));
  return `${start}${masked}${end}`;
}

/**
 * Mask email address for logging
 */
export function maskEmail(email: string): string {
  const [localPart, domain] = email.split('@');
  if (localPart === undefined || domain === undefined) {
    return maskSensitiveData(email);
  }
  const maskedLocal =
    localPart.length > 2
      ? `${localPart[0]}${'*'.repeat(localPart.length - 2)}${localPart[localPart.length - 1]}`
      : '*'.repeat(localPart.length);
  return `${maskedLocal}@${domain}`;
}

/**
 * Truncate a string to a maximum length
 */
export function truncate(str: string, maxLength: number, suffix: string = '...'): string {
  if (str.length <= maxLength) {
    return str;
  }
  return str.slice(0, maxLength - suffix.length) + suffix;
}

/**
 * Deep clone an object
 */
export function deepClone<T>(obj: T): T {
  return JSON.parse(JSON.stringify(obj)) as T;
}

/**
 * Check if we're in a production environment
 */
export function isProduction(env: { ENVIRONMENT?: string }): boolean {
  return env.ENVIRONMENT === 'production';
}

/**
 * Get current timestamp in ISO format
 */
export function now(): string {
  return new Date().toISOString();
}

/**
 * Calculate size of a base64 encoded string in bytes
 */
export function getBase64Size(base64: string): number {
  const padding = (base64.match(/=/g) ?? []).length;
  return Math.floor((base64.length * 3) / 4) - padding;
}

/**
 * Validate that all required environment variables are set
 */
export function validateEnvVars(
  env: Record<string, unknown>,
  required: string[]
): { valid: boolean; missing: string[] } {
  const missing = required.filter(
    (key) => env[key] === undefined || env[key] === null || env[key] === ''
  );
  return {
    valid: missing.length === 0,
    missing,
  };
}

/**
 * Parse comma-separated string into array
 */
export function parseCommaSeparated(value: string | undefined): string[] {
  if (value === undefined || value.trim() === '') {
    return [];
  }
  return value
    .split(',')
    .map((s) => s.trim())
    .filter((s) => s !== '');
}

/**
 * Create a timeout promise that rejects after specified time
 */
export function timeout<T>(promise: Promise<T>, ms: number, message?: string): Promise<T> {
  return Promise.race([
    promise,
    new Promise<T>((_, reject) =>
      setTimeout(() => reject(new Error(message ?? `Operation timed out after ${ms}ms`)), ms)
    ),
  ]);
}
