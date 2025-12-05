/**
 * 🌡️ THERMAL GENIUS
 * Specialist in cooling & temperature management
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class ThermalGenius extends GeniusBase {
  name = "ThermalGenius";
  squad = "optimization";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];
    const m = context.metrics || {};

    // CPU temperature
    if (m.cpu_temp > 95) {
      findings.push(`🔥 CRITICAL CPU temp: ${m.cpu_temp}°C`);
      recs.push("SHUTDOWN IMMEDIATELY to prevent damage");
      recs.push("Clean cooling system thoroughly");
      recs.push("Replace thermal paste");
      recs.push("Check fan operation");
    } else if (m.cpu_temp > 85) {
      findings.push(`High CPU temperature: ${m.cpu_temp}°C`);
      recs.push("Clean dust from vents and fans");
      recs.push("Improve case airflow");
      recs.push("Consider reapplying thermal paste");
    } else if (m.cpu_temp > 70) {
      findings.push(`Elevated CPU temp: ${m.cpu_temp}°C`);
      recs.push("Monitor during heavy workloads");
      recs.push("Ensure vents are unobstructed");
    }

    // GPU temperature
    if (m.gpu_temp && m.gpu_temp > 85) {
      findings.push(`High GPU temperature: ${m.gpu_temp}°C`);
      recs.push("Clean GPU fans and heatsink");
      recs.push("Adjust fan curve in GPU settings");
      recs.push("Check thermal pad condition");
      recs.push("Improve case ventilation");
    }

    // System temperature
    if (m.system_temp && m.system_temp > 70) {
      findings.push(`Elevated system temp: ${m.system_temp}°C`);
      recs.push("Check ambient room temperature");
      recs.push("Ensure proper ventilation");
      recs.push("Clean all fans and vents");
    }

    // Thermal throttling
    if (m.thermal_throttling && m.thermal_throttling > 0) {
      findings.push(`Thermal throttling detected: ${m.thermal_throttling} events`);
      recs.push("System reducing performance to cool down");
      recs.push("Address cooling issues immediately");
      recs.push("Check for dust buildup");
    }

    // Optimal temperatures
    if (findings.length === 0) {
      findings.push("Thermal: Optimal");
      findings.push(`CPU: ${m.cpu_temp || 'N/A'}°C`);
      if (m.gpu_temp) findings.push(`GPU: ${m.gpu_temp}°C`);
      recs.push("Cooling system working well");
    }

    return this.resp(findings, recs, 0.91);
  }
}
