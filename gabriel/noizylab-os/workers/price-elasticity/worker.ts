/**
 * NoizyLab OS - Price Elasticity Worker
 * Dynamic Pricing & Demand Optimization Engine
 * 
 * Features:
 * - Real-time price elasticity calculation
 * - Demand curve modeling
 * - Competitor price monitoring
 * - Revenue optimization algorithms
 * - Price sensitivity analysis
 * - A/B pricing experiments
 * - Seasonal pricing adjustments
 * - Customer segment pricing
 */

import { Hono } from 'hono';

interface Env {
  PRICING_KV: KVNamespace;
  DB: D1Database;
  AI: Ai;
}

interface PricePoint {
  price: number;
  demand: number;
  revenue: number;
  timestamp: Date;
  context: PriceContext;
}

interface PriceContext {
  season: string;
  dayOfWeek: number;
  competitorPrices: number[];
  inventoryLevel: number;
  marketTrend: string;
  customerSegment?: string;
}

interface ElasticityModel {
  productId: string;
  baseElasticity: number;
  seasonalFactors: Map<string, number>;
  segmentFactors: Map<string, number>;
  crossPriceElasticities: Map<string, number>;
  timeDecay: number;
  confidenceInterval: { lower: number; upper: number };
  modelR2: number;
  lastUpdated: Date;
}

interface DemandCurve {
  productId: string;
  curveType: 'linear' | 'log-linear' | 'exponential' | 'sigmoid';
  parameters: CurveParameters;
  priceRange: { min: number; max: number };
  optimalPrice: number;
  maxRevenue: number;
}

interface CurveParameters {
  a: number;  // Intercept or scale
  b: number;  // Slope or elasticity
  c?: number; // Additional parameter for complex curves
  d?: number; // Asymptote parameter
}

interface PricingExperiment {
  id: string;
  productId: string;
  name: string;
  variants: PriceVariant[];
  startDate: Date;
  endDate?: Date;
  status: 'draft' | 'running' | 'completed' | 'paused';
  results?: ExperimentResults;
}

interface PriceVariant {
  id: string;
  name: string;
  price: number;
  allocation: number;  // Percentage of traffic
  conversions: number;
  impressions: number;
  revenue: number;
}

interface ExperimentResults {
  winner: string;
  confidence: number;
  liftPercent: number;
  statisticalSignificance: boolean;
  revenueImpact: number;
  recommendation: string;
}

interface CompetitorIntel {
  competitorId: string;
  competitorName: string;
  productId: string;
  price: number;
  lastChecked: Date;
  priceHistory: { price: number; date: Date }[];
  pricingStrategy: string;
}

interface OptimizationResult {
  productId: string;
  currentPrice: number;
  recommendedPrice: number;
  expectedDemandChange: number;
  expectedRevenueChange: number;
  confidence: number;
  constraints: string[];
  reasoning: string[];
}

interface SegmentPricing {
  segmentId: string;
  segmentName: string;
  characteristics: Record<string, any>;
  priceMultiplier: number;
  elasticity: number;
  lifetime_value: number;
  churnRisk: number;
  recommendedPrice: number;
}

const app = new Hono<{ Bindings: Env }>();

// ==================== ELASTICITY CALCULATION ====================

app.post('/elasticity/calculate', async (c) => {
  const { productId, priceHistory, demandHistory, period = 90 } = await c.req.json();
  
  // Filter to relevant period
  const cutoffDate = new Date(Date.now() - period * 24 * 60 * 60 * 1000);
  const relevantData = priceHistory
    .map((p: any, i: number) => ({
      price: p.price,
      demand: demandHistory[i]?.quantity || 0,
      date: new Date(p.date)
    }))
    .filter((d: any) => d.date >= cutoffDate);
  
  if (relevantData.length < 10) {
    return c.json({ error: 'Insufficient data points for elasticity calculation' }, 400);
  }
  
  // Calculate point elasticity using midpoint method
  const elasticities = [];
  for (let i = 1; i < relevantData.length; i++) {
    const prev = relevantData[i - 1];
    const curr = relevantData[i];
    
    if (prev.price !== curr.price && prev.price > 0 && curr.price > 0) {
      const priceChange = (curr.price - prev.price) / ((curr.price + prev.price) / 2);
      const demandChange = (curr.demand - prev.demand) / ((curr.demand + prev.demand) / 2 || 1);
      
      if (priceChange !== 0) {
        elasticities.push(demandChange / priceChange);
      }
    }
  }
  
  if (elasticities.length === 0) {
    return c.json({ error: 'No price variations found in data' }, 400);
  }
  
  // Calculate statistics
  const avgElasticity = elasticities.reduce((a, b) => a + b, 0) / elasticities.length;
  const variance = elasticities.reduce((sum, e) => sum + Math.pow(e - avgElasticity, 2), 0) / elasticities.length;
  const stdDev = Math.sqrt(variance);
  
  // Build model
  const model: ElasticityModel = {
    productId,
    baseElasticity: avgElasticity,
    seasonalFactors: await calculateSeasonalFactors(relevantData),
    segmentFactors: new Map(),
    crossPriceElasticities: new Map(),
    timeDecay: 0.95,
    confidenceInterval: {
      lower: avgElasticity - 1.96 * stdDev,
      upper: avgElasticity + 1.96 * stdDev
    },
    modelR2: calculateR2(relevantData, avgElasticity),
    lastUpdated: new Date()
  };
  
  // Store model
  await c.env.PRICING_KV.put(`elasticity:${productId}`, JSON.stringify(model));
  
  // Interpret elasticity
  const interpretation = interpretElasticity(avgElasticity);
  
  return c.json({
    productId,
    elasticity: avgElasticity,
    interpretation,
    confidence: model.modelR2,
    confidenceInterval: model.confidenceInterval,
    dataPoints: relevantData.length,
    recommendations: generateElasticityRecommendations(avgElasticity)
  });
});

