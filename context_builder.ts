/**
 * 🏗️ CONTEXT BUILDER
 * Builds unified context for all geniuses
 * Fish Music Inc - CB_01
 */

import { GeniusContext } from '../../geniuses/base/GeniusBase';

export function buildContext(raw: any): GeniusContext {
  return {
    device: {
      id: raw.device_id,
      name: raw.device_name || 'Unknown Device',
      type: raw.device_type || 'laptop',
      os: raw.os || 'Unknown OS',
      model: raw.model,
      serial: raw.serial
    },
    
    logs: {
      kernel_panics: raw.logs?.kernel_panics || 0,
      disk_errors: raw.logs?.disk_errors || 0,
      thermal_events: raw.logs?.thermal_events || 0,
      event_critical: raw.logs?.event_critical || 0,
      event_error: raw.logs?.event_error || 0,
      event_warning: raw.logs?.event_warning || 0,
      raw: raw.logs?.raw || ''
    },
    
    metrics: {
      cpu_temp: raw.metrics?.cpu_temp,
      cpu_usage: raw.metrics?.cpu_usage,
      ram_usage: raw.metrics?.ram_usage,
      ssd_life: raw.metrics?.ssd_life,
      disk_usage: raw.metrics?.disk_usage,
      disk_speed: raw.metrics?.disk_speed,
      gpu_temp: raw.metrics?.gpu_temp,
      latency: raw.metrics?.latency,
      packet_loss: raw.metrics?.packet_loss,
      battery_health: raw.metrics?.battery_health,
      processes: raw.metrics?.processes || [],
      issues: raw.metrics?.issues || [],
      repair_history: raw.metrics?.repair_history || [],
      
      // User context
      stress_level: raw.user?.stress_level,
      tech_knowledge: raw.user?.tech_knowledge || 'beginner',
      accessibility_needs: raw.user?.accessibility_needs || [],
      
      // Business context
      urgency: raw.urgency || 'normal',
      device_count: raw.device_count || 1,
      omega_enabled: raw.omega_enabled || false
    },
    
    session_id: raw.session_id,
    user_id: raw.user_id
  };
}

export function enrichContext(context: GeniusContext, additionalData: any): GeniusContext {
  return {
    ...context,
    metrics: {
      ...context.metrics,
      ...additionalData
    }
  };
}
