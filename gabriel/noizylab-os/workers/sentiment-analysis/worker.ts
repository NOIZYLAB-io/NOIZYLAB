/**
 * NoizyLab OS - Sentiment Analysis Worker
 * 
 * Real-Time Emotion Intelligence System:
 * - Customer sentiment detection from text/voice/behavior
 * - Frustration level monitoring and escalation triggers
 * - Conversation tone analysis and recommendations
 * - Customer satisfaction prediction
 * - Emotion timeline tracking per customer
 * - Agent performance sentiment scoring
 * - Proactive intervention triggers
 * - Multi-language sentiment support
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  CACHE: KVNamespace;
  AI: any;
  ALERTS_QUEUE: Queue;
  SENTIMENT_INDEX: VectorizeIndex;
}

interface SentimentAnalysis {
  id: string;
  overallSentiment: 'very_negative' | 'negative' | 'neutral' | 'positive' | 'very_positive';
  sentimentScore: number; // -1 to 1
  emotions: EmotionBreakdown;
  frustrationLevel: number; // 0-100
  urgencyLevel: number; // 0-100
  escalationRisk: number; // 0-100
  keyPhrases: string[];
  recommendations: string[];
  confidence: number;
}

interface EmotionBreakdown {
  joy: number;
  trust: number;
  fear: number;
  surprise: number;
  sadness: number;
  disgust: number;
  anger: number;
  anticipation: number;
}

interface ConversationMood {
  conversationId: string;
  currentMood: string;
  moodTrajectory: 'improving' | 'stable' | 'declining';
  criticalMoments: CriticalMoment[];
  interventionNeeded: boolean;
  suggestedActions: string[];
}

interface CriticalMoment {
  timestamp: string;
  trigger: string;
  sentimentShift: number;
  context: string;
}

interface CustomerEmotionProfile {
  customerId: string;
  baselineSentiment: number;
  volatility: number;
  triggerPatterns: string[];
  preferredCommunicationStyle: string;
  satisfactionHistory: number[];
  churnRisk: number;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// =============================================================================
// EMOTION LEXICON & PATTERNS
// =============================================================================

const EMOTION_KEYWORDS: Record<string, { emotion: string; weight: number }[]> = {
  // Anger signals
  'unacceptable': [{ emotion: 'anger', weight: 0.9 }],
  'ridiculous': [{ emotion: 'anger', weight: 0.8 }, { emotion: 'disgust', weight: 0.5 }],
  'furious': [{ emotion: 'anger', weight: 1.0 }],
  'outrageous': [{ emotion: 'anger', weight: 0.9 }],
  'terrible': [{ emotion: 'anger', weight: 0.7 }, { emotion: 'disgust', weight: 0.6 }],
  'worst': [{ emotion: 'anger', weight: 0.8 }, { emotion: 'disgust', weight: 0.7 }],
  'incompetent': [{ emotion: 'anger', weight: 0.85 }, { emotion: 'disgust', weight: 0.6 }],
  'scam': [{ emotion: 'anger', weight: 0.95 }, { emotion: 'fear', weight: 0.4 }],
  'rip off': [{ emotion: 'anger', weight: 0.9 }],
  'lawsuit': [{ emotion: 'anger', weight: 1.0 }, { emotion: 'fear', weight: 0.3 }],
  
  // Frustration signals
  'frustrated': [{ emotion: 'anger', weight: 0.6 }, { emotion: 'sadness', weight: 0.4 }],
  'annoyed': [{ emotion: 'anger', weight: 0.5 }],
  'disappointed': [{ emotion: 'sadness', weight: 0.7 }, { emotion: 'anger', weight: 0.3 }],
  'fed up': [{ emotion: 'anger', weight: 0.75 }],
  'wasted': [{ emotion: 'anger', weight: 0.5 }, { emotion: 'sadness', weight: 0.5 }],
  'useless': [{ emotion: 'disgust', weight: 0.7 }, { emotion: 'anger', weight: 0.5 }],
  'impossible': [{ emotion: 'anger', weight: 0.4 }, { emotion: 'fear', weight: 0.3 }],
  
  // Fear/Concern signals
  'worried': [{ emotion: 'fear', weight: 0.7 }],
  'concerned': [{ emotion: 'fear', weight: 0.5 }],
  'afraid': [{ emotion: 'fear', weight: 0.8 }],
  'scared': [{ emotion: 'fear', weight: 0.85 }],
  'anxious': [{ emotion: 'fear', weight: 0.6 }, { emotion: 'anticipation', weight: 0.3 }],
  'nervous': [{ emotion: 'fear', weight: 0.5 }],
  
  // Sadness signals
  'sad': [{ emotion: 'sadness', weight: 0.8 }],
  'devastated': [{ emotion: 'sadness', weight: 1.0 }],
  'heartbroken': [{ emotion: 'sadness', weight: 0.95 }],
  'upset': [{ emotion: 'sadness', weight: 0.6 }, { emotion: 'anger', weight: 0.4 }],
  'depressed': [{ emotion: 'sadness', weight: 0.9 }],
  
  // Positive signals
  'happy': [{ emotion: 'joy', weight: 0.8 }],
  'excellent': [{ emotion: 'joy', weight: 0.85 }, { emotion: 'trust', weight: 0.5 }],
  'amazing': [{ emotion: 'joy', weight: 0.9 }, { emotion: 'surprise', weight: 0.4 }],
  'fantastic': [{ emotion: 'joy', weight: 0.9 }],
  'wonderful': [{ emotion: 'joy', weight: 0.85 }],
  'grateful': [{ emotion: 'joy', weight: 0.7 }, { emotion: 'trust', weight: 0.6 }],
  'thankful': [{ emotion: 'joy', weight: 0.6 }, { emotion: 'trust', weight: 0.7 }],
  'impressed': [{ emotion: 'joy', weight: 0.6 }, { emotion: 'surprise', weight: 0.5 }],
  'recommend': [{ emotion: 'trust', weight: 0.8 }, { emotion: 'joy', weight: 0.5 }],
  'professional': [{ emotion: 'trust', weight: 0.7 }],
  'reliable': [{ emotion: 'trust', weight: 0.8 }],
};

const ESCALATION_PHRASES = [
  'speak to manager', 'supervisor', 'complaint', 'legal', 'lawyer',
  'better business bureau', 'bbb', 'attorney', 'sue', 'refund',
  'cancel', 'never again', 'social media', 'review', 'report',
  'consumer protection', 'authorities', 'unacceptable'
];

const URGENCY_INDICATORS = [
  'asap', 'urgent', 'emergency', 'immediately', 'right now',
  'critical', 'deadline', 'important', 'cannot wait', 'need today'
];

// =============================================================================
// TEXT SENTIMENT ANALYSIS
// =============================================================================

app.post('/api/analyze/text', async (c) => {
  const { text, customerId, conversationId, context } = await c.req.json();
  
  if (!text) {
    return c.json({ error: 'Text is required' }, 400);
  }
  
  // Basic text preprocessing
  const normalizedText = text.toLowerCase().trim();
  const words = normalizedText.split(/\s+/);
  
  // Extract emotions from lexicon
  const emotions = extractEmotions(normalizedText);
  
  // Calculate frustration level
  const frustrationLevel = calculateFrustrationLevel(normalizedText, emotions);
  
  // Calculate urgency
  const urgencyLevel = calculateUrgencyLevel(normalizedText);
  
  // Calculate escalation risk
  const escalationRisk = calculateEscalationRisk(normalizedText, emotions, frustrationLevel);
  
  // Use AI for deeper analysis
  const aiAnalysis = await performAIAnalysis(c.env, text, context);
  
  // Merge lexicon and AI results
  const mergedEmotions = mergeEmotionResults(emotions, aiAnalysis.emotions);
  
  // Calculate overall sentiment score
  const sentimentScore = calculateSentimentScore(mergedEmotions);
  
  // Determine sentiment category
  const overallSentiment = categorizeSentiment(sentimentScore);
  
  // Extract key phrases
  const keyPhrases = await extractKeyPhrases(c.env, text);
  
  // Generate recommendations
  const recommendations = generateRecommendations(
    overallSentiment, frustrationLevel, escalationRisk, mergedEmotions
  );
  
  const analysis: SentimentAnalysis = {
    id: crypto.randomUUID(),
    overallSentiment,
    sentimentScore: Math.round(sentimentScore * 1000) / 1000,
    emotions: mergedEmotions,
    frustrationLevel: Math.round(frustrationLevel),
    urgencyLevel: Math.round(urgencyLevel),
    escalationRisk: Math.round(escalationRisk),
    keyPhrases,
    recommendations,
    confidence: aiAnalysis.confidence
  };
  
  // Store analysis
  await storeSentimentAnalysis(c.env, analysis, customerId, conversationId, text);
  
  // Alert if high risk
  if (escalationRisk > 70 || frustrationLevel > 80) {
    await c.env.ALERTS_QUEUE.send({
      type: 'sentiment_alert',
      customerId,
      conversationId,
      analysis,
      timestamp: Date.now()
    });
  }
  
  return c.json(analysis);
});

function extractEmotions(text: string): EmotionBreakdown {
  const emotions: EmotionBreakdown = {
    joy: 0, trust: 0, fear: 0, surprise: 0,
    sadness: 0, disgust: 0, anger: 0, anticipation: 0
  };
  
  let matchCount = 0;
  
  for (const [keyword, emotionWeights] of Object.entries(EMOTION_KEYWORDS)) {
    if (text.includes(keyword)) {
      matchCount++;
      for (const { emotion, weight } of emotionWeights) {
        emotions[emotion as keyof EmotionBreakdown] += weight;
      }
    }
  }
  
  // Normalize
  if (matchCount > 0) {
    for (const key of Object.keys(emotions) as (keyof EmotionBreakdown)[]) {
      emotions[key] = Math.min(1, emotions[key] / Math.max(1, matchCount * 0.5));
    }
  }
  
  return emotions;
}

function calculateFrustrationLevel(text: string, emotions: EmotionBreakdown): number {
  let frustration = 0;
  
  // Emotion-based frustration
  frustration += emotions.anger * 40;
  frustration += emotions.disgust * 30;
  frustration += emotions.sadness * 20;
  frustration += emotions.fear * 10;
  
  // Pattern-based frustration
  const exclamationCount = (text.match(/!/g) || []).length;
  frustration += Math.min(20, exclamationCount * 5);
  
  const capsRatio = (text.match(/[A-Z]/g) || []).length / Math.max(1, text.length);
  if (capsRatio > 0.3) {
    frustration += 15;
  }
  
  // Repeated punctuation
  if (text.match(/[!?]{2,}/)) {
    frustration += 10;
  }
  
  // Negative intensifiers
  const intensifiers = ['very', 'extremely', 'absolutely', 'totally', 'completely'];
  for (const intensifier of intensifiers) {
    if (text.includes(intensifier)) {
      frustration += 5;
    }
  }
  
  return Math.min(100, frustration);
}

function calculateUrgencyLevel(text: string): number {
  let urgency = 0;
  
  for (const indicator of URGENCY_INDICATORS) {
    if (text.includes(indicator)) {
      urgency += 15;
    }
  }
  
  // Time-related urgency
  if (text.match(/\d+\s*(hour|day|minute)/i)) {
    urgency += 10;
  }
  
  // Deadline mentions
  if (text.match(/(deadline|due|by\s+\w+day)/i)) {
    urgency += 20;
  }
  
  return Math.min(100, urgency);
}

function calculateEscalationRisk(text: string, emotions: EmotionBreakdown, frustration: number): number {
  let risk = 0;
  
  // Check escalation phrases
  for (const phrase of ESCALATION_PHRASES) {
    if (text.includes(phrase)) {
      risk += 15;
    }
  }
  
  // Emotion-based risk
  risk += emotions.anger * 25;
  risk += frustration * 0.3;
  
  // Threat indicators
  if (text.match(/(lawyer|attorney|sue|legal action)/i)) {
    risk += 30;
  }
  
  // Social media threat
  if (text.match(/(twitter|facebook|yelp|google review|social media)/i)) {
    risk += 20;
  }
  
  return Math.min(100, risk);
}

async function performAIAnalysis(env: Env, text: string, context?: string): Promise<{ emotions: Partial<EmotionBreakdown>; confidence: number }> {
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: `You are an emotion analysis expert. Analyze the emotional content of customer messages.

Respond with JSON only:
{
  "emotions": {
    "joy": 0.0-1.0,
    "trust": 0.0-1.0,
    "fear": 0.0-1.0,
    "surprise": 0.0-1.0,
    "sadness": 0.0-1.0,
    "disgust": 0.0-1.0,
    "anger": 0.0-1.0,
    "anticipation": 0.0-1.0
  },
  "confidence": 0.0-1.0,
  "dominant_emotion": "emotion_name"
}`
      },
      {
        role: 'user',
        content: `Analyze this message${context ? ` (Context: ${context})` : ''}: "${text}"`
      }
    ]
  });
  
  try {
    const result = JSON.parse(response.response);
    return {
      emotions: result.emotions,
      confidence: result.confidence || 0.7
    };
  } catch (e) {
    return {
      emotions: {},
      confidence: 0.5
    };
  }
}

function mergeEmotionResults(lexicon: EmotionBreakdown, ai: Partial<EmotionBreakdown>): EmotionBreakdown {
  const merged: EmotionBreakdown = { ...lexicon };
  
  for (const [key, value] of Object.entries(ai)) {
    if (typeof value === 'number') {
      merged[key as keyof EmotionBreakdown] = (lexicon[key as keyof EmotionBreakdown] + value) / 2;
    }
  }
  
  return merged;
}

function calculateSentimentScore(emotions: EmotionBreakdown): number {
  // Positive emotions
  const positive = emotions.joy * 0.4 + emotions.trust * 0.3 + emotions.anticipation * 0.2 + emotions.surprise * 0.1;
  
  // Negative emotions
  const negative = emotions.anger * 0.35 + emotions.fear * 0.2 + emotions.sadness * 0.25 + emotions.disgust * 0.2;
  
  // Score from -1 to 1
  return Math.max(-1, Math.min(1, positive - negative));
}

function categorizeSentiment(score: number): SentimentAnalysis['overallSentiment'] {
  if (score <= -0.6) return 'very_negative';
  if (score <= -0.2) return 'negative';
  if (score <= 0.2) return 'neutral';
  if (score <= 0.6) return 'positive';
  return 'very_positive';
}

async function extractKeyPhrases(env: Env, text: string): Promise<string[]> {
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'Extract 3-5 key phrases from the text that indicate customer sentiment or concerns. Return as JSON array of strings.'
      },
      { role: 'user', content: text }
    ]
  });
  
  try {
    return JSON.parse(response.response);
  } catch (e) {
    return [];
  }
}

function generateRecommendations(
  sentiment: string,
  frustration: number,
  escalationRisk: number,
  emotions: EmotionBreakdown
): string[] {
  const recommendations: string[] = [];
  
  if (escalationRisk > 70) {
    recommendations.push('🚨 ESCALATE: Transfer to senior agent or manager immediately');
    recommendations.push('Acknowledge their concerns explicitly before problem-solving');
  }
  
  if (frustration > 70) {
    recommendations.push('Use empathetic language: "I understand how frustrating this must be"');
    recommendations.push('Offer immediate tangible action to show progress');
  }
  
  if (emotions.anger > 0.6) {
    recommendations.push('Let the customer vent - do not interrupt');
    recommendations.push('Avoid defensive language or making excuses');
    recommendations.push('Focus on solutions, not blame');
  }
  
  if (emotions.fear > 0.5) {
    recommendations.push('Provide reassurance and clear next steps');
    recommendations.push('Be specific about timelines and outcomes');
  }
  
  if (emotions.sadness > 0.5) {
    recommendations.push('Express genuine sympathy');
    recommendations.push('Consider offering a goodwill gesture');
  }
  
  if (sentiment === 'positive' || sentiment === 'very_positive') {
    recommendations.push('Great opportunity for upsell or loyalty program mention');
    recommendations.push('Ask for review or referral');
  }
  
  return recommendations.slice(0, 5);
}

async function storeSentimentAnalysis(
  env: Env,
  analysis: SentimentAnalysis,
  customerId?: string,
  conversationId?: string,
  text?: string
): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO sentiment_analysis (
      id, customer_id, conversation_id, overall_sentiment,
      sentiment_score, frustration_level, urgency_level,
      escalation_risk, emotions_json, key_phrases_json,
      original_text, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    analysis.id,
    customerId || null,
    conversationId || null,
    analysis.overallSentiment,
    analysis.sentimentScore,
    analysis.frustrationLevel,
    analysis.urgencyLevel,
    analysis.escalationRisk,
    JSON.stringify(analysis.emotions),
    JSON.stringify(analysis.keyPhrases),
    text?.substring(0, 1000) || null
  ).run();
}

// =============================================================================
// CONVERSATION MOOD TRACKING
// =============================================================================

app.get('/api/conversation/:id/mood', async (c) => {
  const conversationId = c.req.param('id');
  
  // Get all sentiment analyses for this conversation
  const analyses = await c.env.DB.prepare(`
    SELECT * FROM sentiment_analysis
    WHERE conversation_id = ?
    ORDER BY created_at ASC
  `).bind(conversationId).all();
  
  if (!analyses.results || analyses.results.length === 0) {
    return c.json({ error: 'No analysis data found' }, 404);
  }
  
  // Calculate mood trajectory
  const scores = analyses.results.map((a: any) => a.sentiment_score as number);
  const recentScores = scores.slice(-3);
  const olderScores = scores.slice(0, -3);
  
  let trajectory: 'improving' | 'stable' | 'declining' = 'stable';
  if (recentScores.length > 0 && olderScores.length > 0) {
    const recentAvg = recentScores.reduce((a, b) => a + b, 0) / recentScores.length;
    const olderAvg = olderScores.reduce((a, b) => a + b, 0) / olderScores.length;
    
    if (recentAvg - olderAvg > 0.2) trajectory = 'improving';
    else if (olderAvg - recentAvg > 0.2) trajectory = 'declining';
  }
  
  // Find critical moments
  const criticalMoments: CriticalMoment[] = [];
  for (let i = 1; i < scores.length; i++) {
    const shift = scores[i] - scores[i - 1];
    if (Math.abs(shift) > 0.4) {
      const analysis = analyses.results[i] as any;
      criticalMoments.push({
        timestamp: analysis.created_at,
        trigger: JSON.parse(analysis.key_phrases_json || '[]')[0] || 'Unknown',
        sentimentShift: shift,
        context: analysis.original_text?.substring(0, 100) || ''
      });
    }
  }
  
  // Current mood assessment
  const latest = analyses.results[analyses.results.length - 1] as any;
  const currentMood = latest.overall_sentiment;
  
  // Intervention needed?
  const interventionNeeded = latest.escalation_risk > 60 || 
                             latest.frustration_level > 70 ||
                             trajectory === 'declining';
  
  // Generate suggested actions
  const suggestedActions = generateConversationActions(
    currentMood, trajectory, interventionNeeded, latest
  );
  
  const mood: ConversationMood = {
    conversationId,
    currentMood,
    moodTrajectory: trajectory,
    criticalMoments,
    interventionNeeded,
    suggestedActions
  };
  
  return c.json(mood);
});

function generateConversationActions(
  mood: string,
  trajectory: string,
  interventionNeeded: boolean,
  latest: any
): string[] {
  const actions: string[] = [];
  
  if (interventionNeeded) {
    actions.push('Consider supervisor callback within 30 minutes');
  }
  
  if (trajectory === 'declining') {
    actions.push('Change communication approach immediately');
    actions.push('Offer concrete resolution or compensation');
  }
  
  if (mood === 'very_negative' || mood === 'negative') {
    actions.push('Send personalized follow-up email with resolution summary');
    actions.push('Flag for quality assurance review');
  }
  
  if (trajectory === 'improving') {
    actions.push('Maintain current approach - it\'s working');
    actions.push('Good candidate for satisfaction survey');
  }
  
  return actions;
}

// =============================================================================
// CUSTOMER EMOTION PROFILE
// =============================================================================

app.get('/api/customer/:id/profile', async (c) => {
  const customerId = c.req.param('id');
  
  // Get historical sentiment data
  const history = await c.env.DB.prepare(`
    SELECT 
      sentiment_score,
      frustration_level,
      escalation_risk,
      emotions_json,
      created_at
    FROM sentiment_analysis
    WHERE customer_id = ?
    ORDER BY created_at DESC
    LIMIT 100
  `).bind(customerId).all();
  
  if (!history.results || history.results.length === 0) {
    return c.json({ error: 'No customer data found' }, 404);
  }
  
  // Calculate baseline sentiment
  const scores = history.results.map((h: any) => h.sentiment_score as number);
  const baselineSentiment = scores.reduce((a, b) => a + b, 0) / scores.length;
  
  // Calculate volatility (standard deviation)
  const variance = scores.reduce((sum, s) => sum + Math.pow(s - baselineSentiment, 2), 0) / scores.length;
  const volatility = Math.sqrt(variance);
  
  // Identify trigger patterns
  const triggerPatterns = await identifyTriggerPatterns(c.env, customerId);
  
  // Determine preferred communication style
  const preferredStyle = await determineCommunicationStyle(c.env, customerId, history.results);
  
  // Calculate churn risk
  const recentScores = scores.slice(0, 10);
  const recentAvg = recentScores.reduce((a, b) => a + b, 0) / recentScores.length;
  const churnRisk = Math.max(0, Math.min(100, (baselineSentiment - recentAvg) * 50 + volatility * 30));
  
  const profile: CustomerEmotionProfile = {
    customerId,
    baselineSentiment: Math.round(baselineSentiment * 1000) / 1000,
    volatility: Math.round(volatility * 1000) / 1000,
    triggerPatterns,
    preferredCommunicationStyle: preferredStyle,
    satisfactionHistory: scores.slice(0, 20).map(s => Math.round((s + 1) * 50)), // Convert to 0-100
    churnRisk: Math.round(churnRisk)
  };
  
  return c.json(profile);
});

async function identifyTriggerPatterns(env: Env, customerId: string): Promise<string[]> {
  const negativeAnalyses = await env.DB.prepare(`
    SELECT key_phrases_json FROM sentiment_analysis
    WHERE customer_id = ? AND sentiment_score < -0.3
    ORDER BY created_at DESC
    LIMIT 20
  `).bind(customerId).all();
  
  const allPhrases: string[] = [];
  for (const analysis of negativeAnalyses.results || []) {
    const phrases = JSON.parse((analysis as any).key_phrases_json || '[]');
    allPhrases.push(...phrases);
  }
  
  // Count frequency
  const phraseCount = new Map<string, number>();
  for (const phrase of allPhrases) {
    phraseCount.set(phrase, (phraseCount.get(phrase) || 0) + 1);
  }
  
  // Return most common triggers
  return Array.from(phraseCount.entries())
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([phrase]) => phrase);
}

async function determineCommunicationStyle(env: Env, customerId: string, history: any[]): Promise<string> {
  // Analyze what worked best
  const improvingConversations = history.filter((h, i, arr) => {
    if (i === 0) return false;
    return (h.sentiment_score as number) > (arr[i - 1].sentiment_score as number) + 0.3;
  });
  
  if (improvingConversations.length === 0) {
    return 'Standard professional tone';
  }
  
  // Use AI to determine style preferences
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'Based on customer interaction history, recommend the best communication style. Respond with a brief 1-2 sentence recommendation.'
      },
      {
        role: 'user',
        content: `Customer baseline sentiment: ${history[0].sentiment_score}. 
        High volatility: ${history.length > 10 ? 'Yes' : 'No'}.
        Most common emotion: ${getMostCommonEmotion(history)}`
      }
    ]
  });
  
  return response.response || 'Empathetic and solution-focused';
}

function getMostCommonEmotion(history: any[]): string {
  const emotionCounts: Record<string, number> = {};
  
  for (const h of history) {
    const emotions = JSON.parse(h.emotions_json || '{}');
    for (const [emotion, value] of Object.entries(emotions)) {
      if (typeof value === 'number' && value > 0.5) {
        emotionCounts[emotion] = (emotionCounts[emotion] || 0) + 1;
      }
    }
  }
  
  return Object.entries(emotionCounts)
    .sort((a, b) => b[1] - a[1])[0]?.[0] || 'neutral';
}

// =============================================================================
// VOICE SENTIMENT ANALYSIS
// =============================================================================

app.post('/api/analyze/voice', async (c) => {
  const { audioFeatures, transcript, customerId, conversationId } = await c.req.json();
  
  // Analyze voice features
  const voiceSentiment = analyzeVoiceFeatures(audioFeatures);
  
  // Analyze transcript if available
  let textSentiment: SentimentAnalysis | null = null;
  if (transcript) {
    const textResponse = await app.request('/api/analyze/text', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: transcript, customerId, conversationId })
    });
    textSentiment = await textResponse.json() as SentimentAnalysis;
  }
  
  // Combine voice and text sentiment
  const combinedSentiment = combineSentimentSources(voiceSentiment, textSentiment);
  
  return c.json({
    voiceAnalysis: voiceSentiment,
    textAnalysis: textSentiment,
    combined: combinedSentiment
  });
});

function analyzeVoiceFeatures(features: any): { sentiment: number; stress: number; confidence: number } {
  if (!features) {
    return { sentiment: 0, stress: 50, confidence: 0.3 };
  }
  
  let sentiment = 0;
  let stress = 50;
  
  // Pitch analysis
  if (features.pitchVariance) {
    // High pitch variance often indicates emotion
    stress += features.pitchVariance > 50 ? 20 : -10;
  }
  
  // Speaking rate
  if (features.speakingRate) {
    // Fast speaking can indicate frustration or urgency
    if (features.speakingRate > 180) stress += 15;
    if (features.speakingRate < 100) stress -= 10;
  }
  
  // Volume
  if (features.volumeLevel) {
    if (features.volumeLevel > 0.8) stress += 20; // Loud = stressed
  }
  
  // Pauses
  if (features.pauseFrequency) {
    // Many pauses might indicate uncertainty or thoughtfulness
    stress += features.pauseFrequency > 0.3 ? 10 : 0;
  }
  
  // Convert stress to sentiment (inverse relationship)
  sentiment = (100 - stress) / 100 * 2 - 1; // Map to -1 to 1
  
  return {
    sentiment: Math.round(sentiment * 1000) / 1000,
    stress: Math.round(stress),
    confidence: 0.6
  };
}

function combineSentimentSources(voice: any, text: SentimentAnalysis | null): any {
  if (!text) {
    return {
      overallSentiment: voice.sentiment > 0 ? 'positive' : voice.sentiment < 0 ? 'negative' : 'neutral',
      sentimentScore: voice.sentiment,
      stressLevel: voice.stress,
      confidence: voice.confidence
    };
  }
  
  // Weight text more heavily as it's more reliable
  const combinedScore = text.sentimentScore * 0.7 + voice.sentiment * 0.3;
  const combinedStress = (voice.stress + text.frustrationLevel) / 2;
  
  return {
    overallSentiment: text.overallSentiment,
    sentimentScore: Math.round(combinedScore * 1000) / 1000,
    stressLevel: Math.round(combinedStress),
    frustrationLevel: text.frustrationLevel,
    escalationRisk: text.escalationRisk,
    confidence: (text.confidence + voice.confidence) / 2
  };
}

// =============================================================================
// REAL-TIME MONITORING DASHBOARD
// =============================================================================

app.get('/api/dashboard/live', async (c) => {
  const since = c.req.query('since') || new Date(Date.now() - 3600000).toISOString();
  
  // Get recent sentiment trends
  const trends = await c.env.DB.prepare(`
    SELECT 
      strftime('%Y-%m-%d %H:00', created_at) as hour,
      AVG(sentiment_score) as avg_sentiment,
      AVG(frustration_level) as avg_frustration,
      AVG(escalation_risk) as avg_escalation,
      COUNT(*) as interaction_count
    FROM sentiment_analysis
    WHERE created_at > ?
    GROUP BY hour
    ORDER BY hour DESC
    LIMIT 24
  `).bind(since).all();
  
  // Get active escalations
  const escalations = await c.env.DB.prepare(`
    SELECT * FROM sentiment_analysis
    WHERE escalation_risk > 70
      AND created_at > datetime('now', '-1 hour')
    ORDER BY escalation_risk DESC
    LIMIT 10
  `).all();
  
  // Get sentiment distribution
  const distribution = await c.env.DB.prepare(`
    SELECT 
      overall_sentiment,
      COUNT(*) as count
    FROM sentiment_analysis
    WHERE created_at > ?
    GROUP BY overall_sentiment
  `).bind(since).all();
  
  return c.json({
    trends: trends.results,
    activeEscalations: escalations.results,
    distribution: distribution.results,
    summary: {
      avgSentiment: trends.results?.[0]?.avg_sentiment || 0,
      totalInteractions: trends.results?.reduce((sum: number, t: any) => sum + t.interaction_count, 0) || 0,
      escalationRate: escalations.results?.length || 0
    }
  });
});

// =============================================================================
// AGENT PERFORMANCE SENTIMENT
// =============================================================================

app.get('/api/agent/:id/sentiment-performance', async (c) => {
  const agentId = c.req.param('id');
  const days = parseInt(c.req.query('days') || '30');
  
  const performance = await c.env.DB.prepare(`
    SELECT 
      AVG(sa.sentiment_score) as avg_final_sentiment,
      AVG(sa.frustration_level) as avg_frustration_handled,
      SUM(CASE WHEN sa.escalation_risk > 70 THEN 1 ELSE 0 END) as escalations,
      COUNT(DISTINCT sa.conversation_id) as total_conversations,
      AVG(CASE 
        WHEN sa2.sentiment_score IS NOT NULL 
        THEN sa.sentiment_score - sa2.sentiment_score 
        ELSE 0 
      END) as avg_sentiment_improvement
    FROM sentiment_analysis sa
    LEFT JOIN (
      SELECT conversation_id, sentiment_score, 
             ROW_NUMBER() OVER (PARTITION BY conversation_id ORDER BY created_at ASC) as rn
      FROM sentiment_analysis
    ) sa2 ON sa.conversation_id = sa2.conversation_id AND sa2.rn = 1
    WHERE sa.agent_id = ?
      AND sa.created_at > datetime('now', '-${days} days')
  `).bind(agentId).first();
  
  return c.json({
    agentId,
    period: `${days} days`,
    metrics: {
      avgFinalSentiment: Math.round((performance?.avg_final_sentiment as number || 0) * 100) / 100,
      avgSentimentImprovement: Math.round((performance?.avg_sentiment_improvement as number || 0) * 100) / 100,
      escalationRate: Math.round(((performance?.escalations as number || 0) / Math.max(1, performance?.total_conversations as number)) * 100),
      totalConversations: performance?.total_conversations || 0
    }
  });
});

export default app;