app.get('/elasticity/:productId', async (c) => {
  const productId = c.req.param('productId');
  const modelJson = await c.env.PRICING_KV.get(`elasticity:${productId}`);
  
  if (!modelJson) {
    return c.json({ error: 'No elasticity model found for product' }, 404);
  }
  
  const model: ElasticityModel = JSON.parse(modelJson);
  
  return c.json({
    ...model,
    interpretation: interpretElasticity(model.baseElasticity),
    recommendations: generateElasticityRecommendations(model.baseElasticity)
  });
});

// ==================== DEMAND CURVE MODELING ====================

app.post('/demand-curve/fit', async (c) => {
  const { productId, pricePoints } = await c.req.json();
  
  // Fit multiple curve types and select best
  const curves: DemandCurve[] = [];
  
  // Linear: Q = a - bP
  const linearFit = fitLinearCurve(pricePoints);
  curves.push(linearFit);
  
  // Log-linear: ln(Q) = a - b*ln(P)
  const logLinearFit = fitLogLinearCurve(pricePoints);
  curves.push(logLinearFit);
  
  // Exponential: Q = a * e^(-bP)
  const exponentialFit = fitExponentialCurve(pricePoints);
  curves.push(exponentialFit);
  
  // Select best fit based on R²
  const bestCurve = curves.reduce((best, curr) => 
    calculateCurveFit(curr, pricePoints) > calculateCurveFit(best, pricePoints) ? curr : best
  );
  
  bestCurve.productId = productId;
  
  // Calculate optimal price
  bestCurve.optimalPrice = findOptimalPrice(bestCurve);
  bestCurve.maxRevenue = calculateRevenue(bestCurve, bestCurve.optimalPrice);
  
  // Store curve
  await c.env.PRICING_KV.put(`demandcurve:${productId}`, JSON.stringify(bestCurve));
  
  // Store in D1
  await c.env.DB.prepare(`
    INSERT INTO demand_curves (product_id, curve_type, parameters, optimal_price, max_revenue, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
    ON CONFLICT(product_id) DO UPDATE SET
      curve_type = excluded.curve_type,
      parameters = excluded.parameters,
      optimal_price = excluded.optimal_price,
      max_revenue = excluded.max_revenue
  `).bind(
    productId,
    bestCurve.curveType,
    JSON.stringify(bestCurve.parameters),
    bestCurve.optimalPrice,
    bestCurve.maxRevenue
  ).run();
  
  return c.json({
    productId,
    bestFit: bestCurve,
    allCurves: curves.map(c => ({
      type: c.curveType,
      fit: calculateCurveFit(c, pricePoints),
      optimalPrice: findOptimalPrice(c)
    })),
    priceRecommendation: {
      optimal: bestCurve.optimalPrice,
      range: {
        min: bestCurve.optimalPrice * 0.9,
        max: bestCurve.optimalPrice * 1.1
      }
    }
  });
});

app.post('/demand-curve/predict', async (c) => {
  const { productId, prices } = await c.req.json();
  
  const curveJson = await c.env.PRICING_KV.get(`demandcurve:${productId}`);
  if (!curveJson) {
    return c.json({ error: 'No demand curve found' }, 404);
  }
  
  const curve: DemandCurve = JSON.parse(curveJson);
  
  const predictions = prices.map((price: number) => ({
    price,
    predictedDemand: predictDemand(curve, price),
    predictedRevenue: calculateRevenue(curve, price),
    vsOptimal: {
      demandDiff: predictDemand(curve, price) - predictDemand(curve, curve.optimalPrice),
      revenueDiff: calculateRevenue(curve, price) - curve.maxRevenue,
      revenueDiffPercent: ((calculateRevenue(curve, price) - curve.maxRevenue) / curve.maxRevenue) * 100
    }
  }));
  
  return c.json({
    productId,
    curveType: curve.curveType,
    predictions,
    optimalPrice: curve.optimalPrice,
    maxRevenue: curve.maxRevenue
  });
});

// ==================== PRICE OPTIMIZATION ====================

