/**
 * NoizyLab OS - 3D Graphics Worker
 * 3D rendering, game engines, WebGL, and graphics pipeline knowledge
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    GRAPHICS_3D_DB: D1Database;
    GRAPHICS_3D_CACHE: KVNamespace;
    GRAPHICS_ASSETS: R2Bucket;
    AI: any;
    VECTORIZE: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// 3D file formats
const formats3D = {
    'gltf': {
        name: 'glTF',
        fullName: 'GL Transmission Format',
        extensions: ['.gltf', '.glb'],
        developer: 'Khronos Group',
        released: 2017,
        features: ['PBR materials', 'Animations', 'Skinning', 'Morphing', 'Binary (.glb)'],
        useCases: ['Web 3D', 'AR/VR', 'Game assets', 'Product visualization'],
        description: 'The "JPEG of 3D" - efficient runtime delivery format'
    },
    'fbx': {
        name: 'FBX',
        fullName: 'Filmbox',
        extensions: ['.fbx'],
        developer: 'Autodesk',
        released: 2006,
        features: ['Animation', 'Rigging', 'Geometry', 'Materials', 'Lights', 'Cameras'],
        useCases: ['Game development', 'Film production', 'Asset exchange'],
        description: 'Industry standard for animation and game pipelines'
    },
    'obj': {
        name: 'OBJ',
        fullName: 'Wavefront OBJ',
        extensions: ['.obj'],
        developer: 'Wavefront Technologies',
        released: 1980s,
        features: ['Geometry', 'UV mapping', 'Normals', 'MTL materials'],
        useCases: ['3D printing', 'CAD exchange', 'Simple geometry'],
        description: 'Simple text-based format, universally supported'
    },
    'usd': {
        name: 'USD/USDZ',
        fullName: 'Universal Scene Description',
        extensions: ['.usd', '.usda', '.usdc', '.usdz'],
        developer: 'Pixar',
        released: 2016,
        features: ['Scene composition', 'Variants', 'Layers', 'AR (USDZ)'],
        useCases: ['VFX', 'AR Quick Look', 'Scene management', 'Collaboration'],
        description: 'Pixar\'s scene description used in film and Apple AR'
    },
    'blend': {
        name: 'Blender',
        fullName: 'Blender Native Format',
        extensions: ['.blend'],
        developer: 'Blender Foundation',
        features: ['Everything in one file', 'Undo history', 'Custom data'],
        useCases: ['Blender projects', 'Asset archiving'],
        description: 'Native Blender format with complete project data'
    },
    'stl': {
        name: 'STL',
        fullName: 'Stereolithography',
        extensions: ['.stl'],
        developer: '3D Systems',
        released: 1987,
        features: ['Triangulated geometry', 'Binary and ASCII'],
        useCases: ['3D printing', 'CAD/CAM', 'Rapid prototyping'],
        description: 'Standard format for 3D printing'
    }
};

// Game engines knowledge
const gameEngines = {
    'unity': {
        name: 'Unity',
        company: 'Unity Technologies',
        released: 2005,
        languages: ['C#', 'UnityScript (deprecated)'],
        platforms: ['PC', 'Mac', 'Linux', 'iOS', 'Android', 'WebGL', 'Consoles', 'VR/AR'],
        renderPipelines: ['Built-in', 'URP (Universal)', 'HDRP (High Definition)'],
        features: ['Visual scripting', 'Asset store', 'Cross-platform', 'AR Foundation'],
        marketShare: '~50% of mobile games',
        pricing: 'Free tier available, Pro: $150/month'
    },
    'unreal': {
        name: 'Unreal Engine',
        company: 'Epic Games',
        released: 1998,
        version: 'UE5',
        languages: ['C++', 'Blueprints (visual scripting)'],
        platforms: ['PC', 'Mac', 'Linux', 'iOS', 'Android', 'Consoles', 'VR/AR'],
        features: ['Nanite', 'Lumen', 'MetaHumans', 'Chaos physics', 'Niagara VFX'],
        marketShare: 'Leading AAA engine',
        pricing: 'Free until $1M revenue, then 5% royalty'
    },
    'godot': {
        name: 'Godot',
        company: 'Godot Engine community',
        released: 2014,
        languages: ['GDScript', 'C#', 'C++', 'Visual scripting'],
        platforms: ['PC', 'Mac', 'Linux', 'iOS', 'Android', 'WebGL'],
        features: ['Open source', 'Lightweight', '2D-first design', 'Node system'],
        pricing: 'Free and open source (MIT)'
    },
    'threejs': {
        name: 'Three.js',
        type: 'Library',
        released: 2010,
        languages: ['JavaScript', 'TypeScript'],
        platforms: ['WebGL', 'WebGPU'],
        features: ['WebGL abstraction', 'PBR materials', 'Post-processing', 'Physics integration'],
        useCases: ['Web 3D', 'Product configurators', 'Data visualization', 'Games'],
        pricing: 'Free and open source (MIT)'
    },
    'babylonjs': {
        name: 'Babylon.js',
        company: 'Microsoft',
        released: 2013,
        languages: ['JavaScript', 'TypeScript'],
        platforms: ['WebGL', 'WebGPU', 'Native'],
        features: ['Physics', 'GUI', 'Particles', 'Node material editor', 'Playground'],
        pricing: 'Free and open source (Apache 2.0)'
    }
};

// Graphics APIs
const graphicsAPIs = {
    'webgl': {
        name: 'WebGL',
        version: '2.0',
        basedOn: 'OpenGL ES 3.0',
        platform: 'Web browsers',
        features: ['3D in browser', 'Shader support', 'Texture compression'],
        support: '98% of browsers'
    },
    'webgpu': {
        name: 'WebGPU',
        status: 'Emerging',
        basedOn: 'Vulkan, Metal, D3D12',
        platform: 'Modern browsers',
        features: ['Compute shaders', 'Better performance', 'Modern API design'],
        support: 'Chrome, Edge, Firefox (in progress)'
    },
    'vulkan': {
        name: 'Vulkan',
        developer: 'Khronos Group',
        released: 2016,
        platforms: ['Windows', 'Linux', 'Android', 'macOS (MoltenVK)'],
        features: ['Low-level control', 'Multi-threading', 'Cross-platform']
    },
    'metal': {
        name: 'Metal',
        developer: 'Apple',
        released: 2014,
        platforms: ['macOS', 'iOS', 'tvOS'],
        features: ['Low overhead', 'GPU compute', 'Ray tracing (Metal 3)']
    },
    'directx': {
        name: 'DirectX 12',
        developer: 'Microsoft',
        released: 2015,
        platforms: ['Windows', 'Xbox'],
        features: ['Low-level access', 'Ray tracing (DXR)', 'Variable rate shading']
    },
    'opengl': {
        name: 'OpenGL',
        version: '4.6',
        developer: 'Khronos Group',
        platforms: ['Cross-platform'],
        status: 'Legacy (succeeded by Vulkan)',
        features: ['Wide support', 'Easy to learn', 'Mature ecosystem']
    }
};

// Rendering techniques
const renderingTechniques = {
    'pbr': {
        name: 'Physically Based Rendering',
        description: 'Realistic material rendering based on physics',
        parameters: ['Albedo', 'Metallic', 'Roughness', 'Normal', 'AO', 'Emission']
    },
    'raytracing': {
        name: 'Ray Tracing',
        description: 'Simulates light behavior for realistic reflections, shadows, GI',
        types: ['Path tracing', 'Ray marching', 'Hybrid rendering']
    },
    'deferred': {
        name: 'Deferred Rendering',
        description: 'Geometry pass + lighting pass for many lights',
        pros: ['Many lights', 'Efficient'],
        cons: ['Memory bandwidth', 'Transparency issues']
    },
    'forward': {
        name: 'Forward Rendering',
        description: 'Traditional single-pass rendering',
        pros: ['Simpler', 'Good for mobile', 'MSAA support'],
        cons: ['Light count limits']
    }
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: '3d-graphics',
        status: 'operational',
        version: '1.0.0',
        description: '3D rendering, game engines, and graphics pipeline intelligence',
        capabilities: [
            '3D format information',
            'Game engine comparison',
            'Graphics API guidance',
            'Rendering technique advice',
            'WebGL/WebGPU help',
            'Shader programming tips',
            'Performance optimization'
        ]
    });
});

// Get 3D formats
app.get('/formats', (c) => {
    return c.json({
        formats: formats3D,
        totalFormats: Object.keys(formats3D).length
    });
});

// Get game engines
app.get('/engines', (c) => {
    return c.json({
        engines: gameEngines,
        totalEngines: Object.keys(gameEngines).length
    });
});

// Get graphics APIs
app.get('/apis', (c) => {
    return c.json({
        apis: graphicsAPIs,
        totalApis: Object.keys(graphicsAPIs).length
    });
});

// Get rendering techniques
app.get('/rendering', (c) => {
    return c.json({
        techniques: renderingTechniques
    });
});

// Engine recommendation
app.post('/recommend', async (c) => {
    const body = await c.req.json();
    const {
        projectType = '3d-game',
        platforms = ['web'],
        team = 'solo',
        budget = 'free'
    } = body;

    let recommendation;

    if (platforms.includes('web')) {
        recommendation = {
            primary: 'Three.js',
            alternative: 'Babylon.js',
            reason: 'Best for web deployment with no plugins required'
        };
    } else if (projectType === 'mobile' || projectType === 'casual') {
        recommendation = {
            primary: 'Unity',
            alternative: 'Godot',
            reason: 'Best mobile deployment and asset store ecosystem'
        };
    } else if (projectType === 'aaa' || projectType === 'realistic') {
        recommendation = {
            primary: 'Unreal Engine',
            alternative: 'Unity HDRP',
            reason: 'Best for high-fidelity graphics with Nanite and Lumen'
        };
    } else if (budget === 'free' && team === 'solo') {
        recommendation = {
            primary: 'Godot',
            alternative: 'Unity Personal',
            reason: 'Free, open source, lightweight for solo developers'
        };
    } else {
        recommendation = {
            primary: 'Unity',
            alternative: 'Unreal Engine',
            reason: 'Industry standard with broad platform support'
        };
    }

    return c.json({
        input: { projectType, platforms, team, budget },
        recommendation,
        comparisonChart: {
            unity: { learning: '⭐⭐⭐', graphics: '⭐⭐⭐⭐', mobile: '⭐⭐⭐⭐⭐', cost: 'Free-$150/mo' },
            unreal: { learning: '⭐⭐', graphics: '⭐⭐⭐⭐⭐', mobile: '⭐⭐⭐', cost: '5% royalty' },
            godot: { learning: '⭐⭐⭐⭐', graphics: '⭐⭐⭐', mobile: '⭐⭐⭐', cost: 'Free' },
            threejs: { learning: '⭐⭐⭐⭐', graphics: '⭐⭐⭐', web: '⭐⭐⭐⭐⭐', cost: 'Free' }
        }
    });
});

// AI-powered 3D graphics query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();

    if (!question) {
        return c.json({ error: 'Question is required' }, 400);
    }

    try {
        const context = `You are a 3D graphics expert with deep knowledge of:
- 3D file formats (glTF, FBX, OBJ, USD, STL, Blender)
- Game engines (Unity, Unreal Engine, Godot, Three.js, Babylon.js)
- Graphics APIs (WebGL, WebGPU, Vulkan, Metal, DirectX, OpenGL)
- Rendering techniques (PBR, ray tracing, deferred/forward rendering)
- Shader programming (GLSL, HLSL, compute shaders)
- 3D modeling and animation
- VR/AR development
- Performance optimization

Game engines: ${Object.keys(gameEngines).join(', ')}
Graphics APIs: ${Object.keys(graphicsAPIs).join(', ')}
3D formats: ${Object.keys(formats3D).join(', ')}`;

        const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
            messages: [
                { role: 'system', content: context },
                { role: 'user', content: question }
            ],
            max_tokens: 1024
        });

        return c.json({
            question,
            answer: response.response,
            sources: ['Khronos specifications', 'Engine documentation', 'Industry practices']
        });
    } catch (error) {
        return c.json({
            question,
            answer: '3D graphics guidance: Use glTF for web delivery, FBX for animation pipelines. Unity for mobile, Unreal for AAA, Three.js for web 3D.',
            error: 'AI temporarily unavailable'
        });
    }
});

// Shader code snippets
app.get('/shaders/:type', (c) => {
    const type = c.req.param('type');

    const shaders: Record<string, any> = {
        vertex: {
            name: 'Basic Vertex Shader',
            language: 'GLSL',
            code: `#version 300 es
precision highp float;

in vec3 position;
in vec3 normal;
in vec2 uv;

uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;
uniform mat3 normalMatrix;

out vec3 vNormal;
out vec2 vUv;
out vec3 vPosition;

void main() {
  vNormal = normalMatrix * normal;
  vUv = uv;
  vPosition = (modelViewMatrix * vec4(position, 1.0)).xyz;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}`
        },
        fragment: {
            name: 'PBR Fragment Shader (Simplified)',
            language: 'GLSL',
            code: `#version 300 es
precision highp float;

in vec3 vNormal;
in vec2 vUv;
in vec3 vPosition;

uniform sampler2D albedoMap;
uniform sampler2D normalMap;
uniform sampler2D metallicMap;
uniform sampler2D roughnessMap;

uniform vec3 lightPosition;
uniform vec3 cameraPosition;

out vec4 fragColor;

void main() {
  vec3 albedo = texture(albedoMap, vUv).rgb;
  float metallic = texture(metallicMap, vUv).r;
  float roughness = texture(roughnessMap, vUv).r;
  
  vec3 N = normalize(vNormal);
  vec3 V = normalize(cameraPosition - vPosition);
  vec3 L = normalize(lightPosition - vPosition);
  vec3 H = normalize(V + L);
  
  // Simplified PBR calculation
  float NdotL = max(dot(N, L), 0.0);
  float NdotH = max(dot(N, H), 0.0);
  
  vec3 diffuse = albedo * NdotL;
  vec3 specular = vec3(pow(NdotH, (1.0 - roughness) * 128.0));
  
  fragColor = vec4(diffuse + specular * metallic, 1.0);
}`
        }
    };

    if (!shaders[type]) {
        return c.json({ error: 'Shader type not found', available: Object.keys(shaders) }, 404);
    }

    return c.json(shaders[type]);
});

export default app;
