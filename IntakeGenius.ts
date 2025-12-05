/**
 * 📋 INTAKE GENIUS
 * Pre-session info collector, friction reducer
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class IntakeGenius extends GeniusBase {
  name = "IntakeGenius";
  squad = "business";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    findings.push("Pre-session intake initiated");

    // Auto-collect device info
    recs.push("Auto-detect and pre-populate:");
    recs.push("  • Device model and specs");
    recs.push("  • OS version");
    recs.push("  • Serial number");
    recs.push("  • Current storage/RAM usage");
    recs.push("  • Network config");

    // Minimal questions
    recs.push("Ask ONLY essential questions:");
    recs.push("  1. What problem are you experiencing?");
    recs.push("  2. When did it start?");
    recs.push("  3. What changed recently? (optional)");

    // Smart pre-fill
    recs.push("Use AI to suggest common issues based on symptoms");
    recs.push("Example: 'Slow startup' → auto-check startup items");

    // Reduce friction
    recs.push("Keep intake under 2 minutes");
    recs.push("Allow 'Skip' for non-critical fields");
    recs.push("Save progress automatically");
    recs.push("Enable voice input for accessibility");

    // Session prep
    recs.push("Pre-populate technician notes");
    recs.push("Run preliminary diagnostic in background");
    recs.push("Have likely fixes ready");

    return this.resp(findings, recs, 0.95);
  }
}