app.post('/optimize', async (c) => {
  const { productId, constraints, objectives } = await c.req.json();
  
  // Get elasticity model
  const elasticityJson = await c.env.PRICING_KV.get(`elasticity:${productId}`);
  const curveJson = await c.env.PRICING_KV.get(`demandcurve:${productId}`);
  
  if (!elasticityJson && !curveJson) {
    return c.json({ error: 'No pricing models found. Calculate elasticity or fit demand curve first.' }, 404);
  }
  
  // Get current pricing
  const currentPriceResult = await c.env.DB.prepare(`
    SELECT current_price, cost FROM products WHERE id = ?
  `).bind(productId).first();
  
  const currentPrice = currentPriceResult?.current_price || constraints.currentPrice || 100;
  const cost = currentPriceResult?.cost || constraints.cost || 0;
  
  // Get competitor prices
  const competitorPrices = await getCompetitorPrices(c.env, productId);
  
  // Optimization logic
  let recommendedPrice = currentPrice;
  const reasoning: string[] = [];
  
  if (curveJson) {
    const curve: DemandCurve = JSON.parse(curveJson);
    
    // Start with optimal from demand curve
    recommendedPrice = curve.optimalPrice;
    reasoning.push(`Demand curve suggests optimal price of $${curve.optimalPrice.toFixed(2)}`);
    
    // Apply constraints
    if (constraints.minMargin) {
      const minPrice = cost / (1 - constraints.minMargin);
      if (recommendedPrice < minPrice) {
        recommendedPrice = minPrice;
        reasoning.push(`Adjusted to $${minPrice.toFixed(2)} to maintain ${(constraints.minMargin * 100).toFixed(0)}% margin`);
      }
    }
    
    if (constraints.maxPrice && recommendedPrice > constraints.maxPrice) {
      recommendedPrice = constraints.maxPrice;
      reasoning.push(`Capped at maximum price constraint of $${constraints.maxPrice.toFixed(2)}`);
    }
    
    if (constraints.minPrice && recommendedPrice < constraints.minPrice) {
      recommendedPrice = constraints.minPrice;
      reasoning.push(`Raised to minimum price constraint of $${constraints.minPrice.toFixed(2)}`);
    }
  }
  
  // Competitor adjustment
  if (competitorPrices.length > 0 && constraints.competitorStrategy) {
    const avgCompetitorPrice = competitorPrices.reduce((a, b) => a + b, 0) / competitorPrices.length;
    
    switch (constraints.competitorStrategy) {
      case 'match':
        recommendedPrice = avgCompetitorPrice;
        reasoning.push(`Matched average competitor price of $${avgCompetitorPrice.toFixed(2)}`);
        break;
      case 'undercut':
        recommendedPrice = Math.min(recommendedPrice, avgCompetitorPrice * 0.95);
        reasoning.push(`Undercut competitors by 5%`);
        break;
      case 'premium':
        recommendedPrice = Math.max(recommendedPrice, avgCompetitorPrice * 1.1);
        reasoning.push(`Premium positioning 10% above competitors`);
        break;
    }
  }
  
  // Calculate expected impact
  const elasticity = elasticityJson ? JSON.parse(elasticityJson).baseElasticity : -1.5;
  const priceChangePercent = (recommendedPrice - currentPrice) / currentPrice;
  const expectedDemandChange = priceChangePercent * elasticity;
  const currentRevenue = currentPrice * 100; // Assume base demand of 100
  const newRevenue = recommendedPrice * (100 * (1 + expectedDemandChange));
  const expectedRevenueChange = (newRevenue - currentRevenue) / currentRevenue;
  
  const result: OptimizationResult = {
    productId,
    currentPrice,
    recommendedPrice,
    expectedDemandChange,
    expectedRevenueChange,
    confidence: curveJson ? 0.85 : 0.65,
    constraints: Object.keys(constraints),
    reasoning
  };
  
  // Log optimization
  await c.env.DB.prepare(`
    INSERT INTO price_optimizations (product_id, current_price, recommended_price, expected_revenue_change, created_at)
    VALUES (?, ?, ?, ?, datetime('now'))
  `).bind(productId, currentPrice, recommendedPrice, expectedRevenueChange).run();
  
  return c.json(result);
});

// ==================== A/B PRICING EXPERIMENTS ====================

app.post('/experiment/create', async (c) => {
  const { productId, name, variants, startDate } = await c.req.json();
  
  const experiment: PricingExperiment = {
    id: `exp_${Date.now()}`,
    productId,
    name,
    variants: variants.map((v: any, i: number) => ({
      id: `var_${i}`,
      name: v.name || `Variant ${i + 1}`,
      price: v.price,
      allocation: v.allocation || 100 / variants.length,
      conversions: 0,
      impressions: 0,
      revenue: 0
    })),
    startDate: new Date(startDate || Date.now()),
    status: 'draft'
  };
  
  // Validate allocations sum to 100
  const totalAllocation = experiment.variants.reduce((sum, v) => sum + v.allocation, 0);
  if (Math.abs(totalAllocation - 100) > 0.1) {
    return c.json({ error: 'Variant allocations must sum to 100%' }, 400);
  }
  
  // Store experiment
  await c.env.PRICING_KV.put(`experiment:${experiment.id}`, JSON.stringify(experiment));
  
  return c.json({
    success: true,
    experiment: {
      id: experiment.id,
      name: experiment.name,
      variants: experiment.variants,
      status: experiment.status
    }
  });
});

app.post('/experiment/:experimentId/start', async (c) => {
  const experimentId = c.req.param('experimentId');
  const expJson = await c.env.PRICING_KV.get(`experiment:${experimentId}`);
  
  if (!expJson) {
    return c.json({ error: 'Experiment not found' }, 404);
  }
  
  const experiment: PricingExperiment = JSON.parse(expJson);
  experiment.status = 'running';
  experiment.startDate = new Date();
  
  await c.env.PRICING_KV.put(`experiment:${experimentId}`, JSON.stringify(experiment));
  
  return c.json({
    success: true,
    experimentId,
    status: 'running',
    startDate: experiment.startDate
  });
});

