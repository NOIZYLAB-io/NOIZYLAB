// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB EBAY SNIPER AGENT
// "The Parts Hunter" Edition
// ═══════════════════════════════════════════════════════════════════════════════

export interface Env {
  DB: D1Database;
  EBAY_APP_ID: string;
  SLACK_WEBHOOK_URL: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// REPAIR SUCCESS RATES & COSTS
// ═══════════════════════════════════════════════════════════════════════════════

const REPAIR_DATA: Record<string, {
  success_rate: number;
  avg_repair_cost: number;
  avg_repair_time_hours: number;
  market_value_working: number;
}> = {
  "MacBook Pro 14 2021": {
    success_rate: 0.78,
    avg_repair_cost: 180,
    avg_repair_time_hours: 3,
    market_value_working: 1600
  },
  "MacBook Pro 16 2021": {
    success_rate: 0.75,
    avg_repair_cost: 200,
    avg_repair_time_hours: 3.5,
    market_value_working: 1900
  },
  "MacBook Pro 14 2023": {
    success_rate: 0.72,
    avg_repair_cost: 220,
    avg_repair_time_hours: 4,
    market_value_working: 2200
  },
  "MacBook Pro 16 2023": {
    success_rate: 0.70,
    avg_repair_cost: 250,
    avg_repair_time_hours: 4.5,
    market_value_working: 2600
  },
  "MacBook Air M2 2022": {
    success_rate: 0.82,
    avg_repair_cost: 120,
    avg_repair_time_hours: 2,
    market_value_working: 900
  },
  "iPhone 15 Pro": {
    success_rate: 0.85,
    avg_repair_cost: 80,
    avg_repair_time_hours: 1.5,
    market_value_working: 800
  },
  "iPhone 15 Pro Max": {
    success_rate: 0.83,
    avg_repair_cost: 100,
    avg_repair_time_hours: 2,
    market_value_working: 950
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// EBAY SEARCH
// ═══════════════════════════════════════════════════════════════════════════════

interface EbayListing {
  itemId: string;
  title: string;
  price: number;
  condition: string;
  location: string;
  url: string;
  imageUrl: string;
  sellerRating: number;
  endTime: string;
}

interface FlipOpportunity {
  listing: EbayListing;
  model: string;
  estimated_repair_cost: number;
  market_value_working: number;
  success_rate: number;
  expected_profit: number;
  risk_adjusted_profit: number;
  repair_time_hours: number;
  hourly_rate: number;
  score: number; // 0-100 opportunity score
}

async function searchEbay(env: Env, query: string, maxPrice: number): Promise<EbayListing[]> {
  // eBay Browse API
  const encodedQuery = encodeURIComponent(query);
  const url = `https://api.ebay.com/buy/browse/v1/item_summary/search?q=${encodedQuery}&filter=price:[..${maxPrice}],conditionIds:{7000}&limit=50&sort=endingSoonest`;

  const response = await fetch(url, {
    headers: {
      "Authorization": `Bearer ${env.EBAY_APP_ID}`,
      "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
      "Content-Type": "application/json"
    }
  });

  if (!response.ok) {
    console.error("eBay API error:", await response.text());
    return [];
  }

  const data = await response.json() as any;
  const items = data.itemSummaries || [];

  return items.map((item: any) => ({
    itemId: item.itemId,
    title: item.title,
    price: parseFloat(item.price?.value || "0"),
    condition: item.condition || "Unknown",
    location: item.itemLocation?.postalCode || "Unknown",
    url: item.itemWebUrl,
    imageUrl: item.image?.imageUrl || "",
    sellerRating: parseFloat(item.seller?.feedbackPercentage || "0"),
    endTime: item.itemEndDate || ""
  }));
}

// ═══════════════════════════════════════════════════════════════════════════════
// PROFIT CALCULATOR
// ═══════════════════════════════════════════════════════════════════════════════

function detectModel(title: string): string | null {
  const normalizedTitle = title.toLowerCase();
  
  for (const model of Object.keys(REPAIR_DATA)) {
    const modelLower = model.toLowerCase();
    const parts = modelLower.split(" ");
    
    // Check if all parts of model name are in title
    if (parts.every(part => normalizedTitle.includes(part))) {
      return model;
    }
  }
  
  return null;
}

function hasDesiredCondition(title: string): boolean {
  const titleLower = title.toLowerCase();
  const positiveIndicators = [
    "screen intact",
    "display works",
    "lcd good",
    "screen works",
    "no cracks",
    "screen perfect"
  ];
  const negativeIndicators = [
    "cracked screen",
    "broken display",
    "smashed",
    "shattered"
  ];
  
  const hasPositive = positiveIndicators.some(ind => titleLower.includes(ind));
  const hasNegative = negativeIndicators.some(ind => titleLower.includes(ind));
  
  return hasPositive || !hasNegative;
}

function calculateFlipOpportunity(listing: EbayListing): FlipOpportunity | null {
  const model = detectModel(listing.title);
  if (!model) return null;
  
  const data = REPAIR_DATA[model];
  if (!data) return null;
  
  // Check for good screen (biggest cost factor)
  const screenIntact = hasDesiredCondition(listing.title);
  const adjustedRepairCost = screenIntact ? data.avg_repair_cost : data.avg_repair_cost + 300;
  
  // Calculate profits
  const totalCost = listing.price + adjustedRepairCost;
  const expectedProfit = data.market_value_working - totalCost;
  const riskAdjustedProfit = expectedProfit * data.success_rate;
  const hourlyRate = riskAdjustedProfit / data.avg_repair_time_hours;
  
  // Score the opportunity (0-100)
  let score = 50;
  if (riskAdjustedProfit > 500) score += 20;
  else if (riskAdjustedProfit > 300) score += 10;
  else if (riskAdjustedProfit < 100) score -= 20;
  
  if (hourlyRate > 150) score += 15;
  else if (hourlyRate > 100) score += 10;
  else if (hourlyRate < 50) score -= 15;
  
  if (data.success_rate > 0.8) score += 10;
  if (listing.sellerRating > 98) score += 5;
  if (screenIntact) score += 10;
  
  score = Math.max(0, Math.min(100, score));
  
  return {
    listing,
    model,
    estimated_repair_cost: adjustedRepairCost,
    market_value_working: data.market_value_working,
    success_rate: data.success_rate,
    expected_profit: expectedProfit,
    risk_adjusted_profit: riskAdjustedProfit,
    repair_time_hours: data.avg_repair_time_hours,
    hourly_rate: hourlyRate,
    score
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// SLACK NOTIFICATION
// ═══════════════════════════════════════════════════════════════════════════════

async function notifySlack(env: Env, opportunities: FlipOpportunity[]): Promise<void> {
  if (!env.SLACK_WEBHOOK_URL || opportunities.length === 0) return;

  const blocks: any[] = [
    {
      type: "header",
      text: {
        type: "plain_text",
        text: `🎯 ${opportunities.length} Flip Opportunities Found!`,
        emoji: true
      }
    }
  ];

  for (const opp of opportunities.slice(0, 5)) { // Max 5 to avoid spam
    const emoji = opp.score >= 80 ? "🔥" : opp.score >= 60 ? "⚡" : "💡";
    
    blocks.push({
      type: "section",
      text: {
        type: "mrkdwn",
        text: `${emoji} *${opp.model}*\n` +
          `💰 Buy: $${opp.listing.price} → Sell: $${opp.market_value_working}\n` +
          `📈 Profit: *$${Math.round(opp.risk_adjusted_profit)}* (${Math.round(opp.success_rate * 100)}% success)\n` +
          `⏱️ $${Math.round(opp.hourly_rate)}/hr • Score: ${opp.score}/100`
      },
      accessory: {
        type: "button",
        text: { type: "plain_text", text: "View Listing", emoji: true },
        url: opp.listing.url
      }
    });

    blocks.push({ type: "divider" });
  }

  await fetch(env.SLACK_WEBHOOK_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ blocks })
  });
}

// ═══════════════════════════════════════════════════════════════════════════════
// MISSION RUNNER
// ═══════════════════════════════════════════════════════════════════════════════

interface MissionConfig {
  name: string;
  queries: string[];
  max_price: number;
  min_profit: number;
  min_score: number;
}

const MISSIONS: MissionConfig[] = [
  {
    name: "MacBook Pro Liquid Damage",
    queries: [
      'MacBook Pro 2021 "liquid damage" -"for parts only"',
      'MacBook Pro 2023 "water damage" screen works',
      'MacBook Pro 14 "damaged" "display intact"',
      'MacBook Pro 16 "liquid" "powers on"'
    ],
    max_price: 600,
    min_profit: 300,
    min_score: 60
  },
  {
    name: "MacBook Air Deals",
    queries: [
      'MacBook Air M2 "for parts" screen works',
      'MacBook Air 2022 "damaged" "display good"'
    ],
    max_price: 400,
    min_profit: 200,
    min_score: 55
  },
  {
    name: "iPhone Pro Repairs",
    queries: [
      'iPhone 15 Pro "cracked back" screen works',
      'iPhone 15 Pro Max "back glass" "lcd good"'
    ],
    max_price: 500,
    min_profit: 150,
    min_score: 50
  }
];

async function runMission(env: Env, mission: MissionConfig): Promise<FlipOpportunity[]> {
  console.log(`🎯 Running mission: ${mission.name}`);
  
  const allOpportunities: FlipOpportunity[] = [];
  
  for (const query of mission.queries) {
    const listings = await searchEbay(env, query, mission.max_price);
    console.log(`  Found ${listings.length} listings for: ${query.slice(0, 40)}...`);
    
    for (const listing of listings) {
      const opp = calculateFlipOpportunity(listing);
      if (opp && 
          opp.risk_adjusted_profit >= mission.min_profit && 
          opp.score >= mission.min_score) {
        allOpportunities.push(opp);
      }
    }
    
    // Rate limit
    await new Promise(r => setTimeout(r, 500));
  }
  
  // Sort by score
  allOpportunities.sort((a, b) => b.score - a.score);
  
  return allOpportunities;
}

// ═══════════════════════════════════════════════════════════════════════════════
// WORKER
// ═══════════════════════════════════════════════════════════════════════════════

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json"
    };

