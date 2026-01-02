// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB BRAIN WORKER - Claude Extended Thinking Diagnostic Engine
// "The Genius" Edition - Solves "Unsolvable" Repair Problems
// ═══════════════════════════════════════════════════════════════════════════════

export interface Env {
  ANTHROPIC_API_KEY: string;
  DB: D1Database;
  AI: Ai;  // Cloudflare AI for embeddings
}

// ═══════════════════════════════════════════════════════════════════════════════
// REPAIR KNOWLEDGE BASE
// ═══════════════════════════════════════════════════════════════════════════════

const COMPONENT_DATABASE: Record<string, {
  description: string;
  function: string;
  failure_modes: string[];
  test_points: string[];
  replacement_difficulty: number;  // 1-10
  common_causes: string[];
}> = {
  "U8900": {
    description: "Power Management IC (PMIC)",
    function: "Manages power rails, charging, and battery management",
    failure_modes: ["No power", "No charge", "Battery not detected", "Kernel panic on battery"],
    test_points: ["PP3V3_G3H", "PPBUS_G3H", "PP5V_S5"],
    replacement_difficulty: 8,
    common_causes: ["Liquid damage", "Voltage spike", "Short circuit downstream"]
  },
  "CD3215": {
    description: "USB-C/Thunderbolt Controller",
    function: "Handles USB-C PD negotiation and Thunderbolt data",
    failure_modes: ["No USB-C", "No charging", "No display output", "USB devices not recognized"],
    test_points: ["PP20V_USBC", "PP5V_S0", "TBT_FORCE_PWR"],
    replacement_difficulty: 9,
    common_causes: ["Bad cable/charger", "Liquid damage", "ESD"]
  },
  "ISL95828": {
    description: "CPU Voltage Regulator (IMVP)",
    function: "Provides precise voltage to CPU cores",
    failure_modes: ["No boot", "Immediate shutdown", "CPU thermal issues"],
    test_points: ["VCORE", "PP1V8_S0", "CPUVR_HOT_L"],
    replacement_difficulty: 7,
    common_causes: ["Thermal stress", "Age", "Power surge"]
  },
  "T2": {
    description: "Apple T2 Security Chip",
    function: "Secure boot, SSD controller, audio, FaceTime camera",
    failure_modes: ["Boot loop", "No SSD", "No audio", "Recovery mode stuck"],
    test_points: ["T2_RESET_L", "PP0V9_S0_T2", "SSD_PWREN"],
    replacement_difficulty: 10,
    common_causes: ["Software corruption", "Bridge OS failure", "Hardware fault rare"]
  },
  "U3100": {
    description: "GPU/Display Controller",
    function: "Handles display output and GPU power",
    failure_modes: ["No display", "Artifacts", "Backlight issues", "GPU panic"],
    test_points: ["PPVDDGFX", "GPU_PWROK", "EDP_HPD"],
    replacement_difficulty: 9,
    common_causes: ["Thermal damage", "Flexgate", "Manufacturing defect"]
  }
};

