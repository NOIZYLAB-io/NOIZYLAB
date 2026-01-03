/**
 * NoizyLab OS - Natural Language Query Worker
 * English-to-SQL Intelligence Engine
 * 
 * Features:
 * - Natural language to SQL conversion
 * - Schema-aware query generation
 * - Query validation and safety checks
 * - Query optimization suggestions
 * - Conversational follow-ups
 * - Result summarization with AI
 * - Query history and favorites
 * - Auto-visualization recommendations
 */

import { Hono } from 'hono';

interface Env {
  QUERY_KV: KVNamespace;
  DB: D1Database;
  AI: Ai;
}

interface SchemaInfo {
  tables: TableSchema[];
  relationships: Relationship[];
  views: ViewSchema[];
  lastUpdated: Date;
}

interface TableSchema {
  name: string;
  description: string;
  columns: ColumnSchema[];
  rowCount?: number;
  sampleValues?: Record<string, string[]>;
}

interface ColumnSchema {
  name: string;
  type: string;
  nullable: boolean;
  isPrimaryKey: boolean;
  isForeignKey: boolean;
  references?: { table: string; column: string };
  description?: string;
  examples?: string[];
}

interface Relationship {
  fromTable: string;
  fromColumn: string;
  toTable: string;
  toColumn: string;
  type: 'one-to-one' | 'one-to-many' | 'many-to-many';
}

interface ViewSchema {
  name: string;
  description: string;
  query: string;
}

interface QueryResult {
  id: string;
  naturalLanguage: string;
  generatedSQL: string;
  executionTime: number;
  rowCount: number;
  columns: string[];
  data: any[];
  summary?: string;
  visualizationRecommendation?: VisualizationRecommendation;
  followUpSuggestions: string[];
}

interface VisualizationRecommendation {
  type: 'bar' | 'line' | 'pie' | 'scatter' | 'table' | 'metric' | 'map';
  config: Record<string, any>;
  reasoning: string;
}

interface QueryValidation {
  isValid: boolean;
  isSafe: boolean;
  errors: string[];
  warnings: string[];
  suggestions: string[];
  estimatedCost: 'low' | 'medium' | 'high';
}

interface ConversationContext {
  sessionId: string;
  queries: { question: string; sql: string; timestamp: Date }[];
  entityMentions: Map<string, string>;
  lastTables: string[];
}

const app = new Hono<{ Bindings: Env }>();

// ==================== SCHEMA MANAGEMENT ====================

app.post('/schema/sync', async (c) => {
  // Introspect database schema
  const tables = await introspectTables(c.env);
  const relationships = await detectRelationships(c.env, tables);
  const views = await getViews(c.env);
  
  const schema: SchemaInfo = {
    tables,
    relationships,
    views,
    lastUpdated: new Date()
  };
  
  // Store schema
  await c.env.QUERY_KV.put('schema:main', JSON.stringify(schema));
  
  return c.json({
    success: true,
    tableCount: tables.length,
    viewCount: views.length,
    relationshipCount: relationships.length,
    lastUpdated: schema.lastUpdated
  });
});

app.get('/schema', async (c) => {
  const schemaJson = await c.env.QUERY_KV.get('schema:main');
  if (!schemaJson) {
    return c.json({ error: 'Schema not synced. Run POST /schema/sync first.' }, 404);
  }
  
  const schema: SchemaInfo = JSON.parse(schemaJson);
  
  return c.json({
    schema,
    summary: {
      tables: schema.tables.map(t => ({ name: t.name, columns: t.columns.length })),
      relationships: schema.relationships.length
    }
  });
});

// ==================== NATURAL LANGUAGE QUERY ====================

