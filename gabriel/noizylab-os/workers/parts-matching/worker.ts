/**
 * NoizyLab OS - Parts Matching Neural Network Worker
 * 🧠 AI-Powered Component Compatibility & Cross-Reference System
 * 
 * Uses vector embeddings to find compatible parts across different
 * device models, generations, and even brands.
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  PARTS_MATCHING_KV: KVNamespace;
  D1_DATABASE: D1Database;
  R2_BUCKET: R2Bucket;
  AI: Ai;
  VECTORIZE: VectorizeIndex;
  INVENTORY_SERVICE: Fetcher;
  EBAY_SNIPER_SERVICE: Fetcher;
  PRICING_SERVICE: Fetcher;
}

interface Part {
  part_id: string;
  part_number: string;
  name: string;
  description: string;
  category: PartCategory;
  manufacturer: string;
  compatible_devices: string[];
  specifications: Record<string, any>;
  form_factor: FormFactor;
  connector_types: string[];
  voltage_rating?: string;
  dimensions?: Dimensions;
  weight_grams?: number;
  oem_alternatives: string[];
  aftermarket_alternatives: string[];
  embedding_vector?: number[];
  confidence_score: number;
}

interface PartCategory {
  primary: string;
  secondary: string;
  tertiary?: string;
}

interface FormFactor {
  type: string;
  mounting: string;
  orientation?: string;
}

interface Dimensions {
  length_mm: number;
  width_mm: number;
  height_mm: number;
  tolerance_mm: number;
}

interface CompatibilityMatch {
  source_part: Part;
  matched_part: Part;
  compatibility_score: number;
  match_type: 'exact' | 'equivalent' | 'compatible' | 'partial' | 'risky';
  match_factors: MatchFactor[];
  warnings: string[];
  recommendation: string;
  price_comparison?: PriceComparison;
}

interface MatchFactor {
  factor: string;
  source_value: any;
  match_value: any;
  score: number;
  weight: number;
}

interface PriceComparison {
  source_price: number;
  match_price: number;
  savings: number;
  savings_percentage: number;
}

interface CrossReferenceEntry {
  part_number: string;
  manufacturer: string;
  cross_references: CrossReference[];
  verified: boolean;
  last_verified: string;
}

interface CrossReference {
  ref_part_number: string;
  ref_manufacturer: string;
  compatibility_type: 'direct' | 'functional' | 'upgrade' | 'downgrade';
  notes: string;
  verified_by: string;
}

interface DevicePartMatrix {
  device_id: string;
  device_model: string;
  parts_required: {
    part_category: string;
    original_part: string;
    compatible_parts: CompatibilityMatch[];
  }[];
}

interface SearchResult {
  parts: CompatibilityMatch[];
  total_found: number;
  search_strategy: string;
  search_time_ms: number;
  suggestions: string[];
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// Part category embeddings configuration
const CATEGORY_WEIGHTS: Record<string, number> = {
  'battery': 0.95,
  'display': 0.98,
  'charging_port': 0.90,
  'flex_cable': 0.85,
  'speaker': 0.88,
  'camera': 0.95,
  'motherboard': 0.99,
  'housing': 0.70,
  'button': 0.80,
  'sensor': 0.92,
  'antenna': 0.90,
  'connector': 0.85,
};

// Specification importance for matching
const SPEC_IMPORTANCE: Record<string, number> = {
  'voltage': 1.0,
  'amperage': 0.95,
  'capacity_mah': 0.90,
  'resolution': 0.95,
  'connector_type': 1.0,
  'pin_count': 1.0,
  'frequency': 0.85,
  'impedance': 0.80,
  'dimensions': 0.75,
};

// ==================== Part Registration ====================

app.post('/parts/register', async (c) => {
  const part: Part = await c.req.json();

  // Generate text description for embedding
  const textForEmbedding = generatePartDescription(part);

  // Generate embedding using AI
  const embeddingResponse = await c.env.AI.run('@cf/baai/bge-base-en-v1.5', {
    text: textForEmbedding,
  });

  part.embedding_vector = embeddingResponse.data[0];

  // Store in Vectorize
  await c.env.VECTORIZE.upsert([{
    id: part.part_id,
    values: part.embedding_vector,
    metadata: {
      part_number: part.part_number,
      name: part.name,
      category: part.category.primary,
      manufacturer: part.manufacturer,
      devices: part.compatible_devices.join(','),
    },
  }]);

  // Store full part data in D1
  await c.env.D1_DATABASE.prepare(`
    INSERT OR REPLACE INTO parts (
      id, part_number, name, description, category, manufacturer,
      compatible_devices, specifications, form_factor, connector_types,
      embedding_vector, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
  `).bind(
    part.part_id,
    part.part_number,
    part.name,
    part.description,
    JSON.stringify(part.category),
    part.manufacturer,
    JSON.stringify(part.compatible_devices),
    JSON.stringify(part.specifications),
    JSON.stringify(part.form_factor),
    JSON.stringify(part.connector_types),
    JSON.stringify(part.embedding_vector)
  ).run();

  return c.json({
    success: true,
    part_id: part.part_id,
    embedding_dimensions: part.embedding_vector.length,
    indexed: true,
  });
});

// ==================== Find Compatible Parts ====================

app.post('/parts/find-compatible', async (c) => {
  const { part_number, manufacturer, device_model, category, min_score = 0.7 } = await c.req.json();
  const startTime = Date.now();

  // First, get the source part
  let sourcePart: Part | null = null;

  if (part_number) {
    const result = await c.env.D1_DATABASE.prepare(`
      SELECT * FROM parts WHERE part_number = ? AND manufacturer = ?
    `).bind(part_number, manufacturer || '').first();

    if (result) {
      sourcePart = {
        part_id: result.id as string,
        part_number: result.part_number as string,
        name: result.name as string,
        description: result.description as string,
        category: JSON.parse(result.category as string),
        manufacturer: result.manufacturer as string,
        compatible_devices: JSON.parse(result.compatible_devices as string),
        specifications: JSON.parse(result.specifications as string),
        form_factor: JSON.parse(result.form_factor as string),
        connector_types: JSON.parse(result.connector_types as string),
        oem_alternatives: [],
        aftermarket_alternatives: [],
        embedding_vector: JSON.parse(result.embedding_vector as string),
        confidence_score: 1.0,
      };
    }
  }

  if (!sourcePart) {
    // Create a synthetic part from the query for embedding search
    const queryText = `${category || ''} ${part_number || ''} for ${device_model || ''} ${manufacturer || ''}`.trim();

    const embeddingResponse = await c.env.AI.run('@cf/baai/bge-base-en-v1.5', {
      text: queryText,
    });

    // Search by embedding
    const vectorResults = await c.env.VECTORIZE.query(embeddingResponse.data[0], {
      topK: 20,
      filter: category ? { category: { $eq: category } } : undefined,
      returnMetadata: true,
    });

    const matches = await Promise.all(
      vectorResults.matches.map(async (match) => {
        const partData = await c.env.D1_DATABASE.prepare(`
          SELECT * FROM parts WHERE id = ?
        `).bind(match.id).first();

        if (!partData) return null;

        const matchedPart = parsePart(partData);
        return {
          source_part: { part_number, category, device_model } as any,
          matched_part: matchedPart,
          compatibility_score: match.score || 0,
          match_type: getMatchType(match.score || 0),
          match_factors: [],
          warnings: [],
          recommendation: getRecommendation(match.score || 0),
        };
      })
    );

    return c.json({
      parts: matches.filter(m => m && m.compatibility_score >= min_score),
      total_found: matches.filter(m => m).length,
      search_strategy: 'semantic_embedding',
      search_time_ms: Date.now() - startTime,
      suggestions: ['Register the part for better matching accuracy'],
    });
  }

  // Search using vector similarity
  const vectorResults = await c.env.VECTORIZE.query(sourcePart.embedding_vector!, {
    topK: 50,
    filter: { category: { $eq: sourcePart.category.primary } },
    returnMetadata: true,
  });

  // Score and rank matches
  const matches: CompatibilityMatch[] = [];

  for (const result of vectorResults.matches) {
    if (result.id === sourcePart.part_id) continue; // Skip self

    const partData = await c.env.D1_DATABASE.prepare(`
      SELECT * FROM parts WHERE id = ?
    `).bind(result.id).first();

    if (!partData) continue;

    const matchedPart = parsePart(partData);
    const detailedScore = calculateDetailedCompatibility(sourcePart, matchedPart);

    if (detailedScore.score >= min_score) {
      // Get price comparison
      const priceComparison = await getPriceComparison(c.env, sourcePart, matchedPart);

      matches.push({
        source_part: sourcePart,
        matched_part: matchedPart,
        compatibility_score: detailedScore.score,
        match_type: getMatchType(detailedScore.score),
        match_factors: detailedScore.factors,
        warnings: detailedScore.warnings,
        recommendation: getRecommendation(detailedScore.score),
        price_comparison: priceComparison,
      });
    }
  }

  // Sort by compatibility score
  matches.sort((a, b) => b.compatibility_score - a.compatibility_score);

  return c.json({
    parts: matches.slice(0, 20),
    total_found: matches.length,
    search_strategy: 'vector_with_spec_validation',
    search_time_ms: Date.now() - startTime,
    suggestions: generateSearchSuggestions(matches),
  });
});

// ==================== Cross-Reference Lookup ====================

app.get('/cross-reference/:partNumber', async (c) => {
  const partNumber = c.req.param('partNumber');

  // Check cache first
  const cached = await c.env.PARTS_MATCHING_KV.get(`xref:${partNumber}`);
  if (cached) {
    return c.json(JSON.parse(cached));
  }

  // Search D1 for cross-references
  const crossRefs = await c.env.D1_DATABASE.prepare(`
    SELECT * FROM cross_references WHERE part_number = ? OR ref_part_number = ?
  `).bind(partNumber, partNumber).all();

  // Also search for semantic matches
  const partData = await c.env.D1_DATABASE.prepare(`
    SELECT * FROM parts WHERE part_number = ?
  `).bind(partNumber).first();

  let semanticMatches: any[] = [];

  if (partData && partData.embedding_vector) {
    const embedding = JSON.parse(partData.embedding_vector as string);
    const vectorResults = await c.env.VECTORIZE.query(embedding, {
      topK: 10,
      returnMetadata: true,
    });

    semanticMatches = vectorResults.matches
      .filter(m => m.score && m.score > 0.85 && m.id !== partData.id)
      .map(m => ({
        part_number: m.metadata?.part_number,
        manufacturer: m.metadata?.manufacturer,
        similarity: m.score,
        type: 'semantic_match',
      }));
  }

  const result = {
    part_number: partNumber,
    direct_cross_references: crossRefs.results,
    semantic_matches: semanticMatches,
    total_alternatives: (crossRefs.results?.length || 0) + semanticMatches.length,
  };

  // Cache for 1 hour
  await c.env.PARTS_MATCHING_KV.put(`xref:${partNumber}`, JSON.stringify(result), { expirationTtl: 3600 });

  return c.json(result);
});

// ==================== Device Part Matrix ====================

app.post('/device/part-matrix', async (c) => {
  const { device_model, repair_type } = await c.req.json();

  // Get all parts for this device model
  const deviceParts = await c.env.D1_DATABASE.prepare(`
    SELECT * FROM parts 
    WHERE compatible_devices LIKE ? 
    ${repair_type ? "AND category LIKE ?" : ""}
    ORDER BY category
  `).bind(
    `%${device_model}%`,
    repair_type ? `%${repair_type}%` : null
  ).all();

  // Build compatibility matrix
  const matrix: DevicePartMatrix = {
    device_id: device_model,
    device_model: device_model,
    parts_required: [],
  };

  const categorizedParts = new Map<string, Part[]>();

  for (const partData of deviceParts.results || []) {
    const part = parsePart(partData);
    const category = part.category.primary;

    if (!categorizedParts.has(category)) {
      categorizedParts.set(category, []);
    }
    categorizedParts.get(category)!.push(part);
  }

  for (const [category, parts] of categorizedParts) {
    const originalPart = parts.find(p => p.manufacturer.toLowerCase().includes('apple') || p.manufacturer.toLowerCase().includes('oem'));

    if (originalPart) {
      const compatibleParts = await findCompatibleForMatrix(c.env, originalPart, parts);

      matrix.parts_required.push({
        part_category: category,
        original_part: originalPart.part_number,
        compatible_parts: compatibleParts,
      });
    }
  }

  return c.json(matrix);
});

// ==================== Bulk Compatibility Check ====================

app.post('/parts/bulk-check', async (c) => {
  const { parts } = await c.req.json();

  const results = await Promise.all(
    parts.map(async (partQuery: any) => {
      try {
        const response = await c.env.fetch(new Request('https://internal/parts/find-compatible', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(partQuery),
        }));

        return {
          query: partQuery,
          result: await response.json(),
          status: 'success',
        };
      } catch (error) {
        return {
          query: partQuery,
          error: String(error),
          status: 'error',
        };
      }
    })
  );

  return c.json({
    total_queries: parts.length,
    successful: results.filter(r => r.status === 'success').length,
    failed: results.filter(r => r.status === 'error').length,
    results,
  });
});

// ==================== AI-Powered Part Identification ====================

app.post('/parts/identify', async (c) => {
  const { description, image_url, context } = await c.req.json();

  // Use AI to extract part details from description
  const aiResponse = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: `You are an expert electronics parts identifier. Extract structured part information from descriptions.
Return JSON with: { part_type, likely_manufacturer, key_specs: [], probable_part_numbers: [], device_compatibility: [] }`,
      },
      {
        role: 'user',
        content: `Identify this part: "${description}"${context ? `\nContext: ${context}` : ''}`,
      },
    ],
  });

  let parsedIdentification;
  try {
    const responseText = (aiResponse as any).response || '';
    const jsonMatch = responseText.match(/\{[\s\S]*\}/);
    parsedIdentification = jsonMatch ? JSON.parse(jsonMatch[0]) : { raw: responseText };
  } catch {
    parsedIdentification = { raw_response: aiResponse };
  }

  // Search for matching parts based on AI identification
  const searchQueries = [
    parsedIdentification.part_type,
    ...(parsedIdentification.probable_part_numbers || []),
    ...(parsedIdentification.device_compatibility || []),
  ].filter(Boolean);

  const searchResults = [];

  for (const query of searchQueries.slice(0, 3)) {
    const embeddingResponse = await c.env.AI.run('@cf/baai/bge-base-en-v1.5', {
      text: query,
    });

    const vectorResults = await c.env.VECTORIZE.query(embeddingResponse.data[0], {
      topK: 5,
      returnMetadata: true,
    });

    searchResults.push({
      query,
      matches: vectorResults.matches,
    });
  }

  return c.json({
    identification: parsedIdentification,
    search_results: searchResults,
    confidence: parsedIdentification.probable_part_numbers?.length > 0 ? 0.8 : 0.5,
  });
});

// ==================== Price Optimization ====================

app.post('/parts/optimize-price', async (c) => {
  const { part_number, manufacturer, quantity = 1 } = await c.req.json();

  // Find compatible parts
  const compatibleResponse = await c.env.fetch(new Request('https://internal/parts/find-compatible', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ part_number, manufacturer, min_score: 0.8 }),
  }));

  const compatibleParts: SearchResult = await compatibleResponse.json();

  // Get pricing for each compatible part
  const pricedAlternatives = await Promise.all(
    compatibleParts.parts.slice(0, 10).map(async (match) => {
      const pricingResponse = await c.env.PRICING_SERVICE.fetch(new Request('https://pricing/quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          part_number: match.matched_part.part_number,
          quantity,
        }),
      }));

      const pricing = await pricingResponse.json() as any;

      // Also check eBay for deals
      const ebayResponse = await c.env.EBAY_SNIPER_SERVICE.fetch(new Request('https://ebay/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          keywords: `${match.matched_part.part_number} ${match.matched_part.name}`,
          max_results: 5,
        }),
      }));

      const ebayResults = await ebayResponse.json() as any;

      return {
        part: match.matched_part,
        compatibility_score: match.compatibility_score,
        match_type: match.match_type,
        standard_price: pricing.unit_price || 0,
        ebay_best_price: ebayResults.listings?.[0]?.price || null,
        total_cost: (pricing.unit_price || 0) * quantity,
        availability: pricing.availability || 'unknown',
      };
    })
  );

  // Sort by total cost
  pricedAlternatives.sort((a, b) => a.total_cost - b.total_cost);

  const originalPrice = pricedAlternatives[0]?.standard_price || 0;
  const bestPrice = pricedAlternatives.reduce((min, p) => Math.min(min, p.standard_price || Infinity), Infinity);

  return c.json({
    original_part: part_number,
    quantity,
    alternatives: pricedAlternatives,
    best_value: pricedAlternatives[0],
    potential_savings: {
      per_unit: originalPrice - bestPrice,
      total: (originalPrice - bestPrice) * quantity,
      percentage: originalPrice > 0 ? ((originalPrice - bestPrice) / originalPrice) * 100 : 0,
    },
    recommendation: generatePriceRecommendation(pricedAlternatives),
  });
});

// ==================== Similarity Learning ====================

app.post('/parts/learn-similarity', async (c) => {
  const { part_a, part_b, is_compatible, technician_id, notes } = await c.req.json();

  // Store the feedback for model improvement
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO similarity_feedback (
      part_a, part_b, is_compatible, technician_id, notes, created_at
    ) VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(part_a, part_b, is_compatible ? 1 : 0, technician_id, notes).run();

  // Update cross-reference table if compatible
  if (is_compatible) {
    await c.env.D1_DATABASE.prepare(`
      INSERT OR REPLACE INTO cross_references (
        part_number, ref_part_number, compatibility_type, verified_by, verified_at
      ) VALUES (?, ?, 'functional', ?, datetime('now'))
    `).bind(part_a, part_b, technician_id).run();
  }

  // Invalidate cached cross-references
  await c.env.PARTS_MATCHING_KV.delete(`xref:${part_a}`);
  await c.env.PARTS_MATCHING_KV.delete(`xref:${part_b}`);

  return c.json({
    success: true,
    message: 'Feedback recorded - model will improve with more data',
    feedback_count: await getFeedbackCount(c.env),
  });
});

// ==================== Stats & Analytics ====================

app.get('/stats', async (c) => {
  const [totalParts, totalCrossRefs, totalFeedback, recentMatches] = await Promise.all([
    c.env.D1_DATABASE.prepare('SELECT COUNT(*) as count FROM parts').first(),
    c.env.D1_DATABASE.prepare('SELECT COUNT(*) as count FROM cross_references').first(),
    c.env.D1_DATABASE.prepare('SELECT COUNT(*) as count FROM similarity_feedback').first(),
    c.env.D1_DATABASE.prepare(`
      SELECT COUNT(*) as count FROM match_logs 
      WHERE created_at > datetime('now', '-24 hours')
    `).first(),
  ]);

  return c.json({
    total_parts_indexed: totalParts?.count || 0,
    total_cross_references: totalCrossRefs?.count || 0,
    total_feedback_entries: totalFeedback?.count || 0,
    matches_last_24h: recentMatches?.count || 0,
    embedding_model: '@cf/baai/bge-base-en-v1.5',
    matching_algorithm: 'hybrid_vector_spec',
  });
});

// ==================== Helper Functions ====================

function generatePartDescription(part: Part): string {
  const specs = Object.entries(part.specifications || {})
    .map(([k, v]) => `${k}: ${v}`)
    .join(', ');

  return `${part.name} ${part.part_number} ${part.category.primary} ${part.category.secondary || ''} 
    manufacturer: ${part.manufacturer} 
    devices: ${part.compatible_devices.join(', ')} 
    connectors: ${part.connector_types.join(', ')} 
    specs: ${specs}
    form factor: ${part.form_factor?.type || ''} ${part.form_factor?.mounting || ''}`.trim();
}

function parsePart(data: any): Part {
  return {
    part_id: data.id,
    part_number: data.part_number,
    name: data.name,
    description: data.description,
    category: JSON.parse(data.category || '{}'),
    manufacturer: data.manufacturer,
    compatible_devices: JSON.parse(data.compatible_devices || '[]'),
    specifications: JSON.parse(data.specifications || '{}'),
    form_factor: JSON.parse(data.form_factor || '{}'),
    connector_types: JSON.parse(data.connector_types || '[]'),
    oem_alternatives: JSON.parse(data.oem_alternatives || '[]'),
    aftermarket_alternatives: JSON.parse(data.aftermarket_alternatives || '[]'),
    embedding_vector: data.embedding_vector ? JSON.parse(data.embedding_vector) : undefined,
    confidence_score: data.confidence_score || 1.0,
  };
}

function calculateDetailedCompatibility(source: Part, target: Part): {
  score: number;
  factors: MatchFactor[];
  warnings: string[];
} {
  const factors: MatchFactor[] = [];
  const warnings: string[] = [];

  // Category match
  const categoryMatch = source.category.primary === target.category.primary;
  factors.push({
    factor: 'category',
    source_value: source.category.primary,
    match_value: target.category.primary,
    score: categoryMatch ? 1.0 : 0.3,
    weight: CATEGORY_WEIGHTS[source.category.primary] || 0.8,
  });

  if (!categoryMatch) {
    warnings.push(`Different primary category: ${source.category.primary} vs ${target.category.primary}`);
  }

  // Connector compatibility
  const connectorOverlap = source.connector_types.filter(c => target.connector_types.includes(c));
  const connectorScore = source.connector_types.length > 0
    ? connectorOverlap.length / source.connector_types.length
    : 0.5;

  factors.push({
    factor: 'connector_types',
    source_value: source.connector_types,
    match_value: target.connector_types,
    score: connectorScore,
    weight: SPEC_IMPORTANCE.connector_type,
  });

  if (connectorScore < 1.0) {
    warnings.push('Not all connectors match - physical fit may differ');
  }

  // Specification comparison
  for (const [spec, importance] of Object.entries(SPEC_IMPORTANCE)) {
    const sourceSpec = source.specifications[spec];
    const targetSpec = target.specifications[spec];

    if (sourceSpec !== undefined && targetSpec !== undefined) {
      const specScore = compareSpecification(spec, sourceSpec, targetSpec);
      factors.push({
        factor: spec,
        source_value: sourceSpec,
        match_value: targetSpec,
        score: specScore,
        weight: importance,
      });

      if (specScore < 0.9 && importance > 0.9) {
        warnings.push(`Critical spec mismatch in ${spec}: ${sourceSpec} vs ${targetSpec}`);
      }
    }
  }

  // Device compatibility overlap
  const deviceOverlap = source.compatible_devices.filter(d =>
    target.compatible_devices.some(td => td.toLowerCase().includes(d.toLowerCase()) || d.toLowerCase().includes(td.toLowerCase()))
  );

  factors.push({
    factor: 'device_compatibility',
    source_value: source.compatible_devices.length,
    match_value: deviceOverlap.length,
    score: source.compatible_devices.length > 0 ? deviceOverlap.length / source.compatible_devices.length : 0,
    weight: 0.7,
  });

  // Calculate weighted average score
  const totalWeight = factors.reduce((sum, f) => sum + f.weight, 0);
  const weightedSum = factors.reduce((sum, f) => sum + f.score * f.weight, 0);
  const finalScore = totalWeight > 0 ? weightedSum / totalWeight : 0;

  return { score: finalScore, factors, warnings };
}

function compareSpecification(spec: string, sourceValue: any, targetValue: any): number {
  // Handle numeric comparisons
  if (typeof sourceValue === 'number' && typeof targetValue === 'number') {
    const ratio = Math.min(sourceValue, targetValue) / Math.max(sourceValue, targetValue);
    return ratio;
  }

  // Handle string comparisons
  if (typeof sourceValue === 'string' && typeof targetValue === 'string') {
    // Extract numeric values if present
    const sourceNum = parseFloat(sourceValue.replace(/[^\d.]/g, ''));
    const targetNum = parseFloat(targetValue.replace(/[^\d.]/g, ''));

    if (!isNaN(sourceNum) && !isNaN(targetNum)) {
      const ratio = Math.min(sourceNum, targetNum) / Math.max(sourceNum, targetNum);
      return ratio > 0.95 ? 1.0 : ratio;
    }

    // Exact string match
    return sourceValue.toLowerCase() === targetValue.toLowerCase() ? 1.0 : 0.5;
  }

  return 0.5; // Unknown comparison
}

function getMatchType(score: number): 'exact' | 'equivalent' | 'compatible' | 'partial' | 'risky' {
  if (score >= 0.98) return 'exact';
  if (score >= 0.90) return 'equivalent';
  if (score >= 0.80) return 'compatible';
  if (score >= 0.70) return 'partial';
  return 'risky';
}

function getRecommendation(score: number): string {
  if (score >= 0.98) return 'Perfect match - direct replacement';
  if (score >= 0.90) return 'Excellent alternative - functionally equivalent';
  if (score >= 0.80) return 'Good alternative - minor differences acceptable';
  if (score >= 0.70) return 'Usable with caution - verify fit before install';
  return 'Not recommended - significant compatibility concerns';
}

function generateSearchSuggestions(matches: CompatibilityMatch[]): string[] {
  const suggestions: string[] = [];

  if (matches.length === 0) {
    suggestions.push('Try broader search terms or different category');
    suggestions.push('Register part to improve future matching');
  } else if (matches.every(m => m.compatibility_score < 0.85)) {
    suggestions.push('No high-confidence matches found');
    suggestions.push('Consider OEM part for best compatibility');
  } else if (matches.some(m => m.warnings.length > 0)) {
    suggestions.push('Review warnings before selecting alternative');
  }

  return suggestions;
}

async function getPriceComparison(env: Env, source: Part, match: Part): Promise<PriceComparison | undefined> {
  try {
    const [sourcePrice, matchPrice] = await Promise.all([
      env.PRICING_SERVICE.fetch(new Request('https://pricing/quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ part_number: source.part_number }),
      })).then(r => r.json()),
      env.PRICING_SERVICE.fetch(new Request('https://pricing/quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ part_number: match.part_number }),
      })).then(r => r.json()),
    ]) as any[];

    const sp = sourcePrice.unit_price || 0;
    const mp = matchPrice.unit_price || 0;

    return {
      source_price: sp,
      match_price: mp,
      savings: sp - mp,
      savings_percentage: sp > 0 ? ((sp - mp) / sp) * 100 : 0,
    };
  } catch {
    return undefined;
  }
}

async function findCompatibleForMatrix(env: Env, original: Part, allParts: Part[]): Promise<CompatibilityMatch[]> {
  const matches: CompatibilityMatch[] = [];

  for (const part of allParts) {
    if (part.part_id === original.part_id) continue;

    const { score, factors, warnings } = calculateDetailedCompatibility(original, part);

    if (score >= 0.7) {
      matches.push({
        source_part: original,
        matched_part: part,
        compatibility_score: score,
        match_type: getMatchType(score),
        match_factors: factors,
        warnings,
        recommendation: getRecommendation(score),
      });
    }
  }

  return matches.sort((a, b) => b.compatibility_score - a.compatibility_score);
}

function generatePriceRecommendation(alternatives: any[]): string {
  if (alternatives.length === 0) return 'No alternatives found';

  const best = alternatives[0];
  if (best.compatibility_score >= 0.95) {
    return `Best value: ${best.part.part_number} at $${best.standard_price.toFixed(2)} with ${Math.round(best.compatibility_score * 100)}% compatibility`;
  }

  const highCompat = alternatives.find(a => a.compatibility_score >= 0.95);
  if (highCompat) {
    return `For highest compatibility, consider ${highCompat.part.part_number} at $${highCompat.standard_price.toFixed(2)}`;
  }

  return `Lowest price option: ${best.part.part_number} - verify compatibility before purchase`;
}

async function getFeedbackCount(env: Env): Promise<number> {
  const result = await env.D1_DATABASE.prepare('SELECT COUNT(*) as count FROM similarity_feedback').first();
  return (result?.count as number) || 0;
}

export default app;
