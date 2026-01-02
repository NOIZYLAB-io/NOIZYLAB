/**
 * ████ NOIZYLAB ANALYTICS WORKER ████
 * 
 * FULL BUSINESS INTELLIGENCE ENGINE
 * - Real-time KPI dashboards
 * - Technician performance metrics
 * - Revenue & profitability analysis
 * - Customer lifetime value tracking
 * - Predictive analytics with AI
 * - Exportable reports (PDF, CSV)
 */

export interface Env {
  DB: D1Database;
  ANALYTICS_KV: KVNamespace;
  AI: Ai;
  BRAIN: Fetcher;
}

interface KPISnapshot {
  period: string;
  tickets_created: number;
  tickets_closed: number;
  avg_resolution_time_hours: number;
  first_response_time_minutes: number;
  customer_satisfaction: number;
  revenue: number;
  parts_cost: number;
  gross_margin: number;
  technicians_active: number;
}

interface TechnicianMetrics {
  id: string;
  name: string;
  tickets_completed: number;
  avg_completion_time: number;
  customer_rating: number;
  revenue_generated: number;
  specializations: string[];
  efficiency_score: number;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        },
      });
    }

    try {
      // === REAL-TIME DASHBOARD ===
      if (path === '/dashboard' && request.method === 'GET') {
        return this.getDashboard(env);
      }

      if (path === '/dashboard/live' && request.method === 'GET') {
        return this.getLiveMetrics(env);
      }

      // === KPI REPORTS ===
      if (path === '/kpi/daily' && request.method === 'GET') {
        return this.getDailyKPIs(url, env);
      }

      if (path === '/kpi/weekly' && request.method === 'GET') {
        return this.getWeeklyKPIs(url, env);
      }

      if (path === '/kpi/monthly' && request.method === 'GET') {
        return this.getMonthlyKPIs(url, env);
      }

      if (path === '/kpi/trends' && request.method === 'GET') {
        return this.getKPITrends(url, env);
      }

      // === TECHNICIAN ANALYTICS ===
      if (path === '/technicians' && request.method === 'GET') {
        return this.getTechnicianMetrics(url, env);
      }

      if (path.match(/^\/technicians\/[^/]+$/) && request.method === 'GET') {
        const techId = path.split('/')[2];
        return this.getTechnicianDetail(techId, url, env);
      }

      if (path === '/technicians/leaderboard' && request.method === 'GET') {
        return this.getTechnicianLeaderboard(url, env);
      }

      // === REVENUE ANALYTICS ===
      if (path === '/revenue/overview' && request.method === 'GET') {
        return this.getRevenueOverview(url, env);
      }

      if (path === '/revenue/by-category' && request.method === 'GET') {
        return this.getRevenueByCategory(url, env);
      }

      if (path === '/revenue/by-device' && request.method === 'GET') {
        return this.getRevenueByDevice(url, env);
      }

      if (path === '/revenue/forecast' && request.method === 'GET') {
        return this.getRevenueForecast(env);
      }

      // === CUSTOMER ANALYTICS ===
      if (path === '/customers/ltv' && request.method === 'GET') {
        return this.getCustomerLTV(env);
      }

      if (path === '/customers/segments' && request.method === 'GET') {
        return this.getCustomerSegments(env);
      }

      if (path === '/customers/churn-risk' && request.method === 'GET') {
        return this.getChurnRisk(env);
      }

      if (path === '/customers/acquisition' && request.method === 'GET') {
        return this.getAcquisitionMetrics(url, env);
      }

      // === OPERATIONAL ANALYTICS ===
      if (path === '/operations/bottlenecks' && request.method === 'GET') {
        return this.getBottlenecks(env);
      }

      if (path === '/operations/sla-compliance' && request.method === 'GET') {
        return this.getSLACompliance(url, env);
      }

      if (path === '/operations/capacity' && request.method === 'GET') {
        return this.getCapacityPlanning(env);
      }

      // === PREDICTIVE ANALYTICS ===
      if (path === '/predictions/demand' && request.method === 'GET') {
        return this.getDemandPrediction(env);
      }

      if (path === '/predictions/issues' && request.method === 'GET') {
        return this.getPredictedIssues(env);
      }

      // === EXPORTS ===
      if (path === '/export/csv' && request.method === 'POST') {
        return this.exportCSV(request, env);
      }

      if (path === '/export/pdf' && request.method === 'POST') {
        return this.exportPDF(request, env);
      }

      return this.jsonResponse({ error: 'Not found' }, 404);
    } catch (error) {
      console.error('Analytics error:', error);
      return this.jsonResponse({ error: 'Internal error' }, 500);
    }
  },

  // === REAL-TIME DASHBOARD ===
  async getDashboard(env: Env): Promise<Response> {
    // Get all key metrics in parallel
    const [
      todayTickets,
      pendingTickets,
      avgResolution,
      todayRevenue,
      technicianStats,
      recentActivity,
    ] = await Promise.all([
      // Today's tickets
      env.DB.prepare(`
        SELECT COUNT(*) as count FROM tickets 
        WHERE date(created_at) = date('now')
      `).first(),
      
      // Pending tickets
      env.DB.prepare(`
        SELECT 
          COUNT(*) as total,
          SUM(CASE WHEN priority = 'urgent' THEN 1 ELSE 0 END) as urgent,
          SUM(CASE WHEN priority = 'high' THEN 1 ELSE 0 END) as high
        FROM tickets WHERE status NOT IN ('resolved', 'closed')
      `).first(),
      
      // Average resolution time (last 7 days)
      env.DB.prepare(`
        SELECT AVG(
          (julianday(resolved_at) - julianday(created_at)) * 24
        ) as avg_hours
        FROM tickets 
        WHERE resolved_at IS NOT NULL 
        AND resolved_at > datetime('now', '-7 days')
      `).first(),
      
      // Today's revenue
      env.DB.prepare(`
        SELECT COALESCE(SUM(final_price), 0) as revenue
        FROM tickets 
        WHERE date(resolved_at) = date('now')
        AND status IN ('resolved', 'closed')
      `).first(),
      
      // Technician capacity
      env.DB.prepare(`
        SELECT 
          COUNT(DISTINCT assigned_to) as active_technicians,
          COUNT(*) as in_progress_tickets
        FROM tickets 
        WHERE status = 'in_progress' 
        AND assigned_to IS NOT NULL
      `).first(),
      
      // Recent activity
      env.DB.prepare(`
        SELECT * FROM tickets 
        ORDER BY updated_at DESC 
        LIMIT 10
      `).all(),
    ]);

    // Get week over week comparison
    const lastWeek = await env.DB.prepare(`
      SELECT 
        COUNT(*) as tickets,
        COALESCE(SUM(final_price), 0) as revenue
      FROM tickets 
      WHERE created_at BETWEEN datetime('now', '-14 days') AND datetime('now', '-7 days')
    `).first();

    const thisWeek = await env.DB.prepare(`
      SELECT 
        COUNT(*) as tickets,
        COALESCE(SUM(final_price), 0) as revenue
      FROM tickets 
      WHERE created_at > datetime('now', '-7 days')
    `).first();

    const ticketTrend = (lastWeek as any)?.tickets > 0
      ? (((thisWeek as any)?.tickets - (lastWeek as any)?.tickets) / (lastWeek as any)?.tickets * 100).toFixed(1)
      : 0;
    
    const revenueTrend = (lastWeek as any)?.revenue > 0
      ? (((thisWeek as any)?.revenue - (lastWeek as any)?.revenue) / (lastWeek as any)?.revenue * 100).toFixed(1)
      : 0;

    return this.jsonResponse({
      timestamp: new Date().toISOString(),
      today: {
        tickets_created: (todayTickets as any)?.count || 0,
        revenue: (todayRevenue as any)?.revenue || 0,
      },
      pending: {
        total: (pendingTickets as any)?.total || 0,
        urgent: (pendingTickets as any)?.urgent || 0,
        high: (pendingTickets as any)?.high || 0,
      },
      performance: {
        avg_resolution_hours: Math.round((avgResolution as any)?.avg_hours || 0),
        active_technicians: (technicianStats as any)?.active_technicians || 0,
        in_progress: (technicianStats as any)?.in_progress_tickets || 0,
      },
      trends: {
        tickets_wow: ticketTrend,
        revenue_wow: revenueTrend,
      },
      recent_activity: recentActivity.results,
    });
  },

  async getLiveMetrics(env: Env): Promise<Response> {
    // Get last hour metrics for live dashboard
    const hourlyMetrics = await env.DB.prepare(`
      SELECT 
        strftime('%Y-%m-%d %H:00:00', created_at) as hour,
        COUNT(*) as tickets
      FROM tickets 
      WHERE created_at > datetime('now', '-24 hours')
      GROUP BY hour
      ORDER BY hour
    `).all();

    const activeNow = await env.DB.prepare(`
      SELECT 
        COUNT(CASE WHEN status = 'in_progress' THEN 1 END) as in_progress,
        COUNT(CASE WHEN status = 'waiting_parts' THEN 1 END) as waiting_parts,
        COUNT(CASE WHEN status = 'pending_approval' THEN 1 END) as pending_approval
      FROM tickets 
      WHERE status NOT IN ('resolved', 'closed')
    `).first();

    return this.jsonResponse({
      timestamp: new Date().toISOString(),
      hourly_volume: hourlyMetrics.results,
      current_status: activeNow,
    });
  },

  // === KPI REPORTS ===
  async getDailyKPIs(url: URL, env: Env): Promise<Response> {
    const date = url.searchParams.get('date') || new Date().toISOString().split('T')[0];

    const kpis = await env.DB.prepare(`
      SELECT 
        COUNT(*) as tickets_created,
        SUM(CASE WHEN status IN ('resolved', 'closed') THEN 1 ELSE 0 END) as tickets_closed,
        AVG(CASE WHEN resolved_at IS NOT NULL THEN 
          (julianday(resolved_at) - julianday(created_at)) * 24 
        END) as avg_resolution_hours,
        AVG(CASE WHEN first_response_at IS NOT NULL THEN 
          (julianday(first_response_at) - julianday(created_at)) * 24 * 60 
        END) as avg_first_response_minutes,
        COALESCE(SUM(final_price), 0) as revenue,
        COALESCE(SUM(parts_cost), 0) as parts_cost
      FROM tickets 
      WHERE date(created_at) = ?
    `).bind(date).first();

    return this.jsonResponse({
      date,
      kpis: {
        ...kpis,
        gross_margin: (kpis as any)?.revenue > 0 
          ? (((kpis as any).revenue - (kpis as any).parts_cost) / (kpis as any).revenue * 100).toFixed(1)
          : 0,
      },
    });
  },

  async getWeeklyKPIs(url: URL, env: Env): Promise<Response> {
    const weeks = parseInt(url.searchParams.get('weeks') || '4');

    const weeklyData = await env.DB.prepare(`
      SELECT 
        strftime('%Y-W%W', created_at) as week,
        COUNT(*) as tickets_created,
        SUM(CASE WHEN status IN ('resolved', 'closed') THEN 1 ELSE 0 END) as tickets_closed,
        AVG(CASE WHEN resolved_at IS NOT NULL THEN 
          (julianday(resolved_at) - julianday(created_at)) * 24 
        END) as avg_resolution_hours,
        COALESCE(SUM(final_price), 0) as revenue,
        COALESCE(SUM(parts_cost), 0) as parts_cost
      FROM tickets 
      WHERE created_at > datetime('now', '-' || ? || ' weeks')
      GROUP BY week
      ORDER BY week DESC
    `).bind(weeks * 7).all();

    return this.jsonResponse({
      weeks: weeks,
      data: weeklyData.results,
    });
  },

  async getMonthlyKPIs(url: URL, env: Env): Promise<Response> {
    const months = parseInt(url.searchParams.get('months') || '12');

    const monthlyData = await env.DB.prepare(`
      SELECT 
        strftime('%Y-%m', created_at) as month,
        COUNT(*) as tickets_created,
        SUM(CASE WHEN status IN ('resolved', 'closed') THEN 1 ELSE 0 END) as tickets_closed,
        AVG(CASE WHEN resolved_at IS NOT NULL THEN 
          (julianday(resolved_at) - julianday(created_at)) * 24 
        END) as avg_resolution_hours,
        COALESCE(SUM(final_price), 0) as revenue,
        COALESCE(SUM(parts_cost), 0) as parts_cost,
        COUNT(DISTINCT customer_id) as unique_customers
      FROM tickets 
      WHERE created_at > datetime('now', '-' || ? || ' months')
      GROUP BY month
      ORDER BY month DESC
    `).bind(months).all();

    return this.jsonResponse({
      months,
      data: monthlyData.results,
    });
  },

  async getKPITrends(url: URL, env: Env): Promise<Response> {
    const metric = url.searchParams.get('metric') || 'tickets';
    const period = url.searchParams.get('period') || '90';

    let selectField = 'COUNT(*) as value';
    if (metric === 'revenue') selectField = 'COALESCE(SUM(final_price), 0) as value';
    if (metric === 'resolution_time') selectField = 'AVG((julianday(resolved_at) - julianday(created_at)) * 24) as value';

    const trends = await env.DB.prepare(`
      SELECT 
        date(created_at) as date,
        ${selectField}
      FROM tickets 
      WHERE created_at > datetime('now', '-' || ? || ' days')
      GROUP BY date
      ORDER BY date
    `).bind(period).all();

    // Calculate moving average
    const values = (trends.results || []).map((r: any) => r.value || 0);
    const movingAvg = values.map((_, i) => {
      const window = values.slice(Math.max(0, i - 6), i + 1);
      return window.reduce((a, b) => a + b, 0) / window.length;
    });

    return this.jsonResponse({
      metric,
      period_days: period,
      data: trends.results,
      moving_average_7d: movingAvg,
    });
  },

  // === TECHNICIAN ANALYTICS ===
  async getTechnicianMetrics(url: URL, env: Env): Promise<Response> {
    const period = url.searchParams.get('period') || '30';

    const metrics = await env.DB.prepare(`
      SELECT 
        u.id,
        u.name,
        u.email,
        COUNT(t.id) as tickets_completed,
        AVG(CASE WHEN t.resolved_at IS NOT NULL THEN 
          (julianday(t.resolved_at) - julianday(t.created_at)) * 24 
        END) as avg_completion_hours,
        COALESCE(SUM(t.final_price), 0) as revenue_generated,
        AVG(t.customer_rating) as avg_rating
      FROM users u
      LEFT JOIN tickets t ON t.assigned_to = u.id 
        AND t.status IN ('resolved', 'closed')
        AND t.resolved_at > datetime('now', '-' || ? || ' days')
      WHERE u.role = 'technician'
      GROUP BY u.id
      ORDER BY tickets_completed DESC
    `).bind(period).all();

    // Calculate efficiency score (composite metric)
    const enriched = (metrics.results || []).map((tech: any) => ({
      ...tech,
      efficiency_score: this.calculateEfficiencyScore(tech),
    }));

    return this.jsonResponse({
      period_days: period,
      technicians: enriched,
    });
  },

  calculateEfficiencyScore(tech: any): number {
    // Weighted composite: 40% tickets, 30% speed, 30% satisfaction
    const ticketScore = Math.min(tech.tickets_completed / 50, 1) * 40;
    const speedScore = Math.max(0, (1 - tech.avg_completion_hours / 48)) * 30;
    const satisfactionScore = ((tech.avg_rating || 3) / 5) * 30;
    return Math.round(ticketScore + speedScore + satisfactionScore);
  },

  async getTechnicianDetail(techId: string, url: URL, env: Env): Promise<Response> {
    const period = url.searchParams.get('period') || '30';

    const [basic, dailyStats, categoryBreakdown, recentTickets] = await Promise.all([
      // Basic info
      env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(techId).first(),
      
      // Daily stats
      env.DB.prepare(`
        SELECT 
          date(resolved_at) as date,
          COUNT(*) as tickets,
          COALESCE(SUM(final_price), 0) as revenue
        FROM tickets 
        WHERE assigned_to = ? 
        AND status IN ('resolved', 'closed')
        AND resolved_at > datetime('now', '-' || ? || ' days')
        GROUP BY date
        ORDER BY date
      `).bind(techId, period).all(),
      
      // Category breakdown
      env.DB.prepare(`
        SELECT 
          device_type,
          COUNT(*) as count,
          AVG((julianday(resolved_at) - julianday(created_at)) * 24) as avg_hours
        FROM tickets 
        WHERE assigned_to = ? 
        AND status IN ('resolved', 'closed')
        AND resolved_at > datetime('now', '-' || ? || ' days')
        GROUP BY device_type
        ORDER BY count DESC
      `).bind(techId, period).all(),
      
      // Recent tickets
      env.DB.prepare(`
        SELECT * FROM tickets 
        WHERE assigned_to = ? 
        ORDER BY updated_at DESC 
        LIMIT 10
      `).bind(techId).all(),
    ]);

    return this.jsonResponse({
      technician: basic,
      daily_performance: dailyStats.results,
      specializations: categoryBreakdown.results,
      recent_tickets: recentTickets.results,
    });
  },

  async getTechnicianLeaderboard(url: URL, env: Env): Promise<Response> {
    const metric = url.searchParams.get('metric') || 'tickets';
    const period = url.searchParams.get('period') || '30';

    let orderBy = 'tickets_completed DESC';
    if (metric === 'revenue') orderBy = 'revenue_generated DESC';
    if (metric === 'rating') orderBy = 'avg_rating DESC';
    if (metric === 'speed') orderBy = 'avg_hours ASC';

    const leaderboard = await env.DB.prepare(`
      SELECT 
        u.id,
        u.name,
        COUNT(t.id) as tickets_completed,
        COALESCE(SUM(t.final_price), 0) as revenue_generated,
        AVG(t.customer_rating) as avg_rating,
        AVG((julianday(t.resolved_at) - julianday(t.created_at)) * 24) as avg_hours
      FROM users u
      LEFT JOIN tickets t ON t.assigned_to = u.id 
        AND t.status IN ('resolved', 'closed')
        AND t.resolved_at > datetime('now', '-' || ? || ' days')
      WHERE u.role = 'technician'
      GROUP BY u.id
      HAVING tickets_completed > 0
      ORDER BY ${orderBy}
      LIMIT 10
    `).bind(period).all();

    return this.jsonResponse({
      metric,
      period_days: period,
      leaderboard: leaderboard.results,
    });
  },

  // === REVENUE ANALYTICS ===
  async getRevenueOverview(url: URL, env: Env): Promise<Response> {
    const period = url.searchParams.get('period') || '30';

    const [current, previous] = await Promise.all([
      env.DB.prepare(`
        SELECT 
          COALESCE(SUM(final_price), 0) as revenue,
          COALESCE(SUM(parts_cost), 0) as parts_cost,
          COALESCE(SUM(labor_cost), 0) as labor_cost,
          COUNT(*) as transactions
        FROM tickets 
        WHERE resolved_at > datetime('now', '-' || ? || ' days')
        AND status IN ('resolved', 'closed')
      `).bind(period).first(),
      
      env.DB.prepare(`
        SELECT 
          COALESCE(SUM(final_price), 0) as revenue
        FROM tickets 
        WHERE resolved_at BETWEEN datetime('now', '-' || ? || ' days') AND datetime('now', '-' || ? || ' days')
        AND status IN ('resolved', 'closed')
      `).bind(parseInt(period) * 2, period).first(),
    ]);

    const periodGrowth = (previous as any)?.revenue > 0
      ? (((current as any).revenue - (previous as any).revenue) / (previous as any).revenue * 100).toFixed(1)
      : 0;

    return this.jsonResponse({
      period_days: period,
      revenue: (current as any)?.revenue || 0,
      parts_cost: (current as any)?.parts_cost || 0,
      labor_cost: (current as any)?.labor_cost || 0,
      gross_profit: (current as any)?.revenue - (current as any)?.parts_cost - (current as any)?.labor_cost,
      transactions: (current as any)?.transactions || 0,
      avg_ticket_value: (current as any)?.transactions > 0
        ? ((current as any).revenue / (current as any).transactions).toFixed(2)
        : 0,
      period_growth: periodGrowth,
    });
  },

  async getRevenueByCategory(url: URL, env: Env): Promise<Response> {
    const period = url.searchParams.get('period') || '90';

    const byCategory = await env.DB.prepare(`
      SELECT 
        device_type as category,
        COUNT(*) as tickets,
        COALESCE(SUM(final_price), 0) as revenue,
        AVG(final_price) as avg_price,
        COALESCE(SUM(parts_cost), 0) as parts_cost
      FROM tickets 
      WHERE resolved_at > datetime('now', '-' || ? || ' days')
      AND status IN ('resolved', 'closed')
      GROUP BY device_type
      ORDER BY revenue DESC
    `).bind(period).all();

    const total = (byCategory.results || []).reduce((sum, r: any) => sum + r.revenue, 0);
    const enriched = (byCategory.results || []).map((cat: any) => ({
      ...cat,
      percentage: total > 0 ? ((cat.revenue / total) * 100).toFixed(1) : 0,
      gross_margin: cat.revenue > 0 
        ? (((cat.revenue - cat.parts_cost) / cat.revenue) * 100).toFixed(1) 
        : 0,
    }));

    return this.jsonResponse({
      period_days: period,
      categories: enriched,
      total_revenue: total,
    });
  },

  async getRevenueByDevice(url: URL, env: Env): Promise<Response> {
    const period = url.searchParams.get('period') || '90';

    const byDevice = await env.DB.prepare(`
      SELECT 
        device_model,
        device_type,
        COUNT(*) as tickets,
        COALESCE(SUM(final_price), 0) as revenue,
        AVG(final_price) as avg_price
      FROM tickets 
      WHERE resolved_at > datetime('now', '-' || ? || ' days')
      AND status IN ('resolved', 'closed')
      AND device_model IS NOT NULL
      GROUP BY device_model
      ORDER BY tickets DESC
      LIMIT 20
    `).bind(period).all();

    return this.jsonResponse({
      period_days: period,
      devices: byDevice.results,
    });
  },

  async getRevenueForecast(env: Env): Promise<Response> {
    // Get historical monthly data
    const historical = await env.DB.prepare(`
      SELECT 
        strftime('%Y-%m', resolved_at) as month,
        COALESCE(SUM(final_price), 0) as revenue
      FROM tickets 
      WHERE resolved_at > datetime('now', '-12 months')
      AND status IN ('resolved', 'closed')
      GROUP BY month
      ORDER BY month
    `).all();

    // Use AI for forecasting
    const aiResponse = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{
        role: 'user',
        content: `Based on this monthly revenue data: ${JSON.stringify(historical.results)}, 
        predict the next 3 months of revenue. Consider seasonality and trends.
        Return JSON: { "predictions": [{ "month": "YYYY-MM", "predicted_revenue": number, "confidence": "high|medium|low" }], "factors": [] }`
      }]
    });

    return this.jsonResponse({
      historical: historical.results,
      forecast: aiResponse,
    });
  },

  // === CUSTOMER ANALYTICS ===
  async getCustomerLTV(env: Env): Promise<Response> {
    const ltv = await env.DB.prepare(`
      SELECT 
        customer_id,
        customer_name,
        COUNT(*) as total_tickets,
        COALESCE(SUM(final_price), 0) as lifetime_value,
        MIN(created_at) as first_visit,
        MAX(created_at) as last_visit,
        AVG(final_price) as avg_ticket_value
      FROM tickets 
      WHERE customer_id IS NOT NULL
      AND status IN ('resolved', 'closed')
      GROUP BY customer_id
      HAVING total_tickets >= 1
      ORDER BY lifetime_value DESC
      LIMIT 50
    `).all();

    // Calculate LTV metrics
    const enriched = (ltv.results || []).map((customer: any) => {
      const daysSinceFirst = Math.ceil(
        (Date.now() - new Date(customer.first_visit).getTime()) / (1000 * 60 * 60 * 24)
      );
      const monthsActive = Math.max(1, daysSinceFirst / 30);

      return {
        ...customer,
        monthly_value: (customer.lifetime_value / monthsActive).toFixed(2),
        visit_frequency: (customer.total_tickets / monthsActive).toFixed(2),
        customer_tenure_days: daysSinceFirst,
      };
    });

    return this.jsonResponse({
      customers: enriched,
      summary: {
        total_customers: enriched.length,
        avg_ltv: enriched.reduce((sum, c) => sum + c.lifetime_value, 0) / enriched.length,
        top_10_percent_value: enriched.slice(0, Math.ceil(enriched.length * 0.1))
          .reduce((sum, c) => sum + c.lifetime_value, 0),
      },
    });
  },

  async getCustomerSegments(env: Env): Promise<Response> {
    // RFM Segmentation: Recency, Frequency, Monetary
    const customers = await env.DB.prepare(`
      SELECT 
        customer_id,
        customer_name,
        COUNT(*) as frequency,
        COALESCE(SUM(final_price), 0) as monetary,
        MAX(created_at) as last_visit,
        julianday('now') - julianday(MAX(created_at)) as recency_days
      FROM tickets 
      WHERE customer_id IS NOT NULL
      AND status IN ('resolved', 'closed')
      GROUP BY customer_id
    `).all();

    // Segment customers
    const segments: Record<string, any[]> = {
      champions: [],      // High R, F, M
      loyal: [],          // High F, M
      potential: [],      // Medium R, F, M
      new: [],           // High R, Low F
      at_risk: [],       // Low R, High F
      lost: [],          // Very low R
    };

    for (const customer of customers.results || []) {
      const c = customer as any;
      const recencyScore = c.recency_days < 30 ? 3 : c.recency_days < 90 ? 2 : 1;
      const frequencyScore = c.frequency > 5 ? 3 : c.frequency > 2 ? 2 : 1;
      const monetaryScore = c.monetary > 500 ? 3 : c.monetary > 200 ? 2 : 1;

      const segment = this.determineSegment(recencyScore, frequencyScore, monetaryScore);
      segments[segment].push({
        ...c,
        rfm_score: `${recencyScore}${frequencyScore}${monetaryScore}`,
      });
    }

    return this.jsonResponse({
      segments,
      summary: {
        champions: segments.champions.length,
        loyal: segments.loyal.length,
        potential: segments.potential.length,
        new: segments.new.length,
        at_risk: segments.at_risk.length,
        lost: segments.lost.length,
      },
    });
  },

  determineSegment(r: number, f: number, m: number): string {
    if (r >= 3 && f >= 3 && m >= 2) return 'champions';
    if (f >= 3 && m >= 2) return 'loyal';
    if (r >= 2 && f >= 2) return 'potential';
    if (r >= 3 && f <= 1) return 'new';
    if (r <= 1 && f >= 2) return 'at_risk';
    return 'lost';
  },

  async getChurnRisk(env: Env): Promise<Response> {
    // Find customers who haven't returned
    const atRisk = await env.DB.prepare(`
      SELECT 
        customer_id,
        customer_name,
        customer_email,
        COUNT(*) as total_visits,
        COALESCE(SUM(final_price), 0) as lifetime_value,
        MAX(created_at) as last_visit,
        julianday('now') - julianday(MAX(created_at)) as days_since_visit
      FROM tickets 
      WHERE customer_id IS NOT NULL
      AND status IN ('resolved', 'closed')
      GROUP BY customer_id
      HAVING total_visits >= 2 
      AND days_since_visit > 60
      ORDER BY lifetime_value DESC
    `).all();

    // Calculate churn risk score
    const enriched = (atRisk.results || []).map((customer: any) => ({
      ...customer,
      churn_risk: customer.days_since_visit > 180 ? 'HIGH' 
        : customer.days_since_visit > 120 ? 'MEDIUM' : 'LOW',
      potential_lost_value: customer.lifetime_value / customer.total_visits * 12, // Annual projection
    }));

    return this.jsonResponse({
      at_risk_customers: enriched,
      total_potential_lost: enriched.reduce((sum, c) => sum + c.potential_lost_value, 0),
    });
  },

  async getAcquisitionMetrics(url: URL, env: Env): Promise<Response> {
    const period = url.searchParams.get('period') || '90';

    const newCustomers = await env.DB.prepare(`
      SELECT 
        date(MIN(created_at)) as acquisition_date,
        COUNT(*) as new_customers
      FROM tickets 
      WHERE created_at > datetime('now', '-' || ? || ' days')
      GROUP BY customer_id
      HAVING acquisition_date > datetime('now', '-' || ? || ' days')
    `).bind(period, period).all();

    const bySource = await env.DB.prepare(`
      SELECT 
        COALESCE(source, 'unknown') as source,
        COUNT(DISTINCT customer_id) as customers
      FROM tickets 
      WHERE created_at > datetime('now', '-' || ? || ' days')
      GROUP BY source
      ORDER BY customers DESC
    `).bind(period).all();

    return this.jsonResponse({
      period_days: period,
      new_customers: newCustomers.results?.length || 0,
      daily_acquisition: newCustomers.results,
      by_source: bySource.results,
    });
  },

  // === OPERATIONAL ANALYTICS ===
  async getBottlenecks(env: Env): Promise<Response> {
    // Find where tickets get stuck
    const stuckTickets = await env.DB.prepare(`
      SELECT 
        status,
        COUNT(*) as count,
        AVG(julianday('now') - julianday(
          CASE status 
            WHEN 'pending' THEN created_at
            WHEN 'waiting_parts' THEN updated_at
            ELSE created_at
          END
        )) as avg_days_in_status
      FROM tickets 
      WHERE status NOT IN ('resolved', 'closed')
      GROUP BY status
      ORDER BY avg_days_in_status DESC
    `).all();

    // Identify specific bottlenecks
    const longWaiting = await env.DB.prepare(`
      SELECT * FROM tickets 
      WHERE status NOT IN ('resolved', 'closed')
      AND julianday('now') - julianday(updated_at) > 3
      ORDER BY created_at ASC
      LIMIT 10
    `).all();

    return this.jsonResponse({
      status_bottlenecks: stuckTickets.results,
      stuck_tickets: longWaiting.results,
      recommendations: this.generateBottleneckRecommendations(stuckTickets.results || []),
    });
  },

  generateBottleneckRecommendations(bottlenecks: any[]): string[] {
    const recommendations: string[] = [];
    
    for (const b of bottlenecks) {
      if (b.status === 'waiting_parts' && b.avg_days_in_status > 5) {
        recommendations.push('Consider maintaining higher inventory for frequently needed parts');
      }
      if (b.status === 'pending' && b.count > 20) {
        recommendations.push('High pending queue - consider adding technician capacity');
      }
      if (b.status === 'pending_approval' && b.avg_days_in_status > 2) {
        recommendations.push('Quote approvals taking too long - streamline approval process');
      }
    }
    
    return recommendations;
  },

  async getSLACompliance(url: URL, env: Env): Promise<Response> {
    const period = url.searchParams.get('period') || '30';

    // Define SLAs
    const slaTargets = {
      first_response_minutes: 60,
      resolution_hours: 48,
      urgent_response_minutes: 15,
    };

    const compliance = await env.DB.prepare(`
      SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN first_response_at IS NOT NULL AND 
          (julianday(first_response_at) - julianday(created_at)) * 24 * 60 <= 60 
          THEN 1 ELSE 0 END) as first_response_met,
        SUM(CASE WHEN resolved_at IS NOT NULL AND 
          (julianday(resolved_at) - julianday(created_at)) * 24 <= 48 
          THEN 1 ELSE 0 END) as resolution_met,
        SUM(CASE WHEN priority = 'urgent' AND first_response_at IS NOT NULL AND 
          (julianday(first_response_at) - julianday(created_at)) * 24 * 60 <= 15 
          THEN 1 ELSE 0 END) as urgent_response_met,
        SUM(CASE WHEN priority = 'urgent' THEN 1 ELSE 0 END) as total_urgent
      FROM tickets 
      WHERE created_at > datetime('now', '-' || ? || ' days')
    `).bind(period).first();

    const c = compliance as any;

    return this.jsonResponse({
      period_days: period,
      sla_targets: slaTargets,
      compliance: {
        first_response: {
          met: c?.first_response_met || 0,
          total: c?.total || 0,
          percentage: c?.total > 0 ? ((c.first_response_met / c.total) * 100).toFixed(1) : 0,
        },
        resolution: {
          met: c?.resolution_met || 0,
          total: c?.total || 0,
          percentage: c?.total > 0 ? ((c.resolution_met / c.total) * 100).toFixed(1) : 0,
        },
        urgent_response: {
          met: c?.urgent_response_met || 0,
          total: c?.total_urgent || 0,
          percentage: c?.total_urgent > 0 ? ((c.urgent_response_met / c.total_urgent) * 100).toFixed(1) : 0,
        },
      },
    });
  },

  async getCapacityPlanning(env: Env): Promise<Response> {
    const [currentLoad, avgDaily, technicianCount] = await Promise.all([
      // Current workload
      env.DB.prepare(`
        SELECT 
          COUNT(*) as open_tickets,
          SUM(CASE WHEN priority = 'urgent' THEN 1 ELSE 0 END) as urgent
        FROM tickets 
        WHERE status NOT IN ('resolved', 'closed')
      `).first(),
      
      // Average daily tickets
      env.DB.prepare(`
        SELECT AVG(daily_count) as avg_daily
        FROM (
          SELECT date(created_at), COUNT(*) as daily_count
          FROM tickets 
          WHERE created_at > datetime('now', '-30 days')
          GROUP BY date(created_at)
        )
      `).first(),
      
      // Active technicians
      env.DB.prepare(`
        SELECT COUNT(*) as count FROM users WHERE role = 'technician' AND status = 'active'
      `).first(),
    ]);

    const avgDaily_ = (avgDaily as any)?.avg_daily || 10;
    const techCount = (technicianCount as any)?.count || 1;
    const ticketsPerTech = avgDaily_ / techCount;
    const currentBacklog = (currentLoad as any)?.open_tickets || 0;

    return this.jsonResponse({
      current: {
        open_tickets: currentBacklog,
        urgent: (currentLoad as any)?.urgent || 0,
        active_technicians: techCount,
      },
      capacity: {
        avg_daily_tickets: Math.round(avgDaily_),
        tickets_per_technician: ticketsPerTech.toFixed(1),
        capacity_utilization: ((currentBacklog / techCount) / 10 * 100).toFixed(1) + '%',
        estimated_clearance_days: (currentBacklog / avgDaily_).toFixed(1),
      },
      recommendations: this.getCapacityRecommendations(ticketsPerTech, currentBacklog, techCount),
    });
  },

  getCapacityRecommendations(ticketsPerTech: number, backlog: number, techCount: number): string[] {
    const recs: string[] = [];
    
    if (ticketsPerTech > 15) {
      recs.push('High workload per technician - consider hiring additional staff');
    }
    if (backlog > techCount * 20) {
      recs.push('Significant backlog building up - may need overtime or temp workers');
    }
    if (ticketsPerTech < 5) {
      recs.push('Technicians may be underutilized - opportunity for training or cross-skilling');
    }
    
    return recs;
  },

  // === PREDICTIVE ANALYTICS ===
  async getDemandPrediction(env: Env): Promise<Response> {
    // Historical weekly patterns
    const weeklyPattern = await env.DB.prepare(`
      SELECT 
        strftime('%w', created_at) as day_of_week,
        COUNT(*) as avg_tickets
      FROM tickets 
      WHERE created_at > datetime('now', '-90 days')
      GROUP BY day_of_week
      ORDER BY day_of_week
    `).all();

    // Trend analysis
    const monthlyTrend = await env.DB.prepare(`
      SELECT 
        strftime('%Y-%m', created_at) as month,
        COUNT(*) as tickets
      FROM tickets 
      WHERE created_at > datetime('now', '-12 months')
      GROUP BY month
      ORDER BY month
    `).all();

    // AI prediction
    const aiPrediction = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{
        role: 'user',
        content: `Based on weekly pattern: ${JSON.stringify(weeklyPattern.results)} and monthly trend: ${JSON.stringify(monthlyTrend.results)},
        predict next week's daily ticket volume. Return JSON: 
        { "predictions": [{ "day": "Monday", "predicted_tickets": number }], "peak_day": "", "suggested_staffing": {} }`
      }]
    });

    return this.jsonResponse({
      weekly_pattern: weeklyPattern.results,
      monthly_trend: monthlyTrend.results,
      ai_prediction: aiPrediction,
    });
  },

  async getPredictedIssues(env: Env): Promise<Response> {
    // Analyze common issues by device age/type
    const issuePatterns = await env.DB.prepare(`
      SELECT 
        device_type,
        device_model,
        issue_type,
        COUNT(*) as occurrences,
        AVG(final_price) as avg_repair_cost
      FROM tickets 
      WHERE created_at > datetime('now', '-180 days')
      GROUP BY device_type, device_model, issue_type
      HAVING occurrences >= 5
      ORDER BY occurrences DESC
      LIMIT 20
    `).all();

    return this.jsonResponse({
      common_issues: issuePatterns.results,
      insight: 'These are the most frequently occurring issues - consider stocking parts proactively',
    });
  },

  // === EXPORTS ===
  async exportCSV(request: Request, env: Env): Promise<Response> {
    const { report_type, period } = await request.json() as any;

    let data: any[] = [];
    let headers: string[] = [];

    if (report_type === 'tickets') {
      headers = ['ID', 'Created', 'Customer', 'Device', 'Status', 'Revenue'];
      const result = await env.DB.prepare(`
        SELECT id, created_at, customer_name, device_model, status, final_price
        FROM tickets 
        WHERE created_at > datetime('now', '-' || ? || ' days')
        ORDER BY created_at DESC
      `).bind(period || 30).all();
      data = result.results || [];
    }

    // Generate CSV
    const csv = [
      headers.join(','),
      ...data.map(row => Object.values(row).map(v => `"${v}"`).join(','))
    ].join('\n');

    return new Response(csv, {
      headers: {
        'Content-Type': 'text/csv',
        'Content-Disposition': `attachment; filename="${report_type}_report.csv"`,
        'Access-Control-Allow-Origin': '*',
      },
    });
  },

  async exportPDF(request: Request, env: Env): Promise<Response> {
    // For PDF generation, we'd normally use a library like pdfkit
    // Here we'll return JSON that a frontend can render to PDF
    const { report_type } = await request.json() as any;

    return this.jsonResponse({
      message: 'PDF generation data ready',
      report_type,
      generated_at: new Date().toISOString(),
      note: 'Use frontend PDF library to render this data',
    });
  },

  jsonResponse(data: any, status = 200): Response {
    return new Response(JSON.stringify(data), {
      status,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  },
};