const SYMPTOM_PATTERNS: Record<string, {
  possible_causes: string[];
  diagnostic_steps: string[];
  quick_fixes: string[];
}> = {
  "no_power": {
    possible_causes: ["Dead battery", "Faulty charger", "U8900 failure", "Liquid damage", "Short circuit"],
    diagnostic_steps: [
      "Check charger output with multimeter",
      "Measure PPBUS_G3H (should be 12.6V)",
      "Check for shorts on PP3V3_G3H",
      "Inspect board for liquid damage indicators"
    ],
    quick_fixes: [
      "Try known-good charger",
      "Reset SMC (Shift+Ctrl+Option+Power)",
      "Disconnect battery and try DC power only"
    ]
  },
  "no_charge": {
    possible_causes: ["CD3215 failure", "Faulty port", "U8900 issue", "Liquid damage to charging circuit"],
    diagnostic_steps: [
      "Test both USB-C ports",
      "Check PP20V_USBC when charger connected",
      "Measure PPBUS_G3H for charging voltage",
      "Inspect USB-C ports for debris/damage"
    ],
    quick_fixes: [
      "Clean USB-C port with isopropyl alcohol",
      "Try multiple chargers and cables",
      "Reset SMC"
    ]
  },
  "kernel_panic": {
    possible_causes: ["RAM failure", "SSD issue", "T2 problem", "Software corruption", "Thermal throttling"],
    diagnostic_steps: [
      "Run Apple Diagnostics (D at boot)",
      "Check panic logs in Console",
      "Test with external boot drive",
      "Monitor temperatures under load"
    ],
    quick_fixes: [
      "Reset NVRAM (Option+Command+P+R)",
      "Boot to Recovery, run First Aid",
      "Reinstall macOS"
    ]
  },
  "no_display": {
    possible_causes: ["Backlight failure", "Display cable", "U3100/GPU issue", "T-CON board", "LCD panel"],
    diagnostic_steps: [
      "Shine flashlight on screen (check for faint image)",
      "Connect external display",
      "Check EDP_HPD signal",
      "Measure backlight fuse"
    ],
    quick_fixes: [
      "Reset SMC and NVRAM",
      "Reseat display cable",
      "Try external display to isolate"
    ]
  },
  "liquid_damage": {
    possible_causes: ["Corrosion on components", "Short circuits", "Damaged traces", "Oxidized connectors"],
    diagnostic_steps: [
      "Full visual inspection under microscope",
      "Check all power rails for shorts",
      "Look for green/white corrosion",
      "Ultrasonic cleaning before further diagnosis"
    ],
    quick_fixes: [
      "Disconnect battery immediately",
      "Do NOT try to power on",
      "Ultrasonic clean with 99% IPA",
      "Dry thoroughly before testing"
    ]
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// CLAUDE EXTENDED THINKING ENGINE
// ═══════════════════════════════════════════════════════════════════════════════

interface DiagnosticRequest {
  device: string;
  symptoms: string[];
  observations: string;
  tests_performed?: string[];
  photos_analysis?: string;  // From vision worker
  history?: string;
}

interface DiagnosticResult {
  thinking_process: string;
  diagnosis: {
    primary: string;
    confidence: number;
    secondary: string[];
  };
  root_cause: string;
  repair_plan: {
    step: number;
    action: string;
    tools_needed: string[];
    estimated_time: string;
    difficulty: number;
    warning?: string;
  }[];
  parts_needed: {
    component: string;
    part_number?: string;
    estimated_cost: number;
    source?: string;
  }[];
  estimated_success_rate: number;
  total_repair_time: string;
  total_cost: number;
  alternative_approaches?: string[];
  prevention_tips: string[];
}

async function diagnoseWithExtendedThinking(
  env: Env,
  request: DiagnosticRequest
): Promise<DiagnosticResult> {
  // Build context from our knowledge base
  const relevantComponents: string[] = [];
  const relevantSymptoms: string[] = [];
  
  for (const symptom of request.symptoms) {
    const normalized = symptom.toLowerCase().replace(/\s+/g, "_");
    if (SYMPTOM_PATTERNS[normalized]) {
      relevantSymptoms.push(normalized);
    }
  }
  
  // Build the prompt for Claude
  const systemPrompt = `You are an expert electronics repair technician with 20+ years of experience in Apple device repair. You have deep knowledge of:
- Logic board micro-soldering and BGA rework
- Power management circuits and voltage regulation
- USB-C/Thunderbolt architecture
- macOS boot process and diagnostics
- Component-level troubleshooting

COMPONENT DATABASE:
${JSON.stringify(COMPONENT_DATABASE, null, 2)}

SYMPTOM PATTERNS:
${JSON.stringify(SYMPTOM_PATTERNS, null, 2)}

Your task is to provide a detailed diagnosis using extended thinking. Think through the problem step by step, considering all possibilities before reaching a conclusion.`;

  const userPrompt = `DEVICE: ${request.device}

SYMPTOMS:
${request.symptoms.map(s => `- ${s}`).join("\n")}

OBSERVATIONS:
${request.observations}

${request.tests_performed ? `TESTS PERFORMED:\n${request.tests_performed.map(t => `- ${t}`).join("\n")}` : ""}

${request.photos_analysis ? `PHOTO ANALYSIS (from AI vision):\n${request.photos_analysis}` : ""}

${request.history ? `DEVICE HISTORY:\n${request.history}` : ""}

Please provide:
1. Your extended thinking process (show your reasoning)
2. Primary diagnosis with confidence level
3. Root cause analysis
4. Detailed repair plan with step-by-step instructions
5. Parts needed with estimated costs
6. Success rate estimate
7. Alternative approaches if primary repair fails
8. Prevention tips for the future

Respond in JSON format matching the DiagnosticResult interface.`;

  // Call Claude with Extended Thinking
  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2024-01-01",
      "anthropic-beta": "extended-thinking-2025-01-01"
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 16000,
      thinking: {
        type: "enabled",
        budget_tokens: 10000  // Allow deep reasoning
      },
      system: systemPrompt,
      messages: [
        { role: "user", content: userPrompt }
      ]
    })
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Claude API error: ${error}`);
  }

  const data = await response.json() as any;
  
  // Extract thinking and response
  let thinkingProcess = "";
  let responseText = "";
  
  for (const block of data.content) {
    if (block.type === "thinking") {
      thinkingProcess = block.thinking;
    } else if (block.type === "text") {
      responseText = block.text;
    }
  }

  // Parse the JSON response
  try {
    // Extract JSON from response (might have markdown code blocks)
    const jsonMatch = responseText.match(/```json\n?([\s\S]*?)\n?```/) || 
                      responseText.match(/\{[\s\S]*\}/);
    const jsonStr = jsonMatch ? (jsonMatch[1] || jsonMatch[0]) : responseText;
    const result = JSON.parse(jsonStr) as DiagnosticResult;
    result.thinking_process = thinkingProcess;
    return result;
  } catch {
    // Return structured error response
    return {
      thinking_process: thinkingProcess,
      diagnosis: {
        primary: "Unable to parse diagnosis",
        confidence: 0,
        secondary: []
      },
      root_cause: responseText,
      repair_plan: [],
      parts_needed: [],
      estimated_success_rate: 0,
      total_repair_time: "Unknown",
      total_cost: 0,
      prevention_tips: []
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════════
// SMART COMPONENT IDENTIFIER (from image)
// ═══════════════════════════════════════════════════════════════════════════════

interface ComponentMatch {
  designator: string;
  name: string;
  confidence: number;
  datasheet_url?: string;
  replacement_options: {
    source: string;
    part_number: string;
    price: number;
    url: string;
  }[];
}

async function identifyComponent(
  env: Env,
  imageBase64: string,
  boardModel?: string
): Promise<ComponentMatch[]> {
  // Use Claude's vision to identify components
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
      messages: [{
        role: "user",
        content: [
          {
            type: "image",
            source: {
              type: "base64",
              media_type: "image/jpeg",
              data: imageBase64
            }
          },
          {
            type: "text",
            text: `Identify all visible electronic components in this PCB image.
${boardModel ? `This is from a ${boardModel}.` : ""}

For each component, provide:
1. Designator (e.g., U8900, C1234, R5678)
2. Component type and likely function
3. Confidence level (0-1)
4. Common replacement part numbers if known

Focus on ICs, capacitors, resistors, inductors, and connectors.
Respond in JSON array format.`
          }
        ]
      }]
    })
  });

  if (!response.ok) {
    throw new Error(`Claude Vision API error: ${await response.text()}`);
  }

  const data = await response.json() as any;
  const text = data.content[0]?.text || "[]";
  
  try {
    const jsonMatch = text.match(/```json\n?([\s\S]*?)\n?```/) || text.match(/\[[\s\S]*\]/);
    return JSON.parse(jsonMatch ? (jsonMatch[1] || jsonMatch[0]) : "[]");
  } catch {
    return [];
  }
}

// ═══════════════════════════════════════════════════════════════════════════════
// REPAIR HISTORY LEARNING
// ═══════════════════════════════════════════════════════════════════════════════

interface RepairOutcome {
  device: string;
  symptoms: string[];
  diagnosis: string;
  repair_performed: string;
  success: boolean;
  notes?: string;
}

async function learnFromRepair(env: Env, outcome: RepairOutcome): Promise<void> {
  // Store for future learning
  await env.DB.prepare(
    `INSERT INTO repair_outcomes 
     (device, symptoms_json, diagnosis, repair_performed, success, notes, created_at) 
     VALUES (?,?,?,?,?,?,?)`
  ).bind(
    outcome.device,
    JSON.stringify(outcome.symptoms),
    outcome.diagnosis,
    outcome.repair_performed,
    outcome.success ? 1 : 0,
    outcome.notes || null,
    new Date().toISOString()
  ).run();

  // Generate embedding for semantic search
  const text = `${outcome.device} ${outcome.symptoms.join(" ")} ${outcome.diagnosis} ${outcome.repair_performed}`;
  
  // Use Cloudflare AI for embedding
  const embedding = await env.AI.run("@cf/baai/bge-base-en-v1.5", {
    text: [text]
  }) as { data: number[][] };

  if (embedding.data?.[0]) {
    await env.DB.prepare(
      `UPDATE repair_outcomes SET embedding = ? WHERE rowid = last_insert_rowid()`
    ).bind(JSON.stringify(embedding.data[0])).run();
  }
}

async function findSimilarRepairs(
  env: Env,
  symptoms: string[],
  device: string,
  limit: number = 5
): Promise<RepairOutcome[]> {
  const text = `${device} ${symptoms.join(" ")}`;
  
  // Get embedding
  const embedding = await env.AI.run("@cf/baai/bge-base-en-v1.5", {
    text: [text]
  }) as { data: number[][] };

  if (!embedding.data?.[0]) return [];

  // Find similar (in production, use vector DB like Vectorize)
  const all = await env.DB.prepare(
    `SELECT *, embedding FROM repair_outcomes WHERE embedding IS NOT NULL ORDER BY created_at DESC LIMIT 100`
  ).all<any>();

  // Calculate cosine similarity
  const queryVec = embedding.data[0];
  const scored = (all.results || []).map(row => {
    const docVec = JSON.parse(row.embedding);
    const similarity = cosineSimilarity(queryVec, docVec);
    return { ...row, similarity };
  });

  // Sort and return top matches
  scored.sort((a, b) => b.similarity - a.similarity);
  
  return scored.slice(0, limit).map(r => ({
    device: r.device,
    symptoms: JSON.parse(r.symptoms_json),
    diagnosis: r.diagnosis,
    repair_performed: r.repair_performed,
    success: r.success === 1,
    notes: r.notes
  }));
}

function cosineSimilarity(a: number[], b: number[]): number {
  let dotProduct = 0;
  let normA = 0;
  let normB = 0;
  for (let i = 0; i < a.length; i++) {
    dotProduct += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }
  return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
}

// ═══════════════════════════════════════════════════════════════════════════════
// SCHEMATIC SEARCH
// ═══════════════════════════════════════════════════════════════════════════════

interface SchematicResult {
  component: string;
  page: number;
  section: string;
  connected_to: string[];
  power_rails: string[];
  notes: string;
}

async function searchSchematic(
  env: Env,
  boardModel: string,
  query: string
): Promise<SchematicResult[]> {
  // This would integrate with a schematic database
  // For now, return mock data based on common lookups
  
  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2024-01-01"
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 2000,
      system: `You are an expert at reading Apple logic board schematics. 
Given a board model and component query, provide information about:
- The component's location in the schematic
- Connected components and signals
- Relevant power rails
- Common issues and test points`,
      messages: [{
        role: "user",
        content: `Board: ${boardModel}\nQuery: ${query}\n\nProvide schematic information in JSON format.`
      }]
    })
  });

  if (!response.ok) return [];
  
  const data = await response.json() as any;
  const text = data.content[0]?.text || "[]";
  
  try {
    return JSON.parse(text.match(/\[[\s\S]*\]/)?.[0] || "[]");
  } catch {
    return [];
  }
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
          "Access-Control-Allow-Headers": "Content-Type, Authorization"
        }
      });
    }

    try {
      // Health
      if (path === "/health") {
        return Response.json({ ok: true, service: "brain" }, { headers: corsHeaders });
      }

      // Get component info
      if (path === "/component" && method === "GET") {
        const designator = url.searchParams.get("id");
        if (!designator) {
          return Response.json({ ok: false, error: "Missing id" }, { status: 400, headers: corsHeaders });
        }
        
        const component = COMPONENT_DATABASE[designator.toUpperCase()];
        if (!component) {
          return Response.json({ ok: false, error: "Component not found" }, { status: 404, headers: corsHeaders });
        }
        
        return Response.json({ ok: true, component }, { headers: corsHeaders });
      }

      // Get symptom patterns
      if (path === "/symptoms" && method === "GET") {
        const symptom = url.searchParams.get("id");
        if (symptom) {
          const pattern = SYMPTOM_PATTERNS[symptom.toLowerCase().replace(/\s+/g, "_")];
          return Response.json({ ok: true, pattern: pattern || null }, { headers: corsHeaders });
        }
        return Response.json({ ok: true, symptoms: Object.keys(SYMPTOM_PATTERNS) }, { headers: corsHeaders });
      }

      // Extended thinking diagnosis
      if (path === "/diagnose" && method === "POST") {
        const body = await request.json() as DiagnosticRequest;
        
        if (!body.device || !body.symptoms || body.symptoms.length === 0) {
          return Response.json(
            { ok: false, error: "Missing device or symptoms" },
            { status: 400, headers: corsHeaders }
          );
        }
        
        const result = await diagnoseWithExtendedThinking(env, body);
        
        // Store diagnosis
        await env.DB.prepare(
          `INSERT INTO diagnoses (device, symptoms_json, result_json, created_at) VALUES (?,?,?,?)`
        ).bind(
          body.device,
          JSON.stringify(body.symptoms),
          JSON.stringify(result),
          new Date().toISOString()
        ).run();
        
        return Response.json({ ok: true, result }, { headers: corsHeaders });
      }

      // Identify component from image
      if (path === "/identify" && method === "POST") {
        const formData = await request.formData();
        const imageFile = formData.get("image") as File;
        const boardModel = formData.get("board_model") as string;
        
        if (!imageFile) {
          return Response.json({ ok: false, error: "Missing image" }, { status: 400, headers: corsHeaders });
        }
        
        const bytes = await imageFile.arrayBuffer();
        const base64 = btoa(String.fromCharCode(...new Uint8Array(bytes)));
        
        const components = await identifyComponent(env, base64, boardModel);
        
        return Response.json({ ok: true, components }, { headers: corsHeaders });
      }

      // Learn from repair outcome
      if (path === "/learn" && method === "POST") {
        const body = await request.json() as RepairOutcome;
        
        if (!body.device || !body.symptoms || !body.diagnosis || !body.repair_performed) {
          return Response.json(
            { ok: false, error: "Missing required fields" },
            { status: 400, headers: corsHeaders }
          );
        }
        
        await learnFromRepair(env, body);
        
        return Response.json({ ok: true, message: "Learning recorded" }, { headers: corsHeaders });
      }

      // Find similar repairs
      if (path === "/similar" && method === "POST") {
        const body = await request.json() as { device: string; symptoms: string[] };
        
        const similar = await findSimilarRepairs(env, body.symptoms, body.device);
        
        return Response.json({ ok: true, similar }, { headers: corsHeaders });
      }

      // Search schematic
      if (path === "/schematic" && method === "GET") {
        const board = url.searchParams.get("board");
        const query = url.searchParams.get("q");
        
        if (!board || !query) {
          return Response.json(
            { ok: false, error: "Missing board or query" },
            { status: 400, headers: corsHeaders }
          );
        }
        
        const results = await searchSchematic(env, board, query);
        
        return Response.json({ ok: true, results }, { headers: corsHeaders });
      }

      return Response.json({ ok: false, error: "Not found" }, { status: 404, headers: corsHeaders });

    } catch (err: any) {
      console.error("Brain worker error:", err);
      return Response.json(
        { ok: false, error: err.message || "Internal error" },
        { status: 500, headers: corsHeaders }
      );
    }
  }
};
