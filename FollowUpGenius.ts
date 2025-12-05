/**
 * 📞 FOLLOW-UP GENIUS
 * Retention booster, relationship builder
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class FollowUpGenius extends GeniusBase {
  name = "FollowUpGenius";
  squad = "business";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const daysSinceRepair = context.metrics?.days_since_repair || 0;
    const repairType = context.metrics?.repair_type || 'standard';

    findings.push(`Follow-up sequence: ${daysSinceRepair} days post-repair`);

    // 24-hour follow-up
    if (daysSinceRepair === 1) {
      findings.push("24-hour check-in due");
      
      recs.push("Send friendly check-in email:");
      recs.push("  'Hey! How's your [device] running?'");
      recs.push("  'Everything smooth after yesterday's repair?'");
      recs.push("Include quick feedback buttons: 👍 👎");
      recs.push("Offer immediate support if issues");
    }

    // 7-day follow-up
    if (daysSinceRepair === 7) {
      findings.push("1-week check-in due");
      
      recs.push("Request testimonial/review (if happy)");
      recs.push("Send device care tips");
      recs.push("Example: 'Pro tip: Restart weekly for best performance'");
      recs.push("Remind about 7-day guarantee");
    }

    // 30-day follow-up
    if (daysSinceRepair === 30) {
      findings.push("Monthly check-in due");
      
      recs.push("Offer complimentary health scan");
      recs.push("Share performance tips");
      recs.push("Gently suggest maintenance package");
      recs.push("Keep tone helpful, not pushy");
    }

    // 90-day follow-up
    if (daysSinceRepair === 90) {
      findings.push("Quarterly check-in due");
      
      recs.push("Send: 'Time for your quarterly tune-up?'");
      recs.push("Offer seasonal promotion");
      recs.push("Remind about backup best practices");
    }

    // Critical repairs
    if (repairType === 'critical') {
      findings.push("Critical repair - enhanced follow-up");
      
      recs.push("Follow up at: 24h, 7d, 14d, 30d");
      recs.push("Monitor device health remotely (with permission)");
      recs.push("Proactive check-ins if issues predicted");
    }

    // General recommendations
    recs.push("Personalize messages with customer name");
    recs.push("Reference specific device and repair");
    recs.push("Keep emails short and scannable");
    recs.push("Always provide opt-out option");
    recs.push("Track engagement and adjust frequency");

    return this.resp(findings, recs, 0.96);
  }
}
