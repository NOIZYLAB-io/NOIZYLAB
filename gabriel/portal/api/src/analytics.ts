/**
 * Real-time Analytics Dashboard API
 * 
 * Tracks scan volume, revenue, user engagement
 * Powers the admin dashboard
 */

interface DailyMetrics {
  date: string;
  scans: number;
  revenue: number;
  newUsers: number;
  activeUsers: number;
  avgScanTime: number;
  issuesDetected: number;
  repairsCompleted: number;
}

interface RevenueBreakdown {
  goldenAudit: number;
  legacyKit: number;
  proSubscription: number;
  total: number;
}

/**
 * Record a scan event
 */
export async function recordScan(
  scanData: {
    scanId: string;
    userId: string;
    boardType: string;
    duration: number;
    issuesFound: number;
    confidence: number;
  },
  env: Env
): Promise<void> {
  const today = new Date().toISOString().slice(0, 10);
  const hour = new Date().getHours();
  
  // Update daily metrics
  const dailyKey = `metrics:daily:${today}`;
  let daily = await env.KV_ANALYTICS.get(dailyKey);
  const metrics: DailyMetrics = daily ? JSON.parse(daily) : {
    date: today,
    scans: 0,
    revenue: 0,
    newUsers: 0,
    activeUsers: 0,
    avgScanTime: 0,
    issuesDetected: 0,
    repairsCompleted: 0
  };
  
  metrics.scans++;
  metrics.issuesDetected += scanData.issuesFound;
  metrics.avgScanTime = (metrics.avgScanTime * (metrics.scans - 1) + scanData.duration) / metrics.scans;
  
  await env.KV_ANALYTICS.put(dailyKey, JSON.stringify(metrics), {
    expirationTtl: 90 * 24 * 60 * 60 // 90 days
  });
  
  // Update hourly heatmap
  const hourlyKey = `metrics:hourly:${today}:${hour}`;
  let hourlyCount = await env.KV_ANALYTICS.get(hourlyKey);
  await env.KV_ANALYTICS.put(hourlyKey, String((parseInt(hourlyCount || '0') + 1)), {
    expirationTtl: 7 * 24 * 60 * 60 // 7 days
  });
  
  // Update board type distribution
  const boardKey = `metrics:boards:${today}`;
  let boards = await env.KV_ANALYTICS.get(boardKey);
  const boardDist = boards ? JSON.parse(boards) : {};
  boardDist[scanData.boardType] = (boardDist[scanData.boardType] || 0) + 1;
  await env.KV_ANALYTICS.put(boardKey, JSON.stringify(boardDist));
  
  // Track active user
  await env.KV_ANALYTICS.put(`active:${today}:${scanData.userId}`, '1', {
    expirationTtl: 24 * 60 * 60
  });
}

/**
 * Record a payment event
 */
export async function recordPayment(
  paymentData: {
    userId: string;
    productId: string;
    amount: number;
    currency: string;
  },
  env: Env
): Promise<void> {
  const today = new Date().toISOString().slice(0, 10);
  const month = today.slice(0, 7);
  
  // Update daily revenue
  const dailyKey = `metrics:daily:${today}`;
  let daily = await env.KV_ANALYTICS.get(dailyKey);
  const metrics: DailyMetrics = daily ? JSON.parse(daily) : {
    date: today,
    scans: 0,
    revenue: 0,
    newUsers: 0,
    activeUsers: 0,
    avgScanTime: 0,
    issuesDetected: 0,
    repairsCompleted: 0
  };
  
  metrics.revenue += paymentData.amount;
  await env.KV_ANALYTICS.put(dailyKey, JSON.stringify(metrics));
  
  // Update monthly revenue breakdown
  const monthlyKey = `revenue:${month}`;
  let monthly = await env.KV_ANALYTICS.get(monthlyKey);
  const breakdown: RevenueBreakdown = monthly ? JSON.parse(monthly) : {
    goldenAudit: 0,
    legacyKit: 0,
    proSubscription: 0,
    total: 0
  };
  
  switch (paymentData.productId) {
    case 'golden_audit':
      breakdown.goldenAudit += paymentData.amount;
      break;
    case 'legacy_kit':
      breakdown.legacyKit += paymentData.amount;
      break;
    case 'pro_monthly':
    case 'pro_yearly':
      breakdown.proSubscription += paymentData.amount;
      break;
  }
  breakdown.total += paymentData.amount;
  
  await env.KV_ANALYTICS.put(monthlyKey, JSON.stringify(breakdown));
  
  // Record transaction for audit trail
  const txKey = `tx:${Date.now()}:${paymentData.userId}`;
  await env.KV_ANALYTICS.put(txKey, JSON.stringify({
    ...paymentData,
    timestamp: new Date().toISOString()
  }), {
    expirationTtl: 365 * 24 * 60 * 60 // 1 year
  });
}

