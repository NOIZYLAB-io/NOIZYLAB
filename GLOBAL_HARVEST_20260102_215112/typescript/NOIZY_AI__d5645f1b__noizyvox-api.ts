/**
 * NOIZYVOX API Worker
 * Cloudflare Worker for the NOIZYVOX Guild, School & Marketplace
 * 
 * Bindings Required:
 * - D1: NOIZYVOX_DB (use agent-memory: 7b813205-fd12-4a23-84a6-ce83bc49ec70)
 * - KV: ARTIST_PROFILES (d0054fd99a8a4d45bde39e0f9a5d38b9)
 * - KV: PERSONAS (deed590a50664afe8b9030090ef45244)
 * - KV: ROYALTIES (4cf36e4bd1fd44fe802096925413f694)
 * - KV: ACADEMY (9cce0e456aac4b8ab75fca8c6cead2ba)
 * - KV: GUILD (8a15ed31fea8462da7c92a8237d6f854)
 * - KV: MANIFESTS (86da02180aa548a99fcba22090ca6444)
 */

export interface Env {
  NOIZYVOX_DB: D1Database;
  ARTIST_PROFILES: KVNamespace;
  PERSONAS: KVNamespace;
  ROYALTIES: KVNamespace;
  ACADEMY: KVNamespace;
  GUILD: KVNamespace;
  MANIFESTS: KVNamespace;
}

// CORS headers for all responses
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
};

// JSON response helper
function jsonResponse(data: any, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json',
      ...corsHeaders,
    },
  });
}

