/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * DAZEFLOW - MC96ECOUNIVERSE Truth Capture System
 * Daily reflection, journaling, gratitude tracking, and life documentation
 * "Every day, capture a truth. Every truth, builds a life."
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════════════

interface Env {
  AI: any;
  KV: KVNamespace;
  DB: D1Database;
}

interface DazeEntry {
  id: string;
  date: string;
  truth: string;
  gratitude: string[];
  mood: string;
  energy: number; // 1-10
  wins: string[];
  challenges: string[];
  intentions: string[];
  reflections?: string;
  aiInsight?: string;
  tags: string[];
  createdAt: string;
  updatedAt?: string;
}

interface DazeStats {
  totalEntries: number;
  currentStreak: number;
  longestStreak: number;
  averageMood: number;
  topTags: { tag: string; count: number }[];
  monthlyEntries: number;
}

// ═══════════════════════════════════════════════════════════════════════════════
// CONSTANTS
// ═══════════════════════════════════════════════════════════════════════════════

const MOODS = [
  { id: 'radiant', emoji: '✨', description: 'Exceptional, peak state' },
  { id: 'joyful', emoji: '😊', description: 'Happy and content' },
  { id: 'peaceful', emoji: '😌', description: 'Calm and balanced' },
  { id: 'focused', emoji: '🎯', description: 'In the zone' },
  { id: 'thoughtful', emoji: '🤔', description: 'Reflective' },
  { id: 'neutral', emoji: '😐', description: 'Steady, even' },
  { id: 'tired', emoji: '😴', description: 'Low energy' },
  { id: 'anxious', emoji: '😰', description: 'Worried or stressed' },
  { id: 'sad', emoji: '😢', description: 'Down or blue' },
  { id: 'frustrated', emoji: '😤', description: 'Blocked or irritated' }
];

const PROMPTS = [
  "What's one truth you learned today?",
  "What are you grateful for right now?",
  "What small win can you celebrate?",
  "What challenge are you facing?",
  "What intention do you set for tomorrow?",
  "How did you grow today?",
  "What made you smile?",
  "What would you do differently?",
  "Who positively impacted your day?",
  "What's one thing you're proud of?"
];

// ═══════════════════════════════════════════════════════════════════════════════
// APP
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// UTILITY FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════════