/**
 * Get dashboard metrics
 */
export async function getDashboardMetrics(
  range: 'today' | '7d' | '30d' | '90d',
  env: Env
): Promise<{
  summary: {
    totalScans: number;
    totalRevenue: number;
    avgConfidence: number;
    activeUsers: number;
  };
  daily: DailyMetrics[];
  revenueBreakdown: RevenueBreakdown;
  topBoards: { name: string; count: number }[];
  hourlyHeatmap: number[];
}> {
  const today = new Date();
  const days = range === 'today' ? 1 : range === '7d' ? 7 : range === '30d' ? 30 : 90;
  
  const dailyMetrics: DailyMetrics[] = [];
  let totalScans = 0;
  let totalRevenue = 0;
  const allBoards: Record<string, number> = {};
  
  // Fetch daily metrics for range
  for (let i = 0; i < days; i++) {
    const date = new Date(today);
    date.setDate(date.getDate() - i);
    const dateStr = date.toISOString().slice(0, 10);
    
    const dailyKey = `metrics:daily:${dateStr}`;
    const daily = await env.KV_ANALYTICS.get(dailyKey);
    
    if (daily) {
      const metrics: DailyMetrics = JSON.parse(daily);
      dailyMetrics.push(metrics);
      totalScans += metrics.scans;
      totalRevenue += metrics.revenue;
    }
    
    // Aggregate board types
    const boardKey = `metrics:boards:${dateStr}`;
    const boards = await env.KV_ANALYTICS.get(boardKey);
    if (boards) {
      const boardDist = JSON.parse(boards);
      for (const [board, count] of Object.entries(boardDist)) {
        allBoards[board] = (allBoards[board] || 0) + (count as number);
      }
    }
  }
  
  // Get hourly heatmap for today
  const todayStr = today.toISOString().slice(0, 10);
  const hourlyHeatmap: number[] = [];
  for (let h = 0; h < 24; h++) {
    const hourlyKey = `metrics:hourly:${todayStr}:${h}`;
    const count = await env.KV_ANALYTICS.get(hourlyKey);
    hourlyHeatmap.push(parseInt(count || '0'));
  }
  
  // Get current month revenue breakdown
  const month = todayStr.slice(0, 7);
  const monthlyKey = `revenue:${month}`;
  const monthly = await env.KV_ANALYTICS.get(monthlyKey);
  const revenueBreakdown: RevenueBreakdown = monthly ? JSON.parse(monthly) : {
    goldenAudit: 0,
    legacyKit: 0,
    proSubscription: 0,
    total: 0
  };
  
  // Sort boards by count
  const topBoards = Object.entries(allBoards)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([name, count]) => ({ name, count }));
  
  // Count active users today
  const activeList = await env.KV_ANALYTICS.list({ prefix: `active:${todayStr}:` });
  const activeUsers = activeList.keys.length;
  
  return {
    summary: {
      totalScans,
      totalRevenue,
      avgConfidence: dailyMetrics.length > 0 
        ? dailyMetrics.reduce((sum, m) => sum + (m.avgScanTime || 0), 0) / dailyMetrics.length 
        : 0,
      activeUsers
    },
    daily: dailyMetrics.reverse(),
    revenueBreakdown,
    topBoards,
    hourlyHeatmap
  };
}

/**
 * Get real-time stats for live dashboard
 */
export async function getRealtimeStats(env: Env): Promise<{
  scansLastHour: number;
  scansLastMinute: number;
  activeNow: number;
  revenueToday: number;
}> {
  const now = new Date();
  const today = now.toISOString().slice(0, 10);
  const hour = now.getHours();
  
  // Scans this hour
  const hourlyKey = `metrics:hourly:${today}:${hour}`;
  const scansLastHour = parseInt(await env.KV_ANALYTICS.get(hourlyKey) || '0');
  
  // Today's revenue
  const dailyKey = `metrics:daily:${today}`;
  const daily = await env.KV_ANALYTICS.get(dailyKey);
  const revenueToday = daily ? JSON.parse(daily).revenue : 0;
  
  // Active users (approximate from today's active list)
  const activeList = await env.KV_ANALYTICS.list({ prefix: `active:${today}:` });
  
  return {
    scansLastHour,
    scansLastMinute: Math.floor(scansLastHour / 60), // Rough estimate
    activeNow: Math.min(activeList.keys.length, 100), // Cap display
    revenueToday
  };
}

interface Env {
  KV_ANALYTICS: KVNamespace;
}

export type { DailyMetrics, RevenueBreakdown };
