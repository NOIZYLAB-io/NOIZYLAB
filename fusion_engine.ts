/**
 * 🔬 FUSION ENGINE
 * Merges multi-genius responses into unified answer
 * Fish Music Inc - CB_01
 */

import { GeniusResponse } from '../../geniuses/base/GeniusBase';

export interface FusedResponse {
  all_findings: string[];
  all_recommendations: string[];
  geniuses_consulted: string[];
  confidence_average: number;
  priority_actions: string[];
}

export function fuse(results: GeniusResponse[]): FusedResponse {
  console.log(`🔬 Fusing ${results.length} genius responses...`);
  
  const merged: FusedResponse = {
    all_findings: [],
    all_recommendations: [],
    geniuses_consulted: [],
    confidence_average: 0,
    priority_actions: []
  };

  // Aggregate findings
  for (const result of results) {
    merged.all_findings.push(...result.findings);
    merged.all_recommendations.push(...result.recommendations);
    merged.geniuses_consulted.push(result.genius);
  }

  // Remove duplicates
  merged.all_findings = Array.from(new Set(merged.all_findings));
  merged.all_recommendations = Array.from(new Set(merged.all_recommendations));

  // Calculate average confidence
  const confidences = results
    .map(r => r.confidence || 0.9)
    .filter(c => c > 0);
  
  merged.confidence_average = confidences.length > 0
    ? confidences.reduce((a, b) => a + b, 0) / confidences.length
    : 0.9;

  // Prioritize actions
  merged.priority_actions = prioritizeActions(merged.all_recommendations);

  console.log(`✅ Fusion complete. Confidence: ${(merged.confidence_average * 100).toFixed(1)}%`);

  return merged;
}

function prioritizeActions(recommendations: string[]): string[] {
  const priorities: string[] = [];
  
  // Critical first
  const critical = recommendations.filter(r => 
    r.includes('BACKUP') || 
    r.includes('URGENT') ||
    r.includes('CRITICAL') ||
    r.includes('IMMEDIATELY')
  );
  priorities.push(...critical);
  
  // High priority second
  const high = recommendations.filter(r =>
    r.includes('Replace') ||
    r.includes('Update') ||
    r.includes('Fix')
  );
  priorities.push(...high.filter(h => !priorities.includes(h)));
  
  // Everything else
  const rest = recommendations.filter(r => !priorities.includes(r));
  priorities.push(...rest);
  
  return priorities.slice(0, 10);  // Top 10 actions
}
