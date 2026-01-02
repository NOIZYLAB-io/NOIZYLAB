// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB PRICING INTELLIGENCE - Smart Repair Pricing Engine
// "The Accountant" Edition - Maximize Profits, Stay Competitive
// ═══════════════════════════════════════════════════════════════════════════════

export interface Env {
  DB: D1Database;
  KV_CACHE: KVNamespace;
}

// ═══════════════════════════════════════════════════════════════════════════════
// MARKET DATA
// ═══════════════════════════════════════════════════════════════════════════════

interface MarketRate {
  repair_type: string;
  device_category: string;
  min_price: number;
  max_price: number;
  avg_price: number;
  your_price?: number;
  competitor_prices: number[];
}

const MARKET_RATES: Record<string, MarketRate> = {
  "macbook_screen_replacement": {
    repair_type: "Screen Replacement",
    device_category: "MacBook",
    min_price: 299,
    max_price: 899,
    avg_price: 549,
    competitor_prices: [399, 499, 549, 599, 649]
  },
  "macbook_battery_replacement": {
    repair_type: "Battery Replacement",
    device_category: "MacBook",
    min_price: 129,
    max_price: 299,
    avg_price: 189,
    competitor_prices: [149, 179, 189, 199, 229]
  },
  "macbook_keyboard_replacement": {
    repair_type: "Keyboard Replacement",
    device_category: "MacBook",
    min_price: 199,
    max_price: 499,
    avg_price: 349,
    competitor_prices: [249, 299, 349, 399, 449]
  },
  "macbook_logic_board_repair": {
    repair_type: "Logic Board Repair",
    device_category: "MacBook",
    min_price: 249,
    max_price: 799,
    avg_price: 449,
    competitor_prices: [299, 399, 449, 549, 649]
  },
  "macbook_liquid_damage": {
    repair_type: "Liquid Damage Repair",
    device_category: "MacBook",
    min_price: 299,
    max_price: 899,
    avg_price: 499,
    competitor_prices: [349, 449, 499, 599, 699]
  },
  "iphone_screen_replacement": {
    repair_type: "Screen Replacement",
    device_category: "iPhone",
    min_price: 79,
    max_price: 329,
    avg_price: 179,
    competitor_prices: [99, 149, 179, 199, 249]
  },
  "iphone_battery_replacement": {
    repair_type: "Battery Replacement",
    device_category: "iPhone",
    min_price: 49,
    max_price: 129,
    avg_price: 79,
    competitor_prices: [59, 69, 79, 89, 99]
  },
  "iphone_charging_port": {
    repair_type: "Charging Port Repair",
    device_category: "iPhone",
    min_price: 59,
    max_price: 149,
    avg_price: 99,
    competitor_prices: [69, 89, 99, 119, 129]
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// COST CALCULATION
// ═══════════════════════════════════════════════════════════════════════════════

interface CostBreakdown {
  parts_cost: number;
  labor_cost: number;
  overhead: number;
  total_cost: number;
  suggested_price: number;
  profit_margin: number;
  hourly_rate_achieved: number;
}

interface PricingFactors {
  parts_cost: number;
  labor_minutes: number;
  difficulty: "easy" | "medium" | "hard" | "expert";
  urgency: "standard" | "rush" | "emergency";
  warranty_months: number;
  device_age_years?: number;
  customer_type?: "new" | "returning" | "vip";
}

const LABOR_RATES: Record<string, number> = {
  easy: 60,      // $60/hr
  medium: 80,    // $80/hr
  hard: 120,     // $120/hr
  expert: 180    // $180/hr
};

const URGENCY_MULTIPLIERS: Record<string, number> = {
  standard: 1.0,
  rush: 1.5,      // Same day
  emergency: 2.0  // Within hours
};

const WARRANTY_COSTS: Record<number, number> = {
  0: 0,
  3: 0.05,   // 5% of repair
  6: 0.08,   // 8%
  12: 0.12,  // 12%
  24: 0.18   // 18%
};

function calculateCost(factors: PricingFactors): CostBreakdown {
  // Base labor cost
  const hourlyRate = LABOR_RATES[factors.difficulty];
  const laborHours = factors.labor_minutes / 60;
  const baseLaborCost = laborHours * hourlyRate;
  
  // Apply urgency multiplier
  const urgencyMultiplier = URGENCY_MULTIPLIERS[factors.urgency];
  const adjustedLaborCost = baseLaborCost * urgencyMultiplier;
  
  // Parts markup (30-50% depending on difficulty)
  const partsMarkup = factors.difficulty === "expert" ? 0.5 : 
                      factors.difficulty === "hard" ? 0.4 : 0.3;
  const partsWithMarkup = factors.parts_cost * (1 + partsMarkup);
  
  // Overhead (rent, tools, utilities) - typically 15-20%
  const overhead = (adjustedLaborCost + partsWithMarkup) * 0.18;
  
  // Warranty reserve
  const warrantyReserve = WARRANTY_COSTS[factors.warranty_months] || 0;
  
  // Total cost
  const totalCost = factors.parts_cost + adjustedLaborCost + overhead;
  
  // Suggested price (target 40-60% margin)
  const targetMargin = factors.difficulty === "expert" ? 0.55 : 
                       factors.difficulty === "hard" ? 0.50 : 
                       factors.difficulty === "medium" ? 0.45 : 0.40;
  
  const suggestedPrice = Math.round(totalCost / (1 - targetMargin));
  
  // Add warranty cost
  const finalPrice = Math.round(suggestedPrice * (1 + warrantyReserve));
  
  // Customer discount
  let customerDiscount = 0;
  if (factors.customer_type === "returning") customerDiscount = 0.05;
  if (factors.customer_type === "vip") customerDiscount = 0.10;
  
  const discountedPrice = Math.round(finalPrice * (1 - customerDiscount));
  
  // Calculate actual metrics
  const profitMargin = (discountedPrice - totalCost) / discountedPrice;
  const hourlyRateAchieved = (discountedPrice - factors.parts_cost) / laborHours;
  
  return {
    parts_cost: factors.parts_cost,
    labor_cost: adjustedLaborCost,
    overhead,
    total_cost: totalCost,
    suggested_price: discountedPrice,
    profit_margin: Math.round(profitMargin * 100),
    hourly_rate_achieved: Math.round(hourlyRateAchieved)
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// COMPETITIVE ANALYSIS
// ═══════════════════════════════════════════════════════════════════════════════

interface CompetitivePosition {
  your_price: number;
  market_avg: number;
  market_min: number;
  market_max: number;
  position: "budget" | "competitive" | "premium" | "luxury";
  percentile: number;
  recommendation: string;
}

function analyzeCompetitivePosition(
  yourPrice: number,
  repairKey: string
): CompetitivePosition {
  const market = MARKET_RATES[repairKey];
  if (!market) {
    return {
      your_price: yourPrice,
      market_avg: yourPrice,
      market_min: yourPrice * 0.7,
      market_max: yourPrice * 1.3,
      position: "competitive",
      percentile: 50,
      recommendation: "No market data available"
    };
  }
  
  // Calculate percentile
  const allPrices = [...market.competitor_prices, yourPrice].sort((a, b) => a - b);
  const yourIndex = allPrices.indexOf(yourPrice);
  const percentile = Math.round((yourIndex / (allPrices.length - 1)) * 100);
  
  // Determine position
  let position: "budget" | "competitive" | "premium" | "luxury";
  let recommendation: string;
  
  if (yourPrice < market.avg * 0.85) {
    position = "budget";
    recommendation = "You're priced below market. Consider raising prices or emphasizing value to avoid appearing low-quality.";
  } else if (yourPrice <= market.avg * 1.15) {
    position = "competitive";
    recommendation = "You're competitively priced. Focus on service quality and turnaround time to differentiate.";
  } else if (yourPrice <= market.avg * 1.4) {
    position = "premium";
    recommendation = "Premium pricing. Ensure your service, warranty, and customer experience justify the higher price.";
  } else {
    position = "luxury";
    recommendation = "Luxury pricing. You need exceptional service, guarantees, and branding to sustain this position.";
  }
  
  return {
    your_price: yourPrice,
    market_avg: market.avg_price,
    market_min: market.min_price,
    market_max: market.max_price,
    position,
    percentile,
    recommendation
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// DYNAMIC PRICING
// ═══════════════════════════════════════════════════════════════════════════════

interface DynamicPriceAdjustment {
  base_price: number;
  adjusted_price: number;
  adjustments: { factor: string; impact: number }[];
  reason: string;
}

async function calculateDynamicPrice(
  env: Env,
  basePrice: number,
  repairType: string
): Promise<DynamicPriceAdjustment> {
  const adjustments: { factor: string; impact: number }[] = [];
  let adjustedPrice = basePrice;
  
  // Check current workload (from DB)
  const openTickets = await env.DB.prepare(
    "SELECT COUNT(*) as count FROM tickets WHERE status NOT IN ('CLOSED', 'PURGED')"
  ).first<any>();
  
  const workload = openTickets?.count || 0;
  
  // Demand-based pricing
  if (workload > 20) {
    const demandMultiplier = 1.15;  // 15% increase when busy
    const impact = Math.round(basePrice * 0.15);
    adjustments.push({ factor: "High demand", impact });
    adjustedPrice *= demandMultiplier;
  } else if (workload < 5) {
    const discountMultiplier = 0.95;  // 5% discount when slow
    const impact = -Math.round(basePrice * 0.05);
    adjustments.push({ factor: "Capacity available", impact });
    adjustedPrice *= discountMultiplier;
  }
  
  // Time-based pricing
  const hour = new Date().getHours();
  const dayOfWeek = new Date().getDay();
  
  // Weekend premium
  if (dayOfWeek === 0 || dayOfWeek === 6) {
    const weekendPremium = 1.1;
    const impact = Math.round(basePrice * 0.1);
    adjustments.push({ factor: "Weekend service", impact });
    adjustedPrice *= weekendPremium;
  }
  
  // After-hours premium
  if (hour < 9 || hour > 18) {
    const afterHoursPremium = 1.2;
    const impact = Math.round(basePrice * 0.2);
    adjustments.push({ factor: "After-hours service", impact });
    adjustedPrice *= afterHoursPremium;
  }
  
  // Seasonal adjustment (example: back-to-school)
  const month = new Date().getMonth();
  if (month === 7 || month === 8) {  // August, September
    const seasonalPremium = 1.08;
    const impact = Math.round(basePrice * 0.08);
    adjustments.push({ factor: "Back-to-school season", impact });
    adjustedPrice *= seasonalPremium;
  }
  
  // Round to nearest $5
  adjustedPrice = Math.round(adjustedPrice / 5) * 5;
  
  // Generate reason
  const reason = adjustments.length > 0
    ? `Price adjusted due to: ${adjustments.map(a => a.factor).join(", ")}`
    : "Standard pricing applied";
  
  return {
    base_price: basePrice,
    adjusted_price: adjustedPrice,
    adjustments,
    reason
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// BUNDLE PRICING
// ═══════════════════════════════════════════════════════════════════════════════

interface BundleQuote {
  repairs: { type: string; individual_price: number }[];
  individual_total: number;
  bundle_price: number;
  savings: number;
  savings_percent: number;
}

function calculateBundlePrice(repairs: { type: string; price: number }[]): BundleQuote {
  const individualTotal = repairs.reduce((sum, r) => sum + r.price, 0);
  
  // Bundle discount tiers
  let discountPercent = 0;
  if (repairs.length >= 4) discountPercent = 0.20;      // 20% off for 4+
  else if (repairs.length >= 3) discountPercent = 0.15; // 15% off for 3
  else if (repairs.length >= 2) discountPercent = 0.10; // 10% off for 2
  
  const bundlePrice = Math.round(individualTotal * (1 - discountPercent));
  const savings = individualTotal - bundlePrice;
  
  return {
    repairs: repairs.map(r => ({ type: r.type, individual_price: r.price })),
    individual_total: individualTotal,
    bundle_price: bundlePrice,
    savings,
    savings_percent: Math.round(discountPercent * 100)
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// PROFITABILITY ANALYSIS
// ═══════════════════════════════════════════════════════════════════════════════

interface ProfitabilityReport {
  period: string;
  total_revenue: number;
  total_costs: number;
  gross_profit: number;
  gross_margin: number;
  repairs_by_type: { type: string; count: number; revenue: number; profit: number }[];
  avg_ticket_value: number;
  avg_profit_per_repair: number;
  top_profitable_repairs: string[];
  recommendations: string[];
}

async function analyzeProfitability(
  env: Env,
  startDate: string,
  endDate: string
): Promise<ProfitabilityReport> {
  // Get completed repairs in period
  const repairs = await env.DB.prepare(`
    SELECT 
      t.id,
      t.channel as repair_type,
      p.amount as revenue,
      e.estimate_amount as estimated_cost
    FROM tickets t
    LEFT JOIN payments p ON p.ticket_id = t.id
    LEFT JOIN estimates e ON e.ticket_id = t.id
    WHERE t.status = 'CLOSED'
      AND t.created_at >= ?
      AND t.created_at <= ?
  `).bind(startDate, endDate).all<any>();
  
  const results = repairs.results || [];
  
  // Calculate totals
  let totalRevenue = 0;
  let totalCosts = 0;
  const byType: Record<string, { count: number; revenue: number; cost: number }> = {};
  
  for (const repair of results) {
    const revenue = repair.revenue || 0;
    const cost = (repair.estimated_cost || revenue) * 0.6;  // Estimate 40% margin
    
    totalRevenue += revenue;
    totalCosts += cost;
    
    const type = repair.repair_type || "unknown";
    if (!byType[type]) byType[type] = { count: 0, revenue: 0, cost: 0 };
    byType[type].count++;
    byType[type].revenue += revenue;
    byType[type].cost += cost;
  }
  
  const grossProfit = totalRevenue - totalCosts;
  const grossMargin = totalRevenue > 0 ? (grossProfit / totalRevenue) * 100 : 0;
  
  // By type analysis
  const repairsByType = Object.entries(byType).map(([type, data]) => ({
    type,
    count: data.count,
    revenue: data.revenue,
    profit: data.revenue - data.cost
  }));
  
  // Sort by profit
  repairsByType.sort((a, b) => b.profit - a.profit);
  
  // Generate recommendations
  const recommendations: string[] = [];
  
  if (grossMargin < 35) {
    recommendations.push("Gross margin below 35%. Consider raising prices or reducing parts costs.");
  }
  if (grossMargin > 60) {
    recommendations.push("Excellent margins! Consider competitive pricing to increase volume.");
  }
  
  const avgTicket = results.length > 0 ? totalRevenue / results.length : 0;
  if (avgTicket < 150) {
    recommendations.push("Low average ticket value. Focus on upselling additional services.");
  }
  
  return {
    period: `${startDate} to ${endDate}`,
    total_revenue: totalRevenue,
    total_costs: totalCosts,
    gross_profit: grossProfit,
    gross_margin: Math.round(grossMargin),
    repairs_by_type: repairsByType,
    avg_ticket_value: Math.round(avgTicket),
    avg_profit_per_repair: results.length > 0 ? Math.round(grossProfit / results.length) : 0,
    top_profitable_repairs: repairsByType.slice(0, 3).map(r => r.type),
    recommendations
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// WORKER
// ═══════════════════════════════════════════════════════════════════════════════

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json"
    };

    if (method === "OPTIONS") {
      return new Response(null, {
        headers: { ...corsHeaders, "Access-Control-Allow-Methods": "GET, POST" }
      });
    }

    try {
      // Health
      if (path === "/health") {
        return Response.json({ ok: true, service: "pricing" }, { headers: corsHeaders });
      }

      // Get market rates
      if (path === "/market-rates") {
        return Response.json({ ok: true, rates: MARKET_RATES }, { headers: corsHeaders });
      }

      // Calculate repair cost
      if (path === "/calculate" && method === "POST") {
        const body = await request.json() as PricingFactors;
        const result = calculateCost(body);
        return Response.json({ ok: true, ...result }, { headers: corsHeaders });
      }

      // Competitive analysis
      if (path === "/competitive" && method === "POST") {
        const body = await request.json() as { price: number; repair_key: string };
        const result = analyzeCompetitivePosition(body.price, body.repair_key);
        return Response.json({ ok: true, ...result }, { headers: corsHeaders });
      }

      // Dynamic pricing
      if (path === "/dynamic" && method === "POST") {
        const body = await request.json() as { base_price: number; repair_type: string };
        const result = await calculateDynamicPrice(env, body.base_price, body.repair_type);
        return Response.json({ ok: true, ...result }, { headers: corsHeaders });
      }

      // Bundle pricing
      if (path === "/bundle" && method === "POST") {
        const body = await request.json() as { repairs: { type: string; price: number }[] };
        const result = calculateBundlePrice(body.repairs);
        return Response.json({ ok: true, ...result }, { headers: corsHeaders });
      }

      // Profitability report
      if (path === "/profitability" && method === "GET") {
        const startDate = url.searchParams.get("start") || new Date(Date.now() - 30 * 86400_000).toISOString().slice(0, 10);
        const endDate = url.searchParams.get("end") || new Date().toISOString().slice(0, 10);
        const result = await analyzeProfitability(env, startDate, endDate);
        return Response.json({ ok: true, ...result }, { headers: corsHeaders });
      }

      return Response.json({ ok: false, error: "Not found" }, { status: 404, headers: corsHeaders });

    } catch (err: any) {
      return Response.json({ ok: false, error: err.message }, { status: 500, headers: corsHeaders });
    }
  }
};
