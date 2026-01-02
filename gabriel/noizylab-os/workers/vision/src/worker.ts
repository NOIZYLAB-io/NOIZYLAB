// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB VISION WORKER - Golden Reference PCB Analysis
// "The All-Seeing Eye" Edition
// ═══════════════════════════════════════════════════════════════════════════════

export interface Env {
  // AI
  AI: Ai;
  
  // Storage
  GOLDEN_REFS: R2Bucket;    // Golden reference images
  UPLOADS: R2Bucket;        // User uploads
  DB: D1Database;
  
  // Config
  GEMINI_API_KEY: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════════════

interface BoardFinding {
  component: string;
  issue: string;
  confidence: number;
  severity: "critical" | "high" | "medium" | "low";
  fix_video?: string;
  coordinates: {
    x1: number;
    y1: number;
    x2: number;
    y2: number;
  };
  repair_time_mins: number;
  parts_cost_usd: number;
  skill_level: "beginner" | "intermediate" | "advanced" | "expert";
}

interface AnalysisResult {
  board_id: string;
  analysis_id: string;
  timestamp: string;
  findings: BoardFinding[];
  overall_health: number;
  estimated_repair_cost: number;
  estimated_repair_time: string;
  flip_profit_potential: number;
}

// ═══════════════════════════════════════════════════════════════════════════════
// GOLDEN REFERENCE DATABASE
// ═══════════════════════════════════════════════════════════════════════════════

const BOARD_REGISTRY: Record<string, {
  name: string;
  golden_ref_key: string;
  components: string[];
  common_failures: string[];
  avg_repair_value: number;
  market_value_working: number;
}> = {
  "820-00239": {
    name: "MacBook Pro 15\" 2016 (Touch Bar)",
    golden_ref_key: "golden/macbook-pro-15-2016-820-00239.jpg",
    components: ["U8900", "U7800", "CD3215", "ISL95828"],
    common_failures: ["Flexgate", "Stage light", "USB-C chip failure"],
    avg_repair_value: 350,
    market_value_working: 800
  },
  "820-00281": {
    name: "MacBook Pro 13\" 2017 (Touch Bar)",
    golden_ref_key: "golden/macbook-pro-13-2017-820-00281.jpg",
    components: ["U8900", "U7800", "CD3215", "ISL95828", "U3100"],
    common_failures: ["Keyboard failure", "Battery swelling", "USB-C"],
    avg_repair_value: 280,
    market_value_working: 650
  },
  "820-01041": {
    name: "MacBook Pro 15\" 2018",
    golden_ref_key: "golden/macbook-pro-15-2018-820-01041.jpg",
    components: ["U8900", "U7800", "CD3217", "ISL95338", "T2"],
    common_failures: ["T2 chip failure", "Bridge OS crash", "Keyboard"],
    avg_repair_value: 400,
    market_value_working: 1000
  },
  "820-01598": {
    name: "MacBook Pro 16\" 2019",
    golden_ref_key: "golden/macbook-pro-16-2019-820-01598.jpg",
    components: ["U8900", "U7800", "CD3217", "ISL95338", "T2", "U3100"],
    common_failures: ["Display cable", "T2 issues", "Speaker popping"],
    avg_repair_value: 450,
    market_value_working: 1200
  },
  "820-02020": {
    name: "MacBook Pro 14\" 2021 M1 Pro",
    golden_ref_key: "golden/macbook-pro-14-2021-820-02020.jpg",
    components: ["M1 Pro SoC", "NAND", "USB-C controllers"],
    common_failures: ["Liquid damage", "Display spots", "NAND failure"],
    avg_repair_value: 550,
    market_value_working: 1600
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// VISION ANALYSIS
// ═══════════════════════════════════════════════════════════════════════════════

async function analyzeBoard(
  env: Env,
  userImageBytes: ArrayBuffer,
  boardId: string
): Promise<AnalysisResult> {
  const board = BOARD_REGISTRY[boardId];
  if (!board) {
    throw new Error(`Unknown board ID: ${boardId}`);
  }

  // Fetch golden reference
  const goldenRef = await env.GOLDEN_REFS.get(board.golden_ref_key);
  if (!goldenRef) {
    throw new Error(`Golden reference not found: ${board.golden_ref_key}`);
  }
  const goldenBytes = await goldenRef.arrayBuffer();

  // Use Cloudflare AI for initial analysis
  // Note: In production, you'd call Gemini API for ultra-high resolution
  const analysisId = crypto.randomUUID();

  // Build prompt for vision model
  const prompt = `You are an expert PCB diagnostic AI for ${board.name}.

TASK: Compare the user's board image against the golden reference and identify:
1. Missing or damaged components
2. Corrosion or liquid damage indicators
3. Cold solder joints or cracked traces
4. Burn marks or discoloration
5. Physical damage (cracks, chips, bent pins)

KNOWN COMPONENTS ON THIS BOARD:
${board.components.join(", ")}

COMMON FAILURES FOR THIS MODEL:
${board.common_failures.join(", ")}

For each issue found, provide:
- Component designator (e.g., U8900)
- Issue description
- Confidence level (0-1)
- Severity (critical/high/medium/low)
- Approximate pixel coordinates [x1, y1, x2, y2]
- Estimated repair time in minutes
- Parts cost in USD
- Required skill level

Respond in JSON format only.`;

  // Call Gemini for ultra-high resolution analysis
  const geminiResponse = await callGeminiVision(env, prompt, userImageBytes, goldenBytes);

  // Parse findings
  const findings = parseGeminiFindings(geminiResponse, boardId);

  // Calculate metrics
  const totalRepairCost = findings.reduce((sum, f) => sum + f.parts_cost_usd, 0) + 
    (findings.length * 25); // Labor baseline
  const totalRepairMins = findings.reduce((sum, f) => sum + f.repair_time_mins, 0);
  const overallHealth = Math.max(0, 100 - (findings.length * 15) - 
    (findings.filter(f => f.severity === "critical").length * 20));

  // Calculate flip profit
  const purchasePrice = overallHealth < 30 ? board.market_value_working * 0.15 :
    overallHealth < 50 ? board.market_value_working * 0.25 :
    overallHealth < 70 ? board.market_value_working * 0.4 :
    board.market_value_working * 0.6;
  
  const flipProfit = board.market_value_working - purchasePrice - totalRepairCost;

  return {
    board_id: boardId,
    analysis_id: analysisId,
    timestamp: new Date().toISOString(),
    findings,
    overall_health: overallHealth,
    estimated_repair_cost: totalRepairCost,
    estimated_repair_time: formatDuration(totalRepairMins),
    flip_profit_potential: Math.max(0, flipProfit)
  };
}

async function callGeminiVision(
  env: Env,
  prompt: string,
  userImage: ArrayBuffer,
  goldenImage: ArrayBuffer
): Promise<string> {
  // Convert to base64
  const userB64 = arrayBufferToBase64(userImage);
  const goldenB64 = arrayBufferToBase64(goldenImage);

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${env.GEMINI_API_KEY}`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [{
          parts: [
            { text: prompt },
            { 
              inline_data: { 
                mime_type: "image/jpeg", 
                data: goldenB64 
              }
            },
            { text: "Golden Reference (perfect board) above. User's board below:" },
            { 
              inline_data: { 
                mime_type: "image/jpeg", 
                data: userB64 
              }
            }
          ]
        }],
        generationConfig: {
          temperature: 0.1,
          maxOutputTokens: 4096,
          responseMimeType: "application/json"
        }
      })
    }
  );

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Gemini API error: ${error}`);
  }

  const data = await response.json() as any;
  return data.candidates?.[0]?.content?.parts?.[0]?.text ?? "{}";
}

function parseGeminiFindings(jsonStr: string, boardId: string): BoardFinding[] {
  try {
    const parsed = JSON.parse(jsonStr);
    const findings = parsed.findings || parsed.issues || [];
    
    return findings.map((f: any) => ({
      component: f.component || f.designator || "Unknown",
      issue: f.issue || f.description || "Unspecified issue",
      confidence: Math.min(1, Math.max(0, f.confidence || 0.5)),
      severity: f.severity || "medium",
      fix_video: getFixVideo(boardId, f.component, f.issue),
      coordinates: {
        x1: f.coordinates?.[0] || f.x1 || 0,
        y1: f.coordinates?.[1] || f.y1 || 0,
        x2: f.coordinates?.[2] || f.x2 || 100,
        y2: f.coordinates?.[3] || f.y2 || 100
      },
      repair_time_mins: f.repair_time_mins || f.time || 30,
      parts_cost_usd: f.parts_cost_usd || f.parts_cost || 0,
      skill_level: f.skill_level || "intermediate"
    }));
  } catch {
    return [];
  }
}

function getFixVideo(boardId: string, component: string, issue: string): string | undefined {
  // Map common repairs to tutorial videos
  const videos: Record<string, string> = {
    "U8900:cold solder": "https://noizylab.ai/v/u8900-reflow",
    "CD3215:failure": "https://noizylab.ai/v/cd3215-replacement",
    "ISL95828:short": "https://noizylab.ai/v/isl95828-diagnosis",
    "T2:crash": "https://noizylab.ai/v/t2-recovery",
    "NAND:failure": "https://noizylab.ai/v/nand-swap"
  };
  
  const key = `${component}:${issue.toLowerCase().split(" ")[0]}`;
  return videos[key];
}

function formatDuration(mins: number): string {
  if (mins < 60) return `${mins} minutes`;
  const hours = Math.floor(mins / 60);
  const remaining = mins % 60;
  return remaining > 0 ? `${hours}h ${remaining}m` : `${hours} hours`;
}

function arrayBufferToBase64(buffer: ArrayBuffer): string {
  const bytes = new Uint8Array(buffer);
  let binary = "";
  for (let i = 0; i < bytes.byteLength; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

// ═══════════════════════════════════════════════════════════════════════════════
// AR OVERLAY GENERATOR
// ═══════════════════════════════════════════════════════════════════════════════

interface AROverlay {
  canvas_width: number;
  canvas_height: number;
  markers: ARMarker[];
}

interface ARMarker {
  id: string;
  component: string;
  issue: string;
  severity: string;
  bounds: { x: number; y: number; width: number; height: number };
  label_position: { x: number; y: number };
  color: string;
}

function generateAROverlay(
  result: AnalysisResult,
  imageWidth: number,
  imageHeight: number
): AROverlay {
  const severityColors: Record<string, string> = {
    critical: "#ff0000",
    high: "#ff6600",
    medium: "#ffcc00",
    low: "#00cc00"
  };

  const markers: ARMarker[] = result.findings.map((f, i) => {
    const bounds = {
      x: f.coordinates.x1,
      y: f.coordinates.y1,
      width: f.coordinates.x2 - f.coordinates.x1,
      height: f.coordinates.y2 - f.coordinates.y1
    };

    // Position label above the marker
    const labelY = bounds.y > 50 ? bounds.y - 30 : bounds.y + bounds.height + 20;

    return {
      id: `marker-${i}`,
      component: f.component,
      issue: f.issue,
      severity: f.severity,
      bounds,
      label_position: { x: bounds.x, y: labelY },
      color: severityColors[f.severity] || "#ffffff"
    };
  });

  return {
    canvas_width: imageWidth,
    canvas_height: imageHeight,
    markers
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// WORKER FETCH HANDLER
// ═══════════════════════════════════════════════════════════════════════════════

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    // CORS
    if (method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization"
        }
      });
    }

    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json"
    };

