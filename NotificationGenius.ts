/**
 * 🔔 NOTIFICATION GENIUS
 * The communicator, timing strategist, notification optimizer
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class NotificationGenius extends GeniusBase {
  name = "NotificationGenius";
  squad = "experience";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const notifType = context.metrics?.notification_type || 'general';
    const userPrefs = context.metrics?.notification_prefs || {};

    findings.push(`Notification type: ${notifType}`);

    // Critical alerts
    if (notifType === 'critical') {
      findings.push("Critical alert - immediate notification required");
      
      recs.push("Send immediately via all channels");
      recs.push("Use urgent but not scary language");
      recs.push("Example: '⚠️ Important: Your data needs backup now'");
      recs.push("Provide clear action button");
      recs.push("Follow up if not acknowledged in 1 hour");
    }

    // Progress updates
    if (notifType === 'progress') {
      findings.push("Session progress update");
      
      recs.push("Send every 25% progress increment");
      recs.push("Keep messages brief: 'Repair 50% complete'");
      recs.push("Include ETA");
      recs.push("Don't spam - max 4-5 updates per session");
    }

    // Completion
    if (notifType === 'completion') {
      findings.push("Task completed notification");
      
      recs.push("Celebrate the win: '✅ All done!'");
      recs.push("Summarize what was fixed");
      recs.push("Provide next steps");
      recs.push("Include link to full report");
    }

    // Recommendations
    if (notifType === 'recommendation') {
      findings.push("Suggestion/recommendation notification");
      
      recs.push("Make it helpful, not salesy");
      recs.push("Example: '💡 Pro tip: Weekly restarts keep your Mac happy'");
      recs.push("Allow easy dismiss");
      recs.push("Limit to 1 recommendation per week");
    }

    // Respect preferences
    if (userPrefs.email_only) {
      recs.push("Send via email only (no push/SMS)");
    }
    
    if (userPrefs.quiet_hours) {
      recs.push("Respect quiet hours: no notifications 10PM-8AM");
    }

    return this.resp(findings, recs, 0.93);
  }
}
