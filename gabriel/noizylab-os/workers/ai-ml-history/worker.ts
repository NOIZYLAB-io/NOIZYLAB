import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env { AI_HISTORY_DB: D1Database; AI_CACHE: KVNamespace; AI: any; }

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// ==============================================================================
// NOIZYLAB OS - AI/ML HISTORY WORKER
// Complete History of Artificial Intelligence from Turing to GPT
// ==============================================================================

const AI_ML_HISTORY = {
    // ===========================================================================
    // FOUNDATIONS (1940s-1960s)
    // ===========================================================================
    foundations: {
        turing_machine: {
            name: 'Turing Machine Concept',
            year: 1936,
            pioneer: 'Alan Turing',
            significance: 'Theoretical foundation of computation and AI'
        },
        turing_test: {
            name: 'Turing Test',
            year: 1950,
            pioneer: 'Alan Turing',
            paper: 'Computing Machinery and Intelligence',
            significance: 'Proposed test for machine intelligence'
        },
        perceptron: {
            name: 'Perceptron',
            year: 1958,
            pioneer: 'Frank Rosenblatt',
            significance: 'First neural network hardware',
            location: 'Cornell Aeronautical Laboratory'
        },
        dartmouth_conference: {
            name: 'Dartmouth Conference',
            year: 1956,
            pioneers: ['John McCarthy', 'Marvin Minsky', 'Claude Shannon', 'Nathaniel Rochester'],
            significance: 'Birth of AI as a field - coined "Artificial Intelligence"'
        },
        lisp: {
            name: 'LISP Programming Language',
            year: 1958,
            pioneer: 'John McCarthy',
            significance: 'First AI programming language'
        },
        eliza: {
            name: 'ELIZA',
            year: 1966,
            pioneer: 'Joseph Weizenbaum',
            institution: 'MIT',
            significance: 'First chatbot, natural language processing pioneer'
        },
        shakey: {
            name: 'Shakey the Robot',
            year: 1966,
            institution: 'SRI',
            significance: 'First mobile robot with AI'
        }
    },

    // ===========================================================================
    // EXPERT SYSTEMS ERA (1970s-1980s)
    // ===========================================================================
    expertSystems: {
        mycin: {
            name: 'MYCIN',
            year: 1972,
            institution: 'Stanford',
            pioneer: 'Edward Shortliffe',
            significance: 'Medical diagnosis expert system'
        },
        dendral: {
            name: 'DENDRAL',
            year: 1965,
            institution: 'Stanford',
            pioneers: ['Edward Feigenbaum', 'Joshua Lederberg'],
            significance: 'First successful expert system'
        },
        r1_xcon: {
            name: 'R1/XCON',
            year: 1980,
            pioneer: 'John McDermott',
            company: 'DEC',
            significance: 'First commercial expert system ($40M/year savings)'
        },
        prolog: {
            name: 'Prolog',
            year: 1972,
            pioneers: ['Alain Colmerauer', 'Robert Kowalski'],
            significance: 'Logic programming for AI'
        },
        fifth_gen: {
            name: 'Fifth Generation Computer Project',
            year: 1982,
            country: 'Japan',
            significance: 'National AI initiative ($400M investment)'
        },
        ai_winter_1: {
            name: 'First AI Winter',
            years: '1974-1980',
            significance: 'Reduced funding after overpromising'
        },
        ai_winter_2: {
            name: 'Second AI Winter',
            years: '1987-1993',
            significance: 'Expert systems market collapse'
        }
    },

    // ===========================================================================
    // MACHINE LEARNING FOUNDATIONS
    // ===========================================================================
    mlFoundations: {
        backpropagation: {
            name: 'Backpropagation',
            year: 1986,
            pioneers: ['David Rumelhart', 'Geoffrey Hinton', 'Ronald Williams'],
            paper: 'Learning representations by back-propagating errors',
            significance: 'Enabled training deep networks'
        },
        decision_trees: {
            name: 'ID3 Algorithm',
            year: 1986,
            pioneer: 'Ross Quinlan',
            significance: 'Decision tree learning'
        },
        c45: {
            name: 'C4.5 Algorithm',
            year: 1993,
            pioneer: 'Ross Quinlan',
            significance: 'Improved decision trees'
        },
        svm: {
            name: 'Support Vector Machines',
            year: 1995,
            pioneers: ['Corinna Cortes', 'Vladimir Vapnik'],
            significance: 'Kernel methods for classification'
        },
        random_forest: {
            name: 'Random Forests',
            year: 2001,
            pioneer: 'Leo Breiman',
            significance: 'Ensemble learning method'
        },
        boosting: {
            name: 'AdaBoost',
            year: 1995,
            pioneers: ['Yoav Freund', 'Robert Schapire'],
            significance: 'First successful boosting algorithm'
        },
        xgboost: {
            name: 'XGBoost',
            year: 2014,
            pioneer: 'Tianqi Chen',
            significance: 'Gradient boosting that dominates competitions'
        },
        bayesian_networks: {
            name: 'Bayesian Networks',
            year: 1988,
            pioneer: 'Judea Pearl',
            significance: 'Probabilistic graphical models'
        }
    },

    // ===========================================================================
    // DEEP LEARNING REVOLUTION
    // ===========================================================================
    deepLearning: {
        cnn_lenet: {
            name: 'LeNet / CNN',
            year: 1989,
            pioneer: 'Yann LeCun',
            significance: 'Convolutional neural networks for image recognition'
        },
        lstm: {
            name: 'LSTM (Long Short-Term Memory)',
            year: 1997,
            pioneers: ['Sepp Hochreiter', 'Jürgen Schmidhuber'],
            significance: 'Solved vanishing gradient for sequences'
        },
        alexnet: {
            name: 'AlexNet',
            year: 2012,
            pioneers: ['Alex Krizhevsky', 'Ilya Sutskever', 'Geoffrey Hinton'],
            significance: 'ImageNet breakthrough, started deep learning revolution'
        },
        dropout: {
            name: 'Dropout',
            year: 2012,
            pioneers: ['Geoffrey Hinton', 'et al.'],
            significance: 'Regularization technique for neural networks'
        },
        batch_norm: {
            name: 'Batch Normalization',
            year: 2015,
            pioneers: ['Sergey Ioffe', 'Christian Szegedy'],
            significance: 'Accelerates training, enables deeper networks'
        },
        resnet: {
            name: 'ResNet',
            year: 2015,
            pioneer: 'Kaiming He (Microsoft)',
            significance: 'Residual connections, 152 layers deep'
        },
        vgg: {
            name: 'VGGNet',
            year: 2014,
            institution: 'Oxford Visual Geometry Group',
            significance: 'Simple, deep architecture'
        },
        googlenet: {
            name: 'GoogLeNet/Inception',
            year: 2014,
            company: 'Google',
            significance: 'Inception modules'
        },
        gan: {
            name: 'GAN (Generative Adversarial Networks)',
            year: 2014,
            pioneer: 'Ian Goodfellow',
            significance: 'Generator vs discriminator paradigm'
        },
        vae: {
            name: 'VAE (Variational Autoencoder)',
            year: 2013,
            pioneers: ['Kingma', 'Welling'],
            significance: 'Probabilistic generative model'
        },
        word2vec: {
            name: 'Word2Vec',
            year: 2013,
            pioneer: 'Tomas Mikolov (Google)',
            significance: 'Word embeddings, "king - man + woman = queen"'
        }
    },

    // ===========================================================================
    // TRANSFORMER ERA & LLMs
    // ===========================================================================
    transformerEra: {
        attention_mechanism: {
            name: 'Attention Mechanism',
            year: 2014,
            pioneers: ['Bahdanau', 'Cho', 'Bengio'],
            significance: 'Key to sequence-to-sequence models'
        },
        transformer: {
            name: 'Transformer Architecture',
            year: 2017,
            paper: 'Attention Is All You Need',
            authors: ['Vaswani', 'et al.'],
            company: 'Google',
            significance: 'Foundation of modern NLP and LLMs'
        },
        bert: {
            name: 'BERT',
            year: 2018,
            company: 'Google',
            significance: 'Bidirectional encoder, revolutionized NLP benchmarks'
        },
        gpt1: {
            name: 'GPT-1',
            year: 2018,
            company: 'OpenAI',
            parameters: '117M',
            significance: 'Generative pre-training'
        },
        gpt2: {
            name: 'GPT-2',
            year: 2019,
            company: 'OpenAI',
            parameters: '1.5B',
            significance: 'Too dangerous to release (initially)'
        },
        gpt3: {
            name: 'GPT-3',
            year: 2020,
            company: 'OpenAI',
            parameters: '175B',
            significance: 'Few-shot learning, emergent capabilities'
        },
        gpt4: {
            name: 'GPT-4',
            year: 2023,
            company: 'OpenAI',
            significance: 'Multimodal, passed bar exam, medical licensing'
        },
        gpt4o: {
            name: 'GPT-4o',
            year: 2024,
            company: 'OpenAI',
            significance: 'Omnimodal - native audio/video/text'
        },
        o1: {
            name: 'o1 / o1-pro',
            year: 2024,
            company: 'OpenAI',
            significance: 'Chain-of-thought reasoning, PhD-level performance'
        },
        chatgpt: {
            name: 'ChatGPT',
            year: 2022,
            company: 'OpenAI',
            significance: 'Consumer AI breakthrough, 100M users in 2 months'
        },
        claude: {
            name: 'Claude',
            year: 2023,
            company: 'Anthropic',
            versions: ['Claude 1', 'Claude 2', 'Claude 3 (Opus, Sonnet, Haiku)', 'Claude 3.5', 'Claude 4'],
            significance: 'Constitutional AI, long context'
        },
        llama: {
            name: 'LLaMA',
            year: 2023,
            company: 'Meta',
            versions: ['LLaMA', 'LLaMA 2', 'LLaMA 3', 'LLaMA 3.1', 'LLaMA 3.2', 'LLaMA 4'],
            significance: 'Open-source LLM revolution'
        },
        gemini: {
            name: 'Gemini',
            year: 2023,
            company: 'Google DeepMind',
            versions: ['Gemini Ultra', 'Gemini Pro', 'Gemini Nano', 'Gemini 1.5', 'Gemini 2'],
            significance: 'Google\'s frontier multimodal model'
        },
        palm: {
            name: 'PaLM',
            year: 2022,
            company: 'Google',
            parameters: '540B',
            significance: 'Pathways Language Model'
        },
        mistral: {
            name: 'Mistral',
            year: 2023,
            company: 'Mistral AI',
            significance: 'Efficient open-source models'
        },
        phi: {
            name: 'Phi',
            year: 2023,
            company: 'Microsoft',
            versions: ['Phi-1', 'Phi-2', 'Phi-3'],
            significance: 'Small but capable models'
        }
    },

    // ===========================================================================
    // COMPUTER VISION MILESTONES
    // ===========================================================================
    computerVision: {
        imagenet: {
            name: 'ImageNet',
            year: 2009,
            pioneer: 'Fei-Fei Li',
            significance: '14M images, enabled deep learning breakthroughs'
        },
        yolo: {
            name: 'YOLO (You Only Look Once)',
            year: 2015,
            pioneer: 'Joseph Redmon',
            significance: 'Real-time object detection'
        },
        unet: {
            name: 'U-Net',
            year: 2015,
            significance: 'Medical image segmentation'
        },
        sam: {
            name: 'Segment Anything Model (SAM)',
            year: 2023,
            company: 'Meta',
            significance: 'Universal image segmentation'
        },
        clip: {
            name: 'CLIP',
            year: 2021,
            company: 'OpenAI',
            significance: 'Vision-language understanding'
        },
        vit: {
            name: 'Vision Transformer (ViT)',
            year: 2020,
            company: 'Google',
            significance: 'Transformers for images'
        }
    },

    // ===========================================================================
    // GENERATIVE AI & DIFFUSION
    // ===========================================================================
    generativeAI: {
        stable_diffusion: {
            name: 'Stable Diffusion',
            year: 2022,
            company: 'Stability AI',
            significance: 'Open-source image generation'
        },
        dalle: {
            name: 'DALL-E',
            versions: ['DALL-E (2021)', 'DALL-E 2 (2022)', 'DALL-E 3 (2023)'],
            company: 'OpenAI',
            significance: 'Text-to-image generation'
        },
        midjourney: {
            name: 'Midjourney',
            year: 2022,
            significance: 'Artistic AI image generation'
        },
        imagen: {
            name: 'Imagen',
            year: 2022,
            company: 'Google',
            significance: 'Photorealistic image generation'
        },
        sora: {
            name: 'Sora',
            year: 2024,
            company: 'OpenAI',
            significance: 'Text-to-video generation'
        },
        runway: {
            name: 'Runway Gen-2/Gen-3',
            year: 2023,
            company: 'Runway',
            significance: 'Video generation and editing'
        },
        music_gen: {
            name: 'MusicGen',
            year: 2023,
            company: 'Meta',
            significance: 'Text-to-music generation'
        },
        suno: {
            name: 'Suno AI',
            year: 2023,
            significance: 'AI music generation with vocals'
        }
    },

    // ===========================================================================
    // REINFORCEMENT LEARNING MILESTONES
    // ===========================================================================
    reinforcementLearning: {
        td_learning: {
            name: 'Temporal Difference Learning',
            year: 1988,
            pioneer: 'Richard Sutton',
            significance: 'Foundation of RL'
        },
        q_learning: {
            name: 'Q-Learning',
            year: 1989,
            pioneer: 'Chris Watkins',
            significance: 'Model-free RL algorithm'
        },
        dqn: {
            name: 'Deep Q-Network (DQN)',
            year: 2013,
            company: 'DeepMind',
            pioneer: 'Volodymyr Mnih',
            significance: 'Deep learning + RL, played Atari games'
        },
        alphago: {
            name: 'AlphaGo',
            year: 2016,
            company: 'DeepMind',
            significance: 'Beat world champion Lee Sedol at Go'
        },
        alphazero: {
            name: 'AlphaZero',
            year: 2017,
            company: 'DeepMind',
            significance: 'Self-taught chess, shogi, Go mastery'
        },
        alphastar: {
            name: 'AlphaStar',
            year: 2019,
            company: 'DeepMind',
            significance: 'Grandmaster level StarCraft II'
        },
        muzero: {
            name: 'MuZero',
            year: 2019,
            company: 'DeepMind',
            significance: 'Learned game rules from scratch'
        },
        openai_five: {
            name: 'OpenAI Five',
            year: 2018,
            company: 'OpenAI',
            significance: 'Beat world champions at Dota 2'
        },
        rlhf: {
            name: 'RLHF (Reinforcement Learning from Human Feedback)',
            year: 2017,
            pioneers: ['Christiano', 'et al.'],
            significance: 'How ChatGPT was trained to be helpful'
        },
        ppo: {
            name: 'PPO (Proximal Policy Optimization)',
            year: 2017,
            company: 'OpenAI',
            pioneer: 'John Schulman',
            significance: 'Stable policy gradient algorithm'
        }
    },

    // ===========================================================================
    // AI RESEARCH INSTITUTIONS & COMPANIES
    // ===========================================================================
    institutions: {
        openai: {
            name: 'OpenAI',
            founded: 2015,
            founders: ['Sam Altman', 'Elon Musk', 'Ilya Sutskever', 'Greg Brockman'],
            significance: 'GPT series, ChatGPT, DALL-E'
        },
        deepmind: {
            name: 'Google DeepMind',
            founded: 2010,
            founder: 'Demis Hassabis',
            significance: 'AlphaGo, AlphaFold, Gemini'
        },
        anthropic: {
            name: 'Anthropic',
            founded: 2021,
            founders: ['Dario Amodei', 'Daniela Amodei'],
            significance: 'Claude, Constitutional AI, safety research'
        },
        meta_ai: {
            name: 'Meta AI (FAIR)',
            founded: 2013,
            significance: 'LLaMA, PyTorch, open research'
        },
        google_brain: {
            name: 'Google Brain',
            founded: 2011,
            significance: 'TensorFlow, Transformer (merged with DeepMind)'
        },
        microsoft_research: {
            name: 'Microsoft Research AI',
            significance: 'Azure AI, Copilot, Phi models'
        },
        nvidia_ai: {
            name: 'NVIDIA AI Research',
            significance: 'CUDA, GPU computing, AI hardware'
        }
    },

    // ===========================================================================
    // AI PIONEERS
    // ===========================================================================
    pioneers: {
        turing: { name: 'Alan Turing', years: '1912-1954', contributions: ['Turing Machine', 'Turing Test', 'Code breaking'] },
        mccarthy: { name: 'John McCarthy', years: '1927-2011', contributions: ['Coined "AI"', 'LISP', 'Dartmouth Conference'] },
        minsky: { name: 'Marvin Minsky', years: '1927-2016', contributions: ['AI Lab co-founder', 'Neural networks', 'Frames'] },
        shannon: { name: 'Claude Shannon', years: '1916-2001', contributions: ['Information theory', 'Chess programming'] },
        hinton: { name: 'Geoffrey Hinton', years: '1947-', contributions: ['Backpropagation', 'Deep learning', 'Capsule networks'] },
        lecun: { name: 'Yann LeCun', years: '1960-', contributions: ['CNN', 'LeNet', 'Meta Chief AI Scientist'] },
        bengio: { name: 'Yoshua Bengio', years: '1964-', contributions: ['Deep learning', 'Attention mechanisms', 'MILA'] },
        ng: { name: 'Andrew Ng', years: '1976-', contributions: ['Google Brain', 'Coursera ML course', 'AI education'] },
        goodfellow: { name: 'Ian Goodfellow', years: '1985-', contributions: ['GANs', 'Deep learning textbook'] },
        sutskever: { name: 'Ilya Sutskever', years: '1985-', contributions: ['OpenAI co-founder', 'AlexNet', 'GPT'] },
        vaswani: { name: 'Ashish Vaswani', years: '-', contributions: ['Transformer architecture'] },
        altman: { name: 'Sam Altman', years: '1985-', contributions: ['OpenAI CEO', 'Y Combinator'] },
        hassabis: { name: 'Demis Hassabis', years: '1976-', contributions: ['DeepMind founder', 'AlphaGo', 'AlphaFold'] }
    }
};

