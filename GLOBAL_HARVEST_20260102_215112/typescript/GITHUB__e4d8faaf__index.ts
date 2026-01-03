/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * NOIZYLAB - Full Repair Service System
 * Equipment registration, work orders, and service management
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  KV: KVNamespace;
}

interface Equipment {
  id: string;
  name: string;
  brand: string;
  model: string;
  serial_number?: string;
  category: string;
  owner_id: string;
  status: 'active' | 'in_repair' | 'retired';
  created_at: string;
}

interface WorkOrder {
  id: string;
  equipment_id: string;
  description: string;
  priority: 'low' | 'medium' | 'high' | 'urgent';
  status: 'open' | 'in_progress' | 'pending_parts' | 'completed' | 'cancelled';
  technician_id?: string;
  notes: string[];
  created_at: string;
  updated_at: string;
  completed_at?: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// APP SETUP
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  return c.json({
    name: 'NOIZYLAB',
    version: '1.0.0',
    status: 'operational',
    mission: 'Full Repair Service System',
    endpoints: [
      '/health',
      '/equipment',
      '/equipment/:id',
      '/workorders',
      '/workorders/:id',
      '/workorders/:id/notes',
      '/stats'
    ]
  });
});

app.get('/health', async (c) => {
  const checks: Record<string, string> = { worker: 'ok' };

  try {
    await c.env.DB.prepare('SELECT 1').first();
    checks.d1 = 'ok';
  } catch {
    checks.d1 = 'error';
  }

  try {
    await c.env.KV.get('health');
    checks.kv = 'ok';
  } catch {
    checks.kv = 'error';
  }

  return c.json({ ...checks, timestamp: new Date().toISOString() });
});

// ═══════════════════════════════════════════════════════════════════════════════
// EQUIPMENT MANAGEMENT
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/equipment', async (c) => {
  const status = c.req.query('status');
  const category = c.req.query('category');

  let sql = 'SELECT * FROM equipment WHERE 1=1';
  const params: any[] = [];

  if (status) {
    sql += ' AND status = ?';
    params.push(status);
  }
  if (category) {
    sql += ' AND category = ?';
    params.push(category);
  }

  sql += ' ORDER BY created_at DESC LIMIT 100';

  try {
    const stmt = c.env.DB.prepare(sql);
    const results = params.length > 0 ? await stmt.bind(...params).all() : await stmt.all();
    
    return c.json({
      equipment: results.results || [],
      total: results.results?.length || 0
    });
  } catch {
    return c.json({ equipment: [], total: 0, note: 'D1 not initialized' });
  }
});

