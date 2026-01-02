// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB CHAT AGENT - Real-Time AI Repair Assistant
// "The Mentor" Edition - Your Expert in Your Pocket
// ═══════════════════════════════════════════════════════════════════════════════

export interface Env {
  ANTHROPIC_API_KEY: string;
  OPENAI_API_KEY: string;
  DB: D1Database;
  CHAT_SESSIONS: KVNamespace;
}

// ═══════════════════════════════════════════════════════════════════════════════
// AGENT PERSONAS
// ═══════════════════════════════════════════════════════════════════════════════

const PERSONAS: Record<string, {
  name: string;
  role: string;
  system_prompt: string;
  temperature: number;
  voice_mode?: string;
}> = {
  MASTER_TECH: {
    name: "Master Tech",
    role: "Senior Repair Technician",
    system_prompt: `You are a master electronics repair technician with 25+ years of experience. You specialize in:
- Apple device repair (MacBooks, iPhones, iPads)
- Micro-soldering and BGA rework
- Component-level troubleshooting
- Schematic reading and signal tracing

Communication style:
- Direct and practical
- Use technical terms but explain when needed
- Share real-world tips and shortcuts
- Warn about common mistakes
- Encourage proper technique

When helping with repairs:
1. Ask clarifying questions if needed
2. Provide step-by-step guidance
3. Explain WHY each step matters
4. Suggest tools and techniques
5. Offer alternatives when available

Safety first - always remind about ESD, proper ventilation, and safety glasses.`,
    temperature: 0.7,
    voice_mode: "TEACHING"
  },
  
  DIAGNOSTIC_AI: {
    name: "Dr. Circuit",
    role: "Diagnostic Specialist",
    system_prompt: `You are an AI diagnostic specialist for electronics repair. Your expertise:
- Power rail analysis and voltage diagnosis
- Signal tracing and logic analysis  
- Thermal analysis interpretation
- Failure mode identification

Your approach:
- Methodical and systematic
- Data-driven decision making
- Consider all possibilities before concluding
- Explain the logic behind each diagnostic step

Always ask for:
- Specific voltage readings
- Visual observations
- Smell/sound indicators
- History of the device

Provide probability-based diagnoses when uncertain.`,
    temperature: 0.3,
    voice_mode: "FOCUS"
  },
  
  PARTS_HUNTER: {
    name: "Scavenger",
    role: "Parts Sourcing Expert",
    system_prompt: `You are an expert at finding replacement parts for electronics repair. You know:
- Best suppliers for each component type
- How to identify compatible alternatives
- Cross-reference part numbers
- Evaluate quality vs cost tradeoffs
- Spot counterfeit components

Help users find:
- Exact replacement parts
- Compatible alternatives
- Donor board opportunities
- Bulk buying strategies

Always consider shipping times and reliability of sources.`,
    temperature: 0.5,
    voice_mode: "NEUTRAL"
  },
  
  BUSINESS_COACH: {
    name: "Coach",
    role: "Repair Business Advisor",
    system_prompt: `You are a business coach for electronics repair professionals. You help with:
- Pricing strategies for repairs
- Customer communication
- Workshop organization
- Tool and equipment investments
- Marketing and lead generation
- Scaling operations

Your advice is:
- Practical and actionable
- Based on real repair shop economics
- Focused on profitability and sustainability
- Balanced between quality and efficiency`,
    temperature: 0.6,
    voice_mode: "CELEBRATE"
  },
  
  CALM_GUIDE: {
    name: "Zen",
    role: "Calm Mode Guide",
    system_prompt: `You are a calm, patient guide for repair work. Your role:
- Reduce stress and anxiety during difficult repairs
- Provide encouragement and reassurance
- Break complex tasks into manageable steps
- Remind about taking breaks
- Celebrate small wins

Your tone is:
- Warm and supportive
- Never rushed or pressuring
- Understanding of frustration
- Focused on the process, not just results

Include mindfulness tips:
- Deep breathing reminders
- Posture checks
- Hydration reminders
- Progress acknowledgment`,
    temperature: 0.8,
    voice_mode: "EMPATHY"
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// CHAT SESSION MANAGEMENT
// ═══════════════════════════════════════════════════════════════════════════════

interface ChatMessage {
  role: "user" | "assistant" | "system";
  content: string;
  timestamp: string;
  metadata?: {
    persona?: string;
    tool_calls?: any[];
    images?: string[];
  };
}

interface ChatSession {
  id: string;
  persona: string;
  context: {
    device?: string;
    ticket_id?: number;
    repair_stage?: string;
  };
  messages: ChatMessage[];
  created_at: string;
  updated_at: string;
}

async function getSession(env: Env, sessionId: string): Promise<ChatSession | null> {
  const data = await env.CHAT_SESSIONS.get(sessionId);
  return data ? JSON.parse(data) : null;
}

async function saveSession(env: Env, session: ChatSession): Promise<void> {
  session.updated_at = new Date().toISOString();
  await env.CHAT_SESSIONS.put(session.id, JSON.stringify(session), {
    expirationTtl: 86400 * 7  // 7 days
  });
}

function createSession(persona: string = "MASTER_TECH"): ChatSession {
  return {
    id: crypto.randomUUID(),
    persona,
    context: {},
    messages: [],
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString()
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// TOOL DEFINITIONS (Function Calling)
// ═══════════════════════════════════════════════════════════════════════════════

const TOOLS = [
  {
    name: "search_parts",
    description: "Search for replacement parts across suppliers",
    parameters: {
      type: "object",
      properties: {
        query: { type: "string", description: "Part number or component description" },
        board_model: { type: "string", description: "Board model number (e.g., 820-00239)" }
      },
      required: ["query"]
    }
  },
  {
    name: "lookup_schematic",
    description: "Look up component information in board schematics",
    parameters: {
      type: "object",
      properties: {
        component: { type: "string", description: "Component designator (e.g., U8900)" },
        board_model: { type: "string", description: "Board model number" }
      },
      required: ["component"]
    }
  },
  {
    name: "get_repair_guide",
    description: "Get step-by-step repair guide for a specific issue",
    parameters: {
      type: "object",
      properties: {
        device: { type: "string", description: "Device model" },
        issue: { type: "string", description: "The issue to repair" }
      },
      required: ["device", "issue"]
    }
  },
  {
    name: "calculate_repair_cost",
    description: "Calculate estimated cost for a repair",
    parameters: {
      type: "object",
      properties: {
        parts: { 
          type: "array", 
          items: { type: "string" },
          description: "List of parts needed"
        },
        labor_hours: { type: "number", description: "Estimated labor hours" },
        difficulty: { type: "string", enum: ["easy", "medium", "hard", "expert"] }
      },
      required: ["parts", "labor_hours"]
    }
  },
  {
    name: "find_similar_cases",
    description: "Find similar repair cases from history",
    parameters: {
      type: "object",
      properties: {
        symptoms: { 
          type: "array", 
          items: { type: "string" },
          description: "List of symptoms"
        },
        device: { type: "string", description: "Device model" }
      },
      required: ["symptoms"]
    }
  }
];

// ═══════════════════════════════════════════════════════════════════════════════
// TOOL EXECUTION
// ═══════════════════════════════════════════════════════════════════════════════

async function executeTool(
  env: Env,
  toolName: string,
  args: any
): Promise<string> {
  switch (toolName) {
    case "search_parts":
      // In production, this would call real suppliers' APIs
      return JSON.stringify({
        results: [
          { supplier: "iFixit", part: args.query, price: 24.99, in_stock: true },
          { supplier: "AliExpress", part: args.query, price: 8.50, in_stock: true, shipping: "2-3 weeks" },
          { supplier: "eBay", part: `${args.query} donor board`, price: 45.00, in_stock: true }
        ]
      });
      
    case "lookup_schematic":
      return JSON.stringify({
        component: args.component,
        function: "Power Management IC",
        connected_to: ["PPBUS_G3H", "PP5V_S5", "SMC"],
        test_points: ["Pin 1: VCC", "Pin 5: ENABLE", "Pin 12: GND"],
        common_issues: ["Check for shorts to ground", "Verify enable signal from SMC"]
      });
      
    case "get_repair_guide":
      return JSON.stringify({
        steps: [
          "Disconnect battery and all peripherals",
          "Remove logic board from chassis",
          "Locate component under microscope",
          "Apply flux and preheat to 150°C",
          "Reflow/replace component",
          "Clean with IPA",
          "Reassemble and test"
        ],
        tools_needed: ["Hot air station", "Microscope", "Flux", "IPA"],
        estimated_time: "45-60 minutes"
      });
      
    case "calculate_repair_cost":
      const partsCost = args.parts.length * 15;  // Simplified
      const laborRate = args.difficulty === "expert" ? 150 : 
                       args.difficulty === "hard" ? 100 : 
                       args.difficulty === "medium" ? 75 : 50;
      const laborCost = args.labor_hours * laborRate;
      return JSON.stringify({
        parts_cost: partsCost,
        labor_cost: laborCost,
        total: partsCost + laborCost,
        suggested_price: Math.round((partsCost + laborCost) * 1.5)
      });
      
    case "find_similar_cases":
      return JSON.stringify({
        cases: [
          { 
            id: 1, 
            symptoms: args.symptoms,
            diagnosis: "Faulty PMIC", 
            solution: "Replaced U8900",
            success_rate: 0.85
          }
        ]
      });
      
    default:
      return JSON.stringify({ error: "Unknown tool" });
  }
}

// ═══════════════════════════════════════════════════════════════════════════════
// CHAT COMPLETION
// ═══════════════════════════════════════════════════════════════════════════════

async function chat(
  env: Env,
  session: ChatSession,
  userMessage: string,
  imageBase64?: string
): Promise<{ response: string; tool_results?: any[] }> {
  const persona = PERSONAS[session.persona] || PERSONAS.MASTER_TECH;
  
  // Build messages array
  const messages: any[] = [
    { role: "system", content: persona.system_prompt }
  ];
  
  // Add context if available
  if (session.context.device) {
    messages.push({
      role: "system",
      content: `Current device: ${session.context.device}`
    });
  }
  
  // Add conversation history (last 20 messages)
  for (const msg of session.messages.slice(-20)) {
    messages.push({ role: msg.role, content: msg.content });
  }
  
  // Add current message
  if (imageBase64) {
    messages.push({
      role: "user",
      content: [
        { type: "image", source: { type: "base64", media_type: "image/jpeg", data: imageBase64 } },
        { type: "text", text: userMessage }
      ]
    });
  } else {
    messages.push({ role: "user", content: userMessage });
  }
  
  // Call Claude with tools
  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2024-01-01"
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 4000,
      temperature: persona.temperature,
      system: persona.system_prompt,
      messages: messages.slice(1),  // Remove system from messages
      tools: TOOLS.map(t => ({
        name: t.name,
        description: t.description,
        input_schema: t.parameters
      }))
    })
  });

  if (!response.ok) {
    throw new Error(`Claude API error: ${await response.text()}`);
  }

  const data = await response.json() as any;
  
  // Handle tool calls
  const toolResults: any[] = [];
  let finalResponse = "";
  
  for (const block of data.content) {
    if (block.type === "text") {
      finalResponse += block.text;
    } else if (block.type === "tool_use") {
      const result = await executeTool(env, block.name, block.input);
      toolResults.push({
        tool: block.name,
        input: block.input,
        output: JSON.parse(result)
      });
      
      // Get follow-up response with tool results
      messages.push({ role: "assistant", content: data.content });
      messages.push({
        role: "user",
        content: [{
          type: "tool_result",
          tool_use_id: block.id,
          content: result
        }]
      });
      
      const followUp = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": env.ANTHROPIC_API_KEY,
          "anthropic-version": "2024-01-01"
        },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 4000,
          temperature: persona.temperature,
          messages: messages.slice(1)
        })
      });
      
      if (followUp.ok) {
        const followUpData = await followUp.json() as any;
        finalResponse = followUpData.content
          .filter((b: any) => b.type === "text")
          .map((b: any) => b.text)
          .join("");
      }
    }
  }
  
  // Save messages to session
  session.messages.push({
    role: "user",
    content: userMessage,
    timestamp: new Date().toISOString()
  });
  
  session.messages.push({
    role: "assistant",
    content: finalResponse,
    timestamp: new Date().toISOString(),
    metadata: {
      persona: session.persona,
      tool_calls: toolResults.length > 0 ? toolResults : undefined
    }
  });
  
  return { response: finalResponse, tool_results: toolResults };
}

