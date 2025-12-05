/**
 * 🌐 CROSS-SYSTEM GENIUS
 * Multi-platform orchestrator, OS translator
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class CrossSystemGenius extends GeniusBase {
  name = "CrossSystemGenius";
  squad = "intelligence";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const osType = context.device?.os || 'unknown';
    const hasMultipleDevices = context.metrics?.device_count > 1;

    findings.push("Cross-platform compatibility check");
    findings.push(`Primary OS: ${osType}`);

    // Multi-device scenarios
    if (hasMultipleDevices) {
      findings.push("User has multiple devices");
      
      recs.push("Sync settings and preferences across devices");
      recs.push("Unified health dashboard for all devices");
      recs.push("Cross-platform file sharing recommendations");
      recs.push("Suggest cloud sync (iCloud, OneDrive, Syncthing)");
    }

    // macOS ↔ Windows translation
    if (osType.includes('mac')) {
      findings.push("macOS-specific optimizations");
      
      recs.push("macOS cleanup paths:");
      recs.push("  • ~/Library/Caches");
      recs.push("  • ~/Library/Logs");
      recs.push("  • ~/.Trash");
      recs.push("Translate to Windows equivalents when needed");
    }

    if (osType.includes('Windows')) {
      findings.push("Windows-specific optimizations");
      
      recs.push("Windows cleanup paths:");
      recs.push("  • %TEMP%");
      recs.push("  • C:\\Windows\\Temp");
      recs.push("  • Recycle Bin");
      recs.push("Translate to macOS equivalents when needed");
    }

    // Linux support
    if (osType.includes('Linux') || osType.includes('Ubuntu')) {
      findings.push("Linux-specific optimizations");
      
      recs.push("Linux cleanup:");
      recs.push("  • apt clean / yum clean");
      recs.push("  • ~/.cache");
      recs.push("  • /var/log (if permitted)");
    }

    // Normalize metrics
    recs.push("Normalize metrics across OS types:");
    recs.push("  • CPU % (universal)");
    recs.push("  • RAM % (universal)");
    recs.push("  • Disk % (universal)");
    recs.push("  • Temp °C (universal)");

    // Bridge GABRIEL ↔ OMEN
    if (context.metrics?.omega_enabled) {
      findings.push("OMEGA BRAIN integration active");
      
      recs.push("Coordinate Mac (GABRIEL) ↔ Windows (OMEN)");
      recs.push("Use SMB for file sharing");
      recs.push("Use SSH for remote commands");
      recs.push("Use Ray for distributed compute");
      recs.push("Use Redis for shared memory");
    }

    return this.resp(findings, recs, 0.94);
  }
}
