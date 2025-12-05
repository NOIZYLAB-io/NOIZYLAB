/**
 * 🐧 LINUX GENIUS
 * Specialist in Linux/Unix diagnostics
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class LinuxGenius extends GeniusBase {
  name = "LinuxGenius";
  squad = "diagnosis";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];

    const logs = context.logs || {};

    // Journalctl errors
    if (logs.journal_errors > 0) {
      findings.push(`${logs.journal_errors} errors in system journal`);
      recs.push("Check: journalctl -p err -b");
      recs.push("Investigate failed services");
      recs.push("Review systemd unit status");
    }

    // Kernel OOPS
    if (logs.kernel_oops > 0) {
      findings.push("Kernel OOPS events detected");
      recs.push("Check dmesg for kernel errors");
      recs.push("Update kernel to latest stable");
      recs.push("Investigate problematic drivers");
    }

    // Service failures
    if (logs.failed_services && logs.failed_services.length > 0) {
      findings.push(`${logs.failed_services.length} failed services`);
      recs.push("Run: systemctl status <service>");
      recs.push("Check service dependencies");
      recs.push("Review service logs");
    }

    // Disk issues
    if (logs.disk_smart_errors > 0) {
      findings.push("SMART errors detected on disk");
      recs.push("Run: smartctl -a /dev/sda");
      recs.push("Backup critical data");
      recs.push("Plan disk replacement");
    }

    // All clear
    if (findings.length === 0) {
      findings.push("Linux system: Healthy");
      recs.push("Services running normally");
    }

    return this.resp(findings, recs, 0.91);
  }
}