function generateId(): string {
  return `daze_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;
}

function getToday(): string {
  return new Date().toISOString().split('T')[0];
}

function getDayOfYear(date: string): number {
  const d = new Date(date);
  const start = new Date(d.getFullYear(), 0, 0);
  const diff = d.getTime() - start.getTime();
  return Math.floor(diff / (1000 * 60 * 60 * 24));
}

async function generateAIInsight(entry: DazeEntry, env: Env): Promise<string | null> {
  if (!env.AI) return null;

  try {
    const result = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{
        role: 'system',
        content: 'You are a wise, compassionate life coach. Provide brief, insightful observations based on journal entries. Keep responses under 50 words. Be encouraging but authentic.'
      }, {
        role: 'user',
        content: `Based on this journal entry, provide a brief insight:

Truth: ${entry.truth}
Mood: ${entry.mood}
Energy: ${entry.energy}/10
Gratitude: ${entry.gratitude.join(', ')}
Wins: ${entry.wins.join(', ')}
Challenges: ${entry.challenges.join(', ')}
Intentions: ${entry.intentions.join(', ')}`
      }]
    });
    return result.response;
  } catch {
    return null;
  }
}

// ═══════════════════════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/', (c) => c.json({
  service: 'DAZEFLOW',
  version: '1.0.0',
  status: 'OPERATIONAL',
  philosophy: 'Every day, capture a truth. Every truth, builds a life.',
  features: [
    'daily-truth-capture',
    'gratitude-tracking',
    'mood-monitoring',
    'streak-tracking',
    'ai-insights',
    'reflection-prompts'
  ],
  moods: MOODS.length,
  timestamp: new Date().toISOString()
}));

app.get('/health', (c) => c.json({ ok: true, service: 'dazeflow' }));

// ═══════════════════════════════════════════════════════════════════════════════
// DAILY ENTRY CRUD
// ═══════════════════════════════════════════════════════════════════════════════

// Get today's entry (or create prompt)
app.get('/today', async (c) => {
  try {
    const today = getToday();

    if (c.env.KV) {
      const existing = await c.env.KV.get(`daze:${today}`, 'json') as DazeEntry | null;
      
      if (existing) {
        return c.json({
          success: true,
          exists: true,
          entry: existing
        });
      }
    }

    // No entry yet - provide prompts
    const randomPrompts = PROMPTS.sort(() => Math.random() - 0.5).slice(0, 3);
    const randomMood = MOODS[Math.floor(Math.random() * MOODS.length)];

    return c.json({
      success: true,
      exists: false,
      date: today,
      prompts: randomPrompts,
      suggestedMood: randomMood,
      allMoods: MOODS
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Create or update today's entry
app.post('/today', async (c) => {
  try {
    const today = getToday();
    const body = await c.req.json();

    if (!body.truth) {
      return c.json({ success: false, error: 'Truth is required' }, 400);
    }

    const entry: DazeEntry = {
      id: generateId(),
      date: today,
      truth: body.truth,
      gratitude: body.gratitude || [],
      mood: body.mood || 'neutral',
      energy: Math.min(10, Math.max(1, body.energy || 5)),
      wins: body.wins || [],
      challenges: body.challenges || [],
      intentions: body.intentions || [],
      reflections: body.reflections,
      tags: body.tags || [],
      createdAt: new Date().toISOString()
    };

    // Generate AI insight
    entry.aiInsight = await generateAIInsight(entry, c.env);

    // Check for existing entry
    if (c.env.KV) {
      const existing = await c.env.KV.get(`daze:${today}`, 'json') as DazeEntry | null;
      if (existing) {
        entry.id = existing.id;
        entry.createdAt = existing.createdAt;
        entry.updatedAt = new Date().toISOString();
      }

      await c.env.KV.put(`daze:${today}`, JSON.stringify(entry));

      // Update index
      const index = await c.env.KV.get('daze:index', 'json') as string[] || [];
      if (!index.includes(today)) {
        index.push(today);
        await c.env.KV.put('daze:index', JSON.stringify(index));
      }
    }

    return c.json({
      success: true,
      entry,
      message: entry.updatedAt ? 'Entry updated' : 'Entry created'
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Get entry by date
app.get('/entry/:date', async (c) => {
  try {
    const date = c.req.param('date');

    if (!c.env.KV) {
      return c.json({ success: false, error: 'Storage not configured' }, 500);
    }

    const entry = await c.env.KV.get(`daze:${date}`, 'json') as DazeEntry | null;

    if (!entry) {
      return c.json({ success: false, error: 'Entry not found' }, 404);
    }

    return c.json({ success: true, entry });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// List entries (paginated)
app.get('/entries', async (c) => {
  try {
    const limit = parseInt(c.req.query('limit') || '30');
    const offset = parseInt(c.req.query('offset') || '0');

    if (!c.env.KV) {
      return c.json({ success: false, error: 'Storage not configured' }, 500);
    }

    const index = await c.env.KV.get('daze:index', 'json') as string[] || [];
    const sortedDates = index.sort().reverse();
    const paginatedDates = sortedDates.slice(offset, offset + limit);

    const entries: DazeEntry[] = [];
    for (const date of paginatedDates) {
      const entry = await c.env.KV.get(`daze:${date}`, 'json') as DazeEntry;
      if (entry) entries.push(entry);
    }

    return c.json({
      success: true,
      total: index.length,
      offset,
      limit,
      entries
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// STATS & ANALYTICS
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/stats', async (c) => {
  try {
    if (!c.env.KV) {
      return c.json({ success: false, error: 'Storage not configured' }, 500);
    }

    const index = await c.env.KV.get('daze:index', 'json') as string[] || [];
    
    if (index.length === 0) {
      return c.json({
        success: true,
        stats: {
          totalEntries: 0,
          currentStreak: 0,
          longestStreak: 0,
          averageMood: 0,
          topTags: [],
          monthlyEntries: 0
        }
      });
    }

    // Calculate streaks
    const sortedDates = index.sort().reverse();
    let currentStreak = 0;
    let longestStreak = 0;
    let tempStreak = 0;
    let lastDayOfYear = getDayOfYear(getToday()) + 1;

    for (const date of sortedDates) {
      const dayOfYear = getDayOfYear(date);
      if (lastDayOfYear - dayOfYear === 1) {
        tempStreak++;
      } else if (lastDayOfYear - dayOfYear > 1) {
        longestStreak = Math.max(longestStreak, tempStreak);
        tempStreak = 1;
      }
      lastDayOfYear = dayOfYear;
    }
    longestStreak = Math.max(longestStreak, tempStreak);
    currentStreak = tempStreak;

    // Calculate mood average and tags
    let moodSum = 0;
    let moodCount = 0;
    const tagCounts: Record<string, number> = {};
    const thisMonth = getToday().substring(0, 7);
    let monthlyEntries = 0;

    for (const date of sortedDates.slice(0, 100)) { // Last 100 entries
      const entry = await c.env.KV.get(`daze:${date}`, 'json') as DazeEntry;
      if (entry) {
        moodSum += entry.energy;
        moodCount++;
        
        for (const tag of entry.tags) {
          tagCounts[tag] = (tagCounts[tag] || 0) + 1;
        }

        if (date.startsWith(thisMonth)) {
          monthlyEntries++;
        }
      }
    }

    const topTags = Object.entries(tagCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([tag, count]) => ({ tag, count }));

    const stats: DazeStats = {
      totalEntries: index.length,
      currentStreak,
      longestStreak,
      averageMood: moodCount > 0 ? moodSum / moodCount : 0,
      topTags,
      monthlyEntries
    };

    return c.json({ success: true, stats });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// PROMPTS & INSPIRATION
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/prompts', (c) => c.json({
  success: true,
  prompts: PROMPTS,
  moods: MOODS
}));

app.get('/prompts/random', (c) => {
  const count = parseInt(c.req.query('count') || '3');
  const randomPrompts = PROMPTS.sort(() => Math.random() - 0.5).slice(0, count);
  
  return c.json({
    success: true,
    prompts: randomPrompts
  });
});

app.get('/moods', (c) => c.json({
  success: true,
  moods: MOODS
}));

// AI-generated reflection prompt
app.get('/prompts/ai', async (c) => {
  try {
    if (!c.env.AI) {
      return c.json({ 
        success: true, 
        prompt: PROMPTS[Math.floor(Math.random() * PROMPTS.length)],
        source: 'default'
      });
    }

    const result = await c.env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{
        role: 'system',
        content: 'Generate a single thoughtful journaling prompt for daily reflection. Keep it under 20 words. Be profound but accessible.'
      }, {
        role: 'user',
        content: `Generate a unique journaling prompt for ${new Date().toLocaleDateString('en-US', { weekday: 'long' })}.`
      }]
    });

    return c.json({
      success: true,
      prompt: result.response,
      source: 'ai'
    });
  } catch (error: any) {
    return c.json({ 
      success: true, 
      prompt: PROMPTS[Math.floor(Math.random() * PROMPTS.length)],
      source: 'fallback'
    });
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// SEARCH & FILTER
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/search', async (c) => {
  try {
    const query = c.req.query('q');
    const tag = c.req.query('tag');
    const mood = c.req.query('mood');
    const limit = parseInt(c.req.query('limit') || '20');

    if (!c.env.KV) {
      return c.json({ success: false, error: 'Storage not configured' }, 500);
    }

    const index = await c.env.KV.get('daze:index', 'json') as string[] || [];
    const results: DazeEntry[] = [];

    for (const date of index.sort().reverse()) {
      if (results.length >= limit) break;

      const entry = await c.env.KV.get(`daze:${date}`, 'json') as DazeEntry;
      if (!entry) continue;

      let matches = true;

      if (query) {
        const searchText = [
          entry.truth,
          entry.reflections,
          ...entry.gratitude,
          ...entry.wins,
          ...entry.challenges,
          ...entry.intentions
        ].join(' ').toLowerCase();
        
        if (!searchText.includes(query.toLowerCase())) {
          matches = false;
        }
      }

      if (tag && !entry.tags.includes(tag)) {
        matches = false;
      }

      if (mood && entry.mood !== mood) {
        matches = false;
      }

      if (matches) {
        results.push(entry);
      }
    }

    return c.json({
      success: true,
      query,
      tag,
      mood,
      count: results.length,
      entries: results
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// WEEKLY/MONTHLY REVIEW
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/review/:period', async (c) => {
  try {
    const period = c.req.param('period'); // 'week' or 'month'
    
    if (!c.env.KV || !c.env.AI) {
      return c.json({ success: false, error: 'Required services not configured' }, 500);
    }

    const today = new Date();
    let startDate: Date;

    if (period === 'week') {
      startDate = new Date(today);
      startDate.setDate(today.getDate() - 7);
    } else if (period === 'month') {
      startDate = new Date(today);
      startDate.setMonth(today.getMonth() - 1);
    } else {
      return c.json({ success: false, error: 'Invalid period. Use "week" or "month"' }, 400);
    }

    const index = await c.env.KV.get('daze:index', 'json') as string[] || [];
    const entries: DazeEntry[] = [];

    for (const date of index) {
      const entryDate = new Date(date);
      if (entryDate >= startDate && entryDate <= today) {
        const entry = await c.env.KV.get(`daze:${date}`, 'json') as DazeEntry;
        if (entry) entries.push(entry);
      }
    }

    if (entries.length === 0) {
      return c.json({
        success: true,
        period,
        message: `No entries found for the past ${period}`,
        entries: []
      });
    }

    // Generate AI review
    const entrySummary = entries.map(e => 
      `${e.date}: Truth: "${e.truth}" | Mood: ${e.mood} | Energy: ${e.energy}/10`
    ).join('\n');

    const aiReview = await c.env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{
        role: 'system',
        content: 'You are a thoughtful life coach analyzing journal entries. Provide insights about patterns, growth, and suggestions. Keep it encouraging and actionable. Under 150 words.'
      }, {
        role: 'user',
        content: `Review these ${period}ly journal entries and provide insights:\n\n${entrySummary}`
      }]
    });

    return c.json({
      success: true,
      period,
      startDate: startDate.toISOString().split('T')[0],
      endDate: today.toISOString().split('T')[0],
      entryCount: entries.length,
      averageEnergy: entries.reduce((sum, e) => sum + e.energy, 0) / entries.length,
      review: aiReview.response,
      entries
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORT
// ═══════════════════════════════════════════════════════════════════════════════

export default app;