app.post('/query', async (c) => {
  const { question, sessionId, executeQuery = true } = await c.req.json();
  
  // Get schema
  const schemaJson = await c.env.QUERY_KV.get('schema:main');
  if (!schemaJson) {
    return c.json({ error: 'Schema not synced. Run POST /schema/sync first.' }, 404);
  }
  
  const schema: SchemaInfo = JSON.parse(schemaJson);
  
  // Get conversation context if exists
  let context: ConversationContext | null = null;
  if (sessionId) {
    const contextJson = await c.env.QUERY_KV.get(`context:${sessionId}`);
    context = contextJson ? JSON.parse(contextJson) : null;
  }
  
  // Generate SQL using AI
  const sql = await generateSQL(c.env, question, schema, context);
  
  // Validate query
  const validation = validateQuery(sql, schema);
  
  if (!validation.isSafe) {
    return c.json({
      error: 'Query validation failed',
      validation,
      generatedSQL: sql
    }, 400);
  }
  
  let result: QueryResult = {
    id: `query_${Date.now()}`,
    naturalLanguage: question,
    generatedSQL: sql,
    executionTime: 0,
    rowCount: 0,
    columns: [],
    data: [],
    followUpSuggestions: []
  };
  
  // Execute query if requested
  if (executeQuery && validation.isValid) {
    const startTime = Date.now();
    
    try {
      const queryResult = await c.env.DB.prepare(sql).all();
      
      result.executionTime = Date.now() - startTime;
      result.data = queryResult.results || [];
      result.rowCount = result.data.length;
      result.columns = result.data.length > 0 ? Object.keys(result.data[0]) : [];
      
      // Generate summary
      result.summary = await summarizeResults(c.env, question, result.data);
      
      // Recommend visualization
      result.visualizationRecommendation = recommendVisualization(result);
      
      // Generate follow-up suggestions
      result.followUpSuggestions = generateFollowUps(question, result, schema);
      
    } catch (e: any) {
      return c.json({
        error: 'Query execution failed',
        message: e.message,
        generatedSQL: sql,
        validation
      }, 500);
    }
  }
  
  // Update conversation context
  if (sessionId) {
    await updateContext(c.env, sessionId, question, sql, schema);
  }
  
  // Store query in history
  await c.env.DB.prepare(`
    INSERT INTO query_history (id, question, sql, execution_time, row_count, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(result.id, question, sql, result.executionTime, result.rowCount).run();
  
  return c.json({
    result,
    validation
  });
});

app.post('/query/explain', async (c) => {
  const { question } = await c.req.json();
  
  const schemaJson = await c.env.QUERY_KV.get('schema:main');
  if (!schemaJson) {
    return c.json({ error: 'Schema not synced' }, 404);
  }
  
  const schema: SchemaInfo = JSON.parse(schemaJson);
  
  // Generate SQL
  const sql = await generateSQL(c.env, question, schema, null);
  
  // Generate detailed explanation
  const explanation = await explainQuery(c.env, question, sql, schema);
  
  return c.json({
    question,
    sql,
    explanation,
    tablesMentioned: extractTables(sql, schema),
    validation: validateQuery(sql, schema)
  });
});

app.post('/query/optimize', async (c) => {
  const { sql } = await c.req.json();
  
  const schemaJson = await c.env.QUERY_KV.get('schema:main');
  if (!schemaJson) {
    return c.json({ error: 'Schema not synced' }, 404);
  }
  
  const schema: SchemaInfo = JSON.parse(schemaJson);
  
  // Analyze query for optimizations
  const optimizations = analyzeQueryOptimizations(sql, schema);
  
  // Generate optimized version
  const optimizedSQL = applyOptimizations(sql, optimizations);
  
  return c.json({
    originalSQL: sql,
    optimizedSQL,
    optimizations,
    expectedImprovement: optimizations.length > 0 ? 'significant' : 'minimal'
  });
});

// ==================== CONVERSATION ====================

app.post('/conversation/start', async (c) => {
  const sessionId = `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  
  const context: ConversationContext = {
    sessionId,
    queries: [],
    entityMentions: new Map(),
    lastTables: []
  };
  
  await c.env.QUERY_KV.put(`context:${sessionId}`, JSON.stringify(context), { expirationTtl: 3600 });
  
  return c.json({
    sessionId,
    message: 'Conversation started. Ask questions about your data.',
    suggestedQuestions: await generateSuggestedQuestions(c.env)
  });
});

app.post('/conversation/:sessionId/ask', async (c) => {
  const sessionId = c.req.param('sessionId');
  const { question } = await c.req.json();
  
  // Delegate to main query endpoint
  const response = await fetch(new URL('/query', c.req.url), {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, sessionId, executeQuery: true })
  });
  
  return c.json(await response.json());
});

