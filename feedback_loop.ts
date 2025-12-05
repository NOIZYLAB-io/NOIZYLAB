/**
 * 🔁 FEEDBACK LOOP
 * Self-improvement engine for geniuses
 * Fish Music Inc - CB_01
 */

export interface SessionFeedback {
  session_id: string;
  geniuses_used: string[];
  success: boolean;
  user_satisfaction: number;  // 0-100
  issues_resolved: number;
  time_taken_minutes: number;
}

export function feedbackLoop(history: SessionFeedback[]) {
  console.log(`🔁 Analyzing ${history.length} sessions for improvement...`);
  
  if (history.length === 0) {
    return {
      total_sessions: 0,
      overall_success_rate: 0,
      genius_performance: {}
    };
  }
  
  // Calculate overall metrics
  const successfulSessions = history.filter(h => h.success).length;
  const successRate = successfulSessions / history.length;
  
  // Calculate per-genius performance
  const geniusPerformance: Record<string, any> = {};
  
  for (const session of history) {
    for (const genius of session.geniuses_used) {
      if (!geniusPerformance[genius]) {
        geniusPerformance[genius] = {
          times_called: 0,
          successes: 0,
          avg_satisfaction: 0,
          total_satisfaction: 0
        };
      }
      
      geniusPerformance[genius].times_called += 1;
      if (session.success) {
        geniusPerformance[genius].successes += 1;
      }
      geniusPerformance[genius].total_satisfaction += session.user_satisfaction;
    }
  }
  
  // Calculate averages
  for (const genius in geniusPerformance) {
    const perf = geniusPerformance[genius];
    perf.success_rate = perf.successes / perf.times_called;
    perf.avg_satisfaction = perf.total_satisfaction / perf.times_called;
    delete perf.total_satisfaction;
  }
  
  console.log(`✅ Success rate: ${(successRate * 100).toFixed(1)}%`);
  
  return {
    total_sessions: history.length,
    overall_success_rate: successRate,
    genius_performance: geniusPerformance,
    insights: generateInsights(geniusPerformance)
  };
}

function generateInsights(performance: Record<string, any>): string[] {
  const insights: string[] = [];
  
  // Find top performers
  const sorted = Object.entries(performance)
    .sort((a, b) => b[1].success_rate - a[1].success_rate);
  
  if (sorted.length > 0) {
    const top = sorted[0];
    insights.push(`Top performer: ${top[0]} (${(top[1].success_rate * 100).toFixed(1)}% success)`);
  }
  
  // Find underperformers
  const underperformers = sorted.filter(([_, perf]) => perf.success_rate < 0.7);
  if (underperformers.length > 0) {
    insights.push(`${underperformers.length} geniuses need retraining`);
  }
  
  return insights;
}
