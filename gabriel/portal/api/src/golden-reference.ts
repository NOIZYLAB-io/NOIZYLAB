/**
 * Golden Reference Management System
 * 
 * Handles storage, retrieval, and comparison of known-good PCB images
 * Uses Cloudflare R2 for storage and KV for metadata indexing
 */

// Reference manifest structure
interface ComponentManifest {
  id: string;           // Reference designator (R1, C5, U3)
  type: string;         // resistor, capacitor, ic, connector, etc.
  package: string;      // 0402, 0603, QFN48, BGA, etc.
  expected_value: string;
  position: {
    x: number;          // Normalized 0-1 coordinates
    y: number;
  };
  bounding_box: {
    width: number;
    height: number;
  };
  critical: boolean;    // Is this safety-critical?
  polarity_sensitive: boolean;
  solder_points: number;
}

interface GoldenReference {
  id: string;
  name: string;
  manufacturer: string;
  model: string;
  version: string;
  created_at: string;
  updated_at: string;
  created_by: string;
  
  // Image metadata
  image_width: number;
  image_height: number;
  image_url: string;
  thumbnail_url: string;
  
  // Components
  components: ComponentManifest[];
  component_count: number;
  
  // Metadata
  tags: string[];
  category: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced' | 'expert';
  
  // Statistics
  scan_count: number;
  success_rate: number;
}

/**
 * Create a new Golden Reference
 */
export async function createReference(
  request: Request,
  env: Env
): Promise<Response> {
  const formData = await request.formData();
  
  const image = formData.get('image') as File;
  const manifest = JSON.parse(formData.get('manifest') as string);
  const metadata = JSON.parse(formData.get('metadata') as string);
  
  if (!image || !manifest) {
    return jsonResponse({ error: 'Missing required fields' }, 400);
  }
  
  const referenceId = crypto.randomUUID();
  const timestamp = new Date().toISOString();
  
  // Process and store images
  const imageBuffer = await image.arrayBuffer();
  
  // Store full resolution image
  await env.R2_REFERENCES.put(
    `references/${referenceId}/full.jpg`,
    imageBuffer,
    { httpMetadata: { contentType: 'image/jpeg' } }
  );
  
  // Generate and store thumbnail (in production, use Workers Image Resizing)
  await env.R2_REFERENCES.put(
    `references/${referenceId}/thumb.jpg`,
    imageBuffer, // Would be resized in production
    { httpMetadata: { contentType: 'image/jpeg' } }
  );
  
  // Build reference document
  const reference: GoldenReference = {
    id: referenceId,
    name: metadata.name,
    manufacturer: metadata.manufacturer,
    model: metadata.model,
    version: metadata.version || '1.0',
    created_at: timestamp,
    updated_at: timestamp,
    created_by: metadata.created_by,
    
    image_width: manifest.image_width,
    image_height: manifest.image_height,
    image_url: `https://r2.noizylab.ai/references/${referenceId}/full.jpg`,
    thumbnail_url: `https://r2.noizylab.ai/references/${referenceId}/thumb.jpg`,
    
    components: manifest.components,
    component_count: manifest.components.length,
    
    tags: metadata.tags || [],
    category: metadata.category || 'other',
    difficulty: metadata.difficulty || 'intermediate',
    
    scan_count: 0,
    success_rate: 0
  };
  
  // Store manifest
  await env.R2_REFERENCES.put(
    `references/${referenceId}/manifest.json`,
    JSON.stringify(reference),
    { httpMetadata: { contentType: 'application/json' } }
  );
  
  // Index in KV for fast lookups
  await env.KV_REFERENCES.put(`ref:${referenceId}`, JSON.stringify({
    id: referenceId,
    name: reference.name,
    manufacturer: reference.manufacturer,
    model: reference.model,
    thumbnail_url: reference.thumbnail_url,
    component_count: reference.component_count,
    category: reference.category
  }));
  
  // Add to category index
  const categoryKey = `category:${reference.category}`;
  let categoryRefs = await env.KV_REFERENCES.get(categoryKey);
  const refs = categoryRefs ? JSON.parse(categoryRefs) : [];
  refs.push(referenceId);
  await env.KV_REFERENCES.put(categoryKey, JSON.stringify(refs));
  
  // Add to manufacturer index
  const mfgKey = `manufacturer:${reference.manufacturer.toLowerCase()}`;
  let mfgRefs = await env.KV_REFERENCES.get(mfgKey);
  const mfgList = mfgRefs ? JSON.parse(mfgRefs) : [];
  mfgList.push(referenceId);
  await env.KV_REFERENCES.put(mfgKey, JSON.stringify(mfgList));
  
  return jsonResponse({
    success: true,
    referenceId,
    message: 'Golden Reference created successfully'
  });
}

