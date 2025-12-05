/**
 * 💬 SUPPORT GENIUS
 * The explainer, translator, jargon killer
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class SupportGenius extends GeniusBase {
  name = "SupportGenius";
  squad = "experience";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const techLevel = context.metrics?.tech_knowledge || 'beginner';

    findings.push(`User tech level: ${techLevel}`);

    if (techLevel === 'beginner' || techLevel === 'low') {
      findings.push("Non-technical user detected");
      
      recs.push("Translate ALL jargon into everyday language");
      recs.push("Example: 'RAM' → 'your computer's short-term memory'");
      recs.push("Example: 'SSD' → 'your storage drive'");
      recs.push("Example: 'kernel panic' → 'system crash'");
      recs.push("Use metaphors: 'RAM is like your desk—bigger desk = more space'");
      recs.push("Show visual steps when possible");
    } else if (techLevel === 'intermediate') {
      findings.push("Some technical knowledge present");
      
      recs.push("Balance technical terms with brief explanations");
      recs.push("Offer 'Learn more' links for deeper dives");
      recs.push("Assume basic computer literacy");
    } else {
      findings.push("Power user / technical user");
      
      recs.push("Use precise technical language");
      recs.push("Show detailed logs and metrics");
      recs.push("Provide advanced options");
      recs.push("Skip hand-holding");
    }

    return this.resp(findings, recs, 0.95);
  }
}
