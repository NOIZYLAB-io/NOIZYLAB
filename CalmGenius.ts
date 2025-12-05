/**
 * 😌 CALM GENIUS
 * The anxiety killer, panic diffuser, tech therapist
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class CalmGenius extends GeniusBase {
  name = "CalmGenius";
  squad = "experience";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    // Detect user stress signals
    const metrics = context.metrics || {};
    const userStress = metrics.stress_level || 'unknown';

    findings.push("User stress level assessed");
    
    if (userStress === 'high' || userStress === 'unknown') {
      findings.push("Anxiety reduction mode activated");
      
      recs.push("Use calming language: 'Everything is under control'");
      recs.push("Break complex tasks into tiny, simple steps");
      recs.push("Provide constant reassurance and progress updates");
      recs.push("Avoid technical jargon completely");
      recs.push("Show estimated time remaining clearly");
      recs.push("Remind user: 'You can stop anytime. You're in control.'");
    } else {
      findings.push("User stress: Normal");
      recs.push("Maintain friendly, supportive tone");
      recs.push("Standard communication approach is fine");
    }

    return this.resp(findings, recs, 0.97);
  }
}
