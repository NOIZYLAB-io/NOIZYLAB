/**
 * GORUNFREEX1TRILLION - DEVOPS KIT
 * Docker, Kubernetes, CI/CD, Monitoring, Infrastructure as Code
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// DOCKERFILE GENERATOR
// ============================================

class DockerfileGenerator {
  constructor(options = {}) {
    this.baseImage = options.baseImage || 'node:20-alpine';
    this.workdir = options.workdir || '/app';
    this.port = options.port || 3000;
    this.instructions = [];
  }

  from(image, as) {
    this.instructions.push(`FROM ${image}${as ? ` AS ${as}` : ''}`);
    return this;
  }

  workdir(dir) {
    this.instructions.push(`WORKDIR ${dir}`);
    return this;
  }

  copy(src, dest) {
    this.instructions.push(`COPY ${src} ${dest}`);
    return this;
  }

  run(command) {
    this.instructions.push(`RUN ${command}`);
    return this;
  }

  env(key, value) {
    this.instructions.push(`ENV ${key}=${value}`);
    return this;
  }

  expose(port) {
    this.instructions.push(`EXPOSE ${port}`);
    return this;
  }

  cmd(command) {
    const cmd = Array.isArray(command) ? JSON.stringify(command) : `["${command}"]`;
    this.instructions.push(`CMD ${cmd}`);
    return this;
  }

  entrypoint(command) {
    const ep = Array.isArray(command) ? JSON.stringify(command) : `["${command}"]`;
    this.instructions.push(`ENTRYPOINT ${ep}`);
    return this;
  }

  label(key, value) {
    this.instructions.push(`LABEL ${key}="${value}"`);
    return this;
  }

  arg(name, defaultValue) {
    this.instructions.push(`ARG ${name}${defaultValue ? `=${defaultValue}` : ''}`);
    return this;
  }

  user(username) {
    this.instructions.push(`USER ${username}`);
    return this;
  }

  volume(path) {
    this.instructions.push(`VOLUME ${path}`);
    return this;
  }

  healthcheck(options) {
    const parts = ['HEALTHCHECK'];
    if (options.interval) parts.push(`--interval=${options.interval}`);
    if (options.timeout) parts.push(`--timeout=${options.timeout}`);
    if (options.retries) parts.push(`--retries=${options.retries}`);
    parts.push(`CMD ${options.cmd}`);
    this.instructions.push(parts.join(' '));
    return this;
  }

  comment(text) {
    this.instructions.push(`# ${text}`);
    return this;
  }

  blank() {
    this.instructions.push('');
    return this;
  }

  // Preset for Node.js app
  nodeApp(options = {}) {
    return this
      .from(options.baseImage || 'node:20-alpine')
      .workdir('/app')
      .comment('Install dependencies')
      .copy('package*.json', './')
      .run('npm ci --only=production')
      .blank()
      .comment('Copy application code')
      .copy('.', '.')
      .blank()
      .env('NODE_ENV', 'production')
      .expose(options.port || 3000)
      .cmd(['node', options.entry || 'index.js']);
  }

  // Multi-stage build
  multiStage(options = {}) {
    return this
      .comment('Build stage')
      .from('node:20-alpine', 'builder')
      .workdir('/app')
      .copy('package*.json', './')
      .run('npm ci')
      .copy('.', '.')
      .run('npm run build')
      .blank()
      .comment('Production stage')
      .from('node:20-alpine')
      .workdir('/app')
      .copy('--from=builder /app/dist', './dist')
      .copy('--from=builder /app/node_modules', './node_modules')
      .copy('--from=builder /app/package.json', './')
      .env('NODE_ENV', 'production')
      .expose(options.port || 3000)
      .cmd(['node', 'dist/index.js']);
  }

  generate() {
    if (this.instructions.length === 0) {
      this.nodeApp();
    }
    return this.instructions.join('\n');
  }
}

// ============================================
// DOCKER COMPOSE GENERATOR
// ============================================

class DockerComposeGenerator {
  constructor(options = {}) {
    this.version = options.version || '3.8';
    this.services = {};
    this.networks = {};
    this.volumes = {};
  }

  service(name, config) {
    this.services[name] = {
      image: config.image,
      build: config.build,
      container_name: config.containerName,
      ports: config.ports,
      environment: config.environment,
      env_file: config.envFile,
      volumes: config.volumes,
      depends_on: config.dependsOn,
      networks: config.networks,
      restart: config.restart || 'unless-stopped',
      command: config.command,
      healthcheck: config.healthcheck,
      deploy: config.deploy,
      labels: config.labels
    };

    // Remove undefined values
    Object.keys(this.services[name]).forEach(key => {
      if (this.services[name][key] === undefined) {
        delete this.services[name][key];
      }
    });

    return this;
  }

  network(name, config = {}) {
    this.networks[name] = {
      driver: config.driver || 'bridge',
      ...config
    };
    return this;
  }

  volume(name, config = {}) {
    this.volumes[name] = config.driver ? config : null;
    return this;
  }

  // Preset: App + Database
  withPostgres(appConfig, dbConfig = {}) {
    return this
      .service('app', {
        build: '.',
        ports: [`${appConfig.port || 3000}:3000`],
        environment: {
          DATABASE_URL: 'postgres://postgres:postgres@db:5432/app',
          ...appConfig.environment
        },
        dependsOn: ['db'],
        networks: ['app-network']
      })
      .service('db', {
        image: 'postgres:15-alpine',
        environment: {
          POSTGRES_USER: dbConfig.user || 'postgres',
          POSTGRES_PASSWORD: dbConfig.password || 'postgres',
          POSTGRES_DB: dbConfig.database || 'app'
        },
        volumes: ['postgres-data:/var/lib/postgresql/data'],
        networks: ['app-network']
      })
      .network('app-network')
      .volume('postgres-data');
  }

  // Preset: App + Redis
  withRedis(appConfig) {
    return this
      .service('app', {
        build: '.',
        ports: [`${appConfig.port || 3000}:3000`],
        environment: {
          REDIS_URL: 'redis://redis:6379',
          ...appConfig.environment
        },
        dependsOn: ['redis'],
        networks: ['app-network']
      })
      .service('redis', {
        image: 'redis:7-alpine',
        volumes: ['redis-data:/data'],
        networks: ['app-network']
      })
      .network('app-network')
      .volume('redis-data');
  }

  generate() {
    const compose = {
      version: this.version,
      services: this.services
    };

    if (Object.keys(this.networks).length > 0) {
      compose.networks = this.networks;
    }

    if (Object.keys(this.volumes).length > 0) {
      compose.volumes = this.volumes;
    }

    return this.toYAML(compose);
  }

  toYAML(obj, indent = 0) {
    const spaces = '  '.repeat(indent);
    let yaml = '';

    for (const [key, value] of Object.entries(obj)) {
      if (value === null || value === undefined) continue;

      if (Array.isArray(value)) {
        yaml += `${spaces}${key}:\n`;
        value.forEach(item => {
          if (typeof item === 'object') {
            yaml += `${spaces}  -\n`;
            yaml += this.toYAML(item, indent + 2);
          } else {
            yaml += `${spaces}  - ${item}\n`;
          }
        });
      } else if (typeof value === 'object') {
        yaml += `${spaces}${key}:\n`;
        yaml += this.toYAML(value, indent + 1);
      } else {
        yaml += `${spaces}${key}: ${value}\n`;
      }
    }

    return yaml;
  }
}

// ============================================
// KUBERNETES MANIFEST GENERATOR
// ============================================

class K8sManifestGenerator {
  constructor(options = {}) {
    this.namespace = options.namespace || 'default';
    this.manifests = [];
  }

  deployment(name, config) {
    const manifest = {
      apiVersion: 'apps/v1',
      kind: 'Deployment',
      metadata: {
        name,
        namespace: this.namespace,
        labels: config.labels || { app: name }
      },
      spec: {
        replicas: config.replicas || 1,
        selector: {
          matchLabels: config.labels || { app: name }
        },
        template: {
          metadata: {
            labels: config.labels || { app: name }
          },
          spec: {
            containers: [{
              name,
              image: config.image,
              ports: config.ports?.map(p => ({ containerPort: p })),
              env: config.env?.map(e => ({ name: e.name, value: e.value })),
              envFrom: config.envFrom,
              resources: config.resources || {
                requests: { memory: '128Mi', cpu: '100m' },
                limits: { memory: '256Mi', cpu: '200m' }
              },
              livenessProbe: config.livenessProbe,
              readinessProbe: config.readinessProbe
            }]
          }
        }
      }
    };

    this.manifests.push(manifest);
    return this;
  }

  service(name, config) {
    const manifest = {
      apiVersion: 'v1',
      kind: 'Service',
      metadata: {
        name,
        namespace: this.namespace
      },
      spec: {
        type: config.type || 'ClusterIP',
        selector: config.selector || { app: name },
        ports: config.ports?.map(p => ({
          port: p.port,
          targetPort: p.targetPort || p.port,
          protocol: p.protocol || 'TCP'
        }))
      }
    };

    this.manifests.push(manifest);
    return this;
  }

  ingress(name, config) {
    const manifest = {
      apiVersion: 'networking.k8s.io/v1',
      kind: 'Ingress',
      metadata: {
        name,
        namespace: this.namespace,
        annotations: config.annotations || {}
      },
      spec: {
        rules: config.rules?.map(r => ({
          host: r.host,
          http: {
            paths: r.paths?.map(p => ({
              path: p.path,
              pathType: p.pathType || 'Prefix',
              backend: {
                service: {
                  name: p.serviceName,
                  port: { number: p.servicePort }
                }
              }
            }))
          }
        }))
      }
    };

    if (config.tls) {
      manifest.spec.tls = config.tls;
    }

    this.manifests.push(manifest);
    return this;
  }

  configMap(name, data) {
    const manifest = {
      apiVersion: 'v1',
      kind: 'ConfigMap',
      metadata: {
        name,
        namespace: this.namespace
      },
      data
    };

    this.manifests.push(manifest);
    return this;
  }

  secret(name, data) {
    const encodedData = {};
    for (const [key, value] of Object.entries(data)) {
      encodedData[key] = Buffer.from(value).toString('base64');
    }

    const manifest = {
      apiVersion: 'v1',
      kind: 'Secret',
      metadata: {
        name,
        namespace: this.namespace
      },
      type: 'Opaque',
      data: encodedData
    };

    this.manifests.push(manifest);
    return this;
  }

  hpa(name, config) {
    const manifest = {
      apiVersion: 'autoscaling/v2',
      kind: 'HorizontalPodAutoscaler',
      metadata: {
        name,
        namespace: this.namespace
      },
      spec: {
        scaleTargetRef: {
          apiVersion: 'apps/v1',
          kind: 'Deployment',
          name: config.deploymentName || name
        },
        minReplicas: config.minReplicas || 1,
        maxReplicas: config.maxReplicas || 10,
        metrics: [{
          type: 'Resource',
          resource: {
            name: 'cpu',
            target: {
              type: 'Utilization',
              averageUtilization: config.targetCPU || 80
            }
          }
        }]
      }
    };

    this.manifests.push(manifest);
    return this;
  }

  generate() {
    return this.manifests.map(m => this.toYAML(m)).join('---\n');
  }

  toYAML(obj, indent = 0) {
    const spaces = '  '.repeat(indent);
    let yaml = '';

    for (const [key, value] of Object.entries(obj)) {
      if (value === null || value === undefined) continue;

      if (Array.isArray(value)) {
        yaml += `${spaces}${key}:\n`;
        value.forEach(item => {
          if (typeof item === 'object') {
            const firstKey = Object.keys(item)[0];
            yaml += `${spaces}- ${firstKey}: ${typeof item[firstKey] === 'object' ? '' : item[firstKey]}\n`;
            if (typeof item[firstKey] === 'object') {
              yaml += this.toYAML(item[firstKey], indent + 2);
            }
            const rest = { ...item };
            delete rest[firstKey];
            if (Object.keys(rest).length > 0) {
              yaml += this.toYAML(rest, indent + 1);
            }
          } else {
            yaml += `${spaces}- ${item}\n`;
          }
        });
      } else if (typeof value === 'object') {
        yaml += `${spaces}${key}:\n`;
        yaml += this.toYAML(value, indent + 1);
      } else {
        yaml += `${spaces}${key}: ${value}\n`;
      }
    }

    return yaml;
  }
}

// ============================================
// CI/CD PIPELINE GENERATOR
// ============================================

class CIPipelineGenerator {
  constructor(platform = 'github') {
    this.platform = platform;
    this.config = {};
  }

  githubActions(config) {
    return {
      name: config.name || 'CI/CD Pipeline',
      on: config.on || {
        push: { branches: ['main', 'master'] },
        pull_request: { branches: ['main', 'master'] }
      },
      env: config.env,
      jobs: {
        build: {
          'runs-on': 'ubuntu-latest',
          steps: [
            { uses: 'actions/checkout@v4' },
            {
              name: 'Setup Node.js',
              uses: 'actions/setup-node@v4',
              with: { 'node-version': config.nodeVersion || '20' }
            },
            { name: 'Install dependencies', run: 'npm ci' },
            ...(config.lint ? [{ name: 'Lint', run: 'npm run lint' }] : []),
            ...(config.test ? [{ name: 'Test', run: 'npm test' }] : []),
            ...(config.build ? [{ name: 'Build', run: 'npm run build' }] : []),
            ...(config.customSteps || [])
          ]
        },
        ...(config.deploy ? {
          deploy: {
            needs: 'build',
            'runs-on': 'ubuntu-latest',
            if: "github.ref == 'refs/heads/main'",
            steps: config.deploySteps || []
          }
        } : {})
      }
    };
  }

  gitlabCI(config) {
    return {
      image: config.image || 'node:20',
      stages: ['install', 'test', 'build', 'deploy'],
      cache: {
        paths: ['node_modules/']
      },
      install: {
        stage: 'install',
        script: ['npm ci']
      },
      test: {
        stage: 'test',
        script: ['npm test']
      },
      build: {
        stage: 'build',
        script: ['npm run build'],
        artifacts: {
          paths: ['dist/']
        }
      },
      ...(config.deploy ? {
        deploy: {
          stage: 'deploy',
          script: config.deployScript || ['echo "Deploy"'],
          only: ['main']
        }
      } : {})
    };
  }

  generate(config = {}) {
    switch (this.platform) {
      case 'github':
        return this.toYAML(this.githubActions(config));
      case 'gitlab':
        return this.toYAML(this.gitlabCI(config));
      default:
        return '';
    }
  }

  toYAML(obj, indent = 0) {
    // Reuse from K8s generator
    const spaces = '  '.repeat(indent);
    let yaml = '';

    for (const [key, value] of Object.entries(obj)) {
      if (value === null || value === undefined) continue;

      if (Array.isArray(value)) {
        yaml += `${spaces}${key}:\n`;
        value.forEach(item => {
          if (typeof item === 'object') {
            yaml += `${spaces}-\n`;
            yaml += this.toYAML(item, indent + 1);
          } else {
            yaml += `${spaces}- ${item}\n`;
          }
        });
      } else if (typeof value === 'object') {
        yaml += `${spaces}${key}:\n`;
        yaml += this.toYAML(value, indent + 1);
      } else {
        yaml += `${spaces}${key}: ${JSON.stringify(value)}\n`;
      }
    }

    return yaml;
  }
}

// ============================================
// HEALTH CHECKER
// ============================================

class HealthChecker extends EventEmitter {
  constructor() {
    super();
    this.checks = new Map();
    this.results = new Map();
  }

  addCheck(name, checker) {
    this.checks.set(name, checker);
    return this;
  }

  async runChecks() {
    const results = {};

    for (const [name, checker] of this.checks) {
      try {
        const start = Date.now();
        const result = await checker();
        results[name] = {
          status: result ? 'healthy' : 'unhealthy',
          duration: Date.now() - start,
          ...result
        };
      } catch (error) {
        results[name] = {
          status: 'unhealthy',
          error: error.message
        };
      }
    }

    const allHealthy = Object.values(results).every(r => r.status === 'healthy');
    this.emit('checked', { healthy: allHealthy, results });

    return { healthy: allHealthy, results };
  }

  // Common health checks
  static httpCheck(url, timeout = 5000) {
    return async () => {
      const start = Date.now();
      try {
        // Simulated HTTP check
        return { status: 'healthy', responseTime: Date.now() - start };
      } catch (error) {
        throw error;
      }
    };
  }

  static dbCheck(connection) {
    return async () => {
      // Simulated DB check
      return { status: 'healthy', connections: 5 };
    };
  }

  static diskCheck(threshold = 90) {
    return async () => {
      const usage = 45; // Simulated
      return {
        status: usage < threshold ? 'healthy' : 'unhealthy',
        usage: `${usage}%`
      };
    };
  }

  static memoryCheck(threshold = 90) {
    return async () => {
      const used = process.memoryUsage();
      const usedMB = Math.round(used.heapUsed / 1024 / 1024);
      return { status: 'healthy', usedMB };
    };
  }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  DockerfileGenerator,
  DockerComposeGenerator,
  K8sManifestGenerator,
  CIPipelineGenerator,
  HealthChecker,

  createDockerfile: (options) => new DockerfileGenerator(options),
  createCompose: (options) => new DockerComposeGenerator(options),
  createK8s: (options) => new K8sManifestGenerator(options),
  createPipeline: (platform) => new CIPipelineGenerator(platform),
  createHealthChecker: () => new HealthChecker()
};
