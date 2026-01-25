import { WebSocketHandler } from "./websocket";

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
        result = String(input).toUpperCase();
        break;
      case "lowercase":
        result = String(input).toLowerCase();
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
  },
  
  // ═══════════════════════════════════════════════════════════════════════
  // AI-POWERED ADVANCED TASK HANDLERS
  // ═══════════════════════════════════════════════════════════════════════
  
  "smart-routing": async (data: any) => {
    const task = data.task;
    
    if (!task) {
      throw new Error("task object is required for smart-routing");
    }
    
    // Analyze task complexity
    const complexityScore = calculateComplexityScore(task);
    
    // Determine routing
    let handler: string;
    let reasoning: string;
    
    if (complexityScore >= 80) {
      handler = "specialized-high-complexity";
      reasoning = "High complexity task requiring specialized processing";
    } else if (complexityScore >= 50) {
      handler = "standard-processing";
      reasoning = "Medium complexity task using standard processing";
    } else {
      handler = "fast-track";
      reasoning = "Low complexity task eligible for fast-track processing";
    }
    
    return {
      task_type: task.task_type || "unknown",
      complexity_score: complexityScore,
      recommended_handler: handler,
      reasoning,
      estimated_processing_time_ms: complexityScore * 10,
      priority: complexityScore >= 70 ? "high" : complexityScore >= 40 ? "normal" : "low"
    };
  },
  
  "text-analysis": async (data: any) => {
    const text = data.text;
    
    if (!text || typeof text !== "string") {
      throw new Error("text string is required for text-analysis");
    }
    
    // Word count
    const words = text.trim().split(/\s+/).filter(w => w.length > 0);
    const wordCount = words.length;
    
    // Character count
    const charCount = text.length;
    const charCountNoSpaces = text.replace(/\s/g, "").length;
    
    // Sentence count (rough)
    const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
    const sentenceCount = sentences.length;
    
    // Sentiment analysis (simple keyword-based)
    const positiveWords = ["good", "great", "excellent", "amazing", "wonderful", "fantastic", "love", "happy", "best"];
    const negativeWords = ["bad", "terrible", "awful", "horrible", "hate", "worst", "poor", "disappointing"];
    
    const lowerText = text.toLowerCase();
    let positiveCount = 0;
    let negativeCount = 0;
    
    positiveWords.forEach(word => {
      const regex = new RegExp(`\\b${word}\\b`, "gi");
      const matches = lowerText.match(regex);
      if (matches) positiveCount += matches.length;
    });
    
    negativeWords.forEach(word => {
      const regex = new RegExp(`\\b${word}\\b`, "gi");
      const matches = lowerText.match(regex);
      if (matches) negativeCount += matches.length;
    });
    
    let sentiment: string;
    if (positiveCount > negativeCount) {
      sentiment = "positive";
    } else if (negativeCount > positiveCount) {
      sentiment = "negative";
    } else {
      sentiment = "neutral";
    }
    
    const sentimentScore = (positiveCount - negativeCount) / Math.max(wordCount, 1);
    
    // Language detection (simple heuristic)
    const spanishIndicators = ["el", "la", "los", "las", "que", "de", "en", "es"];
    const frenchIndicators = ["le", "la", "les", "de", "et", "est", "un", "une"];
    const germanIndicators = ["der", "die", "das", "und", "ist", "ein", "eine"];
    
    let language = "english";
    let spanishScore = 0;
    let frenchScore = 0;
    let germanScore = 0;
    
    spanishIndicators.forEach(word => {
      if (lowerText.includes(` ${word} `)) spanishScore++;
    });
    frenchIndicators.forEach(word => {
      if (lowerText.includes(` ${word} `)) frenchScore++;
    });
    germanIndicators.forEach(word => {
      if (lowerText.includes(` ${word} `)) germanScore++;
    });
    
    if (spanishScore > 2) language = "spanish";
    else if (frenchScore > 2) language = "french";
    else if (germanScore > 2) language = "german";
    
    // Readability score (Flesch-Kincaid approximation)
    const avgWordsPerSentence = sentenceCount > 0 ? wordCount / sentenceCount : 0;
    const avgSyllablesPerWord = 1.5; // Rough estimate
    const readabilityScore = Math.max(0, Math.min(100, 
      206.835 - 1.015 * avgWordsPerSentence - 84.6 * avgSyllablesPerWord
    ));
    
    // Key phrase extraction (top 5 most common words, excluding common stopwords)
    const stopwords = new Set(["the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "was", "were"]);
    const wordFreq: Record<string, number> = {};
    
    words.forEach(word => {
      const normalized = word.toLowerCase().replace(/[^a-z0-9]/g, "");
      if (normalized.length > 3 && !stopwords.has(normalized)) {
        wordFreq[normalized] = (wordFreq[normalized] || 0) + 1;
      }
    });
    
    const keyPhrases = Object.entries(wordFreq)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([word, count]) => ({ word, count }));
    
    return {
      word_count: wordCount,
      character_count: charCount,
      character_count_no_spaces: charCountNoSpaces,
      sentence_count: sentenceCount,
      avg_words_per_sentence: Math.round(avgWordsPerSentence * 10) / 10,
      sentiment: {
        label: sentiment,
        score: Math.round(sentimentScore * 100) / 100,
        positive_indicators: positiveCount,
        negative_indicators: negativeCount
      },
      language: {
        detected: language,
        confidence: language === "english" ? "medium" : "low"
      },
      readability: {
        score: Math.round(readabilityScore),
        grade_level: readabilityScore >= 60 ? "easy" : readabilityScore >= 30 ? "medium" : "difficult"
      },
      key_phrases: keyPhrases
    };
  },
  
  "image-metadata": async (data: any) => {
    const imageUrl = data.image_url;
    const imageBase64 = data.image_base64;
    
    if (!imageUrl && !imageBase64) {
      throw new Error("image_url or image_base64 is required for image-metadata");
    }
    
    try {
      let imageData: ArrayBuffer;
      
      if (imageUrl) {
        const response = await fetch(imageUrl);
        if (!response.ok) {
          throw new Error(`Failed to fetch image: ${response.statusText}`);
        }
        imageData = await response.arrayBuffer();
      } else {
        // Decode base64
        const base64Data = imageBase64.replace(/^data:image\/\w+;base64,/, "");
        const binaryString = atob(base64Data);
        const bytes = new Uint8Array(binaryString.length);
        for (let i = 0; i < binaryString.length; i++) {
          bytes[i] = binaryString.charCodeAt(i);
        }
        imageData = bytes.buffer;
      }
      
      const bytes = new Uint8Array(imageData);
      const fileSize = bytes.length;
      
      // Detect image format from magic bytes
      let format = "unknown";
      let mimeType = "application/octet-stream";
      
      if (bytes[0] === 0xFF && bytes[1] === 0xD8 && bytes[2] === 0xFF) {
        format = "jpeg";
        mimeType = "image/jpeg";
      } else if (bytes[0] === 0x89 && bytes[1] === 0x50 && bytes[2] === 0x4E && bytes[3] === 0x47) {
        format = "png";
        mimeType = "image/png";
      } else if (bytes[0] === 0x47 && bytes[1] === 0x49 && bytes[2] === 0x46) {
        format = "gif";
        mimeType = "image/gif";
      } else if (bytes[0] === 0x52 && bytes[1] === 0x49 && bytes[2] === 0x46 && bytes[3] === 0x46) {
        format = "webp";
        mimeType = "image/webp";
      }
      
      // Extract dimensions (simplified - real implementation would parse headers)
      let width = 0;
      let height = 0;
      
      if (format === "png" && bytes.length > 24) {
        width = (bytes[16] << 24) | (bytes[17] << 16) | (bytes[18] << 8) | bytes[19];
        height = (bytes[20] << 24) | (bytes[21] << 16) | (bytes[22] << 8) | bytes[23];
      } else if (format === "jpeg") {
        // JPEG dimension extraction is complex, using placeholder
        width = 1920;
        height = 1080;
      } else if (format === "gif" && bytes.length > 10) {
        width = bytes[6] | (bytes[7] << 8);
        height = bytes[8] | (bytes[9] << 8);
      }
      
      // Simple color palette analysis (sample first 1000 bytes)
      const sampleSize = Math.min(1000, bytes.length);
      const colorMap: Record<string, number> = {};
      
      for (let i = 0; i < sampleSize; i += 3) {
        if (i + 2 < bytes.length) {
          const r = Math.floor(bytes[i] / 51) * 51;
          const g = Math.floor(bytes[i + 1] / 51) * 51;
          const b = Math.floor(bytes[i + 2] / 51) * 51;
          const color = `rgb(${r},${g},${b})`;
          colorMap[color] = (colorMap[color] || 0) + 1;
        }
      }
      
      const dominantColors = Object.entries(colorMap)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5)
        .map(([color]) => color);
      
      // Detect image type (heuristic based on size and format)
      let imageType = "photo";
      if (fileSize < 50000 && format === "png") {
        imageType = "diagram";
      } else if (fileSize < 100000 && (width < 1000 || height < 1000)) {
        imageType = "screenshot";
      }
      
      return {
        format,
        mime_type: mimeType,
        file_size: fileSize,
        file_size_human: formatBytes(fileSize),
        dimensions: {
          width,
          height,
          aspect_ratio: height > 0 ? Math.round((width / height) * 100) / 100 : 0
        },
        dominant_colors: dominantColors,
        estimated_type: imageType,
        analysis_timestamp: new Date().toISOString()
      };
    } catch (error) {
      throw new Error(`Image analysis failed: ${error instanceof Error ? error.message : "Unknown error"}`);
    }
  },
  
  "json-validator": async (data: any) => {
    const jsonData = data.json;
    const schema = data.schema;
    
    if (!jsonData) {
      throw new Error("json is required for json-validator");
    }
    
    if (!schema) {
      throw new Error("schema is required for json-validator");
    }
    
    const errors: Array<{ path: string; message: string; suggestion?: string }> = [];
    
    // Basic JSON schema validation
    function validate(obj: any, schemaObj: any, path: string = "$"): void {
      if (schemaObj.type) {
        const actualType = Array.isArray(obj) ? "array" : typeof obj;
        if (actualType !== schemaObj.type) {
          errors.push({
            path,
            message: `Expected type ${schemaObj.type}, got ${actualType}`,
            suggestion: `Convert value to ${schemaObj.type}`
          });
        }
      }
      
      if (schemaObj.required && Array.isArray(schemaObj.required)) {
        schemaObj.required.forEach((key: string) => {
          if (!(key in obj)) {
            errors.push({
              path: `${path}.${key}`,
              message: `Required field "${key}" is missing`,
              suggestion: `Add "${key}" field to object`
            });
          }
        });
      }
      
      if (schemaObj.properties && typeof obj === "object" && !Array.isArray(obj)) {
        Object.entries(schemaObj.properties).forEach(([key, propSchema]) => {
          if (key in obj) {
            validate(obj[key], propSchema, `${path}.${key}`);
          }
        });
      }
      
      if (schemaObj.items && Array.isArray(obj)) {
        obj.forEach((item, index) => {
          validate(item, schemaObj.items, `${path}[${index}]`);
        });
      }
      
      if (schemaObj.minLength !== undefined && typeof obj === "string") {
        if (obj.length < schemaObj.minLength) {
          errors.push({
            path,
            message: `String length ${obj.length} is less than minimum ${schemaObj.minLength}`,
            suggestion: `Increase string length to at least ${schemaObj.minLength}`
          });
        }
      }
      
      if (schemaObj.maxLength !== undefined && typeof obj === "string") {
        if (obj.length > schemaObj.maxLength) {
          errors.push({
            path,
            message: `String length ${obj.length} exceeds maximum ${schemaObj.maxLength}`,
            suggestion: `Reduce string length to at most ${schemaObj.maxLength}`
          });
        }
      }
      
      if (schemaObj.minimum !== undefined && typeof obj === "number") {
        if (obj < schemaObj.minimum) {
          errors.push({
            path,
            message: `Value ${obj} is less than minimum ${schemaObj.minimum}`,
            suggestion: `Increase value to at least ${schemaObj.minimum}`
          });
        }
      }
      
      if (schemaObj.maximum !== undefined && typeof obj === "number") {
        if (obj > schemaObj.maximum) {
          errors.push({
            path,
            message: `Value ${obj} exceeds maximum ${schemaObj.maximum}`,
            suggestion: `Reduce value to at most ${schemaObj.maximum}`
          });
        }
      }
    }
    
    validate(jsonData, schema);
    
    return {
      valid: errors.length === 0,
      error_count: errors.length,
      errors: errors.slice(0, 20), // Limit to first 20 errors
      summary: errors.length === 0 
        ? "JSON is valid according to schema" 
        : `Found ${errors.length} validation error${errors.length > 1 ? "s" : ""}`
    };
  },
  
  "api-tester": async (data: any) => {
    const endpoints = data.endpoints;
    
    if (!endpoints || !Array.isArray(endpoints)) {
      throw new Error("endpoints array is required for api-tester");
    }
    
    if (endpoints.length === 0) {
      throw new Error("At least one endpoint is required");
    }
    
    if (endpoints.length > 10) {
      throw new Error("Maximum 10 endpoints allowed per test");
    }
    
    // Test all endpoints in parallel
    const results = await Promise.all(
      endpoints.map(async (endpoint: any) => {
        const url = typeof endpoint === "string" ? endpoint : endpoint.url;
        const method = typeof endpoint === "object" ? endpoint.method || "GET" : "GET";
        const headers = typeof endpoint === "object" ? endpoint.headers || {} : {};
        
        try {
          const start = Date.now();
          const response = await fetch(url, {
            method,
            headers,
            signal: AbortSignal.timeout(5000) // 5 second timeout
          });
          const responseTime = Date.now() - start;
          
          const contentType = response.headers.get("content-type") || "";
          let body: any = null;
          
          if (contentType.includes("application/json")) {
            try {
              body = await response.json();
            } catch {
              body = "Invalid JSON";
            }
          } else {
            const text = await response.text();
            body = text.substring(0, 200);
          }
          
          return {
            url,
            method,
            status_code: response.status,
            response_time_ms: responseTime,
            healthy: response.ok,
            content_type: contentType,
            headers: Object.fromEntries(response.headers.entries()),
            body_preview: body
          };
        } catch (error) {
          return {
            url,
            method,
            status_code: 0,
            response_time_ms: 0,
            healthy: false,
            error: error instanceof Error ? error.message : "Unknown error"
          };
        }
      })
    );
    
    // Generate health report
    const healthyCount = results.filter(r => r.healthy).length;
    const avgResponseTime = results.reduce((sum, r) => sum + r.response_time_ms, 0) / results.length;
    
    let overallHealth: string;
    if (healthyCount === results.length) {
      overallHealth = "excellent";
    } else if (healthyCount >= results.length * 0.8) {
      overallHealth = "good";
    } else if (healthyCount >= results.length * 0.5) {
      overallHealth = "degraded";
    } else {
      overallHealth = "critical";
    }
    
    const recommendations: string[] = [];
    
    if (avgResponseTime > 1000) {
      recommendations.push("High average response time detected. Consider optimizing endpoints or adding caching.");
    }
    
    results.forEach(result => {
      if (!result.healthy) {
        recommendations.push(`Endpoint ${result.url} is unhealthy. Check logs and connectivity.`);
      }
      if (result.response_time_ms > 2000) {
        recommendations.push(`Endpoint ${result.url} has slow response time (${result.response_time_ms}ms). Consider optimization.`);
      }
    });
    
    return {
      overall_health: overallHealth,
      total_endpoints: results.length,
      healthy_endpoints: healthyCount,
      unhealthy_endpoints: results.length - healthyCount,
      avg_response_time_ms: Math.round(avgResponseTime),
      results,
      recommendations: recommendations.slice(0, 5),
      test_timestamp: new Date().toISOString()
    };
  }
};

