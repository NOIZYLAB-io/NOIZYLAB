interface TaskRequest {
  task_id?: string;
  task_type: string;
  task_data: Record<string, any>;
  priority?: string;
}

interface TaskResponse {
  task_id: string;
  status: "accepted" | "processing" | "completed" | "failed";
  result?: any;
  error?: string;
  timestamp: string;
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
  }
};

export default {
  async fetch(request: Request, env: Record<string, any>, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    const corsHeaders = {
      "Access-Control-Allow-Origin": env.ALLOWED_ORIGINS || "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization",
      "Content-Type": "application/json"
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    if (url.pathname === "/health") {
      return new Response(JSON.stringify({ 
        status: "ok", 
        env: env.ENV,
        agent: "cloud-agent",
        version: "1.0.0"
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

    if (url.pathname === "/api/delegate" && request.method === "POST") {
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

        return new Response(JSON.stringify({
          task_id,
          status: "completed",
          result,
          timestamp: new Date().toISOString()
        } as TaskResponse), {
          headers: corsHeaders
        });

      } catch (error) {
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
      version: "1.0.0",
      endpoints: {
        health: "/health",
        capabilities: "/api/capabilities",
        delegate: "/api/delegate (POST)",
        status: "/api/status?task_id=<id> (GET)"
      }
    }), {
      headers: corsHeaders
    });
  }
};
