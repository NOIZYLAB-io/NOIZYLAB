/**
 * NoizyLab OS - Supplier Intelligence Worker
 * 
 * AI-Powered Supplier Management System:
 * - Supplier quality scoring and ranking
 * - Price prediction and negotiation support
 * - Lead time forecasting
 * - Risk assessment and monitoring
 * - Alternative supplier discovery
 * - Supply chain disruption detection
 * - Contract optimization recommendations
 * - Market intelligence aggregation
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  CACHE: KVNamespace;
  AI: any;
  ALERTS_QUEUE: Queue;
  SUPPLIER_INDEX: VectorizeIndex;
}

interface SupplierScore {
  supplierId: string;
  overallScore: number;
  dimensions: {
    quality: number;
    reliability: number;
    pricing: number;
    communication: number;
    flexibility: number;
  };
  trend: 'improving' | 'stable' | 'declining';
  riskLevel: 'low' | 'medium' | 'high' | 'critical';
  recommendations: string[];
}

interface PricePrediction {
  partNumber: string;
  currentPrice: number;
  predictedPrice: number;
  confidence: number;
  priceDirection: 'up' | 'stable' | 'down';
  factors: string[];
  bestTimeToOrder: string;
  negotiationLeverage: number;
}

interface SupplierRisk {
  supplierId: string;
  riskScore: number;
  riskFactors: RiskFactor[];
  mitigationStrategies: string[];
  alternativeSuppliers: string[];
}

interface RiskFactor {
  type: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  description: string;
  probability: number;
  impact: number;
}

interface MarketIntelligence {
  partCategory: string;
  marketTrend: string;
  priceIndex: number;
  supplyStatus: 'abundant' | 'normal' | 'tight' | 'shortage';
  keyEvents: string[];
  forecast: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// =============================================================================
// SUPPLIER SCORING ENGINE
// =============================================================================

app.get('/api/supplier/:id/score', async (c) => {
  const supplierId = c.req.param('id');
  
  // Get supplier data
  const supplier = await c.env.DB.prepare(`
    SELECT * FROM suppliers WHERE id = ?
  `).bind(supplierId).first();
  
  if (!supplier) {
    return c.json({ error: 'Supplier not found' }, 404);
  }
  
  // Calculate dimension scores
  const quality = await calculateQualityScore(c.env, supplierId);
  const reliability = await calculateReliabilityScore(c.env, supplierId);
  const pricing = await calculatePricingScore(c.env, supplierId);
  const communication = await calculateCommunicationScore(c.env, supplierId);
  const flexibility = await calculateFlexibilityScore(c.env, supplierId);
  
  // Weighted overall score
  const weights = { quality: 0.3, reliability: 0.25, pricing: 0.2, communication: 0.15, flexibility: 0.1 };
  const overallScore = 
    quality * weights.quality +
    reliability * weights.reliability +
    pricing * weights.pricing +
    communication * weights.communication +
    flexibility * weights.flexibility;
  
  // Calculate trend
  const trend = await calculateScoreTrend(c.env, supplierId);
  
  // Determine risk level
  let riskLevel: 'low' | 'medium' | 'high' | 'critical' = 'low';
  if (overallScore < 50) riskLevel = 'critical';
  else if (overallScore < 65) riskLevel = 'high';
  else if (overallScore < 80) riskLevel = 'medium';
  
  // Generate recommendations
  const recommendations = generateSupplierRecommendations(
    { quality, reliability, pricing, communication, flexibility },
    trend,
    riskLevel
  );
  
  const score: SupplierScore = {
    supplierId,
    overallScore: Math.round(overallScore * 10) / 10,
    dimensions: {
      quality: Math.round(quality * 10) / 10,
      reliability: Math.round(reliability * 10) / 10,
      pricing: Math.round(pricing * 10) / 10,
      communication: Math.round(communication * 10) / 10,
      flexibility: Math.round(flexibility * 10) / 10
    },
    trend,
    riskLevel,
    recommendations
  };
  
  // Store score history
  await storeSupplierScore(c.env, score);
  
  return c.json(score);
});

async function calculateQualityScore(env: Env, supplierId: string): Promise<number> {
  const metrics = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total_orders,
      SUM(CASE WHEN defect_count = 0 THEN 1 ELSE 0 END) as perfect_orders,
      AVG(defect_rate) as avg_defect_rate,
      AVG(quality_rating) as avg_quality_rating,
      SUM(CASE WHEN return_reason = 'quality' THEN 1 ELSE 0 END) as quality_returns
    FROM purchase_orders
    WHERE supplier_id = ? AND status = 'completed'
      AND created_at > datetime('now', '-12 months')
  `).bind(supplierId).first();
  
  if (!metrics || (metrics.total_orders as number) === 0) return 70; // Default score
  
  const perfectOrderRate = (metrics.perfect_orders as number) / (metrics.total_orders as number);
  const defectPenalty = Math.min(30, (metrics.avg_defect_rate as number || 0) * 10);
  const returnPenalty = Math.min(20, (metrics.quality_returns as number) * 5);
  
  let score = 100;
  score *= perfectOrderRate;
  score -= defectPenalty;
  score -= returnPenalty;
  
  // Factor in quality ratings if available
  if (metrics.avg_quality_rating) {
    score = (score + (metrics.avg_quality_rating as number) * 20) / 2;
  }
  
  return Math.max(0, Math.min(100, score));
}

async function calculateReliabilityScore(env: Env, supplierId: string): Promise<number> {
  const metrics = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total_orders,
      SUM(CASE WHEN delivered_on_time = 1 THEN 1 ELSE 0 END) as on_time_orders,
      AVG(julianday(actual_delivery) - julianday(promised_delivery)) as avg_delay_days,
      SUM(CASE WHEN order_cancelled = 1 THEN 1 ELSE 0 END) as cancelled_orders,
      SUM(CASE WHEN quantity_fulfilled < quantity_ordered THEN 1 ELSE 0 END) as short_shipments
    FROM purchase_orders
    WHERE supplier_id = ? AND status IN ('completed', 'cancelled')
      AND created_at > datetime('now', '-12 months')
  `).bind(supplierId).first();
  
  if (!metrics || (metrics.total_orders as number) === 0) return 70;
  
  const totalOrders = metrics.total_orders as number;
  const onTimeRate = (metrics.on_time_orders as number) / totalOrders;
  const cancellationRate = (metrics.cancelled_orders as number) / totalOrders;
  const shortShipmentRate = (metrics.short_shipments as number) / totalOrders;
  const avgDelay = metrics.avg_delay_days as number || 0;
  
  let score = onTimeRate * 100;
  score -= cancellationRate * 30;
  score -= shortShipmentRate * 15;
  score -= Math.min(20, avgDelay * 3);
  
  return Math.max(0, Math.min(100, score));
}

async function calculatePricingScore(env: Env, supplierId: string): Promise<number> {
  // Compare supplier prices to market average
  const priceComparison = await env.DB.prepare(`
    SELECT 
      sp.part_number,
      sp.unit_price as supplier_price,
      mp.market_avg_price,
      mp.market_min_price
    FROM supplier_prices sp
    JOIN market_prices mp ON sp.part_number = mp.part_number
    WHERE sp.supplier_id = ?
      AND sp.updated_at > datetime('now', '-30 days')
  `).bind(supplierId).all();
  
  if (!priceComparison.results || priceComparison.results.length === 0) return 70;
  
  // Calculate price competitiveness
  let totalCompetitiveness = 0;
  
  for (const item of priceComparison.results) {
    const i = item as any;
    const marketAvg = i.market_avg_price;
    const supplierPrice = i.supplier_price;
    
    if (marketAvg > 0) {
      const competitiveness = (marketAvg - supplierPrice) / marketAvg * 100 + 50;
      totalCompetitiveness += Math.max(0, Math.min(100, competitiveness));
    }
  }
  
  const avgCompetitiveness = totalCompetitiveness / priceComparison.results.length;
  
  // Factor in price stability
  const priceStability = await env.DB.prepare(`
    SELECT AVG(ABS(price_change_pct)) as avg_volatility
    FROM supplier_price_history
    WHERE supplier_id = ?
      AND created_at > datetime('now', '-6 months')
  `).bind(supplierId).first();
  
  let score = avgCompetitiveness;
  if (priceStability?.avg_volatility) {
    score -= Math.min(15, (priceStability.avg_volatility as number) * 2);
  }
  
  return Math.max(0, Math.min(100, score));
}

async function calculateCommunicationScore(env: Env, supplierId: string): Promise<number> {
  const metrics = await env.DB.prepare(`
    SELECT 
      AVG(response_time_hours) as avg_response_time,
      AVG(communication_rating) as avg_rating,
      SUM(CASE WHEN issue_resolved = 1 THEN 1 ELSE 0 END) as resolved_issues,
      COUNT(*) as total_issues
    FROM supplier_communications
    WHERE supplier_id = ?
      AND created_at > datetime('now', '-6 months')
  `).bind(supplierId).first();
  
  if (!metrics) return 70;
  
  // Response time scoring (24h = 100, 48h = 70, 72h+ = 40)
  const avgResponseTime = (metrics.avg_response_time as number) || 24;
  let responseScore = Math.max(40, 100 - (avgResponseTime - 24) * 1.25);
  
  // Issue resolution rate
  const totalIssues = (metrics.total_issues as number) || 1;
  const resolutionRate = (metrics.resolved_issues as number || 0) / totalIssues;
  
  // Combine with rating
  const rating = (metrics.avg_rating as number) || 3;
  const ratingScore = rating * 20;
  
  return Math.max(0, Math.min(100, (responseScore + resolutionRate * 100 + ratingScore) / 3));
}

async function calculateFlexibilityScore(env: Env, supplierId: string): Promise<number> {
  const metrics = await env.DB.prepare(`
    SELECT 
      SUM(CASE WHEN rush_order_accepted = 1 THEN 1 ELSE 0 END) as rush_accepted,
      SUM(CASE WHEN rush_order_requested = 1 THEN 1 ELSE 0 END) as rush_requested,
      SUM(CASE WHEN order_modified = 1 AND modification_accepted = 1 THEN 1 ELSE 0 END) as mods_accepted,
      SUM(CASE WHEN order_modified = 1 THEN 1 ELSE 0 END) as mods_requested,
      AVG(min_order_quantity) as avg_moq
    FROM purchase_orders
    WHERE supplier_id = ?
      AND created_at > datetime('now', '-12 months')
  `).bind(supplierId).first();
  
  if (!metrics) return 70;
  
  // Rush order acceptance rate
  const rushRequested = (metrics.rush_requested as number) || 1;
  const rushAcceptanceRate = (metrics.rush_accepted as number || 0) / rushRequested;
  
  // Modification acceptance rate
  const modsRequested = (metrics.mods_requested as number) || 1;
  const modAcceptanceRate = (metrics.mods_accepted as number || 0) / modsRequested;
  
  // MOQ flexibility (lower is better)
  const avgMoq = (metrics.avg_moq as number) || 100;
  const moqScore = Math.max(50, 100 - avgMoq / 10);
  
  return Math.max(0, Math.min(100, (rushAcceptanceRate * 100 + modAcceptanceRate * 100 + moqScore) / 3));
}

async function calculateScoreTrend(env: Env, supplierId: string): Promise<'improving' | 'stable' | 'declining'> {
  const history = await env.DB.prepare(`
    SELECT overall_score, created_at
    FROM supplier_scores
    WHERE supplier_id = ?
    ORDER BY created_at DESC
    LIMIT 6
  `).bind(supplierId).all();
  
  if (!history.results || history.results.length < 3) return 'stable';
  
  const scores = history.results.map((h: any) => h.overall_score as number);
  const recentAvg = (scores[0] + scores[1] + scores[2]) / 3;
  const oldAvg = scores.slice(3).reduce((a, b) => a + b, 0) / Math.max(1, scores.length - 3);
  
  const change = recentAvg - oldAvg;
  
  if (change > 5) return 'improving';
  if (change < -5) return 'declining';
  return 'stable';
}

function generateSupplierRecommendations(
  scores: { quality: number; reliability: number; pricing: number; communication: number; flexibility: number },
  trend: string,
  riskLevel: string
): string[] {
  const recommendations: string[] = [];
  
  // Quality recommendations
  if (scores.quality < 70) {
    recommendations.push('Implement incoming quality inspection for this supplier');
    recommendations.push('Request quality improvement plan with milestones');
  }
  
  // Reliability recommendations
  if (scores.reliability < 70) {
    recommendations.push('Consider safety stock increase to buffer against delays');
    recommendations.push('Request commitment to improved lead times');
  }
  
  // Pricing recommendations
  if (scores.pricing < 60) {
    recommendations.push('Initiate price renegotiation or seek alternative quotes');
    recommendations.push('Consider volume consolidation for better pricing');
  }
  
  // Communication recommendations
  if (scores.communication < 70) {
    recommendations.push('Establish regular check-in cadence with supplier');
    recommendations.push('Request dedicated account manager');
  }
  
  // Risk-based recommendations
  if (riskLevel === 'high' || riskLevel === 'critical') {
    recommendations.push('Identify and qualify backup suppliers immediately');
    recommendations.push('Reduce order concentration with this supplier');
  }
  
  // Trend-based recommendations
  if (trend === 'declining') {
    recommendations.push('Schedule quarterly business review to address declining performance');
  } else if (trend === 'improving') {
    recommendations.push('Consider increased order allocation as reward for improvement');
  }
  
  return recommendations.slice(0, 5); // Top 5 recommendations
}

async function storeSupplierScore(env: Env, score: SupplierScore): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO supplier_scores (
      supplier_id, overall_score, quality_score, reliability_score,
      pricing_score, communication_score, flexibility_score,
      trend, risk_level, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    score.supplierId,
    score.overallScore,
    score.dimensions.quality,
    score.dimensions.reliability,
    score.dimensions.pricing,
    score.dimensions.communication,
    score.dimensions.flexibility,
    score.trend,
    score.riskLevel
  ).run();
}

// =============================================================================
// PRICE PREDICTION ENGINE
// =============================================================================

app.post('/api/price/predict', async (c) => {
  const { partNumber, supplierId } = await c.req.json();
  
  // Get price history
  const priceHistory = await c.env.DB.prepare(`
    SELECT unit_price, created_at
    FROM supplier_price_history
    WHERE part_number = ? AND supplier_id = ?
    ORDER BY created_at DESC
    LIMIT 24
  `).bind(partNumber, supplierId).all();
  
  // Get current price
  const currentPrice = await c.env.DB.prepare(`
    SELECT unit_price FROM supplier_prices
    WHERE part_number = ? AND supplier_id = ?
  `).bind(partNumber, supplierId).first();
  
  if (!currentPrice) {
    return c.json({ error: 'Price not found' }, 404);
  }
  
  // Get market factors
  const marketFactors = await getMarketFactors(c.env, partNumber);
  
  // Use AI for prediction
  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: `You are a supply chain pricing analyst. Predict future price based on historical data and market factors.
        
        Respond with JSON:
        {
          "predictedPrice": XX.XX,
          "confidence": 0.XX,
          "direction": "up|stable|down",
          "factors": ["factor1", "factor2"],
          "bestOrderTiming": "description",
          "negotiationLeverage": 0.XX
        }`
      },
      {
        role: 'user',
        content: `Part: ${partNumber}
        Current Price: $${currentPrice.unit_price}
        Price History (newest first): ${JSON.stringify(priceHistory.results?.slice(0, 12))}
        Market Factors: ${JSON.stringify(marketFactors)}`
      }
    ]
  });
  
  try {
    const prediction = JSON.parse(response.response);
    
    const result: PricePrediction = {
      partNumber,
      currentPrice: currentPrice.unit_price as number,
      predictedPrice: prediction.predictedPrice,
      confidence: prediction.confidence,
      priceDirection: prediction.direction,
      factors: prediction.factors,
      bestTimeToOrder: prediction.bestOrderTiming,
      negotiationLeverage: prediction.negotiationLeverage
    };
    
    return c.json(result);
  } catch (e) {
    // Fallback to simple trend analysis
    const prices = priceHistory.results?.map((p: any) => p.unit_price as number) || [];
    const avgRecent = prices.slice(0, 6).reduce((a, b) => a + b, 0) / Math.max(1, Math.min(6, prices.length));
    const avgOlder = prices.slice(6, 12).reduce((a, b) => a + b, 0) / Math.max(1, Math.min(6, prices.length - 6));
    
    const trendPct = avgOlder > 0 ? (avgRecent - avgOlder) / avgOlder : 0;
    
    return c.json({
      partNumber,
      currentPrice: currentPrice.unit_price as number,
      predictedPrice: (currentPrice.unit_price as number) * (1 + trendPct),
      confidence: 0.6,
      priceDirection: trendPct > 0.02 ? 'up' : trendPct < -0.02 ? 'down' : 'stable',
      factors: ['Historical trend analysis'],
      bestTimeToOrder: 'Based on current data',
      negotiationLeverage: 0.5
    });
  }
});

async function getMarketFactors(env: Env, partNumber: string): Promise<any> {
  // Get part category
  const part = await env.DB.prepare(`
    SELECT category, subcategory FROM parts WHERE part_number = ?
  `).bind(partNumber).first();
  
  if (!part) return {};
  
  // Get category market data
  const marketData = await env.DB.prepare(`
    SELECT * FROM market_intelligence
    WHERE category = ?
    ORDER BY created_at DESC LIMIT 1
  `).bind(part.category).first();
  
  // Get commodity indices if applicable
  const commodities = await env.DB.prepare(`
    SELECT commodity, price_index, trend
    FROM commodity_prices
    WHERE commodity IN (SELECT commodity FROM part_commodities WHERE part_number = ?)
  `).bind(partNumber).all();
  
  return {
    category: part.category,
    marketData,
    commodityPrices: commodities.results
  };
}

// =============================================================================
// SUPPLIER RISK ASSESSMENT
// =============================================================================

app.get('/api/supplier/:id/risk', async (c) => {
  const supplierId = c.req.param('id');
  
  const riskFactors: RiskFactor[] = [];
  
  // Financial risk
  const financialRisk = await assessFinancialRisk(c.env, supplierId);
  if (financialRisk) riskFactors.push(financialRisk);
  
  // Concentration risk
  const concentrationRisk = await assessConcentrationRisk(c.env, supplierId);
  if (concentrationRisk) riskFactors.push(concentrationRisk);
  
  // Geographic risk
  const geoRisk = await assessGeographicRisk(c.env, supplierId);
  if (geoRisk) riskFactors.push(geoRisk);
  
  // Quality trend risk
  const qualityRisk = await assessQualityTrendRisk(c.env, supplierId);
  if (qualityRisk) riskFactors.push(qualityRisk);
  
  // Capacity risk
  const capacityRisk = await assessCapacityRisk(c.env, supplierId);
  if (capacityRisk) riskFactors.push(capacityRisk);
  
  // Single source risk
  const singleSourceRisk = await assessSingleSourceRisk(c.env, supplierId);
  if (singleSourceRisk) riskFactors.push(singleSourceRisk);
  
  // Calculate overall risk score
  const riskScore = riskFactors.reduce((sum, f) => sum + f.probability * f.impact, 0) / 
                    Math.max(1, riskFactors.length);
  
  // Generate mitigation strategies
  const mitigationStrategies = generateMitigationStrategies(riskFactors);
  
  // Find alternative suppliers
  const alternatives = await findAlternativeSuppliers(c.env, supplierId);
  
  const risk: SupplierRisk = {
    supplierId,
    riskScore: Math.round(riskScore * 100) / 100,
    riskFactors,
    mitigationStrategies,
    alternativeSuppliers: alternatives
  };
  
  return c.json(risk);
});

async function assessFinancialRisk(env: Env, supplierId: string): Promise<RiskFactor | null> {
  const supplier = await env.DB.prepare(`
    SELECT financial_rating, payment_terms_days, credit_limit
    FROM suppliers WHERE id = ?
  `).bind(supplierId).first();
  
  if (!supplier) return null;
  
  const rating = supplier.financial_rating as string;
  if (rating === 'poor' || rating === 'unknown') {
    return {
      type: 'financial',
      severity: rating === 'poor' ? 'high' : 'medium',
      description: `Supplier has ${rating} financial rating`,
      probability: rating === 'poor' ? 0.4 : 0.2,
      impact: 0.8
    };
  }
  
  return null;
}

async function assessConcentrationRisk(env: Env, supplierId: string): Promise<RiskFactor | null> {
  const concentration = await env.DB.prepare(`
    SELECT 
      SUM(order_value) as supplier_spend,
      (SELECT SUM(order_value) FROM purchase_orders WHERE created_at > datetime('now', '-12 months')) as total_spend
    FROM purchase_orders
    WHERE supplier_id = ? AND created_at > datetime('now', '-12 months')
  `).bind(supplierId).first();
  
  if (!concentration) return null;
  
  const supplierSpend = concentration.supplier_spend as number || 0;
  const totalSpend = concentration.total_spend as number || 1;
  const concentrationPct = supplierSpend / totalSpend;
  
  if (concentrationPct > 0.3) {
    return {
      type: 'concentration',
      severity: concentrationPct > 0.5 ? 'critical' : 'high',
      description: `${(concentrationPct * 100).toFixed(0)}% of spend concentrated with this supplier`,
      probability: 0.3,
      impact: concentrationPct
    };
  }
  
  return null;
}

async function assessGeographicRisk(env: Env, supplierId: string): Promise<RiskFactor | null> {
  const supplier = await env.DB.prepare(`
    SELECT country, region FROM suppliers WHERE id = ?
  `).bind(supplierId).first();
  
  if (!supplier) return null;
  
  // High-risk regions (simplified)
  const highRiskRegions = ['conflict_zone', 'trade_restricted', 'natural_disaster_prone'];
  const country = supplier.country as string;
  const region = supplier.region as string;
  
  // Check for regional risks (in production, this would use external data)
  const regionRisk = await env.DB.prepare(`
    SELECT risk_level, risk_type FROM region_risks
    WHERE country = ? OR region = ?
  `).bind(country, region).first();
  
  if (regionRisk && (regionRisk.risk_level as string) !== 'low') {
    return {
      type: 'geographic',
      severity: regionRisk.risk_level as 'low' | 'medium' | 'high' | 'critical',
      description: `Supplier located in ${regionRisk.risk_type} region (${country})`,
      probability: 0.25,
      impact: 0.7
    };
  }
  
  return null;
}

async function assessQualityTrendRisk(env: Env, supplierId: string): Promise<RiskFactor | null> {
  const qualityTrend = await env.DB.prepare(`
    SELECT 
      AVG(CASE WHEN created_at > datetime('now', '-3 months') THEN defect_rate ELSE NULL END) as recent_defect_rate,
      AVG(CASE WHEN created_at <= datetime('now', '-3 months') THEN defect_rate ELSE NULL END) as older_defect_rate
    FROM purchase_orders
    WHERE supplier_id = ? AND created_at > datetime('now', '-12 months')
  `).bind(supplierId).first();
  
  if (!qualityTrend) return null;
  
  const recentRate = qualityTrend.recent_defect_rate as number || 0;
  const olderRate = qualityTrend.older_defect_rate as number || 0;
  
  if (recentRate > olderRate * 1.5 && recentRate > 0.02) {
    return {
      type: 'quality_trend',
      severity: recentRate > 0.05 ? 'high' : 'medium',
      description: `Quality declining: defect rate increased from ${(olderRate * 100).toFixed(1)}% to ${(recentRate * 100).toFixed(1)}%`,
      probability: 0.6,
      impact: 0.5
    };
  }
  
  return null;
}

async function assessCapacityRisk(env: Env, supplierId: string): Promise<RiskFactor | null> {
  const capacityData = await env.DB.prepare(`
    SELECT 
      estimated_capacity,
      SUM(quantity_ordered) as total_ordered
    FROM suppliers s
    JOIN purchase_orders po ON s.id = po.supplier_id
    WHERE s.id = ? AND po.created_at > datetime('now', '-3 months')
    GROUP BY s.id
  `).bind(supplierId).first();
  
  if (!capacityData || !capacityData.estimated_capacity) return null;
  
  const utilization = (capacityData.total_ordered as number) / (capacityData.estimated_capacity as number);
  
  if (utilization > 0.85) {
    return {
      type: 'capacity',
      severity: utilization > 0.95 ? 'critical' : 'high',
      description: `Supplier at ${(utilization * 100).toFixed(0)}% capacity utilization`,
      probability: 0.4,
      impact: 0.6
    };
  }
  
  return null;
}

async function assessSingleSourceRisk(env: Env, supplierId: string): Promise<RiskFactor | null> {
  const singleSourceParts = await env.DB.prepare(`
    SELECT COUNT(*) as count
    FROM parts p
    WHERE NOT EXISTS (
      SELECT 1 FROM supplier_parts sp2 
      WHERE sp2.part_number = p.part_number AND sp2.supplier_id != ?
    )
    AND EXISTS (
      SELECT 1 FROM supplier_parts sp WHERE sp.part_number = p.part_number AND sp.supplier_id = ?
    )
  `).bind(supplierId, supplierId).first();
  
  const count = singleSourceParts?.count as number || 0;
  
  if (count > 0) {
    return {
      type: 'single_source',
      severity: count > 5 ? 'high' : 'medium',
      description: `${count} parts have this supplier as single source`,
      probability: 0.2,
      impact: 0.9
    };
  }
  
  return null;
}

function generateMitigationStrategies(riskFactors: RiskFactor[]): string[] {
  const strategies: string[] = [];
  
  for (const risk of riskFactors) {
    switch (risk.type) {
      case 'financial':
        strategies.push('Implement credit monitoring for supplier');
        strategies.push('Consider requiring performance bond');
        break;
      case 'concentration':
        strategies.push('Develop secondary supplier qualification plan');
        strategies.push('Set maximum order allocation cap');
        break;
      case 'geographic':
        strategies.push('Maintain safety stock for affected parts');
        strategies.push('Identify local alternative suppliers');
        break;
      case 'quality_trend':
        strategies.push('Increase incoming inspection frequency');
        strategies.push('Conduct supplier quality audit');
        break;
      case 'capacity':
        strategies.push('Negotiate capacity reservation agreement');
        strategies.push('Provide rolling forecasts to supplier');
        break;
      case 'single_source':
        strategies.push('Qualify additional suppliers for critical parts');
        strategies.push('Reverse engineer critical components');
        break;
    }
  }
  
  return [...new Set(strategies)].slice(0, 6);
}

async function findAlternativeSuppliers(env: Env, supplierId: string): Promise<string[]> {
  // Get parts supplied by this supplier
  const parts = await env.DB.prepare(`
    SELECT part_number FROM supplier_parts WHERE supplier_id = ?
  `).bind(supplierId).all();
  
  if (!parts.results) return [];
  
  // Find other suppliers for these parts
  const alternatives = await env.DB.prepare(`
    SELECT DISTINCT s.id, s.name, COUNT(*) as overlap_count
    FROM suppliers s
    JOIN supplier_parts sp ON s.id = sp.supplier_id
    WHERE sp.part_number IN (${parts.results.map(() => '?').join(',')})
      AND s.id != ?
    GROUP BY s.id
    ORDER BY overlap_count DESC
    LIMIT 5
  `).bind(...parts.results.map((p: any) => p.part_number), supplierId).all();
  
  return alternatives.results?.map((a: any) => a.id) || [];
}

// =============================================================================
// MARKET INTELLIGENCE
// =============================================================================

app.get('/api/market/:category', async (c) => {
  const category = c.req.param('category');
  
  // Get cached market data
  const cached = await c.env.CACHE.get(`market:${category}`, 'json');
  if (cached) {
    return c.json(cached);
  }
  
  // Get price index trend
  const priceIndex = await c.env.DB.prepare(`
    SELECT 
      AVG(unit_price) as avg_price,
      strftime('%Y-%m', created_at) as month
    FROM supplier_prices sp
    JOIN parts p ON sp.part_number = p.part_number
    WHERE p.category = ?
    GROUP BY month
    ORDER BY month DESC
    LIMIT 12
  `).bind(category).all();
  
  // Get supply/demand signals
  const supplySignals = await c.env.DB.prepare(`
    SELECT 
      AVG(lead_time_days) as avg_lead_time,
      AVG(availability_score) as avg_availability
    FROM supplier_parts sp
    JOIN parts p ON sp.part_number = p.part_number
    WHERE p.category = ?
      AND sp.updated_at > datetime('now', '-30 days')
  `).bind(category).first();
  
  // Determine supply status
  const avgLeadTime = (supplySignals?.avg_lead_time as number) || 7;
  const avgAvailability = (supplySignals?.avg_availability as number) || 0.8;
  
  let supplyStatus: 'abundant' | 'normal' | 'tight' | 'shortage' = 'normal';
  if (avgLeadTime > 21 || avgAvailability < 0.5) supplyStatus = 'shortage';
  else if (avgLeadTime > 14 || avgAvailability < 0.7) supplyStatus = 'tight';
  else if (avgLeadTime < 5 && avgAvailability > 0.9) supplyStatus = 'abundant';
  
  // Use AI for market analysis
  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: `You are a supply chain market analyst. Provide brief market intelligence for electronics repair parts.
        
        Respond with JSON:
        {
          "marketTrend": "brief trend description",
          "keyEvents": ["event1", "event2"],
          "forecast": "brief 3-month forecast"
        }`
      },
      {
        role: 'user',
        content: `Category: ${category}
        Supply Status: ${supplyStatus}
        Avg Lead Time: ${avgLeadTime} days
        Price Trend: ${JSON.stringify(priceIndex.results?.slice(0, 3))}`
      }
    ]
  });
  
  let aiInsights = { marketTrend: '', keyEvents: [], forecast: '' };
  try {
    aiInsights = JSON.parse(response.response);
  } catch (e) {
    // Use defaults
  }
  
  const intelligence: MarketIntelligence = {
    partCategory: category,
    marketTrend: aiInsights.marketTrend || 'Stable market conditions',
    priceIndex: priceIndex.results?.[0]?.avg_price as number || 0,
    supplyStatus,
    keyEvents: aiInsights.keyEvents || [],
    forecast: aiInsights.forecast || 'No significant changes expected'
  };
  
  // Cache for 1 hour
  await c.env.CACHE.put(`market:${category}`, JSON.stringify(intelligence), { expirationTtl: 3600 });
  
  return c.json(intelligence);
});

// =============================================================================
// SUPPLIER DISCOVERY
// =============================================================================

app.post('/api/discover', async (c) => {
  const { partNumber, requirements } = await c.req.json();
  
  // Get part details
  const part = await c.env.DB.prepare(`
    SELECT * FROM parts WHERE part_number = ?
  `).bind(partNumber).first();
  
  if (!part) {
    return c.json({ error: 'Part not found' }, 404);
  }
  
  // Create search embedding
  const searchText = `${part.category} ${part.description} ${requirements?.join(' ') || ''}`;
  const embedding = await c.env.AI.run('@cf/baai/bge-base-en-v1.5', {
    text: searchText
  });
  
  // Search supplier index
  const similar = await c.env.SUPPLIER_INDEX.query(embedding.data[0], {
    topK: 10,
    filter: { active: true }
  });
  
  // Get supplier details
  const supplierIds = similar.matches?.map(m => m.id) || [];
  
  if (supplierIds.length === 0) {
    return c.json({ suppliers: [], message: 'No matching suppliers found' });
  }
  
  const suppliers = await c.env.DB.prepare(`
    SELECT s.*, ss.overall_score, ss.risk_level
    FROM suppliers s
    LEFT JOIN (
      SELECT supplier_id, overall_score, risk_level
      FROM supplier_scores
      WHERE (supplier_id, created_at) IN (
        SELECT supplier_id, MAX(created_at)
        FROM supplier_scores
        GROUP BY supplier_id
      )
    ) ss ON s.id = ss.supplier_id
    WHERE s.id IN (${supplierIds.map(() => '?').join(',')})
    ORDER BY ss.overall_score DESC
  `).bind(...supplierIds).all();
  
  return c.json({
    partNumber,
    suppliers: suppliers.results?.map((s: any, i: number) => ({
      ...s,
      matchScore: similar.matches?.[i]?.score || 0
    }))
  });
});

// =============================================================================
// NEGOTIATION SUPPORT
// =============================================================================

app.post('/api/negotiate/analyze', async (c) => {
  const { supplierId, partNumbers, targetPriceReduction } = await c.req.json();
  
  // Get current pricing and volumes
  const currentPricing = await c.env.DB.prepare(`
    SELECT 
      sp.part_number,
      sp.unit_price,
      SUM(po.quantity_ordered) as annual_volume,
      SUM(po.order_value) as annual_spend
    FROM supplier_prices sp
    LEFT JOIN purchase_orders po ON sp.supplier_id = po.supplier_id 
      AND sp.part_number = po.part_number
      AND po.created_at > datetime('now', '-12 months')
    WHERE sp.supplier_id = ? AND sp.part_number IN (${partNumbers.map(() => '?').join(',')})
    GROUP BY sp.part_number
  `).bind(supplierId, ...partNumbers).all();
  
  // Get supplier score
  const score = await c.env.DB.prepare(`
    SELECT * FROM supplier_scores
    WHERE supplier_id = ?
    ORDER BY created_at DESC LIMIT 1
  `).bind(supplierId).first();
  
  // Get competitive pricing
  const competitivePricing = await c.env.DB.prepare(`
    SELECT 
      sp.part_number,
      MIN(sp.unit_price) as min_price,
      AVG(sp.unit_price) as avg_price,
      COUNT(DISTINCT sp.supplier_id) as supplier_count
    FROM supplier_prices sp
    WHERE sp.part_number IN (${partNumbers.map(() => '?').join(',')})
      AND sp.supplier_id != ?
    GROUP BY sp.part_number
  `).bind(...partNumbers, supplierId).all();
  
  // Calculate negotiation leverage
  const totalSpend = currentPricing.results?.reduce((sum: number, p: any) => sum + (p.annual_spend || 0), 0) || 0;
  const supplierScore = score?.overall_score as number || 70;
  
  // Generate negotiation strategy using AI
  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: `You are a procurement negotiation expert. Analyze the situation and provide negotiation strategy.
        
        Respond with JSON:
        {
          "leverage_score": 0.XX,
          "recommended_approach": "description",
          "talking_points": ["point1", "point2"],
          "risks": ["risk1"],
          "alternative_value_adds": ["alternative1"],
          "target_achievability": 0.XX
        }`
      },
      {
        role: 'user',
        content: `Supplier Score: ${supplierScore}
        Annual Spend: $${totalSpend}
        Target Price Reduction: ${targetPriceReduction}%
        Current Pricing: ${JSON.stringify(currentPricing.results)}
        Competitive Pricing: ${JSON.stringify(competitivePricing.results)}`
      }
    ]
  });
  
  try {
    const strategy = JSON.parse(response.response);
    return c.json({
      supplierId,
      currentSpend: totalSpend,
      potentialSavings: totalSpend * (targetPriceReduction / 100),
      negotiationStrategy: strategy,
      competitiveAnalysis: competitivePricing.results
    });
  } catch (e) {
    return c.json({
      supplierId,
      currentSpend: totalSpend,
      potentialSavings: totalSpend * (targetPriceReduction / 100),
      negotiationStrategy: {
        leverage_score: totalSpend > 50000 ? 0.7 : 0.5,
        recommended_approach: 'Volume commitment in exchange for price reduction',
        talking_points: ['Competitive alternatives available', 'Long-term partnership value'],
        target_achievability: 0.6
      },
      competitiveAnalysis: competitivePricing.results
    });
  }
});

// =============================================================================
// SUPPLIER RANKINGS
// =============================================================================

app.get('/api/rankings', async (c) => {
  const category = c.req.query('category');
  const limit = parseInt(c.req.query('limit') || '20');
  
  let query = `
    SELECT 
      s.id, s.name, s.country,
      ss.overall_score, ss.quality_score, ss.reliability_score,
      ss.pricing_score, ss.risk_level, ss.trend
    FROM suppliers s
    JOIN (
      SELECT supplier_id, overall_score, quality_score, reliability_score,
             pricing_score, risk_level, trend
      FROM supplier_scores
      WHERE (supplier_id, created_at) IN (
        SELECT supplier_id, MAX(created_at)
        FROM supplier_scores
        GROUP BY supplier_id
      )
    ) ss ON s.id = ss.supplier_id
    WHERE s.active = 1
  `;
  
  if (category) {
    query += ` AND s.id IN (
      SELECT DISTINCT supplier_id FROM supplier_parts sp
      JOIN parts p ON sp.part_number = p.part_number
      WHERE p.category = '${category}'
    )`;
  }
  
  query += ` ORDER BY ss.overall_score DESC LIMIT ${limit}`;
  
  const rankings = await c.env.DB.prepare(query).all();
  
  return c.json({
    rankings: rankings.results?.map((r: any, i: number) => ({
      rank: i + 1,
      ...r
    })),
    category: category || 'all',
    generatedAt: new Date().toISOString()
  });
});

export default app;
