/**
 * 🍎 MAC REPAIR GENIUS
 * Specialist in macOS diagnostics & repair
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class MacRepairGenius extends GeniusBase {
  name = "MacRepairGenius";
  squad = "diagnosis";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const logs = context.logs || {};

    // Kernel panics
    if (logs.kernel_panics && logs.kernel_panics > 0) {
      findings.push(`Detected ${logs.kernel_panics} kernel panics`);
      recs.push("Run Disk Utility First Aid");
      recs.push("Reset NVRAM: Reboot + hold Option+Cmd+P+R");
      recs.push("Reset SMC: Shutdown, hold power 10s");
      recs.push("Check for problematic kernel extensions");
    }

    // Disk errors
    if (logs.disk_errors && logs.disk_errors > 0) {
      findings.push(`${logs.disk_errors} disk I/O errors found`);
      recs.push("BACKUP IMMEDIATELY - disk integrity failing");
      recs.push("Run: diskutil verifyVolume /");
      recs.push("Consider drive replacement");
    }

    // Thermal events
    if (logs.thermal_events && logs.thermal_events > 10) {
      findings.push("Excessive thermal throttling events");
      recs.push("Clean dust from vents");
      recs.push("Check ambient temperature");
      recs.push("Reset SMC for fan control");
    }

    // No issues found
    if (findings.length === 0) {
      findings.push("macOS health: Excellent");
      recs.push("System operating normally");
      recs.push("Continue regular maintenance");
    }

    return this.resp(findings, recs, 0.92);
  }
}
