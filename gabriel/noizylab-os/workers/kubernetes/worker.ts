/**
 * ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗ 
 * ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗
 * ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝
 * ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗
 * ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝
 * ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ 
 * 
 * KUBERNETES WORKER - Container Orchestration Expert
 * Round 5: DevOps & Infrastructure Legends
 * 
 * Master of Kubernetes, Helm, Operators, Service Mesh, and cloud-native!
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    AI: any;
    K8S_KV: KVNamespace;
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// ═══════════════════════════════════════════════════════════════════
// KUBERNETES KNOWLEDGE BASE
// ═══════════════════════════════════════════════════════════════════

const K8S_RESOURCES = {
    workloads: {
        'Pod': {
            description: 'Smallest deployable unit, contains one or more containers',
            apiVersion: 'v1',
            kind: 'Pod',
            useCase: 'Basic container runtime unit'
        },
        'Deployment': {
            description: 'Declarative updates for Pods and ReplicaSets',
            apiVersion: 'apps/v1',
            kind: 'Deployment',
            useCase: 'Stateless applications, rolling updates'
        },
        'StatefulSet': {
            description: 'Manages stateful applications with stable network identity',
            apiVersion: 'apps/v1',
            kind: 'StatefulSet',
            useCase: 'Databases, distributed systems'
        },
        'DaemonSet': {
            description: 'Ensures all nodes run a copy of a Pod',
            apiVersion: 'apps/v1',
            kind: 'DaemonSet',
            useCase: 'Log collectors, monitoring agents'
        },
        'Job': {
            description: 'Creates Pods that run to completion',
            apiVersion: 'batch/v1',
            kind: 'Job',
            useCase: 'Batch processing, one-time tasks'
        },
        'CronJob': {
            description: 'Creates Jobs on a time-based schedule',
            apiVersion: 'batch/v1',
            kind: 'CronJob',
            useCase: 'Scheduled tasks, periodic jobs'
        },
        'ReplicaSet': {
            description: 'Maintains stable set of replica Pods',
            apiVersion: 'apps/v1',
            kind: 'ReplicaSet',
            useCase: 'Usually managed by Deployment'
        }
    },
    networking: {
        'Service': {
            description: 'Exposes Pods as a network service',
            types: ['ClusterIP', 'NodePort', 'LoadBalancer', 'ExternalName'],
            apiVersion: 'v1'
        },
        'Ingress': {
            description: 'HTTP/HTTPS routing to Services',
            apiVersion: 'networking.k8s.io/v1',
            controllers: ['nginx', 'traefik', 'haproxy', 'istio', 'kong']
        },
        'NetworkPolicy': {
            description: 'Pod network traffic rules',
            apiVersion: 'networking.k8s.io/v1'
        },
        'Gateway': {
            description: 'Gateway API for advanced traffic routing',
            apiVersion: 'gateway.networking.k8s.io/v1'
        }
    },
    storage: {
        'PersistentVolume': {
            description: 'Cluster-level storage resource',
            apiVersion: 'v1'
        },
        'PersistentVolumeClaim': {
            description: 'Request for storage by a user',
            apiVersion: 'v1'
        },
        'StorageClass': {
            description: 'Describes storage "classes"',
            provisioners: ['kubernetes.io/aws-ebs', 'kubernetes.io/gce-pd', 'kubernetes.io/azure-disk']
        },
        'ConfigMap': {
            description: 'Non-confidential key-value configuration',
            apiVersion: 'v1'
        },
        'Secret': {
            description: 'Sensitive data storage',
            types: ['Opaque', 'kubernetes.io/tls', 'kubernetes.io/dockerconfigjson']
        }
    },
    security: {
        'ServiceAccount': {
            description: 'Identity for processes in Pods',
            apiVersion: 'v1'
        },
        'Role': {
            description: 'Namespace-scoped permissions',
            apiVersion: 'rbac.authorization.k8s.io/v1'
        },
        'ClusterRole': {
            description: 'Cluster-wide permissions',
            apiVersion: 'rbac.authorization.k8s.io/v1'
        },
        'RoleBinding': {
            description: 'Binds Role to subjects',
            apiVersion: 'rbac.authorization.k8s.io/v1'
        },
        'ClusterRoleBinding': {
            description: 'Binds ClusterRole to subjects',
            apiVersion: 'rbac.authorization.k8s.io/v1'
        },
        'PodSecurityPolicy': {
            description: 'Pod security standards (deprecated)',
            replacement: 'Pod Security Standards'
        }
    }
};

const K8S_DISTRIBUTIONS = {
    'vanilla': {
        name: 'Kubernetes (vanilla)',
        maintainer: 'CNCF',
        description: 'Upstream Kubernetes',
        installMethods: ['kubeadm', 'kops', 'kubespray']
    },
    'eks': {
        name: 'Amazon EKS',
        maintainer: 'AWS',
        description: 'Managed Kubernetes on AWS',
        features: ['Fargate support', 'IAM integration', 'VPC networking']
    },
    'gke': {
        name: 'Google GKE',
        maintainer: 'Google Cloud',
        description: 'Managed Kubernetes on GCP',
        features: ['Autopilot', 'GKE Enterprise', 'Anthos integration']
    },
    'aks': {
        name: 'Azure AKS',
        maintainer: 'Microsoft',
        description: 'Managed Kubernetes on Azure',
        features: ['Azure AD integration', 'Virtual nodes', 'Azure Arc']
    },
    'openshift': {
        name: 'Red Hat OpenShift',
        maintainer: 'Red Hat',
        description: 'Enterprise Kubernetes platform',
        features: ['Developer tools', 'Operators Hub', 'Security hardened']
    },
    'rancher': {
        name: 'Rancher/RKE',
        maintainer: 'SUSE',
        description: 'Multi-cluster management platform',
        features: ['Multi-cluster', 'Fleet management', 'K3s support']
    },
    'k3s': {
        name: 'K3s',
        maintainer: 'SUSE/Rancher',
        description: 'Lightweight Kubernetes for edge/IoT',
        size: '~70MB binary',
        features: ['Single binary', 'SQLite/etcd', 'ARM support']
    },
    'minikube': {
        name: 'Minikube',
        maintainer: 'Kubernetes SIG',
        description: 'Local Kubernetes for development',
        features: ['Multi-driver', 'Addons', 'LoadBalancer tunnel']
    },
    'kind': {
        name: 'Kind (Kubernetes in Docker)',
        maintainer: 'Kubernetes SIG',
        description: 'Kubernetes clusters using Docker containers',
        useCase: 'CI/CD, local development, testing'
    }
};

const HELM_KNOWLEDGE = {
    concepts: {
        chart: 'Package containing Kubernetes resources',
        release: 'Instance of a chart running in cluster',
        repository: 'Collection of charts',
        values: 'Configuration for chart installation'
    },
    commands: {
        'helm install': 'Install a chart',
        'helm upgrade': 'Upgrade a release',
        'helm rollback': 'Rollback to previous release',
        'helm uninstall': 'Remove a release',
        'helm list': 'List releases',
        'helm repo add': 'Add chart repository',
        'helm search': 'Search for charts',
        'helm template': 'Render chart templates locally'
    },
    bestPractices: [
        'Use semantic versioning for charts',
        'Include NOTES.txt for post-install info',
        'Define resource requests and limits',
        'Use values.yaml for defaults',
        'Validate with helm lint',
        'Use helm test for chart testing'
    ]
};

// ═══════════════════════════════════════════════════════════════════
// MANIFEST TEMPLATES
// ═══════════════════════════════════════════════════════════════════

const K8S_TEMPLATES = {
    deployment: `apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5`,

    service: `apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP`,

    ingress: `apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: my-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-app-service
            port:
              number: 80
  tls:
  - hosts:
    - my-app.example.com
    secretName: my-app-tls`,

    hpa: `apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70`
};

// ═══════════════════════════════════════════════════════════════════
// API ENDPOINTS
// ═══════════════════════════════════════════════════════════════════

app.get('/', (c) => {
    return c.json({
        worker: 'kubernetes',
        status: 'operational',
        version: '1.0.0',
        description: 'Kubernetes Expert - K8s, Helm, Operators, Cloud-Native',
        endpoints: [
            'GET /resources - List K8s resource types',
            'GET /distributions - K8s distributions',
            'GET /helm - Helm knowledge',
            'GET /templates/:type - Get manifest templates',
            'GET /kubectl - kubectl command reference',
            'POST /generate - Generate K8s manifests',
            'POST /ask - Ask Kubernetes questions'
        ]
    });
});

app.get('/resources', (c) => {
    return c.json({
        workloads: Object.keys(K8S_RESOURCES.workloads),
        networking: Object.keys(K8S_RESOURCES.networking),
        storage: Object.keys(K8S_RESOURCES.storage),
        security: Object.keys(K8S_RESOURCES.security),
        details: K8S_RESOURCES
    });
});

app.get('/distributions', (c) => {
    return c.json({
        count: Object.keys(K8S_DISTRIBUTIONS).length,
        distributions: K8S_DISTRIBUTIONS,
        recommendations: {
            production: ['eks', 'gke', 'aks', 'openshift'],
            development: ['minikube', 'kind', 'k3s'],
            edge: ['k3s'],
            multiCluster: ['rancher']
        }
    });
});

app.get('/helm', (c) => {
    return c.json(HELM_KNOWLEDGE);
});

app.get('/templates/:type', (c) => {
    const type = c.req.param('type');
    const template = K8S_TEMPLATES[type as keyof typeof K8S_TEMPLATES];

    if (!template) {
        return c.json({
            error: 'Template not found',
            available: Object.keys(K8S_TEMPLATES)
        }, 404);
    }

    return c.json({
        type,
        template,
        usage: `kubectl apply -f ${type}.yaml`
    });
});

app.get('/kubectl', (c) => {
    const commands = {
        basics: {
            'kubectl get pods': 'List pods',
            'kubectl get services': 'List services',
            'kubectl get deployments': 'List deployments',
            'kubectl describe pod <name>': 'Show pod details',
            'kubectl logs <pod>': 'View pod logs',
            'kubectl exec -it <pod> -- /bin/sh': 'Shell into pod'
        },
        management: {
            'kubectl apply -f <file>': 'Apply configuration',
            'kubectl delete -f <file>': 'Delete resources',
            'kubectl scale deployment <name> --replicas=3': 'Scale deployment',
            'kubectl rollout status deployment/<name>': 'Check rollout status',
            'kubectl rollout undo deployment/<name>': 'Rollback deployment'
        },
        debugging: {
            'kubectl get events --sort-by=.metadata.creationTimestamp': 'Get events',
            'kubectl top pods': 'Resource usage',
            'kubectl port-forward <pod> 8080:80': 'Port forward',
            'kubectl debug <pod> --image=busybox': 'Debug pod'
        }
    };

    return c.json(commands);
});

app.post('/generate', async (c) => {
    const { resourceType, name, image, replicas, port } = await c.req.json();

    const prompt = `Generate a Kubernetes manifest for:
Resource Type: ${resourceType || 'Deployment'}
Name: ${name || 'my-app'}
Image: ${image || 'nginx:latest'}
Replicas: ${replicas || 3}
Port: ${port || 80}

Include best practices like resource limits, health checks, and labels.`;

    try {
        const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
            messages: [
                {
                    role: 'system',
                    content: 'You are a Kubernetes expert. Generate production-ready manifests with best practices.'
                },
                { role: 'user', content: prompt }
            ],
            max_tokens: 2000
        });

        return c.json({
            resourceType: resourceType || 'Deployment',
            generatedManifest: response.response
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

    const systemPrompt = `You are a Kubernetes and cloud-native expert with deep knowledge of:
- Kubernetes architecture, API, and all resource types
- Helm charts, Kustomize, and GitOps
- Container orchestration and scheduling
- Networking (Services, Ingress, NetworkPolicies, Service Mesh)
- Storage (PV, PVC, StorageClasses)
- Security (RBAC, PSP, Network Policies, Secrets)
- Monitoring and observability (Prometheus, Grafana)
- All major K8s distributions (EKS, GKE, AKS, OpenShift, Rancher, K3s)
- Operators and custom resources

Provide detailed, practical answers with YAML examples when appropriate.`;

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
            answer: response.response
        });
    } catch (error) {
        return c.json({ error: 'AI query failed', details: String(error) }, 500);
    }
});

export default app;