app.post('/experiment/:experimentId/record', async (c) => {
  const experimentId = c.req.param('experimentId');
  const { variantId, event, revenue } = await c.req.json();
  
  const expJson = await c.env.PRICING_KV.get(`experiment:${experimentId}`);
  if (!expJson) {
    return c.json({ error: 'Experiment not found' }, 404);
  }
  
  const experiment: PricingExperiment = JSON.parse(expJson);
  const variant = experiment.variants.find(v => v.id === variantId);
  
  if (!variant) {
    return c.json({ error: 'Variant not found' }, 404);
  }
  
  if (event === 'impression') {
    variant.impressions++;
  } else if (event === 'conversion') {
    variant.conversions++;
    variant.revenue += revenue || variant.price;
  }
  
  await c.env.PRICING_KV.put(`experiment:${experimentId}`, JSON.stringify(experiment));
  
  return c.json({ success: true, variantId, event });
});

app.get('/experiment/:experimentId/assign', async (c) => {
  const experimentId = c.req.param('experimentId');
  const userId = c.req.query('userId') || `anon_${Math.random().toString(36).substr(2, 9)}`;
  
  const expJson = await c.env.PRICING_KV.get(`experiment:${experimentId}`);
  if (!expJson) {
    return c.json({ error: 'Experiment not found' }, 404);
  }
  
  const experiment: PricingExperiment = JSON.parse(expJson);
  
  if (experiment.status !== 'running') {
    return c.json({ error: 'Experiment is not running' }, 400);
  }
  
  // Check for existing assignment
  const existingAssignment = await c.env.PRICING_KV.get(`assignment:${experimentId}:${userId}`);
  if (existingAssignment) {
    const variant = experiment.variants.find(v => v.id === existingAssignment);
    return c.json({ variantId: existingAssignment, price: variant?.price });
  }
  
  // Assign based on allocation
  const random = Math.random() * 100;
  let cumulative = 0;
  let assignedVariant = experiment.variants[0];
  
  for (const variant of experiment.variants) {
    cumulative += variant.allocation;
    if (random < cumulative) {
      assignedVariant = variant;
      break;
    }
  }
  
  // Store assignment
  await c.env.PRICING_KV.put(`assignment:${experimentId}:${userId}`, assignedVariant.id, { expirationTtl: 86400 * 30 });
  
  return c.json({
    variantId: assignedVariant.id,
    price: assignedVariant.price
  });
});

app.get('/experiment/:experimentId/results', async (c) => {
  const experimentId = c.req.param('experimentId');
  const expJson = await c.env.PRICING_KV.get(`experiment:${experimentId}`);
  
  if (!expJson) {
    return c.json({ error: 'Experiment not found' }, 404);
  }
  
  const experiment: PricingExperiment = JSON.parse(expJson);
  
  // Calculate statistics
  const results = analyzeExperimentResults(experiment);
  
  return c.json({
    experimentId,
    name: experiment.name,
    status: experiment.status,
    variants: experiment.variants.map(v => ({
      ...v,
      conversionRate: v.impressions > 0 ? v.conversions / v.impressions : 0,
      revenuePerImpression: v.impressions > 0 ? v.revenue / v.impressions : 0
    })),
    analysis: results,
    sampleSizeRecommendation: calculateRequiredSampleSize(experiment)
  });
});

// ==================== COMPETITOR MONITORING ====================

app.post('/competitor/track', async (c) => {
  const { productId, competitorId, competitorName, price, url } = await c.req.json();
  
  const key = `competitor:${productId}:${competitorId}`;
  const existingJson = await c.env.PRICING_KV.get(key);
  
  let intel: CompetitorIntel;
  
  if (existingJson) {
    intel = JSON.parse(existingJson);
    intel.priceHistory.push({ price: intel.price, date: intel.lastChecked });
    intel.price = price;
    intel.lastChecked = new Date();
  } else {
    intel = {
      competitorId,
      competitorName,
      productId,
      price,
      lastChecked: new Date(),
      priceHistory: [],
      pricingStrategy: 'unknown'
    };
  }
  
  // Analyze pricing strategy if enough history
  if (intel.priceHistory.length >= 10) {
    intel.pricingStrategy = analyzePricingStrategy(intel.priceHistory);
  }
  
  await c.env.PRICING_KV.put(key, JSON.stringify(intel));
  
  // Store in D1
  await c.env.DB.prepare(`
    INSERT INTO competitor_prices (product_id, competitor_id, competitor_name, price, checked_at)
    VALUES (?, ?, ?, ?, datetime('now'))
  `).bind(productId, competitorId, competitorName, price).run();
  
  return c.json({
    success: true,
    intel: {
      competitorId,
      competitorName,
      currentPrice: price,
      strategy: intel.pricingStrategy,
      priceHistoryCount: intel.priceHistory.length
    }
  });
});

