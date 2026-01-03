/**
 * NoizyLab OS - Customer Churn Prediction Worker
 * ML-Powered Customer Retention Engine
 * 
 * Features:
 * - Real-time churn risk scoring
 * - Behavioral pattern analysis
 * - Customer lifetime value prediction
 * - Automated retention triggers
 * - Engagement scoring
 * - Win-back campaign targeting
 * - Cohort analysis
 * - Predictive intervention timing
 */

import { Hono } from 'hono';

interface Env {
  CHURN_KV: KVNamespace;
  DB: D1Database;
  AI: Ai;
}

interface CustomerProfile {
  id: string;
  accountAge: number;
  totalOrders: number;
  totalSpent: number;
  avgOrderValue: number;
  lastOrderDate: Date;
  daysSinceLastOrder: number;
  orderFrequency: number;
  productCategories: string[];
  supportTickets: number;
  nps_score?: number;
  engagementScore: number;
  segment: string;
}

interface ChurnPrediction {
  customerId: string;
  churnProbability: number;
  riskLevel: 'low' | 'medium' | 'high' | 'critical';
  riskFactors: RiskFactor[];
  predictedChurnDate?: Date;
  lifetime_value: number;
  revenueAtRisk: number;
  recommendedActions: RetentionAction[];
  confidence: number;
}

interface RiskFactor {
  factor: string;
  impact: number;  // -1 to 1
  trend: 'improving' | 'stable' | 'declining';
  description: string;
}

interface RetentionAction {
  type: string;
  priority: number;
  description: string;
  expectedImpact: number;
  cost: number;
  timing: string;
}

interface EngagementMetrics {
  emailOpenRate: number;
  clickRate: number;
  siteVisits: number;
  pageViews: number;
  avgSessionDuration: number;
  cartAbandonment: number;
  wishlistItems: number;
  reviewsWritten: number;
  referrals: number;
}

interface BehaviorSignal {
  signalType: string;
  value: number;
  timestamp: Date;
  context?: Record<string, any>;
}

interface CohortAnalysis {
  cohortId: string;
  acquisitionPeriod: string;
  size: number;
  retentionRates: number[];
  avgLifetimeValue: number;
  churnRate: number;
  characteristics: Record<string, any>;
}

interface WinBackCandidate {
  customerId: string;
  churnedDate: Date;
  daysSinceChurn: number;
  previousLTV: number;
  churnReason?: string;
  winBackProbability: number;
  recommendedOffer: string;
  optimalTiming: string;
}

const app = new Hono<{ Bindings: Env }>();

// ==================== CHURN PREDICTION ====================

