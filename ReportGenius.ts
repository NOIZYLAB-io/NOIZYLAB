/**
 * 📊 REPORT GENIUS
 * The storyteller, summarizer, report beautifier
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class ReportGenius extends GeniusBase {
  name = "ReportGenius";
  squad = "experience";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const reportType = context.metrics?.report_type || 'standard';

    findings.push(`Report generation requested: ${reportType}`);

    // Standard report
    if (reportType === 'standard') {
      recs.push("Include: Device info, before/after scores, fixes performed");
      recs.push("Use clear sections with visual separation");
      recs.push("Highlight key improvements in bold");
      recs.push("Add recommendations section");
      recs.push("Include next scan date");
    }

    // Executive summary
    if (reportType === 'executive') {
      recs.push("Lead with bottom line: 'Device is healthy' or 'Action required'");
      recs.push("Use bullet points, not paragraphs");
      recs.push("Include only critical info");
      recs.push("Make it scannable in 30 seconds");
    }

    // Technical deep-dive
    if (reportType === 'technical') {
      recs.push("Include full logs, metrics, and raw data");
      recs.push("Show detailed before/after comparisons");
      recs.push("List all commands executed");
      recs.push("Provide troubleshooting appendix");
    }

    // Visual formatting
    recs.push("Use Noizy.AI brand colors (Gold, Violet, Teal)");
    recs.push("Add health score visualization");
    recs.push("Make report shareable (PDF + link)");
    recs.push("End with: '🔥 GORUNFREE! 🎸🔥'");

    return this.resp(findings, recs, 0.96);
  }
}