app.post('/equipment', async (c) => {
  const body = await c.req.json<Partial<Equipment>>();

  if (!body.name || !body.brand || !body.owner_id) {
    return c.json({ error: 'name, brand, and owner_id required' }, 400);
  }

  const equipment: Equipment = {
    id: `eq-${Date.now()}`,
    name: body.name,
    brand: body.brand,
    model: body.model || '',
    serial_number: body.serial_number,
    category: body.category || 'general',
    owner_id: body.owner_id,
    status: 'active',
    created_at: new Date().toISOString()
  };

  try {
    await c.env.DB.prepare(`
      INSERT INTO equipment (id, name, brand, model, serial_number, category, owner_id, status, created_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      equipment.id,
      equipment.name,
      equipment.brand,
      equipment.model,
      equipment.serial_number || null,
      equipment.category,
      equipment.owner_id,
      equipment.status,
      equipment.created_at
    ).run();
  } catch {
    await c.env.KV.put(`equipment:${equipment.id}`, JSON.stringify(equipment));
  }

  return c.json({ success: true, equipment }, 201);
});

app.get('/equipment/:id', async (c) => {
  const id = c.req.param('id');

  try {
    const equipment = await c.env.DB.prepare('SELECT * FROM equipment WHERE id = ?').bind(id).first();
    
    if (equipment) {
      return c.json(equipment);
    }
  } catch {}

  // Fallback to KV
  const kvData = await c.env.KV.get(`equipment:${id}`);
  if (kvData) {
    return c.json(JSON.parse(kvData));
  }

  return c.json({ error: 'Equipment not found' }, 404);
});

app.put('/equipment/:id', async (c) => {
  const id = c.req.param('id');
  const body = await c.req.json<Partial<Equipment>>();

  const updates: string[] = [];
  const params: any[] = [];

  if (body.name) { updates.push('name = ?'); params.push(body.name); }
  if (body.status) { updates.push('status = ?'); params.push(body.status); }
  if (body.category) { updates.push('category = ?'); params.push(body.category); }
  if (body.model) { updates.push('model = ?'); params.push(body.model); }

  if (updates.length === 0) {
    return c.json({ error: 'No updates provided' }, 400);
  }

  params.push(id);

  try {
    await c.env.DB.prepare(`UPDATE equipment SET ${updates.join(', ')} WHERE id = ?`)
      .bind(...params)
      .run();

    return c.json({ success: true, id });
  } catch (error) {
    return c.json({ error: 'Update failed' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// WORK ORDER MANAGEMENT
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/workorders', async (c) => {
  const status = c.req.query('status');
  const priority = c.req.query('priority');

  let sql = 'SELECT * FROM workorders WHERE 1=1';
  const params: any[] = [];

  if (status) {
    sql += ' AND status = ?';
    params.push(status);
  }
  if (priority) {
    sql += ' AND priority = ?';
    params.push(priority);
  }

  sql += ' ORDER BY created_at DESC LIMIT 100';

  try {
    const stmt = c.env.DB.prepare(sql);
    const results = params.length > 0 ? await stmt.bind(...params).all() : await stmt.all();
    
    return c.json({
      workorders: results.results || [],
      total: results.results?.length || 0
    });
  } catch {
    return c.json({ workorders: [], total: 0 });
  }
});

app.post('/workorders', async (c) => {
  const body = await c.req.json<{
    equipment_id: string;
    description: string;
    priority?: 'low' | 'medium' | 'high' | 'urgent';
  }>();

  if (!body.equipment_id || !body.description) {
    return c.json({ error: 'equipment_id and description required' }, 400);
  }

  const workorder: WorkOrder = {
    id: `wo-${Date.now()}`,
    equipment_id: body.equipment_id,
    description: body.description,
    priority: body.priority || 'medium',
    status: 'open',
    notes: [],
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString()
  };

  try {
    await c.env.DB.prepare(`
      INSERT INTO workorders (id, equipment_id, description, priority, status, technician_id, notes, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      workorder.id,
      workorder.equipment_id,
      workorder.description,
      workorder.priority,
      workorder.status,
      null,
      JSON.stringify(workorder.notes),
      workorder.created_at,
      workorder.updated_at
    ).run();

    // Update equipment status
    await c.env.DB.prepare(`UPDATE equipment SET status = 'in_repair' WHERE id = ?`)
      .bind(body.equipment_id)
      .run();
  } catch {
    await c.env.KV.put(`workorder:${workorder.id}`, JSON.stringify(workorder));
  }

  return c.json({ success: true, workorder }, 201);
});

app.get('/workorders/:id', async (c) => {
  const id = c.req.param('id');

  try {
    const workorder = await c.env.DB.prepare('SELECT * FROM workorders WHERE id = ?').bind(id).first();
    
    if (workorder) {
      return c.json({
        ...workorder,
        notes: JSON.parse((workorder as any).notes || '[]')
      });
    }
  } catch {}

  const kvData = await c.env.KV.get(`workorder:${id}`);
  if (kvData) {
    return c.json(JSON.parse(kvData));
  }

  return c.json({ error: 'Work order not found' }, 404);
});

app.put('/workorders/:id', async (c) => {
  const id = c.req.param('id');
  const body = await c.req.json<Partial<WorkOrder>>();

  const updates: string[] = ['updated_at = ?'];
  const params: any[] = [new Date().toISOString()];

  if (body.status) { 
    updates.push('status = ?'); 
    params.push(body.status);
    
    if (body.status === 'completed') {
      updates.push('completed_at = ?');
      params.push(new Date().toISOString());
    }
  }
  if (body.priority) { updates.push('priority = ?'); params.push(body.priority); }
  if (body.technician_id) { updates.push('technician_id = ?'); params.push(body.technician_id); }

  params.push(id);

  try {
    await c.env.DB.prepare(`UPDATE workorders SET ${updates.join(', ')} WHERE id = ?`)
      .bind(...params)
      .run();

    // If completed, update equipment status back to active
    if (body.status === 'completed') {
      const wo = await c.env.DB.prepare('SELECT equipment_id FROM workorders WHERE id = ?').bind(id).first() as any;
      if (wo?.equipment_id) {
        await c.env.DB.prepare(`UPDATE equipment SET status = 'active' WHERE id = ?`)
          .bind(wo.equipment_id)
          .run();
      }
    }

    return c.json({ success: true, id });
  } catch (error) {
    return c.json({ error: 'Update failed' }, 500);
  }
});

app.post('/workorders/:id/notes', async (c) => {
  const id = c.req.param('id');
  const body = await c.req.json<{ note: string; author?: string }>();

  if (!body.note) {
    return c.json({ error: 'note required' }, 400);
  }

  try {
    const workorder = await c.env.DB.prepare('SELECT notes FROM workorders WHERE id = ?').bind(id).first() as any;
    
    if (!workorder) {
      return c.json({ error: 'Work order not found' }, 404);
    }

    const notes = JSON.parse(workorder.notes || '[]');
    notes.push({
      text: body.note,
      author: body.author || 'system',
      timestamp: new Date().toISOString()
    });

    await c.env.DB.prepare(`UPDATE workorders SET notes = ?, updated_at = ? WHERE id = ?`)
      .bind(JSON.stringify(notes), new Date().toISOString(), id)
      .run();

    return c.json({ success: true, notes });
  } catch (error) {
    return c.json({ error: 'Failed to add note' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// STATISTICS
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/stats', async (c) => {
  try {
    const equipmentCount = await c.env.DB.prepare('SELECT COUNT(*) as count FROM equipment').first() as any;
    const workordersOpen = await c.env.DB.prepare("SELECT COUNT(*) as count FROM workorders WHERE status IN ('open', 'in_progress')").first() as any;
    const workordersCompleted = await c.env.DB.prepare("SELECT COUNT(*) as count FROM workorders WHERE status = 'completed'").first() as any;

    return c.json({
      equipment: {
        total: equipmentCount?.count || 0
      },
      workorders: {
        open: workordersOpen?.count || 0,
        completed: workordersCompleted?.count || 0
      },
      timestamp: new Date().toISOString()
    });
  } catch {
    return c.json({
      equipment: { total: 0 },
      workorders: { open: 0, completed: 0 },
      note: 'Stats unavailable - D1 not initialized'
    });
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// INIT D1 TABLES
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/init', async (c) => {
  const queries = [
    `CREATE TABLE IF NOT EXISTS equipment (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      brand TEXT NOT NULL,
      model TEXT,
      serial_number TEXT,
      category TEXT,
      owner_id TEXT NOT NULL,
      status TEXT DEFAULT 'active',
      created_at TEXT NOT NULL
    )`,
    `CREATE TABLE IF NOT EXISTS workorders (
      id TEXT PRIMARY KEY,
      equipment_id TEXT NOT NULL,
      description TEXT NOT NULL,
      priority TEXT DEFAULT 'medium',
      status TEXT DEFAULT 'open',
      technician_id TEXT,
      notes TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      completed_at TEXT,
      FOREIGN KEY (equipment_id) REFERENCES equipment(id)
    )`,
    `CREATE INDEX IF NOT EXISTS idx_equipment_owner ON equipment(owner_id)`,
    `CREATE INDEX IF NOT EXISTS idx_equipment_status ON equipment(status)`,
    `CREATE INDEX IF NOT EXISTS idx_workorders_equipment ON workorders(equipment_id)`,
    `CREATE INDEX IF NOT EXISTS idx_workorders_status ON workorders(status)`
  ];

  const results: string[] = [];

  for (const sql of queries) {
    try {
      await c.env.DB.prepare(sql).run();
      results.push(`✅ ${sql.substring(0, 50)}...`);
    } catch (error) {
      results.push(`❌ ${sql.substring(0, 50)}... - ${error}`);
    }
  }

  return c.json({ message: 'D1 initialization complete', results });
});

export default app;
