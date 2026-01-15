interface AgentTask {
  agent: string;
  action: string;
  params?: Record<string, any>;
}

interface AgentResponse {
  success: boolean;
  agent: string;
  action: string;
  result?: any;
  error?: string;
  timestamp: string;
}

// Cloud Agent implementations
const cloudAgents = {
  async systemGuardian(action: string, params: Record<string, any> = {}): Promise<any> {
    switch (action) {
      case 'status':
        return {
          uptime: Date.now(),
          health: 'healthy',
          services: ['monitoring', 'alerts']
        };
      case 'monitor':
        return {
          cpu: 'normal',
          memory: 'normal',
          disk: 'normal'
        };
      default:
        throw new Error(`Unknown action: ${action}`);
    }
  },

  async mc96(action: string, params: Record<string, any> = {}): Promise<any> {
    switch (action) {
      case 'organize':
        return {
          organized: true,
          filesProcessed: 0,
          message: 'Cloud organization completed'
        };
      case 'vault-status':
        return {
          vaultHealth: 'ok',
          totalFiles: 0
        };
      default:
        throw new Error(`Unknown action: ${action}`);
    }
  },

  async gabriel(action: string, params: Record<string, any> = {}): Promise<any> {
    switch (action) {
      case 'health':
        return {
          status: 'online',
          capabilities: ['voice', 'ui', 'automation']
        };
      case 'execute':
        return {
          executed: true,
          command: params.command || 'none'
        };
      default:
        throw new Error(`Unknown action: ${action}`);
    }
  }
};

export default {
  async fetch(request: Request, env: Record<string, any>, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    
    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // Health check endpoint
    if (url.pathname === "/health") {
      return new Response(JSON.stringify({ 
        status: "ok", 
        env: env.ENV,
        timestamp: new Date().toISOString()
      }), {
        headers: { 
          "content-type": "application/json",
          ...corsHeaders
        }
      });
    }

    // Agent delegation endpoint
    if (url.pathname === "/agent/delegate" && request.method === 'POST') {
      try {
        const task: AgentTask = await request.json();
        
        if (!task.agent || !task.action) {
          return new Response(JSON.stringify({
            success: false,
            error: 'Missing required fields: agent, action'
          }), {
            status: 400,
            headers: { 
              "content-type": "application/json",
              ...corsHeaders
            }
          });
        }

        const agentFunc = cloudAgents[task.agent as keyof typeof cloudAgents];
        if (!agentFunc) {
          return new Response(JSON.stringify({
            success: false,
            error: `Unknown agent: ${task.agent}. Available: ${Object.keys(cloudAgents).join(', ')}`
          }), {
            status: 404,
            headers: { 
              "content-type": "application/json",
              ...corsHeaders
            }
          });
        }

        const result = await agentFunc(task.action, task.params || {});
        
        const response: AgentResponse = {
          success: true,
          agent: task.agent,
          action: task.action,
          result,
          timestamp: new Date().toISOString()
        };

        return new Response(JSON.stringify(response), {
          headers: { 
            "content-type": "application/json",
            ...corsHeaders
          }
        });
      } catch (error: any) {
        const response: AgentResponse = {
          success: false,
          agent: 'unknown',
          action: 'unknown',
          error: error.message || 'Unknown error',
          timestamp: new Date().toISOString()
        };

        return new Response(JSON.stringify(response), {
          status: 500,
          headers: { 
            "content-type": "application/json",
            ...corsHeaders
          }
        });
      }
    }

    // List available agents
    if (url.pathname === "/agent/list") {
      return new Response(JSON.stringify({
        agents: Object.keys(cloudAgents),
        endpoint: '/agent/delegate',
        timestamp: new Date().toISOString()
      }), {
        headers: { 
          "content-type": "application/json",
          ...corsHeaders
        }
      });
    }

    return new Response("NOIZYLAB Worker is running 🚀\n\nEndpoints:\n- GET  /health\n- GET  /agent/list\n- POST /agent/delegate", {
      headers: { 
        "content-type": "text/plain",
        ...corsHeaders
      }
    });
  }
};