    // Health
    if (path === "/health") {
      return Response.json({ ok: true, service: "ebay-sniper" }, { headers: corsHeaders });
    }

    // List missions
    if (path === "/missions") {
      return Response.json({ ok: true, missions: MISSIONS.map(m => m.name) }, { headers: corsHeaders });
    }

    // Run specific mission
    if (path === "/run" && request.method === "POST") {
      const body = await request.json() as any;
      const missionName = body?.mission;
      
      const mission = missionName 
        ? MISSIONS.find(m => m.name === missionName)
        : MISSIONS[0];
      
      if (!mission) {
        return Response.json({ ok: false, error: "Mission not found" }, { status: 404, headers: corsHeaders });
      }
      
      const opportunities = await runMission(env, mission);
      
      // Notify Slack
      await notifySlack(env, opportunities);
      
      // Store in DB
      for (const opp of opportunities) {
        await env.DB.prepare(
          "INSERT OR IGNORE INTO flip_opportunities (item_id, model, price, profit, score, url, created_at) VALUES (?,?,?,?,?,?,?)"
        ).bind(
          opp.listing.itemId,
          opp.model,
          opp.listing.price,
          Math.round(opp.risk_adjusted_profit),
          opp.score,
          opp.listing.url,
          new Date().toISOString()
        ).run();
      }
      
      return Response.json({
        ok: true,
        mission: mission.name,
        found: opportunities.length,
        top_opportunities: opportunities.slice(0, 10)
      }, { headers: corsHeaders });
    }

