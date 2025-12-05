/**
 * 💾 STORAGE GENIUS
 * Specialist in disk health & storage optimization
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class StorageGenius extends GeniusBase {
  name = "StorageGenius";
  squad = "optimization";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];
    const m = context.metrics || {};

    // SSD wear
    if (m.ssd_life < 50) {
      findings.push(`🚨 SSD wear critical: ${m.ssd_life}% life remaining`);
      recs.push("BACKUP IMMEDIATELY");
      recs.push("Replace SSD within 30 days");
      recs.push("Monitor SMART status daily");
    } else if (m.ssd_life < 70) {
      findings.push(`SSD aging: ${m.ssd_life}% life remaining`);
      recs.push("Backup important data");
      recs.push("Plan replacement in 3-6 months");
    }

    // Storage capacity
    if (m.disk_usage > 95) {
      findings.push(`Disk critical: ${m.disk_usage}% full`);
      recs.push("Free space IMMEDIATELY");
      recs.push("System may become unstable");
    } else if (m.disk_usage > 85) {
      findings.push(`Disk filling up: ${m.disk_usage}% used`);
      recs.push("Clear cache files (~8GB typical)");
      recs.push("Remove unused apps");
      recs.push("Move large files to external drive");
    }

    // Slow disk
    if (m.disk_speed && m.disk_speed < 200) {
      findings.push(`Slow disk I/O: ${m.disk_speed}MB/s`);
      recs.push("Check for fragmentation (HDD)");
      recs.push("Run TRIM optimization (SSD)");
      recs.push("Scan for bad sectors");
      recs.push("Consider SSD upgrade if HDD");
    }

    // SMART errors
    if (m.smart_errors && m.smart_errors > 0) {
      findings.push(`${m.smart_errors} SMART errors detected`);
      recs.push("⚠️  Drive failure imminent");
      recs.push("Backup and replace ASAP");
    }

    // Healthy
    if (findings.length === 0) {
      findings.push("Storage: Healthy");
      findings.push(`Capacity: ${m.disk_usage || 'N/A'}% used`);
      findings.push(`SSD life: ${m.ssd_life || 'N/A'}%`);
      recs.push("Regular backups recommended");
    }

    return this.resp(findings, recs, 0.96);
  }
}
