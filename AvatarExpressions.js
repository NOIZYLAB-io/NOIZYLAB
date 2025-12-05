/**
 * NOIZY.AI AVATAR EXPRESSIONS
 * Data-driven shader states for holographic representation
 * SAFE: These are visual effects, not emotions
 */

export const EXPRESSIONS = {
  idle: {
    name: 'idle',
    description: 'Calm standby state',
    shader: {
      gradient: 'soft-blue',
      pulse: { speed: 0.5, amplitude: 0.1 },
      glow: { intensity: 0.4, spread: 2.0 },
      geometry: { jitter: 0, scale: 1.0 }
    },
    animation: {
      duration: 3000,
      easing: 'ease-in-out',
      loop: true
    }
  },

  thinking: {
    name: 'thinking',
    description: 'Processing input',
    shader: {
      gradient: 'purple-shimmer',
      pulse: { speed: 1.2, amplitude: 0.15 },
      glow: { intensity: 0.6, spread: 3.0 },
      geometry: { jitter: 0.02, scale: 1.02 }
    },
    animation: {
      duration: 800,
      easing: 'linear',
      loop: true
    }
  },

  processing: {
    name: 'processing',
    description: 'Executing task',
    shader: {
      gradient: 'edge-shimmer',
      pulse: { speed: 2.0, amplitude: 0.2 },
      glow: { intensity: 0.8, spread: 4.0 },
      geometry: { jitter: 0.01, scale: 1.05 }
    },
    animation: {
      duration: 500,
      easing: 'linear',
      loop: true
    }
  },

  error: {
    name: 'error',
    description: 'Error state',
    shader: {
      gradient: 'red-alert',
      pulse: { speed: 0.3, amplitude: 0.3 },
      glow: { intensity: 0.9, spread: 5.0 },
      geometry: { jitter: 0.03, scale: 0.98 }
    },
    animation: {
      duration: 2000,
      easing: 'ease-out',
      loop: true
    }
  },

  success: {
    name: 'success',
    description: 'Task completed',
    shader: {
      gradient: 'white-pulse',
      pulse: { speed: 0.8, amplitude: 0.4 },
      glow: { intensity: 1.0, spread: 6.0 },
      geometry: { jitter: 0, scale: 1.1 }
    },
    animation: {
      duration: 1500,
      easing: 'ease-out',
      loop: false
    }
  },

  talking: {
    name: 'talking',
    description: 'Audio output active',
    shader: {
      gradient: 'blue-ripple',
      pulse: { speed: 1.5, amplitude: 0.25 },
      glow: { intensity: 0.7, spread: 3.5 },
      geometry: { jitter: 0.01, scale: 1.03 },
      ripple: { enabled: true, rings: 3, speed: 1.2 }
    },
    animation: {
      duration: 400,
      easing: 'linear',
      loop: true
    }
  },

  standby: {
    name: 'standby',
    description: 'Low power state',
    shader: {
      gradient: 'dim-teal',
      pulse: { speed: 0.2, amplitude: 0.05 },
      glow: { intensity: 0.2, spread: 1.0 },
      geometry: { jitter: 0, scale: 0.95 }
    },
    animation: {
      duration: 5000,
      easing: 'ease-in-out',
      loop: true
    }
  },

  attention: {
    name: 'attention',
    description: 'User addressed system',
    shader: {
      gradient: 'amber-spike',
      pulse: { speed: 2.5, amplitude: 0.35 },
      glow: { intensity: 0.95, spread: 5.0 },
      geometry: { jitter: 0.02, scale: 1.08 }
    },
    animation: {
      duration: 300,
      easing: 'ease-out',
      loop: false
    }
  }
};

export function getExpression(name) {
  return EXPRESSIONS[name] || EXPRESSIONS.idle;
}

export function blendExpressions(from, to, progress) {
  const fromExp = getExpression(from);
  const toExp = getExpression(to);
  
  return {
    shader: {
      pulse: {
        speed: lerp(fromExp.shader.pulse.speed, toExp.shader.pulse.speed, progress),
        amplitude: lerp(fromExp.shader.pulse.amplitude, toExp.shader.pulse.amplitude, progress)
      },
      glow: {
        intensity: lerp(fromExp.shader.glow.intensity, toExp.shader.glow.intensity, progress),
        spread: lerp(fromExp.shader.glow.spread, toExp.shader.glow.spread, progress)
      },
      geometry: {
        jitter: lerp(fromExp.shader.geometry.jitter, toExp.shader.geometry.jitter, progress),
        scale: lerp(fromExp.shader.geometry.scale, toExp.shader.geometry.scale, progress)
      }
    }
  };
}

function lerp(a, b, t) {
  return a + (b - a) * t;
}