app.get('/conversation/:sessionId/history', async (c) => {
  const sessionId = c.req.param('sessionId');
  
  const contextJson = await c.env.QUERY_KV.get(`context:${sessionId}`);
  if (!contextJson) {
    return c.json({ error: 'Session not found' }, 404);
  }
  
  const context: ConversationContext = JSON.parse(contextJson);
  
  return c.json({
    sessionId,
    queryCount: context.queries.length,
    queries: context.queries,
    recentTables: context.lastTables
  });
});

// ==================== QUERY TEMPLATES ====================

app.get('/templates', async (c) => {
  const schemaJson = await c.env.QUERY_KV.get('schema:main');
  if (!schemaJson) {
    return c.json({ error: 'Schema not synced' }, 404);
  }
  
  const schema: SchemaInfo = JSON.parse(schemaJson);
  
  // Generate templates based on schema
  const templates = generateQueryTemplates(schema);
  
  return c.json({
    templates,
    categories: [...new Set(templates.map(t => t.category))]
  });
});

app.get('/templates/:category', async (c) => {
  const category = c.req.param('category');
  
  const schemaJson = await c.env.QUERY_KV.get('schema:main');
  if (!schemaJson) {
    return c.json({ error: 'Schema not synced' }, 404);
  }
  
  const schema: SchemaInfo = JSON.parse(schemaJson);
  const templates = generateQueryTemplates(schema).filter(t => t.category === category);
  
  return c.json({ templates });
});

// ==================== SAVED QUERIES ====================