// ═══════════════════════════════════════════════════════════════════════════════
// STREAMING CHAT (SSE)
// ═══════════════════════════════════════════════════════════════════════════════

async function* streamChat(
  env: Env,
  session: ChatSession,
  userMessage: string
): AsyncGenerator<string> {
  const persona = PERSONAS[session.persona] || PERSONAS.MASTER_TECH;
  
  const messages: any[] = [];
  for (const msg of session.messages.slice(-20)) {
    messages.push({ role: msg.role, content: msg.content });
  }
  messages.push({ role: "user", content: userMessage });
  
  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2024-01-01"
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 4000,
      temperature: persona.temperature,
      system: persona.system_prompt,
      messages,
      stream: true
    })
  });

  if (!response.ok || !response.body) {
    throw new Error("Stream failed");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let fullResponse = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    
    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() || "";
    
    for (const line of lines) {
      if (line.startsWith("data: ")) {
        const data = line.slice(6);
        if (data === "[DONE]") continue;
        
        try {
          const parsed = JSON.parse(data);
          if (parsed.type === "content_block_delta" && parsed.delta?.text) {
            fullResponse += parsed.delta.text;
            yield parsed.delta.text;
          }
        } catch {}
      }
    }
  }
  
  // Save to session
  session.messages.push({ role: "user", content: userMessage, timestamp: new Date().toISOString() });
  session.messages.push({ role: "assistant", content: fullResponse, timestamp: new Date().toISOString() });
  await saveSession(env, session);
}

