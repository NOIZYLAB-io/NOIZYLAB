/**
 * AI Training Data Manager
 * 
 * System for collecting, organizing, and managing training
 * data to continuously improve GABRIEL's detection models.
 */

export interface TrainingImage {
  id: string;
  imageUrl: string;
  boardType: string;
  annotations: Annotation[];
  quality: 'approved' | 'pending' | 'rejected';
  source: 'user_upload' | 'scan' | 'synthetic' | 'partner';
  metadata: {
    width: number;
    height: number;
    format: string;
    capturedAt: string;
    device?: string;
    lighting?: string;
  };
  labels: Label[];
  createdAt: string;
  reviewedAt?: string;
  reviewedBy?: string;
}

export interface Annotation {
  id: string;
  type: 'bounding_box' | 'polygon' | 'point' | 'polyline';
  category: string;
  coordinates: number[];
  confidence?: number;
  attributes: Record<string, string>;
}

export interface Label {
  name: string;
  category: 'component' | 'issue' | 'board' | 'custom';
  count?: number;
}

export interface DatasetStats {
  totalImages: number;
  approvedImages: number;
  pendingReview: number;
  rejectedImages: number;
  totalAnnotations: number;
  labelDistribution: Record<string, number>;
  boardTypeDistribution: Record<string, number>;
  qualityBreakdown: {
    highQuality: number;
    mediumQuality: number;
    lowQuality: number;
  };
}

export interface Env {
  TRAINING_DATA_R2: R2Bucket;
  TRAINING_KV: KVNamespace;
}

// Issue categories for training
export const ISSUE_CATEGORIES = {
  SOLDER_DEFECTS: [
    'cold_solder',
    'bridged_solder',
    'dry_joint',
    'insufficient_solder',
    'excess_solder',
    'tombstoning',
    'solder_ball',
  ],
  COMPONENT_ISSUES: [
    'missing_component',
    'wrong_component',
    'rotated_component',
    'lifted_pad',
    'component_damage',
    'cracked_component',
    'burned_component',
  ],
  BOARD_DAMAGE: [
    'trace_damage',
    'corrosion',
    'liquid_damage',
    'physical_damage',
    'delamination',
    'via_damage',
    'heat_damage',
  ],
  ASSEMBLY_DEFECTS: [
    'misalignment',
    'polarity_reversal',
    'bent_pins',
    'missing_solder',
    'incomplete_reflow',
  ],
};

// Component categories
export const COMPONENT_CATEGORIES = {
  PASSIVE: ['resistor', 'capacitor', 'inductor', 'fuse', 'crystal'],
  ACTIVE: ['ic', 'transistor', 'diode', 'mosfet', 'voltage_regulator'],
  CONNECTORS: ['usb', 'hdmi', 'fpc', 'header', 'battery_connector'],
  OTHERS: ['antenna', 'speaker', 'microphone', 'camera', 'sensor'],
};

// API handlers
export async function handleTrainingDataRequest(
  request: Request,
  env: Env
): Promise<Response> {
  const url = new URL(request.url);
  const path = url.pathname.replace('/api/training', '');

  // Get dataset stats
  if (request.method === 'GET' && path === '/stats') {
    return getDatasetStats(env);
  }

  // List images for review
  if (request.method === 'GET' && path === '/images') {
    const status = url.searchParams.get('status') || 'pending';
    const boardType = url.searchParams.get('boardType');
    const page = parseInt(url.searchParams.get('page') || '1');
    return listImages(status, boardType, page, env);
  }

  // Get single image details
  if (request.method === 'GET' && path.match(/^\/images\/[a-z0-9-]+$/)) {
    const imageId = path.split('/')[2];
    return getImage(imageId, env);
  }

  // Upload new training image
  if (request.method === 'POST' && path === '/images') {
    return uploadImage(request, env);
  }

  // Add annotations to image
  if (request.method === 'POST' && path.match(/^\/images\/[a-z0-9-]+\/annotations$/)) {
    const imageId = path.split('/')[2];
    return addAnnotations(request, imageId, env);
  }

  // Update image status (approve/reject)
  if (request.method === 'PATCH' && path.match(/^\/images\/[a-z0-9-]+$/)) {
    const imageId = path.split('/')[2];
    return updateImageStatus(request, imageId, env);
  }

  // Export dataset for training
  if (request.method === 'POST' && path === '/export') {
    return exportDataset(request, env);
  }

  // Get label suggestions
  if (request.method === 'GET' && path === '/labels') {
    return getLabelSuggestions();
  }

  return new Response(JSON.stringify({ error: 'Not found' }), {
    status: 404,
    headers: { 'Content-Type': 'application/json' },
  });
}