app.post('/saved', async (c) => {
  const { name, description, question, sql, userId } = await c.req.json();
  
  const id = `saved_${Date.now()}`;
  
  await c.env.DB.prepare(`
    INSERT INTO saved_queries (id, name, description, question, sql, user_id, created_at)
    VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(id, name, description, question, sql, userId).run();
  
  return c.json({
    success: true,
    id,
    name
  });
});

app.get('/saved', async (c) => {
  const userId = c.req.query('userId');
  
  let query = 'SELECT * FROM saved_queries';
  if (userId) {
    query += ` WHERE user_id = '${userId}'`;
  }
  query += ' ORDER BY created_at DESC';
  
  const result = await c.env.DB.prepare(query).all();
  
  return c.json({
    queries: result.results || []
  });
});

app.delete('/saved/:id', async (c) => {
  const id = c.req.param('id');
  
  await c.env.DB.prepare('DELETE FROM saved_queries WHERE id = ?').bind(id).run();
  
  return c.json({ success: true });
});

// ==================== HELPER FUNCTIONS ====================

async function introspectTables(env: Env): Promise<TableSchema[]> {
  const tables: TableSchema[] = [];
  
  // Get table list
  const tableList = await env.DB.prepare(`
    SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name NOT LIKE '_cf_%'
  `).all();
  
  for (const tableRow of tableList.results || []) {
    const tableName = tableRow.name as string;
    
    // Get column info
    const columnInfo = await env.DB.prepare(`PRAGMA table_info('${tableName}')`).all();
    
    const columns: ColumnSchema[] = (columnInfo.results || []).map(col => ({
      name: col.name as string,
      type: col.type as string,
      nullable: col.notnull === 0,
      isPrimaryKey: col.pk === 1,
      isForeignKey: false,
      description: undefined,
      examples: []
    }));
    
    // Get sample values
    const sampleData = await env.DB.prepare(`SELECT * FROM "${tableName}" LIMIT 5`).all();
    const sampleValues: Record<string, string[]> = {};
    
    for (const col of columns) {
      sampleValues[col.name] = (sampleData.results || [])
        .map(row => String(row[col.name]))
        .filter(v => v !== 'null' && v !== 'undefined');
    }
    
    // Get row count
    const countResult = await env.DB.prepare(`SELECT COUNT(*) as count FROM "${tableName}"`).first();
    
    tables.push({
      name: tableName,
      description: inferTableDescription(tableName),
      columns,
      rowCount: (countResult?.count as number) || 0,
      sampleValues
    });
  }
  
  return tables;
}

function inferTableDescription(tableName: string): string {
  const descriptions: Record<string, string> = {
    customers: 'Customer information including contact details and segments',
    orders: 'Order records with status and totals',
    order_items: 'Individual items within orders',
    products: 'Product catalog with pricing and inventory',
    inventory: 'Stock levels and reorder information',
    repairs: 'Repair job records and status',
    technicians: 'Technician profiles and skills',
    parts: 'Parts inventory and specifications',
    invoices: 'Billing and payment records',
    users: 'System user accounts'
  };
  
  return descriptions[tableName.toLowerCase()] || `Data stored in ${tableName}`;
}

async function detectRelationships(env: Env, tables: TableSchema[]): Promise<Relationship[]> {
  const relationships: Relationship[] = [];
  
  // Detect foreign key patterns
  for (const table of tables) {
    for (const column of table.columns) {
      // Check for _id naming pattern
      if (column.name.endsWith('_id') && !column.isPrimaryKey) {
        const referencedTable = column.name.replace('_id', 's');
        const matchingTable = tables.find(t => 
          t.name.toLowerCase() === referencedTable.toLowerCase() ||
          t.name.toLowerCase() === column.name.replace('_id', '').toLowerCase()
        );
        
        if (matchingTable) {
          relationships.push({
            fromTable: table.name,
            fromColumn: column.name,
            toTable: matchingTable.name,
            toColumn: 'id',
            type: 'many-to-many'
          });
          
          column.isForeignKey = true;
          column.references = { table: matchingTable.name, column: 'id' };
        }
      }
    }
  }
  
  return relationships;
}

async function getViews(env: Env): Promise<ViewSchema[]> {
  const views: ViewSchema[] = [];
  
  const viewList = await env.DB.prepare(`
    SELECT name, sql FROM sqlite_master WHERE type='view'
  `).all();
  
  for (const viewRow of viewList.results || []) {
    views.push({
      name: viewRow.name as string,
      description: `View: ${viewRow.name}`,
      query: viewRow.sql as string
    });
  }
  
  return views;
}

async function generateSQL(
  env: Env,
  question: string,
  schema: SchemaInfo,
  context: ConversationContext | null
): Promise<string> {
  // Build schema context for AI
  const schemaContext = schema.tables.map(t => 
    `Table: ${t.name}\nColumns: ${t.columns.map(c => `${c.name} (${c.type})`).join(', ')}\nDescription: ${t.description}`
  ).join('\n\n');
  
  const relationshipContext = schema.relationships.map(r =>
    `${r.fromTable}.${r.fromColumn} -> ${r.toTable}.${r.toColumn}`
  ).join('\n');
  
  // Build conversation context
  let conversationHistory = '';
  if (context && context.queries.length > 0) {
    conversationHistory = 'Previous queries in this conversation:\n' +
      context.queries.slice(-3).map(q => `Q: ${q.question}\nSQL: ${q.sql}`).join('\n\n');
  }
  
  const prompt = `You are a SQL expert. Generate a SQLite query based on the user's natural language question.

Database Schema:
${schemaContext}

Relationships:
${relationshipContext}

${conversationHistory ? `\n${conversationHistory}\n` : ''}

User Question: ${question}

Rules:
1. Generate only valid SQLite syntax
2. Use proper JOINs based on relationships
3. Include appropriate WHERE clauses
4. Use aliases for readability
5. If the question is ambiguous, make reasonable assumptions
6. For aggregations, include GROUP BY
7. Limit results to 100 rows unless specified
8. Only return the SQL query, nothing else

SQL Query:`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 500,
      temperature: 0.1
    });
    
    let sql = (response as any).response || '';
    
    // Clean up the response
    sql = sql.trim();
    sql = sql.replace(/```sql\n?/g, '').replace(/```\n?/g, '');
    sql = sql.split(';')[0] + ';';
    
    // Basic validation - ensure it's a SELECT
    if (!sql.toLowerCase().startsWith('select')) {
      // Try to extract SELECT statement
      const selectMatch = sql.match(/SELECT[\s\S]+?;/i);
      if (selectMatch) {
        sql = selectMatch[0];
      }
    }
    
    return sql;
  } catch (e) {
    // Fallback to rule-based generation
    return generateSQLRuleBased(question, schema);
  }
}

function generateSQLRuleBased(question: string, schema: SchemaInfo): string {
  const lowerQuestion = question.toLowerCase();
  
  // Detect intent
  const isCount = lowerQuestion.includes('how many') || lowerQuestion.includes('count');
  const isTop = lowerQuestion.includes('top') || lowerQuestion.includes('best') || lowerQuestion.includes('most');
  const isRecent = lowerQuestion.includes('recent') || lowerQuestion.includes('latest') || lowerQuestion.includes('last');
  const isTotal = lowerQuestion.includes('total') || lowerQuestion.includes('sum');
  const isAverage = lowerQuestion.includes('average') || lowerQuestion.includes('avg');
  
  // Detect table
  let targetTable = schema.tables[0]?.name || 'items';
  for (const table of schema.tables) {
    if (lowerQuestion.includes(table.name.toLowerCase()) || 
        lowerQuestion.includes(table.name.slice(0, -1).toLowerCase())) {
      targetTable = table.name;
      break;
    }
  }
  
  const table = schema.tables.find(t => t.name === targetTable);
  
  // Build query
  let sql = '';
  
  if (isCount) {
    sql = `SELECT COUNT(*) as count FROM ${targetTable}`;
  } else if (isTop) {
    const numMatch = lowerQuestion.match(/top (\d+)/);
    const limit = numMatch ? parseInt(numMatch[1]) : 10;
    sql = `SELECT * FROM ${targetTable} ORDER BY created_at DESC LIMIT ${limit}`;
  } else if (isRecent) {
    sql = `SELECT * FROM ${targetTable} ORDER BY created_at DESC LIMIT 10`;
  } else if (isTotal && table) {
    const numericCol = table.columns.find(c => 
      ['total', 'amount', 'price', 'cost', 'value'].some(n => c.name.includes(n))
    );
    if (numericCol) {
      sql = `SELECT SUM(${numericCol.name}) as total FROM ${targetTable}`;
    } else {
      sql = `SELECT * FROM ${targetTable} LIMIT 100`;
    }
  } else if (isAverage && table) {
    const numericCol = table.columns.find(c => 
      c.type.toLowerCase().includes('int') || c.type.toLowerCase().includes('real')
    );
    if (numericCol) {
      sql = `SELECT AVG(${numericCol.name}) as average FROM ${targetTable}`;
    } else {
      sql = `SELECT * FROM ${targetTable} LIMIT 100`;
    }
  } else {
    sql = `SELECT * FROM ${targetTable} LIMIT 100`;
  }
  
  return sql + ';';
}

function validateQuery(sql: string, schema: SchemaInfo): QueryValidation {
  const errors: string[] = [];
  const warnings: string[] = [];
  const suggestions: string[] = [];
  
  const lowerSQL = sql.toLowerCase();
  
  // Safety checks
  const unsafeKeywords = ['drop', 'delete', 'truncate', 'alter', 'create', 'insert', 'update'];
  const hasUnsafe = unsafeKeywords.some(k => lowerSQL.includes(k));
  
  if (hasUnsafe) {
    errors.push('Query contains unsafe operations (only SELECT allowed)');
  }
  
  // Check if it's a SELECT
  if (!lowerSQL.trim().startsWith('select')) {
    errors.push('Query must be a SELECT statement');
  }
  
  // Check for table references
  const tableNames = schema.tables.map(t => t.name.toLowerCase());
  const referencedTables = sql.match(/from\s+(\w+)/gi);
  
  if (referencedTables) {
    for (const ref of referencedTables) {
      const tableName = ref.replace(/from\s+/i, '').toLowerCase();
      if (!tableNames.includes(tableName)) {
        warnings.push(`Table '${tableName}' may not exist`);
      }
    }
  }
  
  // Check for potential performance issues
  if (!lowerSQL.includes('limit') && !lowerSQL.includes('group by')) {
    warnings.push('Consider adding LIMIT to prevent large result sets');
    suggestions.push('Add LIMIT 100 to the query');
  }
  
  if (lowerSQL.includes('select *')) {
    suggestions.push('Consider selecting specific columns instead of *');
  }
  
  // Estimate cost
  let estimatedCost: 'low' | 'medium' | 'high' = 'low';
  if (lowerSQL.includes('join') && lowerSQL.includes('join')) {
    estimatedCost = 'medium';
  }
  if ((lowerSQL.match(/join/gi) || []).length > 2) {
    estimatedCost = 'high';
  }
  if (!lowerSQL.includes('where') && !lowerSQL.includes('limit')) {
    estimatedCost = 'high';
  }
  
  return {
    isValid: errors.length === 0,
    isSafe: !hasUnsafe,
    errors,
    warnings,
    suggestions,
    estimatedCost
  };
}

async function summarizeResults(env: Env, question: string, data: any[]): Promise<string> {
  if (data.length === 0) {
    return 'No results found.';
  }
  
  if (data.length === 1 && Object.keys(data[0]).length === 1) {
    const key = Object.keys(data[0])[0];
    return `The ${key} is ${data[0][key]}.`;
  }
  
  const prompt = `Summarize these query results in 1-2 sentences:
Question: ${question}
Results: ${JSON.stringify(data.slice(0, 5))}
${data.length > 5 ? `(showing 5 of ${data.length} results)` : ''}

Summary:`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 100,
      temperature: 0.3
    });
    
    return (response as any).response?.trim() || `Found ${data.length} results.`;
  } catch (e) {
    return `Found ${data.length} results.`;
  }
}

function recommendVisualization(result: QueryResult): VisualizationRecommendation {
  const { columns, data, rowCount } = result;
  
  if (rowCount === 0) {
    return { type: 'table', config: {}, reasoning: 'No data to visualize' };
  }
  
  if (rowCount === 1 && columns.length === 1) {
    return {
      type: 'metric',
      config: { value: data[0][columns[0]], label: columns[0] },
      reasoning: 'Single value result is best shown as a metric'
    };
  }
  
  // Check for time series
  const hasDateColumn = columns.some(c => 
    c.toLowerCase().includes('date') || c.toLowerCase().includes('time')
  );
  const hasNumericColumn = data.length > 0 && columns.some(c => 
    typeof data[0][c] === 'number'
  );
  
  if (hasDateColumn && hasNumericColumn) {
    return {
      type: 'line',
      config: {
        xAxis: columns.find(c => c.toLowerCase().includes('date') || c.toLowerCase().includes('time')),
        yAxis: columns.find(c => typeof data[0][c] === 'number')
      },
      reasoning: 'Time series data is best visualized as a line chart'
    };
  }
  
  // Check for categorical + numeric
  const categoricalColumn = columns.find(c => 
    data.length > 0 && typeof data[0][c] === 'string' && 
    !c.toLowerCase().includes('id')
  );
  
  if (categoricalColumn && hasNumericColumn && rowCount <= 10) {
    return {
      type: 'bar',
      config: {
        xAxis: categoricalColumn,
        yAxis: columns.find(c => typeof data[0][c] === 'number')
      },
      reasoning: 'Categorical comparison is best shown as a bar chart'
    };
  }
  
  if (categoricalColumn && hasNumericColumn && rowCount <= 6) {
    return {
      type: 'pie',
      config: {
        labels: categoricalColumn,
        values: columns.find(c => typeof data[0][c] === 'number')
      },
      reasoning: 'Distribution data with few categories works well as a pie chart'
    };
  }
  
  return {
    type: 'table',
    config: { columns },
    reasoning: 'Default to table view for detailed data inspection'
  };
}

function generateFollowUps(question: string, result: QueryResult, schema: SchemaInfo): string[] {
  const followUps: string[] = [];
  
  // Based on result type
  if (result.rowCount > 0) {
    followUps.push(`Show me more details about the first result`);
    
    if (result.columns.includes('id')) {
      followUps.push(`What's the history for ID ${result.data[0].id}?`);
    }
  }
  
  // Based on tables in query
  const tablesInQuery = extractTables(result.generatedSQL, schema);
  for (const table of tablesInQuery) {
    const relatedTables = schema.relationships
      .filter(r => r.fromTable === table || r.toTable === table)
      .map(r => r.fromTable === table ? r.toTable : r.fromTable);
    
    for (const related of relatedTables.slice(0, 2)) {
      followUps.push(`Show me the related ${related} data`);
    }
  }
  
  // Generic follow-ups
  if (result.rowCount > 10) {
    followUps.push(`Show me only the top 5`);
  }
  
  followUps.push(`Break this down by month`);
  followUps.push(`What's the total?`);
  
  return followUps.slice(0, 5);
}