// ═══════════════════════════════════════════════════════════════════════════════
// WORKER
// ═══════════════════════════════════════════════════════════════════════════════

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json"
    };

    if (method === "OPTIONS") {
      return new Response(null, {
        headers: {
          ...corsHeaders,
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type"
        }
      });
    }

    try {
      // Health
      if (path === "/health") {
        return Response.json({ ok: true, service: "chat-agent" }, { headers: corsHeaders });
      }

      // List personas
      if (path === "/personas") {
        const personas = Object.entries(PERSONAS).map(([id, p]) => ({
          id,
          name: p.name,
          role: p.role
        }));
        return Response.json({ ok: true, personas }, { headers: corsHeaders });
      }

      // Create session
      if (path === "/session" && method === "POST") {
        const body = await request.json() as any;
        const session = createSession(body?.persona);
        
        if (body?.device) session.context.device = body.device;
        if (body?.ticket_id) session.context.ticket_id = body.ticket_id;
        
        await saveSession(env, session);
        
        return Response.json({ ok: true, session_id: session.id, persona: session.persona }, { headers: corsHeaders });
      }

      // Get session
      if (path.match(/^\/session\/[\w-]+$/) && method === "GET") {
        const sessionId = path.split("/").pop()!;
        const session = await getSession(env, sessionId);
        
        if (!session) {
          return Response.json({ ok: false, error: "Session not found" }, { status: 404, headers: corsHeaders });
        }
        
        return Response.json({ ok: true, session }, { headers: corsHeaders });
      }

      // Chat (non-streaming)
      if (path === "/chat" && method === "POST") {
        const body = await request.json() as any;
        const { session_id, message, image } = body;
        
        if (!session_id || !message) {
          return Response.json({ ok: false, error: "Missing session_id or message" }, { status: 400, headers: corsHeaders });
        }
        
        let session = await getSession(env, session_id);
        if (!session) {
          session = createSession();
          session.id = session_id;
        }
        
        const result = await chat(env, session, message, image);
        await saveSession(env, session);
        
        return Response.json({ 
          ok: true, 
          response: result.response,
          tool_results: result.tool_results,
          voice_mode: PERSONAS[session.persona]?.voice_mode
        }, { headers: corsHeaders });
      }

      // Streaming chat
      if (path === "/chat/stream" && method === "POST") {
        const body = await request.json() as any;
        const { session_id, message } = body;
        
        if (!session_id || !message) {
          return Response.json({ ok: false, error: "Missing session_id or message" }, { status: 400, headers: corsHeaders });
        }
        
        let session = await getSession(env, session_id);
        if (!session) {
          session = createSession();
          session.id = session_id;
        }
        
        const stream = new ReadableStream({
          async start(controller) {
            const encoder = new TextEncoder();
            try {
              for await (const chunk of streamChat(env, session!, message)) {
                controller.enqueue(encoder.encode(`data: ${JSON.stringify({ text: chunk })}\n\n`));
              }
              controller.enqueue(encoder.encode("data: [DONE]\n\n"));
            } catch (err: any) {
              controller.enqueue(encoder.encode(`data: ${JSON.stringify({ error: err.message })}\n\n`));
            }
            controller.close();
          }
        });
        
        return new Response(stream, {
          headers: {
            "Content-Type": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*"
          }
        });
      }

      // Quick question (no session)
      if (path === "/ask" && method === "POST") {
        const body = await request.json() as any;
        const { question, persona } = body;
        
        if (!question) {
          return Response.json({ ok: false, error: "Missing question" }, { status: 400, headers: corsHeaders });
        }
        
        const session = createSession(persona || "MASTER_TECH");
        const result = await chat(env, session, question);
        
        return Response.json({ 
          ok: true, 
          answer: result.response,
          persona: session.persona
        }, { headers: corsHeaders });
      }

      return Response.json({ ok: false, error: "Not found" }, { status: 404, headers: corsHeaders });

    } catch (err: any) {
      console.error("Chat agent error:", err);
      return Response.json(
        { ok: false, error: err.message || "Internal error" },
        { status: 500, headers: corsHeaders }
      );
    }
  }
};