app.get('/competitor/:productId', async (c) => {
  const productId = c.req.param('productId');
  
  // Get all competitor data for product
  const competitors = await c.env.DB.prepare(`
    SELECT competitor_id, competitor_name, price, checked_at
    FROM competitor_prices
    WHERE product_id = ?
    ORDER BY checked_at DESC
  `).bind(productId).all();
  
  // Group by competitor
  const competitorMap = new Map<string, any>();
  for (const row of competitors.results || []) {
    if (!competitorMap.has(row.competitor_id as string)) {
      competitorMap.set(row.competitor_id as string, {
        competitorId: row.competitor_id,
        competitorName: row.competitor_name,
        currentPrice: row.price,
        lastChecked: row.checked_at,
        priceHistory: []
      });
    }
    competitorMap.get(row.competitor_id as string).priceHistory.push({
      price: row.price,
      date: row.checked_at
    });
  }
  
  const competitorList = Array.from(competitorMap.values());
  
  // Calculate market position
  const prices = competitorList.map(c => c.currentPrice);
  const avgPrice = prices.length > 0 ? prices.reduce((a, b) => a + b, 0) / prices.length : 0;
  const minPrice = prices.length > 0 ? Math.min(...prices) : 0;
  const maxPrice = prices.length > 0 ? Math.max(...prices) : 0;
  
  return c.json({
    productId,
    competitors: competitorList,
    marketAnalysis: {
      averagePrice: avgPrice,
      priceRange: { min: minPrice, max: maxPrice },
      competitorCount: competitorList.length
    },
    recommendations: generateCompetitorRecommendations(competitorList, avgPrice)
  });
});

// ==================== SEGMENT PRICING ====================

app.post('/segment/analyze', async (c) => {
  const { productId, segments } = await c.req.json();
  
  const segmentPricings: SegmentPricing[] = [];
  
  for (const segment of segments) {
    // Get segment purchase history
    const purchaseData = await c.env.DB.prepare(`
      SELECT price, quantity, customer_segment
      FROM order_items oi
      JOIN orders o ON oi.order_id = o.id
      JOIN customers c ON o.customer_id = c.id
      WHERE oi.product_id = ? AND c.segment = ?
    `).bind(productId, segment.id).all();
    
    // Calculate segment-specific elasticity
    const segmentElasticity = calculateSegmentElasticity(purchaseData.results || []);
    
    // Calculate price sensitivity
    const sensitivity = Math.abs(segmentElasticity);
    
    // Determine optimal price multiplier
    let priceMultiplier = 1;
    if (sensitivity < 1) {
      // Inelastic - can charge premium
      priceMultiplier = 1.1 + (1 - sensitivity) * 0.2;
    } else if (sensitivity > 2) {
      // Highly elastic - need competitive price
      priceMultiplier = 0.9 - (sensitivity - 2) * 0.1;
    }
    
    // Get base price
    const basePriceResult = await c.env.DB.prepare(`
      SELECT current_price FROM products WHERE id = ?
    `).bind(productId).first();
    const basePrice = (basePriceResult?.current_price as number) || 100;
    
    segmentPricings.push({
      segmentId: segment.id,
      segmentName: segment.name,
      characteristics: segment.characteristics || {},
      priceMultiplier,
      elasticity: segmentElasticity,
      lifetime_value: segment.ltv || 0,
      churnRisk: segment.churnRisk || 0.1,
      recommendedPrice: basePrice * priceMultiplier
    });
  }
  
  // Store segment analysis
  await c.env.PRICING_KV.put(`segments:${productId}`, JSON.stringify(segmentPricings));
  
  return c.json({
    productId,
    segmentAnalysis: segmentPricings,
    recommendations: segmentPricings.map(s => ({
      segment: s.segmentName,
      action: s.priceMultiplier > 1 ? 'Premium pricing opportunity' : 'Competitive pricing needed',
      suggestedPrice: s.recommendedPrice,
      expectedImpact: `${((s.priceMultiplier - 1) * 100).toFixed(1)}% price adjustment`
    }))
  });
});

// ==================== SEASONAL PRICING ====================

app.post('/seasonal/analyze', async (c) => {
  const { productId, historicalData } = await c.req.json();
  
  // Group data by month
  const monthlyData: Map<number, { sales: number; avgPrice: number; count: number }> = new Map();
  
  for (const record of historicalData) {
    const month = new Date(record.date).getMonth();
    const existing = monthlyData.get(month) || { sales: 0, avgPrice: 0, count: 0 };
    existing.sales += record.quantity;
    existing.avgPrice = (existing.avgPrice * existing.count + record.price) / (existing.count + 1);
    existing.count++;
    monthlyData.set(month, existing);
  }
  
  // Calculate seasonal indices
  const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const avgSales = Array.from(monthlyData.values()).reduce((sum, m) => sum + m.sales, 0) / 12;
  
  const seasonalFactors = monthNames.map((name, i) => {
    const monthData = monthlyData.get(i);
    const index = monthData ? monthData.sales / avgSales : 1;
    
    // Price recommendation based on demand
    let priceRecommendation: string;
    if (index > 1.2) {
      priceRecommendation = 'Premium pricing (high demand season)';
    } else if (index < 0.8) {
      priceRecommendation = 'Promotional pricing (low demand season)';
    } else {
      priceRecommendation = 'Standard pricing';
    }
    
    return {
      month: name,
      seasonalIndex: index,
      pricingMultiplier: 0.9 + index * 0.2,  // Range from 0.7 to 1.3
      recommendation: priceRecommendation
    };
  });
  
  // Store seasonal analysis
  await c.env.PRICING_KV.put(`seasonal:${productId}`, JSON.stringify(seasonalFactors));
  
  return c.json({
    productId,
    seasonalAnalysis: seasonalFactors,
    peakSeason: seasonalFactors.reduce((max, curr) => curr.seasonalIndex > max.seasonalIndex ? curr : max).month,
    lowSeason: seasonalFactors.reduce((min, curr) => curr.seasonalIndex < min.seasonalIndex ? curr : min).month,
    annualPricingCalendar: generatePricingCalendar(seasonalFactors)
  });
});

