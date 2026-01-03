/**
 * ═══════════════════════════════════════════════════════════════════
 * NOIZY.AI COMMAND CENTER - ADMIN WORKER
 * ═══════════════════════════════════════════════════════════════════
 * 
 * Claude (or you) can call these endpoints to control Cloudflare.
 * All the power of the API, wrapped in simple URLs.
 * 
 * ENDPOINTS:
 *   /health           - Check if worker is alive
 *   /speed-boost      - Enable ALL speed optimizations
 *   /purge-cache      - Purge entire cache
 *   /dns-list         - List DNS records
 *   /status           - Get current zone settings
 * 
 * SECURITY: Requires X-NOIZY-KEY header or ?key= param
 * 
 * GORUNFREE - Rob Plowman + Claude - December 2025
 * ═══════════════════════════════════════════════════════════════════
 */

const ZONE_ID = "d801959518bee8d71333263a16b32afd";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // Health check - no auth needed
    if (path === '/health' || path === '/') {
      return jsonResponse({
        status: 'NOIZY COMMAND CENTER ONLINE',
        timestamp: new Date().toISOString(),
        endpoints: ['/speed-boost', '/purge-cache', '/dns-list', '/status'],
        empire: 'NOIZY.AI',
        gorunfree: true
      });
    }
    
    // ═══════════════════════════════════════════════════════════════
    // AUTHENTICATION - All other endpoints need the secret key
    // ═══════════════════════════════════════════════════════════════
    const authKey = request.headers.get('X-NOIZY-KEY') || url.searchParams.get('key');
    
    if (authKey !== env.ADMIN_SECRET) {
      return jsonResponse({ error: 'Unauthorized. GORUNFREE requires the key.' }, 403);
    }
    
    // Get API token from secrets
    const API_TOKEN = env.CF_API_TOKEN;
    
    if (!API_TOKEN) {
      return jsonResponse({ error: 'CF_API_TOKEN not configured' }, 500);
    }
    
    // ═══════════════════════════════════════════════════════════════
    // ROUTE HANDLERS
    // ═══════════════════════════════════════════════════════════════
    
    switch (path) {
      case '/speed-boost':
        return await speedBoost(API_TOKEN);
      
      case '/purge-cache':
        return await purgeCache(API_TOKEN);
      
      case '/dns-list':
        return await dnsList(API_TOKEN);
      
      case '/status':
        return await getStatus(API_TOKEN);
        
      case '/dns-add':
        return await dnsAdd(API_TOKEN, url.searchParams);
      
      default:
        return jsonResponse({ error: 'Unknown command', available: ['/speed-boost', '/purge-cache', '/dns-list', '/status'] }, 404);
    }
  }
};