    // Run all missions
    if (path === "/run-all" && request.method === "POST") {
      const allOpportunities: FlipOpportunity[] = [];
      
      for (const mission of MISSIONS) {
        const opps = await runMission(env, mission);
        allOpportunities.push(...opps);
      }
      
      // Dedupe by itemId
      const seen = new Set<string>();
      const unique = allOpportunities.filter(o => {
        if (seen.has(o.listing.itemId)) return false;
        seen.add(o.listing.itemId);
        return true;
      });
      
      unique.sort((a, b) => b.score - a.score);
      
      await notifySlack(env, unique);
      
      return Response.json({
        ok: true,
        total_found: unique.length,
        top_opportunities: unique.slice(0, 20)
      }, { headers: corsHeaders });
    }

    // Get stored opportunities
    if (path === "/opportunities") {
      const rows = await env.DB.prepare(
        "SELECT * FROM flip_opportunities ORDER BY score DESC, created_at DESC LIMIT 100"
      ).all<any>();
      
      return Response.json({ ok: true, opportunities: rows.results ?? [] }, { headers: corsHeaders });
    }

    return Response.json({ ok: false, error: "Not found" }, { status: 404, headers: corsHeaders });
  },

  // Scheduled: Run daily at 6 AM UTC
  async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext): Promise<void> {
    console.log("🕐 Running scheduled eBay sniper...");
    
    const allOpportunities: FlipOpportunity[] = [];
    
    for (const mission of MISSIONS) {
      const opps = await runMission(env, mission);
      allOpportunities.push(...opps);
    }
    
    const seen = new Set<string>();
    const unique = allOpportunities.filter(o => {
      if (seen.has(o.listing.itemId)) return false;
      seen.add(o.listing.itemId);
      return true;
    });
    
    unique.sort((a, b) => b.score - a.score);
    
    if (unique.length > 0) {
      await notifySlack(env, unique);
    }
    
    console.log(`✅ Found ${unique.length} opportunities`);
  }
};
