/**
 * NOIZY.AI AVATAR MATERIALS
 * Shader definitions for holographic appearance
 * SAFE: Visual styling only, no behavioral implications
 */

export const MATERIAL_PRESETS = {
  // Core holographic body
  holoCore: {
    type: 'holographic',
    baseColor: [0.2, 0.6, 1.0],
    opacity: 0.85,
    emissive: true,
    emissiveIntensity: 0.4,
    scanlines: true,
    scanlineSpeed: 0.5,
    fresnelPower: 2.0,
    noiseScale: 0.1
  },

  // Metallic light ribbons
  lightRibbon: {
    type: 'ribbon',
    baseColor: [0.8, 0.9, 1.0],
    opacity: 0.9,
    emissive: true,
    emissiveIntensity: 0.8,
    flowSpeed: 1.2,
    width: 0.02,
    glow: true
  },

  // Pulsating geometry edges
  geometryEdge: {
    type: 'edge',
    baseColor: [0.4, 0.8, 1.0],
    opacity: 1.0,
    emissive: true,
    emissiveIntensity: 1.0,
    pulseSpeed: 1.0,
    thickness: 0.005
  },

  // Volumetric fog effect
  volumeFog: {
    type: 'volumetric',
    baseColor: [0.3, 0.5, 0.8],
    opacity: 0.15,
    density: 0.3,
    falloff: 2.0,
    animated: true,
    animSpeed: 0.2
  },

  // Grid pattern overlay
  gridOverlay: {
    type: 'grid',
    baseColor: [0.5, 0.7, 1.0],
    opacity: 0.3,
    gridSize: 0.1,
    lineWidth: 0.002,
    animated: true,
    scrollSpeed: 0.1
  },

  // Error state material
  errorPulse: {
    type: 'holographic',
    baseColor: [1.0, 0.2, 0.2],
    opacity: 0.9,
    emissive: true,
    emissiveIntensity: 0.7,
    pulseSpeed: 0.3,
    pulseAmplitude: 0.3
  },

  // Success flash material
  successFlash: {
    type: 'flash',
    baseColor: [1.0, 1.0, 1.0],
    opacity: 1.0,
    emissive: true,
    emissiveIntensity: 1.5,
    fadeSpeed: 0.8
  }
};

// Generate CSS for 2D fallback
export function generateCSS(materialName, state = {}) {
  const mat = MATERIAL_PRESETS[materialName];
  if (!mat) return {};

  const [r, g, b] = mat.baseColor;
  const rgb = `${Math.floor(r * 255)}, ${Math.floor(g * 255)}, ${Math.floor(b * 255)}`;

  return {
    background: `rgba(${rgb}, ${mat.opacity * 0.5})`,
    boxShadow: mat.emissive ? `0 0 ${mat.emissiveIntensity * 30}px rgba(${rgb}, 0.5)` : 'none',
    border: mat.type === 'edge' ? `${mat.thickness * 1000}px solid rgba(${rgb}, 1)` : 'none',
    animation: mat.animated ? `pulse ${1 / (mat.pulseSpeed || 1)}s ease-in-out infinite` : 'none'
  };
}

// Three.js shader uniforms generator
export function generateUniforms(materialName, state = {}) {
  const mat = MATERIAL_PRESETS[materialName];
  if (!mat) return {};

  return {
    uBaseColor: { value: mat.baseColor },
    uOpacity: { value: mat.opacity },
    uEmissiveIntensity: { value: mat.emissiveIntensity || 0 },
    uTime: { value: 0 },
    uPulseSpeed: { value: mat.pulseSpeed || 1.0 },
    uPulseAmplitude: { value: mat.pulseAmplitude || 0.1 },
    uNoiseScale: { value: mat.noiseScale || 0.1 },
    uScanlineSpeed: { value: mat.scanlineSpeed || 0.5 },
    uMode: { value: state.mode || 0 }
  };
}

// Vertex shader for holographic effect
export const HOLO_VERTEX_SHADER = `
varying vec2 vUv;
varying vec3 vNormal;
varying vec3 vPosition;

void main() {
  vUv = uv;
  vNormal = normalize(normalMatrix * normal);
  vPosition = position;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
`;

// Fragment shader for holographic effect
export const HOLO_FRAGMENT_SHADER = `
uniform vec3 uBaseColor;
uniform float uOpacity;
uniform float uEmissiveIntensity;
uniform float uTime;
uniform float uPulseSpeed;
uniform float uScanlineSpeed;

varying vec2 vUv;
varying vec3 vNormal;
varying vec3 vPosition;

void main() {
  // Fresnel effect
  vec3 viewDir = normalize(cameraPosition - vPosition);
  float fresnel = pow(1.0 - dot(vNormal, viewDir), 2.0);
  
  // Scanlines
  float scanline = sin(vUv.y * 100.0 + uTime * uScanlineSpeed) * 0.5 + 0.5;
  scanline = smoothstep(0.4, 0.6, scanline);
  
  // Pulse
  float pulse = sin(uTime * uPulseSpeed) * 0.5 + 0.5;
  
  // Combine
  vec3 color = uBaseColor * (1.0 + fresnel * 0.5);
  color += uBaseColor * uEmissiveIntensity * pulse;
  color *= 0.8 + scanline * 0.2;
  
  float alpha = uOpacity * (0.7 + fresnel * 0.3);
  
  gl_FragColor = vec4(color, alpha);
}
`;

