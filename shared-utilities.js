/**
 * SHARED UTILITIES LIBRARY
 * Common functions used across all Cloudflare Workers
 * 
 * Features:
 * - Date/time utilities
 * - String helpers
 * - Validation functions
 * - API response builders
 * - Error handling
 * - Logging helpers
 * - Security utilities
 * - Performance helpers
 */

// ============================================================================
// DATE & TIME UTILITIES
// ============================================================================

export const DateUtils = {
  // Get current timestamp
  now() {
    return new Date().toISOString();
  },
  
  // Add days to date
  addDays(date, days) {
    const result = new Date(date);
    result.setDate(result.setDate() + days);
    return result.toISOString();
  },
  
  // Format date for display
  formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  },
  
  // Get business days from now
  getBusinessDays(days) {
    const result = new Date();
    let added = 0;
    
    while (added < days) {
      result.setDate(result.getDate() + 1);
      // Skip weekends
      if (result.getDay() !== 0 && result.getDay() !== 6) {
        added++;
      }
    }
    
    return result.toISOString();
  },
  
  // Check if date is within range
  isWithinDays(date, days) {
    const targetDate = new Date(date);
    const now = new Date();
    const diffTime = Math.abs(targetDate - now);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays <= days;
  }
};

// ============================================================================
// STRING UTILITIES
// ============================================================================

export const StringUtils = {
  // Generate random ID
  generateId(prefix = 'ID', length = 8) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let id = prefix + '-';
    for (let i = 0; i < length; i++) {
      id += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return id;
  },
  
  // Truncate string
  truncate(str, maxLength) {
    if (str.length <= maxLength) return str;
    return str.substring(0, maxLength) + '...';
  },
  
  // Slugify string
  slugify(str) {
    return str
      .toLowerCase()
      .replace(/[^\w\s-]/g, '')
      .replace(/[\s_-]+/g, '-')
      .replace(/^-+|-+$/g, '');
  },
  
  // Capitalize first letter
  capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  },
  
  // Strip HTML tags
  stripHtml(html) {
    return html.replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();
  },
  
  // Format phone number
  formatPhone(phone) {
    const cleaned = phone.replace(/\D/g, '');
    const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
      return `(${match[1]}) ${match[2]}-${match[3]}`;
    }
    return phone;
  }
};

// ============================================================================
// VALIDATION UTILITIES
// ============================================================================

export const ValidationUtils = {
  // Validate email
  isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  },
  
  // Validate phone
  isValidPhone(phone) {
    const cleaned = phone.replace(/\D/g, '');
    return cleaned.length === 10 || cleaned.length === 11;
  },
  
  // Validate URL
  isValidUrl(url) {
    try {
      new URL(url);
      return true;
    } catch {
      return false;
    }
  },
  
  // Validate required fields
  validateRequired(data, fields) {
    const missing = [];
    for (const field of fields) {
      if (!data[field]) {
        missing.push(field);
      }
    }
    return { valid: missing.length === 0, missing };
  },
  
  // Sanitize input
  sanitize(str) {
    return str
      .replace(/[<>]/g, '')
      .trim();
  }
};

// ============================================================================
// API RESPONSE BUILDERS
// ============================================================================

export const ResponseUtils = {
  // Success response
  success(data, corsHeaders = {}) {
    return new Response(JSON.stringify({
      success: true,
      ...data
    }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        ...corsHeaders
      }
    });
  },
  
  // Error response
  error(message, status = 400, corsHeaders = {}) {
    return new Response(JSON.stringify({
      success: false,
      error: message
    }), {
      status,
      headers: {
        'Content-Type': 'application/json',
        ...corsHeaders
      }
    });
  },
  
  // Not found response
  notFound(corsHeaders = {}) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Not found'
    }), {
      status: 404,
      headers: {
        'Content-Type': 'application/json',
        ...corsHeaders
      }
    });
  },
  
  // Unauthorized response
  unauthorized(corsHeaders = {}) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Unauthorized'
    }), {
      status: 401,
      headers: {
        'Content-Type': 'application/json',
        ...corsHeaders
      }
    });
  },
  
  // Rate limit response
  rateLimited(corsHeaders = {}) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Rate limit exceeded'
    }), {
      status: 429,
      headers: {
        'Content-Type': 'application/json',
        'Retry-After': '60',
        ...corsHeaders
      }
    });
  },
  
  // HTML response
  html(content) {
    return new Response(content, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });
  }
};

