/**
 * 👥 CRM GENIUS
 * Customer relationship manager, memory keeper
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class CRMGenius extends GeniusBase {
  name = "CRMGenius";
  squad = "business";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const customerHistory = context.metrics?.customer_history || {};
    const previousSessions = customerHistory.sessions || 0;
    const lastVisit = customerHistory.last_visit || null;
    const totalSpent = customerHistory.total_spent || 0;

    findings.push(`Customer profile accessed`);
    findings.push(`Previous sessions: ${previousSessions}`);

    // First-time customer
    if (previousSessions === 0) {
      findings.push("First-time customer");
      
      recs.push("Extra friendly greeting: 'Welcome to Noizy.AI!'");
      recs.push("Explain process clearly");
      recs.push("Set expectations properly");
      recs.push("Follow up within 48 hours");
      recs.push("Ask for feedback");
    }

    // Returning customer
    if (previousSessions > 0) {
      findings.push("Returning customer");
      
      recs.push(`Personalized greeting: 'Welcome back, ${context.user_id}!'`);
      recs.push("Reference past repairs if relevant");
      recs.push("Show device history");
      recs.push("Highlight improvements since last visit");
    }

    // VIP customer
    if (previousSessions > 5 || totalSpent > 500) {
      findings.push("VIP customer detected");
      
      recs.push("Priority treatment");
      recs.push("Offer loyalty discount (10%)");
      recs.push("Thank them for continued trust");
      recs.push("Provide direct tech contact");
    }

    // Persistent issues
    if (customerHistory.recurring_issues?.length > 0) {
      findings.push("Recurring issues detected");
      
      recs.push("Proactively address known problem areas");
      recs.push("Suggest permanent solutions");
      recs.push("Offer preventive maintenance package");
    }

    // General CRM
    recs.push("Update customer profile with latest interaction");
    recs.push("Track satisfaction score");
    recs.push("Note preferences (communication style, urgency, etc.)");

    return this.resp(findings, recs, 0.92);
  }
}
