/**
 * ████ NOIZYLAB AR GUIDE WORKER ████
 * 
 * AUGMENTED REALITY REPAIR GUIDANCE
 * - 3D component highlighting
 * - Step-by-step animated guides
 * - Real-time overlay instructions
 * - Voice-guided repairs
 * - Live annotation sharing
 * - AI-powered next step prediction
 */

export interface Env {
  DB: D1Database;
  GUIDES_STORAGE: R2Bucket;
  AI: Ai;
  BRAIN: Fetcher;
  VOICE: Fetcher;
}

interface RepairGuide {
  id: string;
  device_type: string;
  device_model: string;
  repair_type: string;
  difficulty: 'easy' | 'medium' | 'hard' | 'expert';
  estimated_time_minutes: number;
  tools_required: string[];
  parts_required: string[];
  steps: RepairStep[];
  safety_warnings: string[];
  created_by: string;
  approved: boolean;
  views: number;
  success_rate: number;
}

interface RepairStep {
  number: number;
  title: string;
  description: string;
  voice_narration?: string;
  ar_annotations: ARAnnotation[];
  image_url?: string;
  video_url?: string;
  duration_seconds: number;
  safety_critical: boolean;
  common_mistakes: string[];
  checkpoints: string[];
}

interface ARAnnotation {
  id: string;
  type: 'highlight' | 'arrow' | 'circle' | 'text' | 'animation' | '3d_model';
  position: { x: number; y: number; z?: number };
  size?: { width: number; height: number };
  color?: string;
  content?: string;
  animation?: 'pulse' | 'bounce' | 'rotate' | 'fade';
  duration_ms?: number;
  linked_component?: string;
}

