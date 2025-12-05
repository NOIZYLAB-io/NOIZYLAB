/**
 * ⚙️ HARDWARE GENIUS
 * Specialist in hardware diagnostics
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class HardwareGenius extends GeniusBase {
  name = "HardwareGenius";
  squad = "diagnosis";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const m = context.metrics || {};

    // CPU temperature
    if (m.cpu_temp > 85) {
      findings.push(`High CPU temperature: ${m.cpu_temp}°C`);
      recs.push("Clean dust from cooling system");
      recs.push("Check thermal paste condition");
      recs.push("Verify fan operation");
      recs.push("Improve case airflow");
    }

    // SSD health
    if (m.ssd_life < 60) {
      findings.push(`SSD wear: ${m.ssd_life}% life remaining`);
      recs.push("⚠️  BACKUP NOW - drive degrading");
      recs.push("Plan SSD replacement");
      recs.push("Monitor SMART status weekly");
    }

    // RAM pressure
    if (m.ram_usage > 90) {
      findings.push(`RAM at critical pressure: ${m.ram_usage}%`);
      recs.push("Close unnecessary applications");
      recs.push("Check for memory leaks");
      recs.push("Consider RAM upgrade if persistent");
    }

    // GPU temperature
    if (m.gpu_temp && m.gpu_temp > 80) {
      findings.push(`GPU running hot: ${m.gpu_temp}°C`);
      recs.push("Clean GPU fans");
      recs.push("Adjust fan curve");
      recs.push("Check GPU thermal pads");
    }

    // Battery health (laptops)
    if (m.battery_health && m.battery_health < 80) {
      findings.push(`Battery degraded: ${m.battery_health}% health`);
      recs.push("Battery replacement recommended");
      recs.push("Use optimized charging if available");
    }

    // All clear
    if (findings.length === 0) {
      findings.push("Hardware health: Excellent");
      recs.push("All components operating normally");
    }

    return this.resp(findings, recs, 0.94);
  }
}