/**
 * Get a Golden Reference by ID
 */
export async function getReference(
  referenceId: string,
  env: Env
): Promise<GoldenReference | null> {
  const manifest = await env.R2_REFERENCES.get(`references/${referenceId}/manifest.json`);
  
  if (!manifest) {
    return null;
  }
  
  return manifest.json();
}

/**
 * List references with optional filters
 */
export async function listReferences(
  options: {
    category?: string;
    manufacturer?: string;
    search?: string;
    limit?: number;
    offset?: number;
  },
  env: Env
): Promise<{ references: GoldenReference[]; total: number }> {
  let referenceIds: string[] = [];
  
  if (options.category) {
    const categoryRefs = await env.KV_REFERENCES.get(`category:${options.category}`);
    referenceIds = categoryRefs ? JSON.parse(categoryRefs) : [];
  } else if (options.manufacturer) {
    const mfgRefs = await env.KV_REFERENCES.get(`manufacturer:${options.manufacturer.toLowerCase()}`);
    referenceIds = mfgRefs ? JSON.parse(mfgRefs) : [];
  } else {
    // Get all references (paginated)
    const list = await env.R2_REFERENCES.list({ prefix: 'references/', delimiter: '/' });
    referenceIds = list.delimitedPrefixes.map(p => p.replace('references/', '').replace('/', ''));
  }
  
  const total = referenceIds.length;
  const limit = options.limit || 20;
  const offset = options.offset || 0;
  
  const paginatedIds = referenceIds.slice(offset, offset + limit);
  
  const references = await Promise.all(
    paginatedIds.map(id => getReference(id, env))
  );
  
  return {
    references: references.filter(Boolean) as GoldenReference[],
    total
  };
}

/**
 * Search references by name, manufacturer, or model
 */
export async function searchReferences(
  query: string,
  env: Env
): Promise<GoldenReference[]> {
  const normalizedQuery = query.toLowerCase();
  
  // Get all reference metadata from KV
  const list = await env.KV_REFERENCES.list({ prefix: 'ref:' });
  
  const matches: GoldenReference[] = [];
  
  for (const key of list.keys) {
    const data = await env.KV_REFERENCES.get(key.name);
    if (data) {
      const ref = JSON.parse(data);
      if (
        ref.name.toLowerCase().includes(normalizedQuery) ||
        ref.manufacturer.toLowerCase().includes(normalizedQuery) ||
        ref.model.toLowerCase().includes(normalizedQuery)
      ) {
        const fullRef = await getReference(ref.id, env);
        if (fullRef) matches.push(fullRef);
      }
    }
  }
  
  return matches;
}

/**
 * Compare scanned image to Golden Reference
 */
