/**
 * ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗ 
 * ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗
 * ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝
 * ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗
 * ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝
 * ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ 
 * 
 * INFRASTRUCTURE-AS-CODE WORKER - IaC Expert
 * Round 5: DevOps & Infrastructure Legends
 * 
 * Master of Terraform, Pulumi, CloudFormation, Ansible, Chef, Puppet!
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  AI: any;
  IAC_KV: KVNamespace;
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// ═══════════════════════════════════════════════════════════════════
// IAC TOOLS KNOWLEDGE BASE
// ═══════════════════════════════════════════════════════════════════

const IAC_TOOLS = {
  'terraform': {
    name: 'Terraform',
    vendor: 'HashiCorp',
    year: 2014,
    language: 'HCL (HashiCorp Configuration Language)',
    type: 'Declarative',
    approach: 'Immutable infrastructure',
    stateManagement: 'State file (local/remote)',
    features: [
      'Provider ecosystem (3000+)',
      'Modules for reusability',
      'State management',
      'Plan/Apply workflow',
      'Workspaces',
      'Remote backends',
      'Terragrunt wrapper',
      'Import existing resources',
      'Drift detection',
      'Graph visualization'
    ],
    providers: {
      cloud: ['AWS', 'Azure', 'GCP', 'DigitalOcean', 'Linode'],
      saas: ['Cloudflare', 'Datadog', 'PagerDuty', 'GitHub'],
      infrastructure: ['Kubernetes', 'Docker', 'VMware', 'Proxmox']
    },
    commands: {
      'terraform init': 'Initialize working directory',
      'terraform plan': 'Preview changes',
      'terraform apply': 'Apply changes',
      'terraform destroy': 'Destroy infrastructure',
      'terraform fmt': 'Format code',
      'terraform validate': 'Validate configuration'
    },
    bestPractices: [
      'Use remote state with locking',
      'Modularize configurations',
      'Use workspaces for environments',
      'Version pin providers',
      'Use terraform fmt and validate in CI'
    ]
  },
  'pulumi': {
    name: 'Pulumi',
    vendor: 'Pulumi',
    year: 2018,
    language: 'TypeScript, Python, Go, C#, Java, YAML',
    type: 'Declarative (with imperative capabilities)',
    approach: 'Infrastructure as real code',
    stateManagement: 'Pulumi Cloud or self-managed',
    features: [
      'Real programming languages',
      'Strong typing',
      'IDE support',
      'Testing frameworks',
      'Policy as code',
      'Secrets management',
      'Stack references',
      'Component resources',
      'Automation API',
      'Pulumi AI'
    ],
    commands: {
      'pulumi new': 'Create new project',
      'pulumi preview': 'Preview changes',
      'pulumi up': 'Deploy changes',
      'pulumi destroy': 'Destroy resources',
      'pulumi stack': 'Manage stacks'
    },
    bestPractices: [
      'Use component resources for abstraction',
      'Leverage programming language features',
      'Write unit tests for infrastructure',
      'Use Pulumi ESC for secrets',
      'Implement policy packs'
    ]
  },
  'cloudformation': {
    name: 'AWS CloudFormation',
    vendor: 'Amazon Web Services',
    year: 2011,
    language: 'YAML, JSON',
    type: 'Declarative',
    approach: 'AWS-native IaC',
    stateManagement: 'AWS managed',
    features: [
      'Native AWS integration',
      'StackSets for multi-account',
      'Change sets',
      'Nested stacks',
      'Drift detection',
      'Custom resources',
      'Macros',
      'Resource import',
      'SAM for serverless',
      'CDK integration'
    ],
    intrinsicFunctions: ['Ref', 'Fn::GetAtt', 'Fn::Sub', 'Fn::Join', 'Fn::If'],
    commands: {
      'aws cloudformation create-stack': 'Create stack',
      'aws cloudformation update-stack': 'Update stack',
      'aws cloudformation delete-stack': 'Delete stack',
      'aws cloudformation describe-stacks': 'Describe stacks'
    }
  },
  'aws-cdk': {
    name: 'AWS CDK',
    vendor: 'Amazon Web Services',
    year: 2019,
    language: 'TypeScript, Python, Java, C#, Go',
    type: 'Declarative (code-first)',
    approach: 'High-level constructs',
    stateManagement: 'CloudFormation under the hood',
    features: [
      'L1, L2, L3 constructs',
      'Construct libraries',
      'Asset bundling',
      'CDK Pipelines',
      'Aspects for cross-cutting concerns',
      'Testing support',
      'cfn-nag integration',
      'Snapshop testing'
    ],
    commands: {
      'cdk init': 'Initialize CDK app',
      'cdk synth': 'Synthesize CloudFormation',
      'cdk deploy': 'Deploy stack',
      'cdk diff': 'Compare deployed vs local',
      'cdk destroy': 'Destroy stack'
    }
  },
  'ansible': {
    name: 'Ansible',
    vendor: 'Red Hat',
    year: 2012,
    language: 'YAML',
    type: 'Declarative/Procedural',
    approach: 'Agentless configuration management',
    stateManagement: 'Stateless (idempotent)',
    features: [
      'Agentless (SSH/WinRM)',
      'Playbooks',
      'Roles',
      'Galaxy (community content)',
      'Inventory management',
      'Vault for secrets',
      'Collections',
      'AWX/Tower for enterprise',
      'Molecule for testing',
      'Dynamic inventory'
    ],
    commands: {
      'ansible-playbook': 'Run playbook',
      'ansible-galaxy': 'Manage roles/collections',
      'ansible-vault': 'Encrypt secrets',
      'ansible-inventory': 'Manage inventory',
      'ansible-lint': 'Lint playbooks'
    },
    bestPractices: [
      'Use roles for reusability',
      'Encrypt secrets with Vault',
      'Use molecule for testing',
      'Implement idempotent tasks',
      'Use dynamic inventory'
    ]
  },
  'chef': {
    name: 'Chef',
    vendor: 'Progress',
    year: 2009,
    language: 'Ruby DSL',
    type: 'Declarative',
    approach: 'Agent-based configuration',
    stateManagement: 'Chef Server',
    features: [
      'Cookbooks & recipes',
      'Chef Infra Server',
      'InSpec for compliance',
      'Habitat for application automation',
      'Chef Workstation',
      'Policyfiles',
      'Data bags',
      'Environments',
      'Test Kitchen'
    ]
  },
  'puppet': {
    name: 'Puppet',
    vendor: 'Perforce',
    year: 2005,
    language: 'Puppet DSL',
    type: 'Declarative',
    approach: 'Agent-based configuration',
    stateManagement: 'Puppet Server',
    features: [
      'Manifests & modules',
      'Puppet Forge',
      'Facter for facts',
      'Hiera for data',
      'PuppetDB',
      'Bolt for orchestration',
      'Resource abstraction layer'
    ]
  },
  'opentofu': {
    name: 'OpenTofu',
    vendor: 'Linux Foundation',
    year: 2023,
    language: 'HCL',
    type: 'Declarative',
    approach: 'Open-source Terraform fork',
    stateManagement: 'State file (compatible with Terraform)',
    features: [
      'Drop-in Terraform replacement',
      'Community-driven',
      'MPL 2.0 license',
      'Provider ecosystem compatibility',
      'State encryption',
      'Enhanced functions'
    ]
  }
};

// ═══════════════════════════════════════════════════════════════════
// IAC TEMPLATES
// ═══════════════════════════════════════════════════════════════════

const IAC_TEMPLATES = {
  'terraform-aws-vpc': `# Terraform AWS VPC Module
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-west-2"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "main-vpc"
    Environment = "production"
    ManagedBy   = "terraform"
  }
}

resource "aws_subnet" "public" {
  count             = 3
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet-\${count.index + 1}"
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}

output "vpc_id" {
  value = aws_vpc.main.id
}`,

  'pulumi-ts-s3': `import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an S3 bucket
const bucket = new aws.s3.Bucket("my-bucket", {
    acl: "private",
    versioning: {
        enabled: true,
    },
    serverSideEncryptionConfiguration: {
        rule: {
            applyServerSideEncryptionByDefault: {
                sseAlgorithm: "AES256",
            },
        },
    },
    tags: {
        Environment: "production",
        ManagedBy: "pulumi",
    },
});

// Block public access
const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("my-bucket-pab", {
    bucket: bucket.id,
    blockPublicAcls: true,
    blockPublicPolicy: true,
    ignorePublicAcls: true,
    restrictPublicBuckets: true,
});

export const bucketName = bucket.bucket;
export const bucketArn = bucket.arn;`,

  'ansible-nginx': `---
# Ansible Playbook: Install and Configure Nginx
- name: Install and configure Nginx
  hosts: webservers
  become: yes
  vars:
    nginx_port: 80
    server_name: example.com

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600
      when: ansible_os_family == "Debian"

    - name: Install Nginx
      package:
        name: nginx
        state: present

    - name: Configure Nginx virtual host
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/sites-available/default
        mode: '0644'
      notify: Restart Nginx

    - name: Enable Nginx service
      service:
        name: nginx
        state: started
        enabled: yes

  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted`
};

// ═══════════════════════════════════════════════════════════════════
// API ENDPOINTS
// ═══════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  return c.json({
    worker: 'infrastructure-as-code',
    status: 'operational',
    version: '1.0.0',
    description: 'IaC Expert - Terraform, Pulumi, CloudFormation, Ansible & more',
    endpoints: [
      'GET /tools - List all IaC tools',
      'GET /tool/:name - Get tool details',
      'GET /templates/:type - Get IaC templates',
      'GET /compare - Compare IaC tools',
      'POST /generate - Generate IaC code',
      'POST /ask - Ask IaC questions'
    ]
  });
});

app.get('/tools', (c) => {
  const tools = Object.entries(IAC_TOOLS).map(([key, tool]) => ({
    id: key,
    name: tool.name,
    vendor: tool.vendor,
    language: tool.language,
    type: tool.type
  }));

  return c.json({
    count: tools.length,
    tools,
    categories: {
      provisioning: ['terraform', 'pulumi', 'cloudformation', 'aws-cdk', 'opentofu'],
      configuration: ['ansible', 'chef', 'puppet']
    }
  });
});

app.get('/tool/:name', (c) => {
  const name = c.req.param('name');
  const tool = IAC_TOOLS[name as keyof typeof IAC_TOOLS];

  if (!tool) {
    return c.json({ error: 'Tool not found', available: Object.keys(IAC_TOOLS) }, 404);
  }

  return c.json(tool);
});

app.get('/templates/:type', (c) => {
  const type = c.req.param('type');
  const template = IAC_TEMPLATES[type as keyof typeof IAC_TEMPLATES];

  if (!template) {
    return c.json({
      error: 'Template not found',
      available: Object.keys(IAC_TEMPLATES)
    }, 404);
  }

  return c.json({ type, template });
});

app.get('/compare', (c) => {
  return c.json({
    forMultiCloud: {
      winner: 'Terraform or Pulumi',
      reason: 'Extensive provider support across all clouds'
    },
    forAWSOnly: {
      winner: 'AWS CDK or CloudFormation',
      reason: 'Native AWS integration, no state management overhead'
    },
    forProgrammers: {
      winner: 'Pulumi or AWS CDK',
      reason: 'Real programming languages with IDE support'
    },
    forConfiguration: {
      winner: 'Ansible',
      reason: 'Agentless, simple YAML, great for config management'
    },
    forOpenSource: {
      winner: 'OpenTofu',
      reason: 'Community-driven, fully open source, Terraform-compatible'
    }
  });
});

app.post('/generate', async (c) => {
  const { tool, resource, provider, options } = await c.req.json();

  const prompt = `Generate ${tool || 'Terraform'} code for:
Resource: ${resource || 'web server'}
Cloud Provider: ${provider || 'AWS'}
Options: ${JSON.stringify(options || {})}

Include best practices, comments, and variables for customization.`;

  try {
    const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
      messages: [
        {
          role: 'system',
          content: `You are an Infrastructure-as-Code expert specializing in ${tool || 'Terraform'}. Generate production-ready, secure, and well-documented code.`
        },
        { role: 'user', content: prompt }
      ],
      max_tokens: 2000
    });

    return c.json({
      tool: tool || 'Terraform',
      resource: resource || 'web server',
      provider: provider || 'AWS',
      generatedCode: response.response
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

  const systemPrompt = `You are an Infrastructure-as-Code expert with deep knowledge of:
- Terraform, OpenTofu, and HCL
- Pulumi with TypeScript, Python, Go
- AWS CloudFormation and CDK
- Ansible, Chef, Puppet
- State management and backends
- Module design and reusability
- Security best practices
- Multi-cloud deployments
- GitOps workflows

Provide detailed, practical answers with code examples.`;

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
