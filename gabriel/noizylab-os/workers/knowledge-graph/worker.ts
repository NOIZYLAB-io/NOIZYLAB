/**
 * NoizyLab OS - Knowledge Graph Worker
 * 🕸️ Neo4j-Style Repair Knowledge Network
 * 
 * A graph-based knowledge system that connects devices, components,
 * symptoms, repairs, technicians, and outcomes into a queryable
 * network for intelligent repair recommendations.
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  KNOWLEDGE_GRAPH_KV: KVNamespace;
  D1_DATABASE: D1Database;
  R2_BUCKET: R2Bucket;
  AI: Ai;
  BRAIN_SERVICE: Fetcher;
  ANALYTICS_SERVICE: Fetcher;
}

// Graph Node Types
type NodeType = 'Device' | 'Component' | 'Symptom' | 'Repair' | 'Technician' | 'Tool' | 'Part' | 'Solution' | 'Cause' | 'Model' | 'Brand';

interface GraphNode {
  id: string;
  type: NodeType;
  label: string;
  properties: Record<string, any>;
  created_at: string;
  updated_at: string;
  embedding?: number[];
}

// Edge Types for relationships
type EdgeType =
  | 'HAS_COMPONENT'
  | 'EXHIBITS_SYMPTOM'
  | 'REPAIRED_BY'
  | 'USES_PART'
  | 'REQUIRES_TOOL'
  | 'CAUSES'
  | 'RESOLVES'
  | 'SIMILAR_TO'
  | 'PERFORMED_BY'
  | 'BELONGS_TO'
  | 'LEADS_TO'
  | 'PREVENTED_BY'
  | 'RELATED_TO'
  | 'IS_MODEL_OF'
  | 'MADE_BY';

interface GraphEdge {
  id: string;
  source_id: string;
  target_id: string;
  type: EdgeType;
  properties: Record<string, any>;
  weight: number;
  confidence: number;
  created_at: string;
}

interface GraphQuery {
  start_node?: string;
  node_type?: NodeType;
  edge_types?: EdgeType[];
  max_depth?: number;
  limit?: number;
  filters?: Record<string, any>;
}

interface GraphPath {
  nodes: GraphNode[];
  edges: GraphEdge[];
  total_weight: number;
  confidence: number;
}

interface GraphTraversal {
  paths: GraphPath[];
  visited_nodes: number;
  query_time_ms: number;
}

interface RecommendationQuery {
  symptoms: string[];
  device_model?: string;
  component?: string;
  context?: string;
}

interface RepairRecommendation {
  repair_type: string;
  confidence: number;
  supporting_evidence: GraphPath[];
  required_parts: string[];
  required_tools: string[];
  estimated_time: string;
  success_rate: number;
  related_solutions: string[];
}

interface KnowledgeInsight {
  insight_type: string;
  description: string;
  supporting_data: any;
  confidence: number;
  actionable: boolean;
}

interface GraphStats {
  total_nodes: number;
  total_edges: number;
  nodes_by_type: Record<NodeType, number>;
  edges_by_type: Record<EdgeType, number>;
  most_connected_nodes: { id: string; connections: number }[];
  graph_density: number;
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// ==================== Node Management ====================

app.post('/nodes', async (c) => {
  const node: Omit<GraphNode, 'id' | 'created_at' | 'updated_at'> = await c.req.json();

  const nodeId = `${node.type.toLowerCase()}-${Date.now()}-${Math.random().toString(36).substring(7)}`;

  // Generate embedding for semantic search
  let embedding: number[] | undefined;
  if (node.label && node.properties) {
    const textForEmbedding = `${node.type} ${node.label} ${JSON.stringify(node.properties)}`;
    const embeddingResponse = await c.env.AI.run('@cf/baai/bge-base-en-v1.5', {
      text: textForEmbedding,
    });
    embedding = embeddingResponse.data[0];
  }

  const fullNode: GraphNode = {
    id: nodeId,
    ...node,
    embedding,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  };

  // Store in D1
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO graph_nodes (id, type, label, properties, embedding, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'), datetime('now'))
  `).bind(nodeId, node.type, node.label, JSON.stringify(node.properties), JSON.stringify(embedding)).run();

  // Cache adjacency list
  await updateAdjacencyCache(c.env, nodeId, []);

  return c.json({ success: true, node: fullNode });
});

app.get('/nodes/:id', async (c) => {
  const nodeId = c.req.param('id');

  const result = await c.env.D1_DATABASE.prepare(`
    SELECT * FROM graph_nodes WHERE id = ?
  `).bind(nodeId).first();

  if (!result) {
    return c.json({ error: 'Node not found' }, 404);
  }

  return c.json(parseNode(result));
});

app.get('/nodes', async (c) => {
  const type = c.req.query('type') as NodeType | undefined;
  const label = c.req.query('label');
  const limit = parseInt(c.req.query('limit') || '100');

  let query = 'SELECT * FROM graph_nodes WHERE 1=1';
  const params: any[] = [];

  if (type) {
    query += ' AND type = ?';
    params.push(type);
  }

  if (label) {
    query += ' AND label LIKE ?';
    params.push(`%${label}%`);
  }

  query += ` LIMIT ${limit}`;

  const results = await c.env.D1_DATABASE.prepare(query).bind(...params).all();

  return c.json({
    nodes: (results.results || []).map(parseNode),
    total: results.results?.length || 0,
  });
});

// ==================== Edge Management ====================

app.post('/edges', async (c) => {
  const edge: Omit<GraphEdge, 'id' | 'created_at'> = await c.req.json();

  const edgeId = `edge-${Date.now()}-${Math.random().toString(36).substring(7)}`;

  const fullEdge: GraphEdge = {
    id: edgeId,
    ...edge,
    created_at: new Date().toISOString(),
  };

  // Verify source and target exist
  const [sourceNode, targetNode] = await Promise.all([
    c.env.D1_DATABASE.prepare('SELECT id FROM graph_nodes WHERE id = ?').bind(edge.source_id).first(),
    c.env.D1_DATABASE.prepare('SELECT id FROM graph_nodes WHERE id = ?').bind(edge.target_id).first(),
  ]);

  if (!sourceNode || !targetNode) {
    return c.json({ error: 'Source or target node not found' }, 400);
  }

  // Store edge
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO graph_edges (id, source_id, target_id, type, properties, weight, confidence, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(edgeId, edge.source_id, edge.target_id, edge.type, JSON.stringify(edge.properties), edge.weight, edge.confidence).run();

  // Update adjacency caches
  await updateAdjacencyForEdge(c.env, edge.source_id, edge.target_id, edgeId);

  return c.json({ success: true, edge: fullEdge });
});

app.get('/edges', async (c) => {
  const nodeId = c.req.query('node_id');
  const type = c.req.query('type') as EdgeType | undefined;

  let query = 'SELECT * FROM graph_edges WHERE 1=1';
  const params: any[] = [];

  if (nodeId) {
    query += ' AND (source_id = ? OR target_id = ?)';
    params.push(nodeId, nodeId);
  }

  if (type) {
    query += ' AND type = ?';
    params.push(type);
  }

  const results = await c.env.D1_DATABASE.prepare(query).bind(...params).all();

  return c.json({
    edges: (results.results || []).map(parseEdge),
    total: results.results?.length || 0,
  });
});

// ==================== Graph Traversal ====================

app.post('/traverse', async (c) => {
  const query: GraphQuery = await c.req.json();
  const startTime = Date.now();

  let visitedNodes = new Set<string>();
  const paths: GraphPath[] = [];

  // BFS traversal from start node
  if (query.start_node) {
    const traversalResult = await bfsTraverse(
      c.env,
      query.start_node,
      query.max_depth || 3,
      query.edge_types,
      query.filters
    );

    paths.push(...traversalResult.paths);
    visitedNodes = new Set(traversalResult.visited);
  }

  // Filter by node type if specified
  let filteredPaths = paths;
  if (query.node_type) {
    filteredPaths = paths.filter(p =>
      p.nodes.some(n => n.type === query.node_type)
    );
  }

  // Limit results
  const limitedPaths = filteredPaths.slice(0, query.limit || 50);

  return c.json({
    paths: limitedPaths,
    visited_nodes: visitedNodes.size,
    query_time_ms: Date.now() - startTime,
  });
});

// ==================== Path Finding ====================

app.post('/path', async (c) => {
  const { source_id, target_id, max_depth = 5 } = await c.req.json();

  const path = await findShortestPath(c.env, source_id, target_id, max_depth);

  if (!path) {
    return c.json({ error: 'No path found', source_id, target_id }, 404);
  }

  return c.json({ path });
});

// ==================== Semantic Search ====================

app.post('/search/semantic', async (c) => {
  const { query, node_types, limit = 20 } = await c.req.json();

  // Generate query embedding
  const embeddingResponse = await c.env.AI.run('@cf/baai/bge-base-en-v1.5', {
    text: query,
  });

  const queryEmbedding = embeddingResponse.data[0];

  // Search nodes by embedding similarity
  const allNodes = await c.env.D1_DATABASE.prepare(`
    SELECT * FROM graph_nodes 
    ${node_types ? `WHERE type IN (${node_types.map(() => '?').join(',')})` : ''}
    LIMIT 1000
  `).bind(...(node_types || [])).all();

  // Calculate cosine similarity for each node
  const scoredNodes = (allNodes.results || [])
    .map((row: any) => {
      const node = parseNode(row);
      if (!node.embedding) return null;

      const similarity = cosineSimilarity(queryEmbedding, node.embedding);
      return { node, similarity };
    })
    .filter((item): item is { node: GraphNode; similarity: number } => item !== null && item.similarity > 0.5)
    .sort((a, b) => b.similarity - a.similarity)
    .slice(0, limit);

  return c.json({
    query,
    results: scoredNodes,
    total: scoredNodes.length,
  });
});

// ==================== Repair Recommendations ====================

app.post('/recommend/repair', async (c) => {
  const query: RecommendationQuery = await c.req.json();

  const recommendations: RepairRecommendation[] = [];

  // Find symptom nodes
  const symptomNodes = await findNodesByLabels(c.env, 'Symptom', query.symptoms);

  // For each symptom, traverse to find solutions
  for (const symptomNode of symptomNodes) {
    // Find paths: Symptom -> CAUSED_BY -> Cause -> RESOLVED_BY -> Solution
    const causePaths = await traverseWithEdgeTypes(
      c.env,
      symptomNode.id,
      ['CAUSES', 'RESOLVES', 'REQUIRES_TOOL', 'USES_PART'],
      4
    );

    // Group by solution type
    const solutions = new Map<string, {
      paths: GraphPath[];
      parts: Set<string>;
      tools: Set<string>;
    }>();

    for (const path of causePaths.paths) {
      const solutionNode = path.nodes.find(n => n.type === 'Solution' || n.type === 'Repair');
      if (solutionNode) {
        const key = solutionNode.label;
        if (!solutions.has(key)) {
          solutions.set(key, { paths: [], parts: new Set(), tools: new Set() });
        }

        solutions.get(key)!.paths.push(path);

        // Collect parts and tools
        for (const node of path.nodes) {
          if (node.type === 'Part') solutions.get(key)!.parts.add(node.label);
          if (node.type === 'Tool') solutions.get(key)!.tools.add(node.label);
        }
      }
    }

    // Convert to recommendations
    for (const [repairType, data] of solutions) {
      const avgConfidence = data.paths.reduce((sum, p) => sum + p.confidence, 0) / data.paths.length;

      recommendations.push({
        repair_type: repairType,
        confidence: avgConfidence,
        supporting_evidence: data.paths.slice(0, 3),
        required_parts: Array.from(data.parts),
        required_tools: Array.from(data.tools),
        estimated_time: estimateRepairTime(repairType),
        success_rate: await getSuccessRate(c.env, repairType),
        related_solutions: await getRelatedSolutions(c.env, repairType),
      });
    }
  }

  // Use AI to enhance recommendations if needed
  if (recommendations.length === 0 && query.symptoms.length > 0) {
    const aiRecommendation = await getAIRecommendation(c.env, query);
    if (aiRecommendation) {
      recommendations.push(aiRecommendation);
    }
  }

  // Sort by confidence
  recommendations.sort((a, b) => b.confidence - a.confidence);

  return c.json({
    query,
    recommendations: recommendations.slice(0, 10),
    total_found: recommendations.length,
  });
});

// ==================== Knowledge Insights ====================

app.get('/insights', async (c) => {
  const insights: KnowledgeInsight[] = [];

  // Find frequently occurring symptom combinations
  const symptomClusters = await findSymptomClusters(c.env);
  for (const cluster of symptomClusters.slice(0, 3)) {
    insights.push({
      insight_type: 'symptom_pattern',
      description: `Symptoms "${cluster.symptoms.join('", "')}" frequently occur together`,
      supporting_data: cluster,
      confidence: cluster.confidence,
      actionable: true,
    });
  }

  // Find high-success repair patterns
  const successPatterns = await findHighSuccessPatterns(c.env);
  for (const pattern of successPatterns.slice(0, 3)) {
    insights.push({
      insight_type: 'success_pattern',
      description: `${pattern.repair_type} has ${Math.round(pattern.success_rate * 100)}% success rate when using ${pattern.key_factor}`,
      supporting_data: pattern,
      confidence: pattern.confidence,
      actionable: true,
    });
  }

  // Find emerging issues (new symptom-device combinations)
  const emergingIssues = await findEmergingIssues(c.env);
  for (const issue of emergingIssues.slice(0, 3)) {
    insights.push({
      insight_type: 'emerging_issue',
      description: `New pattern detected: ${issue.symptom} increasing in ${issue.device_model}`,
      supporting_data: issue,
      confidence: issue.confidence,
      actionable: true,
    });
  }

  return c.json({ insights });
});

// ==================== Knowledge Import ====================

app.post('/import/repair-data', async (c) => {
  const { repairs } = await c.req.json();

  let nodesCreated = 0;
  let edgesCreated = 0;

  for (const repair of repairs) {
    // Create or get device node
    const deviceNode = await findOrCreateNode(c.env, 'Device', repair.device_model, {
      model: repair.device_model,
      brand: extractBrand(repair.device_model),
    });

    // Create symptom nodes
    for (const symptom of repair.symptoms || []) {
      const symptomNode = await findOrCreateNode(c.env, 'Symptom', symptom, {
        description: symptom,
      });

      // Link device to symptom
      await createEdgeIfNotExists(c.env, deviceNode.id, symptomNode.id, 'EXHIBITS_SYMPTOM', {
        repair_id: repair.id,
        date: repair.date,
      });
      edgesCreated++;
    }

    // Create repair/solution node
    const repairNode = await findOrCreateNode(c.env, 'Repair', repair.repair_type, {
      type: repair.repair_type,
      outcome: repair.outcome,
    });

    // Link symptom to repair (solution)
    for (const symptom of repair.symptoms || []) {
      const symptomNode = await findOrCreateNode(c.env, 'Symptom', symptom, {});
      await createEdgeIfNotExists(c.env, symptomNode.id, repairNode.id, 'RESOLVES', {
        confidence: repair.outcome === 'success' ? 1.0 : 0.5,
      });
      edgesCreated++;
    }

    // Create part nodes
    for (const part of repair.parts_used || []) {
      const partNode = await findOrCreateNode(c.env, 'Part', part.name, {
        part_number: part.part_number,
      });

      await createEdgeIfNotExists(c.env, repairNode.id, partNode.id, 'USES_PART', {
        quantity: part.quantity || 1,
      });
      edgesCreated++;
    }

    // Create technician node
    if (repair.technician_id) {
      const techNode = await findOrCreateNode(c.env, 'Technician', repair.technician_name || repair.technician_id, {
        id: repair.technician_id,
      });

      await createEdgeIfNotExists(c.env, repairNode.id, techNode.id, 'PERFORMED_BY', {
        date: repair.date,
        outcome: repair.outcome,
      });
      edgesCreated++;
    }

    nodesCreated++;
  }

  return c.json({
    success: true,
    repairs_processed: repairs.length,
    nodes_created: nodesCreated,
    edges_created: edgesCreated,
  });
});

// ==================== Graph Statistics ====================

app.get('/stats', async (c) => {
  const [nodeStats, edgeStats, topConnected] = await Promise.all([
    c.env.D1_DATABASE.prepare(`
      SELECT type, COUNT(*) as count FROM graph_nodes GROUP BY type
    `).all(),
    c.env.D1_DATABASE.prepare(`
      SELECT type, COUNT(*) as count FROM graph_edges GROUP BY type
    `).all(),
    c.env.D1_DATABASE.prepare(`
      SELECT source_id as id, COUNT(*) as connections 
      FROM graph_edges 
      GROUP BY source_id 
      ORDER BY connections DESC 
      LIMIT 10
    `).all(),
  ]);

  const nodesByType: Record<string, number> = {};
  for (const row of nodeStats.results || []) {
    nodesByType[row.type as string] = row.count as number;
  }

  const edgesByType: Record<string, number> = {};
  for (const row of edgeStats.results || []) {
    edgesByType[row.type as string] = row.count as number;
  }

  const totalNodes = Object.values(nodesByType).reduce((a, b) => a + b, 0);
  const totalEdges = Object.values(edgesByType).reduce((a, b) => a + b, 0);

  // Graph density = 2E / (N * (N-1)) for undirected, E / (N * (N-1)) for directed
  const density = totalNodes > 1 ? totalEdges / (totalNodes * (totalNodes - 1)) : 0;

  return c.json({
    total_nodes: totalNodes,
    total_edges: totalEdges,
    nodes_by_type: nodesByType,
    edges_by_type: edgesByType,
    most_connected_nodes: (topConnected.results || []).map(row => ({
      id: row.id,
      connections: row.connections,
    })),
    graph_density: density,
  });
});

// ==================== Cypher-like Query ====================

app.post('/query/cypher', async (c) => {
  const { query } = await c.req.json();

  // Parse simple Cypher-like queries
  // MATCH (n:Symptom)-[:RESOLVES]->(r:Repair) WHERE n.label = 'no_power' RETURN r

  const parsed = parseCypherQuery(query);

  if (!parsed) {
    return c.json({ error: 'Could not parse query' }, 400);
  }

  const results = await executeCypherQuery(c.env, parsed);

  return c.json({
    query,
    results,
    count: results.length,
  });
});

// ==================== Visualization Data ====================

app.get('/visualize', async (c) => {
  const centerNode = c.req.query('center');
  const depth = parseInt(c.req.query('depth') || '2');

  let nodes: GraphNode[] = [];
  let edges: GraphEdge[] = [];

  if (centerNode) {
    // Get subgraph around center node
    const traversal = await bfsTraverse(c.env, centerNode, depth, undefined, undefined);
    const nodeIds = new Set<string>();

    for (const path of traversal.paths) {
      for (const node of path.nodes) {
        if (!nodeIds.has(node.id)) {
          nodeIds.add(node.id);
          nodes.push(node);
        }
      }
      edges.push(...path.edges);
    }
  } else {
    // Get most important nodes
    const importantNodes = await c.env.D1_DATABASE.prepare(`
      SELECT n.*, COUNT(e.id) as edge_count
      FROM graph_nodes n
      LEFT JOIN graph_edges e ON n.id = e.source_id OR n.id = e.target_id
      GROUP BY n.id
      ORDER BY edge_count DESC
      LIMIT 100
    `).all();

    nodes = (importantNodes.results || []).map(parseNode);

    // Get edges between these nodes
    const nodeIds = nodes.map(n => n.id);
    const edgeResults = await c.env.D1_DATABASE.prepare(`
      SELECT * FROM graph_edges 
      WHERE source_id IN (${nodeIds.map(() => '?').join(',')})
      AND target_id IN (${nodeIds.map(() => '?').join(',')})
    `).bind(...nodeIds, ...nodeIds).all();

    edges = (edgeResults.results || []).map(parseEdge);
  }

  // Format for visualization library (D3, Cytoscape, etc.)
  return c.json({
    nodes: nodes.map(n => ({
      id: n.id,
      label: n.label,
      type: n.type,
      properties: n.properties,
      // Visualization hints
      color: getNodeColor(n.type),
      size: 10,
    })),
    edges: edges.map(e => ({
      id: e.id,
      source: e.source_id,
      target: e.target_id,
      type: e.type,
      weight: e.weight,
      label: e.type,
    })),
    stats: {
      nodes: nodes.length,
      edges: edges.length,
    },
  });
});

// ==================== Helper Functions ====================

function parseNode(row: any): GraphNode {
  return {
    id: row.id,
    type: row.type as NodeType,
    label: row.label,
    properties: JSON.parse(row.properties || '{}'),
    created_at: row.created_at,
    updated_at: row.updated_at,
    embedding: row.embedding ? JSON.parse(row.embedding) : undefined,
  };
}

function parseEdge(row: any): GraphEdge {
  return {
    id: row.id,
    source_id: row.source_id,
    target_id: row.target_id,
    type: row.type as EdgeType,
    properties: JSON.parse(row.properties || '{}'),
    weight: row.weight,
    confidence: row.confidence,
    created_at: row.created_at,
  };
}

async function updateAdjacencyCache(env: Env, nodeId: string, neighbors: string[]): Promise<void> {
  await env.KNOWLEDGE_GRAPH_KV.put(`adj:${nodeId}`, JSON.stringify(neighbors), { expirationTtl: 3600 });
}

async function updateAdjacencyForEdge(env: Env, sourceId: string, targetId: string, edgeId: string): Promise<void> {
  // Update source's adjacency
  const sourceAdj = await env.KNOWLEDGE_GRAPH_KV.get(`adj:${sourceId}`);
  const sourceNeighbors = sourceAdj ? JSON.parse(sourceAdj) : [];
  if (!sourceNeighbors.includes(targetId)) {
    sourceNeighbors.push(targetId);
    await updateAdjacencyCache(env, sourceId, sourceNeighbors);
  }

  // Update target's adjacency (for undirected-like queries)
  const targetAdj = await env.KNOWLEDGE_GRAPH_KV.get(`adj:${targetId}`);
  const targetNeighbors = targetAdj ? JSON.parse(targetAdj) : [];
  if (!targetNeighbors.includes(sourceId)) {
    targetNeighbors.push(sourceId);
    await updateAdjacencyCache(env, targetId, targetNeighbors);
  }
}

async function bfsTraverse(
  env: Env,
  startId: string,
  maxDepth: number,
  edgeTypes?: EdgeType[],
  filters?: Record<string, any>
): Promise<{ paths: GraphPath[]; visited: string[] }> {
  const paths: GraphPath[] = [];
  const visited = new Set<string>();
  const queue: { nodeId: string; path: GraphPath; depth: number }[] = [];

  // Get start node
  const startNode = await env.D1_DATABASE.prepare('SELECT * FROM graph_nodes WHERE id = ?').bind(startId).first();
  if (!startNode) return { paths: [], visited: [] };

  const initialPath: GraphPath = {
    nodes: [parseNode(startNode)],
    edges: [],
    total_weight: 0,
    confidence: 1,
  };

  queue.push({ nodeId: startId, path: initialPath, depth: 0 });
  visited.add(startId);

  while (queue.length > 0) {
    const current = queue.shift()!;

    if (current.depth >= maxDepth) {
      paths.push(current.path);
      continue;
    }

    // Get edges from current node
    let edgeQuery = 'SELECT * FROM graph_edges WHERE source_id = ?';
    const params: any[] = [current.nodeId];

    if (edgeTypes && edgeTypes.length > 0) {
      edgeQuery += ` AND type IN (${edgeTypes.map(() => '?').join(',')})`;
      params.push(...edgeTypes);
    }

    const edges = await env.D1_DATABASE.prepare(edgeQuery).bind(...params).all();

    if (!edges.results || edges.results.length === 0) {
      paths.push(current.path);
      continue;
    }

    for (const edgeRow of edges.results) {
      const edge = parseEdge(edgeRow);

      if (!visited.has(edge.target_id)) {
        visited.add(edge.target_id);

        const targetNode = await env.D1_DATABASE.prepare('SELECT * FROM graph_nodes WHERE id = ?').bind(edge.target_id).first();
        if (targetNode) {
          const newPath: GraphPath = {
            nodes: [...current.path.nodes, parseNode(targetNode)],
            edges: [...current.path.edges, edge],
            total_weight: current.path.total_weight + edge.weight,
            confidence: current.path.confidence * edge.confidence,
          };

          queue.push({
            nodeId: edge.target_id,
            path: newPath,
            depth: current.depth + 1,
          });
        }
      }
    }
  }

  return { paths, visited: Array.from(visited) };
}

async function findShortestPath(env: Env, sourceId: string, targetId: string, maxDepth: number): Promise<GraphPath | null> {
  const visited = new Set<string>();
  const queue: { nodeId: string; path: GraphPath }[] = [];

  const startNode = await env.D1_DATABASE.prepare('SELECT * FROM graph_nodes WHERE id = ?').bind(sourceId).first();
  if (!startNode) return null;

  queue.push({
    nodeId: sourceId,
    path: { nodes: [parseNode(startNode)], edges: [], total_weight: 0, confidence: 1 },
  });
  visited.add(sourceId);

  while (queue.length > 0) {
    const current = queue.shift()!;

    if (current.nodeId === targetId) {
      return current.path;
    }

    if (current.path.nodes.length > maxDepth) continue;

    const edges = await env.D1_DATABASE.prepare(
      'SELECT * FROM graph_edges WHERE source_id = ?'
    ).bind(current.nodeId).all();

    for (const edgeRow of edges.results || []) {
      const edge = parseEdge(edgeRow);

      if (!visited.has(edge.target_id)) {
        visited.add(edge.target_id);

        const targetNode = await env.D1_DATABASE.prepare('SELECT * FROM graph_nodes WHERE id = ?').bind(edge.target_id).first();
        if (targetNode) {
          queue.push({
            nodeId: edge.target_id,
            path: {
              nodes: [...current.path.nodes, parseNode(targetNode)],
              edges: [...current.path.edges, edge],
              total_weight: current.path.total_weight + edge.weight,
              confidence: current.path.confidence * edge.confidence,
            },
          });
        }
      }
    }
  }

  return null;
}

function cosineSimilarity(a: number[], b: number[]): number {
  if (a.length !== b.length) return 0;

  let dotProduct = 0;
  let normA = 0;
  let normB = 0;

  for (let i = 0; i < a.length; i++) {
    dotProduct += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }

  const denominator = Math.sqrt(normA) * Math.sqrt(normB);
  return denominator === 0 ? 0 : dotProduct / denominator;
}

async function findNodesByLabels(env: Env, type: NodeType, labels: string[]): Promise<GraphNode[]> {
  if (labels.length === 0) return [];

  const placeholders = labels.map(() => '?').join(',');
  const results = await env.D1_DATABASE.prepare(`
    SELECT * FROM graph_nodes WHERE type = ? AND label IN (${placeholders})
  `).bind(type, ...labels).all();

  return (results.results || []).map(parseNode);
}

async function traverseWithEdgeTypes(
  env: Env,
  startId: string,
  edgeTypes: EdgeType[],
  maxDepth: number
): Promise<{ paths: GraphPath[] }> {
  return bfsTraverse(env, startId, maxDepth, edgeTypes, undefined);
}

function estimateRepairTime(repairType: string): string {
  const times: Record<string, string> = {
    'battery_replacement': '30-45 mins',
    'screen_replacement': '45-60 mins',
    'charging_port_repair': '45-60 mins',
    'motherboard_repair': '2-4 hours',
    'data_recovery': '1-24 hours',
  };

  for (const [key, time] of Object.entries(times)) {
    if (repairType.toLowerCase().includes(key.split('_')[0])) {
      return time;
    }
  }

  return '1-2 hours';
}

async function getSuccessRate(env: Env, repairType: string): Promise<number> {
  const result = await env.D1_DATABASE.prepare(`
    SELECT 
      COUNT(CASE WHEN json_extract(properties, '$.outcome') = 'success' THEN 1 END) * 1.0 / COUNT(*) as rate
    FROM graph_nodes 
    WHERE type = 'Repair' AND label LIKE ?
  `).bind(`%${repairType}%`).first();

  return (result?.rate as number) || 0.8;
}

async function getRelatedSolutions(env: Env, repairType: string): Promise<string[]> {
  const results = await env.D1_DATABASE.prepare(`
    SELECT DISTINCT target.label
    FROM graph_edges e
    JOIN graph_nodes source ON e.source_id = source.id
    JOIN graph_nodes target ON e.target_id = target.id
    WHERE source.label LIKE ? AND e.type = 'SIMILAR_TO' AND target.type = 'Repair'
    LIMIT 5
  `).bind(`%${repairType}%`).all();

  return (results.results || []).map((r: any) => r.label);
}

async function getAIRecommendation(env: Env, query: RecommendationQuery): Promise<RepairRecommendation | null> {
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'You are an expert electronics repair technician. Based on symptoms, recommend the most likely repair needed.',
      },
      {
        role: 'user',
        content: `Symptoms: ${query.symptoms.join(', ')}\nDevice: ${query.device_model || 'Unknown'}\nComponent: ${query.component || 'Unknown'}\n\nWhat repair is most likely needed? Provide a JSON response with: repair_type, confidence (0-1), required_parts (array), required_tools (array), estimated_time`,
      },
    ],
  });

  try {
    const responseText = (response as any).response || '';
    const jsonMatch = responseText.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      const parsed = JSON.parse(jsonMatch[0]);
      return {
        repair_type: parsed.repair_type || 'general_diagnosis',
        confidence: parsed.confidence || 0.5,
        supporting_evidence: [],
        required_parts: parsed.required_parts || [],
        required_tools: parsed.required_tools || [],
        estimated_time: parsed.estimated_time || '1-2 hours',
        success_rate: 0.7,
        related_solutions: [],
      };
    }
  } catch {
    // Parse failed
  }

  return null;
}

async function findSymptomClusters(env: Env): Promise<{ symptoms: string[]; confidence: number }[]> {
  // Find symptoms that frequently appear together
  const results = await env.D1_DATABASE.prepare(`
    SELECT e1.source_id, n1.label as symptom1, n2.label as symptom2, COUNT(*) as cooccurrence
    FROM graph_edges e1
    JOIN graph_edges e2 ON e1.source_id = e2.source_id AND e1.target_id < e2.target_id
    JOIN graph_nodes n1 ON e1.target_id = n1.id
    JOIN graph_nodes n2 ON e2.target_id = n2.id
    WHERE n1.type = 'Symptom' AND n2.type = 'Symptom'
    GROUP BY symptom1, symptom2
    HAVING cooccurrence > 2
    ORDER BY cooccurrence DESC
    LIMIT 10
  `).all();

  return (results.results || []).map((r: any) => ({
    symptoms: [r.symptom1, r.symptom2],
    confidence: Math.min(1, r.cooccurrence / 10),
  }));
}

async function findHighSuccessPatterns(env: Env): Promise<{ repair_type: string; success_rate: number; key_factor: string; confidence: number }[]> {
  // This would involve more complex graph analysis in production
  return [
    { repair_type: 'battery_replacement', success_rate: 0.95, key_factor: 'OEM parts', confidence: 0.9 },
    { repair_type: 'screen_replacement', success_rate: 0.92, key_factor: 'proper calibration', confidence: 0.85 },
  ];
}

async function findEmergingIssues(env: Env): Promise<{ symptom: string; device_model: string; confidence: number }[]> {
  // Detect new symptom patterns in recent data
  const results = await env.D1_DATABASE.prepare(`
    SELECT n.label as symptom, d.label as device_model, COUNT(*) as occurrences
    FROM graph_edges e
    JOIN graph_nodes n ON e.target_id = n.id
    JOIN graph_nodes d ON e.source_id = d.id
    WHERE n.type = 'Symptom' AND d.type = 'Device'
    AND e.created_at > datetime('now', '-30 days')
    GROUP BY n.label, d.label
    HAVING occurrences > 3
    ORDER BY occurrences DESC
    LIMIT 5
  `).all();

  return (results.results || []).map((r: any) => ({
    symptom: r.symptom,
    device_model: r.device_model,
    confidence: Math.min(1, r.occurrences / 10),
  }));
}

async function findOrCreateNode(env: Env, type: NodeType, label: string, properties: Record<string, any>): Promise<GraphNode> {
  // Check if node exists
  const existing = await env.D1_DATABASE.prepare(`
    SELECT * FROM graph_nodes WHERE type = ? AND label = ?
  `).bind(type, label).first();

  if (existing) {
    return parseNode(existing);
  }

  // Create new node
  const nodeId = `${type.toLowerCase()}-${Date.now()}-${Math.random().toString(36).substring(7)}`;

  await env.D1_DATABASE.prepare(`
    INSERT INTO graph_nodes (id, type, label, properties, created_at, updated_at)
    VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))
  `).bind(nodeId, type, label, JSON.stringify(properties)).run();

  return {
    id: nodeId,
    type,
    label,
    properties,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  };
}

async function createEdgeIfNotExists(
  env: Env,
  sourceId: string,
  targetId: string,
  type: EdgeType,
  properties: Record<string, any>
): Promise<void> {
  const existing = await env.D1_DATABASE.prepare(`
    SELECT id FROM graph_edges WHERE source_id = ? AND target_id = ? AND type = ?
  `).bind(sourceId, targetId, type).first();

  if (!existing) {
    const edgeId = `edge-${Date.now()}-${Math.random().toString(36).substring(7)}`;
    await env.D1_DATABASE.prepare(`
      INSERT INTO graph_edges (id, source_id, target_id, type, properties, weight, confidence, created_at)
      VALUES (?, ?, ?, ?, ?, 1.0, 0.8, datetime('now'))
    `).bind(edgeId, sourceId, targetId, type, JSON.stringify(properties)).run();
  }
}

function extractBrand(model: string): string {
  const brands = ['Apple', 'Samsung', 'Google', 'OnePlus', 'Xiaomi', 'Huawei', 'Sony', 'LG'];
  for (const brand of brands) {
    if (model.toLowerCase().includes(brand.toLowerCase())) {
      return brand;
    }
  }
  if (model.includes('iPhone') || model.includes('MacBook') || model.includes('iPad')) {
    return 'Apple';
  }
  return 'Unknown';
}

function parseCypherQuery(query: string): any | null {
  // Very simplified Cypher parser for demo
  const matchPattern = /MATCH\s+\((\w+):(\w+)\)/i;
  const wherePattern = /WHERE\s+(\w+)\.(\w+)\s*=\s*['"]([^'"]+)['"]/i;
  const returnPattern = /RETURN\s+(\w+)/i;

  const matchResult = query.match(matchPattern);
  const whereResult = query.match(wherePattern);
  const returnResult = query.match(returnPattern);

  if (!matchResult) return null;

  return {
    nodeVar: matchResult[1],
    nodeType: matchResult[2],
    whereClause: whereResult ? {
      var: whereResult[1],
      prop: whereResult[2],
      value: whereResult[3],
    } : null,
    returnVar: returnResult ? returnResult[1] : matchResult[1],
  };
}

async function executeCypherQuery(env: Env, parsed: any): Promise<any[]> {
  let query = `SELECT * FROM graph_nodes WHERE type = ?`;
  const params: any[] = [parsed.nodeType];

  if (parsed.whereClause && parsed.whereClause.prop === 'label') {
    query += ` AND label = ?`;
    params.push(parsed.whereClause.value);
  }

  const results = await env.D1_DATABASE.prepare(query).bind(...params).all();
  return (results.results || []).map(parseNode);
}

function getNodeColor(type: NodeType): string {
  const colors: Record<NodeType, string> = {
    'Device': '#4A90D9',
    'Component': '#7B68EE',
    'Symptom': '#FF6B6B',
    'Repair': '#4ECDC4',
    'Technician': '#95E1D3',
    'Tool': '#F7DC6F',
    'Part': '#BB8FCE',
    'Solution': '#58D68D',
    'Cause': '#E74C3C',
    'Model': '#3498DB',
    'Brand': '#9B59B6',
  };
  return colors[type] || '#95A5A6';
}

export default app;
