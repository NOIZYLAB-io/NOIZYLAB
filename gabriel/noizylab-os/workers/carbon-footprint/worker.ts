/**
 * NoizyLab OS - Carbon Footprint Tracker Worker
 * 
 * AI-powered sustainability and environmental impact monitoring system
 * that tracks carbon emissions, energy usage, and environmental metrics
 * across all operations.
 * 
 * Features:
 * - Real-time carbon emission tracking
 * - Energy consumption monitoring
 * - Supply chain carbon analysis
 * - Fleet emission tracking
 * - Renewable energy optimization
 * - Carbon offset recommendations
 * - ESG reporting automation
 * - Sustainability goal tracking
 * - Scope 1, 2, 3 emission calculations
 * - AI-powered reduction recommendations
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  CARBON_CACHE: KVNamespace;
  REPORTS_STORAGE: R2Bucket;
  AI: any;
  ALERT_QUEUE: Queue;
  ENVIRONMENT: string;
}

interface EmissionSource {
  id: string;
  name: string;
  scope: 1 | 2 | 3;
  category: string;
  unit: string;
  emissionFactor: number;
  dataSource: string;
}

interface EmissionRecord {
  id: string;
  sourceId: string;
  timestamp: string;
  quantity: number;
  emissions: number; // kg CO2e
  metadata: any;
}

interface CarbonGoal {
  id: string;
  name: string;
  targetYear: number;
  baselineYear: number;
  baselineEmissions: number;
  targetReduction: number; // percentage
  scope: 'all' | 1 | 2 | 3;
  status: 'on-track' | 'at-risk' | 'behind' | 'achieved';
}

interface EnergySource {
  id: string;
  name: string;
  type: 'grid' | 'solar' | 'wind' | 'hydro' | 'natural-gas' | 'diesel';
  renewable: boolean;
  emissionFactor: number; // kg CO2e per kWh
  location: string;
}

interface OffsetProject {
  id: string;
  name: string;
  type: 'reforestation' | 'renewable-energy' | 'methane-capture' | 'carbon-capture' | 'other';
  location: string;
  pricePerTon: number;
  verified: boolean;
  certifications: string[];
  availableCredits: number;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// ===========================================
// EMISSION FACTORS DATABASE
// ===========================================

const EMISSION_FACTORS = {
  // Scope 1 - Direct emissions
  'natural-gas': 2.0, // kg CO2e per m³
  'diesel': 2.68, // kg CO2e per liter
  'gasoline': 2.31, // kg CO2e per liter
  'propane': 1.51, // kg CO2e per liter
  'refrigerant-r410a': 2088, // kg CO2e per kg leaked
  
  // Scope 2 - Indirect from electricity
  'grid-us-avg': 0.42, // kg CO2e per kWh
  'grid-eu-avg': 0.28,
  'grid-uk': 0.21,
  'solar': 0.041,
  'wind': 0.011,
  'hydro': 0.024,
  
  // Scope 3 - Value chain
  'air-travel-short': 0.255, // kg CO2e per km per passenger
  'air-travel-long': 0.195,
  'car-travel': 0.171, // kg CO2e per km
  'shipping-road': 0.096, // kg CO2e per ton-km
  'shipping-sea': 0.016,
  'shipping-air': 0.602,
  'waste-landfill': 0.587, // kg CO2e per kg
  'waste-recycled': 0.021,
  'water-supply': 0.344, // kg CO2e per m³
  'paper': 0.919, // kg CO2e per kg
  'electronics': 100, // kg CO2e per kg (approximate)
};

// ===========================================
// CARBON DASHBOARD
// ===========================================

app.get('/carbon/dashboard', async (c) => {
  const env = c.env;
  const year = parseInt(c.req.query('year') || new Date().getFullYear().toString());
  
  // Get emissions by scope
  const scopeEmissions = await env.DB.prepare(`
    SELECT es.scope, SUM(er.emissions) as total_emissions
    FROM emission_records er
    JOIN emission_sources es ON er.source_id = es.id
    WHERE strftime('%Y', er.timestamp) = ?
    GROUP BY es.scope
  `).bind(year.toString()).all();
  
  // Get monthly trend
  const monthlyTrend = await env.DB.prepare(`
    SELECT strftime('%Y-%m', timestamp) as month, SUM(emissions) as total
    FROM emission_records
    WHERE strftime('%Y', timestamp) = ?
    GROUP BY month
    ORDER BY month
  `).bind(year.toString()).all();
  
  // Get top emission sources
  const topSources = await env.DB.prepare(`
    SELECT es.name, es.category, SUM(er.emissions) as total_emissions
    FROM emission_records er
    JOIN emission_sources es ON er.source_id = es.id
    WHERE strftime('%Y', er.timestamp) = ?
    GROUP BY es.id
    ORDER BY total_emissions DESC
    LIMIT 10
  `).bind(year.toString()).all();
  
  // Get carbon intensity
  const revenue = await env.DB.prepare(`
    SELECT SUM(amount) as total FROM financial_records WHERE strftime('%Y', date) = ?
  `).bind(year.toString()).first() as any;
  
  const totalEmissions = scopeEmissions.results.reduce((sum: number, s: any) => sum + s.total_emissions, 0);
  const carbonIntensity = revenue?.total ? totalEmissions / (revenue.total / 1000000) : 0; // tons CO2e per $M revenue
  
  // Get goal progress
  const goals = await env.DB.prepare(`
    SELECT * FROM carbon_goals WHERE target_year >= ?
  `).bind(year).all();
  
  // Calculate renewable energy percentage
  const energyMix = await calculateEnergyMix(env, year);
  
  return c.json({
    success: true,
    dashboard: {
      year,
      totalEmissions: Math.round(totalEmissions),
      emissionsByScope: {
        scope1: scopeEmissions.results.find((s: any) => s.scope === 1)?.total_emissions || 0,
        scope2: scopeEmissions.results.find((s: any) => s.scope === 2)?.total_emissions || 0,
        scope3: scopeEmissions.results.find((s: any) => s.scope === 3)?.total_emissions || 0
      },
      monthlyTrend: monthlyTrend.results,
      topSources: topSources.results,
      carbonIntensity: Math.round(carbonIntensity * 100) / 100,
      renewablePercentage: energyMix.renewablePercentage,
      goals: goals.results,
      lastUpdated: new Date().toISOString()
    }
  });
});

// ===========================================
// EMISSION TRACKING
// ===========================================

app.post('/carbon/emissions/record', async (c) => {
  const env = c.env;
  const { sourceId, quantity, timestamp, metadata } = await c.req.json();
  
  // Get emission source
  const source = await env.DB.prepare(`
    SELECT * FROM emission_sources WHERE id = ?
  `).bind(sourceId).first() as any;
  
  if (!source) {
    return c.json({ success: false, error: 'Emission source not found' }, 404);
  }
  
  // Calculate emissions
  const emissions = quantity * source.emission_factor;
  
  const id = `ER-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  await env.DB.prepare(`
    INSERT INTO emission_records (id, source_id, timestamp, quantity, emissions, metadata)
    VALUES (?, ?, ?, ?, ?, ?)
  `).bind(
    id,
    sourceId,
    timestamp || new Date().toISOString(),
    quantity,
    emissions,
    JSON.stringify(metadata || {})
  ).run();
  
  // Check against thresholds
  await checkEmissionThresholds(env, source, emissions);
  
  // Invalidate cache
  await env.CARBON_CACHE.delete('dashboard');
  
  return c.json({
    success: true,
    record: {
      id,
      sourceId,
      quantity,
      unit: source.unit,
      emissions,
      emissionsUnit: 'kg CO2e',
      timestamp: timestamp || new Date().toISOString()
    }
  });
});

app.post('/carbon/emissions/bulk', async (c) => {
  const env = c.env;
  const { records } = await c.req.json();
  
  const results: any[] = [];
  
  for (const record of records) {
    const source = await env.DB.prepare(`
      SELECT * FROM emission_sources WHERE id = ?
    `).bind(record.sourceId).first() as any;
    
    if (source) {
      const emissions = record.quantity * source.emission_factor;
      const id = `ER-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
      
      await env.DB.prepare(`
        INSERT INTO emission_records (id, source_id, timestamp, quantity, emissions, metadata)
        VALUES (?, ?, ?, ?, ?, ?)
      `).bind(id, record.sourceId, record.timestamp, record.quantity, emissions, JSON.stringify(record.metadata || {})).run();
      
      results.push({ id, sourceId: record.sourceId, emissions, success: true });
    } else {
      results.push({ sourceId: record.sourceId, success: false, error: 'Source not found' });
    }
  }
  
  return c.json({
    success: true,
    processed: results.length,
    successful: results.filter(r => r.success).length,
    results
  });
});

// ===========================================
// EMISSION SOURCES MANAGEMENT
// ===========================================

app.get('/carbon/sources', async (c) => {
  const env = c.env;
  const scope = c.req.query('scope');
  
  let query = 'SELECT * FROM emission_sources';
  if (scope) {
    query += ` WHERE scope = ${parseInt(scope)}`;
  }
  query += ' ORDER BY scope, category, name';
  
  const sources = await env.DB.prepare(query).all();
  
  return c.json({
    success: true,
    sources: sources.results
  });
});

app.post('/carbon/sources', async (c) => {
  const env = c.env;
  const source = await c.req.json();
  
  const id = `ES-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  await env.DB.prepare(`
    INSERT INTO emission_sources (id, name, scope, category, unit, emission_factor, data_source, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    id,
    source.name,
    source.scope,
    source.category,
    source.unit,
    source.emissionFactor,
    source.dataSource
  ).run();
  
  return c.json({
    success: true,
    source: { id, ...source }
  });
});

// ===========================================
// ENERGY MONITORING
// ===========================================

app.get('/carbon/energy', async (c) => {
  const env = c.env;
  const year = parseInt(c.req.query('year') || new Date().getFullYear().toString());
  
  // Get energy consumption by source
  const consumption = await env.DB.prepare(`
    SELECT es.name, es.type, es.renewable, SUM(ec.kwh) as total_kwh, 
           SUM(ec.kwh * es.emission_factor) as emissions
    FROM energy_consumption ec
    JOIN energy_sources es ON ec.source_id = es.id
    WHERE strftime('%Y', ec.timestamp) = ?
    GROUP BY es.id
    ORDER BY total_kwh DESC
  `).bind(year.toString()).all();
  
  // Calculate totals
  const totalKwh = consumption.results.reduce((sum: number, c: any) => sum + c.total_kwh, 0);
  const renewableKwh = consumption.results
    .filter((c: any) => c.renewable)
    .reduce((sum: number, c: any) => sum + c.total_kwh, 0);
  
  // Get monthly trend
  const monthlyTrend = await env.DB.prepare(`
    SELECT strftime('%Y-%m', timestamp) as month, SUM(kwh) as total_kwh
    FROM energy_consumption
    WHERE strftime('%Y', timestamp) = ?
    GROUP BY month
    ORDER BY month
  `).bind(year.toString()).all();
  
  // Get cost data
  const costs = await env.DB.prepare(`
    SELECT SUM(cost) as total_cost FROM energy_consumption
    WHERE strftime('%Y', timestamp) = ?
  `).bind(year.toString()).first() as any;
  
  return c.json({
    success: true,
    energy: {
      year,
      totalConsumption: Math.round(totalKwh),
      renewableConsumption: Math.round(renewableKwh),
      renewablePercentage: totalKwh > 0 ? Math.round((renewableKwh / totalKwh) * 100) : 0,
      totalEmissions: consumption.results.reduce((sum: number, c: any) => sum + c.emissions, 0),
      totalCost: costs?.total_cost || 0,
      bySource: consumption.results,
      monthlyTrend: monthlyTrend.results
    }
  });
});

app.post('/carbon/energy/record', async (c) => {
  const env = c.env;
  const { sourceId, kwh, cost, timestamp, meterReading } = await c.req.json();
  
  const source = await env.DB.prepare(`
    SELECT * FROM energy_sources WHERE id = ?
  `).bind(sourceId).first() as any;
  
  if (!source) {
    return c.json({ success: false, error: 'Energy source not found' }, 404);
  }
  
  const id = `EC-${Date.now()}`;
  const emissions = kwh * source.emission_factor;
  
  await env.DB.prepare(`
    INSERT INTO energy_consumption (id, source_id, timestamp, kwh, cost, emissions, meter_reading)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `).bind(id, sourceId, timestamp || new Date().toISOString(), kwh, cost || 0, emissions, meterReading).run();
  
  // Also record as emission
  await env.DB.prepare(`
    INSERT INTO emission_records (id, source_id, timestamp, quantity, emissions, metadata)
    SELECT ?, es.id, ?, ?, ?, ?
    FROM emission_sources es WHERE es.name = 'Electricity'
  `).bind(`ER-${id}`, timestamp || new Date().toISOString(), kwh, emissions, JSON.stringify({ energySourceId: sourceId })).run();
  
  return c.json({
    success: true,
    record: {
      id,
      sourceId,
      kwh,
      emissions,
      cost,
      renewable: source.renewable
    }
  });
});

// ===========================================
// FLEET EMISSIONS
// ===========================================

app.get('/carbon/fleet', async (c) => {
  const env = c.env;
  
  // Get fleet overview
  const vehicles = await env.DB.prepare(`
    SELECT v.*, 
           (SELECT SUM(emissions) FROM fleet_trips t WHERE t.vehicle_id = v.id) as total_emissions,
           (SELECT SUM(distance) FROM fleet_trips t WHERE t.vehicle_id = v.id) as total_distance
    FROM fleet_vehicles v
    ORDER BY total_emissions DESC
  `).all();
  
  // Get fleet-wide stats
  const fleetStats = await env.DB.prepare(`
    SELECT 
      COUNT(DISTINCT vehicle_id) as vehicle_count,
      SUM(distance) as total_distance,
      SUM(fuel_used) as total_fuel,
      SUM(emissions) as total_emissions,
      AVG(emissions / NULLIF(distance, 0)) as avg_emissions_per_km
    FROM fleet_trips
    WHERE timestamp > datetime('now', '-365 days')
  `).first() as any;
  
  // Get EV vs ICE breakdown
  const vehicleTypes = await env.DB.prepare(`
    SELECT fuel_type, COUNT(*) as count, 
           (SELECT SUM(emissions) FROM fleet_trips t 
            JOIN fleet_vehicles v2 ON t.vehicle_id = v2.id 
            WHERE v2.fuel_type = v.fuel_type) as total_emissions
    FROM fleet_vehicles v
    GROUP BY fuel_type
  `).all();
  
  return c.json({
    success: true,
    fleet: {
      totalVehicles: fleetStats?.vehicle_count || 0,
      totalDistance: Math.round(fleetStats?.total_distance || 0),
      totalFuel: Math.round(fleetStats?.total_fuel || 0),
      totalEmissions: Math.round(fleetStats?.total_emissions || 0),
      avgEmissionsPerKm: Math.round((fleetStats?.avg_emissions_per_km || 0) * 1000) / 1000,
      vehicles: vehicles.results,
      byFuelType: vehicleTypes.results
    }
  });
});

app.post('/carbon/fleet/trip', async (c) => {
  const env = c.env;
  const { vehicleId, distance, fuelUsed, startLocation, endLocation, timestamp } = await c.req.json();
  
  // Get vehicle details
  const vehicle = await env.DB.prepare(`
    SELECT * FROM fleet_vehicles WHERE id = ?
  `).bind(vehicleId).first() as any;
  
  if (!vehicle) {
    return c.json({ success: false, error: 'Vehicle not found' }, 404);
  }
  
  // Calculate emissions
  let emissions: number;
  if (vehicle.fuel_type === 'electric') {
    // For EVs, calculate based on energy consumption
    const kwh = distance * (vehicle.energy_consumption || 0.2); // kWh per km
    emissions = kwh * (EMISSION_FACTORS['grid-us-avg'] as number);
  } else {
    // For ICE vehicles
    const emissionFactor = EMISSION_FACTORS[vehicle.fuel_type as keyof typeof EMISSION_FACTORS] || 2.31;
    emissions = fuelUsed * emissionFactor;
  }
  
  const id = `FT-${Date.now()}`;
  
  await env.DB.prepare(`
    INSERT INTO fleet_trips (id, vehicle_id, timestamp, distance, fuel_used, emissions, start_location, end_location)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(id, vehicleId, timestamp || new Date().toISOString(), distance, fuelUsed || 0, emissions, startLocation, endLocation).run();
  
  return c.json({
    success: true,
    trip: {
      id,
      vehicleId,
      distance,
      fuelUsed,
      emissions: Math.round(emissions * 100) / 100,
      emissionsUnit: 'kg CO2e'
    }
  });
});

// ===========================================
// SUPPLY CHAIN EMISSIONS (SCOPE 3)
// ===========================================

app.get('/carbon/supply-chain', async (c) => {
  const env = c.env;
  
  // Get supplier emissions
  const suppliers = await env.DB.prepare(`
    SELECT s.*, 
           (SELECT SUM(emissions) FROM supply_chain_emissions sce WHERE sce.supplier_id = s.id) as total_emissions
    FROM suppliers s
    ORDER BY total_emissions DESC
    LIMIT 20
  `).all();
  
  // Get emissions by category
  const byCategory = await env.DB.prepare(`
    SELECT category, SUM(emissions) as total_emissions
    FROM supply_chain_emissions
    WHERE timestamp > datetime('now', '-365 days')
    GROUP BY category
    ORDER BY total_emissions DESC
  `).all();
  
  // Get shipping emissions
  const shipping = await env.DB.prepare(`
    SELECT transport_mode, SUM(emissions) as total_emissions, SUM(distance) as total_distance
    FROM shipping_emissions
    WHERE timestamp > datetime('now', '-365 days')
    GROUP BY transport_mode
  `).all();
  
  return c.json({
    success: true,
    supplyChain: {
      topSuppliers: suppliers.results,
      byCategory: byCategory.results,
      shipping: shipping.results,
      totalScope3: byCategory.results.reduce((sum: number, c: any) => sum + c.total_emissions, 0) +
                   shipping.results.reduce((sum: number, s: any) => sum + s.total_emissions, 0)
    }
  });
});

app.post('/carbon/supply-chain/calculate', async (c) => {
  const env = c.env;
  const { supplierId, productId, quantity, transportMode, distance } = await c.req.json();
  
  // Get product emission factor
  const product = await env.DB.prepare(`
    SELECT * FROM products WHERE id = ?
  `).bind(productId).first() as any;
  
  // Calculate product emissions
  const productEmissions = quantity * (product?.carbon_footprint || 0);
  
  // Calculate transport emissions
  const transportFactor = EMISSION_FACTORS[`shipping-${transportMode}` as keyof typeof EMISSION_FACTORS] || 0.096;
  const weight = quantity * (product?.weight || 1); // kg
  const transportEmissions = (weight / 1000) * distance * transportFactor; // ton-km
  
  const totalEmissions = productEmissions + transportEmissions;
  
  const id = `SCE-${Date.now()}`;
  
  await env.DB.prepare(`
    INSERT INTO supply_chain_emissions (id, supplier_id, product_id, quantity, emissions, transport_emissions, timestamp, category)
    VALUES (?, ?, ?, ?, ?, ?, datetime('now'), ?)
  `).bind(id, supplierId, productId, quantity, totalEmissions, transportEmissions, product?.category || 'general').run();
  
  return c.json({
    success: true,
    emissions: {
      id,
      productEmissions: Math.round(productEmissions),
      transportEmissions: Math.round(transportEmissions),
      totalEmissions: Math.round(totalEmissions),
      unit: 'kg CO2e'
    }
  });
});

// ===========================================
// CARBON GOALS & TARGETS
// ===========================================

app.get('/carbon/goals', async (c) => {
  const env = c.env;
  
  const goals = await env.DB.prepare(`
    SELECT * FROM carbon_goals ORDER BY target_year
  `).all();
  
  // Calculate progress for each goal
  const goalsWithProgress = await Promise.all(
    goals.results.map(async (goal: any) => {
      const currentEmissions = await getCurrentEmissions(env, goal.scope);
      const reduction = ((goal.baseline_emissions - currentEmissions) / goal.baseline_emissions) * 100;
      const progress = (reduction / goal.target_reduction) * 100;
      
      return {
        ...goal,
        currentEmissions: Math.round(currentEmissions),
        currentReduction: Math.round(reduction * 10) / 10,
        progress: Math.min(100, Math.max(0, Math.round(progress))),
        status: progress >= 100 ? 'achieved' : 
                progress >= 75 ? 'on-track' : 
                progress >= 50 ? 'at-risk' : 'behind',
        remainingReduction: Math.max(0, goal.baseline_emissions * (goal.target_reduction / 100) - (goal.baseline_emissions - currentEmissions))
      };
    })
  );
  
  return c.json({
    success: true,
    goals: goalsWithProgress
  });
});

app.post('/carbon/goals', async (c) => {
  const env = c.env;
  const goal = await c.req.json();
  
  const id = `CG-${Date.now()}`;
  
  // Get baseline emissions
  const baselineEmissions = await getEmissionsForYear(env, goal.baselineYear, goal.scope);
  
  await env.DB.prepare(`
    INSERT INTO carbon_goals (id, name, target_year, baseline_year, baseline_emissions, target_reduction, scope, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(id, goal.name, goal.targetYear, goal.baselineYear, baselineEmissions, goal.targetReduction, goal.scope).run();
  
  return c.json({
    success: true,
    goal: {
      id,
      ...goal,
      baselineEmissions
    }
  });
});

// ===========================================
// CARBON OFFSETS
// ===========================================

app.get('/carbon/offsets/projects', async (c) => {
  const env = c.env;
  
  const projects = await env.DB.prepare(`
    SELECT * FROM offset_projects
    WHERE available_credits > 0
    ORDER BY price_per_ton ASC
  `).all();
  
  return c.json({
    success: true,
    projects: projects.results.map((p: any) => ({
      ...p,
      certifications: JSON.parse(p.certifications || '[]')
    }))
  });
});

app.post('/carbon/offsets/purchase', async (c) => {
  const env = c.env;
  const { projectId, tons, purpose } = await c.req.json();
  
  const project = await env.DB.prepare(`
    SELECT * FROM offset_projects WHERE id = ?
  `).bind(projectId).first() as any;
  
  if (!project) {
    return c.json({ success: false, error: 'Offset project not found' }, 404);
  }
  
  if (project.available_credits < tons) {
    return c.json({ success: false, error: 'Insufficient credits available' }, 400);
  }
  
  const cost = tons * project.price_per_ton;
  const id = `OFF-${Date.now()}`;
  
  // Record purchase
  await env.DB.prepare(`
    INSERT INTO offset_purchases (id, project_id, tons, cost, purpose, purchased_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(id, projectId, tons, cost, purpose).run();
  
  // Update available credits
  await env.DB.prepare(`
    UPDATE offset_projects SET available_credits = available_credits - ? WHERE id = ?
  `).bind(tons, projectId).run();
  
  return c.json({
    success: true,
    purchase: {
      id,
      projectId,
      projectName: project.name,
      tons,
      cost,
      co2Offset: tons * 1000, // kg CO2e
      certificate: `CERT-${id}`
    }
  });
});

app.get('/carbon/offsets/recommendations', async (c) => {
  const env = c.env;
  
  // Get current emissions gap
  const currentEmissions = await getCurrentEmissions(env, 'all');
  const goals = await env.DB.prepare(`
    SELECT * FROM carbon_goals WHERE target_year = strftime('%Y', 'now')
  `).all();
  
  let offsetNeeded = 0;
  for (const goal of goals.results as any[]) {
    const targetEmissions = goal.baseline_emissions * (1 - goal.target_reduction / 100);
    if (currentEmissions > targetEmissions) {
      offsetNeeded += currentEmissions - targetEmissions;
    }
  }
  
  // Get recommended projects
  const projects = await env.DB.prepare(`
    SELECT * FROM offset_projects
    WHERE available_credits > 0 AND verified = 1
    ORDER BY price_per_ton ASC
    LIMIT 5
  `).all();
  
  // AI recommendations
  const recommendations = await generateOffsetRecommendations(env, offsetNeeded, projects.results);
  
  return c.json({
    success: true,
    recommendations: {
      currentEmissions: Math.round(currentEmissions),
      offsetNeeded: Math.round(offsetNeeded),
      estimatedCost: Math.round(offsetNeeded * (projects.results[0] as any)?.price_per_ton || 0),
      recommendedProjects: projects.results,
      aiRecommendations: recommendations
    }
  });
});

// ===========================================
// ESG REPORTING
// ===========================================

app.post('/carbon/reports/generate', async (c) => {
  const env = c.env;
  const { year, framework } = await c.req.json();
  
  const reportId = `RPT-${Date.now()}`;
  
  // Gather all data
  const scopeEmissions = await getEmissionsByScope(env, year);
  const energyData = await getEnergyData(env, year);
  const goals = await getGoalProgress(env);
  const offsets = await getOffsetsPurchased(env, year);
  
  // Calculate key metrics
  const totalEmissions = scopeEmissions.scope1 + scopeEmissions.scope2 + scopeEmissions.scope3;
  const netEmissions = totalEmissions - offsets.totalOffset;
  
  // Generate report content based on framework
  const reportContent = await generateESGReport(env, {
    framework,
    year,
    scopeEmissions,
    energyData,
    goals,
    offsets,
    totalEmissions,
    netEmissions
  });
  
  // Store report
  await env.REPORTS_STORAGE.put(
    `reports/${year}/${reportId}.json`,
    JSON.stringify(reportContent),
    { customMetadata: { framework, year: year.toString() } }
  );
  
  // Record in DB
  await env.DB.prepare(`
    INSERT INTO carbon_reports (id, year, framework, generated_at, total_emissions, net_emissions)
    VALUES (?, ?, ?, datetime('now'), ?, ?)
  `).bind(reportId, year, framework, totalEmissions, netEmissions).run();
  
  return c.json({
    success: true,
    report: {
      id: reportId,
      framework,
      year,
      summary: {
        totalEmissions: Math.round(totalEmissions),
        netEmissions: Math.round(netEmissions),
        scope1: Math.round(scopeEmissions.scope1),
        scope2: Math.round(scopeEmissions.scope2),
        scope3: Math.round(scopeEmissions.scope3),
        renewablePercentage: energyData.renewablePercentage,
        carbonIntensity: reportContent.carbonIntensity,
        offsetsPurchased: offsets.totalOffset
      },
      downloadUrl: `/carbon/reports/${reportId}/download`
    }
  });
});

app.get('/carbon/reports/:reportId/download', async (c) => {
  const env = c.env;
  const reportId = c.req.param('reportId');
  
  // Get report metadata
  const report = await env.DB.prepare(`
    SELECT * FROM carbon_reports WHERE id = ?
  `).bind(reportId).first() as any;
  
  if (!report) {
    return c.json({ success: false, error: 'Report not found' }, 404);
  }
  
  // Get report content from R2
  const content = await env.REPORTS_STORAGE.get(`reports/${report.year}/${reportId}.json`);
  
  if (!content) {
    return c.json({ success: false, error: 'Report content not found' }, 404);
  }
  
  const reportData = await content.json();
  
  return c.json({
    success: true,
    report: reportData
  });
});

// ===========================================
// AI RECOMMENDATIONS
// ===========================================

app.get('/carbon/recommendations', async (c) => {
  const env = c.env;
  
  // Gather current state
  const currentEmissions = await getCurrentEmissions(env, 'all');
  const topSources = await env.DB.prepare(`
    SELECT es.name, es.category, es.scope, SUM(er.emissions) as total
    FROM emission_records er
    JOIN emission_sources es ON er.source_id = es.id
    WHERE er.timestamp > datetime('now', '-365 days')
    GROUP BY es.id
    ORDER BY total DESC
    LIMIT 10
  `).all();
  
  const energyMix = await calculateEnergyMix(env, new Date().getFullYear());
  const goals = await env.DB.prepare(`SELECT * FROM carbon_goals`).all();
  
  // Generate AI recommendations
  const prompt = `Analyze this carbon footprint data and provide specific, actionable recommendations:

Current Annual Emissions: ${currentEmissions} kg CO2e
Top Emission Sources:
${topSources.results.map((s: any) => `- ${s.name} (Scope ${s.scope}): ${s.total} kg CO2e`).join('\n')}

Renewable Energy: ${energyMix.renewablePercentage}%
Carbon Goals: ${goals.results.map((g: any) => `${g.name}: ${g.target_reduction}% by ${g.target_year}`).join(', ')}

Provide 5 specific recommendations with estimated CO2 reduction potential.`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 1000
    });
    
    // Parse AI response into structured recommendations
    const recommendations = parseAIRecommendations(response.response, topSources.results);
    
    return c.json({
      success: true,
      recommendations,
      analysis: {
        currentEmissions,
        topSources: topSources.results,
        renewablePercentage: energyMix.renewablePercentage,
        biggestOpportunity: topSources.results[0]
      }
    });
  } catch (error) {
    // Fallback recommendations
    return c.json({
      success: true,
      recommendations: generateFallbackRecommendations(topSources.results, energyMix),
      analysis: {
        currentEmissions,
        topSources: topSources.results,
        renewablePercentage: energyMix.renewablePercentage
      }
    });
  }
});

// ===========================================
// HELPER FUNCTIONS
// ===========================================

async function calculateEnergyMix(env: Env, year: number): Promise<any> {
  const mix = await env.DB.prepare(`
    SELECT es.renewable, SUM(ec.kwh) as total_kwh
    FROM energy_consumption ec
    JOIN energy_sources es ON ec.source_id = es.id
    WHERE strftime('%Y', ec.timestamp) = ?
    GROUP BY es.renewable
  `).bind(year.toString()).all();
  
  const total = mix.results.reduce((sum: number, m: any) => sum + m.total_kwh, 0);
  const renewable = mix.results.find((m: any) => m.renewable)?.total_kwh || 0;
  
  return {
    totalKwh: total,
    renewableKwh: renewable,
    renewablePercentage: total > 0 ? Math.round((renewable / total) * 100) : 0
  };
}

async function checkEmissionThresholds(env: Env, source: any, emissions: number): Promise<void> {
  // Check if emissions exceed threshold for alerting
  const threshold = await env.DB.prepare(`
    SELECT * FROM emission_thresholds WHERE source_id = ?
  `).bind(source.id).first() as any;
  
  if (threshold && emissions > threshold.limit) {
    await env.ALERT_QUEUE.send({
      type: 'emission_threshold_exceeded',
      sourceId: source.id,
      sourceName: source.name,
      emissions,
      threshold: threshold.limit,
      timestamp: new Date().toISOString()
    });
  }
}

async function getCurrentEmissions(env: Env, scope: string | number): Promise<number> {
  let query = `
    SELECT SUM(er.emissions) as total
    FROM emission_records er
    JOIN emission_sources es ON er.source_id = es.id
    WHERE er.timestamp > datetime('now', '-365 days')
  `;
  
  if (scope !== 'all') {
    query += ` AND es.scope = ${scope}`;
  }
  
  const result = await env.DB.prepare(query).first() as any;
  return result?.total || 0;
}

async function getEmissionsForYear(env: Env, year: number, scope: string | number): Promise<number> {
  let query = `
    SELECT SUM(er.emissions) as total
    FROM emission_records er
    JOIN emission_sources es ON er.source_id = es.id
    WHERE strftime('%Y', er.timestamp) = ?
  `;
  
  if (scope !== 'all') {
    query += ` AND es.scope = ${scope}`;
  }
  
  const result = await env.DB.prepare(query).bind(year.toString()).first() as any;
  return result?.total || 0;
}

async function getEmissionsByScope(env: Env, year: number): Promise<any> {
  const results = await env.DB.prepare(`
    SELECT es.scope, SUM(er.emissions) as total
    FROM emission_records er
    JOIN emission_sources es ON er.source_id = es.id
    WHERE strftime('%Y', er.timestamp) = ?
    GROUP BY es.scope
  `).bind(year.toString()).all();
  
  return {
    scope1: results.results.find((r: any) => r.scope === 1)?.total || 0,
    scope2: results.results.find((r: any) => r.scope === 2)?.total || 0,
    scope3: results.results.find((r: any) => r.scope === 3)?.total || 0
  };
}

async function getEnergyData(env: Env, year: number): Promise<any> {
  const energy = await env.DB.prepare(`
    SELECT SUM(kwh) as total_kwh, SUM(cost) as total_cost, SUM(emissions) as total_emissions
    FROM energy_consumption
    WHERE strftime('%Y', timestamp) = ?
  `).bind(year.toString()).first() as any;
  
  const mix = await calculateEnergyMix(env, year);
  
  return {
    totalKwh: energy?.total_kwh || 0,
    totalCost: energy?.total_cost || 0,
    totalEmissions: energy?.total_emissions || 0,
    renewablePercentage: mix.renewablePercentage
  };
}

async function getGoalProgress(env: Env): Promise<any[]> {
  const goals = await env.DB.prepare(`SELECT * FROM carbon_goals`).all();
  return goals.results;
}

async function getOffsetsPurchased(env: Env, year: number): Promise<any> {
  const offsets = await env.DB.prepare(`
    SELECT SUM(tons) as total_tons, SUM(cost) as total_cost
    FROM offset_purchases
    WHERE strftime('%Y', purchased_at) = ?
  `).bind(year.toString()).first() as any;
  
  return {
    totalOffset: (offsets?.total_tons || 0) * 1000, // kg CO2e
    totalCost: offsets?.total_cost || 0
  };
}

async function generateESGReport(env: Env, data: any): Promise<any> {
  return {
    ...data,
    carbonIntensity: data.totalEmissions / 1000000, // placeholder
    methodology: 'GHG Protocol',
    generatedAt: new Date().toISOString(),
    verified: false
  };
}

async function generateOffsetRecommendations(env: Env, offsetNeeded: number, projects: any[]): Promise<string[]> {
  const recommendations: string[] = [];
  
  if (offsetNeeded > 0) {
    recommendations.push(`Consider purchasing ${Math.round(offsetNeeded / 1000)} tons of carbon offsets to meet your current year goals.`);
  }
  
  if (projects.length > 0) {
    const cheapest = projects[0] as any;
    recommendations.push(`Most cost-effective option: ${cheapest.name} at $${cheapest.price_per_ton}/ton`);
  }
  
  recommendations.push('Prioritize emission reductions before purchasing offsets for maximum impact.');
  
  return recommendations;
}

function parseAIRecommendations(response: string, topSources: any[]): any[] {
  // Parse AI response into structured format
  const recommendations = response.split('\n')
    .filter(line => line.trim().startsWith('-') || line.trim().match(/^\d+\./))
    .slice(0, 5)
    .map((line, index) => ({
      id: index + 1,
      recommendation: line.replace(/^[\d\.\-\s]+/, '').trim(),
      priority: index < 2 ? 'high' : index < 4 ? 'medium' : 'low',
      estimatedImpact: 'TBD'
    }));
  
  return recommendations.length > 0 ? recommendations : generateFallbackRecommendations(topSources, { renewablePercentage: 0 });
}

function generateFallbackRecommendations(topSources: any[], energyMix: any): any[] {
  const recommendations = [];
  
  if (energyMix.renewablePercentage < 50) {
    recommendations.push({
      id: 1,
      recommendation: 'Increase renewable energy procurement to reduce Scope 2 emissions',
      priority: 'high',
      estimatedImpact: '20-40% reduction in Scope 2'
    });
  }
  
  recommendations.push({
    id: 2,
    recommendation: 'Implement energy efficiency measures in facilities',
    priority: 'high',
    estimatedImpact: '10-15% reduction in energy consumption'
  });
  
  recommendations.push({
    id: 3,
    recommendation: 'Transition fleet vehicles to electric',
    priority: 'medium',
    estimatedImpact: '50-70% reduction in fleet emissions'
  });
  
  recommendations.push({
    id: 4,
    recommendation: 'Engage suppliers on their carbon reduction efforts',
    priority: 'medium',
    estimatedImpact: '10-20% reduction in Scope 3'
  });
  
  recommendations.push({
    id: 5,
    recommendation: 'Implement smart building management systems',
    priority: 'low',
    estimatedImpact: '5-10% energy savings'
  });
  
  return recommendations;
}

export default {
  fetch: app.fetch,
  async queue(batch: MessageBatch, env: Env) {
    for (const message of batch.messages) {
      const data = message.body as any;
      
      if (data.type === 'emission_threshold_exceeded') {
        console.log('Emission threshold alert:', data);
        // Integrate with alerting system
      }
      
      message.ack();
    }
  }
};