export async function compareToGoldenReference(
  scannedComponents: any[],
  referenceId: string,
  env: Env
): Promise<{
  issues: Issue[];
  matchedCount: number;
  totalReferenceComponents: number;
  confidence: number;
}> {
  const reference = await getReference(referenceId, env);
  
  if (!reference) {
    throw new Error('Reference not found');
  }
  
  const issues: Issue[] = [];
  let matchedCount = 0;
  
  for (const refComponent of reference.components) {
    // Find matching component in scan by position (with tolerance)
    const match = scannedComponents.find(scanned => {
      const positionMatch = 
        Math.abs(scanned.position.x - refComponent.position.x) < 0.02 &&
        Math.abs(scanned.position.y - refComponent.position.y) < 0.02;
      
      const idMatch = scanned.id === refComponent.id;
      
      return positionMatch || idMatch;
    });
    
    if (!match) {
      issues.push({
        component: refComponent.id,
        type: 'MISSING',
        severity: refComponent.critical ? 'HIGH' : 'MEDIUM',
        expected: refComponent.expected_value,
        position: refComponent.position
      });
    } else {
      matchedCount++;
      
      // Check value
      if (match.value_detected && match.value_detected !== refComponent.expected_value) {
        issues.push({
          component: refComponent.id,
          type: 'WRONG_VALUE',
          severity: 'HIGH',
          expected: refComponent.expected_value,
          detected: match.value_detected,
          position: match.position
        });
      }
      
      // Check solder quality
      if (match.solder_quality !== undefined && match.solder_quality < 0.7) {
        issues.push({
          component: refComponent.id,
          type: 'SOLDER_DEFECT',
          severity: match.solder_quality < 0.4 ? 'HIGH' : 'MEDIUM',
          confidence: match.solder_quality,
          position: match.position
        });
      }
      
      // Check polarity for sensitive components
      if (refComponent.polarity_sensitive && match.polarity_reversed) {
        issues.push({
          component: refComponent.id,
          type: 'POLARITY_ERROR',
          severity: 'HIGH',
          position: match.position
        });
      }
    }
  }
  
  // Check for unexpected components
  for (const scanned of scannedComponents) {
    const inReference = reference.components.some(ref =>
      Math.abs(scanned.position.x - ref.position.x) < 0.02 &&
      Math.abs(scanned.position.y - ref.position.y) < 0.02
    );
    
    if (!inReference) {
      issues.push({
        component: scanned.id || 'Unknown',
        type: 'UNEXPECTED',
        severity: 'MEDIUM',
        detected: scanned.type,
        position: scanned.position
      });
    }
  }
  
  // Calculate confidence based on match rate and issue severity
  const matchRate = matchedCount / reference.components.length;
  const highSeverityCount = issues.filter(i => i.severity === 'HIGH').length;
  const confidence = Math.max(0, matchRate - (highSeverityCount * 0.1));
  
  // Update reference scan statistics
  await updateReferenceStats(referenceId, issues.length === 0, env);
  
  return {
    issues,
    matchedCount,
    totalReferenceComponents: reference.components.length,
    confidence
  };
}

/**
 * Update reference statistics after a scan
 */
async function updateReferenceStats(
  referenceId: string,
  success: boolean,
  env: Env
): Promise<void> {
  const reference = await getReference(referenceId, env);
  if (!reference) return;
  
  reference.scan_count++;
  const successCount = Math.round(reference.success_rate * (reference.scan_count - 1));
  reference.success_rate = (successCount + (success ? 1 : 0)) / reference.scan_count;
  reference.updated_at = new Date().toISOString();
  
  await env.R2_REFERENCES.put(
    `references/${referenceId}/manifest.json`,
    JSON.stringify(reference),
    { httpMetadata: { contentType: 'application/json' } }
  );
}

/**
 * Delete a Golden Reference
 */
export async function deleteReference(
  referenceId: string,
  env: Env
): Promise<boolean> {
  const reference = await getReference(referenceId, env);
  if (!reference) return false;
  
  // Delete from R2
  await env.R2_REFERENCES.delete(`references/${referenceId}/full.jpg`);
  await env.R2_REFERENCES.delete(`references/${referenceId}/thumb.jpg`);
  await env.R2_REFERENCES.delete(`references/${referenceId}/manifest.json`);
  
  // Remove from KV indexes
  await env.KV_REFERENCES.delete(`ref:${referenceId}`);
  
  // Remove from category index
  const categoryKey = `category:${reference.category}`;
  const categoryRefs = await env.KV_REFERENCES.get(categoryKey);
  if (categoryRefs) {
    const refs = JSON.parse(categoryRefs).filter((id: string) => id !== referenceId);
    await env.KV_REFERENCES.put(categoryKey, JSON.stringify(refs));
  }
  
  return true;
}

// Types
interface Issue {
  component: string;
  type: 'MISSING' | 'WRONG_VALUE' | 'SOLDER_DEFECT' | 'UNEXPECTED' | 'POLARITY_ERROR';
  severity: 'HIGH' | 'MEDIUM' | 'LOW';
  expected?: string;
  detected?: string;
  confidence?: number;
  position?: { x: number; y: number };
}

interface Env {
  R2_REFERENCES: R2Bucket;
  KV_REFERENCES: KVNamespace;
}

function jsonResponse(data: any, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export type { GoldenReference, ComponentManifest, Issue };
