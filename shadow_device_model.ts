/**
 * 👻 SHADOW DEVICE MODEL
 * Creates virtual device model for safe simulation
 * Fish Music Inc - CB_01
 */

export interface ShadowDevice {
  cpu: number;
  temp: number;
  storage: number;
  health: number;
  predict: () => string;
  simulate: (action: string) => SimulationResult;
}

export interface SimulationResult {
  action: string;
  predicted_outcome: string;
  risk_level: 'safe' | 'caution' | 'dangerous';
  proceed: boolean;
}

export function shadowModel(context: any): ShadowDevice {
  const metrics = context.metrics || {};
  
  return {
    cpu: metrics.cpu_usage || 0,
    temp: metrics.cpu_temp || 40,
    storage: metrics.disk_usage || 50,
    health: metrics.ssd_life || 100,
    
    predict: function() {
      if (this.temp > 90) return 'overheat_imminent';
      if (this.health < 40) return 'drive_failure_imminent';
      if (this.storage > 95) return 'out_of_space_imminent';
      return 'stable';
    },
    
    simulate: function(action: string): SimulationResult {
      // Simulate action outcome
      const risk = this.assessRisk(action);
      
      return {
        action,
        predicted_outcome: risk.outcome,
        risk_level: risk.level,
        proceed: risk.level !== 'dangerous'
      };
    }
  };
}

function assessRisk(action: string): { outcome: string; level: 'safe' | 'caution' | 'dangerous' } {
  const lower = action.toLowerCase();
  
  // Dangerous actions
  if (lower.includes('delete') || lower.includes('format') || lower.includes('erase')) {
    return {
      outcome: 'Data loss possible',
      level: 'dangerous'
    };
  }
  
  // Caution actions
  if (lower.includes('update') || lower.includes('modify') || lower.includes('change')) {
    return {
      outcome: 'May require restart or reconfiguration',
      level: 'caution'
    };
  }
  
  // Safe actions
  return {
    outcome: 'No risk detected',
    level: 'safe'
  };
}
