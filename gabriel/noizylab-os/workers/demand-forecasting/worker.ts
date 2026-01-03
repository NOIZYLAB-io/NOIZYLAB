/**
 * NoizyLab OS - Demand Forecasting Worker
 * Predictive Inventory & Parts Ordering Engine
 * 
 * Features:
 * - Time series forecasting (ARIMA, ETS, Prophet-style)
 * - Seasonal decomposition
 * - Multi-variate demand prediction
 * - Automatic reorder point calculation
 * - Safety stock optimization
 * - Lead time analysis
 * - Demand sensing (real-time adjustments)
 * - Promotional impact modeling
 */

import { Hono } from 'hono';

interface Env {
  FORECAST_KV: KVNamespace;
  DB: D1Database;
  AI: Ai;
}

interface TimeSeriesPoint {
  date: Date;
  value: number;
  metadata?: Record<string, any>;
}

interface ForecastResult {
  productId: string;
  forecastPeriod: { start: Date; end: Date };
  predictions: ForecastPoint[];
  accuracy: ForecastAccuracy;
  seasonalPattern: SeasonalPattern;
  trendAnalysis: TrendAnalysis;
  recommendations: InventoryRecommendation[];
}

interface ForecastPoint {
  date: Date;
  predicted: number;
  lowerBound: number;
  upperBound: number;
  confidence: number;
}

interface ForecastAccuracy {
  mape: number;  // Mean Absolute Percentage Error
  rmse: number;  // Root Mean Square Error
  mae: number;   // Mean Absolute Error
  r2: number;    // R-squared
  backtestResults: BacktestResult[];
}

interface BacktestResult {
  period: string;
  actual: number;
  predicted: number;
  error: number;
  percentError: number;
}

interface SeasonalPattern {
  detected: boolean;
  period: number;  // Days
  peakMonths: number[];
  troughMonths: number[];
  seasonalIndices: number[];
  strength: number;  // 0-1
}

interface TrendAnalysis {
  direction: 'increasing' | 'decreasing' | 'stable';
  slope: number;
  changePoints: ChangePoint[];
  growthRate: number;
  volatility: number;
}

interface ChangePoint {
  date: Date;
  type: 'increase' | 'decrease' | 'level_shift';
  magnitude: number;
  significance: number;
}

interface InventoryRecommendation {
  type: string;
  priority: 'low' | 'medium' | 'high' | 'critical';
  description: string;
  quantityRecommended: number;
  timing: string;
  expectedImpact: string;
}

interface ReorderAnalysis {
  productId: string;
  currentStock: number;
  reorderPoint: number;
  safetyStock: number;
  economicOrderQuantity: number;
  daysUntilReorder: number;
  recommendedOrderDate: Date;
  recommendedQuantity: number;
  stockoutRisk: number;
}

interface DemandDriver {
  factor: string;
  correlation: number;
  lag: number;  // Days
  importance: number;
  predictedImpact: number;
}

interface PromotionalImpact {
  promotionId: string;
  promotionType: string;
  expectedLift: number;
  historicalLift: number;
  confidenceInterval: { lower: number; upper: number };
  cannibalizations: { productId: string; impact: number }[];
}

const app = new Hono<{ Bindings: Env }>();

// ==================== FORECASTING ====================

