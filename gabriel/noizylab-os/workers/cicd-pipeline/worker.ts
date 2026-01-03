/**
 * ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗ 
 * ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗
 * ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝
 * ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗
 * ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝
 * ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ 
 * 
 * CI/CD PIPELINE WORKER - Continuous Integration & Deployment Expert
 * Round 5: DevOps & Infrastructure Legends
 * 
 * The ultimate CI/CD expert knowing GitHub Actions, Jenkins, GitLab CI,
 * CircleCI, Azure DevOps, TeamCity, Travis CI, ArgoCD, Spinnaker, and more!
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  AI: any;
  CICD_KV: KVNamespace;
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// ═══════════════════════════════════════════════════════════════════
// CI/CD PLATFORM KNOWLEDGE BASE
// ═══════════════════════════════════════════════════════════════════

const CICD_PLATFORMS = {
  'github-actions': {
    name: 'GitHub Actions',
    vendor: 'GitHub/Microsoft',
    year: 2019,
    type: 'Cloud-native',
    languages: ['YAML'],
    features: [
      'Matrix builds',
      'Reusable workflows',
      'Self-hosted runners',
      'GitHub-hosted runners',
      'Secrets management',
      'Environments',
      'Caching',
      'Artifacts',
      'Container actions',
      'Composite actions'
    ],
    marketplaceActions: 15000,
    pricing: 'Free tier + minutes-based',
    strengths: [
      'Native GitHub integration',
      'Huge marketplace',
      'Easy to start',
      'Great for open source',
      'Container-first design'
    ],
    configFile: '.github/workflows/*.yml',
    documentation: 'https://docs.github.com/en/actions'
  },
  'jenkins': {
    name: 'Jenkins',
    vendor: 'Jenkins Community',
    year: 2011,
    type: 'Self-hosted',
    languages: ['Groovy', 'Declarative Pipeline', 'Scripted Pipeline'],
    features: [
      'Pipeline as Code',
      'Distributed builds',
      'Plugin ecosystem (1800+)',
      'Blue Ocean UI',
      'Shared libraries',
      'Declarative & scripted pipelines',
      'Master/agent architecture',
      'Credentials management',
      'Build triggers',
      'Parameterized builds'
    ],
    plugins: 1800,
    pricing: 'Free & open source',
    strengths: [
      'Extremely flexible',
      'Massive plugin ecosystem',
      'Self-hosted control',
      'Enterprise-ready',
      'Battle-tested at scale'
    ],
    configFile: 'Jenkinsfile',
    documentation: 'https://www.jenkins.io/doc/'
  },
  'gitlab-ci': {
    name: 'GitLab CI/CD',
    vendor: 'GitLab',
    year: 2015,
    type: 'Integrated',
    languages: ['YAML'],
    features: [
      'Auto DevOps',
      'Container Registry',
      'Kubernetes integration',
      'Review Apps',
      'Feature flags',
      'Security scanning (SAST/DAST)',
      'Multi-project pipelines',
      'Parent-child pipelines',
      'DAG pipelines',
      'Merge trains'
    ],
    pricing: 'Free tier + paid tiers',
    strengths: [
      'Complete DevOps platform',
      'Built-in security scanning',
      'Kubernetes-native',
      'Auto DevOps magic',
      'Single application for full DevOps'
    ],
    configFile: '.gitlab-ci.yml',
    documentation: 'https://docs.gitlab.com/ee/ci/'
  },
  'circleci': {
    name: 'CircleCI',
    vendor: 'CircleCI',
    year: 2011,
    type: 'Cloud/Self-hosted',
    languages: ['YAML'],
    features: [
      'Orbs (reusable configs)',
      'Docker layer caching',
      'Parallelism',
      'Resource classes',
      'Insights dashboard',
      'Config policies',
      'Dynamic config',
      'SSH debugging',
      'Test splitting',
      'Approval workflows'
    ],
    orbs: 3000,
    pricing: 'Free tier + credits-based',
    strengths: [
      'Speed & performance',
      'Excellent Docker support',
      'Great parallelization',
      'Powerful caching',
      'Orbs marketplace'
    ],
    configFile: '.circleci/config.yml',
    documentation: 'https://circleci.com/docs/'
  },
  'azure-devops': {
    name: 'Azure DevOps Pipelines',
    vendor: 'Microsoft',
    year: 2018,
    type: 'Cloud/Self-hosted',
    languages: ['YAML', 'Classic Editor'],
    features: [
      'Multi-stage pipelines',
      'Template expressions',
      'Deployment jobs',
      'Environments',
      'Service connections',
      'Variable groups',
      'Approvals & checks',
      'Gates',
      'Release management',
      'Artifacts'
    ],
    pricing: 'Free tier + parallel jobs',
    strengths: [
      'Microsoft ecosystem integration',
      'Enterprise features',
      'Azure-native',
      'Comprehensive tooling',
      'YAML & visual designer'
    ],
    configFile: 'azure-pipelines.yml',
    documentation: 'https://docs.microsoft.com/azure/devops/pipelines/'
  },
  'argocd': {
    name: 'ArgoCD',
    vendor: 'Argo Project/CNCF',
    year: 2018,
    type: 'GitOps',
    languages: ['YAML', 'Kustomize', 'Helm', 'Jsonnet'],
    features: [
      'GitOps continuous delivery',
      'Declarative setup',
      'Multi-cluster support',
      'SSO integration',
      'RBAC',
      'Webhooks',
      'Health assessment',
      'Automated sync',
      'Rollback support',
      'Application sets'
    ],
    pricing: 'Free & open source',
    strengths: [
      'GitOps pioneer',
      'Kubernetes-native',
      'Declarative deployments',
      'Visual application state',
      'Multi-cluster management'
    ],
    configFile: 'Application CRD',
    documentation: 'https://argo-cd.readthedocs.io/'
  },
  'tekton': {
    name: 'Tekton',
    vendor: 'CD Foundation',
    year: 2019,
    type: 'Kubernetes-native',
    languages: ['YAML'],
    features: [
      'Task & Pipeline CRDs',
      'Triggers',
      'Catalog',
      'Dashboard',
      'Results',
      'Chains (supply chain security)',
      'Workspace volumes',
      'Parameter passing',
      'Conditions',
      'Finally tasks'
    ],
    pricing: 'Free & open source',
    strengths: [
      'Cloud-native primitives',
      'Kubernetes-native',
      'Standardized CI/CD',
      'Vendor-neutral',
      'Building block approach'
    ],
    configFile: 'Task/Pipeline CRDs',
    documentation: 'https://tekton.dev/docs/'
  },
  'drone': {
    name: 'Drone CI',
    vendor: 'Harness',
    year: 2014,
    type: 'Container-native',
    languages: ['YAML', 'Starlark'],
    features: [
      'Container-first design',
      'Plugins as containers',
      'Multi-platform builds',
      'Kubernetes executor',
      'Promotion pipelines',
      'Secrets management',
      'Configuration as code',
      'Cron scheduler',
      'Matrix builds',
      'Jsonnet support'
    ],
    pricing: 'Open source + Enterprise',
    strengths: [
      'Simple & lightweight',
      'Container-native',
      'Easy plugin creation',
      'Fast startup',
      'Minimal configuration'
    ],
    configFile: '.drone.yml',
    documentation: 'https://docs.drone.io/'
  },
  'spinnaker': {
    name: 'Spinnaker',
    vendor: 'Netflix/Google',
    year: 2015,
    type: 'Multi-cloud CD',
    languages: ['JSON', 'Pipeline Templates'],
    features: [
      'Multi-cloud deployments',
      'Deployment strategies',
      'Canary analysis',
      'Blue/green deployments',
      'Rolling updates',
      'Pipeline templates',
      'Manual judgments',
      'Automated rollbacks',
      'Cloud provider plugins',
      'Chaos monkey integration'
    ],
    pricing: 'Free & open source',
    strengths: [
      'Multi-cloud expertise',
      'Advanced deployment strategies',
      'Netflix-proven scale',
      'Canary analysis',
      'Enterprise deployments'
    ],
    configFile: 'Pipeline JSON/Templates',
    documentation: 'https://spinnaker.io/docs/'
  },
  'teamcity': {
    name: 'TeamCity',
    vendor: 'JetBrains',
    year: 2006,
    type: 'Self-hosted/Cloud',
    languages: ['Kotlin DSL', 'XML'],
    features: [
      'Build chains',
      'Personal builds',
      'Pre-tested commits',
      'Build grid',
      'VCS triggers',
      'Kotlin DSL configuration',
      'Build templates',
      'Composite builds',
      'Remote run',
      'Code coverage'
    ],
    pricing: 'Free tier + Commercial',
    strengths: [
      'JetBrains IDE integration',
      'Kotlin DSL power',
      'Personal builds',
      'Excellent UI',
      'Enterprise features'
    ],
    configFile: '.teamcity/settings.kts',
    documentation: 'https://www.jetbrains.com/help/teamcity/'
  }
};

// ═══════════════════════════════════════════════════════════════════
// PIPELINE PATTERNS & BEST PRACTICES
// ═══════════════════════════════════════════════════════════════════

const PIPELINE_PATTERNS = {
  stages: [
    {
      name: 'Build',
      description: 'Compile code, build containers, create artifacts',
      tasks: ['Compile', 'Lint', 'Build Docker image', 'Create artifacts']
    },
    {
      name: 'Test',
      description: 'Run all test suites',
      tasks: ['Unit tests', 'Integration tests', 'E2E tests', 'Coverage']
    },
    {
      name: 'Security',
      description: 'Security scanning and compliance',
      tasks: ['SAST', 'DAST', 'Dependency scan', 'Container scan', 'Secrets detection']
    },
    {
      name: 'Deploy',
      description: 'Deploy to environments',
      tasks: ['Dev deploy', 'Staging deploy', 'Production deploy']
    },
    {
      name: 'Verify',
      description: 'Post-deployment verification',
      tasks: ['Smoke tests', 'Health checks', 'Monitoring alerts']
    }
  ],
  deploymentStrategies: {
    'rolling': {
      name: 'Rolling Update',
      description: 'Gradually replace instances',
      riskLevel: 'Medium',
      rollbackTime: 'Fast',
      resourceOverhead: 'Low'
    },
    'blue-green': {
      name: 'Blue-Green Deployment',
      description: 'Maintain two identical environments',
      riskLevel: 'Low',
      rollbackTime: 'Instant',
      resourceOverhead: 'High (2x)'
    },
    'canary': {
      name: 'Canary Release',
      description: 'Gradually shift traffic to new version',
      riskLevel: 'Low',
      rollbackTime: 'Fast',
      resourceOverhead: 'Medium'
    },
    'recreate': {
      name: 'Recreate',
      description: 'Terminate old, deploy new',
      riskLevel: 'High',
      rollbackTime: 'Slow',
      resourceOverhead: 'None'
    },
    'a-b-testing': {
      name: 'A/B Testing',
      description: 'Route subset of users to new version',
      riskLevel: 'Low',
      rollbackTime: 'Instant',
      resourceOverhead: 'Medium'
    },
    'shadow': {
      name: 'Shadow Deployment',
      description: 'Mirror traffic to new version without affecting users',
      riskLevel: 'Very Low',
      rollbackTime: 'N/A',
      resourceOverhead: 'High'
    }
  },
  bestPractices: [
    'Pipeline as Code - Version control your pipelines',
    'Fail fast - Run quick checks first',
    'Parallelize where possible',
    'Cache dependencies aggressively',
    'Use immutable artifacts',
    'Implement proper secret management',
    'Add manual approval gates for production',
    'Monitor pipeline metrics',
    'Keep builds under 10 minutes',
    'Use ephemeral build environments'
  ]
};

// ═══════════════════════════════════════════════════════════════════
// GITHUB ACTIONS TEMPLATES
// ═══════════════════════════════════════════════════════════════════

const GITHUB_ACTIONS_TEMPLATES = {
  'node-ci': `name: Node.js CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18.x, 20.x, 22.x]
    
    steps:
    - uses: actions/checkout@v4
    - name: Use Node.js \${{ matrix.node-version }}
      uses: actions/setup-node@v4
      with:
        node-version: \${{ matrix.node-version }}
        cache: 'npm'
    - run: npm ci
    - run: npm run build --if-present
    - run: npm test

  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Run Snyk to check for vulnerabilities
      uses: snyk/actions/node@master
      env:
        SNYK_TOKEN: \${{ secrets.SNYK_TOKEN }}`,

  'docker-build': `name: Docker Build & Push

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: \${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3
    
    - name: Login to Container Registry
      uses: docker/login-action@v3
      with:
        registry: \${{ env.REGISTRY }}
        username: \${{ github.actor }}
        password: \${{ secrets.GITHUB_TOKEN }}
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: \${{ env.REGISTRY }}/\${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=semver,pattern={{version}}
          type=sha
    
    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: \${{ steps.meta.outputs.tags }}
        labels: \${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max`,

  'deploy-cloudflare': `name: Deploy to Cloudflare Workers

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    name: Deploy
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Deploy to Cloudflare Workers
      uses: cloudflare/wrangler-action@v3
      with:
        apiToken: \${{ secrets.CLOUDFLARE_API_TOKEN }}
        accountId: \${{ secrets.CLOUDFLARE_ACCOUNT_ID }}`
};

// ═══════════════════════════════════════════════════════════════════
// API ENDPOINTS
// ═══════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  return c.json({
    worker: 'cicd-pipeline',
    status: 'operational',
    version: '1.0.0',
    description: 'CI/CD Pipeline Expert - GitHub Actions, Jenkins, GitLab CI & more',
    endpoints: [
      'GET /platforms - List all CI/CD platforms',
      'GET /platform/:name - Get platform details',
      'GET /patterns - Pipeline patterns & best practices',
      'GET /strategies - Deployment strategies',
      'GET /templates/:type - Get pipeline templates',
      'GET /compare - Compare CI/CD platforms',
      'POST /generate - Generate pipeline config',
      'POST /ask - Ask CI/CD questions'
    ],
    capabilities: [
      'CI/CD platform expertise',
      'Pipeline generation',
      'Best practices guidance',
      'Deployment strategies',
      'Template library'
    ]
  });
});

app.get('/platforms', (c) => {
  const platforms = Object.entries(CICD_PLATFORMS).map(([key, platform]) => ({
    id: key,
    name: platform.name,
    vendor: platform.vendor,
    year: platform.year,
    type: platform.type,
    configFile: platform.configFile
  }));

  return c.json({
    count: platforms.length,
    platforms,
    categories: {
      cloud: ['github-actions', 'circleci', 'azure-devops'],
      selfHosted: ['jenkins', 'teamcity', 'drone'],
      gitops: ['argocd', 'tekton'],
      multiCloud: ['spinnaker'],
      integrated: ['gitlab-ci']
    }
  });
});

app.get('/platform/:name', (c) => {
  const name = c.req.param('name');
  const platform = CICD_PLATFORMS[name as keyof typeof CICD_PLATFORMS];

  if (!platform) {
    return c.json({ error: 'Platform not found', available: Object.keys(CICD_PLATFORMS) }, 404);
  }

  return c.json(platform);
});

app.get('/patterns', (c) => {
  return c.json({
    pipelineStages: PIPELINE_PATTERNS.stages,
    bestPractices: PIPELINE_PATTERNS.bestPractices,
    tips: [
      'Keep pipelines fast - aim for under 10 minutes',
      'Use caching for dependencies',
      'Parallelize independent jobs',
      'Implement security scanning early',
      'Use semantic versioning for releases'
    ]
  });
});

app.get('/strategies', (c) => {
  return c.json({
    deploymentStrategies: PIPELINE_PATTERNS.deploymentStrategies,
    recommendation: {
      lowRisk: 'blue-green',
      costEffective: 'rolling',
      gradualRollout: 'canary',
      testing: 'shadow'
    }
  });
});

app.get('/templates/:type', (c) => {
  const type = c.req.param('type');
  const template = GITHUB_ACTIONS_TEMPLATES[type as keyof typeof GITHUB_ACTIONS_TEMPLATES];

  if (!template) {
    return c.json({
      error: 'Template not found',
      available: Object.keys(GITHUB_ACTIONS_TEMPLATES)
    }, 404);
  }

  return c.json({
    type,
    platform: 'GitHub Actions',
    template,
    usage: 'Save as .github/workflows/<name>.yml'
  });
});

app.get('/compare', (c) => {
  const comparison = {
    forOpenSource: {
      winner: 'GitHub Actions',
      reason: 'Free for public repos, huge marketplace, native GitHub integration'
    },
    forEnterprise: {
      winner: 'Jenkins or GitLab CI',
      reason: 'Self-hosted control, extensive customization, proven at scale'
    },
    forKubernetes: {
      winner: 'ArgoCD + Tekton',
      reason: 'GitOps native, Kubernetes-first design, declarative approach'
    },
    forMultiCloud: {
      winner: 'Spinnaker',
      reason: 'Built for multi-cloud, advanced deployment strategies'
    },
    forSimplicity: {
      winner: 'GitHub Actions or CircleCI',
      reason: 'Easy to start, great documentation, minimal setup'
    },
    forSpeed: {
      winner: 'CircleCI',
      reason: 'Excellent parallelization, Docker layer caching, resource classes'
    }
  };

  return c.json(comparison);
});

app.post('/generate', async (c) => {
  const { platform, language, features } = await c.req.json();

  const prompt = `Generate a CI/CD pipeline configuration for:
Platform: ${platform || 'github-actions'}
Language/Framework: ${language || 'Node.js'}
Features needed: ${(features || ['build', 'test', 'deploy']).join(', ')}

Provide a complete, production-ready pipeline configuration with comments explaining each section.`;

  try {
    const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
      messages: [
        {
          role: 'system',
          content: `You are a CI/CD expert specializing in ${platform || 'GitHub Actions'}. Generate production-ready pipeline configurations with best practices.`
        },
        { role: 'user', content: prompt }
      ],
      max_tokens: 2000
    });

    return c.json({
      platform: platform || 'github-actions',
      language: language || 'Node.js',
      features: features || ['build', 'test', 'deploy'],
      generatedConfig: response.response
    });
  } catch (error) {
    return c.json({ error: 'AI generation failed', details: String(error) }, 500);
  }
});

app.post('/ask', async (c) => {
  const { question } = await c.req.json();

  if (!question) {
    return c.json({ error: 'Question is required' }, 400);
  }

  const systemPrompt = `You are a CI/CD and DevOps expert with deep knowledge of:
- GitHub Actions, Jenkins, GitLab CI, CircleCI, Azure DevOps
- ArgoCD, Tekton, Spinnaker, Drone CI, TeamCity
- Pipeline design patterns and best practices
- Deployment strategies (blue-green, canary, rolling)
- Container-based CI/CD, Docker, Kubernetes
- GitOps principles and implementation
- Security scanning (SAST, DAST, SCA)
- Pipeline optimization and caching

Provide detailed, practical answers with code examples when appropriate.`;

  try {
    const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: question }
      ],
      max_tokens: 1500
    });

    return c.json({
      question,
      answer: response.response,
      relatedTopics: [
        'Pipeline patterns',
        'Deployment strategies',
        'Security scanning',
        'Caching optimization'
      ]
    });
  } catch (error) {
    return c.json({ error: 'AI query failed', details: String(error) }, 500);
  }
});

export default app;