function extractTables(sql: string, schema: SchemaInfo): string[] {
  const tables: string[] = [];
  const tableNames = schema.tables.map(t => t.name.toLowerCase());
  
  const fromMatches = sql.match(/from\s+(\w+)/gi) || [];
  const joinMatches = sql.match(/join\s+(\w+)/gi) || [];
  
  for (const match of [...fromMatches, ...joinMatches]) {
    const tableName = match.replace(/from\s+|join\s+/i, '').toLowerCase();
    if (tableNames.includes(tableName) && !tables.includes(tableName)) {
      tables.push(tableName);
    }
  }
  
  return tables;
}

async function updateContext(
  env: Env,
  sessionId: string,
  question: string,
  sql: string,
  schema: SchemaInfo
): Promise<void> {
  const contextJson = await env.QUERY_KV.get(`context:${sessionId}`);
  const context: ConversationContext = contextJson 
    ? JSON.parse(contextJson) 
    : { sessionId, queries: [], entityMentions: new Map(), lastTables: [] };
  
  context.queries.push({ question, sql, timestamp: new Date() });
  context.lastTables = extractTables(sql, schema);
  
  // Keep only last 10 queries
  if (context.queries.length > 10) {
    context.queries = context.queries.slice(-10);
  }
  
  await env.QUERY_KV.put(`context:${sessionId}`, JSON.stringify(context), { expirationTtl: 3600 });
}