interface ARSession {
  id: string;
  user_id: string;
  guide_id: string;
  current_step: number;
  started_at: string;
  last_activity: string;
  completed_steps: number[];
  notes: string[];
  photos_taken: string[];
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;

    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        },
      });
    }

    try {
      // === GUIDE MANAGEMENT ===
      if (path === '/guides' && request.method === 'GET') {
        return this.listGuides(url, env);
      }

      if (path === '/guides' && request.method === 'POST') {
        return this.createGuide(request, env);
      }

      if (path.match(/^\/guides\/[^/]+$/) && request.method === 'GET') {
        const guideId = path.split('/')[2];
        return this.getGuide(guideId, env);
      }

      if (path.match(/^\/guides\/[^/]+$/) && request.method === 'PUT') {
        const guideId = path.split('/')[2];
        return this.updateGuide(guideId, request, env);
      }

      // === AI GUIDE GENERATION ===
      if (path === '/guides/generate' && request.method === 'POST') {
        return this.generateGuide(request, env);
      }

      if (path === '/guides/generate-from-image' && request.method === 'POST') {
        return this.generateFromImage(request, env);
      }

      // === AR SESSIONS ===
      if (path === '/sessions/start' && request.method === 'POST') {
        return this.startSession(request, env);
      }

      if (path.match(/^\/sessions\/[^/]+\/step$/) && request.method === 'POST') {
        const sessionId = path.split('/')[2];
        return this.navigateStep(sessionId, request, env);
      }

      if (path.match(/^\/sessions\/[^/]+\/complete$/) && request.method === 'POST') {
        const sessionId = path.split('/')[2];
        return this.completeStep(sessionId, request, env);
      }

      if (path.match(/^\/sessions\/[^/]+\/note$/) && request.method === 'POST') {
        const sessionId = path.split('/')[2];
        return this.addNote(sessionId, request, env);
      }

      if (path.match(/^\/sessions\/[^/]+\/photo$/) && request.method === 'POST') {
        const sessionId = path.split('/')[2];
        return this.capturePhoto(sessionId, request, env);
      }

      if (path.match(/^\/sessions\/[^/]+$/) && request.method === 'GET') {
        const sessionId = path.split('/')[2];
        return this.getSession(sessionId, env);
      }

      // === AR OVERLAYS ===
      if (path === '/ar/calibrate' && request.method === 'POST') {
        return this.calibrateAR(request, env);
      }

      if (path === '/ar/detect-components' && request.method === 'POST') {
        return this.detectComponents(request, env);
      }

      if (path === '/ar/overlay-data' && request.method === 'POST') {
        return this.getOverlayData(request, env);
      }

      // === VOICE NARRATION ===
      if (path.match(/^\/guides\/[^/]+\/narration\/[^/]+$/) && request.method === 'GET') {
        const guideId = path.split('/')[2];
        const stepNumber = parseInt(path.split('/')[4]);
        return this.getNarration(guideId, stepNumber, env);
      }

      // === COLLABORATION ===
      if (path === '/share/live' && request.method === 'POST') {
        return this.startLiveShare(request, env);
      }

      if (path.match(/^\/share\/[^/]+\/annotate$/) && request.method === 'POST') {
        const shareId = path.split('/')[2];
        return this.addLiveAnnotation(shareId, request, env);
      }

      // === SEARCH ===
      if (path === '/search' && request.method === 'GET') {
        return this.searchGuides(url, env);
      }

      if (path === '/suggest' && request.method === 'POST') {
        return this.suggestGuide(request, env);
      }

      return this.jsonResponse({ error: 'Not found' }, 404);
    } catch (error) {
      console.error('AR Guide error:', error);
      return this.jsonResponse({ error: 'Internal error' }, 500);
    }
  },

  // === GUIDE MANAGEMENT ===
  async listGuides(url: URL, env: Env): Promise<Response> {
    const deviceType = url.searchParams.get('device_type');
    const deviceModel = url.searchParams.get('device_model');
    const repairType = url.searchParams.get('repair_type');
    const difficulty = url.searchParams.get('difficulty');

    let query = 'SELECT * FROM repair_guides WHERE approved = 1';
    const params: any[] = [];

    if (deviceType) {
      query += ' AND device_type = ?';
      params.push(deviceType);
    }
    if (deviceModel) {
      query += ' AND device_model LIKE ?';
      params.push(`%${deviceModel}%`);
    }
    if (repairType) {
      query += ' AND repair_type = ?';
      params.push(repairType);
    }
    if (difficulty) {
      query += ' AND difficulty = ?';
      params.push(difficulty);
    }

    query += ' ORDER BY views DESC, success_rate DESC';

    const result = await env.DB.prepare(query).bind(...params).all();

    return this.jsonResponse({
      guides: result.results,
      total: result.results?.length || 0,
    });
  },

  async createGuide(request: Request, env: Env): Promise<Response> {
    const data = await request.json() as Partial<RepairGuide>;
    const guideId = crypto.randomUUID();

    await env.DB.prepare(`
      INSERT INTO repair_guides (
        id, device_type, device_model, repair_type, difficulty,
        estimated_time_minutes, tools_required, parts_required,
        steps, safety_warnings, created_by, approved, views, success_rate,
        created_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0, 0, datetime('now'))
    `).bind(
      guideId,
      data.device_type,
      data.device_model,
      data.repair_type,
      data.difficulty || 'medium',
      data.estimated_time_minutes || 30,
      JSON.stringify(data.tools_required || []),
      JSON.stringify(data.parts_required || []),
      JSON.stringify(data.steps || []),
      JSON.stringify(data.safety_warnings || []),
      data.created_by || 'system'
    ).run();

    return this.jsonResponse({ id: guideId, message: 'Guide created' });
  },

  async getGuide(guideId: string, env: Env): Promise<Response> {
    const guide = await env.DB.prepare(
      'SELECT * FROM repair_guides WHERE id = ?'
    ).bind(guideId).first() as any;

    if (!guide) {
      return this.jsonResponse({ error: 'Guide not found' }, 404);
    }

    // Increment views
    await env.DB.prepare(
      'UPDATE repair_guides SET views = views + 1 WHERE id = ?'
    ).bind(guideId).run();

    return this.jsonResponse({
      ...guide,
      tools_required: JSON.parse(guide.tools_required || '[]'),
      parts_required: JSON.parse(guide.parts_required || '[]'),
      steps: JSON.parse(guide.steps || '[]'),
      safety_warnings: JSON.parse(guide.safety_warnings || '[]'),
    });
  },

  async updateGuide(guideId: string, request: Request, env: Env): Promise<Response> {
    const data = await request.json() as Partial<RepairGuide>;

    await env.DB.prepare(`
      UPDATE repair_guides SET
        device_type = COALESCE(?, device_type),
        device_model = COALESCE(?, device_model),
        repair_type = COALESCE(?, repair_type),
        difficulty = COALESCE(?, difficulty),
        estimated_time_minutes = COALESCE(?, estimated_time_minutes),
        tools_required = COALESCE(?, tools_required),
        parts_required = COALESCE(?, parts_required),
        steps = COALESCE(?, steps),
        safety_warnings = COALESCE(?, safety_warnings),
        approved = COALESCE(?, approved),
        updated_at = datetime('now')
      WHERE id = ?
    `).bind(
      data.device_type || null,
      data.device_model || null,
      data.repair_type || null,
      data.difficulty || null,
      data.estimated_time_minutes || null,
      data.tools_required ? JSON.stringify(data.tools_required) : null,
      data.parts_required ? JSON.stringify(data.parts_required) : null,
      data.steps ? JSON.stringify(data.steps) : null,
      data.safety_warnings ? JSON.stringify(data.safety_warnings) : null,
      data.approved !== undefined ? (data.approved ? 1 : 0) : null,
      guideId
    ).run();

    return this.jsonResponse({ message: 'Guide updated' });
  },

  // === AI GUIDE GENERATION ===
  async generateGuide(request: Request, env: Env): Promise<Response> {
    const { device_type, device_model, repair_type, complexity } = await request.json() as any;

    // Use Claude for detailed guide generation
    const brainResponse = await env.BRAIN.fetch('https://brain/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        type: 'generate_guide',
        context: {
          device_type,
          device_model,
          repair_type,
          complexity,
        },
      }),
    });

    if (!brainResponse.ok) {
      // Fallback to Workers AI
      const aiResult = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
        messages: [{
          role: 'system',
          content: `You are an expert hardware repair guide creator. Generate detailed step-by-step repair guides with AR annotation suggestions.`
        }, {
          role: 'user',
          content: `Create a repair guide for: ${device_type} ${device_model} - ${repair_type}
          
          Return JSON:
          {
            "title": "",
            "difficulty": "easy|medium|hard|expert",
            "estimated_time_minutes": number,
            "tools_required": [],
            "parts_required": [],
            "safety_warnings": [],
            "steps": [
              {
                "number": 1,
                "title": "",
                "description": "",
                "voice_narration": "",
                "duration_seconds": number,
                "safety_critical": boolean,
                "common_mistakes": [],
                "checkpoints": [],
                "ar_annotations": [
                  {
                    "type": "highlight|arrow|circle|text",
                    "position": { "x": 0.5, "y": 0.5 },
                    "content": "",
                    "color": "#FF0000"
                  }
                ]
              }
            ]
          }`
        }],
      });

      return this.jsonResponse({
        generated: true,
        source: 'workers_ai',
        guide: aiResult,
      });
    }

    const brainGuide = await brainResponse.json();
    return this.jsonResponse({
      generated: true,
      source: 'brain_worker',
      guide: brainGuide,
    });
  },

  async generateFromImage(request: Request, env: Env): Promise<Response> {
    const formData = await request.formData();
    const image = formData.get('image') as File;
    const deviceInfo = formData.get('device_info') as string;

    if (!image) {
      return this.jsonResponse({ error: 'No image provided' }, 400);
    }

    const imageData = await image.arrayBuffer();

    // Use vision model to analyze device and suggest repair
    const visionResult = await env.AI.run('@cf/llava-hf/llava-1.5-7b-hf', {
      image: [...new Uint8Array(imageData)],
      prompt: `Analyze this device image. Identify:
      1. What device is this?
      2. What components are visible?
      3. Is there any visible damage?
      4. What repairs might be needed?
      5. Suggest AR annotation points for repair guidance.
      
      Additional context: ${deviceInfo || 'none'}`,
      max_tokens: 1000,
    });

    // Store image for reference
    const imageKey = `guide-generation/${Date.now()}-${image.name}`;
    await env.GUIDES_STORAGE.put(imageKey, imageData);

    return this.jsonResponse({
      analysis: visionResult,
      image_reference: imageKey,
      suggested_repairs: this.extractSuggestedRepairs(visionResult),
    });
  },

  extractSuggestedRepairs(visionResult: any): string[] {
    // Parse vision result for repair suggestions
    const description = (visionResult as any)?.response || '';
    const repairs: string[] = [];
    
    if (description.toLowerCase().includes('crack')) repairs.push('Screen replacement');
    if (description.toLowerCase().includes('battery')) repairs.push('Battery replacement');
    if (description.toLowerCase().includes('port')) repairs.push('Port repair');
    if (description.toLowerCase().includes('button')) repairs.push('Button replacement');
    
    return repairs;
  },

  // === AR SESSIONS ===
  async startSession(request: Request, env: Env): Promise<Response> {
    const { guide_id, user_id } = await request.json() as any;

    // Verify guide exists
    const guide = await env.DB.prepare(
      'SELECT * FROM repair_guides WHERE id = ?'
    ).bind(guide_id).first() as any;

    if (!guide) {
      return this.jsonResponse({ error: 'Guide not found' }, 404);
    }

    const sessionId = crypto.randomUUID();

    await env.DB.prepare(`
      INSERT INTO ar_sessions (
        id, user_id, guide_id, current_step, started_at, last_activity,
        completed_steps, notes, photos_taken
      ) VALUES (?, ?, ?, 1, datetime('now'), datetime('now'), '[]', '[]', '[]')
    `).bind(sessionId, user_id, guide_id).run();

    const steps = JSON.parse(guide.steps || '[]');
    const firstStep = steps[0] || null;

    return this.jsonResponse({
      session_id: sessionId,
      guide: {
        ...guide,
        tools_required: JSON.parse(guide.tools_required || '[]'),
        parts_required: JSON.parse(guide.parts_required || '[]'),
        safety_warnings: JSON.parse(guide.safety_warnings || '[]'),
        steps,
      },
      current_step: firstStep,
      total_steps: steps.length,
    });
  },

  async navigateStep(sessionId: string, request: Request, env: Env): Promise<Response> {
    const { direction, step_number } = await request.json() as any;

    const session = await env.DB.prepare(
      'SELECT * FROM ar_sessions WHERE id = ?'
    ).bind(sessionId).first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found' }, 404);
    }

    const guide = await env.DB.prepare(
      'SELECT steps FROM repair_guides WHERE id = ?'
    ).bind(session.guide_id).first() as any;

    const steps = JSON.parse(guide?.steps || '[]');

    let newStep = session.current_step;
    if (step_number !== undefined) {
      newStep = step_number;
    } else if (direction === 'next') {
      newStep = Math.min(session.current_step + 1, steps.length);
    } else if (direction === 'prev') {
      newStep = Math.max(session.current_step - 1, 1);
    }

    await env.DB.prepare(`
      UPDATE ar_sessions SET 
        current_step = ?, 
        last_activity = datetime('now')
      WHERE id = ?
    `).bind(newStep, sessionId).run();

    const currentStepData = steps[newStep - 1] || null;

    return this.jsonResponse({
      session_id: sessionId,
      current_step: newStep,
      total_steps: steps.length,
      step_data: currentStepData,
      progress_percent: Math.round((newStep / steps.length) * 100),
    });
  },

  async completeStep(sessionId: string, request: Request, env: Env): Promise<Response> {
    const { step_number, verification_photo } = await request.json() as any;

    const session = await env.DB.prepare(
      'SELECT * FROM ar_sessions WHERE id = ?'
    ).bind(sessionId).first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found' }, 404);
    }

    const completedSteps = JSON.parse(session.completed_steps || '[]');
    if (!completedSteps.includes(step_number)) {
      completedSteps.push(step_number);
    }

    await env.DB.prepare(`
      UPDATE ar_sessions SET 
        completed_steps = ?,
        last_activity = datetime('now')
      WHERE id = ?
    `).bind(JSON.stringify(completedSteps), sessionId).run();

    // Get guide info
    const guide = await env.DB.prepare(
      'SELECT steps FROM repair_guides WHERE id = ?'
    ).bind(session.guide_id).first() as any;

    const steps = JSON.parse(guide?.steps || '[]');
    const isComplete = completedSteps.length >= steps.length;

    if (isComplete) {
      // Update guide success rate
      await env.DB.prepare(`
        UPDATE repair_guides SET 
          success_rate = ((success_rate * views) + 100) / (views + 1)
        WHERE id = ?
      `).bind(session.guide_id).run();
    }

    return this.jsonResponse({
      step_completed: step_number,
      completed_steps: completedSteps,
      total_steps: steps.length,
      progress_percent: Math.round((completedSteps.length / steps.length) * 100),
      repair_complete: isComplete,
    });
  },

  async addNote(sessionId: string, request: Request, env: Env): Promise<Response> {
    const { note, step_number } = await request.json() as any;

    const session = await env.DB.prepare(
      'SELECT notes FROM ar_sessions WHERE id = ?'
    ).bind(sessionId).first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found' }, 404);
    }

    const notes = JSON.parse(session.notes || '[]');
    notes.push({
      id: crypto.randomUUID(),
      step_number,
      note,
      timestamp: new Date().toISOString(),
    });

    await env.DB.prepare(`
      UPDATE ar_sessions SET 
        notes = ?,
        last_activity = datetime('now')
      WHERE id = ?
    `).bind(JSON.stringify(notes), sessionId).run();

    return this.jsonResponse({ message: 'Note added', notes });
  },

  async capturePhoto(sessionId: string, request: Request, env: Env): Promise<Response> {
    const formData = await request.formData();
    const photo = formData.get('photo') as File;
    const stepNumber = formData.get('step_number') as string;

    if (!photo) {
      return this.jsonResponse({ error: 'No photo provided' }, 400);
    }

    const session = await env.DB.prepare(
      'SELECT photos_taken FROM ar_sessions WHERE id = ?'
    ).bind(sessionId).first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found' }, 404);
    }

    // Store photo
    const photoKey = `sessions/${sessionId}/step-${stepNumber}-${Date.now()}.jpg`;
    await env.GUIDES_STORAGE.put(photoKey, await photo.arrayBuffer());

    const photos = JSON.parse(session.photos_taken || '[]');
    photos.push({
      key: photoKey,
      step_number: parseInt(stepNumber),
      timestamp: new Date().toISOString(),
    });

    await env.DB.prepare(`
      UPDATE ar_sessions SET 
        photos_taken = ?,
        last_activity = datetime('now')
      WHERE id = ?
    `).bind(JSON.stringify(photos), sessionId).run();

    return this.jsonResponse({ message: 'Photo captured', photo_key: photoKey });
  },

  async getSession(sessionId: string, env: Env): Promise<Response> {
    const session = await env.DB.prepare(
      'SELECT * FROM ar_sessions WHERE id = ?'
    ).bind(sessionId).first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found' }, 404);
    }

    const guide = await env.DB.prepare(
      'SELECT * FROM repair_guides WHERE id = ?'
    ).bind(session.guide_id).first() as any;

    const steps = JSON.parse(guide?.steps || '[]');

    return this.jsonResponse({
      ...session,
      completed_steps: JSON.parse(session.completed_steps || '[]'),
      notes: JSON.parse(session.notes || '[]'),
      photos_taken: JSON.parse(session.photos_taken || '[]'),
      guide_info: {
        title: guide?.title,
        device: `${guide?.device_type} ${guide?.device_model}`,
        repair_type: guide?.repair_type,
      },
      current_step_data: steps[session.current_step - 1],
      total_steps: steps.length,
    });
  },

  // === AR OVERLAYS ===
  async calibrateAR(request: Request, env: Env): Promise<Response> {
    const formData = await request.formData();
    const calibrationImage = formData.get('image') as File;
    const deviceModel = formData.get('device_model') as string;

    if (!calibrationImage) {
      return this.jsonResponse({ error: 'Calibration image required' }, 400);
    }

    const imageData = await calibrationImage.arrayBuffer();

    // Analyze device orientation and scale
    const calibration = await env.AI.run('@cf/llava-hf/llava-1.5-7b-hf', {
      image: [...new Uint8Array(imageData)],
      prompt: `Analyze this device image for AR calibration:
      1. Identify the device orientation (portrait/landscape)
      2. Estimate the device dimensions
      3. Identify key reference points (corners, buttons, ports)
      4. Return calibration data for AR overlay alignment.
      
      Device model: ${deviceModel}`,
      max_tokens: 500,
    });

    return this.jsonResponse({
      calibrated: true,
      device_model: deviceModel,
      calibration_data: {
        orientation: 'landscape', // Would be extracted from AI response
        scale_factor: 1.0,
        reference_points: [
          { name: 'top_left', x: 0, y: 0 },
          { name: 'top_right', x: 1, y: 0 },
          { name: 'bottom_left', x: 0, y: 1 },
          { name: 'bottom_right', x: 1, y: 1 },
        ],
        analysis: calibration,
      },
    });
  },

  async detectComponents(request: Request, env: Env): Promise<Response> {
    const formData = await request.formData();
    const image = formData.get('image') as File;
    const deviceModel = formData.get('device_model') as string;

    if (!image) {
      return this.jsonResponse({ error: 'Image required' }, 400);
    }

    const imageData = await image.arrayBuffer();

    // Detect components using vision AI
    const detection = await env.AI.run('@cf/llava-hf/llava-1.5-7b-hf', {
      image: [...new Uint8Array(imageData)],
      prompt: `Identify all visible electronic components in this ${deviceModel || 'device'} image:
      For each component, provide:
      - Name/type
      - Approximate position (x, y as percentage 0-1)
      - Size (small/medium/large)
      - Condition (good/damaged/unknown)
      
      Format as JSON array.`,
      max_tokens: 1000,
    });

    return this.jsonResponse({
      device_model: deviceModel,
      components_detected: detection,
      ar_highlights: this.generateComponentHighlights(detection),
    });
  },

  generateComponentHighlights(detection: any): ARAnnotation[] {
    // Generate AR annotations for detected components
    // This would parse the AI response and create proper annotations
    return [
      {
        id: 'comp_1',
        type: 'highlight',
        position: { x: 0.5, y: 0.3 },
        size: { width: 0.1, height: 0.05 },
        color: '#00FF00',
        content: 'Main Processor',
        animation: 'pulse',
      },
      {
        id: 'comp_2',
        type: 'circle',
        position: { x: 0.2, y: 0.6 },
        size: { width: 0.08, height: 0.08 },
        color: '#FF0000',
        content: 'Battery Connector',
        animation: 'fade',
      },
    ];
  },

  async getOverlayData(request: Request, env: Env): Promise<Response> {
    const { guide_id, step_number, device_position } = await request.json() as any;

    const guide = await env.DB.prepare(
      'SELECT steps FROM repair_guides WHERE id = ?'
    ).bind(guide_id).first() as any;

    if (!guide) {
      return this.jsonResponse({ error: 'Guide not found' }, 404);
    }

    const steps = JSON.parse(guide.steps || '[]');
    const step = steps[step_number - 1];

    if (!step) {
      return this.jsonResponse({ error: 'Step not found' }, 404);
    }

    // Adjust annotations based on device position/orientation
    const adjustedAnnotations = (step.ar_annotations || []).map((ann: ARAnnotation) => ({
      ...ann,
      // In real implementation, adjust positions based on device_position
      adjusted_position: this.adjustPositionForDevice(ann.position, device_position),
    }));

    return this.jsonResponse({
      step_number,
      step_title: step.title,
      annotations: adjustedAnnotations,
      voice_narration_url: step.voice_narration ? `/guides/${guide_id}/narration/${step_number}` : null,
      checkpoints: step.checkpoints || [],
      warnings: step.safety_critical ? step.common_mistakes : [],
    });
  },

  adjustPositionForDevice(position: any, devicePosition: any): any {
    // Apply transformation based on device orientation/position
    // Simplified - would use proper matrix transformation in production
    return {
      x: position.x + (devicePosition?.offset_x || 0),
      y: position.y + (devicePosition?.offset_y || 0),
      z: position.z || 0,
    };
  },

  // === VOICE NARRATION ===
  async getNarration(guideId: string, stepNumber: number, env: Env): Promise<Response> {
    const guide = await env.DB.prepare(
      'SELECT steps FROM repair_guides WHERE id = ?'
    ).bind(guideId).first() as any;

    if (!guide) {
      return this.jsonResponse({ error: 'Guide not found' }, 404);
    }

    const steps = JSON.parse(guide.steps || '[]');
    const step = steps[stepNumber - 1];

    if (!step || !step.voice_narration) {
      return this.jsonResponse({ error: 'No narration for this step' }, 404);
    }

    // Check cache first
    const cacheKey = `narration/${guideId}/${stepNumber}`;
    const cached = await env.GUIDES_STORAGE.get(cacheKey);

    if (cached) {
      return new Response(cached.body, {
        headers: {
          'Content-Type': 'audio/mpeg',
          'Cache-Control': 'public, max-age=86400',
        },
      });
    }

    // Generate via Voice Worker
    const voiceResponse = await env.VOICE.fetch('https://voice/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: step.voice_narration,
        voice_id: 'repair_guide_voice',
        emotion: 'calm_instructional',
      }),
    });

    if (voiceResponse.ok) {
      const audio = await voiceResponse.arrayBuffer();
      // Cache the audio
      await env.GUIDES_STORAGE.put(cacheKey, audio);
      
      return new Response(audio, {
        headers: {
          'Content-Type': 'audio/mpeg',
          'Cache-Control': 'public, max-age=86400',
        },
      });
    }

    return this.jsonResponse({ error: 'Failed to generate narration' }, 500);
  },

  // === COLLABORATION ===
  async startLiveShare(request: Request, env: Env): Promise<Response> {
    const { session_id, user_id } = await request.json() as any;
    const shareId = crypto.randomUUID().substring(0, 8).toUpperCase();

    await env.DB.prepare(`
      INSERT INTO live_shares (
        id, session_id, created_by, created_at, active, annotations
      ) VALUES (?, ?, ?, datetime('now'), 1, '[]')
    `).bind(shareId, session_id, user_id).run();

    return this.jsonResponse({
      share_id: shareId,
      share_url: `https://ar.noizylab.com/share/${shareId}`,
      expires_in: '2 hours',
    });
  },

  async addLiveAnnotation(shareId: string, request: Request, env: Env): Promise<Response> {
    const annotation = await request.json() as ARAnnotation;

    const share = await env.DB.prepare(
      'SELECT annotations FROM live_shares WHERE id = ? AND active = 1'
    ).bind(shareId).first() as any;

    if (!share) {
      return this.jsonResponse({ error: 'Share not found or expired' }, 404);
    }

    const annotations = JSON.parse(share.annotations || '[]');
    annotations.push({
      ...annotation,
      id: crypto.randomUUID(),
      timestamp: Date.now(),
    });

    await env.DB.prepare(`
      UPDATE live_shares SET annotations = ? WHERE id = ?
    `).bind(JSON.stringify(annotations), shareId).run();

    return this.jsonResponse({ message: 'Annotation added', annotations });
  },

  // === SEARCH ===
  async searchGuides(url: URL, env: Env): Promise<Response> {
    const query = url.searchParams.get('q') || '';

    const results = await env.DB.prepare(`
      SELECT * FROM repair_guides 
      WHERE approved = 1
      AND (
        device_type LIKE ? OR
        device_model LIKE ? OR
        repair_type LIKE ?
      )
      ORDER BY views DESC
      LIMIT 20
    `).bind(`%${query}%`, `%${query}%`, `%${query}%`).all();

    return this.jsonResponse({
      query,
      results: results.results,
      total: results.results?.length || 0,
    });
  },

  async suggestGuide(request: Request, env: Env): Promise<Response> {
    const { issue_description, device_type, device_model } = await request.json() as any;

    // Use AI to match issue to guide
    const aiSuggestion = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{
        role: 'user',
        content: `Based on this repair issue: "${issue_description}" for ${device_type} ${device_model},
        what type of repair guide would be most helpful?
        Return JSON: { "suggested_repair_type": "", "confidence": "high|medium|low", "keywords": [] }`
      }]
    });

    // Search for matching guides
    const guides = await env.DB.prepare(`
      SELECT * FROM repair_guides 
      WHERE approved = 1
      AND device_type = ?
      AND (device_model LIKE ? OR device_model IS NULL)
      ORDER BY views DESC
      LIMIT 5
    `).bind(device_type, `%${device_model}%`).all();

    return this.jsonResponse({
      ai_suggestion: aiSuggestion,
      matching_guides: guides.results,
    });
  },

  jsonResponse(data: any, status = 200): Response {
    return new Response(JSON.stringify(data), {
      status,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  },
};
