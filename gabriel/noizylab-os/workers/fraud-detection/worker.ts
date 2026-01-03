/**
 * NoizyLab OS - Fraud Detection Worker
 * 
 * AI-Powered Fraud Detection System:
 * - Warranty fraud detection
 * - Customer abuse pattern recognition
 * - Serial number manipulation detection
 * - Suspicious claim clustering
 * - Risk scoring with ML models
 * - Real-time transaction monitoring
 * - False positive management
 * - Investigator dashboard support
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  CACHE: KVNamespace;
  AI: any;
  ALERTS_QUEUE: Queue;
  FRAUD_INDEX: VectorizeIndex;
}

interface FraudSignal {
  type: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  score: number;
  evidence: string[];
  metadata: Record<string, any>;
}

interface RiskAssessment {
  transactionId: string;
  customerId: string;
  overallRisk: number;
  riskLevel: 'low' | 'medium' | 'high' | 'critical';
  signals: FraudSignal[];
  recommendation: 'approve' | 'review' | 'reject' | 'investigate';
  confidence: number;
  explanation: string;
  similarCases: any[];
}

interface FraudPattern {
  id: string;
  name: string;
  description: string;
  indicators: string[];
  weightage: number;
  falsePositiveRate: number;
  lastUpdated: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// =============================================================================
// FRAUD PATTERNS DATABASE
// =============================================================================

const FRAUD_PATTERNS: FraudPattern[] = [
  {
    id: 'warranty_stacking',
    name: 'Warranty Stacking',
    description: 'Multiple warranty claims for same issue across different channels',
    indicators: ['multiple_claims_same_device', 'cross_channel_claims', 'timing_overlap'],
    weightage: 0.9,
    falsePositiveRate: 0.05,
    lastUpdated: new Date().toISOString()
  },
  {
    id: 'serial_manipulation',
    name: 'Serial Number Manipulation',
    description: 'Tampered or swapped serial numbers',
    indicators: ['serial_format_anomaly', 'serial_history_gap', 'manufacture_date_mismatch'],
    weightage: 0.95,
    falsePositiveRate: 0.02,
    lastUpdated: new Date().toISOString()
  },
  {
    id: 'professional_returner',
    name: 'Professional Returner',
    description: 'Customer with abnormally high return/claim rate',
    indicators: ['high_claim_frequency', 'multiple_devices', 'pattern_timing'],
    weightage: 0.75,
    falsePositiveRate: 0.15,
    lastUpdated: new Date().toISOString()
  },
  {
    id: 'damage_staging',
    name: 'Damage Staging',
    description: 'Intentional damage claimed as manufacturing defect',
    indicators: ['damage_inconsistency', 'repair_history_conflict', 'timing_suspicious'],
    weightage: 0.85,
    falsePositiveRate: 0.1,
    lastUpdated: new Date().toISOString()
  },
  {
    id: 'identity_ring',
    name: 'Identity Ring',
    description: 'Multiple fake identities used by same person/group',
    indicators: ['address_clustering', 'device_sharing', 'payment_linking'],
    weightage: 0.92,
    falsePositiveRate: 0.03,
    lastUpdated: new Date().toISOString()
  },
  {
    id: 'counterfeit_parts',
    name: 'Counterfeit Parts Claim',
    description: 'Claiming warranty on non-genuine parts',
    indicators: ['part_authenticity_fail', 'supplier_mismatch', 'quality_anomaly'],
    weightage: 0.88,
    falsePositiveRate: 0.08,
    lastUpdated: new Date().toISOString()
  },
  {
    id: 'timing_exploit',
    name: 'Warranty Timing Exploit',
    description: 'Claims submitted just before warranty expiration',
    indicators: ['end_of_warranty_timing', 'backdated_purchase', 'receipt_manipulation'],
    weightage: 0.65,
    falsePositiveRate: 0.2,
    lastUpdated: new Date().toISOString()
  },
  {
    id: 'geographic_anomaly',
    name: 'Geographic Anomaly',
    description: 'Suspicious geographic patterns in claims',
    indicators: ['location_velocity', 'region_clustering', 'cross_border_patterns'],
    weightage: 0.7,
    falsePositiveRate: 0.12,
    lastUpdated: new Date().toISOString()
  }
];

// =============================================================================
// REAL-TIME TRANSACTION SCREENING
// =============================================================================

app.post('/api/screen', async (c) => {
  const { transaction } = await c.req.json();
  
  // Gather all fraud signals
  const signals: FraudSignal[] = [];
  
  // Check velocity (multiple claims in short time)
  const velocitySignal = await checkVelocity(c.env, transaction);
  if (velocitySignal) signals.push(velocitySignal);
  
  // Check customer history
  const historySignal = await checkCustomerHistory(c.env, transaction.customerId);
  if (historySignal) signals.push(historySignal);
  
  // Check device authenticity
  const authenticitySignal = await checkDeviceAuthenticity(c.env, transaction.serialNumber);
  if (authenticitySignal) signals.push(authenticitySignal);
  
  // Check geographic anomalies
  const geoSignal = await checkGeographicAnomaly(c.env, transaction);
  if (geoSignal) signals.push(geoSignal);
  
  // Check amount anomalies
  const amountSignal = await checkAmountAnomaly(c.env, transaction);
  if (amountSignal) signals.push(amountSignal);
  
  // Check for linked identities
  const identitySignal = await checkLinkedIdentities(c.env, transaction);
  if (identitySignal) signals.push(identitySignal);
  
  // AI deep analysis
  const aiSignals = await aiDeepAnalysis(c.env, transaction, signals);
  signals.push(...aiSignals);
  
  // Calculate overall risk score
  const assessment = await calculateRiskAssessment(c.env, transaction, signals);
  
  // Store assessment
  await storeAssessment(c.env, assessment);
  
  // Alert if high risk
  if (assessment.riskLevel === 'critical' || assessment.riskLevel === 'high') {
    await c.env.ALERTS_QUEUE.send({
      type: 'fraud_alert',
      assessment,
      timestamp: Date.now()
    });
  }
  
  return c.json(assessment);
});

async function checkVelocity(env: Env, transaction: any): Promise<FraudSignal | null> {
  const result = await env.DB.prepare(`
    SELECT COUNT(*) as count, SUM(amount) as total
    FROM warranty_claims
    WHERE customer_id = ? AND created_at > datetime('now', '-30 days')
  `).bind(transaction.customerId).first();
  
  const count = (result?.count as number) || 0;
  const total = (result?.total as number) || 0;
  
  // Thresholds
  const CLAIM_THRESHOLD = 3;
  const AMOUNT_THRESHOLD = 1000;
  
  if (count >= CLAIM_THRESHOLD || total >= AMOUNT_THRESHOLD) {
    return {
      type: 'velocity_anomaly',
      severity: count >= 5 ? 'high' : 'medium',
      score: Math.min(1, (count / CLAIM_THRESHOLD + total / AMOUNT_THRESHOLD) / 2),
      evidence: [
        `${count} claims in last 30 days (threshold: ${CLAIM_THRESHOLD})`,
        `$${total.toFixed(2)} total claimed (threshold: $${AMOUNT_THRESHOLD})`
      ],
      metadata: { claimCount: count, totalAmount: total }
    };
  }
  
  return null;
}

async function checkCustomerHistory(env: Env, customerId: string): Promise<FraudSignal | null> {
  const history = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total_claims,
      SUM(CASE WHEN status = 'approved' THEN 1 ELSE 0 END) as approved,
      SUM(CASE WHEN status = 'rejected' THEN 1 ELSE 0 END) as rejected,
      SUM(CASE WHEN flagged_fraud = 1 THEN 1 ELSE 0 END) as flagged,
      AVG(claim_amount) as avg_amount
    FROM warranty_claims
    WHERE customer_id = ?
  `).bind(customerId).first();
  
  if (!history) return null;
  
  const fraudRate = (history.flagged as number) / Math.max(1, history.total_claims as number);
  const rejectionRate = (history.rejected as number) / Math.max(1, history.total_claims as number);
  
  if (fraudRate > 0.1 || rejectionRate > 0.3) {
    return {
      type: 'customer_history_risk',
      severity: fraudRate > 0.2 ? 'high' : 'medium',
      score: Math.max(fraudRate, rejectionRate * 0.7),
      evidence: [
        `${(fraudRate * 100).toFixed(1)}% fraud flag rate`,
        `${(rejectionRate * 100).toFixed(1)}% rejection rate`,
        `${history.total_claims} total claims`
      ],
      metadata: { ...history }
    };
  }
  
  return null;
}

async function checkDeviceAuthenticity(env: Env, serialNumber: string): Promise<FraudSignal | null> {
  // Check serial number format
  const validFormats = [
    /^[A-Z]{2}\d{10}$/,           // Standard format
    /^[A-Z0-9]{12}$/,              // Compact format
    /^\d{3}-\d{7}-[A-Z]{2}$/       // Alternate format
  ];
  
  const isValidFormat = validFormats.some(f => f.test(serialNumber));
  
  // Check if serial exists in authentic registry
  const authentic = await env.DB.prepare(`
    SELECT * FROM device_registry WHERE serial_number = ?
  `).bind(serialNumber).first();
  
  // Check for serial number reuse
  const claimHistory = await env.DB.prepare(`
    SELECT COUNT(DISTINCT customer_id) as owners
    FROM warranty_claims WHERE serial_number = ?
  `).bind(serialNumber).first();
  
  const signals: string[] = [];
  let score = 0;
  
  if (!isValidFormat) {
    signals.push('Serial number format anomaly detected');
    score += 0.4;
  }
  
  if (!authentic) {
    signals.push('Serial number not found in authentic registry');
    score += 0.5;
  }
  
  if ((claimHistory?.owners as number) > 2) {
    signals.push(`Serial claimed by ${claimHistory?.owners} different customers`);
    score += 0.3;
  }
  
  if (score > 0) {
    return {
      type: 'device_authenticity',
      severity: score > 0.7 ? 'critical' : score > 0.4 ? 'high' : 'medium',
      score: Math.min(1, score),
      evidence: signals,
      metadata: { serialNumber, isValidFormat, isAuthentic: !!authentic }
    };
  }
  
  return null;
}

async function checkGeographicAnomaly(env: Env, transaction: any): Promise<FraudSignal | null> {
  if (!transaction.location) return null;
  
  // Check location velocity (impossible travel)
  const lastLocation = await env.DB.prepare(`
    SELECT location_lat, location_lng, created_at
    FROM warranty_claims
    WHERE customer_id = ?
    ORDER BY created_at DESC LIMIT 1
  `).bind(transaction.customerId).first();
  
  if (lastLocation && lastLocation.location_lat) {
    const distance = calculateDistance(
      lastLocation.location_lat as number,
      lastLocation.location_lng as number,
      transaction.location.lat,
      transaction.location.lng
    );
    
    const timeDiff = Date.now() - new Date(lastLocation.created_at as string).getTime();
    const hours = timeDiff / (1000 * 60 * 60);
    const impossibleSpeed = distance / hours; // km/h
    
    if (impossibleSpeed > 1000) { // Faster than commercial flight
      return {
        type: 'geographic_anomaly',
        severity: 'high',
        score: Math.min(1, impossibleSpeed / 2000),
        evidence: [
          `${distance.toFixed(0)}km traveled in ${hours.toFixed(1)} hours`,
          `Implied speed: ${impossibleSpeed.toFixed(0)} km/h (impossible)`
        ],
        metadata: { distance, hours, speed: impossibleSpeed }
      };
    }
  }
  
  // Check for high-fraud regions
  const regionStats = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total,
      SUM(CASE WHEN flagged_fraud = 1 THEN 1 ELSE 0 END) as fraud
    FROM warranty_claims
    WHERE region = ?
  `).bind(transaction.region).first();
  
  if (regionStats) {
    const regionFraudRate = (regionStats.fraud as number) / Math.max(1, regionStats.total as number);
    if (regionFraudRate > 0.15) {
      return {
        type: 'high_fraud_region',
        severity: 'medium',
        score: regionFraudRate,
        evidence: [`Region ${transaction.region} has ${(regionFraudRate * 100).toFixed(1)}% fraud rate`],
        metadata: { region: transaction.region, fraudRate: regionFraudRate }
      };
    }
  }
  
  return null;
}

function calculateDistance(lat1: number, lon1: number, lat2: number, lon2: number): number {
  const R = 6371; // Earth's radius in km
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
            Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
            Math.sin(dLon/2) * Math.sin(dLon/2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  return R * c;
}

async function checkAmountAnomaly(env: Env, transaction: any): Promise<FraudSignal | null> {
  // Get device value and repair cost statistics
  const stats = await env.DB.prepare(`
    SELECT 
      AVG(claim_amount) as avg_amount,
      MAX(claim_amount) as max_amount,
      STDEV(claim_amount) as std_amount
    FROM warranty_claims
    WHERE device_type = ?
  `).bind(transaction.deviceType).first();
  
  if (!stats || !stats.avg_amount) return null;
  
  const avgAmount = stats.avg_amount as number;
  const stdAmount = (stats.std_amount as number) || avgAmount * 0.3;
  const zScore = (transaction.amount - avgAmount) / stdAmount;
  
  if (Math.abs(zScore) > 2) {
    return {
      type: 'amount_anomaly',
      severity: Math.abs(zScore) > 3 ? 'high' : 'medium',
      score: Math.min(1, Math.abs(zScore) / 4),
      evidence: [
        `Claim amount $${transaction.amount} is ${zScore.toFixed(1)} std deviations from mean`,
        `Average for ${transaction.deviceType}: $${avgAmount.toFixed(2)}`
      ],
      metadata: { zScore, avgAmount, claimAmount: transaction.amount }
    };
  }
  
  return null;
}

async function checkLinkedIdentities(env: Env, transaction: any): Promise<FraudSignal | null> {
  // Find linked accounts through various signals
  const links = await env.DB.prepare(`
    SELECT DISTINCT c2.customer_id, c2.email, c2.phone
    FROM customers c1
    JOIN customers c2 ON (
      c1.device_fingerprint = c2.device_fingerprint OR
      c1.payment_hash = c2.payment_hash OR
      c1.address_hash = c2.address_hash OR
      c1.ip_address = c2.ip_address
    )
    WHERE c1.customer_id = ? AND c2.customer_id != ?
  `).bind(transaction.customerId, transaction.customerId).all();
  
  if (links.results && links.results.length > 0) {
    // Check fraud history of linked accounts
    const linkedIds = links.results.map((l: any) => l.customer_id);
    const linkedFraud = await env.DB.prepare(`
      SELECT COUNT(*) as fraud_count
      FROM warranty_claims
      WHERE customer_id IN (${linkedIds.map(() => '?').join(',')})
        AND flagged_fraud = 1
    `).bind(...linkedIds).first();
    
    const fraudCount = (linkedFraud?.fraud_count as number) || 0;
    
    if (fraudCount > 0 || links.results.length > 3) {
      return {
        type: 'linked_identity_risk',
        severity: fraudCount > 2 ? 'critical' : fraudCount > 0 ? 'high' : 'medium',
        score: Math.min(1, (links.results.length / 5) + (fraudCount / 3)),
        evidence: [
          `${links.results.length} linked accounts detected`,
          `${fraudCount} fraud flags on linked accounts`
        ],
        metadata: { linkedAccounts: links.results.length, linkedFraudCount: fraudCount }
      };
    }
  }
  
  return null;
}

async function aiDeepAnalysis(env: Env, transaction: any, existingSignals: FraudSignal[]): Promise<FraudSignal[]> {
  const signals: FraudSignal[] = [];
  
  // Use AI to analyze claim description for inconsistencies
  if (transaction.description) {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      messages: [
        {
          role: 'system',
          content: `You are a fraud detection AI. Analyze warranty claim descriptions for signs of fraud.
          
Look for:
- Inconsistencies in the story
- Technical impossibilities
- Coached/scripted language
- Emotional manipulation
- Vague damage descriptions
- Suspicious timing mentions

Respond with JSON:
{
  "fraud_likelihood": 0-1,
  "red_flags": ["flag1", "flag2"],
  "analysis": "brief analysis"
}`
        },
        {
          role: 'user',
          content: `Analyze this claim: Device: ${transaction.deviceType}, Issue: ${transaction.description}, Amount: $${transaction.amount}`
        }
      ]
    });
    
    try {
      const analysis = JSON.parse(response.response);
      if (analysis.fraud_likelihood > 0.5) {
        signals.push({
          type: 'ai_content_analysis',
          severity: analysis.fraud_likelihood > 0.8 ? 'high' : 'medium',
          score: analysis.fraud_likelihood,
          evidence: analysis.red_flags,
          metadata: { analysis: analysis.analysis }
        });
      }
    } catch (e) {
      // AI response parsing failed, skip
    }
  }
  
  // Pattern matching across historical fraud cases
  const historicalMatch = await findSimilarFraudCases(env, transaction);
  if (historicalMatch.similarity > 0.8) {
    signals.push({
      type: 'historical_pattern_match',
      severity: 'high',
      score: historicalMatch.similarity,
      evidence: [`Matches ${historicalMatch.matchCount} known fraud patterns`],
      metadata: { ...historicalMatch }
    });
  }
  
  return signals;
}

async function findSimilarFraudCases(env: Env, transaction: any): Promise<{ similarity: number; matchCount: number }> {
  // Create embedding of current transaction
  const embedding = await env.AI.run('@cf/baai/bge-base-en-v1.5', {
    text: `${transaction.deviceType} ${transaction.description} ${transaction.amount}`
  });
  
  // Search for similar fraud cases
  const similar = await env.FRAUD_INDEX.query(embedding.data[0], {
    topK: 5,
    filter: { fraud_confirmed: true }
  });
  
  if (similar.matches && similar.matches.length > 0) {
    const avgSimilarity = similar.matches.reduce((sum, m) => sum + m.score, 0) / similar.matches.length;
    return {
      similarity: avgSimilarity,
      matchCount: similar.matches.length
    };
  }
  
  return { similarity: 0, matchCount: 0 };
}

async function calculateRiskAssessment(env: Env, transaction: any, signals: FraudSignal[]): Promise<RiskAssessment> {
  // Weighted risk calculation
  let totalWeight = 0;
  let weightedScore = 0;
  
  const severityWeights = { low: 0.3, medium: 0.5, high: 0.8, critical: 1.0 };
  
  for (const signal of signals) {
    const weight = severityWeights[signal.severity];
    weightedScore += signal.score * weight;
    totalWeight += weight;
  }
  
  const overallRisk = totalWeight > 0 ? weightedScore / totalWeight : 0;
  
  // Determine risk level
  let riskLevel: 'low' | 'medium' | 'high' | 'critical' = 'low';
  if (overallRisk > 0.8) riskLevel = 'critical';
  else if (overallRisk > 0.6) riskLevel = 'high';
  else if (overallRisk > 0.3) riskLevel = 'medium';
  
  // Determine recommendation
  let recommendation: 'approve' | 'review' | 'reject' | 'investigate' = 'approve';
  if (riskLevel === 'critical') recommendation = 'reject';
  else if (riskLevel === 'high') recommendation = 'investigate';
  else if (riskLevel === 'medium') recommendation = 'review';
  
  // Generate explanation
  const explanation = await generateExplanation(env, signals, riskLevel);
  
  return {
    transactionId: transaction.id,
    customerId: transaction.customerId,
    overallRisk,
    riskLevel,
    signals,
    recommendation,
    confidence: Math.min(0.95, 0.5 + signals.length * 0.1),
    explanation,
    similarCases: []
  };
}

async function generateExplanation(env: Env, signals: FraudSignal[], riskLevel: string): Promise<string> {
  if (signals.length === 0) {
    return 'No fraud indicators detected. Transaction appears legitimate.';
  }
  
  const signalSummary = signals.map(s => `${s.type}: ${s.evidence[0]}`).join('; ');
  
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'Generate a brief, professional fraud risk explanation for human reviewers. Be factual and concise.'
      },
      {
        role: 'user',
        content: `Risk Level: ${riskLevel}. Signals: ${signalSummary}`
      }
    ]
  });
  
  return response.response || `Risk assessment: ${riskLevel}. Multiple fraud indicators detected.`;
}

async function storeAssessment(env: Env, assessment: RiskAssessment): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO fraud_assessments (
      transaction_id, customer_id, overall_risk, risk_level,
      recommendation, confidence, signals_json, explanation, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    assessment.transactionId,
    assessment.customerId,
    assessment.overallRisk,
    assessment.riskLevel,
    assessment.recommendation,
    assessment.confidence,
    JSON.stringify(assessment.signals),
    assessment.explanation
  ).run();
}

// =============================================================================
// FRAUD INVESTIGATION APIs
// =============================================================================

app.get('/api/cases/pending', async (c) => {
  const limit = parseInt(c.req.query('limit') || '50');
  const severity = c.req.query('severity');
  
  let query = `
    SELECT fa.*, c.name as customer_name, c.email
    FROM fraud_assessments fa
    JOIN customers c ON fa.customer_id = c.customer_id
    WHERE fa.status = 'pending'
  `;
  
  if (severity) {
    query += ` AND fa.risk_level = '${severity}'`;
  }
  
  query += ` ORDER BY fa.overall_risk DESC LIMIT ${limit}`;
  
  const cases = await c.env.DB.prepare(query).all();
  
  return c.json({
    cases: cases.results?.map((r: any) => ({
      ...r,
      signals: JSON.parse(r.signals_json || '[]')
    })),
    total: cases.results?.length || 0
  });
});

app.get('/api/case/:id', async (c) => {
  const caseId = c.req.param('id');
  
  const fraudCase = await c.env.DB.prepare(`
    SELECT fa.*, c.*, 
           GROUP_CONCAT(wc.id) as related_claims
    FROM fraud_assessments fa
    JOIN customers c ON fa.customer_id = c.customer_id
    LEFT JOIN warranty_claims wc ON wc.customer_id = c.customer_id
    WHERE fa.id = ?
    GROUP BY fa.id
  `).bind(caseId).first();
  
  if (!fraudCase) {
    return c.json({ error: 'Case not found' }, 404);
  }
  
  // Get investigation timeline
  const timeline = await c.env.DB.prepare(`
    SELECT * FROM fraud_investigation_logs
    WHERE assessment_id = ?
    ORDER BY created_at DESC
  `).bind(caseId).all();
  
  // Get similar confirmed fraud cases
  const similar = await c.env.DB.prepare(`
    SELECT * FROM fraud_assessments
    WHERE risk_level IN ('high', 'critical')
      AND status = 'confirmed_fraud'
      AND id != ?
    ORDER BY ABS(overall_risk - ?) ASC
    LIMIT 5
  `).bind(caseId, fraudCase.overall_risk).all();
  
  return c.json({
    case: {
      ...fraudCase,
      signals: JSON.parse((fraudCase as any).signals_json || '[]')
    },
    timeline: timeline.results,
    similarCases: similar.results
  });
});

app.post('/api/case/:id/decision', async (c) => {
  const caseId = c.req.param('id');
  const { decision, notes, investigatorId } = await c.req.json();
  
  // Update case status
  await c.env.DB.prepare(`
    UPDATE fraud_assessments
    SET status = ?, investigator_id = ?, resolved_at = datetime('now')
    WHERE id = ?
  `).bind(decision, investigatorId, caseId).run();
  
  // Log investigation action
  await c.env.DB.prepare(`
    INSERT INTO fraud_investigation_logs (
      assessment_id, action, notes, investigator_id, created_at
    ) VALUES (?, ?, ?, ?, datetime('now'))
  `).bind(caseId, decision, notes, investigatorId).run();
  
  // Update ML model feedback
  if (decision === 'confirmed_fraud' || decision === 'false_positive') {
    await updateModelFeedback(c.env, caseId, decision);
  }
  
  return c.json({ success: true, decision });
});

async function updateModelFeedback(env: Env, caseId: string, decision: string): Promise<void> {
  const fraudCase = await env.DB.prepare(`
    SELECT * FROM fraud_assessments WHERE id = ?
  `).bind(caseId).first();
  
  if (fraudCase) {
    // Store feedback for model retraining
    await env.DB.prepare(`
      INSERT INTO model_feedback (
        case_id, prediction, actual_result, signals_json, created_at
      ) VALUES (?, ?, ?, ?, datetime('now'))
    `).bind(
      caseId,
      fraudCase.risk_level,
      decision === 'confirmed_fraud' ? 'fraud' : 'legitimate',
      fraudCase.signals_json
    ).run();
  }
}

// =============================================================================
// PATTERN MANAGEMENT
// =============================================================================

app.get('/api/patterns', async (c) => {
  const patterns = await c.env.DB.prepare(`
    SELECT fp.*, 
           COUNT(DISTINCT fa.id) as matches,
           SUM(CASE WHEN fa.status = 'confirmed_fraud' THEN 1 ELSE 0 END) as confirmed
    FROM fraud_patterns fp
    LEFT JOIN fraud_pattern_matches fpm ON fp.id = fpm.pattern_id
    LEFT JOIN fraud_assessments fa ON fpm.assessment_id = fa.id
    GROUP BY fp.id
    ORDER BY fp.weightage DESC
  `).all();
  
  return c.json({
    patterns: patterns.results,
    builtIn: FRAUD_PATTERNS
  });
});

app.post('/api/patterns', async (c) => {
  const pattern = await c.req.json();
  
  await c.env.DB.prepare(`
    INSERT INTO fraud_patterns (
      id, name, description, indicators_json, weightage, created_at
    ) VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    pattern.id || crypto.randomUUID(),
    pattern.name,
    pattern.description,
    JSON.stringify(pattern.indicators),
    pattern.weightage
  ).run();
  
  return c.json({ success: true, pattern });
});

// =============================================================================
// ANALYTICS & REPORTING
// =============================================================================

app.get('/api/analytics/dashboard', async (c) => {
  const timeframe = c.req.query('timeframe') || '30d';
  const days = parseInt(timeframe) || 30;
  
  // Overall statistics
  const stats = await c.env.DB.prepare(`
    SELECT 
      COUNT(*) as total_screened,
      SUM(CASE WHEN risk_level = 'critical' THEN 1 ELSE 0 END) as critical,
      SUM(CASE WHEN risk_level = 'high' THEN 1 ELSE 0 END) as high,
      SUM(CASE WHEN risk_level = 'medium' THEN 1 ELSE 0 END) as medium,
      SUM(CASE WHEN risk_level = 'low' THEN 1 ELSE 0 END) as low,
      SUM(CASE WHEN status = 'confirmed_fraud' THEN 1 ELSE 0 END) as confirmed_fraud,
      SUM(CASE WHEN status = 'false_positive' THEN 1 ELSE 0 END) as false_positives,
      AVG(overall_risk) as avg_risk_score
    FROM fraud_assessments
    WHERE created_at > datetime('now', '-${days} days')
  `).first();
  
  // Fraud trend over time
  const trend = await c.env.DB.prepare(`
    SELECT 
      DATE(created_at) as date,
      COUNT(*) as total,
      SUM(CASE WHEN risk_level IN ('high', 'critical') THEN 1 ELSE 0 END) as flagged,
      AVG(overall_risk) as avg_risk
    FROM fraud_assessments
    WHERE created_at > datetime('now', '-${days} days')
    GROUP BY DATE(created_at)
    ORDER BY date ASC
  `).all();
  
  // Top fraud patterns
  const topPatterns = await c.env.DB.prepare(`
    SELECT 
      json_extract(signals_json, '$[0].type') as pattern_type,
      COUNT(*) as occurrences,
      AVG(overall_risk) as avg_risk
    FROM fraud_assessments
    WHERE risk_level IN ('high', 'critical')
      AND created_at > datetime('now', '-${days} days')
    GROUP BY pattern_type
    ORDER BY occurrences DESC
    LIMIT 10
  `).all();
  
  // Financial impact
  const impact = await c.env.DB.prepare(`
    SELECT 
      SUM(CASE WHEN fa.status = 'confirmed_fraud' THEN wc.claim_amount ELSE 0 END) as prevented_loss,
      SUM(CASE WHEN fa.status = 'false_positive' THEN wc.claim_amount ELSE 0 END) as potential_friction,
      COUNT(DISTINCT fa.customer_id) as affected_customers
    FROM fraud_assessments fa
    JOIN warranty_claims wc ON fa.transaction_id = wc.id
    WHERE fa.created_at > datetime('now', '-${days} days')
  `).first();
  
  return c.json({
    stats,
    trend: trend.results,
    topPatterns: topPatterns.results,
    impact,
    modelPerformance: {
      precision: stats ? 
        (stats.confirmed_fraud as number) / 
        Math.max(1, (stats.confirmed_fraud as number) + (stats.false_positives as number)) : 0,
      alertRate: stats ?
        ((stats.high as number) + (stats.critical as number)) / 
        Math.max(1, stats.total_screened as number) : 0
    }
  });
});

app.get('/api/analytics/rings', async (c) => {
  // Detect potential fraud rings (connected groups of suspicious accounts)
  const rings = await c.env.DB.prepare(`
    WITH linked AS (
      SELECT 
        c1.customer_id as id1,
        c2.customer_id as id2,
        CASE 
          WHEN c1.device_fingerprint = c2.device_fingerprint THEN 'device'
          WHEN c1.payment_hash = c2.payment_hash THEN 'payment'
          WHEN c1.address_hash = c2.address_hash THEN 'address'
          WHEN c1.ip_address = c2.ip_address THEN 'ip'
        END as link_type
      FROM customers c1
      JOIN customers c2 ON c1.customer_id < c2.customer_id
      WHERE c1.device_fingerprint = c2.device_fingerprint
         OR c1.payment_hash = c2.payment_hash
         OR c1.address_hash = c2.address_hash
         OR c1.ip_address = c2.ip_address
    )
    SELECT 
      id1, id2, link_type,
      (SELECT COUNT(*) FROM fraud_assessments WHERE customer_id = id1 AND risk_level IN ('high', 'critical')) as fraud1,
      (SELECT COUNT(*) FROM fraud_assessments WHERE customer_id = id2 AND risk_level IN ('high', 'critical')) as fraud2
    FROM linked
    WHERE fraud1 > 0 OR fraud2 > 0
    ORDER BY (fraud1 + fraud2) DESC
    LIMIT 100
  `).all();
  
  // Build graph of rings
  const graph = new Map<string, Set<string>>();
  
  for (const link of (rings.results || [])) {
    const l = link as any;
    if (!graph.has(l.id1)) graph.set(l.id1, new Set());
    if (!graph.has(l.id2)) graph.set(l.id2, new Set());
    graph.get(l.id1)!.add(l.id2);
    graph.get(l.id2)!.add(l.id1);
  }
  
  // Find connected components (rings)
  const visited = new Set<string>();
  const detectedRings: any[] = [];
  
  function dfs(node: string, ring: string[]): void {
    visited.add(node);
    ring.push(node);
    const neighbors = graph.get(node);
    if (neighbors) {
      for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
          dfs(neighbor, ring);
        }
      }
    }
  }
  
  for (const node of graph.keys()) {
    if (!visited.has(node)) {
      const ring: string[] = [];
      dfs(node, ring);
      if (ring.length >= 3) {
        detectedRings.push({
          members: ring,
          size: ring.length,
          riskScore: ring.length * 0.15 + 0.5
        });
      }
    }
  }
  
  return c.json({
    rings: detectedRings.sort((a, b) => b.size - a.size).slice(0, 20),
    totalSuspiciousLinks: rings.results?.length || 0
  });
});

// =============================================================================
// REAL-TIME MONITORING
// =============================================================================

app.get('/api/monitor/live', async (c) => {
  const lastId = c.req.query('since') || '0';
  
  const recent = await c.env.DB.prepare(`
    SELECT fa.*, c.name as customer_name
    FROM fraud_assessments fa
    JOIN customers c ON fa.customer_id = c.customer_id
    WHERE fa.id > ?
    ORDER BY fa.created_at DESC
    LIMIT 50
  `).bind(lastId).all();
  
  return c.json({
    assessments: recent.results?.map((r: any) => ({
      ...r,
      signals: JSON.parse(r.signals_json || '[]')
    })),
    lastId: recent.results?.[0]?.id || lastId
  });
});

// =============================================================================
// BATCH ANALYSIS
// =============================================================================

app.post('/api/batch/analyze', async (c) => {
  const { transactionIds } = await c.req.json();
  
  const results = [];
  
  for (const txId of transactionIds) {
    const tx = await c.env.DB.prepare(`
      SELECT * FROM warranty_claims WHERE id = ?
    `).bind(txId).first();
    
    if (tx) {
      // Reuse screening logic
      const assessment = await screenTransaction(c.env, tx);
      results.push(assessment);
    }
  }
  
  return c.json({
    analyzed: results.length,
    highRisk: results.filter(r => r.riskLevel === 'high' || r.riskLevel === 'critical').length,
    results
  });
});

async function screenTransaction(env: Env, transaction: any): Promise<RiskAssessment> {
  const signals: FraudSignal[] = [];
  
  const velocitySignal = await checkVelocity(env, transaction);
  if (velocitySignal) signals.push(velocitySignal);
  
  const historySignal = await checkCustomerHistory(env, transaction.customer_id);
  if (historySignal) signals.push(historySignal);
  
  return calculateRiskAssessment(env, transaction, signals);
}

export default app;
