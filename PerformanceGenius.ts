/**
 * ⚡ PERFORMANCE GENIUS
 * Specialist in system optimization & speed
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class PerformanceGenius extends GeniusBase {
  name = "PerformanceGenius";
  squad = "optimization";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];
    const m = context.metrics || {};

    // RAM pressure
    if (m.ram_usage > 85) {
      findings.push(`High memory usage: ${m.ram_usage}%`);
      recs.push("Close resource-heavy applications");
      recs.push("Reduce browser tabs");
      recs.push("Disable unnecessary startup items");
      recs.push("Consider RAM upgrade if persistent");
    }

    // CPU load
    if (m.cpu_usage > 90) {
      findings.push(`CPU maxed out: ${m.cpu_usage}%`);
      recs.push("Identify CPU-hogging processes");
      recs.push("Check for runaway background tasks");
      recs.push("Optimize scheduled tasks");
    }

    // Disk usage
    if (m.disk_usage > 90) {
      findings.push(`Disk nearly full: ${m.disk_usage}%`);
      recs.push("Clear cache: ~/Library/Caches (Mac) or %TEMP% (Windows)");
      recs.push("Remove unused applications");
      recs.push("Move large files to external storage");
      recs.push("Empty trash/recycle bin");
    }

    // Slow disk
    if (m.disk_speed && m.disk_speed < 200) {
      findings.push(`Slow disk performance: ${m.disk_speed}MB/s`);
      recs.push("Check for disk fragmentation (Windows)");
      recs.push("Run TRIM optimization (SSD)");
      recs.push("Scan for failing sectors");
    }

    // Optimal state
    if (findings.length === 0) {
      findings.push("Performance: Optimal");
      recs.push("System running efficiently");
      recs.push("No optimization needed");
    }

    return this.resp(findings, recs, 0.93);
  }
}