// ==================== HELPER FUNCTIONS ====================

async function calculateSeasonalFactors(data: any[]): Promise<Map<string, number>> {
  const factors = new Map<string, number>();
  const seasons = ['winter', 'spring', 'summer', 'fall'];
  
  for (const season of seasons) {
    // Calculate average demand in each season
    const seasonData = data.filter(d => getSeason(d.date) === season);
    const avgDemand = seasonData.length > 0 
      ? seasonData.reduce((sum, d) => sum + d.demand, 0) / seasonData.length 
      : 1;
    const overallAvg = data.reduce((sum, d) => sum + d.demand, 0) / data.length;
    factors.set(season, avgDemand / overallAvg);
  }
  
  return factors;
}

function getSeason(date: Date): string {
  const month = date.getMonth();
  if (month >= 2 && month <= 4) return 'spring';
  if (month >= 5 && month <= 7) return 'summer';
  if (month >= 8 && month <= 10) return 'fall';
  return 'winter';
}

function calculateR2(data: any[], elasticity: number): number {
  if (data.length < 2) return 0;
  
  // Simplified R² calculation
  const avgDemand = data.reduce((sum, d) => sum + d.demand, 0) / data.length;
  const totalSS = data.reduce((sum, d) => sum + Math.pow(d.demand - avgDemand, 2), 0);
  
  if (totalSS === 0) return 1;
  
  // Predicted demand based on elasticity
  const avgPrice = data.reduce((sum, d) => sum + d.price, 0) / data.length;
  const residualSS = data.reduce((sum, d) => {
    const predicted = avgDemand * (1 + elasticity * (d.price - avgPrice) / avgPrice);
    return sum + Math.pow(d.demand - predicted, 2);
  }, 0);
  
  return Math.max(0, Math.min(1, 1 - residualSS / totalSS));
}

function interpretElasticity(e: number): { category: string; description: string; implications: string[] } {
  if (Math.abs(e) < 0.5) {
    return {
      category: 'Highly Inelastic',
      description: 'Demand barely responds to price changes',
      implications: [
        'Strong pricing power',
        'Can increase prices without significant demand loss',
        'Focus on premium positioning',
        'Limited need for discounting'
      ]
    };
  } else if (Math.abs(e) < 1) {
    return {
      category: 'Inelastic',
      description: 'Demand responds less than proportionally to price changes',
      implications: [
        'Moderate pricing power',
        'Price increases generate net revenue gains',
        'Consider value-based pricing',
        'Discounts may not significantly boost volume'
      ]
    };
  } else if (Math.abs(e) === 1) {
    return {
      category: 'Unit Elastic',
      description: 'Demand responds proportionally to price changes',
      implications: [
        'Revenue neutral to price changes',
        'Focus on cost optimization',
        'Maintain competitive pricing',
        'Consider bundle strategies'
      ]
    };
  } else if (Math.abs(e) < 2) {
    return {
      category: 'Elastic',
      description: 'Demand responds more than proportionally to price changes',
      implications: [
        'Limited pricing power',
        'Price reductions can increase revenue',
        'Consider promotional pricing',
        'Monitor competitor prices closely'
      ]
    };
  } else {
    return {
      category: 'Highly Elastic',
      description: 'Demand is very sensitive to price changes',
      implications: [
        'Very limited pricing power',
        'Must compete on price',
        'Small discounts can drive large volume',
        'Focus on cost leadership'
      ]
    };
  }
}

function generateElasticityRecommendations(elasticity: number): string[] {
  const recommendations = [];
  
  if (Math.abs(elasticity) < 1) {
    recommendations.push('Consider a 5-10% price increase to test market response');
    recommendations.push('Focus on value communication rather than discounts');
    recommendations.push('Bundle with complementary products for additional margin');
  } else {
    recommendations.push('Implement competitive price monitoring');
    recommendations.push('Consider targeted promotions to drive volume');
    recommendations.push('A/B test price points to find optimal balance');
  }
  
  return recommendations;
}

function fitLinearCurve(pricePoints: { price: number; demand: number }[]): DemandCurve {
  // Linear regression: Q = a - bP
  const n = pricePoints.length;
  const sumP = pricePoints.reduce((sum, p) => sum + p.price, 0);
  const sumQ = pricePoints.reduce((sum, p) => sum + p.demand, 0);
  const sumPQ = pricePoints.reduce((sum, p) => sum + p.price * p.demand, 0);
  const sumP2 = pricePoints.reduce((sum, p) => sum + p.price * p.price, 0);
  
  const b = (n * sumPQ - sumP * sumQ) / (n * sumP2 - sumP * sumP) || 0;
  const a = (sumQ - b * sumP) / n;
  
  return {
    productId: '',
    curveType: 'linear',
    parameters: { a, b: -b },  // Negative b for downward slope
    priceRange: {
      min: Math.min(...pricePoints.map(p => p.price)),
      max: Math.max(...pricePoints.map(p => p.price))
    },
    optimalPrice: 0,
    maxRevenue: 0
  };
}