// API Endpoints
app.get('/api/ai/categories', (c) => c.json({ success: true, categories: Object.keys(AI_ML_HISTORY) }));

app.get('/api/ai/search', (c) => {
    const query = (c.req.query('q') || '').toLowerCase();
    const results: any[] = [];
    Object.entries(AI_ML_HISTORY).forEach(([cat, items]) => {
        Object.entries(items).forEach(([key, item]: [string, any]) => {
            if ((item.name || key).toLowerCase().includes(query) || (item.significance && item.significance.toLowerCase().includes(query))) {
                results.push({ category: cat, key, ...item });
            }
        });
    });
    return c.json({ success: true, resultCount: results.length, results });
});

app.get('/api/ai/category/:category', (c) => {
    const cat = c.req.param('category') as keyof typeof AI_ML_HISTORY;
    if (!AI_ML_HISTORY[cat]) return c.json({ error: 'Not found' }, 404);
    return c.json({ success: true, category: cat, items: AI_ML_HISTORY[cat] });
});

app.get('/api/ai/pioneers', (c) => c.json({ success: true, pioneers: AI_ML_HISTORY.pioneers }));
app.get('/api/ai/llms', (c) => c.json({ success: true, llms: AI_ML_HISTORY.transformerEra }));
app.get('/api/ai/deep-learning', (c) => c.json({ success: true, deepLearning: AI_ML_HISTORY.deepLearning }));
app.get('/api/ai/generative', (c) => c.json({ success: true, generativeAI: AI_ML_HISTORY.generativeAI }));
app.get('/api/ai/institutions', (c) => c.json({ success: true, institutions: AI_ML_HISTORY.institutions }));

app.get('/api/ai/timeline', (c) => {
    const timeline: any[] = [];
    Object.entries(AI_ML_HISTORY).forEach(([cat, items]) => {
        Object.entries(items).forEach(([key, item]: [string, any]) => {
            if (item.year) timeline.push({ year: item.year, name: item.name || key, category: cat, significance: item.significance });
        });
    });
    timeline.sort((a, b) => a.year - b.year);
    return c.json({ success: true, timeline });
});

app.get('/health', (c) => c.json({ status: 'healthy', worker: 'ai-ml-history-worker' }));

export default app;
