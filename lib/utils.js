// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB UTILITIES v2.0
// Common Utilities and Helper Functions
// ═══════════════════════════════════════════════════════════════════════════════

// ─── STRING UTILITIES ────────────────────────────────────────────────────────

export function truncate(str, length = 100, suffix = "...") {
  if (!str) return "";
  if (str.length <= length) return str;
  return str.substring(0, length - suffix.length) + suffix;
}

export function slugify(str) {
  return str
    .toLowerCase()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

export function capitalize(str) {
  if (!str) return "";
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

export function sanitizeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// ─── DATE UTILITIES ──────────────────────────────────────────────────────────

export function formatDate(date, format = "iso") {
  const d = date instanceof Date ? date : new Date(date);

  switch (format) {
    case "iso":
      return d.toISOString();
    case "short":
      return d.toLocaleDateString("en-US", { month: "short", day: "numeric" });
    case "long":
      return d.toLocaleDateString("en-US", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
      });
    case "time":
      return d.toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" });
    case "relative":
      return getRelativeTime(d);
    default:
      return d.toISOString();
  }
}

export function getRelativeTime(date) {
  const now = new Date();
  const diff = now - new Date(date);
  const seconds = Math.floor(diff / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);

  if (seconds < 60) return "just now";
  if (minutes < 60) return `${minutes}m ago`;
  if (hours < 24) return `${hours}h ago`;
  if (days < 7) return `${days}d ago`;
  return formatDate(date, "short");
}

export function isToday(date) {
  const today = new Date();
  const d = new Date(date);
  return d.toDateString() === today.toDateString();
}

export function isWithinHours(date, hours) {
  const now = Date.now();
  const timestamp = new Date(date).getTime();
  return now - timestamp < hours * 60 * 60 * 1000;
}

// ─── ID GENERATION ───────────────────────────────────────────────────────────

export function generateId(prefix = "") {
  const timestamp = Date.now();
  const random = Math.random().toString(36).substring(2, 11);
  return prefix ? `${prefix}-${timestamp}-${random}` : `${timestamp}-${random}`;
}

export function generateShortId(length = 8) {
  const chars = "abcdefghijklmnopqrstuvwxyz0123456789";
  let result = "";
  for (let i = 0; i < length; i++) {
    result += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return result;
}

// ─── VALIDATION ──────────────────────────────────────────────────────────────

export function isValidEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

export function isValidUrl(url) {
  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
}

export function isValidJson(str) {
  try {
    JSON.parse(str);
    return true;
  } catch {
    return false;
  }
}

// ─── ARRAY UTILITIES ─────────────────────────────────────────────────────────

export function chunk(array, size) {
  const chunks = [];
  for (let i = 0; i < array.length; i += size) {
    chunks.push(array.slice(i, i + size));
  }
  return chunks;
}

export function unique(array) {
  return [...new Set(array)];
}

export function groupBy(array, key) {
  return array.reduce((groups, item) => {
    const value = typeof key === "function" ? key(item) : item[key];
    (groups[value] = groups[value] || []).push(item);
    return groups;
  }, {});
}

export function sortBy(array, key, order = "asc") {
  return [...array].sort((a, b) => {
    const valueA = typeof key === "function" ? key(a) : a[key];
    const valueB = typeof key === "function" ? key(b) : b[key];

    if (valueA < valueB) return order === "asc" ? -1 : 1;
    if (valueA > valueB) return order === "asc" ? 1 : -1;
    return 0;
  });
}

// ─── OBJECT UTILITIES ────────────────────────────────────────────────────────

export function pick(obj, keys) {
  return keys.reduce((result, key) => {
    if (key in obj) result[key] = obj[key];
    return result;
  }, {});
}

export function omit(obj, keys) {
  const result = { ...obj };
  keys.forEach(key => delete result[key]);
  return result;
}

export function deepMerge(target, source) {
  const result = { ...target };
  for (const key of Object.keys(source)) {
    if (source[key] instanceof Object && key in target) {
      result[key] = deepMerge(target[key], source[key]);
    } else {
      result[key] = source[key];
    }
  }
  return result;
}

// ─── RETRY LOGIC ─────────────────────────────────────────────────────────────

export async function retry(fn, options = {}) {
  const { retries = 3, delay = 1000, backoff = 2 } = options;

  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (attempt === retries) throw error;
      await sleep(delay * Math.pow(backoff, attempt));
    }
  }
}

export function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// ─── RATE LIMITING ───────────────────────────────────────────────────────────

export function createRateLimiter(maxRequests, windowMs) {
  const requests = new Map();

  return function isAllowed(key) {
    const now = Date.now();
    const windowStart = now - windowMs;

    // Clean old entries
    const timestamps = (requests.get(key) || []).filter(t => t > windowStart);

    if (timestamps.length >= maxRequests) {
      return false;
    }

    timestamps.push(now);
    requests.set(key, timestamps);
    return true;
  };
}

// ─── LOGGING ─────────────────────────────────────────────────────────────────

export const LogLevel = {
  DEBUG: 0,
  INFO: 1,
  WARN: 2,
  ERROR: 3
};

export function createLogger(name, minLevel = LogLevel.INFO) {
  const levelNames = ["DEBUG", "INFO", "WARN", "ERROR"];

  return {
    debug: (...args) => minLevel <= LogLevel.DEBUG && console.log(`[${name}] [DEBUG]`, ...args),
    info: (...args) => minLevel <= LogLevel.INFO && console.log(`[${name}] [INFO]`, ...args),
    warn: (...args) => minLevel <= LogLevel.WARN && console.warn(`[${name}] [WARN]`, ...args),
    error: (...args) => minLevel <= LogLevel.ERROR && console.error(`[${name}] [ERROR]`, ...args)
  };
}

// ─── EXPORT ALL ──────────────────────────────────────────────────────────────

export default {
  // String
  truncate,
  slugify,
  capitalize,
  sanitizeHtml,
  // Date
  formatDate,
  getRelativeTime,
  isToday,
  isWithinHours,
  // ID
  generateId,
  generateShortId,
  // Validation
  isValidEmail,
  isValidUrl,
  isValidJson,
  // Array
  chunk,
  unique,
  groupBy,
  sortBy,
  // Object
  pick,
  omit,
  deepMerge,
  // Async
  retry,
  sleep,
  createRateLimiter,
  // Logging
  LogLevel,
  createLogger
};
