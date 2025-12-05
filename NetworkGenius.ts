/**
 * 🌐 NETWORK GENIUS
 * Specialist in network optimization & troubleshooting
 * Fish Music Inc - CB_01
 */

import { GeniusBase, GeniusContext } from '../base/GeniusBase';

export class NetworkGenius extends GeniusBase {
  name = "NetworkGenius";
  squad = "optimization";

  analyze(context: GeniusContext) {
    const findings: string[] = [];
    const recs: string[] = [];
    const m = context.metrics || {};

    // High latency
    if (m.latency > 100) {
      findings.push(`High latency detected: ${m.latency}ms`);
      recs.push("Check router placement and distance");
      recs.push("Look for Wi-Fi interference");
      recs.push("Try different Wi-Fi channel");
      recs.push("Consider wired connection");
    }

    // Packet loss
    if (m.packet_loss > 2) {
      findings.push(`Packet loss: ${m.packet_loss}%`);
      recs.push("Inspect ethernet cables for damage");
      recs.push("Update router firmware");
      recs.push("Contact ISP if persistent");
      recs.push("Check for network congestion");
    }

    // Jitter
    if (m.jitter > 30) {
      findings.push(`Excessive jitter: ${m.jitter}ms`);
      recs.push("Stabilize Wi-Fi signal");
      recs.push("Switch to wired connection");
      recs.push("Reduce network load");
      recs.push("Enable QoS on router");
    }

    // DNS issues
    if (m.dns_resolution_time && m.dns_resolution_time > 200) {
      findings.push("Slow DNS resolution");
      recs.push("Change DNS to 1.1.1.1 or 8.8.8.8");
      recs.push("Flush DNS cache");
      recs.push("Check router DNS settings");
    }

    // Optimal
    if (findings.length === 0) {
      findings.push("Network: Excellent");
      findings.push(`Latency: ${m.latency || 'N/A'}ms`);
      recs.push("Network performing well");
    }

    return this.resp(findings, recs, 0.89);
  }
}
