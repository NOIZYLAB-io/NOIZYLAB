/**
 * 🧭 GENIUS ROUTER
 * Routes requests to appropriate genius squads
 * Fish Music Inc - CB_01
 */

export interface RouteRequest {
  type: 'mac' | 'windows' | 'linux' | 'unknown';
  symptoms: string[];
  urgency: 'low' | 'normal' | 'high' | 'emergency';
  category?: string;
}

export function routeToGeniuses(request: RouteRequest): string[] {
  const geniuses: string[] = [];

  // OS-specific
  if (request.type === 'mac') {
    geniuses.push('MacRepairGenius');
  }
  if (request.type === 'windows') {
    geniuses.push('WindowsRepairGenius');
  }
  if (request.type === 'linux') {
    geniuses.push('LinuxGenius');
  }

  // Symptom-based routing
  if (request.symptoms.includes('heat') || request.symptoms.includes('thermal')) {
    geniuses.push('ThermalGenius', 'HardwareGenius');
  }

  if (request.symptoms.includes('slow') || request.symptoms.includes('lag')) {
    geniuses.push('PerformanceGenius', 'ProcessGenius', 'StorageGenius');
  }

  if (request.symptoms.includes('network') || request.symptoms.includes('internet')) {
    geniuses.push('NetworkGenius');
  }

  if (request.symptoms.includes('malware') || request.symptoms.includes('virus')) {
    geniuses.push('MalwareGenius');
  }

  if (request.symptoms.includes('crash') || request.symptoms.includes('error')) {
    geniuses.push('PatternGenius');
  }

  if (request.symptoms.includes('storage') || request.symptoms.includes('full')) {
    geniuses.push('StorageGenius');
  }

  // Urgency-based additions
  if (request.urgency === 'emergency' || request.urgency === 'high') {
    geniuses.push('ForesightGenius');  // Check for imminent failures
    geniuses.push('CalmGenius');       // Keep user calm
  }

  // Category-based
  if (request.category === 'business') {
    geniuses.push('PricingGenius', 'SchedulingGenius');
  }

  if (request.category === 'support') {
    geniuses.push('SupportGenius', 'AccessibilityGenius');
  }

  // Always include OmegaCore
  geniuses.push('OmegaCoreGenius');

  // Remove duplicates and return
  return Array.from(new Set(geniuses));
}
