/**
 * NOIZY.AI AVATAR MODE COLORS
 * Maps operational modes to visual color states
 * SAFE: These are brand colors, not emotional indicators
 */

export const MODE_COLORS = {
  SAFE_AUTOPILOT: {
    primary: '#3B82F6',      // Blue
    secondary: '#1D4ED8',
    glow: '#60A5FA',
    pulse: 'slow',
    intensity: 0.6
  },
  TECHNICIAN_ASSIST: {
    primary: '#F59E0B',      // Amber
    secondary: '#D97706',
    glow: '#FBBF24',
    pulse: 'medium',
    intensity: 0.75
  },
  FULL_AUTOOPS: {
    primary: '#10B981',      // Green
    secondary: '#059669',
    glow: '#34D399',
    pulse: 'steady',
    intensity: 0.85
  }
};

export const STATE_COLORS = {
  idle: '#06B6D4',           // Teal
  thinking: '#8B5CF6',       // Purple shimmer
  processing: '#A78BFA',     // Light purple
  error: '#EF4444',          // Red
  success: '#FFFFFF',        // White pulse
  talking: '#60A5FA',        // Blue ripple
  standby: '#0D9488',        // Dim teal
  attention: '#F59E0B'       // Bright amber
};

export const LOAD_GRADIENTS = {
  cpu: ['#3B82F6', '#8B5CF6', '#EF4444'],  // Blue → Purple → Red
  gpu: ['#10B981', '#F59E0B', '#EF4444'],  // Green → Amber → Red
  network: ['#06B6D4', '#3B82F6', '#8B5CF6'] // Teal → Blue → Purple
};

export function getModeColor(mode) {
  return MODE_COLORS[mode] || MODE_COLORS.SAFE_AUTOPILOT;
}

export function getLoadColor(type, percentage) {
  const gradient = LOAD_GRADIENTS[type] || LOAD_GRADIENTS.cpu;
  if (percentage < 50) return gradient[0];
  if (percentage < 80) return gradient[1];
  return gradient[2];
}

