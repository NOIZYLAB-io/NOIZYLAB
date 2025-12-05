/**
 * 🔄 PROCESS GENIUS
 * Specialist in process management & optimization
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class ProcessGenius extends GeniusBase {
  name = "ProcessGenius";
  squad = "optimization";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const processes = context.metrics?.processes || [];

    // CPU hogs
    const cpuHogs = processes.filter(p => p.cpu > 50);
    if (cpuHogs.length > 0) {
      findings.push(`${cpuHogs.length} CPU-intensive processes detected`);
      cpuHogs.forEach(p => {
        findings.push(`  • ${p.name}: ${p.cpu}% CPU`);
      });
      recs.push("Terminate unnecessary high-CPU processes");
      recs.push("Check for runaway background tasks");
      recs.push("Investigate resource leaks");
    }

    // Memory hogs
    const memoryHogs = processes.filter(p => p.memory > 500);
    if (memoryHogs.length > 0) {
      findings.push(`${memoryHogs.length} memory-heavy processes`);
      memoryHogs.forEach(p => {
        findings.push(`  • ${p.name}: ${p.memory}MB RAM`);
      });
      recs.push("Close memory-intensive applications");
      recs.push("Check for memory leaks");
      recs.push("Restart problematic apps");
    }

    // Startup bloat
    const startupCount = context.metrics?.startup_items || 0;
    if (startupCount > 10) {
      findings.push(`${startupCount} startup items detected`);
      recs.push("Disable unnecessary startup programs");
      recs.push("Mac: System Settings → Users → Login Items");
      recs.push("Windows: Task Manager → Startup");
    }

    // Zombie processes
    const zombies = processes.filter(p => p.state === 'zombie' || p.cpu === 0 && p.memory > 100);
    if (zombies.length > 0) {
      findings.push(`${zombies.length} zombie/hung processes`);
      recs.push("Force quit unresponsive apps");
      recs.push("Restart system if persistent");
    }

    // All good
    if (findings.length === 0) {
      findings.push("Process management: Optimal");
      findings.push(`${processes.length} processes running normally`);
      recs.push("No process issues detected");
    }

    return this.resp(findings, recs, 0.94);
  }
}
