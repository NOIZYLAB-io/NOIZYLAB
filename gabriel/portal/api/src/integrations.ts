/**
 * Integration Marketplace Backend
 * 
 * Manages third-party integrations for GABRIEL including:
 * - Repair shop management systems
 * - Parts suppliers
 * - Inventory systems
 * - CRM platforms
 */

export interface Integration {
  id: string;
  name: string;
  slug: string;
  category: IntegrationCategory;
  description: string;
  icon: string;
  status: 'stable' | 'beta' | 'coming_soon';
  permissions: string[];
  pricing: 'free' | 'pro' | 'enterprise';
  setupUrl?: string;
  docsUrl?: string;
}

export type IntegrationCategory = 
  | 'inventory'
  | 'crm'
  | 'accounting'
  | 'parts'
  | 'communication'
  | 'analytics'
  | 'storage'
  | 'automation';

export interface IntegrationConfig {
  integrationId: string;
  userId: string;
  credentials: Record<string, string>;
  settings: Record<string, unknown>;
  enabled: boolean;
  lastSyncAt?: string;
  createdAt: string;
}

// Available integrations catalog
export const INTEGRATIONS_CATALOG: Integration[] = [
  // Inventory & Parts
  {
    id: 'int_injured_gadgets',
    name: 'Injured Gadgets',
    slug: 'injured-gadgets',
    category: 'parts',
    description: 'Auto-order replacement parts based on scan results',
    icon: '🔧',
    status: 'stable',
    permissions: ['scan:read', 'parts:order'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/injured-gadgets',
  },
  {
    id: 'int_ifixit',
    name: 'iFixit Parts',
    slug: 'ifixit',
    category: 'parts',
    description: 'Search iFixit catalog for compatible replacement parts',
    icon: '🛠️',
    status: 'stable',
    permissions: ['scan:read'],
    pricing: 'free',
    docsUrl: '/docs/integrations/ifixit',
  },
  {
    id: 'int_replacebase',
    name: 'Replacebase',
    slug: 'replacebase',
    category: 'parts',
    description: 'UK/EU parts supplier integration',
    icon: '📦',
    status: 'stable',
    permissions: ['scan:read', 'parts:order'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/replacebase',
  },
  {
    id: 'int_mobilesentrix',
    name: 'MobileSentrix',
    slug: 'mobilesentrix',
    category: 'parts',
    description: 'Wholesale parts ordering',
    icon: '📱',
    status: 'beta',
    permissions: ['scan:read', 'parts:order'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/mobilesentrix',
  },
  
  // Inventory Systems
  {
    id: 'int_repairshopr',
    name: 'RepairShopr',
    slug: 'repairshopr',
    category: 'inventory',
    description: 'Sync repairs, parts inventory, and customer data',
    icon: '🏪',
    status: 'stable',
    permissions: ['scan:read', 'scan:write', 'customer:sync'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/repairshopr',
  },
  {
    id: 'int_repairdesk',
    name: 'RepairDesk',
    slug: 'repairdesk',
    category: 'inventory',
    description: 'Complete POS and inventory sync',
    icon: '🖥️',
    status: 'stable',
    permissions: ['scan:read', 'scan:write', 'inventory:sync'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/repairdesk',
  },
  {
    id: 'int_cellstore',
    name: 'CellStore Software',
    slug: 'cellstore',
    category: 'inventory',
    description: 'Cell phone repair shop management',
    icon: '📊',
    status: 'beta',
    permissions: ['scan:read', 'scan:write'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/cellstore',
  },
  
  // Communication
  {
    id: 'int_slack',
    name: 'Slack',
    slug: 'slack',
    category: 'communication',
    description: 'Get scan notifications in Slack channels',
    icon: '💬',
    status: 'stable',
    permissions: ['scan:read', 'notification:send'],
    pricing: 'free',
    docsUrl: '/docs/integrations/slack',
  },
  {
    id: 'int_discord',
    name: 'Discord',
    slug: 'discord',
    category: 'communication',
    description: 'Send scan results to Discord servers',
    icon: '🎮',
    status: 'stable',
    permissions: ['scan:read', 'notification:send'],
    pricing: 'free',
    docsUrl: '/docs/integrations/discord',
  },
  {
    id: 'int_twilio',
    name: 'Twilio SMS',
    slug: 'twilio',
    category: 'communication',
    description: 'Send SMS updates to customers',
    icon: '📲',
    status: 'stable',
    permissions: ['scan:read', 'customer:read', 'sms:send'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/twilio',
  },
  
  // Cloud Storage
  {
    id: 'int_google_drive',
    name: 'Google Drive',
    slug: 'google-drive',
    category: 'storage',
    description: 'Automatically backup scan reports to Drive',
    icon: '📁',
    status: 'stable',
    permissions: ['scan:read', 'report:export'],
    pricing: 'free',
    docsUrl: '/docs/integrations/google-drive',
  },
  {
    id: 'int_dropbox',
    name: 'Dropbox',
    slug: 'dropbox',
    category: 'storage',
    description: 'Sync reports and images to Dropbox',
    icon: '💧',
    status: 'stable',
    permissions: ['scan:read', 'report:export'],
    pricing: 'free',
    docsUrl: '/docs/integrations/dropbox',
  },
  
  // CRM
  {
    id: 'int_hubspot',
    name: 'HubSpot',
    slug: 'hubspot',
    category: 'crm',
    description: 'Sync customer data and repair history',
    icon: '🎯',
    status: 'beta',
    permissions: ['customer:sync', 'scan:read'],
    pricing: 'enterprise',
    docsUrl: '/docs/integrations/hubspot',
  },
  {
    id: 'int_salesforce',
    name: 'Salesforce',
    slug: 'salesforce',
    category: 'crm',
    description: 'Enterprise CRM integration',
    icon: '☁️',
    status: 'coming_soon',
    permissions: ['customer:sync', 'scan:read'],
    pricing: 'enterprise',
    docsUrl: '/docs/integrations/salesforce',
  },
  
  // Accounting
  {
    id: 'int_quickbooks',
    name: 'QuickBooks',
    slug: 'quickbooks',
    category: 'accounting',
    description: 'Auto-create invoices from repairs',
    icon: '💰',
    status: 'stable',
    permissions: ['scan:read', 'invoice:create'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/quickbooks',
  },
  {
    id: 'int_xero',
    name: 'Xero',
    slug: 'xero',
    category: 'accounting',
    description: 'Accounting and invoicing sync',
    icon: '📈',
    status: 'beta',
    permissions: ['scan:read', 'invoice:create'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/xero',
  },
  
  // Automation
  {
    id: 'int_zapier',
    name: 'Zapier',
    slug: 'zapier',
    category: 'automation',
    description: 'Connect GABRIEL to 5000+ apps',
    icon: '⚡',
    status: 'stable',
    permissions: ['scan:read', 'webhook:send'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/zapier',
  },
  {
    id: 'int_make',
    name: 'Make (Integromat)',
    slug: 'make',
    category: 'automation',
    description: 'Visual automation workflows',
    icon: '🔄',
    status: 'stable',
    permissions: ['scan:read', 'webhook:send'],
    pricing: 'pro',
    docsUrl: '/docs/integrations/make',
  },
  {
    id: 'int_n8n',
    name: 'n8n',
    slug: 'n8n',
    category: 'automation',
    description: 'Self-hosted workflow automation',
    icon: '🔗',
    status: 'stable',
    permissions: ['scan:read', 'webhook:send'],
    pricing: 'free',
    docsUrl: '/docs/integrations/n8n',
  },
];

// Integration handlers
export interface Env {
  INTEGRATIONS_KV: KVNamespace;
}

interface OAuthConfig {
  clientId: string;
  clientSecret: string;
  authUrl: string;
  tokenUrl: string;
  scopes: string[];
}

const OAUTH_CONFIGS: Record<string, OAuthConfig> = {
  'slack': {
    clientId: 'SLACK_CLIENT_ID',
    clientSecret: 'SLACK_CLIENT_SECRET',
    authUrl: 'https://slack.com/oauth/v2/authorize',
    tokenUrl: 'https://slack.com/api/oauth.v2.access',
    scopes: ['chat:write', 'channels:read'],
  },
  'google-drive': {
    clientId: 'GOOGLE_CLIENT_ID',
    clientSecret: 'GOOGLE_CLIENT_SECRET',
    authUrl: 'https://accounts.google.com/o/oauth2/v2/auth',
    tokenUrl: 'https://oauth2.googleapis.com/token',
    scopes: ['https://www.googleapis.com/auth/drive.file'],
  },
  'dropbox': {
    clientId: 'DROPBOX_CLIENT_ID',
    clientSecret: 'DROPBOX_CLIENT_SECRET',
    authUrl: 'https://www.dropbox.com/oauth2/authorize',
    tokenUrl: 'https://api.dropboxapi.com/oauth2/token',
    scopes: ['files.content.write', 'files.metadata.write'],
  },
  'hubspot': {
    clientId: 'HUBSPOT_CLIENT_ID',
    clientSecret: 'HUBSPOT_CLIENT_SECRET',
    authUrl: 'https://app.hubspot.com/oauth/authorize',
    tokenUrl: 'https://api.hubapi.com/oauth/v1/token',
    scopes: ['contacts', 'crm.objects.contacts.write'],
  },
  'quickbooks': {
    clientId: 'QUICKBOOKS_CLIENT_ID',
    clientSecret: 'QUICKBOOKS_CLIENT_SECRET',
    authUrl: 'https://appcenter.intuit.com/connect/oauth2',
    tokenUrl: 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer',
    scopes: ['com.intuit.quickbooks.accounting'],
  },
};

// Integration API handlers
export async function handleIntegrationRequest(
  request: Request,
  env: Env
): Promise<Response> {
  const url = new URL(request.url);
  const path = url.pathname.replace('/api/integrations', '');
  
  // List all integrations
  if (request.method === 'GET' && path === '') {
    return listIntegrations();
  }
  
  // Get specific integration
  if (request.method === 'GET' && path.match(/^\/[a-z-]+$/)) {
    const slug = path.slice(1);
    return getIntegration(slug);
  }
  
  // Connect integration (OAuth start)
  if (request.method === 'POST' && path.match(/^\/[a-z-]+\/connect$/)) {
    const slug = path.split('/')[1];
    return startOAuthFlow(slug, env);
  }
  
  // OAuth callback
  if (request.method === 'GET' && path.match(/^\/[a-z-]+\/callback$/)) {
    const slug = path.split('/')[1];
    return handleOAuthCallback(request, slug, env);
  }
  
  // Disconnect integration
  if (request.method === 'DELETE' && path.match(/^\/[a-z-]+$/)) {
    const slug = path.slice(1);
    const userId = request.headers.get('X-User-Id') || '';
    return disconnectIntegration(slug, userId, env);
  }
  
  // Get user's connected integrations
  if (request.method === 'GET' && path === '/connected') {
    const userId = request.headers.get('X-User-Id') || '';
    return getConnectedIntegrations(userId, env);
  }
  
  return new Response(JSON.stringify({ error: 'Not found' }), {
    status: 404,
    headers: { 'Content-Type': 'application/json' },
  });
}

function listIntegrations(): Response {
  const byCategory = INTEGRATIONS_CATALOG.reduce((acc, int) => {
    if (!acc[int.category]) acc[int.category] = [];
    acc[int.category].push(int);
    return acc;
  }, {} as Record<IntegrationCategory, Integration[]>);
  
  return new Response(JSON.stringify({
    integrations: INTEGRATIONS_CATALOG,
    byCategory,
    total: INTEGRATIONS_CATALOG.length,
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
}

function getIntegration(slug: string): Response {
  const integration = INTEGRATIONS_CATALOG.find(i => i.slug === slug);
  
  if (!integration) {
    return new Response(JSON.stringify({ error: 'Integration not found' }), {
      status: 404,
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  return new Response(JSON.stringify(integration), {
    headers: { 'Content-Type': 'application/json' },
  });
}

function startOAuthFlow(slug: string, env: Env): Response {
  const config = OAUTH_CONFIGS[slug];
  
  if (!config) {
    return new Response(JSON.stringify({ 
      error: 'OAuth not available for this integration' 
    }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  const state = crypto.randomUUID();
  const redirectUri = `https://gabriel.noizylab.com/api/integrations/${slug}/callback`;
  
  const authUrl = new URL(config.authUrl);
  authUrl.searchParams.set('client_id', config.clientId);
  authUrl.searchParams.set('redirect_uri', redirectUri);
  authUrl.searchParams.set('response_type', 'code');
  authUrl.searchParams.set('scope', config.scopes.join(' '));
  authUrl.searchParams.set('state', state);
  
  return new Response(JSON.stringify({
    authUrl: authUrl.toString(),
    state,
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function handleOAuthCallback(
  request: Request,
  slug: string,
  env: Env
): Promise<Response> {
  const url = new URL(request.url);
  const code = url.searchParams.get('code');
  const state = url.searchParams.get('state');
  
  if (!code || !state) {
    return Response.redirect('/integrations?error=missing_params');
  }
  
  const config = OAUTH_CONFIGS[slug];
  if (!config) {
    return Response.redirect('/integrations?error=invalid_integration');
  }
  
  try {
    // Exchange code for tokens
    const tokenResponse = await fetch(config.tokenUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        grant_type: 'authorization_code',
        code,
        client_id: config.clientId,
        client_secret: config.clientSecret,
        redirect_uri: `https://gabriel.noizylab.com/api/integrations/${slug}/callback`,
      }),
    });
    
    const tokens = await tokenResponse.json() as Record<string, unknown>;
    
    // Store tokens (encrypted)
    // In production, encrypt these tokens before storing
    await env.INTEGRATIONS_KV.put(
      `integration:${state}:${slug}`,
      JSON.stringify({
        accessToken: tokens.access_token,
        refreshToken: tokens.refresh_token,
        expiresAt: Date.now() + (tokens.expires_in as number) * 1000,
        connectedAt: new Date().toISOString(),
      }),
      { expirationTtl: 60 * 60 * 24 * 365 } // 1 year
    );
    
    return Response.redirect(`/integrations/${slug}?success=true`);
  } catch (error) {
    console.error('OAuth error:', error);
    return Response.redirect('/integrations?error=oauth_failed');
  }
}

async function disconnectIntegration(
  slug: string,
  userId: string,
  env: Env
): Promise<Response> {
  await env.INTEGRATIONS_KV.delete(`integration:${userId}:${slug}`);
  
  return new Response(JSON.stringify({ success: true }), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function getConnectedIntegrations(
  userId: string,
  env: Env
): Promise<Response> {
  const connected: IntegrationConfig[] = [];
  
  for (const integration of INTEGRATIONS_CATALOG) {
    const data = await env.INTEGRATIONS_KV.get(
      `integration:${userId}:${integration.slug}`,
      'json'
    );
    
    if (data) {
      connected.push({
        integrationId: integration.id,
        userId,
        credentials: {}, // Don't expose credentials
        settings: {},
        enabled: true,
        lastSyncAt: (data as Record<string, unknown>).connectedAt as string,
        createdAt: (data as Record<string, unknown>).connectedAt as string,
      });
    }
  }
  
  return new Response(JSON.stringify({ connected }), {
    headers: { 'Content-Type': 'application/json' },
  });
}

// Integration event handlers
export async function triggerIntegrationEvent(
  event: string,
  data: Record<string, unknown>,
  userId: string,
  env: Env
): Promise<void> {
  // Get user's connected integrations
  const connected = await getConnectedIntegrations(userId, env);
  const integrations = await connected.json() as { connected: IntegrationConfig[] };
  
  for (const config of integrations.connected) {
    try {
      await dispatchToIntegration(config.integrationId, event, data, env);
    } catch (error) {
      console.error(`Failed to dispatch to ${config.integrationId}:`, error);
    }
  }
}

async function dispatchToIntegration(
  integrationId: string,
  event: string,
  data: Record<string, unknown>,
  env: Env
): Promise<void> {
  const integration = INTEGRATIONS_CATALOG.find(i => i.id === integrationId);
  if (!integration) return;
  
  switch (integration.slug) {
    case 'slack':
      await sendSlackNotification(data, env);
      break;
    case 'discord':
      await sendDiscordNotification(data, env);
      break;
    case 'google-drive':
      await uploadToGoogleDrive(data, env);
      break;
    // Add more handlers as needed
  }
}

async function sendSlackNotification(
  data: Record<string, unknown>,
  env: Env
): Promise<void> {
  // Slack webhook implementation
}

async function sendDiscordNotification(
  data: Record<string, unknown>,
  env: Env
): Promise<void> {
  // Discord webhook implementation
}

async function uploadToGoogleDrive(
  data: Record<string, unknown>,
  env: Env
): Promise<void> {
  // Google Drive upload implementation
}