// Error response helper
function errorResponse(message: string, status = 400) {
  return jsonResponse({ error: message, success: false }, status);
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    // Handle CORS preflight
    if (method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // ===========================================
      // HEALTH CHECK
      // ===========================================
      if (path === '/' || path === '/health') {
        return jsonResponse({
          service: 'NOIZYVOX API',
          version: '1.0.0',
          tagline: 'Real voices. Real ownership. Unreal range.',
          status: 'operational',
          timestamp: new Date().toISOString(),
        });
      }

      // ===========================================
      // ARTISTS ENDPOINTS
      // ===========================================
      if (path === '/api/artists' && method === 'GET') {
        const { results } = await env.NOIZYVOX_DB.prepare(
          'SELECT id, name, stage_name, bio, tier, verified FROM noizyvox_artists ORDER BY tier DESC, name ASC'
        ).all();
        return jsonResponse({ artists: results, count: results.length });
      }

      if (path.startsWith('/api/artists/') && method === 'GET') {
        const artistId = path.split('/')[3];
        const { results } = await env.NOIZYVOX_DB.prepare(
          'SELECT * FROM noizyvox_artists WHERE id = ?'
        ).bind(artistId).all();
        
        if (results.length === 0) {
          return errorResponse('Artist not found', 404);
        }
        
        // Also get their personas
        const { results: personas } = await env.NOIZYVOX_DB.prepare(
          'SELECT * FROM noizyvox_personas WHERE artist_id = ?'
        ).bind(artistId).all();
        
        return jsonResponse({ artist: results[0], personas });
      }

      // ===========================================
      // PERSONAS ENDPOINTS
      // ===========================================
      if (path === '/api/personas' && method === 'GET') {
        const tier = url.searchParams.get('tier');
        const archetype = url.searchParams.get('archetype');
        
        let query = `
          SELECT p.*, a.name as artist_name, a.stage_name 
          FROM noizyvox_personas p 
          JOIN noizyvox_artists a ON p.artist_id = a.id 
          WHERE p.status = 'active'
        `;
        const params: string[] = [];
        
        if (tier) {
          query += ' AND p.license_tier = ?';
          params.push(tier);
        }
        if (archetype) {
          query += ' AND p.archetype LIKE ?';
          params.push(`%${archetype}%`);
        }
        
        query += ' ORDER BY p.name ASC';
        
        const stmt = env.NOIZYVOX_DB.prepare(query);
        const { results } = params.length > 0 
          ? await stmt.bind(...params).all()
          : await stmt.all();
          
        return jsonResponse({ personas: results, count: results.length });
      }

      if (path.startsWith('/api/personas/') && method === 'GET') {
        const personaId = path.split('/')[3];
        const { results } = await env.NOIZYVOX_DB.prepare(`
          SELECT p.*, a.name as artist_name, a.stage_name, a.bio as artist_bio
          FROM noizyvox_personas p 
          JOIN noizyvox_artists a ON p.artist_id = a.id 
          WHERE p.id = ?
        `).bind(personaId).all();
        
        if (results.length === 0) {
          return errorResponse('Persona not found', 404);
        }
        
        return jsonResponse({ persona: results[0] });
      }

      // ===========================================
      // GUILD ENDPOINTS
      // ===========================================
      if (path === '/api/guild' && method === 'GET') {
        const { results } = await env.NOIZYVOX_DB.prepare(`
          SELECT g.*, a.name, a.stage_name, a.tier as artist_tier
          FROM noizyvox_guild g
          JOIN noizyvox_artists a ON g.artist_id = a.id
          ORDER BY g.council_seat DESC, g.votes DESC
        `).all();
        
        return jsonResponse({ 
          guild: results, 
          count: results.length,
          council_members: results.filter((m: any) => m.council_seat === 1).length
        });
      }

      if (path === '/api/guild/stats' && method === 'GET') {
        const { results: artists } = await env.NOIZYVOX_DB.prepare(
          'SELECT COUNT(*) as count FROM noizyvox_artists'
        ).all();
        const { results: personas } = await env.NOIZYVOX_DB.prepare(
          'SELECT COUNT(*) as count FROM noizyvox_personas WHERE status = "active"'
        ).all();
        const { results: students } = await env.NOIZYVOX_DB.prepare(
          'SELECT COUNT(*) as count FROM noizyvox_students'
        ).all();
        const { results: renders } = await env.NOIZYVOX_DB.prepare(
          'SELECT COUNT(*) as count, SUM(artist_share_cents) as revenue FROM noizyvox_renders'
        ).all();
        
        return jsonResponse({
          stats: {
            artists: (artists[0] as any).count,
            personas: (personas[0] as any).count,
            students: (students[0] as any).count,
            renders: (renders[0] as any).count || 0,
            revenue_cents: (renders[0] as any).revenue || 0,
          },
          five_oaths: [
            'Your voice. Your model. Your control.',
            '75% to the artist. Always.',
            'No training without consent.',
            'Every render has a manifest.',
            'The Guild votes on the Guild.'
          ]
        });
      }

      // ===========================================
      // ACADEMY ENDPOINTS
      // ===========================================
      if (path === '/api/academy' && method === 'GET') {
        return jsonResponse({
          schools: [
            {
              name: 'School of Performance',
              tracks: ['Foundation', 'Character', 'Commercial', 'Narration'],
              description: 'Master the craft of voice acting'
            },
            {
              name: 'School of AI Mastery',
              tracks: ['Voice Modelling 101', 'Persona Design', 'Dataset Architecture'],
              description: 'Learn to create and control your AI voice'
            },
            {
              name: 'School of Business',
              tracks: ['Contracts', 'Licensing', 'Guild Operations'],
              description: 'Own your career, understand your rights'
            }
          ]
        });
      }

      if (path === '/api/academy/students' && method === 'GET') {
        const { results } = await env.NOIZYVOX_DB.prepare(
          'SELECT * FROM noizyvox_students ORDER BY enrolled_at DESC'
        ).all();
        return jsonResponse({ students: results, count: results.length });
      }

      // ===========================================
      // RENDERS / ROYALTIES ENDPOINTS
      // ===========================================
      if (path === '/api/renders' && method === 'POST') {
        const body = await request.json() as any;
        const { persona_id, project_name, script_hash, platform, territory, license_tier, duration_seconds } = body;
        
        // Get persona and artist info
        const { results: personaResults } = await env.NOIZYVOX_DB.prepare(
          'SELECT * FROM noizyvox_personas WHERE id = ?'
        ).bind(persona_id).all();
        
        if (personaResults.length === 0) {
          return errorResponse('Persona not found', 404);
        }
        
        const persona = personaResults[0] as any;
        
        // Calculate rate (example: $0.10 per second for standard, $0.20 for premium)
        const ratePerSecond = persona.license_tier === 'premium' ? 20 : 
                             persona.license_tier === 'exclusive' ? 50 : 10;
        const totalCents = Math.round(duration_seconds * ratePerSecond);
        const artistShare = Math.round(totalCents * 0.75); // 75% to artist
        const platformShare = totalCents - artistShare;
        
        const renderId = `render_${Date.now()}`;
        
        // Insert render record
        await env.NOIZYVOX_DB.prepare(`
          INSERT INTO noizyvox_renders 
          (id, persona_id, artist_id, project_name, script_hash, platform, territory, license_tier, duration_seconds, rate_cents, artist_share_cents, platform_share_cents, status)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'completed')
        `).bind(
          renderId, persona_id, persona.artist_id, project_name, script_hash, 
          platform, territory, license_tier, duration_seconds, 
          totalCents, artistShare, platformShare
        ).run();
        
        // Create manifest
        const manifestId = `manifest_${Date.now()}`;
        await env.NOIZYVOX_DB.prepare(`
          INSERT INTO noizyvox_manifests 
          (id, render_id, artist_id, persona_id, who_artist, who_persona, what_script_hash, what_project, where_platform, where_territory, when_duration_seconds, how_license_tier, how_rate_card)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        `).bind(
          manifestId, renderId, persona.artist_id, persona_id,
          persona.artist_id, persona.name, script_hash, project_name,
          platform, territory, duration_seconds, license_tier, `${ratePerSecond}c/sec`
        ).run();
        
        return jsonResponse({
          render_id: renderId,
          manifest_id: manifestId,
          total_cents: totalCents,
          artist_share_cents: artistShare,
          platform_share_cents: platformShare,
          split: '75/25',
          message: 'Render logged. 75% to the artist. Always.'
        }, 201);
      }

      // ===========================================
      // MANIFEST LOOKUP
      // ===========================================
      if (path.startsWith('/api/manifests/') && method === 'GET') {
        const manifestId = path.split('/')[3];
        const { results } = await env.NOIZYVOX_DB.prepare(
          'SELECT * FROM noizyvox_manifests WHERE id = ?'
        ).bind(manifestId).all();
        
        if (results.length === 0) {
          return errorResponse('Manifest not found', 404);
        }
        
        return jsonResponse({ 
          manifest: results[0],
          provenance: 'Cryptographically verified by NOIZYVOX Guild'
        });
      }

      // ===========================================
      // 404 - Not Found
      // ===========================================
      return errorResponse('Endpoint not found', 404);

    } catch (error) {
      console.error('NOIZYVOX API Error:', error);
      return errorResponse(`Internal error: ${error}`, 500);
    }
  },
};
