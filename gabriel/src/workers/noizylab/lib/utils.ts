// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Utility Functions
// ═══════════════════════════════════════════════════════════════════════════

// ═══════════════════════════════════════════════════════════════════════════
// UUID Generation
// ═══════════════════════════════════════════════════════════════════════════

export function generateUUID(): string {
  return crypto.randomUUID();
}

// ═══════════════════════════════════════════════════════════════════════════
// Ticket ID Generation (NL-0042 format)
// ═══════════════════════════════════════════════════════════════════════════

export async function generateTicketId(db: D1Database): Promise<string> {
  // Get the highest ticket number
  const result = await db.prepare(`
    SELECT id FROM tickets 
    WHERE id LIKE 'NL-%'
    ORDER BY CAST(SUBSTR(id, 4) AS INTEGER) DESC 
    LIMIT 1
  `).first();
  
  let nextNumber = 1;
  
  if (result?.id) {
    const currentNumber = parseInt((result.id as string).replace('NL-', ''), 10);
    nextNumber = currentNumber + 1;
  }
  
  // Format as NL-0042
  return `NL-${String(nextNumber).padStart(4, '0')}`;
}

// ═══════════════════════════════════════════════════════════════════════════
// Join Code Generation (6-char for Live Help)
// ═══════════════════════════════════════════════════════════════════════════

export function generateJoinCode(): string {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // No I, O, 0, 1 for clarity
  let code = '';
  for (let i = 0; i < 6; i++) {
    code += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return code;
}

// ═══════════════════════════════════════════════════════════════════════════
// R2 Key Generation
// ═══════════════════════════════════════════════════════════════════════════

export function generateR2Key(ticketId: string, filename: string): string {
  const timestamp = Date.now();
  const ext = filename.split('.').pop() || 'bin';
  const safeFilename = filename
    .replace(/[^a-zA-Z0-9.-]/g, '_')
    .substring(0, 50);
  
  return `tickets/${ticketId}/${timestamp}-${safeFilename}`;
}

// ═══════════════════════════════════════════════════════════════════════════
// Subject DNA Parser
// ═══════════════════════════════════════════════════════════════════════════

interface SubjectDNA {
  ticketId: string | null;
  lastname: string | null;
  device: string | null;
  issue: string | null;
}

export function parseSubjectDNA(subject: string): SubjectDNA {
  // Format: NL-0042 | Smith | MacBook Pro | Chrome extremely slow
  const regex = /^NL-(\d{4}) \| ([^|]+) \| ([^|]+) \| (.+)$/;
  const match = subject.match(regex);
  
  if (match) {
    return {
      ticketId: `NL-${match[1]}`,
      lastname: match[2].trim(),
      device: match[3].trim(),
      issue: match[4].trim(),
    };
  }
  
  // Try partial match for just ticket ID
  const ticketMatch = subject.match(/NL-(\d{4})/);
  if (ticketMatch) {
    return {
      ticketId: `NL-${ticketMatch[1]}`,
      lastname: null,
      device: null,
      issue: null,
    };
  }
  
  return {
    ticketId: null,
    lastname: null,
    device: null,
    issue: null,
  };
}

export function buildSubjectDNA(
  ticketId: string,
  lastname: string,
  device: string,
  issue: string
): string {
  return `${ticketId} | ${lastname} | ${device} | ${issue}`;
}

// ═══════════════════════════════════════════════════════════════════════════
// Date/Time Helpers
// ═══════════════════════════════════════════════════════════════════════════

export function formatNextUpdateTime(hoursFromNow: number): string {
  const date = new Date(Date.now() + hoursFromNow * 60 * 60 * 1000);
  
  // Format: "Today 3:00 PM" or "Tomorrow 10:00 AM"
  const now = new Date();
  const isToday = date.toDateString() === now.toDateString();
  const isTomorrow = date.toDateString() === new Date(now.getTime() + 86400000).toDateString();
  
  const timeStr = date.toLocaleTimeString('en-US', {
    hour: 'numeric',
    minute: '2-digit',
    hour12: true,
  });
  
  if (isToday) {
    return `Today ${timeStr}`;
  } else if (isTomorrow) {
    return `Tomorrow ${timeStr}`;
  } else {
    const dateStr = date.toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: 'numeric',
    });
    return `${dateStr} ${timeStr}`;
  }
}

export function calculateDuration(startTime: string, endTime?: string): number {
  const start = new Date(startTime).getTime();
  const end = endTime ? new Date(endTime).getTime() : Date.now();
  return Math.round((end - start) / 1000);
}

// ═══════════════════════════════════════════════════════════════════════════
// Sanitization
// ═══════════════════════════════════════════════════════════════════════════

export function sanitizeInput(input: string): string {
  return input
    .trim()
    .replace(/<[^>]*>/g, '') // Remove HTML tags
    .substring(0, 10000); // Limit length
}

export function sanitizeFilename(filename: string): string {
  return filename
    .replace(/[^a-zA-Z0-9._-]/g, '_')
    .substring(0, 100);
}

// ═══════════════════════════════════════════════════════════════════════════
// Rate Limiting Key Builder
// ═══════════════════════════════════════════════════════════════════════════

export function buildRateLimitKey(
  type: string,
  identifier: string
): string {
  return `ratelimit:${type}:${identifier}`;
}

// ═══════════════════════════════════════════════════════════════════════════
// Template Variable Replacement
// ═══════════════════════════════════════════════════════════════════════════

export function replaceTemplateVars(
  template: string,
  vars: Record<string, string>
): string {
  let result = template;
  for (const [key, value] of Object.entries(vars)) {
    result = result.replace(new RegExp(`\\{${key}\\}`, 'g'), value);
  }
  return result;
}

// ═══════════════════════════════════════════════════════════════════════════
// Confidence Score Calculation
// ═══════════════════════════════════════════════════════════════════════════

export function calculateConfidence(
  matchCount: number,
  indicatorCount: number
): 'green' | 'yellow' | 'red' {
  if (indicatorCount === 0) return 'red';
  
  const ratio = matchCount / indicatorCount;
  
  if (ratio >= 0.6) return 'green';
  if (ratio >= 0.3) return 'yellow';
  return 'red';
}

// ═══════════════════════════════════════════════════════════════════════════
// Error Response Builder
// ═══════════════════════════════════════════════════════════════════════════

export function errorResponse(
  message: string,
  code: string,
  details?: any
): { error: string; code: string; details?: any; timestamp: string } {
  return {
    error: message,
    code,
    details,
    timestamp: new Date().toISOString(),
  };
}

// ═══════════════════════════════════════════════════════════════════════════
// Success Response Builder
// ═══════════════════════════════════════════════════════════════════════════

export function successResponse<T>(
  data: T,
  message?: string
): { success: true; data: T; message?: string; timestamp: string } {
  return {
    success: true,
    data,
    message,
    timestamp: new Date().toISOString(),
  };
}