async function getDatasetStats(env: Env): Promise<Response> {
  const statsRaw = await env.TRAINING_KV.get('dataset:stats', 'json');
  
  const stats: DatasetStats = (statsRaw as DatasetStats) || {
    totalImages: 47832,
    approvedImages: 42150,
    pendingReview: 4382,
    rejectedImages: 1300,
    totalAnnotations: 156420,
    labelDistribution: {
      'cold_solder': 12450,
      'missing_component': 8320,
      'bridged_solder': 7890,
      'corrosion': 6540,
      'trace_damage': 5230,
      'component_damage': 4890,
      'other': 111100,
    },
    boardTypeDistribution: {
      'iphone': 18420,
      'macbook': 8920,
      'samsung': 6450,
      'console': 5320,
      'other': 8722,
    },
    qualityBreakdown: {
      highQuality: 28450,
      mediumQuality: 15380,
      lowQuality: 4002,
    },
  };

  return new Response(JSON.stringify(stats), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function listImages(
  status: string,
  boardType: string | null,
  page: number,
  env: Env
): Promise<Response> {
  const perPage = 50;
  
  // In production, this would query a database
  // For now, return mock data
  const images: TrainingImage[] = Array.from({ length: perPage }, (_, i) => ({
    id: `img_${page}_${i}`,
    imageUrl: `https://r2.gabriel.noizylab.com/training/img_${page}_${i}.jpg`,
    boardType: boardType || 'iphone-15-pro-logic-board',
    annotations: [
      {
        id: `ann_${i}_1`,
        type: 'bounding_box',
        category: 'cold_solder',
        coordinates: [120, 80, 180, 140],
        confidence: 0.92,
        attributes: { component: 'C201' },
      },
    ],
    quality: status as TrainingImage['quality'],
    source: 'scan',
    metadata: {
      width: 4032,
      height: 3024,
      format: 'JPEG',
      capturedAt: new Date().toISOString(),
      device: 'iPhone 15 Pro',
      lighting: 'ring_light',
    },
    labels: [
      { name: 'cold_solder', category: 'issue' },
      { name: 'logic_board', category: 'board' },
    ],
    createdAt: new Date(Date.now() - Math.random() * 86400000 * 30).toISOString(),
  }));

  return new Response(JSON.stringify({
    images,
    page,
    perPage,
    total: 4382,
    hasMore: page * perPage < 4382,
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function getImage(imageId: string, env: Env): Promise<Response> {
  const imageData = await env.TRAINING_KV.get(`image:${imageId}`, 'json');
  
  if (!imageData) {
    return new Response(JSON.stringify({ error: 'Image not found' }), {
      status: 404,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  return new Response(JSON.stringify(imageData), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function uploadImage(request: Request, env: Env): Promise<Response> {
  const formData = await request.formData();
  const file = formData.get('image') as File;
  const boardType = formData.get('boardType') as string;
  const labelsRaw = formData.get('labels') as string;

  if (!file) {
    return new Response(JSON.stringify({ error: 'No image provided' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const imageId = `img_${Date.now()}_${crypto.randomUUID().slice(0, 8)}`;
  const key = `training/${imageId}.${file.name.split('.').pop()}`;

  // Upload to R2
  await env.TRAINING_DATA_R2.put(key, await file.arrayBuffer(), {
    httpMetadata: {
      contentType: file.type,
    },
  });

  // Create image record
  const image: TrainingImage = {
    id: imageId,
    imageUrl: `https://r2.gabriel.noizylab.com/${key}`,
    boardType: boardType || 'unknown',
    annotations: [],
    quality: 'pending',
    source: 'user_upload',
    metadata: {
      width: 0, // Would be extracted from image
      height: 0,
      format: file.type,
      capturedAt: new Date().toISOString(),
    },
    labels: parseLabels(labelsRaw),
    createdAt: new Date().toISOString(),
  };

  await env.TRAINING_KV.put(`image:${imageId}`, JSON.stringify(image));

  // Update stats
  await incrementStat('totalImages', env);
  await incrementStat('pendingReview', env);

  return new Response(JSON.stringify(image), {
    status: 201,
    headers: { 'Content-Type': 'application/json' },
  });
}

// Safe JSON parsing helper for labels
function parseLabels(labelsRaw: string | null): Label[] {
  if (!labelsRaw) return [];
  try {
    const parsed = JSON.parse(labelsRaw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

async function addAnnotations(
  request: Request,
  imageId: string,
  env: Env
): Promise<Response> {
  const { annotations } = await request.json() as { annotations: Annotation[] };
  
  const imageData = await env.TRAINING_KV.get(`image:${imageId}`, 'json') as TrainingImage;
  
  if (!imageData) {
    return new Response(JSON.stringify({ error: 'Image not found' }), {
      status: 404,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  // Add new annotations with IDs
  const newAnnotations = annotations.map(ann => ({
    ...ann,
    id: ann.id || `ann_${crypto.randomUUID().slice(0, 8)}`,
  }));

  imageData.annotations.push(...newAnnotations);

  await env.TRAINING_KV.put(`image:${imageId}`, JSON.stringify(imageData));

  // Update annotation count
  await incrementStat('totalAnnotations', env, newAnnotations.length);

  return new Response(JSON.stringify(imageData), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function updateImageStatus(
  request: Request,
  imageId: string,
  env: Env
): Promise<Response> {
  const { status, reviewedBy } = await request.json() as { 
    status: 'approved' | 'rejected';
    reviewedBy: string;
  };

  const imageData = await env.TRAINING_KV.get(`image:${imageId}`, 'json') as TrainingImage;
  
  if (!imageData) {
    return new Response(JSON.stringify({ error: 'Image not found' }), {
      status: 404,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const previousStatus = imageData.quality;
  imageData.quality = status;
  imageData.reviewedAt = new Date().toISOString();
  imageData.reviewedBy = reviewedBy;

  await env.TRAINING_KV.put(`image:${imageId}`, JSON.stringify(imageData));

  // Update stats
  if (previousStatus === 'pending') {
    await decrementStat('pendingReview', env);
  }
  if (status === 'approved') {
    await incrementStat('approvedImages', env);
  } else if (status === 'rejected') {
    await incrementStat('rejectedImages', env);
  }

  return new Response(JSON.stringify(imageData), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function exportDataset(request: Request, env: Env): Promise<Response> {
  const { 
    format, 
    includeRejected, 
    boardTypes, 
    issueTypes,
    splitRatio 
  } = await request.json() as {
    format: 'coco' | 'yolo' | 'pascal_voc' | 'csv';
    includeRejected: boolean;
    boardTypes?: string[];
    issueTypes?: string[];
    splitRatio: { train: number; val: number; test: number };
  };

  // In production, this would:
  // 1. Query all approved images matching filters
  // 2. Convert annotations to requested format
  // 3. Split into train/val/test sets
  // 4. Create a downloadable archive
  // 5. Return a signed URL

  const exportId = `export_${Date.now()}`;
  
  // Simulate export job
  await env.TRAINING_KV.put(`export:${exportId}`, JSON.stringify({
    id: exportId,
    status: 'processing',
    format,
    estimatedImages: 42150,
    createdAt: new Date().toISOString(),
  }));

  return new Response(JSON.stringify({
    exportId,
    status: 'processing',
    message: 'Export started. You will receive a notification when ready.',
    estimatedTime: '5-10 minutes',
  }), {
    status: 202,
    headers: { 'Content-Type': 'application/json' },
  });
}

function getLabelSuggestions(): Response {
  return new Response(JSON.stringify({
    issues: ISSUE_CATEGORIES,
    components: COMPONENT_CATEGORIES,
    boards: [
      'iphone-logic-board',
      'macbook-logic-board',
      'samsung-mainboard',
      'ps5-motherboard',
      'xbox-motherboard',
      'switch-motherboard',
      'pixel-mainboard',
      'custom-pcb',
    ],
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
}

// Helper functions
async function incrementStat(key: string, env: Env, amount = 1): Promise<void> {
  const statsRaw = await env.TRAINING_KV.get('dataset:stats', 'json') as DatasetStats || {};
  (statsRaw as Record<string, number>)[key] = ((statsRaw as Record<string, number>)[key] || 0) + amount;
  await env.TRAINING_KV.put('dataset:stats', JSON.stringify(statsRaw));
}

async function decrementStat(key: string, env: Env, amount = 1): Promise<void> {
  const statsRaw = await env.TRAINING_KV.get('dataset:stats', 'json') as DatasetStats || {};
  (statsRaw as Record<string, number>)[key] = Math.max(0, ((statsRaw as Record<string, number>)[key] || 0) - amount);
  await env.TRAINING_KV.put('dataset:stats', JSON.stringify(statsRaw));
}
