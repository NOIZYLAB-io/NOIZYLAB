interface TaskRequest {
  task_id?: string;
  task_type: string;
  task_data: Record<string, any>;
  priority?: string;
  webhook_url?: string;
}

interface TaskResponse {
  task_id: string;
  status: "accepted" | "processing" | "completed" | "failed";
  result?: any;
  error?: string;
  timestamp: string;
}

interface BatchTaskRequest {
  tasks: TaskRequest[];
}

interface MetricsData {
  total_tasks: number;
  completed_tasks: number;
  failed_tasks: number;
  avg_duration_ms: number;
  last_reset: string;
}

// Rate limiting storage
interface RateLimitData {
  count: number;
  reset_time: number;
}

const taskHandlers: Record<string, (data: any) => Promise<any>> = {
  "echo": async (data: any) => {
    return { message: data.message || "Hello from cloud agent!" };
  },
  "inference": async (data: any) => {
    return { model: data.model, response: `Processed: ${data.prompt}` };
  },
  "code-analysis": async (data: any) => {
    return { files_analyzed: data.files?.length || 0, status: "complete" };
  },
  "monitoring": async (data: any) => {
    return { metrics: { cpu: 45, memory: 62, disk: 78 }, status: "healthy" };
  },
  "file-processing": async (data: any) => {
    const file_name = data.file_name || "unknown.txt";
    const file_size = data.file_size || 0;
    const file_type = data.file_type || "text/plain";
    
    return {
      file_name,
      file_size,
      file_type,
      processed: true,
      metadata: {
        lines: Math.floor(file_size / 80),
        estimated_processing_time_ms: file_size / 1000
      }
    };
  },
  "webhook": async (data: any) => {
    const url = data.url;
    const method = data.method || "GET";
    const payload = data.payload;
    
    if (!url) {
      throw new Error("url is required for webhook task");
    }
    
    const options: RequestInit = {
      method,
      headers: { "Content-Type": "application/json" }
    };
    
    if (payload && (method === "POST" || method === "PUT")) {
      options.body = JSON.stringify(payload);
    }
    
    const response = await fetch(url, options);
    const responseData = await response.text();
    
    return {
      url,
      method,
      status_code: response.status,
      response: responseData.substring(0, 1000) // Limit response size
    };
  },
  "data-transform": async (data: any) => {
    const input = data.input;
    const operation = data.operation || "identity";
    
    if (!input) {
      throw new Error("input is required for data-transform task");
    }
    
    let result;
    switch (operation) {
      case "uppercase":
        result = JSON.parse(JSON.stringify(input)).toString().toUpperCase();
        break;
      case "lowercase":
        result = JSON.parse(JSON.stringify(input)).toString().toLowerCase();
        break;
      case "reverse":
        if (Array.isArray(input)) {
          result = [...input].reverse();
        } else {
          result = input.toString().split("").reverse().join("");
        }
        break;
      case "sort":
        if (Array.isArray(input)) {
          result = [...input].sort();
        } else {
          result = input;
        }
        break;
      default:
        result = input;
    }
    
    return {
      operation,
      input,
      result
    };
  },
  "health-check": async (data: any) => {
    const url = data.url;
    
    if (!url) {
      throw new Error("url is required for health-check task");
    }
    
    try {
      const start = Date.now();
      const response = await fetch(url, { method: "HEAD" });
      const duration = Date.now() - start;
      
      return {
        url,
        available: response.ok,
        status_code: response.status,
        response_time_ms: duration,
        timestamp: new Date().toISOString()
      };
    } catch (error) {
      return {
        url,
        available: false,
        error: error instanceof Error ? error.message : "Unknown error",
        timestamp: new Date().toISOString()
      };
    }
  }
};

// Helper function to check API key authentication
function checkAuth(request: Request, env: Record<string, any>): boolean {
  const apiKey = request.headers.get("X-API-Key");
  
  // If no API key is configured, allow all requests
  if (!env.API_KEY) {
    return true;
  }
  
  return apiKey === env.API_KEY;
}

// Helper function to check rate limit
async function checkRateLimit(
  apiKey: string,
  env: Record<string, any>
): Promise<{ allowed: boolean; remaining: number }> {
  if (!env.RATE_LIMIT_KV) {
    // No rate limiting configured
    return { allowed: true, remaining: 10 };
  }
  
  const now = Date.now();
  const windowMs = 60 * 1000; // 1 minute
  const maxRequests = 10;
  
  const key = `ratelimit:${apiKey}`;
  const dataStr = await env.RATE_LIMIT_KV.get(key);
  
  let data: RateLimitData;
  if (dataStr) {
    data = JSON.parse(dataStr);
    
    // Reset if window expired
    if (now > data.reset_time) {
      data = { count: 0, reset_time: now + windowMs };
    }
  } else {
    data = { count: 0, reset_time: now + windowMs };
  }
  
  if (data.count >= maxRequests) {
    return { allowed: false, remaining: 0 };
  }
  
  data.count++;
  await env.RATE_LIMIT_KV.put(key, JSON.stringify(data), {
    expirationTtl: Math.ceil(windowMs / 1000)
  });
  
  return { allowed: true, remaining: maxRequests - data.count };
}