// ═══════════════════════════════════════════════════════════════════
// SPEED BOOST - Enable ALL optimizations
// ═══════════════════════════════════════════════════════════════════
async function speedBoost(API_TOKEN) {
  const results = {};
  const settings = [
    { id: 'minify', value: { css: 'on', html: 'on', js: 'on' }, name: 'Auto Minify' },
    { id: 'rocket_loader', value: 'on', name: 'Rocket Loader' },
    { id: 'early_hints', value: 'on', name: 'Early Hints' },
    { id: 'brotli', value: 'on', name: 'Brotli' },
    { id: 'http2', value: 'on', name: 'HTTP/2' },
    { id: 'http3', value: 'on', name: 'HTTP/3 (QUIC)' },
    { id: '0rtt', value: 'on', name: '0-RTT' },
    { id: 'always_use_https', value: 'on', name: 'Always HTTPS' },
    { id: 'min_tls_version', value: '1.2', name: 'Min TLS 1.2' },
    { id: 'tls_1_3', value: 'on', name: 'TLS 1.3' },
    { id: 'automatic_https_rewrites', value: 'on', name: 'Auto HTTPS Rewrites' },
    { id: 'browser_cache_ttl', value: 14400, name: 'Browser Cache 4hr' },
    { id: 'always_online', value: 'on', name: 'Always Online' },
    { id: 'websockets', value: 'on', name: 'WebSockets' },
    { id: 'ip_geolocation', value: 'on', name: 'IP Geolocation' },
    { id: 'opportunistic_encryption', value: 'on', name: 'Opportunistic Encryption' },
  ];
  
  for (const setting of settings) {
    try {
      const response = await fetch(
        `https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/settings/${setting.id}`,
        {
          method: 'PATCH',
          headers: {
            'Authorization': `Bearer ${API_TOKEN}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ value: setting.value })
        }
      );
      const data = await response.json();
      results[setting.name] = data.success ? '✅' : '❌ ' + (data.errors?.[0]?.message || 'Failed');
    } catch (e) {
      results[setting.name] = '❌ ' + e.message;
    }
  }
  
  // Try tiered cache separately
  try {
    const tcResponse = await fetch(
      `https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/cache/tiered_cache_smart_topology_enable`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ value: 'on' })
      }
    );
    const tcData = await tcResponse.json();
    results['Smart Tiered Cache'] = tcData.success ? '✅' : '⚠️ May need Pro plan';
  } catch (e) {
    results['Smart Tiered Cache'] = '⚠️ ' + e.message;
  }
  
  return jsonResponse({
    action: 'SPEED BOOST',
    zone: 'noizy.ai',
    results,
    message: 'GORUNFREE SPEED BOOST COMPLETE! 🔥'
  });
}

// ═══════════════════════════════════════════════════════════════════
// PURGE CACHE - Clear everything
// ═══════════════════════════════════════════════════════════════════
async function purgeCache(API_TOKEN) {
  try {
    const response = await fetch(
      `https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/purge_cache`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ purge_everything: true })
      }
    );
    const data = await response.json();
    
    return jsonResponse({
      action: 'PURGE CACHE',
      success: data.success,
      message: data.success ? '🧹 Cache purged! Fresh start.' : 'Failed to purge',
      details: data.errors || []
    });
  } catch (e) {
    return jsonResponse({ action: 'PURGE CACHE', error: e.message }, 500);
  }
}

// ═══════════════════════════════════════════════════════════════════
// DNS LIST - Show all DNS records
// ═══════════════════════════════════════════════════════════════════
async function dnsList(API_TOKEN) {
  try {
    const response = await fetch(
      `https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records?per_page=100`,
      {
        headers: {
          'Authorization': `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json'
        }
      }
    );
    const data = await response.json();
    
    if (!data.success) {
      return jsonResponse({ error: 'Failed to fetch DNS', details: data.errors }, 500);
    }
    
    const records = data.result.map(r => ({
      type: r.type,
      name: r.name,
      content: r.content,
      proxied: r.proxied,
      ttl: r.ttl
    }));
    
    return jsonResponse({
      action: 'DNS LIST',
      zone: 'noizy.ai',
      count: records.length,
      records
    });
  } catch (e) {
    return jsonResponse({ action: 'DNS LIST', error: e.message }, 500);
  }
}

// ═══════════════════════════════════════════════════════════════════
// DNS ADD - Add a new DNS record
// Usage: /dns-add?type=CNAME&name=test&content=noizy.ai&proxied=true
// ═══════════════════════════════════════════════════════════════════
async function dnsAdd(API_TOKEN, params) {
  const type = params.get('type') || 'CNAME';
  const name = params.get('name');
  const content = params.get('content') || 'noizy.ai';
  const proxied = params.get('proxied') !== 'false';
  
  if (!name) {
    return jsonResponse({ error: 'Missing ?name= parameter' }, 400);
  }
  
  try {
    const response = await fetch(
      `https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ type, name, content, proxied, ttl: 1 })
      }
    );
    const data = await response.json();
    
    return jsonResponse({
      action: 'DNS ADD',
      success: data.success,
      record: data.success ? { type, name: `${name}.noizy.ai`, content, proxied } : null,
      message: data.success ? `✅ ${name}.noizy.ai created!` : 'Failed',
      errors: data.errors || []
    });
  } catch (e) {
    return jsonResponse({ action: 'DNS ADD', error: e.message }, 500);
  }
}

// ═══════════════════════════════════════════════════════════════════
// STATUS - Get current zone settings
// ═══════════════════════════════════════════════════════════════════
async function getStatus(API_TOKEN) {
  try {
    const response = await fetch(
      `https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/settings`,
      {
        headers: {
          'Authorization': `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json'
        }
      }
    );
    const data = await response.json();
    
    if (!data.success) {
      return jsonResponse({ error: 'Failed to fetch settings', details: data.errors }, 500);
    }
    
    // Extract key settings
    const importantSettings = [
      'minify', 'rocket_loader', 'early_hints', 'brotli', 
      'http2', 'http3', '0rtt', 'always_use_https', 
      'tls_1_3', 'browser_cache_ttl', 'websockets'
    ];
    
    const settings = {};
    for (const s of data.result) {
      if (importantSettings.includes(s.id)) {
        settings[s.id] = s.value;
      }
    }
    
    return jsonResponse({
      action: 'STATUS',
      zone: 'noizy.ai',
      settings,
      message: 'Current NOIZY.AI configuration'
    });
  } catch (e) {
    return jsonResponse({ action: 'STATUS', error: e.message }, 500);
  }
}

// ═══════════════════════════════════════════════════════════════════
// HELPER
// ═══════════════════════════════════════════════════════════════════
function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'X-Powered-By': 'NOIZY.AI COMMAND CENTER',
      'X-GORUNFREE': 'true'
    }
  });
}