    try {
      // Health check
      if (path === "/health") {
        return Response.json({ ok: true, service: "vision" }, { headers: corsHeaders });
      }

      // List supported boards
      if (path === "/boards" && method === "GET") {
        const boards = Object.entries(BOARD_REGISTRY).map(([id, info]) => ({
          id,
          name: info.name,
          common_failures: info.common_failures,
          avg_repair_value: info.avg_repair_value,
          market_value_working: info.market_value_working
        }));
        return Response.json({ ok: true, boards }, { headers: corsHeaders });
      }

      // Analyze board
      if (path === "/analyze" && method === "POST") {
        const formData = await request.formData();
        const imageFile = formData.get("image") as File;
        const boardId = formData.get("board_id") as string;

        if (!imageFile) {
          return Response.json({ ok: false, error: "Missing image" }, { status: 400, headers: corsHeaders });
        }
        if (!boardId) {
          return Response.json({ ok: false, error: "Missing board_id" }, { status: 400, headers: corsHeaders });
        }

        const imageBytes = await imageFile.arrayBuffer();
        const result = await analyzeBoard(env, imageBytes, boardId);

        // Store analysis
        await env.DB.prepare(
          "INSERT INTO board_analyses (id, board_id, result_json, created_at) VALUES (?,?,?,?)"
        ).bind(result.analysis_id, boardId, JSON.stringify(result), new Date().toISOString()).run();

        return Response.json({ ok: true, result }, { headers: corsHeaders });
      }

      // Get AR overlay
      if (path === "/overlay" && method === "POST") {
        const body = await request.json() as any;
        const { analysis_id, image_width, image_height } = body;

        // Fetch stored analysis
        const row = await env.DB.prepare(
          "SELECT result_json FROM board_analyses WHERE id=?"
        ).bind(analysis_id).first<any>();

        if (!row) {
          return Response.json({ ok: false, error: "Analysis not found" }, { status: 404, headers: corsHeaders });
        }

        const result = JSON.parse(row.result_json) as AnalysisResult;
        const overlay = generateAROverlay(result, image_width || 1920, image_height || 1080);

        return Response.json({ ok: true, overlay }, { headers: corsHeaders });
      }

      // Upload golden reference (staff only)
      if (path === "/golden/upload" && method === "POST") {
        // TODO: Auth check
        const formData = await request.formData();
        const imageFile = formData.get("image") as File;
        const boardId = formData.get("board_id") as string;

        if (!imageFile || !boardId) {
          return Response.json({ ok: false, error: "Missing image or board_id" }, { status: 400, headers: corsHeaders });
        }

        const key = `golden/${boardId}.jpg`;
        await env.GOLDEN_REFS.put(key, await imageFile.arrayBuffer(), {
          httpMetadata: { contentType: "image/jpeg" }
        });

        return Response.json({ ok: true, key }, { headers: corsHeaders });
      }

      // 404
      return Response.json({ ok: false, error: "Not found" }, { status: 404, headers: corsHeaders });

    } catch (err: any) {
      console.error("Vision worker error:", err);
      return Response.json(
        { ok: false, error: err.message || "Internal error" },
        { status: 500, headers: corsHeaders }
      );
    }
  }
};