function fitLogLinearCurve(pricePoints: { price: number; demand: number }[]): DemandCurve {
  // Log-linear: ln(Q) = a - b*ln(P), so Q = e^a * P^(-b)
  const logPoints = pricePoints
    .filter(p => p.price > 0 && p.demand > 0)
    .map(p => ({ price: Math.log(p.price), demand: Math.log(p.demand) }));
  
  if (logPoints.length < 2) {
    return fitLinearCurve(pricePoints);
  }
  
  const n = logPoints.length;
  const sumP = logPoints.reduce((sum, p) => sum + p.price, 0);
  const sumQ = logPoints.reduce((sum, p) => sum + p.demand, 0);
  const sumPQ = logPoints.reduce((sum, p) => sum + p.price * p.demand, 0);
  const sumP2 = logPoints.reduce((sum, p) => sum + p.price * p.price, 0);
  
  const b = -(n * sumPQ - sumP * sumQ) / (n * sumP2 - sumP * sumP) || 1;
  const a = Math.exp((sumQ + b * sumP) / n);
  
  return {
    productId: '',
    curveType: 'log-linear',
    parameters: { a, b },
    priceRange: {
      min: Math.min(...pricePoints.map(p => p.price)),
      max: Math.max(...pricePoints.map(p => p.price))
    },
    optimalPrice: 0,
    maxRevenue: 0
  };
}

function fitExponentialCurve(pricePoints: { price: number; demand: number }[]): DemandCurve {
  // Exponential: Q = a * e^(-bP)
  const validPoints = pricePoints.filter(p => p.demand > 0);
  
  if (validPoints.length < 2) {
    return fitLinearCurve(pricePoints);
  }
  
  // Use linearized form: ln(Q) = ln(a) - bP
  const logQ = validPoints.map(p => ({ price: p.price, demand: Math.log(p.demand) }));
  
  const n = logQ.length;
  const sumP = logQ.reduce((sum, p) => sum + p.price, 0);
  const sumQ = logQ.reduce((sum, p) => sum + p.demand, 0);
  const sumPQ = logQ.reduce((sum, p) => sum + p.price * p.demand, 0);
  const sumP2 = logQ.reduce((sum, p) => sum + p.price * p.price, 0);
  
  const b = -(n * sumPQ - sumP * sumQ) / (n * sumP2 - sumP * sumP) || 0.01;
  const a = Math.exp((sumQ + b * sumP) / n);
  
  return {
    productId: '',
    curveType: 'exponential',
    parameters: { a, b },
    priceRange: {
      min: Math.min(...pricePoints.map(p => p.price)),
      max: Math.max(...pricePoints.map(p => p.price))
    },
    optimalPrice: 0,
    maxRevenue: 0
  };
}

function calculateCurveFit(curve: DemandCurve, pricePoints: { price: number; demand: number }[]): number {
  const predictions = pricePoints.map(p => predictDemand(curve, p.price));
  const avgDemand = pricePoints.reduce((sum, p) => sum + p.demand, 0) / pricePoints.length;
  
  const totalSS = pricePoints.reduce((sum, p) => sum + Math.pow(p.demand - avgDemand, 2), 0);
  const residualSS = pricePoints.reduce((sum, p, i) => sum + Math.pow(p.demand - predictions[i], 2), 0);
  
  if (totalSS === 0) return 1;
  return Math.max(0, 1 - residualSS / totalSS);
}

function predictDemand(curve: DemandCurve, price: number): number {
  const { a, b } = curve.parameters;
  
  switch (curve.curveType) {
    case 'linear':
      return Math.max(0, a - b * price);
    case 'log-linear':
      return a * Math.pow(price, -b);
    case 'exponential':
      return a * Math.exp(-b * price);
    default:
      return a - b * price;
  }
}

function calculateRevenue(curve: DemandCurve, price: number): number {
  return price * predictDemand(curve, price);
}

function findOptimalPrice(curve: DemandCurve): number {
  const { a, b } = curve.parameters;
  
  switch (curve.curveType) {
    case 'linear':
      // Revenue = P * (a - bP) = aP - bP²
      // dR/dP = a - 2bP = 0 => P* = a/(2b)
      return b > 0 ? a / (2 * b) : curve.priceRange.max;
    
    case 'log-linear':
      // Revenue = P * a * P^(-b) = a * P^(1-b)
      // For b > 1, no maximum; for b < 1, increases with price
      // Use numerical optimization
      return findOptimalNumerically(curve);
    
    case 'exponential':
      // Revenue = P * a * e^(-bP)
      // dR/dP = a * e^(-bP) * (1 - bP) = 0 => P* = 1/b
      return 1 / b;
    
    default:
      return findOptimalNumerically(curve);
  }
}

function findOptimalNumerically(curve: DemandCurve): number {
  const step = (curve.priceRange.max - curve.priceRange.min) / 100;
  let maxRevenue = 0;
  let optimalPrice = curve.priceRange.min;
  
  for (let price = curve.priceRange.min; price <= curve.priceRange.max; price += step) {
    const revenue = calculateRevenue(curve, price);
    if (revenue > maxRevenue) {
      maxRevenue = revenue;
      optimalPrice = price;
    }
  }
  
  return optimalPrice;
}

async function getCompetitorPrices(env: Env, productId: string): Promise<number[]> {
  const result = await env.DB.prepare(`
    SELECT DISTINCT price
    FROM competitor_prices
    WHERE product_id = ?
    AND checked_at > datetime('now', '-7 days')
  `).bind(productId).all();
  
  return (result.results || []).map(r => r.price as number);
}