app.post('/forecast', async (c) => {
  const { productId, historicalData, horizon = 30, method = 'auto' } = await c.req.json();
  
  // Parse historical data
  const timeSeries: TimeSeriesPoint[] = historicalData.map((d: any) => ({
    date: new Date(d.date),
    value: d.quantity || d.value,
    metadata: d.metadata
  }));
  
  if (timeSeries.length < 30) {
    return c.json({ error: 'Insufficient historical data. Need at least 30 data points.' }, 400);
  }
  
  // Detect seasonality
  const seasonalPattern = detectSeasonality(timeSeries);
  
  // Analyze trend
  const trendAnalysis = analyzeTrend(timeSeries);
  
  // Select best forecasting method
  const selectedMethod = method === 'auto' 
    ? selectBestMethod(timeSeries, seasonalPattern)
    : method;
  
  // Generate forecast
  let predictions: ForecastPoint[];
  
  switch (selectedMethod) {
    case 'exponential_smoothing':
      predictions = exponentialSmoothing(timeSeries, horizon, seasonalPattern);
      break;
    case 'arima':
      predictions = arimaForecast(timeSeries, horizon, seasonalPattern);
      break;
    case 'prophet':
      predictions = prophetStyleForecast(timeSeries, horizon, seasonalPattern);
      break;
    default:
      predictions = exponentialSmoothing(timeSeries, horizon, seasonalPattern);
  }
  
  // Calculate accuracy metrics
  const accuracy = calculateAccuracy(timeSeries, selectedMethod);
  
  // Generate recommendations
  const recommendations = generateForecastRecommendations(predictions, seasonalPattern, trendAnalysis);
  
  const result: ForecastResult = {
    productId,
    forecastPeriod: {
      start: predictions[0]?.date || new Date(),
      end: predictions[predictions.length - 1]?.date || new Date()
    },
    predictions,
    accuracy,
    seasonalPattern,
    trendAnalysis,
    recommendations
  };
  
  // Store forecast
  await c.env.FORECAST_KV.put(`forecast:${productId}`, JSON.stringify(result));
  
  // Store in D1
  await c.env.DB.prepare(`
    INSERT INTO demand_forecasts (product_id, horizon, method, mape, predictions, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    productId,
    horizon,
    selectedMethod,
    accuracy.mape,
    JSON.stringify(predictions)
  ).run();
  
  return c.json(result);
});

app.post('/forecast/batch', async (c) => {
  const { productIds, horizon = 30 } = await c.req.json();
  
  const forecasts: ForecastResult[] = [];
  const errors: { productId: string; error: string }[] = [];
  
  for (const productId of productIds) {
    try {
      // Get historical data from DB
      const history = await c.env.DB.prepare(`
        SELECT date, quantity FROM sales_history
        WHERE product_id = ?
        ORDER BY date DESC
        LIMIT 365
      `).bind(productId).all();
      
      if ((history.results?.length || 0) < 30) {
        errors.push({ productId, error: 'Insufficient data' });
        continue;
      }
      
      const timeSeries = (history.results || []).map((r: any) => ({
        date: new Date(r.date),
        value: r.quantity
      })).reverse();
      
      const seasonalPattern = detectSeasonality(timeSeries);
      const trendAnalysis = analyzeTrend(timeSeries);
      const predictions = exponentialSmoothing(timeSeries, horizon, seasonalPattern);
      const accuracy = calculateAccuracy(timeSeries, 'exponential_smoothing');
      
      forecasts.push({
        productId,
        forecastPeriod: {
          start: predictions[0]?.date || new Date(),
          end: predictions[predictions.length - 1]?.date || new Date()
        },
        predictions,
        accuracy,
        seasonalPattern,
        trendAnalysis,
        recommendations: generateForecastRecommendations(predictions, seasonalPattern, trendAnalysis)
      });
    } catch (e) {
      errors.push({ productId, error: 'Forecast generation failed' });
    }
  }
  
  return c.json({
    forecasts,
    errors,
    summary: {
      successful: forecasts.length,
      failed: errors.length,
      avgAccuracy: forecasts.reduce((sum, f) => sum + (100 - f.accuracy.mape), 0) / forecasts.length
    }
  });
});

// ==================== REORDER ANALYSIS ====================

app.post('/reorder/analyze', async (c) => {
  const { productId, leadTime = 7, serviceLevel = 0.95 } = await c.req.json();
  
  // Get current stock
  const stockResult = await c.env.DB.prepare(`
    SELECT current_stock, unit_cost FROM inventory WHERE product_id = ?
  `).bind(productId).first();
  
  const currentStock = (stockResult?.current_stock as number) || 0;
  const unitCost = (stockResult?.unit_cost as number) || 10;
  
  // Get forecast
  const forecastJson = await c.env.FORECAST_KV.get(`forecast:${productId}`);
  let dailyDemand = 10; // Default
  let demandStdDev = 3;
  
  if (forecastJson) {
    const forecast: ForecastResult = JSON.parse(forecastJson);
    dailyDemand = forecast.predictions.reduce((sum, p) => sum + p.predicted, 0) / forecast.predictions.length;
    demandStdDev = calculateStdDev(forecast.predictions.map(p => p.predicted));
  }
  
  // Calculate reorder parameters
  const zScore = getZScore(serviceLevel);
  const safetyStock = Math.ceil(zScore * demandStdDev * Math.sqrt(leadTime));
  const reorderPoint = Math.ceil(dailyDemand * leadTime + safetyStock);
  
  // Economic Order Quantity (Wilson formula)
  const annualDemand = dailyDemand * 365;
  const orderingCost = 25; // Fixed cost per order
  const holdingCost = unitCost * 0.2; // 20% of unit cost per year
  const eoq = Math.ceil(Math.sqrt((2 * annualDemand * orderingCost) / holdingCost));
  
  // Calculate days until reorder
  const daysUntilReorder = Math.max(0, Math.floor((currentStock - reorderPoint) / dailyDemand));
  
  // Stockout risk
  const stockoutRisk = currentStock <= reorderPoint ? 
    1 - normalCDF((currentStock - dailyDemand * leadTime) / (demandStdDev * Math.sqrt(leadTime))) :
    0.01;
  
  const analysis: ReorderAnalysis = {
    productId,
    currentStock,
    reorderPoint,
    safetyStock,
    economicOrderQuantity: eoq,
    daysUntilReorder,
    recommendedOrderDate: new Date(Date.now() + Math.max(0, daysUntilReorder - 2) * 24 * 60 * 60 * 1000),
    recommendedQuantity: currentStock < reorderPoint ? eoq : 0,
    stockoutRisk
  };
  
  // Store analysis
  await c.env.DB.prepare(`
    INSERT INTO reorder_analysis (product_id, reorder_point, safety_stock, eoq, stockout_risk, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(productId, reorderPoint, safetyStock, eoq, stockoutRisk).run();
  
  return c.json({
    analysis,
    alerts: generateReorderAlerts(analysis),
    parameters: { leadTime, serviceLevel, dailyDemand, demandStdDev }
  });
});

app.get('/reorder/alerts', async (c) => {
  const threshold = parseFloat(c.req.query('threshold') || '0.1');
  
  // Get all products with high stockout risk
  const result = await c.env.DB.prepare(`
    SELECT ra.*, i.product_name
    FROM reorder_analysis ra
    JOIN inventory i ON ra.product_id = i.product_id
    WHERE ra.stockout_risk > ?
    ORDER BY ra.stockout_risk DESC
  `).bind(threshold).all();
  
  const alerts = (result.results || []).map(row => ({
    productId: row.product_id,
    productName: row.product_name,
    stockoutRisk: row.stockout_risk,
    reorderPoint: row.reorder_point,
    recommendedQuantity: row.eoq,
    urgency: (row.stockout_risk as number) > 0.5 ? 'critical' : (row.stockout_risk as number) > 0.2 ? 'high' : 'medium'
  }));
  
  return c.json({
    alerts,
    summary: {
      criticalCount: alerts.filter(a => a.urgency === 'critical').length,
      highCount: alerts.filter(a => a.urgency === 'high').length,
      mediumCount: alerts.filter(a => a.urgency === 'medium').length,
      totalReorderValue: alerts.reduce((sum, a) => sum + (a.recommendedQuantity || 0) * 10, 0)
    }
  });
});

// ==================== DEMAND DRIVERS ====================

app.post('/drivers/analyze', async (c) => {
  const { productId, externalFactors } = await c.req.json();
  
  // Get historical sales
  const salesHistory = await c.env.DB.prepare(`
    SELECT date, quantity FROM sales_history
    WHERE product_id = ?
    ORDER BY date DESC
    LIMIT 365
  `).bind(productId).all();
  
  const sales = (salesHistory.results || []).map((r: any) => ({
    date: new Date(r.date),
    value: r.quantity
  }));
  
  // Analyze demand drivers
  const drivers: DemandDriver[] = [];
  
  // Day of week effect
  const dowEffect = analyzeDayOfWeekEffect(sales);
  if (Math.abs(dowEffect.correlation) > 0.1) {
    drivers.push({
      factor: 'Day of Week',
      correlation: dowEffect.correlation,
      lag: 0,
      importance: Math.abs(dowEffect.correlation),
      predictedImpact: dowEffect.peakDay
    });
  }
  
  // Month effect
  const monthEffect = analyzeMonthEffect(sales);
  if (Math.abs(monthEffect.correlation) > 0.1) {
    drivers.push({
      factor: 'Month/Season',
      correlation: monthEffect.correlation,
      lag: 0,
      importance: Math.abs(monthEffect.correlation),
      predictedImpact: monthEffect.peakMonth
    });
  }
  
  // External factors (price, promotions, weather, etc.)
  if (externalFactors) {
    for (const factor of externalFactors) {
      const correlation = calculateCorrelation(
        sales.map(s => s.value),
        factor.values
      );
      
      if (Math.abs(correlation) > 0.1) {
        drivers.push({
          factor: factor.name,
          correlation,
          lag: factor.lag || 0,
          importance: Math.abs(correlation),
          predictedImpact: correlation * factor.expectedChange
        });
      }
    }
  }
  
  // Sort by importance
  drivers.sort((a, b) => b.importance - a.importance);
  
  return c.json({
    productId,
    drivers,
    topDrivers: drivers.slice(0, 5),
    insights: generateDriverInsights(drivers)
  });
});

// ==================== PROMOTIONAL IMPACT ====================

app.post('/promotion/forecast', async (c) => {
  const { productId, promotionType, discount, startDate, endDate, historicalPromotions } = await c.req.json();
  
  // Analyze historical promotional impact
  let historicalLift = 1.5; // Default 50% lift
  
  if (historicalPromotions && historicalPromotions.length > 0) {
    const lifts = historicalPromotions
      .filter((p: any) => p.type === promotionType)
      .map((p: any) => p.actualLift);
    
    if (lifts.length > 0) {
      historicalLift = lifts.reduce((a: number, b: number) => a + b, 0) / lifts.length;
    }
  }
  
  // Adjust for discount level
  const discountMultiplier = 1 + discount / 100 * 2; // Higher discount = higher lift
  const expectedLift = historicalLift * discountMultiplier;
  
  // Calculate confidence interval
  const stdDev = 0.2 * expectedLift;
  const confidence = {
    lower: expectedLift - 1.96 * stdDev,
    upper: expectedLift + 1.96 * stdDev
  };
  
  // Check for cannibalization effects
  const cannibalizations = await analyzeCannibalizations(c.env, productId, promotionType);
  
  // Get base forecast
  const forecastJson = await c.env.FORECAST_KV.get(`forecast:${productId}`);
  let baseForecast = 100;
  
  if (forecastJson) {
    const forecast: ForecastResult = JSON.parse(forecastJson);
    const start = new Date(startDate);
    const end = new Date(endDate);
    
    const relevantPredictions = forecast.predictions.filter(p => 
      p.date >= start && p.date <= end
    );
    
    baseForecast = relevantPredictions.reduce((sum, p) => sum + p.predicted, 0);
  }
  
  const impact: PromotionalImpact = {
    promotionId: `promo_${Date.now()}`,
    promotionType,
    expectedLift,
    historicalLift,
    confidenceInterval: confidence,
    cannibalizations
  };
  
  return c.json({
    impact,
    forecastedDemand: {
      baseline: baseForecast,
      withPromotion: baseForecast * expectedLift,
      incrementalDemand: baseForecast * (expectedLift - 1),
      lowerBound: baseForecast * confidence.lower,
      upperBound: baseForecast * confidence.upper
    },
    recommendations: generatePromotionRecommendations(impact, discount)
  });
});

// ==================== DEMAND SENSING ====================

app.post('/sense/realtime', async (c) => {
  const { productId, recentSignals } = await c.req.json();
  
  // Get current forecast
  const forecastJson = await c.env.FORECAST_KV.get(`forecast:${productId}`);
  if (!forecastJson) {
    return c.json({ error: 'No forecast found. Generate forecast first.' }, 404);
  }
  
  const forecast: ForecastResult = JSON.parse(forecastJson);
  
  // Analyze recent signals for demand adjustments
  const adjustments: { factor: string; multiplier: number }[] = [];
  
  for (const signal of recentSignals) {
    switch (signal.type) {
      case 'website_traffic':
        // Higher traffic suggests higher demand
        const trafficMultiplier = 1 + (signal.value - signal.baseline) / signal.baseline * 0.5;
        adjustments.push({ factor: 'Website Traffic', multiplier: trafficMultiplier });
        break;
      
      case 'search_volume':
        // Increased searches suggest growing demand
        const searchMultiplier = 1 + (signal.value - signal.baseline) / signal.baseline * 0.3;
        adjustments.push({ factor: 'Search Volume', multiplier: searchMultiplier });
        break;
      
      case 'competitor_stockout':
        // Competitor stockout = demand shift
        adjustments.push({ factor: 'Competitor Stockout', multiplier: 1.2 });
        break;
      
      case 'weather_event':
        // Weather can impact demand
        const weatherMultiplier = signal.favorable ? 1.15 : 0.85;
        adjustments.push({ factor: 'Weather', multiplier: weatherMultiplier });
        break;
      
      case 'social_mention':
        // Viral social mention
        if (signal.sentiment === 'positive') {
          adjustments.push({ factor: 'Social Buzz', multiplier: 1.3 });
        }
        break;
    }
  }
  
  // Calculate combined adjustment
  const combinedMultiplier = adjustments.reduce((mult, adj) => mult * adj.multiplier, 1);
  
  // Adjust forecast
  const adjustedPredictions = forecast.predictions.map(p => ({
    ...p,
    predicted: p.predicted * combinedMultiplier,
    lowerBound: p.lowerBound * combinedMultiplier,
    upperBound: p.upperBound * combinedMultiplier,
    adjustmentApplied: combinedMultiplier
  }));
  
  // Store adjusted forecast
  const adjustedForecast = {
    ...forecast,
    predictions: adjustedPredictions,
    sensingAdjustment: {
      multiplier: combinedMultiplier,
      factors: adjustments,
      timestamp: new Date()
    }
  };
  
  await c.env.FORECAST_KV.put(`forecast:${productId}:sensed`, JSON.stringify(adjustedForecast));
  
  return c.json({
    productId,
    originalForecast: forecast.predictions.slice(0, 7),
    adjustedForecast: adjustedPredictions.slice(0, 7),
    adjustments,
    combinedMultiplier,
    confidence: forecast.accuracy.r2 * (1 - Math.abs(combinedMultiplier - 1) * 0.5)
  });
});

// ==================== HELPER FUNCTIONS ====================

function detectSeasonality(data: TimeSeriesPoint[]): SeasonalPattern {
  if (data.length < 60) {
    return {
      detected: false,
      period: 0,
      peakMonths: [],
      troughMonths: [],
      seasonalIndices: Array(12).fill(1),
      strength: 0
    };
  }
  
  // Calculate monthly averages
  const monthlyAvg = Array(12).fill(0).map(() => ({ sum: 0, count: 0 }));
  
  for (const point of data) {
    const month = point.date.getMonth();
    monthlyAvg[month].sum += point.value;
    monthlyAvg[month].count++;
  }
  
  const overallAvg = data.reduce((sum, p) => sum + p.value, 0) / data.length;
  
  const seasonalIndices = monthlyAvg.map(m => 
    m.count > 0 ? m.sum / m.count / overallAvg : 1
  );
  
  // Detect peaks and troughs
  const peakMonths = seasonalIndices
    .map((v, i) => ({ v, i }))
    .filter(x => x.v > 1.1)
    .map(x => x.i);
  
  const troughMonths = seasonalIndices
    .map((v, i) => ({ v, i }))
    .filter(x => x.v < 0.9)
    .map(x => x.i);
  
  // Calculate seasonality strength
  const variance = seasonalIndices.reduce((sum, v) => sum + Math.pow(v - 1, 2), 0) / 12;
  const strength = Math.min(Math.sqrt(variance) * 5, 1);
  
  return {
    detected: strength > 0.1,
    period: strength > 0.1 ? 365 : 0,
    peakMonths,
    troughMonths,
    seasonalIndices,
    strength
  };
}

function analyzeTrend(data: TimeSeriesPoint[]): TrendAnalysis {
  if (data.length < 10) {
    return {
      direction: 'stable',
      slope: 0,
      changePoints: [],
      growthRate: 0,
      volatility: 0
    };
  }
  
  // Simple linear regression
  const n = data.length;
  let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
  
  for (let i = 0; i < n; i++) {
    sumX += i;
    sumY += data[i].value;
    sumXY += i * data[i].value;
    sumX2 += i * i;
  }
  
  const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
  const avgValue = sumY / n;
  const growthRate = slope / avgValue;
  
  // Determine direction
  let direction: 'increasing' | 'decreasing' | 'stable';
  if (growthRate > 0.01) direction = 'increasing';
  else if (growthRate < -0.01) direction = 'decreasing';
  else direction = 'stable';
  
  // Calculate volatility
  const mean = sumY / n;
  const variance = data.reduce((sum, p) => sum + Math.pow(p.value - mean, 2), 0) / n;
  const volatility = Math.sqrt(variance) / mean;
  
  // Detect change points (simplified)
  const changePoints: ChangePoint[] = [];
  const windowSize = Math.max(Math.floor(n / 10), 3);
  
  for (let i = windowSize; i < n - windowSize; i++) {
    const beforeAvg = data.slice(i - windowSize, i).reduce((sum, p) => sum + p.value, 0) / windowSize;
    const afterAvg = data.slice(i, i + windowSize).reduce((sum, p) => sum + p.value, 0) / windowSize;
    const change = (afterAvg - beforeAvg) / beforeAvg;
    
    if (Math.abs(change) > 0.2) {
      changePoints.push({
        date: data[i].date,
        type: change > 0 ? 'increase' : 'decrease',
        magnitude: Math.abs(change),
        significance: Math.abs(change) / volatility
      });
    }
  }
  
  return {
    direction,
    slope,
    changePoints,
    growthRate,
    volatility
  };
}

function selectBestMethod(data: TimeSeriesPoint[], seasonality: SeasonalPattern): string {
  // Select method based on data characteristics
  if (data.length > 365 && seasonality.detected && seasonality.strength > 0.3) {
    return 'prophet';
  } else if (seasonality.detected) {
    return 'exponential_smoothing';
  } else {
    return 'arima';
  }
}

function exponentialSmoothing(
  data: TimeSeriesPoint[],
  horizon: number,
  seasonality: SeasonalPattern
): ForecastPoint[] {
  const values = data.map(d => d.value);
  const n = values.length;
  
  // Holt-Winters parameters
  const alpha = 0.3;  // Level smoothing
  const beta = 0.1;   // Trend smoothing
  const gamma = 0.2;  // Seasonal smoothing
  
  const period = seasonality.detected ? 12 : 1;
  
  // Initialize components
  let level = values.slice(0, period).reduce((a, b) => a + b, 0) / period;
  let trend = (values.slice(period, 2 * period).reduce((a, b) => a + b, 0) / period - level) / period;
  let seasonal = seasonality.seasonalIndices.length > 0 
    ? [...seasonality.seasonalIndices]
    : Array(period).fill(1);
  
  // Smooth through historical data
  for (let i = 0; i < n; i++) {
    const seasonalIdx = i % period;
    const oldLevel = level;
    
    level = alpha * (values[i] / seasonal[seasonalIdx]) + (1 - alpha) * (level + trend);
    trend = beta * (level - oldLevel) + (1 - beta) * trend;
    seasonal[seasonalIdx] = gamma * (values[i] / level) + (1 - gamma) * seasonal[seasonalIdx];
  }
  
  // Generate forecasts
  const predictions: ForecastPoint[] = [];
  const lastDate = data[n - 1].date;
  
  for (let h = 1; h <= horizon; h++) {
    const forecastDate = new Date(lastDate.getTime() + h * 24 * 60 * 60 * 1000);
    const seasonalIdx = (n + h - 1) % period;
    const predicted = (level + h * trend) * seasonal[seasonalIdx];
    
    // Confidence interval widens with horizon
    const se = calculateStdDev(values) * Math.sqrt(h) * 0.5;
    
    predictions.push({
      date: forecastDate,
      predicted: Math.max(0, predicted),
      lowerBound: Math.max(0, predicted - 1.96 * se),
      upperBound: predicted + 1.96 * se,
      confidence: Math.max(0.5, 0.95 - h * 0.01)
    });
  }
  
  return predictions;
}

function arimaForecast(
  data: TimeSeriesPoint[],
  horizon: number,
  seasonality: SeasonalPattern
): ForecastPoint[] {
  // Simplified ARIMA(1,1,1) implementation
  const values = data.map(d => d.value);
  const n = values.length;
  
  // Difference the series
  const diff = values.slice(1).map((v, i) => v - values[i]);
  
  // AR(1) coefficient
  const ar1 = calculateAutocorrelation(diff, 1);
  
  // MA(1) coefficient (simplified)
  const ma1 = 0.3;
  
  // Forecast
  const predictions: ForecastPoint[] = [];
  const lastDate = data[n - 1].date;
  const lastValue = values[n - 1];
  const lastDiff = diff[diff.length - 1];
  let lastError = 0;
  
  let currentValue = lastValue;
  let currentDiff = lastDiff;
  
  for (let h = 1; h <= horizon; h++) {
    const forecastDate = new Date(lastDate.getTime() + h * 24 * 60 * 60 * 1000);
    
    // ARIMA forecast
    const forecastDiff = ar1 * currentDiff + ma1 * lastError;
    const predicted = currentValue + forecastDiff;
    
    // Confidence interval
    const se = calculateStdDev(diff) * Math.sqrt(h);
    
    predictions.push({
      date: forecastDate,
      predicted: Math.max(0, predicted),
      lowerBound: Math.max(0, predicted - 1.96 * se),
      upperBound: predicted + 1.96 * se,
      confidence: Math.max(0.5, 0.95 - h * 0.015)
    });
    
    currentValue = predicted;
    currentDiff = forecastDiff;
    lastError = 0; // Simplified
  }
  
  return predictions;
}

function prophetStyleForecast(
  data: TimeSeriesPoint[],
  horizon: number,
  seasonality: SeasonalPattern
): ForecastPoint[] {
  // Prophet-style additive model: y = trend + seasonality + noise
  const values = data.map(d => d.value);
  const n = values.length;
  
  // Trend component (piecewise linear)
  const trendAnalysis = analyzeTrend(data);
  
  // Forecast
  const predictions: ForecastPoint[] = [];
  const lastDate = data[n - 1].date;
  const lastValue = values[n - 1];
  
  for (let h = 1; h <= horizon; h++) {
    const forecastDate = new Date(lastDate.getTime() + h * 24 * 60 * 60 * 1000);
    const month = forecastDate.getMonth();
    
    // Trend
    const trendComponent = trendAnalysis.slope * h;
    
    // Seasonality
    const seasonalComponent = seasonality.detected
      ? (seasonality.seasonalIndices[month] - 1) * lastValue
      : 0;
    
    const predicted = lastValue + trendComponent + seasonalComponent;
    
    // Confidence interval
    const se = calculateStdDev(values) * Math.sqrt(h) * 0.4;
    
    predictions.push({
      date: forecastDate,
      predicted: Math.max(0, predicted),
      lowerBound: Math.max(0, predicted - 1.96 * se),
      upperBound: predicted + 1.96 * se,
      confidence: Math.max(0.5, 0.95 - h * 0.01)
    });
  }
  
  return predictions;
}

function calculateAccuracy(data: TimeSeriesPoint[], method: string): ForecastAccuracy {
  // Backtest using last 20% of data
  const testSize = Math.max(Math.floor(data.length * 0.2), 7);
  const trainData = data.slice(0, -testSize);
  const testData = data.slice(-testSize);
  
  const seasonality = detectSeasonality(trainData);
  let predictions: ForecastPoint[];
  
  switch (method) {
    case 'exponential_smoothing':
      predictions = exponentialSmoothing(trainData, testSize, seasonality);
      break;
    case 'arima':
      predictions = arimaForecast(trainData, testSize, seasonality);
      break;
    default:
      predictions = exponentialSmoothing(trainData, testSize, seasonality);
  }
  
  // Calculate error metrics
  const errors = testData.map((actual, i) => ({
    actual: actual.value,
    predicted: predictions[i]?.predicted || actual.value,
    error: actual.value - (predictions[i]?.predicted || actual.value)
  }));
  
  const n = errors.length;
  const mae = errors.reduce((sum, e) => sum + Math.abs(e.error), 0) / n;
  const mse = errors.reduce((sum, e) => sum + e.error * e.error, 0) / n;
  const rmse = Math.sqrt(mse);
  const mape = errors.reduce((sum, e) => sum + Math.abs(e.error / e.actual), 0) / n * 100;
  
  // R-squared
  const actualMean = errors.reduce((sum, e) => sum + e.actual, 0) / n;
  const ssTot = errors.reduce((sum, e) => sum + Math.pow(e.actual - actualMean, 2), 0);
  const ssRes = errors.reduce((sum, e) => sum + e.error * e.error, 0);
  const r2 = 1 - ssRes / ssTot;
  
  return {
    mape: Math.min(mape, 100),
    rmse,
    mae,
    r2: Math.max(0, r2),
    backtestResults: errors.slice(0, 5).map((e, i) => ({
      period: `Day ${i + 1}`,
      actual: e.actual,
      predicted: e.predicted,
      error: e.error,
      percentError: Math.abs(e.error / e.actual) * 100
    }))
  };
}

function generateForecastRecommendations(
  predictions: ForecastPoint[],
  seasonality: SeasonalPattern,
  trend: TrendAnalysis
): InventoryRecommendation[] {
  const recommendations: InventoryRecommendation[] = [];
  
  // Trend-based recommendation
  if (trend.direction === 'increasing' && trend.growthRate > 0.02) {
    recommendations.push({
      type: 'increase_stock',
      priority: 'high',
      description: `Demand trending up ${(trend.growthRate * 100).toFixed(1)}% - increase safety stock`,
      quantityRecommended: Math.ceil(predictions[0].predicted * 0.2),
      timing: 'Immediate',
      expectedImpact: 'Prevent stockouts during growth'
    });
  }
  
  // Seasonal recommendation
  if (seasonality.detected && seasonality.peakMonths.length > 0) {
    const currentMonth = new Date().getMonth();
    const upcomingPeak = seasonality.peakMonths.find(m => m > currentMonth) || seasonality.peakMonths[0];
    const monthsUntilPeak = (upcomingPeak - currentMonth + 12) % 12;
    
    if (monthsUntilPeak <= 2) {
      recommendations.push({
        type: 'seasonal_buildup',
        priority: 'high',
        description: `Peak season in ${monthsUntilPeak} months - build inventory`,
        quantityRecommended: Math.ceil(predictions[0].predicted * (seasonality.seasonalIndices[upcomingPeak] - 1)),
        timing: `Within ${monthsUntilPeak * 4} weeks`,
        expectedImpact: `Capture ${((seasonality.seasonalIndices[upcomingPeak] - 1) * 100).toFixed(0)}% seasonal demand increase`
      });
    }
  }
  
  // Volatility recommendation
  if (trend.volatility > 0.3) {
    recommendations.push({
      type: 'safety_stock',
      priority: 'medium',
      description: 'High demand volatility detected - increase safety stock',
      quantityRecommended: Math.ceil(predictions[0].predicted * trend.volatility),
      timing: 'Next order cycle',
      expectedImpact: 'Buffer against demand variability'
    });
  }
  
  return recommendations;
}

function calculateStdDev(values: number[]): number {
  const n = values.length;
  const mean = values.reduce((a, b) => a + b, 0) / n;
  const variance = values.reduce((sum, v) => sum + Math.pow(v - mean, 2), 0) / n;
  return Math.sqrt(variance);
}

function calculateAutocorrelation(values: number[], lag: number): number {
  const n = values.length;
  const mean = values.reduce((a, b) => a + b, 0) / n;
  
  let numerator = 0;
  let denominator = 0;
  
  for (let i = lag; i < n; i++) {
    numerator += (values[i] - mean) * (values[i - lag] - mean);
  }
  
  for (let i = 0; i < n; i++) {
    denominator += Math.pow(values[i] - mean, 2);
  }
  
  return denominator > 0 ? numerator / denominator : 0;
}

function getZScore(serviceLevel: number): number {
  // Approximate z-score for common service levels
  const zScores: Record<number, number> = {
    0.90: 1.28,
    0.95: 1.65,
    0.99: 2.33
  };
  
  return zScores[serviceLevel] || 1.65;
}

function normalCDF(x: number): number {
  // Approximation of normal CDF
  const a1 = 0.254829592;
  const a2 = -0.284496736;
  const a3 = 1.421413741;
  const a4 = -1.453152027;
  const a5 = 1.061405429;
  const p = 0.3275911;
  
  const sign = x < 0 ? -1 : 1;
  x = Math.abs(x) / Math.sqrt(2);
  
  const t = 1.0 / (1.0 + p * x);
  const y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
  
  return 0.5 * (1.0 + sign * y);
}

function generateReorderAlerts(analysis: ReorderAnalysis): any[] {
  const alerts = [];
  
  if (analysis.stockoutRisk > 0.5) {
    alerts.push({
      type: 'critical',
      message: `Critical stockout risk: ${(analysis.stockoutRisk * 100).toFixed(0)}%`,
      action: `Order ${analysis.recommendedQuantity} units immediately`
    });
  } else if (analysis.currentStock < analysis.reorderPoint) {
    alerts.push({
      type: 'warning',
      message: `Below reorder point (${analysis.currentStock} < ${analysis.reorderPoint})`,
      action: `Place order for ${analysis.recommendedQuantity} units`
    });
  }
  
  if (analysis.daysUntilReorder <= 3) {
    alerts.push({
      type: 'info',
      message: `Reorder needed in ${analysis.daysUntilReorder} days`,
      action: 'Prepare purchase order'
    });
  }
  
  return alerts;
}

function analyzeDayOfWeekEffect(sales: TimeSeriesPoint[]): { correlation: number; peakDay: number } {
  const dayTotals = Array(7).fill(0).map(() => ({ sum: 0, count: 0 }));
  
  for (const sale of sales) {
    const day = sale.date.getDay();
    dayTotals[day].sum += sale.value;
    dayTotals[day].count++;
  }
  
  const avgByDay = dayTotals.map(d => d.count > 0 ? d.sum / d.count : 0);
  const overallAvg = sales.reduce((sum, s) => sum + s.value, 0) / sales.length;
  
  const peakDay = avgByDay.indexOf(Math.max(...avgByDay));
  const variance = avgByDay.reduce((sum, avg) => sum + Math.pow(avg - overallAvg, 2), 0) / 7;
  const correlation = Math.sqrt(variance) / overallAvg;
  
  return { correlation, peakDay };
}

function analyzeMonthEffect(sales: TimeSeriesPoint[]): { correlation: number; peakMonth: number } {
  const monthTotals = Array(12).fill(0).map(() => ({ sum: 0, count: 0 }));
  
  for (const sale of sales) {
    const month = sale.date.getMonth();
    monthTotals[month].sum += sale.value;
    monthTotals[month].count++;
  }
  
  const avgByMonth = monthTotals.map(m => m.count > 0 ? m.sum / m.count : 0);
  const overallAvg = sales.reduce((sum, s) => sum + s.value, 0) / sales.length;
  
  const peakMonth = avgByMonth.indexOf(Math.max(...avgByMonth));
  const variance = avgByMonth.reduce((sum, avg) => sum + Math.pow(avg - overallAvg, 2), 0) / 12;
  const correlation = Math.sqrt(variance) / overallAvg;
  
  return { correlation, peakMonth };
}

function calculateCorrelation(x: number[], y: number[]): number {
  const n = Math.min(x.length, y.length);
  if (n < 2) return 0;
  
  const xMean = x.reduce((a, b) => a + b, 0) / n;
  const yMean = y.reduce((a, b) => a + b, 0) / n;
  
  let numerator = 0;
  let xVar = 0;
  let yVar = 0;
  
  for (let i = 0; i < n; i++) {
    const xDiff = x[i] - xMean;
    const yDiff = y[i] - yMean;
    numerator += xDiff * yDiff;
    xVar += xDiff * xDiff;
    yVar += yDiff * yDiff;
  }
  
  const denominator = Math.sqrt(xVar * yVar);
  return denominator > 0 ? numerator / denominator : 0;
}

function generateDriverInsights(drivers: DemandDriver[]): string[] {
  const insights: string[] = [];
  
  if (drivers.length > 0) {
    insights.push(`Top demand driver: ${drivers[0].factor} (correlation: ${drivers[0].correlation.toFixed(2)})`);
  }
  
  const positiveDrivers = drivers.filter(d => d.correlation > 0.3);
  if (positiveDrivers.length > 0) {
    insights.push(`${positiveDrivers.length} factors positively correlated with demand`);
  }
  
  const negativeDrivers = drivers.filter(d => d.correlation < -0.3);
  if (negativeDrivers.length > 0) {
    insights.push(`${negativeDrivers.length} factors negatively correlated with demand`);
  }
  
  return insights;
}

async function analyzeCannibalizations(env: Env, productId: string, promotionType: string): Promise<any[]> {
  // Simplified cannibalization analysis
  const result = await env.DB.prepare(`
    SELECT p2.product_id, p2.product_name, 0.1 as impact
    FROM products p1
    JOIN products p2 ON p1.category = p2.category AND p1.product_id != p2.product_id
    WHERE p1.product_id = ?
    LIMIT 3
  `).bind(productId).all();
  
  return (result.results || []).map(r => ({
    productId: r.product_id,
    productName: r.product_name,
    impact: -0.1 // 10% reduction
  }));
}

function generatePromotionRecommendations(impact: PromotionalImpact, discount: number): string[] {
  const recommendations: string[] = [];
  
  if (impact.expectedLift > 2) {
    recommendations.push('Expected lift is very high - consider reducing discount');
  }
  
  if (impact.cannibalizations.length > 0) {
    const totalCannibalization = impact.cannibalizations.reduce((sum, c) => sum + Math.abs(c.impact), 0);
    recommendations.push(`Expect ${(totalCannibalization * 100).toFixed(0)}% cannibalization from related products`);
  }
  
  if (discount > 20 && impact.expectedLift < 1.5) {
    recommendations.push('High discount with low expected lift - reconsider promotion strategy');
  }
  
  return recommendations;
}

export default app;
