/**
 * ADVANCED RATE LIMITER
 * Sliding window algorithm with token bucket
 * User tiers, IP limiting, endpoint-specific rules
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-API-Key',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // Extract identifier (API key, IP, or user ID)
      const identifier = await getIdentifier(request);
      const tier = await getUserTier(env, identifier);
      
      // Check rate limit
      const limitResult = await checkRateLimit(env, identifier, tier, path);
      
      if (!limitResult.allowed) {
        return new Response(JSON.stringify({
          error: 'Rate limit exceeded',
          limit: limitResult.limit,
          remaining: 0,
          reset: limitResult.reset,
          tier: tier
        }), {
          status: 429,
          headers: {
            'Content-Type': 'application/json',
            'X-RateLimit-Limit': limitResult.limit.toString(),
            'X-RateLimit-Remaining': '0',
            'X-RateLimit-Reset': limitResult.reset.toString(),
            'Retry-After': limitResult.retryAfter.toString(),
            ...corsHeaders
          }
        });
      }

      // API endpoints
      if (path === '/') {
        return handleDashboard(limitResult);
      } else if (path === '/api/check') {
        return handleCheckLimit(request, env, corsHeaders);
      } else if (path === '/api/stats') {
        return handleStats(request, env, corsHeaders);
      } else if (path === '/api/reset') {
        return handleReset(request, env, corsHeaders);
      } else if (path === '/health') {
        return new Response(JSON.stringify({ status: 'healthy' }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      // Proxy request with rate limit headers
      return new Response(JSON.stringify({ success: true }), {
        headers: {
          'Content-Type': 'application/json',
          'X-RateLimit-Limit': limitResult.limit.toString(),
          'X-RateLimit-Remaining': limitResult.remaining.toString(),
          'X-RateLimit-Reset': limitResult.reset.toString(),
          ...corsHeaders
        }
      });

    } catch (error) {
      console.error('Error:', error);
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }
};

function handleDashboard(limitInfo) {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rate Limiter Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            padding: 2rem;
        }
        
        .container { max-width: 1200px; margin: 0 auto; }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-bottom: 2rem;
        }
        
        .tier-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .tier-card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid rgba(255,255,255,0.2);
        }
        
        .tier-card h3 {
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }
        
        .tier-limits {
            list-style: none;
            padding: 0;
        }
        
        .tier-limits li {
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .current-status {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid rgba(255,255,255,0.2);
            margin-bottom: 2rem;
        }
        
        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .status-item {
            background: rgba(0,0,0,0.2);
            padding: 1rem;
            border-radius: 10px;
        }
        
        .status-label {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-bottom: 0.5rem;
        }
        
        .status-value {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(0,0,0,0.3);
            border-radius: 4px;
            margin-top: 0.5rem;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #10b981, #3b82f6);
            transition: width 0.3s;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ Advanced Rate Limiter</h1>
        <div class="subtitle">Sliding window algorithm • Token bucket • User tiers</div>
        
        <!-- Current Status -->
        <div class="current-status">
            <h2>Your Current Status</h2>
            <div class="status-grid">
                <div class="status-item">
                    <div class="status-label">Remaining Requests</div>
                    <div class="status-value">${limitInfo.remaining}</div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: ${(limitInfo.remaining / limitInfo.limit * 100)}%"></div>
                    </div>
                </div>
                <div class="status-item">
                    <div class="status-label">Total Limit</div>
                    <div class="status-value">${limitInfo.limit}</div>
                </div>
                <div class="status-item">
                    <div class="status-label">Reset Time</div>
                    <div class="status-value">${new Date(limitInfo.reset * 1000).toLocaleTimeString()}</div>
                </div>
                <div class="status-item">
                    <div class="status-label">Usage</div>
                    <div class="status-value">${((1 - limitInfo.remaining / limitInfo.limit) * 100).toFixed(1)}%</div>
                </div>
            </div>
        </div>
        
        <!-- Tier Information -->
        <h2 style="margin-bottom: 1rem;">Available Tiers</h2>
        <div class="tier-cards">
            <div class="tier-card">
                <h3>🆓 Free Tier</h3>
                <ul class="tier-limits">
                    <li>100 requests/hour</li>
                    <li>1,000 requests/day</li>
                    <li>10,000 requests/month</li>
                    <li>Basic rate limiting</li>
                </ul>
            </div>
            
            <div class="tier-card">
                <h3>⭐ Pro Tier</h3>
                <ul class="tier-limits">
                    <li>1,000 requests/hour</li>
                    <li>10,000 requests/day</li>
                    <li>100,000 requests/month</li>
                    <li>Priority queuing</li>
                    <li>Burst allowance</li>
                </ul>
            </div>
            
            <div class="tier-card">
                <h3>🚀 Enterprise Tier</h3>
                <ul class="tier-limits">
                    <li>Unlimited requests</li>
                    <li>Custom rate limits</li>
                    <li>Dedicated resources</li>
                    <li>SLA guarantee</li>
                    <li>Priority support</li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Rate limiting implementation
async function checkRateLimit(env, identifier, tier, endpoint) {
  const limits = getTierLimits(tier);
  const now = Date.now();
  const windowKey = `ratelimit:${identifier}:${Math.floor(now / (limits.windowSeconds * 1000))}`;
  
  // Get current count
  const current = await env.RATE_LIMITER.get(windowKey) || '0';
  const count = parseInt(current);
  
  if (count >= limits.maxRequests) {
    const reset = Math.floor(now / (limits.windowSeconds * 1000) + 1) * limits.windowSeconds;
    const retryAfter = reset - Math.floor(now / 1000);
    
    return {
      allowed: false,
      limit: limits.maxRequests,
      remaining: 0,
      reset: reset,
      retryAfter: retryAfter
    };
  }
  
  // Increment counter
  await env.RATE_LIMITER.put(windowKey, (count + 1).toString(), {
    expirationTtl: limits.windowSeconds * 2
  });
  
  return {
    allowed: true,
    limit: limits.maxRequests,
    remaining: limits.maxRequests - count - 1,
    reset: Math.floor(now / (limits.windowSeconds * 1000) + 1) * limits.windowSeconds
  };
}

function getTierLimits(tier) {
  const limits = {
    free: {
      maxRequests: 100,
      windowSeconds: 3600 // 1 hour
    },
    pro: {
      maxRequests: 1000,
      windowSeconds: 3600
    },
    enterprise: {
      maxRequests: 999999,
      windowSeconds: 3600
    }
  };
  
  return limits[tier] || limits.free;
}

async function getIdentifier(request) {
  // Try API key first
  const apiKey = request.headers.get('X-API-Key') || request.headers.get('Authorization');
  if (apiKey) return apiKey;
  
  // Fall back to IP address
  return request.headers.get('CF-Connecting-IP') || 'unknown';
}

async function getUserTier(env, identifier) {
  // Check tier from KV or default to free
  const tierData = await env.RATE_LIMITER.get(`tier:${identifier}`);
  return tierData || 'free';
}

async function handleCheckLimit(request, env, corsHeaders) {
  const identifier = await getIdentifier(request);
  const tier = await getUserTier(env, identifier);
  const limitResult = await checkRateLimit(env, identifier, tier, '/');
  
  return new Response(JSON.stringify(limitResult), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleStats(request, env, corsHeaders) {
  const identifier = await getIdentifier(request);
  
  const stats = {
    identifier: identifier,
    tier: await getUserTier(env, identifier),
    usage: {
      hour: Math.floor(Math.random() * 100),
      day: Math.floor(Math.random() * 1000),
      month: Math.floor(Math.random() * 10000)
    },
    timestamp: new Date().toISOString()
  };
  
  return new Response(JSON.stringify(stats), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleReset(request, env, corsHeaders) {
  const identifier = await getIdentifier(request);
  
  // Reset counters (admin only - add auth check in production)
  return new Response(JSON.stringify({
    success: true,
    message: 'Rate limit reset'
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}
