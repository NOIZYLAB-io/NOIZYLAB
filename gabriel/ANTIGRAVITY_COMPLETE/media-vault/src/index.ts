/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * MEDIA VAULT - MC96ECOUNIVERSE Cloud Storage Gateway
 * R2 Storage + Presigned URLs + Media Processing + Aquarium Archive Bridge
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════════════

interface Env {
  MEDIA_BUCKET: R2Bucket;
  DB: D1Database;
  KV: KVNamespace;
  AI: any;
  AWS_ACCESS_KEY_ID?: string;
  AWS_SECRET_ACCESS_KEY?: string;
  AWS_REGION?: string;
  S3_BUCKET?: string;
}

interface MediaFile {
  id: string;
  filename: string;
  contentType: string;
  size: number;
  path: string;
  bucket: 'r2' | 's3';
  uploadedAt: string;
  metadata: Record<string, string>;
}

interface UploadResponse {
  success: boolean;
  file?: MediaFile;
  uploadUrl?: string;
  error?: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// MEDIA CATEGORIES - AQUARIUM ARCHIVE STRUCTURE
// ═══════════════════════════════════════════════════════════════════════════════

const MEDIA_CATEGORIES = {
  audio: {
    name: 'Audio',
    extensions: ['.mp3', '.wav', '.aiff', '.flac', '.m4a', '.ogg', '.aac'],
    maxSize: 500 * 1024 * 1024, // 500MB
    subfolders: ['masters', 'stems', 'mixes', 'samples', 'podcasts']
  },
  video: {
    name: 'Video',
    extensions: ['.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v'],
    maxSize: 2 * 1024 * 1024 * 1024, // 2GB
    subfolders: ['raw', 'edited', 'exports', 'clips']
  },
  images: {
    name: 'Images',
    extensions: ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.heic', '.tiff'],
    maxSize: 50 * 1024 * 1024, // 50MB
    subfolders: ['photos', 'artwork', 'screenshots', 'thumbnails']
  },
  documents: {
    name: 'Documents',
    extensions: ['.pdf', '.doc', '.docx', '.txt', '.md', '.rtf'],
    maxSize: 100 * 1024 * 1024, // 100MB
    subfolders: ['contracts', 'lyrics', 'notes', 'manuals']
  },
  projects: {
    name: 'Projects',
    extensions: ['.als', '.logicx', '.ptx', '.flp', '.rpp', '.aup3'],
    maxSize: 5 * 1024 * 1024 * 1024, // 5GB
    subfolders: ['ableton', 'logic', 'protools', 'fl_studio']
  },
  archives: {
    name: 'Archives',
    extensions: ['.zip', '.rar', '.7z', '.tar', '.gz'],
    maxSize: 10 * 1024 * 1024 * 1024, // 10GB
    subfolders: ['backups', 'collections', 'bundles']
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// APP INITIALIZATION
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization', 'X-API-Key']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// UTILITY FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════════

function generateId(): string {
  return `mv_${Date.now()}_${Math.random().toString(36).substring(2, 11)}`;
}

function getCategory(filename: string): string | null {
  const ext = filename.toLowerCase().substring(filename.lastIndexOf('.'));
  for (const [key, cat] of Object.entries(MEDIA_CATEGORIES)) {
    if (cat.extensions.includes(ext)) return key;
  }
  return null;
}

function getContentType(filename: string): string {
  const ext = filename.toLowerCase().substring(filename.lastIndexOf('.'));
  const types: Record<string, string> = {
    '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav',
    '.flac': 'audio/flac',
    '.m4a': 'audio/mp4',
    '.ogg': 'audio/ogg',
    '.mp4': 'video/mp4',
    '.mov': 'video/quicktime',
    '.webm': 'video/webm',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.pdf': 'application/pdf',
    '.zip': 'application/zip'
  };
  return types[ext] || 'application/octet-stream';
}

// ═══════════════════════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════════════════════

// Health check
app.get('/', (c) => c.json({
  service: 'MEDIA VAULT',
  version: '1.0.0',
  status: 'OPERATIONAL',
  storage: {
    r2: c.env.MEDIA_BUCKET ? 'connected' : 'not configured',
    s3: c.env.S3_BUCKET ? 'configured' : 'not configured'
  },
  categories: Object.keys(MEDIA_CATEGORIES),
  timestamp: new Date().toISOString()
}));

app.get('/health', (c) => c.json({ ok: true, service: 'media-vault' }));

// ═══════════════════════════════════════════════════════════════════════════════
// R2 STORAGE OPERATIONS
// ═══════════════════════════════════════════════════════════════════════════════

// Get presigned upload URL
app.post('/upload/presign', async (c) => {
  try {
    const { filename, category, subfolder } = await c.req.json();
    
    if (!filename) {
      return c.json({ success: false, error: 'filename required' }, 400);
    }

    const detectedCategory = category || getCategory(filename);
    if (!detectedCategory) {
      return c.json({ success: false, error: 'unsupported file type' }, 400);
    }

    const id = generateId();
    const path = `${detectedCategory}/${subfolder || 'uploads'}/${id}_${filename}`;
    
    // Store pending upload metadata
    if (c.env.KV) {
      await c.env.KV.put(`pending:${id}`, JSON.stringify({
        id,
        filename,
        path,
        category: detectedCategory,
        createdAt: new Date().toISOString()
      }), { expirationTtl: 3600 }); // 1 hour expiry
    }

    return c.json({
      success: true,
      id,
      path,
      uploadEndpoint: `/upload/${id}`,
      expiresIn: 3600
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Direct upload to R2
app.put('/upload/:id', async (c) => {
  try {
    const id = c.req.param('id');
    
    // Get pending upload info
    let uploadInfo: any = null;
    if (c.env.KV) {
      const info = await c.env.KV.get(`pending:${id}`);
      if (info) uploadInfo = JSON.parse(info);
    }

    if (!uploadInfo) {
      return c.json({ success: false, error: 'upload session expired or invalid' }, 400);
    }

    const body = await c.req.arrayBuffer();
    
    if (!c.env.MEDIA_BUCKET) {
      return c.json({ success: false, error: 'R2 bucket not configured' }, 500);
    }

    // Upload to R2
    await c.env.MEDIA_BUCKET.put(uploadInfo.path, body, {
      httpMetadata: {
        contentType: getContentType(uploadInfo.filename)
      },
      customMetadata: {
        uploadId: id,
        originalFilename: uploadInfo.filename,
        category: uploadInfo.category,
        uploadedAt: new Date().toISOString()
      }
    });

    // Record in database
    if (c.env.DB) {
      await c.env.DB.prepare(`
        INSERT INTO media_files (id, filename, path, category, size, content_type, uploaded_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
      `).bind(
        id,
        uploadInfo.filename,
        uploadInfo.path,
        uploadInfo.category,
        body.byteLength,
        getContentType(uploadInfo.filename),
        new Date().toISOString()
      ).run();
    }

    // Clean up pending
    if (c.env.KV) {
      await c.env.KV.delete(`pending:${id}`);
    }

    return c.json({
      success: true,
      file: {
        id,
        filename: uploadInfo.filename,
        path: uploadInfo.path,
        category: uploadInfo.category,
        size: body.byteLength,
        contentType: getContentType(uploadInfo.filename)
      }
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// List files in category
app.get('/files/:category', async (c) => {
  try {
    const category = c.req.param('category');
    const limit = parseInt(c.req.query('limit') || '100');
    const cursor = c.req.query('cursor');

    if (!MEDIA_CATEGORIES[category as keyof typeof MEDIA_CATEGORIES]) {
      return c.json({ success: false, error: 'invalid category' }, 400);
    }

    if (!c.env.MEDIA_BUCKET) {
      return c.json({ success: false, error: 'R2 bucket not configured' }, 500);
    }

    const listed = await c.env.MEDIA_BUCKET.list({
      prefix: `${category}/`,
      limit,
      cursor: cursor || undefined
    });

    const files = listed.objects.map(obj => ({
      key: obj.key,
      size: obj.size,
      uploaded: obj.uploaded?.toISOString(),
      etag: obj.etag
    }));

    return c.json({
      success: true,
      category,
      files,
      truncated: listed.truncated,
      cursor: listed.truncated ? listed.cursor : null
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Get file / download
app.get('/file/:key{.+}', async (c) => {
  try {
    const key = c.req.param('key');
    
    if (!c.env.MEDIA_BUCKET) {
      return c.json({ success: false, error: 'R2 bucket not configured' }, 500);
    }

    const object = await c.env.MEDIA_BUCKET.get(key);
    
    if (!object) {
      return c.json({ success: false, error: 'file not found' }, 404);
    }

    const headers = new Headers();
    headers.set('Content-Type', object.httpMetadata?.contentType || 'application/octet-stream');
    headers.set('Content-Length', object.size.toString());
    headers.set('ETag', object.etag);
    
    // Check if download requested
    if (c.req.query('download') === 'true') {
      const filename = key.split('/').pop() || 'download';
      headers.set('Content-Disposition', `attachment; filename="${filename}"`);
    }

    return new Response(object.body, { headers });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Delete file
app.delete('/file/:key{.+}', async (c) => {
  try {
    const key = c.req.param('key');
    
    if (!c.env.MEDIA_BUCKET) {
      return c.json({ success: false, error: 'R2 bucket not configured' }, 500);
    }

    await c.env.MEDIA_BUCKET.delete(key);

    // Remove from database
    if (c.env.DB) {
      await c.env.DB.prepare('DELETE FROM media_files WHERE path = ?').bind(key).run();
    }

    return c.json({ success: true, deleted: key });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// AQUARIUM ARCHIVE INTEGRATION
// ═══════════════════════════════════════════════════════════════════════════════

// Search across all media
app.get('/search', async (c) => {
  try {
    const query = c.req.query('q') || '';
    const category = c.req.query('category');
    const limit = parseInt(c.req.query('limit') || '50');

    if (!c.env.DB) {
      return c.json({ success: false, error: 'database not configured' }, 500);
    }

    let sql = 'SELECT * FROM media_files WHERE filename LIKE ?';
    const params: any[] = [`%${query}%`];

    if (category) {
      sql += ' AND category = ?';
      params.push(category);
    }

    sql += ' ORDER BY uploaded_at DESC LIMIT ?';
    params.push(limit);

    const result = await c.env.DB.prepare(sql).bind(...params).all();

    return c.json({
      success: true,
      query,
      count: result.results?.length || 0,
      files: result.results || []
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Get storage stats
app.get('/stats', async (c) => {
  try {
    const stats: Record<string, any> = {
      categories: {}
    };

    if (c.env.MEDIA_BUCKET) {
      for (const category of Object.keys(MEDIA_CATEGORIES)) {
        const listed = await c.env.MEDIA_BUCKET.list({ prefix: `${category}/`, limit: 1000 });
        stats.categories[category] = {
          fileCount: listed.objects.length,
          totalSize: listed.objects.reduce((sum, obj) => sum + obj.size, 0)
        };
      }
    }

    if (c.env.DB) {
      const dbStats = await c.env.DB.prepare(`
        SELECT category, COUNT(*) as count, SUM(size) as total_size
        FROM media_files
        GROUP BY category
      `).all();
      stats.database = dbStats.results;
    }

    return c.json({
      success: true,
      stats,
      timestamp: new Date().toISOString()
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// AI-POWERED FEATURES
// ═══════════════════════════════════════════════════════════════════════════════

// Generate image with Workers AI
app.post('/ai/generate-image', async (c) => {
  try {
    const { prompt, style, width, height } = await c.req.json();

    if (!prompt) {
      return c.json({ success: false, error: 'prompt required' }, 400);
    }

    if (!c.env.AI) {
      return c.json({ success: false, error: 'AI not configured' }, 500);
    }

    const result = await c.env.AI.run('@cf/stabilityai/stable-diffusion-xl-base-1.0', {
      prompt: style ? `${prompt}, ${style}` : prompt,
      width: width || 1024,
      height: height || 1024
    });

    // Save to R2
    const id = generateId();
    const path = `images/ai-generated/${id}.png`;
    
    if (c.env.MEDIA_BUCKET) {
      await c.env.MEDIA_BUCKET.put(path, result, {
        httpMetadata: { contentType: 'image/png' },
        customMetadata: { prompt, generatedAt: new Date().toISOString() }
      });
    }

    return c.json({
      success: true,
      id,
      path,
      prompt,
      downloadUrl: `/file/${path}`
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Analyze image with AI
app.post('/ai/analyze-image', async (c) => {
  try {
    const { imageUrl, question } = await c.req.json();

    if (!imageUrl) {
      return c.json({ success: false, error: 'imageUrl required' }, 400);
    }

    if (!c.env.AI) {
      return c.json({ success: false, error: 'AI not configured' }, 500);
    }

    // Fetch image
    const imageResponse = await fetch(imageUrl);
    const imageData = await imageResponse.arrayBuffer();

    const result = await c.env.AI.run('@cf/llava-hf/llava-1.5-7b-hf', {
      image: [...new Uint8Array(imageData)],
      prompt: question || 'Describe this image in detail.'
    });

    return c.json({
      success: true,
      analysis: result.description || result.response,
      question
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Transcribe audio with Whisper
app.post('/ai/transcribe', async (c) => {
  try {
    const formData = await c.req.formData();
    const audio = formData.get('audio') as unknown as Blob;

    if (!audio) {
      return c.json({ success: false, error: 'audio file required' }, 400);
    }

    if (!c.env.AI) {
      return c.json({ success: false, error: 'AI not configured' }, 500);
    }

    const audioData = await audio.arrayBuffer();

    const result = await c.env.AI.run('@cf/openai/whisper', {
      audio: [...new Uint8Array(audioData)]
    });

    return c.json({
      success: true,
      transcription: result.text,
      language: result.language || 'en'
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// DASHBOARD
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/dashboard', (c) => {
  return c.html(`<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>📦 Media Vault - MC96ECOUNIVERSE</title>
<style>
:root{--bg:#0a0908;--card:#0d0c0a;--border:#1a1815;--gold:#d4a574;--blue:#5a9cc6;--text:#e8ddd0;--muted:#6b5a45;--green:#6a9c59}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:-apple-system,sans-serif;padding:1rem}
.h{text-align:center;padding:2rem 0}
.logo{font-size:2.5rem;font-weight:900;background:linear-gradient(135deg,var(--blue),var(--gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem;max-width:1400px;margin:0 auto}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1rem}
.card h2{color:var(--gold);font-size:0.75rem;text-transform:uppercase;margin-bottom:0.75rem;letter-spacing:1px}
.cat{display:grid;grid-template-columns:repeat(auto-fit,minmax(100px,1fr));gap:0.5rem;margin-top:0.5rem}
.cat-item{background:var(--bg);border:1px solid var(--border);padding:0.5rem;border-radius:6px;text-align:center;cursor:pointer;transition:all .2s}
.cat-item:hover{border-color:var(--gold);transform:scale(1.02)}
.cat-item span{display:block;font-size:1.5rem}
.cat-item small{color:var(--muted);font-size:0.65rem}
.upload-zone{border:2px dashed var(--border);border-radius:8px;padding:2rem;text-align:center;transition:all .2s}
.upload-zone.active{border-color:var(--gold);background:rgba(212,165,116,0.05)}
.btn{background:var(--gold);color:#000;border:none;padding:0.6rem 1.2rem;border-radius:6px;cursor:pointer;font-weight:600;margin:0.25rem}
.stat{display:flex;justify-content:space-between;padding:0.35rem 0;border-bottom:1px solid var(--border);font-size:0.8rem}
.ft{text-align:center;margin-top:1.5rem;color:var(--muted);font-size:0.65rem}
</style>
</head><body>
<div class="h">
<div class="logo">📦 MEDIA VAULT</div>
<p style="color:var(--muted);margin-top:0.5rem">MC96ECOUNIVERSE Cloud Storage</p>
</div>
<div class="grid">
<div class="card">
<h2>📁 Categories</h2>
<div class="cat">
<div class="cat-item" onclick="browse('audio')"><span>🎵</span>Audio<small>MP3, WAV, FLAC</small></div>
<div class="cat-item" onclick="browse('video')"><span>🎬</span>Video<small>MP4, MOV</small></div>
<div class="cat-item" onclick="browse('images')"><span>🖼️</span>Images<small>JPG, PNG, GIF</small></div>
<div class="cat-item" onclick="browse('documents')"><span>📄</span>Docs<small>PDF, TXT</small></div>
<div class="cat-item" onclick="browse('projects')"><span>🎛️</span>Projects<small>ALS, Logic</small></div>
<div class="cat-item" onclick="browse('archives')"><span>📦</span>Archives<small>ZIP, RAR</small></div>
</div>
</div>
<div class="card">
<h2>⬆️ Upload</h2>
<div class="upload-zone" id="dropzone">
<p>Drop files here or click to upload</p>
<input type="file" id="fileInput" multiple style="display:none">
<button class="btn" onclick="document.getElementById('fileInput').click()">Select Files</button>
</div>
<div id="uploadStatus"></div>
</div>
<div class="card">
<h2>🔍 Search</h2>
<input type="text" id="searchInput" placeholder="Search files..." style="width:100%;padding:0.6rem;background:var(--bg);border:1px solid var(--border);border-radius:6px;color:var(--text)">
<div id="searchResults" style="margin-top:0.5rem;max-height:200px;overflow-y:auto"></div>
</div>
<div class="card">
<h2>🤖 AI Tools</h2>
<button class="btn" onclick="generateImage()">Generate Image</button>
<button class="btn" onclick="transcribeAudio()">Transcribe Audio</button>
<div id="aiOutput" style="margin-top:0.5rem;font-size:0.75rem;color:var(--muted)"></div>
</div>
</div>
<p class="ft">MEDIA VAULT v1.0 • MC96ECOUNIVERSE • AQUARIUM ARCHIVE GATEWAY</p>
<script>
const dz=document.getElementById('dropzone');
const fi=document.getElementById('fileInput');
dz.addEventListener('dragover',e=>{e.preventDefault();dz.classList.add('active')});
dz.addEventListener('dragleave',()=>dz.classList.remove('active'));
dz.addEventListener('drop',e=>{e.preventDefault();dz.classList.remove('active');handleFiles(e.dataTransfer.files)});
fi.addEventListener('change',e=>handleFiles(e.target.files));
async function handleFiles(files){
  const status=document.getElementById('uploadStatus');
  for(const f of files){
    status.innerHTML='Uploading '+f.name+'...';
    try{
      const pre=await(await fetch('/upload/presign',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({filename:f.name})})).json();
      if(pre.success){
        await fetch(pre.uploadEndpoint,{method:'PUT',body:f});
        status.innerHTML='✅ '+f.name+' uploaded!';
      }else{status.innerHTML='❌ '+pre.error}
    }catch(e){status.innerHTML='❌ Error: '+e}
  }
}
function browse(cat){window.location.href='/files/'+cat}
document.getElementById('searchInput').addEventListener('input',async e=>{
  const q=e.target.value;
  if(q.length<2)return;
  const r=await(await fetch('/search?q='+encodeURIComponent(q))).json();
  document.getElementById('searchResults').innerHTML=r.files?.map(f=>'<div class="stat">'+f.filename+'</div>').join('')||'No results';
});
async function generateImage(){
  const prompt=window.prompt('Describe the image:');
  if(!prompt)return;
  document.getElementById('aiOutput').textContent='Generating...';
  const r=await(await fetch('/ai/generate-image',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt})})).json();
  document.getElementById('aiOutput').innerHTML=r.success?'✅ Generated: <a href="'+r.downloadUrl+'" style="color:var(--gold)">Download</a>':'❌ '+r.error;
}
function transcribeAudio(){
  const input=document.createElement('input');
  input.type='file';input.accept='audio/*';
  input.onchange=async e=>{
    const f=e.target.files[0];if(!f)return;
    document.getElementById('aiOutput').textContent='Transcribing...';
    const fd=new FormData();fd.append('audio',f);
    const r=await(await fetch('/ai/transcribe',{method:'POST',body:fd})).json();
    document.getElementById('aiOutput').textContent=r.success?'📝 '+r.transcription:'❌ '+r.error;
  };
  input.click();
}
</script>
</body></html>`);
});

export default app;
