/**
 * NoizyLab OS - Creative AI Worker
 * Generative AI for art, music, video, and content creation
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    CREATIVE_AI_DB: D1Database;
    CREATIVE_AI_CACHE: KVNamespace;
    CREATIVE_ASSETS: R2Bucket;
    AI: any;
    VECTORIZE: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// AI art generators
const imageGenerators = {
    'dall-e': {
        name: 'DALL-E',
        company: 'OpenAI',
        version: 'DALL-E 3',
        released: 2023,
        features: ['Text to image', 'High fidelity', 'Style control', 'Inpainting'],
        maxResolution: '1024x1024, 1792x1024, 1024x1792',
        pricing: '$0.04-0.12 per image',
        useCases: ['Marketing', 'Concept art', 'Illustrations']
    },
    'midjourney': {
        name: 'Midjourney',
        version: 'v6',
        released: 2022,
        features: ['Artistic styles', 'Variation', 'Upscaling', 'Blend'],
        accessMethod: 'Discord bot / Web',
        pricing: '$10-120/month',
        useCases: ['Digital art', 'Concept design', 'Illustrations']
    },
    'stable-diffusion': {
        name: 'Stable Diffusion',
        company: 'Stability AI',
        version: 'SDXL, SD3',
        released: 2022,
        features: ['Open source', 'Local running', 'ControlNet', 'LoRA fine-tuning', 'Inpainting'],
        license: 'Open (CreativeML)',
        useCases: ['Custom workflows', 'Product images', 'Art generation']
    },
    'adobe-firefly': {
        name: 'Adobe Firefly',
        company: 'Adobe',
        released: 2023,
        features: ['Commercial safe', 'Photoshop integration', 'Generative fill', 'Text effects'],
        pricing: 'Included in Creative Cloud',
        useCases: ['Professional design', 'Photo editing', 'Marketing']
    },
    'comfyui': {
        name: 'ComfyUI',
        type: 'Workflow tool',
        features: ['Node-based', 'Stable Diffusion backend', 'Custom workflows', 'Batch processing'],
        license: 'Open source',
        useCases: ['Complex pipelines', 'Batch generation', 'Custom models']
    }
};

// AI music generators
const musicGenerators = {
    'suno': {
        name: 'Suno AI',
        released: 2023,
        features: ['Full songs', 'Vocals', 'Multiple genres', 'Custom lyrics'],
        duration: 'Up to 4 minutes',
        pricing: 'Free tier, Pro $10/month',
        useCases: ['Music creation', 'Songwriting', 'Background music']
    },
    'udio': {
        name: 'Udio',
        released: 2024,
        features: ['High quality', 'Genre versatility', 'Vocal synthesis', 'Extension'],
        useCases: ['Music production', 'Demo creation']
    },
    'musicgen': {
        name: 'MusicGen',
        company: 'Meta',
        released: 2023,
        features: ['Open source', 'Text to music', 'Melody conditioning'],
        license: 'CC BY-NC',
        useCases: ['Research', 'Background music', 'Experimentation']
    },
    'aiva': {
        name: 'AIVA',
        released: 2016,
        features: ['Classical focus', 'Composition', 'MIDI export', 'Custom styles'],
        pricing: 'Free-$49/month',
        useCases: ['Film scoring', 'Game music', 'Classical composition']
    },
    'mubert': {
        name: 'Mubert',
        features: ['Royalty-free', 'API access', 'Continuous generation', 'Mood-based'],
        pricing: 'API-based pricing',
        useCases: ['Background music', 'Apps', 'Content creation']
    }
};

// AI video generators
const videoGenerators = {
    'sora': {
        name: 'Sora',
        company: 'OpenAI',
        released: 2024,
        features: ['Text to video', 'Up to 60 seconds', 'High fidelity', 'Complex scenes'],
        status: 'Limited access',
        useCases: ['Film production', 'Advertising', 'Creative projects']
    },
    'runway': {
        name: 'Runway Gen-3',
        company: 'Runway ML',
        released: 2024,
        features: ['Text to video', 'Image to video', 'Motion brush', 'Style transfer'],
        pricing: 'Credits-based',
        useCases: ['Short films', 'Music videos', 'Social content']
    },
    'pika': {
        name: 'Pika',
        released: 2023,
        features: ['Text to video', 'Image to video', 'Video editing', 'Lip sync'],
        pricing: 'Free tier available',
        useCases: ['Social media', 'Prototyping', 'Creative projects']
    },
    'kling': {
        name: 'Kling AI',
        company: 'Kuaishou',
        released: 2024,
        features: ['High quality', 'Long duration', 'Chinese company'],
        useCases: ['Video content', 'Marketing']
    },
    'luma': {
        name: 'Luma Dream Machine',
        company: 'Luma AI',
        released: 2024,
        features: ['Fast generation', 'High quality', 'Character consistency'],
        pricing: 'Free tier, subscription available',
        useCases: ['Quick prototypes', 'Social content']
    }
};

// AI voice/speech tools
const voiceGenerators = {
    'elevenlabs': {
        name: 'ElevenLabs',
        released: 2023,
        features: ['Voice cloning', 'Text to speech', 'Multilingual', 'Emotion control'],
        quality: 'Near-human',
        pricing: 'Free tier, $5-330/month',
        useCases: ['Audiobooks', 'Podcasts', 'Voice overs', 'Dubbing']
    },
    'resemble': {
        name: 'Resemble AI',
        features: ['Voice cloning', 'Emotion', 'Real-time', 'API'],
        useCases: ['Gaming', 'Virtual assistants', 'Content']
    },
    'descript': {
        name: 'Descript Overdub',
        features: ['Voice cloning', 'Podcast editing', 'Filler word removal'],
        pricing: '$12-24/month',
        useCases: ['Podcasts', 'Video editing', 'Voice correction']
    },
    'speechify': {
        name: 'Speechify',
        features: ['Text to speech', 'Multiple voices', 'Browser extension'],
        useCases: ['Reading assistance', 'Accessibility']
    }
};

// Prompt engineering tips
const promptTips = {
    image: [
        'Be specific about style: "oil painting", "digital art", "photograph"',
        'Include lighting: "golden hour", "studio lighting", "dramatic shadows"',
        'Specify camera: "wide angle", "macro", "35mm film"',
        'Add quality modifiers: "highly detailed", "8k", "award-winning"',
        'Use artist references: "in the style of..."',
        'Include mood: "ethereal", "moody", "vibrant"'
    ],
    music: [
        'Specify genre clearly: "lo-fi hip hop", "epic orchestral", "indie folk"',
        'Include tempo: "slow and melancholic", "upbeat and energetic"',
        'Describe instruments: "acoustic guitar", "synth pads", "string quartet"',
        'Add mood descriptors: "nostalgic", "triumphant", "mysterious"',
        'Reference era: "80s synthwave", "classical baroque"'
    ],
    video: [
        'Describe motion: "camera slowly pans", "character walks toward camera"',
        'Specify shot type: "establishing shot", "close-up", "drone footage"',
        'Include environment details: "rainy city at night", "sunlit forest"',
        'Add temporal elements: "sunrise", "time-lapse", "slow motion"'
    ]
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'creative-ai',
        status: 'operational',
        version: '1.0.0',
        description: 'Generative AI for creative content',
        capabilities: [
            'Image generation guidance',
            'Music AI comparison',
            'Video generation info',
            'Voice synthesis tools',
            'Prompt engineering tips',
            'Workflow recommendations',
            'Tool selection advice'
        ]
    });
});

// Get all image generators
app.get('/image', (c) => {
    return c.json({
        generators: imageGenerators,
        total: Object.keys(imageGenerators).length
    });
});

// Get all music generators
app.get('/music', (c) => {
    return c.json({
        generators: musicGenerators,
        total: Object.keys(musicGenerators).length
    });
});

// Get all video generators
app.get('/video', (c) => {
    return c.json({
        generators: videoGenerators,
        total: Object.keys(videoGenerators).length
    });
});

// Get all voice generators
app.get('/voice', (c) => {
    return c.json({
        generators: voiceGenerators,
        total: Object.keys(voiceGenerators).length
    });
});

// Get prompt tips
app.get('/prompts', (c) => {
    const type = c.req.query('type');

    if (type && promptTips[type as keyof typeof promptTips]) {
        return c.json({
            type,
            tips: promptTips[type as keyof typeof promptTips]
        });
    }

    return c.json({
        tips: promptTips,
        categories: Object.keys(promptTips)
    });
});

// Tool recommendation
app.post('/recommend', async (c) => {
    const body = await c.req.json();
    const {
        type = 'image',
        budget = 'free',
        useCase = 'personal',
        needLocal = false
    } = body;

    let recommendations: any[] = [];

    if (type === 'image') {
        if (needLocal) {
            recommendations = [
                { tool: 'Stable Diffusion', reason: 'Free, open source, runs locally' },
                { tool: 'ComfyUI', reason: 'Advanced workflows with local SD' }
            ];
        } else if (budget === 'free') {
            recommendations = [
                { tool: 'Stable Diffusion', reason: 'Open source, free to use' },
                { tool: 'Leonardo AI', reason: 'Free tier available' }
            ];
        } else if (useCase === 'commercial') {
            recommendations = [
                { tool: 'Adobe Firefly', reason: 'Commercial safe, integrated workflow' },
                { tool: 'DALL-E 3', reason: 'High quality, clear licensing' }
            ];
        } else {
            recommendations = [
                { tool: 'Midjourney', reason: 'Best artistic quality' },
                { tool: 'DALL-E 3', reason: 'Best prompt understanding' }
            ];
        }
    } else if (type === 'music') {
        if (budget === 'free') {
            recommendations = [
                { tool: 'Suno AI', reason: 'Free tier with full songs' },
                { tool: 'MusicGen', reason: 'Open source, local running' }
            ];
        } else {
            recommendations = [
                { tool: 'Suno AI Pro', reason: 'Best overall quality and features' },
                { tool: 'AIVA', reason: 'Best for classical/orchestral' }
            ];
        }
    } else if (type === 'video') {
        recommendations = [
            { tool: 'Runway Gen-3', reason: 'Most accessible, good quality' },
            { tool: 'Pika', reason: 'Free tier, quick results' }
        ];
    } else if (type === 'voice') {
        recommendations = [
            { tool: 'ElevenLabs', reason: 'Best quality voice synthesis' },
            { tool: 'Descript', reason: 'Best for podcast editing' }
        ];
    }

    return c.json({
        input: { type, budget, useCase, needLocal },
        recommendations,
        promptTips: promptTips[type as keyof typeof promptTips] || []
    });
});

// AI-powered creative query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();

    if (!question) {
        return c.json({ error: 'Question is required' }, 400);
    }

    try {
        const context = `You are a creative AI expert with deep knowledge of:
- Image generators (DALL-E 3, Midjourney, Stable Diffusion, Adobe Firefly)
- Music generators (Suno AI, Udio, MusicGen, AIVA)
- Video generators (Sora, Runway, Pika, Kling)
- Voice synthesis (ElevenLabs, Resemble AI, Descript)
- Prompt engineering techniques
- AI art workflows and pipelines
- Copyright and licensing considerations

Image tools: ${Object.keys(imageGenerators).join(', ')}
Music tools: ${Object.keys(musicGenerators).join(', ')}
Video tools: ${Object.keys(videoGenerators).join(', ')}`;

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
            sources: ['AI tool documentation', 'Industry practices']
        });
    } catch (error) {
        return c.json({
            question,
            answer: 'Creative AI guidance: Use Midjourney/DALL-E for images, Suno for music, Runway for video, ElevenLabs for voice. Always check licensing for commercial use.',
            error: 'AI temporarily unavailable'
        });
    }
});

export default app;
