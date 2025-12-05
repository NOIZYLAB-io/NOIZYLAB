/**
 * 🛡️ THREAT MONITOR
 * AI security layer, anomaly detection
 * Fish Music Inc - CB_01
 */

export class ThreatMonitor {
  private threats: Array<any> = [];
  private blocklist: Set<string> = new Set();

  validateRequest(request: any): { safe: boolean; reason?: string } {
    console.log('🛡️ Validating request...');

    // Check for dangerous operations
    const dangerous = [
      'rm -rf',
      'format',
      'delete system',
      'erase disk',
      'drop database'
    ];

    const requestStr = JSON.stringify(request).toLowerCase();

    for (const danger of dangerous) {
      if (requestStr.includes(danger)) {
        console.log(`   🚨 Dangerous operation detected: ${danger}`);
        return {
          safe: false,
          reason: `Blocked dangerous operation: ${danger}`
        };
      }
    }

    // Check blocklist
    if (request.ip && this.blocklist.has(request.ip)) {
      return {
        safe: false,
        reason: 'IP on blocklist'
      };
    }

    console.log('   ✅ Request validated');
    return { safe: true };
  }

  detectAnomaly(metrics: any): { anomaly: boolean; details?: string } {
    // Detect unusual patterns
    if (metrics.cpu_usage > 95 && metrics.unknown_processes > 5) {
      return {
        anomaly: true,
        details: 'Possible cryptominer or malware'
      };
    }

    if (metrics.network_traffic > 1000000 && !metrics.expected_upload) {
      return {
        anomaly: true,
        details: 'Unusual network activity - possible data exfiltration'
      };
    }

    return { anomaly: false };
  }

  logThreat(threat: any) {
    this.threats.push({
      ...threat,
      timestamp: new Date().toISOString()
    });

    console.log('🚨 Threat logged:', threat.type);
  }

  block(identifier: string) {
    this.blocklist.add(identifier);
    console.log(`🚫 Blocked: ${identifier}`);
  }

  getThreats() {
    return this.threats;
  }
}

export const threatMonitor = new ThreatMonitor();

export const security = {
  init: () => {
    console.log('🛡️ Security Layer initialized');
  },
  validate: (req: any) => threatMonitor.validateRequest(req),
  detectAnomaly: (metrics: any) => threatMonitor.detectAnomaly(metrics),
  logThreat: (threat: any) => threatMonitor.logThreat(threat),
  block: (id: string) => threatMonitor.block(id)
};