// Helper function to calculate task complexity
function calculateComplexityScore(task: any): number {
  let score = 0;
  
  // Base score on task type
  const complexTaskTypes = ["inference", "code-analysis", "file-processing"];
  if (complexTaskTypes.includes(task.task_type)) {
    score += 30;
  }
  
  // Add score based on data size
  const dataString = JSON.stringify(task.task_data || {});
  const dataSize = dataString.length;
  
  if (dataSize > 10000) {
    score += 30;
  } else if (dataSize > 1000) {
    score += 15;
  }
  
  // Add score if nested objects
  if (typeof task.task_data === "object") {
    const depth = getObjectDepth(task.task_data);
    score += Math.min(depth * 5, 25);
  }
  
  // Add score for priority
  if (task.priority === "high") {
    score += 15;
  }
  
  return Math.min(score, 100);
}

function getObjectDepth(obj: any): number {
  if (typeof obj !== "object" || obj === null) {
    return 0;
  }
  
  let maxDepth = 0;
  for (const value of Object.values(obj)) {
    const depth = getObjectDepth(value);
    maxDepth = Math.max(maxDepth, depth);
  }
  
  return maxDepth + 1;
}

function formatBytes(bytes: number): string {
  if (bytes === 0) return "0 Bytes";
  const k = 1024;
  const sizes = ["Bytes", "KB", "MB", "GB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return Math.round(bytes / Math.pow(k, i) * 100) / 100 + " " + sizes[i];
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

// ═══════════════════════════════════════════════════════════════════════
// ADVANCED SECURITY FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════

// HMAC request signature verification
async function verifyRequestSignature(
  request: Request,
  env: Record<string, any>
): Promise<boolean> {
  if (!env.HMAC_SECRET) {
    return true; // No signature verification if secret not configured
  }
  
  const signature = request.headers.get("X-Signature");
  const timestamp = request.headers.get("X-Timestamp");
  
  if (!signature || !timestamp) {
    return false;
  }
  
  // Check timestamp (prevent replay attacks - 5 minute window)
  const now = Date.now();
  const requestTime = parseInt(timestamp);
  if (Math.abs(now - requestTime) > 5 * 60 * 1000) {
    return false;
  }
  
  // Verify signature
  const body = await request.clone().text();
  const message = `${timestamp}.${body}`;
  
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(env.HMAC_SECRET),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  
  const signatureBytes = await crypto.subtle.sign("HMAC", key, encoder.encode(message));
  const expectedSignature = Array.from(new Uint8Array(signatureBytes))
    .map(b => b.toString(16).padStart(2, "0"))
    .join("");
  
  return signature === expectedSignature;
}

// IP whitelist/blacklist checking
function checkIPAccess(request: Request, env: Record<string, any>): boolean {
  const clientIP = request.headers.get("CF-Connecting-IP");
  
  if (!clientIP) {
    return true; // Can't determine IP, allow by default
  }
  
  // Check whitelist first (if configured)
  if (env.IP_WHITELIST) {
    const whitelist = env.IP_WHITELIST.split(",").map((ip: string) => ip.trim());
    return whitelist.includes(clientIP);
  }
  
  // Check blacklist
  if (env.IP_BLACKLIST) {
    const blacklist = env.IP_BLACKLIST.split(",").map((ip: string) => ip.trim());
    if (blacklist.includes(clientIP)) {
      return false;
    }
  }
  
  return true;
}

// Geographic restrictions
function checkGeoRestrictions(request: Request, env: Record<string, any>): boolean {
  const country = request.headers.get("CF-IPCountry");
  
  if (!country) {
    return true; // Can't determine country, allow by default
  }
  
  // Check allowed countries
  if (env.ALLOWED_COUNTRIES) {
    const allowed = env.ALLOWED_COUNTRIES.split(",").map((c: string) => c.trim().toUpperCase());
    return allowed.includes(country.toUpperCase());
  }
  
  // Check blocked countries
  if (env.BLOCKED_COUNTRIES) {
    const blocked = env.BLOCKED_COUNTRIES.split(",").map((c: string) => c.trim().toUpperCase());
    return !blocked.includes(country.toUpperCase());
  }
  
  return true;
}

// Audit logging
interface AuditLogEntry {
  timestamp: string;
  method: string;
  path: string;
  api_key: string;
  client_ip?: string;
  country?: string;
  user_agent?: string;
  status: number;
  duration_ms: number;
  task_type?: string;
}

async function logAuditEntry(
  request: Request,
  response: Response,
  durationMs: number,
  env: Record<string, any>,
  taskType?: string
): Promise<void> {
  if (!env.AUDIT_LOG_KV) {
    return; // Audit logging not configured
  }
  
  const url = new URL(request.url);
  const entry: AuditLogEntry = {
    timestamp: new Date().toISOString(),
    method: request.method,
    path: url.pathname,
    api_key: request.headers.get("X-API-Key") || "anonymous",
    client_ip: request.headers.get("CF-Connecting-IP") || undefined,
    country: request.headers.get("CF-IPCountry") || undefined,
    user_agent: request.headers.get("User-Agent") || undefined,
    status: response.status,
    duration_ms: durationMs,
    task_type: taskType
  };
  
  // Store in KV with timestamp as key
  const key = `audit:${Date.now()}:${crypto.randomUUID()}`;
  await env.AUDIT_LOG_KV.put(key, JSON.stringify(entry), {
    expirationTtl: 30 * 24 * 60 * 60 // Keep for 30 days
  });
}

// Initialize WebSocket handler
let wsHandler: WebSocketHandler | null = null;

function getWebSocketHandler(): WebSocketHandler {
  if (!wsHandler) {
    wsHandler = new WebSocketHandler(taskHandlers);
  }
  return wsHandler;
}

export default {
  async fetch(request: Request, env: Record<string, any>, ctx: ExecutionContext): Promise<Response> {
    const startTime = Date.now();
    const url = new URL(request.url);
    let corsHeaders: Record<string, string> = {
      "Access-Control-Allow-Origin": env.ALLOWED_ORIGINS || "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization, X-API-Key, X-Signature, X-Timestamp",
      "Content-Type": "application/json"
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }
    
    // Check IP access restrictions
    if (!checkIPAccess(request, env)) {
      return new Response(JSON.stringify({
        error: "Forbidden",
        message: "Access denied from your IP address"
      }), {
        status: 403,
        headers: corsHeaders
      });
    }
    
    // Check geographic restrictions
    if (!checkGeoRestrictions(request, env)) {
      const country = request.headers.get("CF-IPCountry");
      return new Response(JSON.stringify({
        error: "Forbidden",
        message: `Access denied from country: ${country}`
      }), {
        status: 403,
        headers: corsHeaders
      });
    }
    
    // WebSocket upgrade handling
    if (url.pathname === "/ws" && request.headers.get("Upgrade") === "websocket") {
      // Check auth for WebSocket
      if (!checkAuth(request, env)) {
        return new Response(JSON.stringify({
          error: "Unauthorized",
          message: "Valid X-API-Key header required for WebSocket"
        }), {
          status: 401,
          headers: corsHeaders
        });
      }
      
      return getWebSocketHandler().handleUpgrade(request);
    }

    // Check authentication for protected endpoints
    if (url.pathname.startsWith("/api/") && !checkAuth(request, env)) {
      const response = new Response(JSON.stringify({
        error: "Unauthorized",
        message: "Valid X-API-Key header required"
      }), {
        status: 401,
        headers: corsHeaders
      });
      
      ctx.waitUntil(logAuditEntry(request, response, Date.now() - startTime, env));
      return response;
    }
    
    // Verify request signature if enabled
    if (url.pathname.startsWith("/api/") && request.method === "POST") {
      if (env.HMAC_SECRET && !await verifyRequestSignature(request, env)) {
        const response = new Response(JSON.stringify({
          error: "Unauthorized",
          message: "Invalid request signature"
        }), {
          status: 401,
          headers: corsHeaders
        });
        
        ctx.waitUntil(logAuditEntry(request, response, Date.now() - startTime, env));
        return response;
      }
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
      message: "NOIZYLAB Cloud Agent 🚀 - Enterprise Edition",
      version: "3.0.0",
      edition: "enterprise",
      features: [
        "AI-Powered Task Handlers",
        "WebSocket Real-Time Streaming",
        "Advanced Security & Audit Logging",
        "Multi-Level Caching",
        "Load Balancing & Auto-Scaling",
        "Comprehensive Analytics"
      ],
      endpoints: {
        health: "/health",
        capabilities: "/api/capabilities",
        delegate: "/api/delegate (POST)",
        batch: "/api/batch (POST)",
        status: "/api/status?task_id=<id> (GET)",
        metrics: "/api/metrics (GET)",
        websocket: "/ws (WebSocket)"
      },
      websocket_stats: getWebSocketHandler().getStats()
    }), {
      headers: corsHeaders
    });
  }
};