function analyzeExperimentResults(experiment: PricingExperiment): ExperimentResults | null {
  if (experiment.variants.some(v => v.impressions < 100)) {
    return null; // Insufficient data
  }
  
  // Calculate conversion rates
  const rates = experiment.variants.map(v => ({
    id: v.id,
    rate: v.conversions / v.impressions,
    revenue: v.revenue / v.impressions
  }));
  
  // Find best performer
  const best = rates.reduce((max, curr) => curr.revenue > max.revenue ? curr : max);
  const control = rates[0];
  
  // Calculate statistical significance (simplified)
  const liftPercent = ((best.revenue - control.revenue) / control.revenue) * 100;
  const totalImpressions = experiment.variants.reduce((sum, v) => sum + v.impressions, 0);
  const significance = totalImpressions > 1000 && Math.abs(liftPercent) > 5;
  
  return {
    winner: best.id,
    confidence: significance ? 0.95 : 0.8,
    liftPercent,
    statisticalSignificance: significance,
    revenueImpact: best.revenue - control.revenue,
    recommendation: significance 
      ? `Implement ${best.id} pricing for ${liftPercent.toFixed(1)}% revenue lift`
      : 'Continue experiment to reach statistical significance'
  };
}

function calculateRequiredSampleSize(experiment: PricingExperiment): number {
  // Simplified calculation for 80% power, 5% significance
  const currentTotal = experiment.variants.reduce((sum, v) => sum + v.impressions, 0);
  const avgConversionRate = experiment.variants.reduce((sum, v) => sum + v.conversions, 0) / currentTotal || 0.05;
  
  // n = 16 * p * (1-p) / MDE²
  const mde = 0.1; // Minimum detectable effect
  const required = Math.ceil(16 * avgConversionRate * (1 - avgConversionRate) / (mde * mde));
  
  return Math.max(required * experiment.variants.length, 1000);
}

function analyzePricingStrategy(history: { price: number; date: Date }[]): string {
  if (history.length < 5) return 'unknown';
  
  // Check for patterns
  const prices = history.map(h => h.price);
  const priceChanges = prices.slice(1).map((p, i) => p - prices[i]);
  
  // Check for consistent increases (premium strategy)
  const allIncreases = priceChanges.every(c => c >= 0);
  if (allIncreases && priceChanges.some(c => c > 0)) return 'premium_escalation';
  
  // Check for consistent decreases (penetration strategy)
  const allDecreases = priceChanges.every(c => c <= 0);
  if (allDecreases && priceChanges.some(c => c < 0)) return 'penetration';
  
  // Check for high variance (dynamic pricing)
  const avgPrice = prices.reduce((a, b) => a + b, 0) / prices.length;
  const variance = prices.reduce((sum, p) => sum + Math.pow(p - avgPrice, 2), 0) / prices.length;
  const cv = Math.sqrt(variance) / avgPrice;
  
  if (cv > 0.1) return 'dynamic';
  
  return 'stable';
}

function generateCompetitorRecommendations(competitors: any[], avgPrice: number): string[] {
  const recommendations = [];
  
  if (competitors.length === 0) {
    recommendations.push('No competitor data available - set up competitor tracking');
    return recommendations;
  }
  
  if (competitors.length < 3) {
    recommendations.push('Track more competitors for comprehensive market view');
  }
  
  const priceSpread = Math.max(...competitors.map(c => c.currentPrice)) - Math.min(...competitors.map(c => c.currentPrice));
  if (priceSpread / avgPrice > 0.3) {
    recommendations.push('High price variance in market - opportunity for differentiation');
  }
  
  recommendations.push(`Average competitor price: $${avgPrice.toFixed(2)}`);
  
  return recommendations;
}

function calculateSegmentElasticity(purchaseData: any[]): number {
  if (purchaseData.length < 10) return -1.5; // Default elasticity
  
  // Group by price and calculate average quantity
  const priceGroups = new Map<number, { total: number; count: number }>();
  for (const purchase of purchaseData) {
    const roundedPrice = Math.round(purchase.price);
    const group = priceGroups.get(roundedPrice) || { total: 0, count: 0 };
    group.total += purchase.quantity;
    group.count++;
    priceGroups.set(roundedPrice, group);
  }
  
  // Calculate elasticity from grouped data
  const points = Array.from(priceGroups.entries())
    .map(([price, data]) => ({ price, demand: data.total / data.count }))
    .sort((a, b) => a.price - b.price);
  
  if (points.length < 2) return -1.5;
  
  // Calculate average elasticity
  let elasticities = [];
  for (let i = 1; i < points.length; i++) {
    const priceChange = (points[i].price - points[i-1].price) / ((points[i].price + points[i-1].price) / 2);
    const demandChange = (points[i].demand - points[i-1].demand) / ((points[i].demand + points[i-1].demand) / 2);
    if (priceChange !== 0) {
      elasticities.push(demandChange / priceChange);
    }
  }
  
  return elasticities.length > 0 
    ? elasticities.reduce((a, b) => a + b, 0) / elasticities.length 
    : -1.5;
}

function generatePricingCalendar(seasonalFactors: any[]): any[] {
  return seasonalFactors.map(s => ({
    month: s.month,
    strategy: s.recommendation,
    multiplier: s.pricingMultiplier.toFixed(2),
    expectedDemandIndex: s.seasonalIndex.toFixed(2)
  }));
}

export default app;