async function explainQuery(
  env: Env,
  question: string,
  sql: string,
  schema: SchemaInfo
): Promise<any> {
  const prompt = `Explain this SQL query in simple terms:
SQL: ${sql}
Original question: ${question}

Explain:
1. What tables are being queried
2. What filters or conditions are applied
3. What the result will show

Explanation:`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 300,
      temperature: 0.3
    });
    
    return {
      natural: (response as any).response?.trim(),
      technical: {
        tables: extractTables(sql, schema),
        hasWhere: sql.toLowerCase().includes('where'),
        hasJoin: sql.toLowerCase().includes('join'),
        hasGroupBy: sql.toLowerCase().includes('group by'),
        hasOrderBy: sql.toLowerCase().includes('order by')
      }
    };
  } catch (e) {
    return {
      natural: 'Query explanation unavailable',
      technical: {
        tables: extractTables(sql, schema)
      }
    };
  }
}

function analyzeQueryOptimizations(sql: string, schema: SchemaInfo): any[] {
  const optimizations: any[] = [];
  const lowerSQL = sql.toLowerCase();
  
  // Check for SELECT *
  if (lowerSQL.includes('select *')) {
    optimizations.push({
      type: 'select_specific_columns',
      description: 'Replace SELECT * with specific columns',
      impact: 'medium'
    });
  }
  
  // Check for missing LIMIT
  if (!lowerSQL.includes('limit') && !lowerSQL.includes('group by')) {
    optimizations.push({
      type: 'add_limit',
      description: 'Add LIMIT clause to prevent large result sets',
      impact: 'high'
    });
  }
  
  // Check for subqueries that could be JOINs
  if (lowerSQL.includes('select') && (lowerSQL.match(/select/gi) || []).length > 1) {
    optimizations.push({
      type: 'subquery_to_join',
      description: 'Consider converting subqueries to JOINs',
      impact: 'medium'
    });
  }
  
  // Check for functions on indexed columns
  if (lowerSQL.match(/where\s+\w+\([^)]+\)/i)) {
    optimizations.push({
      type: 'avoid_function_on_column',
      description: 'Avoid using functions on columns in WHERE clause',
      impact: 'high'
    });
  }
  
  return optimizations;
}

