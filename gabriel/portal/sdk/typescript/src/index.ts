/**
 * TypeScript SDK for GABRIEL API
 * 
 * Official client library for integrating with GABRIEL
 * board inspection services.
 * 
 * Usage:
 *   const gabriel = new GabrielClient({ apiKey: 'gab_live_xxx' });
 *   const scan = await gabriel.scan.create(imageBuffer);
 *   const result = await gabriel.scan.get(scan.scanId);
 */

export interface GabrielConfig {
  apiKey: string;
  baseUrl?: string;
  timeout?: number;
}

export interface ScanOptions {
  boardType?: string;
  userId?: string;
  webhookUrl?: string;
  priority?: 'normal' | 'high';
}

export interface ScanResult {
  scanId: string;
  status: 'processing' | 'complete' | 'failed';
  boardType?: string;
  confidence?: number;
  issues?: Issue[];
  metadata?: Record<string, unknown>;
  createdAt: string;
  completedAt?: string;
}

export interface Issue {
  id: string;
  component: string;
  type: 'damaged' | 'missing' | 'misaligned' | 'cold_solder' | 'bridged';
  severity: 'critical' | 'warning' | 'info';
  description: string;
  confidence: number;
  location: {
    x: number;
    y: number;
    width: number;
    height: number;
  };
  repairGuide?: string;
}

export interface GoldenReference {
  id: string;
  boardType: string;
  name: string;
  createdAt: string;
  imageUrl?: string;
}

export interface Webhook {
  id: string;
  url: string;
  events: string[];
  active: boolean;
  createdAt: string;
}

export interface APIKey {
  id: string;
  name: string;
  prefix: string;
  permissions: string[];
  createdAt: string;
  lastUsed?: string;
}

export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  perPage: number;
  hasMore: boolean;
}

// ============================================================================
// ERROR TYPES
// ============================================================================

export class GabrielError extends Error {
  constructor(
    message: string,
    public statusCode: number,
    public code: string,
    public details?: Record<string, unknown>
  ) {
    super(message);
    this.name = 'GabrielError';
  }
}

export class AuthenticationError extends GabrielError {
  constructor(message = 'Invalid or missing API key') {
    super(message, 401, 'authentication_error');
    this.name = 'AuthenticationError';
  }
}

export class RateLimitError extends GabrielError {
  constructor(
    public retryAfter: number,
    message = 'Rate limit exceeded'
  ) {
    super(message, 429, 'rate_limit_error', { retryAfter });
    this.name = 'RateLimitError';
  }
}

// ============================================================================
// MAIN CLIENT
// ============================================================================

export class GabrielClient {
  private apiKey: string;
  private baseUrl: string;
  private timeout: number;

  public scan: ScanAPI;
  public reference: ReferenceAPI;
  public webhook: WebhookAPI;
  public board: BoardAPI;

  constructor(config: GabrielConfig) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl || 'https://api.gabriel.noizylab.com';
    this.timeout = config.timeout || 30000;

    this.scan = new ScanAPI(this);
    this.reference = new ReferenceAPI(this);
    this.webhook = new WebhookAPI(this);
    this.board = new BoardAPI(this);
  }

  async request<T>(
    method: string,
    path: string,
    options: {
      body?: unknown;
      headers?: Record<string, string>;
      timeout?: number;
    } = {}
  ): Promise<T> {
    const controller = new AbortController();
    const timeout = setTimeout(
      () => controller.abort(),
      options.timeout || this.timeout
    );

    try {
      const response = await fetch(`${this.baseUrl}${path}`, {
        method,
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
          ...options.headers,
        },
        body: options.body ? JSON.stringify(options.body) : undefined,
        signal: controller.signal,
      });

      clearTimeout(timeout);

      if (!response.ok) {
        await this.handleError(response);
      }

      return response.json();
    } catch (error) {
      clearTimeout(timeout);
      
      if ((error as Error).name === 'AbortError') {
        throw new GabrielError('Request timeout', 408, 'timeout_error');
      }
      
      throw error;
    }
  }

  async requestFormData<T>(
    method: string,
    path: string,
    formData: FormData
  ): Promise<T> {
    const response = await fetch(`${this.baseUrl}${path}`, {
      method,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
      },
      body: formData,
    });

    if (!response.ok) {
      await this.handleError(response);
    }

    return response.json();
  }

  private async handleError(response: Response): Promise<never> {
    const body = await response.json().catch(() => ({}));

    if (response.status === 401) {
      throw new AuthenticationError(body.message);
    }

    if (response.status === 429) {
      const retryAfter = parseInt(response.headers.get('Retry-After') || '60', 10);
      throw new RateLimitError(retryAfter, body.message);
    }

    throw new GabrielError(
      body.message || 'Unknown error',
      response.status,
      body.code || 'unknown_error',
      body.details
    );
  }
}

// ============================================================================
// SCAN API
// ============================================================================

class ScanAPI {
  constructor(private client: GabrielClient) {}

  /**
   * Create a new scan from an image
   */
  async create(
    image: Buffer | Blob | File,
    options: ScanOptions = {}
  ): Promise<{ scanId: string; status: string }> {
    const formData = new FormData();
    formData.append('image', image);
    
    if (options.boardType) formData.append('boardType', options.boardType);
    if (options.userId) formData.append('userId', options.userId);
    if (options.webhookUrl) formData.append('webhookUrl', options.webhookUrl);
    if (options.priority) formData.append('priority', options.priority);

    return this.client.requestFormData('POST', '/api/scan', formData);
  }