// ============================================================================
// ERROR HANDLING
// ============================================================================

export const ErrorUtils = {
  // Wrap async handler with error handling
  async wrapHandler(handler, corsHeaders = {}) {
    try {
      return await handler();
    } catch (error) {
      console.error('Handler error:', error);
      return ResponseUtils.error(error.message, 500, corsHeaders);
    }
  },
  
  // Log error to KV
  async logError(env, error, context = {}) {
    const errorId = StringUtils.generateId('ERR', 12);
    
    try {
      await env.ERROR_LOGS.put(errorId, JSON.stringify({
        id: errorId,
        message: error.message,
        stack: error.stack,
        context,
        timestamp: DateUtils.now()
      }), {
        expirationTtl: 86400 * 7 // 7 days
      });
    } catch (logError) {
      console.error('Failed to log error:', logError);
    }
    
    return errorId;
  }
};

// ============================================================================
// SECURITY UTILITIES
// ============================================================================

export const SecurityUtils = {
  // Generate secure token
  generateToken(length = 32) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let token = '';
    for (let i = 0; i < length; i++) {
      token += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return token;
  },
  
  // Hash string (simple)
  simpleHash(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      const char = str.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash;
    }
    return Math.abs(hash).toString(36);
  },
  
  // Verify API key format
  isValidApiKey(key) {
    return /^[a-zA-Z0-9_-]{20,}$/.test(key);
  },
  
  // Rate limit check
  async checkRateLimit(env, identifier, limit = 100, window = 3600) {
    const key = `ratelimit:${identifier}:${Math.floor(Date.now() / (window * 1000))}`;
    
    const countStr = await env.CACHE.get(key);
    const count = countStr ? parseInt(countStr) : 0;
    
    if (count >= limit) {
      return { allowed: false, remaining: 0 };
    }
    
    await env.CACHE.put(key, String(count + 1), {
      expirationTtl: window
    });
    
    return { allowed: true, remaining: limit - count - 1 };
  }
};

// ============================================================================
// PERFORMANCE UTILITIES
// ============================================================================

export const PerformanceUtils = {
  // Measure execution time
  async measureTime(fn) {
    const start = Date.now();
    const result = await fn();
    const duration = Date.now() - start;
    return { result, duration };
  },
  
  // Cache wrapper
  async withCache(env, key, ttl, fn) {
    // Check cache first
    const cached = await env.CACHE.get(key);
    if (cached) {
      return { data: JSON.parse(cached), fromCache: true };
    }
    
    // Execute function
    const data = await fn();
    
    // Store in cache
    await env.CACHE.put(key, JSON.stringify(data), {
      expirationTtl: ttl
    });
    
    return { data, fromCache: false };
  },
  
  // Batch operations
  async batch(items, fn, batchSize = 10) {
    const results = [];
    
    for (let i = 0; i < items.length; i += batchSize) {
      const batch = items.slice(i, i + batchSize);
      const batchResults = await Promise.all(batch.map(fn));
      results.push(...batchResults);
    }
    
    return results;
  }
};

// ============================================================================
// LOGGING UTILITIES
// ============================================================================

export const LogUtils = {
  // Structured log
  log(level, message, data = {}) {
    console.log(JSON.stringify({
      level,
      message,
      data,
      timestamp: DateUtils.now()
    }));
  },
  
  info(message, data = {}) {
    this.log('INFO', message, data);
  },
  
  warn(message, data = {}) {
    this.log('WARN', message, data);
  },
  
  error(message, data = {}) {
    this.log('ERROR', message, data);
  },
  
  // Log to KV
  async persistLog(env, level, message, data = {}) {
    const logId = StringUtils.generateId('LOG', 12);
    
    try {
      await env.LOGS.put(logId, JSON.stringify({
        id: logId,
        level,
        message,
        data,
        timestamp: DateUtils.now()
      }), {
        expirationTtl: 86400 * 30 // 30 days
      });
    } catch (error) {
      console.error('Failed to persist log:', error);
    }
  }
};

// ============================================================================
// EXPORT ALL
// ============================================================================

export default {
  DateUtils,
  StringUtils,
  ValidationUtils,
  ResponseUtils,
  ErrorUtils,
  SecurityUtils,
  PerformanceUtils,
  LogUtils
};