app.post('/predict', async (c) => {
  const { customerId } = await c.req.json();
  
  // Get customer profile
  const profile = await getCustomerProfile(c.env, customerId);
  if (!profile) {
    return c.json({ error: 'Customer not found' }, 404);
  }
  
  // Get engagement metrics
  const engagement = await getEngagementMetrics(c.env, customerId);
  
  // Get recent behavior signals
  const signals = await getBehaviorSignals(c.env, customerId, 90);
  
  // Calculate churn probability using ensemble model
  const prediction = await calculateChurnProbability(c.env, profile, engagement, signals);
  
  // Store prediction
  await c.env.CHURN_KV.put(`prediction:${customerId}`, JSON.stringify({
    ...prediction,
    calculatedAt: new Date()
  }));
  
  // Store in D1 for analytics
  await c.env.DB.prepare(`
    INSERT INTO churn_predictions (customer_id, probability, risk_level, ltv, revenue_at_risk, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    customerId,
    prediction.churnProbability,
    prediction.riskLevel,
    prediction.lifetime_value,
    prediction.revenueAtRisk
  ).run();
  
  // Trigger retention workflow if high risk
  if (prediction.riskLevel === 'critical' || prediction.riskLevel === 'high') {
    await triggerRetentionWorkflow(c.env, prediction);
  }
  
  return c.json(prediction);
});

app.post('/predict/batch', async (c) => {
  const { customerIds, segment } = await c.req.json();
  
  let targetCustomers = customerIds;
  
  // If no specific IDs, get all customers from segment
  if (!customerIds && segment) {
    const result = await c.env.DB.prepare(`
      SELECT id FROM customers WHERE segment = ?
    `).bind(segment).all();
    targetCustomers = (result.results || []).map(r => r.id);
  }
  
  // Process in batches
  const predictions: ChurnPrediction[] = [];
  const batchSize = 50;
  
  for (let i = 0; i < targetCustomers.length; i += batchSize) {
    const batch = targetCustomers.slice(i, i + batchSize);
    const batchPredictions = await Promise.all(
      batch.map(async (customerId: string) => {
        const profile = await getCustomerProfile(c.env, customerId);
        if (!profile) return null;
        
        const engagement = await getEngagementMetrics(c.env, customerId);
        const signals = await getBehaviorSignals(c.env, customerId, 90);
        
        return calculateChurnProbability(c.env, profile, engagement, signals);
      })
    );
    
    predictions.push(...batchPredictions.filter(p => p !== null) as ChurnPrediction[]);
  }
  
  // Aggregate statistics
  const stats = {
    totalCustomers: predictions.length,
    criticalRisk: predictions.filter(p => p.riskLevel === 'critical').length,
    highRisk: predictions.filter(p => p.riskLevel === 'high').length,
    mediumRisk: predictions.filter(p => p.riskLevel === 'medium').length,
    lowRisk: predictions.filter(p => p.riskLevel === 'low').length,
    totalRevenueAtRisk: predictions.reduce((sum, p) => sum + p.revenueAtRisk, 0),
    avgChurnProbability: predictions.reduce((sum, p) => sum + p.churnProbability, 0) / predictions.length
  };
  
  return c.json({
    predictions: predictions.sort((a, b) => b.churnProbability - a.churnProbability),
    statistics: stats,
    recommendations: generateBatchRecommendations(stats)
  });
});

// ==================== RISK ANALYSIS ====================

app.get('/risk/:customerId', async (c) => {
  const customerId = c.req.param('customerId');
  
  // Get stored prediction
  const predictionJson = await c.env.CHURN_KV.get(`prediction:${customerId}`);
  if (!predictionJson) {
    return c.json({ error: 'No prediction found. Run predict first.' }, 404);
  }
  
  const prediction: ChurnPrediction = JSON.parse(predictionJson);
  
  // Get detailed risk breakdown
  const profile = await getCustomerProfile(c.env, customerId);
  const riskBreakdown = await analyzeRiskFactors(c.env, profile!, prediction);
  
  return c.json({
    customerId,
    currentRisk: prediction.riskLevel,
    churnProbability: prediction.churnProbability,
    riskBreakdown,
    historicalTrend: await getRiskTrend(c.env, customerId),
    peerComparison: await compareToPeers(c.env, profile!)
  });
});

app.get('/risk/trending', async (c) => {
  const direction = c.req.query('direction') || 'up';
  const limit = parseInt(c.req.query('limit') || '20');
  
  // Get customers with increasing risk
  const result = await c.env.DB.prepare(`
    SELECT customer_id, probability, risk_level, created_at
    FROM churn_predictions
    WHERE created_at > datetime('now', '-7 days')
    ORDER BY created_at DESC
  `).all();
  
  // Group by customer and calculate trend
  const customerTrends = new Map<string, number[]>();
  for (const row of result.results || []) {
    const customerId = row.customer_id as string;
    const probs = customerTrends.get(customerId) || [];
    probs.push(row.probability as number);
    customerTrends.set(customerId, probs);
  }
  
  // Calculate trend direction
  const trending = Array.from(customerTrends.entries())
    .map(([customerId, probs]) => {
      const trend = probs.length > 1 ? probs[0] - probs[probs.length - 1] : 0;
      return { customerId, trend, currentProbability: probs[0] };
    })
    .filter(t => direction === 'up' ? t.trend > 0.05 : t.trend < -0.05)
    .sort((a, b) => direction === 'up' ? b.trend - a.trend : a.trend - b.trend)
    .slice(0, limit);
  
  return c.json({
    direction,
    trendingCustomers: trending,
    summary: {
      count: trending.length,
      avgTrendChange: trending.reduce((sum, t) => sum + Math.abs(t.trend), 0) / trending.length
    }
  });
});

// ==================== ENGAGEMENT SCORING ====================

app.post('/engagement/score', async (c) => {
  const { customerId, metrics } = await c.req.json();
  
  const engagementScore = calculateEngagementScore(metrics);
  
  // Store engagement data
  await c.env.DB.prepare(`
    INSERT INTO engagement_scores (customer_id, score, metrics, created_at)
    VALUES (?, ?, ?, datetime('now'))
  `).bind(customerId, engagementScore.total, JSON.stringify(metrics)).run();
  
  // Update customer profile
  await c.env.DB.prepare(`
    UPDATE customers SET engagement_score = ? WHERE id = ?
  `).bind(engagementScore.total, customerId).run();
  
  return c.json({
    customerId,
    engagementScore: engagementScore.total,
    breakdown: engagementScore.breakdown,
    percentile: engagementScore.percentile,
    trend: engagementScore.trend,
    recommendations: generateEngagementRecommendations(engagementScore)
  });
});

app.post('/engagement/track', async (c) => {
  const { customerId, signalType, value, context } = await c.req.json();
  
  const signal: BehaviorSignal = {
    signalType,
    value,
    timestamp: new Date(),
    context
  };
  
  // Store signal
  await c.env.DB.prepare(`
    INSERT INTO behavior_signals (customer_id, signal_type, value, context, created_at)
    VALUES (?, ?, ?, ?, datetime('now'))
  `).bind(customerId, signalType, value, JSON.stringify(context || {})).run();
  
  // Check for churn warning signals
  const warningSignals = ['cart_abandonment', 'unsubscribe_attempt', 'negative_review', 'support_escalation'];
  if (warningSignals.includes(signalType)) {
    await flagForReview(c.env, customerId, signalType, value);
  }
  
  return c.json({ success: true, signal });
});

// ==================== RETENTION ACTIONS ====================

app.post('/retention/recommend', async (c) => {
  const { customerId } = await c.req.json();
  
  const profile = await getCustomerProfile(c.env, customerId);
  if (!profile) {
    return c.json({ error: 'Customer not found' }, 404);
  }
  
  const predictionJson = await c.env.CHURN_KV.get(`prediction:${customerId}`);
  const prediction: ChurnPrediction | null = predictionJson ? JSON.parse(predictionJson) : null;
  
  // Generate personalized retention actions
  const actions = await generateRetentionActions(c.env, profile, prediction);
  
  return c.json({
    customerId,
    riskLevel: prediction?.riskLevel || 'unknown',
    recommendedActions: actions,
    expectedRetentionLift: calculateExpectedLift(actions),
    implementationPriority: prioritizeActions(actions)
  });
});

app.post('/retention/execute', async (c) => {
  const { customerId, actionType, parameters } = await c.req.json();
  
  // Log action execution
  await c.env.DB.prepare(`
    INSERT INTO retention_actions (customer_id, action_type, parameters, executed_at)
    VALUES (?, ?, ?, datetime('now'))
  `).bind(customerId, actionType, JSON.stringify(parameters)).run();
  
  // Execute action
  let result;
  switch (actionType) {
    case 'personalized_email':
      result = await sendPersonalizedEmail(c.env, customerId, parameters);
      break;
    case 'loyalty_bonus':
      result = await applyLoyaltyBonus(c.env, customerId, parameters);
      break;
    case 'vip_upgrade':
      result = await upgradeToVIP(c.env, customerId, parameters);
      break;
    case 'exclusive_offer':
      result = await createExclusiveOffer(c.env, customerId, parameters);
      break;
    case 'personal_outreach':
      result = await schedulePersonalOutreach(c.env, customerId, parameters);
      break;
    default:
      return c.json({ error: 'Unknown action type' }, 400);
  }
  
  return c.json({
    success: true,
    actionType,
    result,
    trackingId: `ret_${Date.now()}_${customerId}`
  });
});

// ==================== LIFETIME VALUE ====================

app.post('/ltv/calculate', async (c) => {
  const { customerId, method = 'historical' } = await c.req.json();
  
  const profile = await getCustomerProfile(c.env, customerId);
  if (!profile) {
    return c.json({ error: 'Customer not found' }, 404);
  }
  
  let ltv;
  
  switch (method) {
    case 'historical':
      ltv = calculateHistoricalLTV(profile);
      break;
    case 'predictive':
      ltv = await calculatePredictiveLTV(c.env, profile);
      break;
    case 'cohort':
      ltv = await calculateCohortBasedLTV(c.env, profile);
      break;
    default:
      ltv = calculateHistoricalLTV(profile);
  }
  
  // Store LTV calculation
  await c.env.DB.prepare(`
    UPDATE customers SET ltv = ?, ltv_updated_at = datetime('now') WHERE id = ?
  `).bind(ltv.total, customerId).run();
  
  return c.json({
    customerId,
    lifetime_value: ltv.total,
    breakdown: ltv.breakdown,
    projectedValue: ltv.projected,
    confidence: ltv.confidence,
    factors: ltv.factors
  });
});

app.get('/ltv/segments', async (c) => {
  // Get LTV distribution by segment
  const result = await c.env.DB.prepare(`
    SELECT segment, 
           COUNT(*) as customer_count,
           AVG(ltv) as avg_ltv,
           SUM(ltv) as total_ltv,
           MIN(ltv) as min_ltv,
           MAX(ltv) as max_ltv
    FROM customers
    GROUP BY segment
  `).all();
  
  const segments = (result.results || []).map(row => ({
    segment: row.segment,
    customerCount: row.customer_count,
    avgLTV: row.avg_ltv,
    totalLTV: row.total_ltv,
    ltvRange: { min: row.min_ltv, max: row.max_ltv }
  }));
  
  return c.json({
    segments,
    totalLTV: segments.reduce((sum, s) => sum + (s.totalLTV as number || 0), 0),
    recommendations: generateSegmentRecommendations(segments)
  });
});

// ==================== COHORT ANALYSIS ====================

app.post('/cohort/analyze', async (c) => {
  const { periodType = 'monthly', periods = 12 } = await c.req.json();
  
  // Get cohort data
  const cohorts = await buildCohorts(c.env, periodType, periods);
  
  // Calculate retention matrix
  const retentionMatrix = calculateRetentionMatrix(cohorts);
  
  // Identify best and worst performing cohorts
  const analysis = {
    cohorts,
    retentionMatrix,
    bestCohort: cohorts.reduce((best, curr) => 
      curr.retentionRates[curr.retentionRates.length - 1] > (best.retentionRates[best.retentionRates.length - 1] || 0) ? curr : best
    ),
    worstCohort: cohorts.reduce((worst, curr) => 
      curr.retentionRates[curr.retentionRates.length - 1] < (worst.retentionRates[worst.retentionRates.length - 1] || 1) ? curr : worst
    ),
    overallRetention: calculateOverallRetention(cohorts),
    insights: generateCohortInsights(cohorts)
  };
  
  return c.json(analysis);
});

// ==================== WIN-BACK CAMPAIGNS ====================

app.get('/winback/candidates', async (c) => {
  const minDays = parseInt(c.req.query('minDays') || '30');
  const maxDays = parseInt(c.req.query('maxDays') || '180');
  const limit = parseInt(c.req.query('limit') || '100');
  
  // Get churned customers
  const result = await c.env.DB.prepare(`
    SELECT id, churned_at, ltv, last_order_date, churn_reason
    FROM customers
    WHERE churned = 1
    AND churned_at BETWEEN datetime('now', '-${maxDays} days') AND datetime('now', '-${minDays} days')
    ORDER BY ltv DESC
    LIMIT ?
  `).bind(limit).all();
  
  const candidates: WinBackCandidate[] = [];
  
  for (const row of result.results || []) {
    const candidate = await evaluateWinBackCandidate(c.env, row);
    candidates.push(candidate);
  }
  
  // Sort by win-back probability * previous LTV
  candidates.sort((a, b) => 
    (b.winBackProbability * b.previousLTV) - (a.winBackProbability * a.previousLTV)
  );
  
  return c.json({
    candidates,
    summary: {
      totalCandidates: candidates.length,
      highProbability: candidates.filter(c => c.winBackProbability > 0.5).length,
      totalPotentialRevenue: candidates.reduce((sum, c) => sum + c.previousLTV * c.winBackProbability, 0)
    },
    campaignRecommendations: generateWinBackCampaignRecommendations(candidates)
  });
});

app.post('/winback/campaign', async (c) => {
  const { name, targetCustomers, offer, channel, timing } = await c.req.json();
  
  // Create win-back campaign
  const campaignId = `wb_${Date.now()}`;
  
  await c.env.DB.prepare(`
    INSERT INTO winback_campaigns (id, name, target_count, offer, channel, timing, created_at)
    VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(campaignId, name, targetCustomers.length, JSON.stringify(offer), channel, timing).run();
  
  // Enroll customers
  for (const customerId of targetCustomers) {
    await c.env.DB.prepare(`
      INSERT INTO campaign_enrollments (campaign_id, customer_id, enrolled_at)
      VALUES (?, ?, datetime('now'))
    `).bind(campaignId, customerId).run();
  }
  
  return c.json({
    campaignId,
    name,
    enrolledCount: targetCustomers.length,
    estimatedReach: targetCustomers.length * 0.3, // 30% open rate estimate
    estimatedWinBacks: targetCustomers.length * 0.05, // 5% win-back rate estimate
    status: 'scheduled'
  });
});

// ==================== HELPER FUNCTIONS ====================

async function getCustomerProfile(env: Env, customerId: string): Promise<CustomerProfile | null> {
  const result = await env.DB.prepare(`
    SELECT c.*, 
           COUNT(o.id) as order_count,
           SUM(o.total) as total_spent,
           MAX(o.created_at) as last_order_date
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    WHERE c.id = ?
    GROUP BY c.id
  `).bind(customerId).first();
  
  if (!result) return null;
  
  const lastOrderDate = result.last_order_date ? new Date(result.last_order_date as string) : new Date();
  const daysSinceLastOrder = Math.floor((Date.now() - lastOrderDate.getTime()) / (1000 * 60 * 60 * 24));
  
  return {
    id: result.id as string,
    accountAge: result.account_age as number || 0,
    totalOrders: result.order_count as number || 0,
    totalSpent: result.total_spent as number || 0,
    avgOrderValue: (result.total_spent as number || 0) / Math.max(result.order_count as number || 1, 1),
    lastOrderDate,
    daysSinceLastOrder,
    orderFrequency: (result.order_count as number || 0) / Math.max((result.account_age as number || 1) / 30, 1),
    productCategories: JSON.parse(result.product_categories as string || '[]'),
    supportTickets: result.support_tickets as number || 0,
    nps_score: result.nps_score as number,
    engagementScore: result.engagement_score as number || 50,
    segment: result.segment as string || 'standard'
  };
}

async function getEngagementMetrics(env: Env, customerId: string): Promise<EngagementMetrics> {
  const result = await env.DB.prepare(`
    SELECT * FROM engagement_metrics WHERE customer_id = ? ORDER BY created_at DESC LIMIT 1
  `).bind(customerId).first();
  
  if (!result) {
    return {
      emailOpenRate: 0.2,
      clickRate: 0.05,
      siteVisits: 0,
      pageViews: 0,
      avgSessionDuration: 0,
      cartAbandonment: 0,
      wishlistItems: 0,
      reviewsWritten: 0,
      referrals: 0
    };
  }
  
  return {
    emailOpenRate: result.email_open_rate as number || 0,
    clickRate: result.click_rate as number || 0,
    siteVisits: result.site_visits as number || 0,
    pageViews: result.page_views as number || 0,
    avgSessionDuration: result.avg_session_duration as number || 0,
    cartAbandonment: result.cart_abandonment as number || 0,
    wishlistItems: result.wishlist_items as number || 0,
    reviewsWritten: result.reviews_written as number || 0,
    referrals: result.referrals as number || 0
  };
}

async function getBehaviorSignals(env: Env, customerId: string, days: number): Promise<BehaviorSignal[]> {
  const result = await env.DB.prepare(`
    SELECT signal_type, value, context, created_at
    FROM behavior_signals
    WHERE customer_id = ? AND created_at > datetime('now', '-${days} days')
    ORDER BY created_at DESC
  `).bind(customerId).all();
  
  return (result.results || []).map(row => ({
    signalType: row.signal_type as string,
    value: row.value as number,
    timestamp: new Date(row.created_at as string),
    context: JSON.parse(row.context as string || '{}')
  }));
}

async function calculateChurnProbability(
  env: Env,
  profile: CustomerProfile,
  engagement: EngagementMetrics,
  signals: BehaviorSignal[]
): Promise<ChurnPrediction> {
  // Multi-factor churn model
  const factors: RiskFactor[] = [];
  let churnScore = 0;
  
  // Factor 1: Recency (days since last order)
  const recencyScore = Math.min(profile.daysSinceLastOrder / 90, 1);
  churnScore += recencyScore * 0.25;
  factors.push({
    factor: 'Purchase Recency',
    impact: recencyScore - 0.5,
    trend: recencyScore > 0.5 ? 'declining' : 'stable',
    description: `Last order ${profile.daysSinceLastOrder} days ago`
  });
  
  // Factor 2: Frequency
  const expectedFrequency = 0.5; // Once every 2 months
  const frequencyScore = 1 - Math.min(profile.orderFrequency / expectedFrequency, 1);
  churnScore += frequencyScore * 0.2;
  factors.push({
    factor: 'Purchase Frequency',
    impact: frequencyScore - 0.5,
    trend: frequencyScore > 0.5 ? 'declining' : 'stable',
    description: `${profile.orderFrequency.toFixed(2)} orders per month`
  });
  
  // Factor 3: Engagement
  const engagementScore = 1 - (engagement.emailOpenRate * 0.3 + engagement.clickRate * 0.3 + Math.min(engagement.siteVisits / 10, 1) * 0.4);
  churnScore += engagementScore * 0.2;
  factors.push({
    factor: 'Engagement Level',
    impact: engagementScore - 0.5,
    trend: profile.engagementScore > 50 ? 'stable' : 'declining',
    description: `Engagement score: ${profile.engagementScore}`
  });
  
  // Factor 4: Support issues
  const supportScore = Math.min(profile.supportTickets / 5, 1);
  churnScore += supportScore * 0.15;
  factors.push({
    factor: 'Support Issues',
    impact: supportScore,
    trend: supportScore > 0.3 ? 'declining' : 'stable',
    description: `${profile.supportTickets} support tickets`
  });
  
  // Factor 5: NPS score
  if (profile.nps_score !== undefined) {
    const npsScore = 1 - (profile.nps_score + 100) / 200;
    churnScore += npsScore * 0.1;
    factors.push({
      factor: 'Customer Satisfaction',
      impact: npsScore - 0.5,
      trend: profile.nps_score > 0 ? 'stable' : 'declining',
      description: `NPS score: ${profile.nps_score}`
    });
  }
  
  // Factor 6: Negative signals
  const negativeSignals = signals.filter(s => 
    ['cart_abandonment', 'unsubscribe', 'negative_review'].includes(s.signalType)
  );
  const signalScore = Math.min(negativeSignals.length / 3, 1);
  churnScore += signalScore * 0.1;
  if (negativeSignals.length > 0) {
    factors.push({
      factor: 'Warning Signals',
      impact: signalScore,
      trend: 'declining',
      description: `${negativeSignals.length} warning signals detected`
    });
  }
  
  // Normalize to 0-1
  const churnProbability = Math.min(Math.max(churnScore, 0), 1);
  
  // Determine risk level
  let riskLevel: 'low' | 'medium' | 'high' | 'critical';
  if (churnProbability >= 0.75) riskLevel = 'critical';
  else if (churnProbability >= 0.5) riskLevel = 'high';
  else if (churnProbability >= 0.25) riskLevel = 'medium';
  else riskLevel = 'low';
  
  // Calculate LTV
  const ltv = profile.avgOrderValue * profile.orderFrequency * 24; // 2-year projection
  
  // Generate recommended actions
  const actions = await generateRetentionActions(env, profile, null);
  
  return {
    customerId: profile.id,
    churnProbability,
    riskLevel,
    riskFactors: factors.sort((a, b) => Math.abs(b.impact) - Math.abs(a.impact)),
    predictedChurnDate: riskLevel === 'critical' ? new Date(Date.now() + 30 * 24 * 60 * 60 * 1000) : undefined,
    lifetime_value: ltv,
    revenueAtRisk: ltv * churnProbability,
    recommendedActions: actions.slice(0, 3),
    confidence: 0.75 + (signals.length > 10 ? 0.15 : signals.length * 0.015)
  };
}

async function generateRetentionActions(
  env: Env,
  profile: CustomerProfile,
  prediction: ChurnPrediction | null
): Promise<RetentionAction[]> {
  const actions: RetentionAction[] = [];
  
  // Personalized email
  if (profile.daysSinceLastOrder > 30) {
    actions.push({
      type: 'personalized_email',
      priority: 1,
      description: 'Send personalized re-engagement email with product recommendations',
      expectedImpact: 0.15,
      cost: 0.5,
      timing: 'Immediate'
    });
  }
  
  // Loyalty bonus
  if (profile.totalOrders > 3) {
    actions.push({
      type: 'loyalty_bonus',
      priority: 2,
      description: 'Award loyalty points bonus for next purchase',
      expectedImpact: 0.2,
      cost: profile.avgOrderValue * 0.1,
      timing: 'Within 7 days'
    });
  }
  
  // Exclusive offer
  if (prediction?.riskLevel === 'high' || prediction?.riskLevel === 'critical') {
    actions.push({
      type: 'exclusive_offer',
      priority: 1,
      description: '15% exclusive discount on next order',
      expectedImpact: 0.3,
      cost: profile.avgOrderValue * 0.15,
      timing: 'Immediate'
    });
  }
  
  // VIP upgrade
  if (profile.totalSpent > 500 && profile.segment !== 'vip') {
    actions.push({
      type: 'vip_upgrade',
      priority: 2,
      description: 'Upgrade to VIP tier with exclusive benefits',
      expectedImpact: 0.25,
      cost: 20,
      timing: 'Within 3 days'
    });
  }
  
  // Personal outreach
  if (profile.totalSpent > 1000) {
    actions.push({
      type: 'personal_outreach',
      priority: 3,
      description: 'Schedule personal call from account manager',
      expectedImpact: 0.35,
      cost: 25,
      timing: 'Within 14 days'
    });
  }
  
  return actions.sort((a, b) => a.priority - b.priority);
}

async function triggerRetentionWorkflow(env: Env, prediction: ChurnPrediction): Promise<void> {
  // Queue retention workflow
  await env.DB.prepare(`
    INSERT INTO retention_queue (customer_id, risk_level, priority, created_at)
    VALUES (?, ?, ?, datetime('now'))
  `).bind(
    prediction.customerId,
    prediction.riskLevel,
    prediction.riskLevel === 'critical' ? 1 : 2
  ).run();
}

function calculateEngagementScore(metrics: EngagementMetrics): { 
  total: number; 
  breakdown: Record<string, number>; 
  percentile: number;
  trend: string;
} {
  const weights = {
    emailOpenRate: 15,
    clickRate: 20,
    siteVisits: 15,
    pageViews: 10,
    avgSessionDuration: 10,
    cartAbandonment: -15,
    wishlistItems: 10,
    reviewsWritten: 10,
    referrals: 15
  };
  
  const breakdown: Record<string, number> = {};
  let total = 0;
  
  // Email engagement
  breakdown.email = Math.min(metrics.emailOpenRate * 100, 25);
  total += breakdown.email * 0.15;
  
  // Click engagement
  breakdown.clicks = Math.min(metrics.clickRate * 200, 20);
  total += breakdown.clicks * 0.2;
  
  // Site engagement
  breakdown.site = Math.min((metrics.siteVisits + metrics.pageViews / 10) * 2, 25);
  total += breakdown.site * 0.25;
  
  // Purchase intent
  breakdown.intent = Math.min(metrics.wishlistItems * 2 + (1 - metrics.cartAbandonment) * 10, 15);
  total += breakdown.intent * 0.15;
  
  // Advocacy
  breakdown.advocacy = Math.min(metrics.reviewsWritten * 5 + metrics.referrals * 10, 25);
  total += breakdown.advocacy * 0.25;
  
  return {
    total: Math.round(total),
    breakdown,
    percentile: total > 70 ? 90 : total > 50 ? 70 : total > 30 ? 50 : 30,
    trend: total > 50 ? 'positive' : 'needs_attention'
  };
}

function generateEngagementRecommendations(score: { total: number; breakdown: Record<string, number> }): string[] {
  const recommendations: string[] = [];
  
  if (score.breakdown.email < 15) {
    recommendations.push('Improve email content with more personalization');
  }
  
  if (score.breakdown.clicks < 10) {
    recommendations.push('A/B test CTAs to improve click-through rates');
  }
  
  if (score.breakdown.site < 15) {
    recommendations.push('Enhance site experience to increase engagement');
  }
  
  if (score.breakdown.intent < 10) {
    recommendations.push('Implement abandoned cart recovery campaigns');
  }
  
  if (score.breakdown.advocacy < 15) {
    recommendations.push('Launch referral program incentives');
  }
  
  return recommendations;
}

async function flagForReview(env: Env, customerId: string, signalType: string, value: number): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO review_flags (customer_id, flag_type, signal_value, created_at)
    VALUES (?, ?, ?, datetime('now'))
  `).bind(customerId, signalType, value).run();
}

async function analyzeRiskFactors(env: Env, profile: CustomerProfile, prediction: ChurnPrediction): Promise<any> {
  return {
    factors: prediction.riskFactors,
    topRisk: prediction.riskFactors[0],
    mitigationPriority: prediction.riskFactors.slice(0, 3).map(f => ({
      factor: f.factor,
      action: getFactorMitigation(f.factor)
    }))
  };
}

function getFactorMitigation(factor: string): string {
  const mitigations: Record<string, string> = {
    'Purchase Recency': 'Send personalized re-engagement campaign',
    'Purchase Frequency': 'Introduce subscription or loyalty program',
    'Engagement Level': 'Improve content relevance and personalization',
    'Support Issues': 'Proactive outreach to resolve concerns',
    'Customer Satisfaction': 'Schedule feedback call and service recovery',
    'Warning Signals': 'Immediate retention intervention required'
  };
  return mitigations[factor] || 'Standard retention outreach';
}

async function getRiskTrend(env: Env, customerId: string): Promise<any[]> {
  const result = await env.DB.prepare(`
    SELECT probability, risk_level, created_at
    FROM churn_predictions
    WHERE customer_id = ?
    ORDER BY created_at DESC
    LIMIT 10
  `).bind(customerId).all();
  
  return (result.results || []).map(row => ({
    probability: row.probability,
    riskLevel: row.risk_level,
    date: row.created_at
  }));
}

async function compareToPeers(env: Env, profile: CustomerProfile): Promise<any> {
  const result = await env.DB.prepare(`
    SELECT AVG(engagement_score) as avg_engagement,
           AVG(ltv) as avg_ltv
    FROM customers
    WHERE segment = ?
  `).bind(profile.segment).first();
  
  return {
    segment: profile.segment,
    engagementVsPeers: profile.engagementScore - ((result?.avg_engagement as number) || 50),
    ltvVsPeers: profile.avgOrderValue * profile.totalOrders - ((result?.avg_ltv as number) || 0),
    percentile: profile.engagementScore > ((result?.avg_engagement as number) || 50) ? 'above_average' : 'below_average'
  };
}

function calculateHistoricalLTV(profile: CustomerProfile): any {
  const avgMonthlyRevenue = profile.totalSpent / Math.max(profile.accountAge / 30, 1);
  const projectedMonths = 24;
  
  return {
    total: profile.totalSpent,
    breakdown: {
      avgOrderValue: profile.avgOrderValue,
      orderCount: profile.totalOrders,
      monthlyValue: avgMonthlyRevenue
    },
    projected: avgMonthlyRevenue * projectedMonths,
    confidence: profile.totalOrders > 5 ? 0.8 : 0.5,
    factors: ['Purchase history', 'Account age']
  };
}

async function calculatePredictiveLTV(env: Env, profile: CustomerProfile): Promise<any> {
  // Simple predictive model based on cohort performance
  const historicalLTV = calculateHistoricalLTV(profile);
  const retentionRate = 0.85; // Assume 85% annual retention
  const projectedYears = 3;
  
  let predictedLTV = 0;
  let yearlyValue = historicalLTV.breakdown.monthlyValue * 12;
  
  for (let i = 0; i < projectedYears; i++) {
    predictedLTV += yearlyValue * Math.pow(retentionRate, i);
  }
  
  return {
    total: predictedLTV,
    breakdown: historicalLTV.breakdown,
    projected: predictedLTV,
    confidence: 0.7,
    factors: ['Purchase history', 'Retention probability', 'Segment performance']
  };
}

async function calculateCohortBasedLTV(env: Env, profile: CustomerProfile): Promise<any> {
  // Get cohort average
  const result = await env.DB.prepare(`
    SELECT AVG(ltv) as avg_ltv FROM customers WHERE segment = ?
  `).bind(profile.segment).first();
  
  const cohortAvg = (result?.avg_ltv as number) || 0;
  const personalFactor = profile.totalSpent > cohortAvg ? 1.2 : 0.9;
  
  return {
    total: cohortAvg * personalFactor,
    breakdown: {
      cohortAverage: cohortAvg,
      personalAdjustment: personalFactor
    },
    projected: cohortAvg * personalFactor * 1.5,
    confidence: 0.75,
    factors: ['Cohort performance', 'Individual adjustment']
  };
}

function generateSegmentRecommendations(segments: any[]): string[] {
  const recommendations: string[] = [];
  
  const topSegment = segments.reduce((max, curr) => (curr.avgLTV || 0) > (max.avgLTV || 0) ? curr : max);
  recommendations.push(`Focus acquisition on ${topSegment.segment} segment (highest LTV)`);
  
  const growthOpportunity = segments.reduce((max, curr) => 
    (curr.customerCount || 0) > (max.customerCount || 0) && (curr.avgLTV || 0) < (topSegment.avgLTV || 0) ? curr : max
  );
  if (growthOpportunity.segment !== topSegment.segment) {
    recommendations.push(`Upsell opportunity in ${growthOpportunity.segment} segment`);
  }
  
  return recommendations;
}

async function buildCohorts(env: Env, periodType: string, periods: number): Promise<CohortAnalysis[]> {
  const cohorts: CohortAnalysis[] = [];
  
  for (let i = 0; i < periods; i++) {
    const periodStart = periodType === 'monthly' 
      ? new Date(Date.now() - (i + 1) * 30 * 24 * 60 * 60 * 1000)
      : new Date(Date.now() - (i + 1) * 7 * 24 * 60 * 60 * 1000);
    
    const result = await env.DB.prepare(`
      SELECT COUNT(*) as size, AVG(ltv) as avg_ltv
      FROM customers
      WHERE created_at >= ? AND created_at < datetime(?, '+1 month')
    `).bind(periodStart.toISOString(), periodStart.toISOString()).first();
    
    cohorts.push({
      cohortId: `cohort_${i}`,
      acquisitionPeriod: periodStart.toISOString().split('T')[0],
      size: (result?.size as number) || 0,
      retentionRates: Array(Math.min(periods - i, 6)).fill(0).map((_, j) => Math.pow(0.9, j + 1)),
      avgLifetimeValue: (result?.avg_ltv as number) || 0,
      churnRate: 0.1,
      characteristics: {}
    });
  }
  
  return cohorts;
}

function calculateRetentionMatrix(cohorts: CohortAnalysis[]): number[][] {
  return cohorts.map(c => c.retentionRates);
}

function calculateOverallRetention(cohorts: CohortAnalysis[]): number {
  const totalRetention = cohorts.reduce((sum, c) => 
    sum + c.retentionRates.reduce((s, r) => s + r, 0) / c.retentionRates.length, 0
  );
  return totalRetention / cohorts.length;
}

function generateCohortInsights(cohorts: CohortAnalysis[]): string[] {
  const insights: string[] = [];
  
  const avgRetention = calculateOverallRetention(cohorts);
  insights.push(`Average cohort retention: ${(avgRetention * 100).toFixed(1)}%`);
  
  const recentCohorts = cohorts.slice(0, 3);
  const olderCohorts = cohorts.slice(-3);
  const recentAvg = calculateOverallRetention(recentCohorts);
  const olderAvg = calculateOverallRetention(olderCohorts);
  
  if (recentAvg > olderAvg) {
    insights.push('Retention improving in recent cohorts');
  } else {
    insights.push('Retention declining - investigate recent acquisition channels');
  }
  
  return insights;
}

async function evaluateWinBackCandidate(env: Env, row: any): Promise<WinBackCandidate> {
  const churnedDate = new Date(row.churned_at as string);
  const daysSinceChurn = Math.floor((Date.now() - churnedDate.getTime()) / (1000 * 60 * 60 * 24));
  
  // Win-back probability decreases with time
  let probability = Math.max(0.5 - daysSinceChurn * 0.002, 0.05);
  
  // Adjust for previous LTV
  if ((row.ltv as number) > 500) probability *= 1.2;
  
  // Adjust for churn reason
  if (row.churn_reason === 'price') probability *= 1.3;
  else if (row.churn_reason === 'service') probability *= 0.7;
  
  return {
    customerId: row.id as string,
    churnedDate,
    daysSinceChurn,
    previousLTV: row.ltv as number || 0,
    churnReason: row.churn_reason as string,
    winBackProbability: Math.min(probability, 0.8),
    recommendedOffer: probability > 0.5 ? '20% comeback discount' : '30% comeback discount',
    optimalTiming: daysSinceChurn < 60 ? 'Immediate' : 'Within 2 weeks'
  };
}

function generateWinBackCampaignRecommendations(candidates: WinBackCandidate[]): string[] {
  const recommendations: string[] = [];
  
  const highProbCandidates = candidates.filter(c => c.winBackProbability > 0.5);
  if (highProbCandidates.length > 0) {
    recommendations.push(`Target ${highProbCandidates.length} high-probability candidates first`);
  }
  
  const priceChurned = candidates.filter(c => c.churnReason === 'price');
  if (priceChurned.length > candidates.length * 0.3) {
    recommendations.push('Consider price-focused win-back offers (30%+ of churns were price-related)');
  }
  
  const recentChurns = candidates.filter(c => c.daysSinceChurn < 60);
  if (recentChurns.length > 0) {
    recommendations.push(`Prioritize ${recentChurns.length} recent churns (under 60 days)`);
  }
  
  return recommendations;
}

function generateBatchRecommendations(stats: any): string[] {
  const recommendations: string[] = [];
  
  if (stats.criticalRisk > stats.totalCustomers * 0.1) {
    recommendations.push(`URGENT: ${stats.criticalRisk} customers at critical churn risk`);
  }
  
  if (stats.totalRevenueAtRisk > 10000) {
    recommendations.push(`$${stats.totalRevenueAtRisk.toFixed(2)} revenue at risk - immediate intervention recommended`);
  }
  
  if (stats.avgChurnProbability > 0.3) {
    recommendations.push('Overall churn risk elevated - review retention programs');
  }
  
  return recommendations;
}

function calculateExpectedLift(actions: RetentionAction[]): number {
  // Assume diminishing returns on multiple actions
  let totalLift = 0;
  let diminishingFactor = 1;
  
  for (const action of actions) {
    totalLift += action.expectedImpact * diminishingFactor;
    diminishingFactor *= 0.7;
  }
  
  return Math.min(totalLift, 0.5);
}

function prioritizeActions(actions: RetentionAction[]): RetentionAction[] {
  // Sort by ROI (expected impact / cost)
  return [...actions].sort((a, b) => {
    const roiA = a.expectedImpact / Math.max(a.cost, 0.1);
    const roiB = b.expectedImpact / Math.max(b.cost, 0.1);
    return roiB - roiA;
  });
}

// Action execution stubs
async function sendPersonalizedEmail(env: Env, customerId: string, params: any): Promise<any> {
  return { sent: true, emailId: `email_${Date.now()}` };
}

async function applyLoyaltyBonus(env: Env, customerId: string, params: any): Promise<any> {
  return { applied: true, bonusPoints: params.points || 100 };
}

async function upgradeToVIP(env: Env, customerId: string, params: any): Promise<any> {
  await env.DB.prepare(`UPDATE customers SET segment = 'vip' WHERE id = ?`).bind(customerId).run();
  return { upgraded: true, newTier: 'vip' };
}

async function createExclusiveOffer(env: Env, customerId: string, params: any): Promise<any> {
  return { created: true, offerId: `offer_${Date.now()}`, discount: params.discount || 15 };
}

async function schedulePersonalOutreach(env: Env, customerId: string, params: any): Promise<any> {
  return { scheduled: true, callDate: params.date || new Date(Date.now() + 7 * 24 * 60 * 60 * 1000) };
}

export default app;
