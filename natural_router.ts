/**
 * 🗣️ NATURAL LANGUAGE ROUTER
 * Routes user input to appropriate geniuses
 * Fish Music Inc - CB_01
 */

export function naturalRoute(input: string): string[] {
  const lower = input.toLowerCase();
  const geniuses: string[] = [];

  // Performance keywords
  if (lower.includes("slow") || lower.includes("lag") || lower.includes("freeze")) {
    geniuses.push("PerformanceGenius", "ProcessGenius");
  }

  // Temperature keywords
  if (lower.includes("hot") || lower.includes("heat") || lower.includes("fan")) {
    geniuses.push("ThermalGenius", "HardwareGenius");
  }

  // Network keywords
  if (lower.includes("internet") || lower.includes("wifi") || lower.includes("network") || lower.includes("connection")) {
    geniuses.push("NetworkGenius");
  }

  // Storage keywords
  if (lower.includes("storage") || lower.includes("disk") || lower.includes("full") || lower.includes("space")) {
    geniuses.push("StorageGenius");
  }

  // Error/crash keywords
  if (lower.includes("error") || lower.includes("crash") || lower.includes("blue screen") || lower.includes("panic")) {
    geniuses.push("MacRepairGenius", "WindowsRepairGenius", "PatternGenius");
  }

  // Malware keywords
  if (lower.includes("virus") || lower.includes("malware") || lower.includes("suspicious") || lower.includes("hack")) {
    geniuses.push("MalwareGenius");
  }

  // Backup keywords
  if (lower.includes("backup") || lower.includes("lost") || lower.includes("recover")) {
    geniuses.push("StorageGenius", "AutomationGenius");
  }

  // Price keywords
  if (lower.includes("cost") || lower.includes("price") || lower.includes("quote") || lower.includes("how much")) {
    geniuses.push("PricingGenius");
  }

  // General help
  if (geniuses.length === 0) {
    geniuses.push("SupportGenius", "CalmGenius");
  }

  // Always add OmegaCore for coordination
  geniuses.push("OmegaCoreGenius");

  // Remove duplicates
  return Array.from(new Set(geniuses));
}