  /**
   * Get scan result by ID
   */
  async get(scanId: string): Promise<ScanResult> {
    return this.client.request('GET', `/api/scan/${scanId}`);
  }

  /**
   * Wait for scan to complete (polls until done)
   */
  async waitForCompletion(
    scanId: string,
    options: { maxWait?: number; pollInterval?: number } = {}
  ): Promise<ScanResult> {
    const maxWait = options.maxWait || 60000;
    const pollInterval = options.pollInterval || 2000;
    const startTime = Date.now();

    while (Date.now() - startTime < maxWait) {
      const result = await this.get(scanId);
      
      if (result.status === 'complete' || result.status === 'failed') {
        return result;
      }

      await new Promise(r => setTimeout(r, pollInterval));
    }

    throw new GabrielError(
      'Scan timed out',
      408,
      'scan_timeout',
      { scanId, maxWait }
    );
  }

  /**
   * List recent scans
   */
  async list(options: {
    page?: number;
    perPage?: number;
    status?: string;
  } = {}): Promise<PaginatedResponse<ScanResult>> {
    const params = new URLSearchParams();
    if (options.page) params.set('page', options.page.toString());
    if (options.perPage) params.set('perPage', options.perPage.toString());
    if (options.status) params.set('status', options.status);

    return this.client.request('GET', `/api/scans?${params}`);
  }

  /**
   * Delete a scan
   */
  async delete(scanId: string): Promise<{ success: boolean }> {
    return this.client.request('DELETE', `/api/scan/${scanId}`);
  }
}

// ============================================================================
// REFERENCE API
// ============================================================================

class ReferenceAPI {
  constructor(private client: GabrielClient) {}

  /**
   * Upload a golden reference image
   */
  async upload(
    image: Buffer | Blob | File,
    options: { boardType: string; name: string }
  ): Promise<GoldenReference> {
    const formData = new FormData();
    formData.append('image', image);
    formData.append('boardType', options.boardType);
    formData.append('name', options.name);

    return this.client.requestFormData('POST', '/api/reference', formData);
  }

  /**
   * List all golden references
   */
  async list(): Promise<GoldenReference[]> {
    const response = await this.client.request<{ references: GoldenReference[] }>(
      'GET',
      '/api/references'
    );
    return response.references;
  }

  /**
   * Get a specific reference
   */
  async get(referenceId: string): Promise<GoldenReference> {
    return this.client.request('GET', `/api/reference/${referenceId}`);
  }

  /**
   * Delete a reference
   */
  async delete(referenceId: string): Promise<{ success: boolean }> {
    return this.client.request('DELETE', `/api/reference/${referenceId}`);
  }
}

// ============================================================================
// WEBHOOK API
// ============================================================================

class WebhookAPI {
  constructor(private client: GabrielClient) {}

  /**
   * Create a webhook
   */
  async create(options: {
    url: string;
    events: string[];
  }): Promise<{ webhook: Webhook; secret: string }> {
    return this.client.request('POST', '/api/webhooks', { body: options });
  }

  /**
   * List all webhooks
   */
  async list(): Promise<Webhook[]> {
    const response = await this.client.request<{ webhooks: Webhook[] }>(
      'GET',
      '/api/webhooks'
    );
    return response.webhooks;
  }

  /**
   * Update a webhook
   */
  async update(
    webhookId: string,
    options: Partial<{ url: string; events: string[]; active: boolean }>
  ): Promise<Webhook> {
    return this.client.request('PATCH', `/api/webhooks/${webhookId}`, {
      body: options,
    });
  }

  /**
   * Delete a webhook
   */
  async delete(webhookId: string): Promise<{ success: boolean }> {
    return this.client.request('DELETE', `/api/webhooks/${webhookId}`);
  }

  /**
   * Send test webhook
   */
  async test(webhookId: string): Promise<{ success: boolean }> {
    return this.client.request('POST', `/api/webhooks/${webhookId}/test`);
  }

  /**
   * Verify webhook signature
   */
  static async verify(
    payload: string,
    signature: string,
    secret: string
  ): Promise<boolean> {
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
      'raw',
      encoder.encode(secret),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['verify']
    );

    const sigBytes = Uint8Array.from(atob(signature), c => c.charCodeAt(0));
    
    return crypto.subtle.verify(
      'HMAC',
      key,
      sigBytes,
      encoder.encode(payload)
    );
  }
}

// ============================================================================
// BOARD API
// ============================================================================

class BoardAPI {
  constructor(private client: GabrielClient) {}

  /**
   * Search boards
   */
  async search(query: string): Promise<any[]> {
    return this.client.request('GET', `/api/boards/search?q=${encodeURIComponent(query)}`);
  }

  /**
   * Get board details
   */
  async get(boardId: string): Promise<any> {
    return this.client.request('GET', `/api/boards/${boardId}`);
  }

  /**
   * List all supported boards
   */
  async list(): Promise<any[]> {
    const response = await this.client.request<{ boards: any[] }>('GET', '/api/boards');
    return response.boards;
  }

  /**
   * Get common issues for a board
   */
  async getIssues(boardId: string): Promise<any[]> {
    return this.client.request('GET', `/api/boards/${boardId}/issues`);
  }
}

// ============================================================================
// EXPORTS
// ============================================================================

export default GabrielClient;

// Export for CommonJS compatibility
module.exports = GabrielClient;
module.exports.GabrielClient = GabrielClient;
module.exports.GabrielError = GabrielError;
module.exports.AuthenticationError = AuthenticationError;
module.exports.RateLimitError = RateLimitError;