// Helper function to update metrics
async function updateMetrics(
  env: Record<string, any>,
  success: boolean,
  durationMs: number
): Promise<void> {
  if (!env.METRICS_KV) {
    return;
  }
  
  const key = "metrics:global";
  const dataStr = await env.METRICS_KV.get(key);
  
  let metrics: MetricsData;
  if (dataStr) {
    metrics = JSON.parse(dataStr);
  } else {
    metrics = {
      total_tasks: 0,
      completed_tasks: 0,
      failed_tasks: 0,
      avg_duration_ms: 0,
      last_reset: new Date().toISOString()
    };
  }
  
  metrics.total_tasks++;
  if (success) {
    metrics.completed_tasks++;
  } else {
    metrics.failed_tasks++;
  }
  
  // Update running average
  metrics.avg_duration_ms = 
    (metrics.avg_duration_ms * (metrics.total_tasks - 1) + durationMs) / metrics.total_tasks;
  
  await env.METRICS_KV.put(key, JSON.stringify(metrics));
}

// Helper function to send webhook
async function sendWebhook(
  url: string,
  payload: TaskResponse
): Promise<void> {
  try {
    await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
  } catch (error) {
    console.error(`Webhook failed: ${error}`);
  }
}

export default {
  async fetch(request: Request, env: Record<string, any>, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    const corsHeaders = {
      "Access-Control-Allow-Origin": env.ALLOWED_ORIGINS || "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization, X-API-Key",
      "Content-Type": "application/json"
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    // Check authentication for protected endpoints
    if (url.pathname.startsWith("/api/") && !checkAuth(request, env)) {
      return new Response(JSON.stringify({
        error: "Unauthorized",
        message: "Valid X-API-Key header required"
      }), {
        status: 401,
        headers: corsHeaders
      });
    }

    // Check rate limit for authenticated requests
    if (url.pathname.startsWith("/api/")) {
      const apiKey = request.headers.get("X-API-Key") || "anonymous";
      const rateLimit = await checkRateLimit(apiKey, env);
      
      if (!rateLimit.allowed) {
        return new Response(JSON.stringify({
          error: "Rate limit exceeded",
          message: "Maximum 10 requests per minute",
          retry_after: 60
        }), {
          status: 429,
          headers: {
            ...corsHeaders,
            "X-RateLimit-Remaining": "0",
            "Retry-After": "60"
          }
        });
      }
      
      // Add rate limit headers to all responses
      corsHeaders["X-RateLimit-Remaining"] = rateLimit.remaining.toString();
    }

    if (url.pathname === "/health") {
      return new Response(JSON.stringify({ 
        status: "ok", 
        env: env.ENV,
        agent: "cloud-agent",
        version: "2.0.0"
      }), {
        headers: corsHeaders
      });
    }

    if (url.pathname === "/api/capabilities") {
      return new Response(JSON.stringify({
        agent_id: "cloud-agent",
        capabilities: Object.keys(taskHandlers),
        status: "ready",
        timestamp: new Date().toISOString()
      }), {
        headers: corsHeaders
      });
    }

    if (url.pathname === "/api/metrics" && request.method === "GET") {
      if (!env.METRICS_KV) {
        return new Response(JSON.stringify({
          error: "Metrics not configured"
        }), {
          status: 503,
          headers: corsHeaders
        });
      }
      
      const dataStr = await env.METRICS_KV.get("metrics:global");
      const metrics: MetricsData = dataStr ? JSON.parse(dataStr) : {
        total_tasks: 0,
        completed_tasks: 0,
        failed_tasks: 0,
        avg_duration_ms: 0,
        last_reset: new Date().toISOString()
      };
      
      return new Response(JSON.stringify(metrics), {
        headers: corsHeaders
      });
    }

    if (url.pathname === "/api/batch" && request.method === "POST") {
      try {
        const batchRequest = await request.json() as BatchTaskRequest;
        
        if (!batchRequest.tasks || !Array.isArray(batchRequest.tasks)) {
          return new Response(JSON.stringify({
            error: "Invalid batch request",
            message: "tasks array is required"
          }), {
            status: 400,
            headers: corsHeaders
          });
        }
        
        if (batchRequest.tasks.length > 10) {
          return new Response(JSON.stringify({
            error: "Batch size exceeded",
            message: "Maximum 10 tasks per batch"
          }), {
            status: 400,
            headers: corsHeaders
          });
        }
        
        // Process all tasks in parallel
        const results = await Promise.all(
          batchRequest.tasks.map(async (task) => {
            const task_id = task.task_id || crypto.randomUUID();
            const startTime = Date.now();
            
            try {
              if (!task.task_type || !taskHandlers[task.task_type]) {
                return {
                  task_id,
                  status: "failed",
                  error: `Unknown task type: ${task.task_type}`,
                  timestamp: new Date().toISOString()
                } as TaskResponse;
              }
              
              const handler = taskHandlers[task.task_type];
              const result = await handler(task.task_data || {});
              
              const duration = Date.now() - startTime;
              ctx.waitUntil(updateMetrics(env, true, duration));
              
              const response: TaskResponse = {
                task_id,
                status: "completed",
                result,
                timestamp: new Date().toISOString()
              };
              
              // Send webhook if specified
              if (task.webhook_url) {
                ctx.waitUntil(sendWebhook(task.webhook_url, response));
              }
              
              return response;
            } catch (error) {
              const duration = Date.now() - startTime;
              ctx.waitUntil(updateMetrics(env, false, duration));
              
              return {
                task_id,
                status: "failed",
                error: error instanceof Error ? error.message : "Unknown error",
                timestamp: new Date().toISOString()
              } as TaskResponse;
            }
          })
        );
        
        return new Response(JSON.stringify({
          batch_id: crypto.randomUUID(),
          results,
          timestamp: new Date().toISOString()
        }), {
          headers: corsHeaders
        });
        
      } catch (error) {
        return new Response(JSON.stringify({
          error: "Batch processing failed",
          message: error instanceof Error ? error.message : "Unknown error"
        }), {
          status: 500,
          headers: corsHeaders
        });
      }
    }

    if (url.pathname === "/api/delegate" && request.method === "POST") {
      const startTime = Date.now();
      try {
        const taskRequest = await request.json() as TaskRequest;
        const task_id = taskRequest.task_id || crypto.randomUUID();

        if (taskRequest.task_id && taskRequest.task_id.length > 100) {
          return new Response(JSON.stringify({
            task_id,
            status: "failed",
            error: "task_id too long (max 100 characters)",
            timestamp: new Date().toISOString()
          } as TaskResponse), {
            status: 400,
            headers: corsHeaders
          });
        }

        if (!taskRequest.task_type || !taskHandlers[taskRequest.task_type]) {
          return new Response(JSON.stringify({
            task_id,
            status: "failed",
            error: `Unknown task type: ${taskRequest.task_type}. Available: ${Object.keys(taskHandlers).join(", ")}`,
            timestamp: new Date().toISOString()
          } as TaskResponse), {
            status: 400,
            headers: corsHeaders
          });
        }

        const handler = taskHandlers[taskRequest.task_type];
        const result = await handler(taskRequest.task_data || {});

        const duration = Date.now() - startTime;
        ctx.waitUntil(updateMetrics(env, true, duration));

        const response: TaskResponse = {
          task_id,
          status: "completed",
          result,
          timestamp: new Date().toISOString()
        };

        // Send webhook if specified
        if (taskRequest.webhook_url) {
          ctx.waitUntil(sendWebhook(taskRequest.webhook_url, response));
        }

        return new Response(JSON.stringify(response), {
          headers: corsHeaders
        });

      } catch (error) {
        const duration = Date.now() - startTime;
        ctx.waitUntil(updateMetrics(env, false, duration));
        
        return new Response(JSON.stringify({
          task_id: "error",
          status: "failed",
          error: error instanceof Error ? error.message : "Unknown error",
          timestamp: new Date().toISOString()
        } as TaskResponse), {
          status: 500,
          headers: corsHeaders
        });
      }
    }

    if (url.pathname === "/api/status" && request.method === "GET") {
      const task_id = url.searchParams.get("task_id");
      if (!task_id) {
        return new Response(JSON.stringify({
          error: "task_id parameter required"
        }), {
          status: 400,
          headers: corsHeaders
        });
      }

      return new Response(JSON.stringify({
        task_id,
        status: "completed",
        message: "Task status endpoint",
        timestamp: new Date().toISOString()
      }), {
        headers: corsHeaders
      });
    }

    return new Response(JSON.stringify({
      message: "NOIZYLAB Cloud Agent 🚀",
      version: "2.0.0",
      endpoints: {
        health: "/health",
        capabilities: "/api/capabilities",
        delegate: "/api/delegate (POST)",
        batch: "/api/batch (POST)",
        status: "/api/status?task_id=<id> (GET)",
        metrics: "/api/metrics (GET)"
      }
    }), {
      headers: corsHeaders
    });
  }
};