function applyOptimizations(sql: string, optimizations: any[]): string {
  let optimizedSQL = sql;
  
  for (const opt of optimizations) {
    if (opt.type === 'add_limit' && !optimizedSQL.toLowerCase().includes('limit')) {
      optimizedSQL = optimizedSQL.replace(/;?\s*$/, ' LIMIT 100;');
    }
  }
  
  return optimizedSQL;
}

async function generateSuggestedQuestions(env: Env): Promise<string[]> {
  const schemaJson = await env.QUERY_KV.get('schema:main');
  if (!schemaJson) return [];
  
  const schema: SchemaInfo = JSON.parse(schemaJson);
  const suggestions: string[] = [];
  
  for (const table of schema.tables.slice(0, 3)) {
    suggestions.push(`How many ${table.name} do we have?`);
    suggestions.push(`Show me the most recent ${table.name}`);
  }
  
  return suggestions;
}

function generateQueryTemplates(schema: SchemaInfo): any[] {
  const templates: any[] = [];
  
  for (const table of schema.tables) {
    // Basic count
    templates.push({
      category: 'Counts',
      name: `Count ${table.name}`,
      question: `How many ${table.name} are there?`,
      sql: `SELECT COUNT(*) as count FROM ${table.name};`
    });
    
    // Recent records
    if (table.columns.some(c => c.name.includes('created') || c.name.includes('date'))) {
      const dateCol = table.columns.find(c => c.name.includes('created') || c.name.includes('date'));
      templates.push({
        category: 'Recent',
        name: `Recent ${table.name}`,
        question: `Show me the most recent ${table.name}`,
        sql: `SELECT * FROM ${table.name} ORDER BY ${dateCol?.name || 'id'} DESC LIMIT 10;`
      });
    }
    
    // Top by numeric column
    const numericCol = table.columns.find(c => 
      ['total', 'amount', 'price', 'cost', 'value', 'score'].some(n => c.name.includes(n))
    );
    if (numericCol) {
      templates.push({
        category: 'Top',
        name: `Top ${table.name} by ${numericCol.name}`,
        question: `Show me the top 10 ${table.name} by ${numericCol.name}`,
        sql: `SELECT * FROM ${table.name} ORDER BY ${numericCol.name} DESC LIMIT 10;`
      });
    }
  }
  
  return templates;
}

export default app;
