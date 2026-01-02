/**
 * ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗██╗      ██████╗ ██╗    ██╗
 * ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║     ██╔═══██╗██║    ██║
 * ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ █████╗  ██║     ██║   ██║██║ █╗ ██║
 * ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██║     ██║   ██║██║███╗██║
 * ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║     ███████╗╚██████╔╝╚███╔███╔╝
 *  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝ 
 *  ██████╗ ██████╗  ██████╗██╗  ██╗███████╗███████╗████████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
 * ██╔═══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
 * ██║   ██║██████╔╝██║     ███████║█████╗  ███████╗   ██║   ██████╔╝███████║   ██║   ██║   ██║██████╔╝
 * ██║   ██║██╔══██╗██║     ██╔══██║██╔══╝  ╚════██║   ██║   ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
 * ╚██████╔╝██║  ██║╚██████╗██║  ██║███████╗███████║   ██║   ██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 *  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 * 
 * NoizyLab OS - Workflow Orchestrator Worker
 * Central AI coordinator for all repair workflows and inter-worker communication
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════
// TYPES & INTERFACES
// ═══════════════════════════════════════════════════════════════════════════

interface Env {
  NOIZYLAB_KV: KVNamespace;
  NOIZYLAB_DB: D1Database;
  NOIZYLAB_QUEUE: Queue;
  AI: Ai;
  ANTHROPIC_API_KEY: string;
  
  // Service bindings to other workers
  BRAIN: Fetcher;
  VISION: Fetcher;
  VOICE: Fetcher;
  PRICING: Fetcher;
  INVENTORY: Fetcher;
  ANALYTICS: Fetcher;
  NOTIFICATIONS: Fetcher;
  QC_INSPECTOR: Fetcher;
  CUSTOMER_PORTAL: Fetcher;
  SCHEMATIC_ANALYZER: Fetcher;
  AR_GUIDE: Fetcher;
  TRAINING: Fetcher;
  EBAY_SNIPER: Fetcher;
  CHAT_AGENT: Fetcher;
}

interface Workflow {
  id: string;
  name: string;
  description: string;
  triggerType: 'ticket_created' | 'status_change' | 'scheduled' | 'manual' | 'event' | 'webhook';
  triggerConditions: TriggerCondition[];
  steps: WorkflowStep[];
  errorHandling: ErrorHandler;
  metadata: WorkflowMetadata;
  enabled: boolean;
  createdAt: string;
  updatedAt: string;
}

interface TriggerCondition {
  field: string;
  operator: 'equals' | 'contains' | 'greater_than' | 'less_than' | 'in' | 'not_in' | 'exists';
  value: any;
}

interface WorkflowStep {
  id: string;
  name: string;
  type: 'service_call' | 'condition' | 'parallel' | 'wait' | 'human_task' | 'ai_decision' | 'transform';
  service?: WorkerService;
  action?: string;
  params?: Record<string, any>;
  condition?: StepCondition;
  parallelSteps?: string[];
  waitConfig?: WaitConfig;
  humanTask?: HumanTask;
  aiDecision?: AIDecisionConfig;
  transform?: TransformConfig;
  onSuccess?: string;  // Next step ID
  onFailure?: string;  // Step ID or 'abort' or 'retry'
  retryConfig?: RetryConfig;
  timeout?: number;
}

type WorkerService = 
  | 'brain' | 'vision' | 'voice' | 'pricing' | 'inventory' 
  | 'analytics' | 'notifications' | 'qc_inspector' | 'customer_portal'
  | 'schematic_analyzer' | 'ar_guide' | 'training' | 'ebay_sniper' | 'chat_agent';

interface StepCondition {
  expression: string;  // e.g., "{{previous.result.score}} > 80"
  trueBranch: string;  // Step ID
  falseBranch: string; // Step ID
}

interface WaitConfig {
  type: 'duration' | 'event' | 'approval';
  duration?: number;  // ms
  eventType?: string;
  approvalRole?: string;
}

interface HumanTask {
  assignTo: 'auto' | 'role' | 'user';
  role?: string;
  userId?: string;
  taskType: string;
  instructions: string;
  dueIn?: number;  // ms
}

interface AIDecisionConfig {
  prompt: string;
  model: 'claude' | 'workers-ai';
  outputSchema: Record<string, any>;
  contextFields: string[];
}

interface TransformConfig {
  type: 'map' | 'filter' | 'reduce' | 'template' | 'script';
  template?: string;
  script?: string;
}

interface RetryConfig {
  maxRetries: number;
  backoffMs: number;
  backoffMultiplier: number;
}

interface ErrorHandler {
  strategy: 'abort' | 'retry' | 'fallback' | 'notify';
  fallbackStepId?: string;
  notifyChannel?: string;
  maxErrors?: number;
}

interface WorkflowMetadata {
  version: string;
  author: string;
  tags: string[];
  priority: 'low' | 'normal' | 'high' | 'critical';
  estimatedDuration?: number;
  avgDuration?: number;
  successRate?: number;
  executionCount?: number;
}

interface WorkflowExecution {
  id: string;
  workflowId: string;
  workflowName: string;
  triggeredBy: string;
  triggerData: any;
  status: 'pending' | 'running' | 'paused' | 'waiting' | 'completed' | 'failed' | 'cancelled';
  currentStepId?: string;
  stepResults: Record<string, StepResult>;
  context: Record<string, any>;
  startedAt: string;
  completedAt?: string;
  error?: string;
}

interface StepResult {
  stepId: string;
  status: 'pending' | 'running' | 'completed' | 'failed' | 'skipped';
  startedAt: string;
  completedAt?: string;
  result?: any;
  error?: string;
  retryCount?: number;
}

interface OrchestrationEvent {
  id: string;
  type: string;
  source: string;
  data: any;
  timestamp: string;
  correlationId?: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// WORKFLOW ENGINE
// ═══════════════════════════════════════════════════════════════════════════

class WorkflowEngine {
  private env: Env;

  constructor(env: Env) {
    this.env = env;
  }

  async startWorkflow(
    workflow: Workflow,
    triggerData: any,
    triggeredBy: string
  ): Promise<WorkflowExecution> {
    const executionId = `exec_${Date.now()}_${Math.random().toString(36).substring(7)}`;

    const execution: WorkflowExecution = {
      id: executionId,
      workflowId: workflow.id,
      workflowName: workflow.name,
      triggeredBy,
      triggerData,
      status: 'running',
      currentStepId: workflow.steps[0]?.id,
      stepResults: {},
      context: { trigger: triggerData },
      startedAt: new Date().toISOString()
    };

    // Save execution
    await this.saveExecution(execution);

    // Start processing
    await this.processExecution(execution, workflow);

    return execution;
  }

  private async processExecution(execution: WorkflowExecution, workflow: Workflow): Promise<void> {
    while (execution.status === 'running' && execution.currentStepId) {
      const step = workflow.steps.find(s => s.id === execution.currentStepId);
      if (!step) {
        execution.status = 'failed';
        execution.error = `Step ${execution.currentStepId} not found`;
        break;
      }

      const result = await this.executeStep(step, execution, workflow);
      execution.stepResults[step.id] = result;

      if (result.status === 'failed') {
        if (step.onFailure === 'abort') {
          execution.status = 'failed';
          execution.error = result.error;
          break;
        } else if (step.onFailure) {
          execution.currentStepId = step.onFailure;
        } else {
          execution.status = 'failed';
          execution.error = result.error;
          break;
        }
      } else if (result.status === 'completed') {
        execution.context[step.id] = result.result;

        if (step.onSuccess) {
          execution.currentStepId = step.onSuccess;
        } else {
          // Find next step in sequence
          const currentIndex = workflow.steps.findIndex(s => s.id === step.id);
          const nextStep = workflow.steps[currentIndex + 1];
          if (nextStep) {
            execution.currentStepId = nextStep.id;
          } else {
            execution.status = 'completed';
            execution.completedAt = new Date().toISOString();
            execution.currentStepId = undefined;
          }
        }
      }

      // Save progress
      await this.saveExecution(execution);
    }
  }

  private async executeStep(
    step: WorkflowStep,
    execution: WorkflowExecution,
    workflow: Workflow
  ): Promise<StepResult> {
    const startedAt = new Date().toISOString();

    try {
      let result: any;

      switch (step.type) {
        case 'service_call':
          result = await this.executeServiceCall(step, execution.context);
          break;

        case 'condition':
          result = await this.evaluateCondition(step, execution.context);
          break;

        case 'parallel':
          result = await this.executeParallel(step, execution, workflow);
          break;

        case 'wait':
          result = await this.executeWait(step, execution);
          break;

        case 'human_task':
          result = await this.createHumanTask(step, execution);
          break;

        case 'ai_decision':
          result = await this.executeAIDecision(step, execution.context);
          break;

        case 'transform':
          result = await this.executeTransform(step, execution.context);
          break;
      }

      return {
        stepId: step.id,
        status: 'completed',
        startedAt,
        completedAt: new Date().toISOString(),
        result
      };

    } catch (error) {
      const err = error as Error;
      
      // Handle retry
      if (step.retryConfig) {
        const currentRetry = execution.stepResults[step.id]?.retryCount || 0;
        if (currentRetry < step.retryConfig.maxRetries) {
          const delay = step.retryConfig.backoffMs * Math.pow(step.retryConfig.backoffMultiplier, currentRetry);
          await new Promise(resolve => setTimeout(resolve, delay));
          
          return {
            stepId: step.id,
            status: 'pending',
            startedAt,
            retryCount: currentRetry + 1
          };
        }
      }

      return {
        stepId: step.id,
        status: 'failed',
        startedAt,
        completedAt: new Date().toISOString(),
        error: err.message
      };
    }
  }

  private async executeServiceCall(step: WorkflowStep, context: Record<string, any>): Promise<any> {
    if (!step.service || !step.action) {
      throw new Error('Service call requires service and action');
    }

    const service = this.getServiceFetcher(step.service);
    const params = this.interpolateParams(step.params || {}, context);

    const response = await service.fetch(`https://internal/${step.action}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params)
    });

    if (!response.ok) {
      throw new Error(`Service call failed: ${response.status}`);
    }

    return response.json();
  }

  private getServiceFetcher(service: WorkerService): Fetcher {
    const serviceMap: Record<WorkerService, Fetcher> = {
      brain: this.env.BRAIN,
      vision: this.env.VISION,
      voice: this.env.VOICE,
      pricing: this.env.PRICING,
      inventory: this.env.INVENTORY,
      analytics: this.env.ANALYTICS,
      notifications: this.env.NOTIFICATIONS,
      qc_inspector: this.env.QC_INSPECTOR,
      customer_portal: this.env.CUSTOMER_PORTAL,
      schematic_analyzer: this.env.SCHEMATIC_ANALYZER,
      ar_guide: this.env.AR_GUIDE,
      training: this.env.TRAINING,
      ebay_sniper: this.env.EBAY_SNIPER,
      chat_agent: this.env.CHAT_AGENT
    };

    return serviceMap[service];
  }

  private interpolateParams(params: Record<string, any>, context: Record<string, any>): Record<string, any> {
    const interpolate = (value: any): any => {
      if (typeof value === 'string') {
        return value.replace(/\{\{([^}]+)\}\}/g, (_, path) => {
          return this.getNestedValue(context, path.trim());
        });
      }
      if (Array.isArray(value)) {
        return value.map(interpolate);
      }
      if (typeof value === 'object' && value !== null) {
        const result: Record<string, any> = {};
        for (const [k, v] of Object.entries(value)) {
          result[k] = interpolate(v);
        }
        return result;
      }
      return value;
    };

    return interpolate(params);
  }

  private getNestedValue(obj: any, path: string): any {
    return path.split('.').reduce((current, key) => current?.[key], obj);
  }

  private async evaluateCondition(step: WorkflowStep, context: Record<string, any>): Promise<{ branch: string }> {
    if (!step.condition) {
      throw new Error('Condition step requires condition config');
    }

    const expression = this.interpolateParams({ expr: step.condition.expression }, context).expr;
    
    // Simple expression evaluator (would use proper sandboxed eval in production)
    let result = false;
    try {
      // Parse simple comparisons
      const match = expression.match(/^(.+?)\s*(>|<|>=|<=|==|!=|===|!==)\s*(.+)$/);
      if (match) {
        const [, left, operator, right] = match;
        const leftVal = isNaN(Number(left)) ? left : Number(left);
        const rightVal = isNaN(Number(right)) ? right : Number(right);

        switch (operator) {
          case '>': result = leftVal > rightVal; break;
          case '<': result = leftVal < rightVal; break;
          case '>=': result = leftVal >= rightVal; break;
          case '<=': result = leftVal <= rightVal; break;
          case '==': result = leftVal == rightVal; break;
          case '!=': result = leftVal != rightVal; break;
          case '===': result = leftVal === rightVal; break;
          case '!==': result = leftVal !== rightVal; break;
        }
      }
    } catch {}

    return { 
      branch: result ? step.condition.trueBranch : step.condition.falseBranch 
    };
  }

  private async executeParallel(
    step: WorkflowStep,
    execution: WorkflowExecution,
    workflow: Workflow
  ): Promise<Record<string, any>> {
    if (!step.parallelSteps || step.parallelSteps.length === 0) {
      return {};
    }

    const parallelExecutions = step.parallelSteps.map(async (stepId) => {
      const parallelStep = workflow.steps.find(s => s.id === stepId);
      if (!parallelStep) {
        return { stepId, error: 'Step not found' };
      }

      const result = await this.executeStep(parallelStep, execution, workflow);
      return { stepId, result };
    });

    const results = await Promise.all(parallelExecutions);
    
    const output: Record<string, any> = {};
    for (const { stepId, result } of results) {
      output[stepId] = result;
      if (result) {
        execution.stepResults[stepId] = result;
      }
    }

    return output;
  }

  private async executeWait(step: WorkflowStep, execution: WorkflowExecution): Promise<{ waited: boolean }> {
    if (!step.waitConfig) {
      return { waited: false };
    }

    switch (step.waitConfig.type) {
      case 'duration':
        if (step.waitConfig.duration) {
          await new Promise(resolve => setTimeout(resolve, step.waitConfig!.duration));
        }
        break;

      case 'event':
        // Queue for event-based continuation
        await this.env.NOIZYLAB_QUEUE.send({
          type: 'workflow_wait',
          executionId: execution.id,
          waitingFor: step.waitConfig.eventType,
          stepId: step.id
        });
        execution.status = 'waiting';
        break;

      case 'approval':
        // Create approval request
        await this.env.NOIZYLAB_QUEUE.send({
          type: 'approval_request',
          executionId: execution.id,
          role: step.waitConfig.approvalRole,
          stepId: step.id
        });
        execution.status = 'paused';
        break;
    }

    return { waited: true };
  }

  private async createHumanTask(step: WorkflowStep, execution: WorkflowExecution): Promise<{ taskId: string }> {
    if (!step.humanTask) {
      throw new Error('Human task step requires humanTask config');
    }

    const taskId = `task_${Date.now()}_${Math.random().toString(36).substring(7)}`;

    await this.env.NOIZYLAB_DB.prepare(`
      INSERT INTO workflow_tasks (id, execution_id, step_id, task_type, instructions, 
        assigned_to, assign_type, status, created_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      taskId,
      execution.id,
      step.id,
      step.humanTask.taskType,
      step.humanTask.instructions,
      step.humanTask.userId || step.humanTask.role || null,
      step.humanTask.assignTo,
      'pending',
      new Date().toISOString()
    ).run();

    // Notify assignee
    await this.env.NOIZYLAB_QUEUE.send({
      type: 'task_assigned',
      taskId,
      executionId: execution.id,
      assignTo: step.humanTask.assignTo,
      role: step.humanTask.role,
      userId: step.humanTask.userId
    });

    execution.status = 'paused';

    return { taskId };
  }

  private async executeAIDecision(step: WorkflowStep, context: Record<string, any>): Promise<any> {
    if (!step.aiDecision) {
      throw new Error('AI decision step requires aiDecision config');
    }

    // Build context for AI
    const aiContext: Record<string, any> = {};
    for (const field of step.aiDecision.contextFields) {
      aiContext[field] = this.getNestedValue(context, field);
    }

    const prompt = `${step.aiDecision.prompt}

Context:
${JSON.stringify(aiContext, null, 2)}

Respond with JSON matching this schema:
${JSON.stringify(step.aiDecision.outputSchema, null, 2)}`;

    if (step.aiDecision.model === 'claude') {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': this.env.ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1024,
          messages: [{ role: 'user', content: prompt }]
        })
      });

      const data = await response.json() as any;
      const content = data.content[0].text;

      const jsonMatch = content.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[0]);
      }
      return { raw: content };

    } else {
      // Workers AI
      const result = await this.env.AI.run('@cf/meta/llama-3-8b-instruct', {
        messages: [{ role: 'user', content: prompt }]
      });

      const content = (result as any).response;
      const jsonMatch = content.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[0]);
      }
      return { raw: content };
    }
  }

  private async executeTransform(step: WorkflowStep, context: Record<string, any>): Promise<any> {
    if (!step.transform) {
      throw new Error('Transform step requires transform config');
    }

    switch (step.transform.type) {
      case 'template':
        return this.interpolateParams({ result: step.transform.template }, context).result;

      case 'map':
      case 'filter':
      case 'reduce':
        // Would implement array transformations
        return context;

      case 'script':
        // Sandboxed script execution would go here
        return context;

      default:
        return context;
    }
  }

  private async saveExecution(execution: WorkflowExecution): Promise<void> {
    await this.env.NOIZYLAB_KV.put(
      `execution:${execution.id}`,
      JSON.stringify(execution),
      { expirationTtl: 86400 * 7 }
    );

    await this.env.NOIZYLAB_DB.prepare(`
      INSERT OR REPLACE INTO workflow_executions 
      (id, workflow_id, status, context, started_at, completed_at, error)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    `).bind(
      execution.id,
      execution.workflowId,
      execution.status,
      JSON.stringify(execution),
      execution.startedAt,
      execution.completedAt || null,
      execution.error || null
    ).run();
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// PREDEFINED WORKFLOWS
// ═══════════════════════════════════════════════════════════════════════════

const STANDARD_WORKFLOWS: Workflow[] = [
  {
    id: 'repair-intake',
    name: 'Repair Intake Workflow',
    description: 'Complete repair intake process from ticket creation to quote',
    triggerType: 'ticket_created',
    triggerConditions: [],
    enabled: true,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    errorHandling: { strategy: 'notify', notifyChannel: 'slack' },
    metadata: {
      version: '1.0.0',
      author: 'system',
      tags: ['intake', 'diagnosis'],
      priority: 'high',
      estimatedDuration: 300000 // 5 min
    },
    steps: [
      {
        id: 'analyze-images',
        name: 'Analyze Device Images',
        type: 'service_call',
        service: 'vision',
        action: 'analyze',
        params: {
          ticketId: '{{trigger.ticketId}}',
          images: '{{trigger.images}}'
        },
        onSuccess: 'ai-diagnosis'
      },
      {
        id: 'ai-diagnosis',
        name: 'AI Diagnosis',
        type: 'service_call',
        service: 'brain',
        action: 'diagnose',
        params: {
          ticketId: '{{trigger.ticketId}}',
          deviceInfo: '{{trigger.deviceInfo}}',
          symptoms: '{{trigger.symptoms}}',
          visionAnalysis: '{{analyze-images.result}}'
        },
        onSuccess: 'check-parts'
      },
      {
        id: 'check-parts',
        name: 'Check Parts Inventory',
        type: 'service_call',
        service: 'inventory',
        action: 'check-availability',
        params: {
          parts: '{{ai-diagnosis.result.recommendedParts}}'
        },
        onSuccess: 'generate-quote'
      },
      {
        id: 'generate-quote',
        name: 'Generate Quote',
        type: 'service_call',
        service: 'pricing',
        action: 'quote',
        params: {
          ticketId: '{{trigger.ticketId}}',
          diagnosis: '{{ai-diagnosis.result}}',
          partsAvailability: '{{check-parts.result}}'
        },
        onSuccess: 'notify-customer'
      },
      {
        id: 'notify-customer',
        name: 'Notify Customer',
        type: 'service_call',
        service: 'notifications',
        action: 'send',
        params: {
          userId: '{{trigger.customerId}}',
          type: 'quote_ready',
          channels: ['email', 'push'],
          data: {
            ticketId: '{{trigger.ticketId}}',
            quote: '{{generate-quote.result}}'
          }
        }
      }
    ]
  },
  {
    id: 'repair-completion',
    name: 'Repair Completion Workflow',
    description: 'QC, customer notification, and invoice generation',
    triggerType: 'status_change',
    triggerConditions: [
      { field: 'newStatus', operator: 'equals', value: 'repair_complete' }
    ],
    enabled: true,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    errorHandling: { strategy: 'retry', maxErrors: 3 },
    metadata: {
      version: '1.0.0',
      author: 'system',
      tags: ['completion', 'qc'],
      priority: 'high'
    },
    steps: [
      {
        id: 'start-qc',
        name: 'Start QC Inspection',
        type: 'service_call',
        service: 'qc_inspector',
        action: 'inspections',
        params: {
          ticketId: '{{trigger.ticketId}}',
          repairId: '{{trigger.repairId}}',
          technicianId: '{{trigger.technicianId}}'
        },
        onSuccess: 'check-qc-result'
      },
      {
        id: 'check-qc-result',
        name: 'Check QC Result',
        type: 'condition',
        condition: {
          expression: '{{start-qc.result.overallScore}} >= 80',
          trueBranch: 'generate-invoice',
          falseBranch: 'notify-rework'
        }
      },
      {
        id: 'notify-rework',
        name: 'Notify Technician - Rework',
        type: 'service_call',
        service: 'notifications',
        action: 'send',
        params: {
          userId: '{{trigger.technicianId}}',
          type: 'qc_failed',
          channels: ['push', 'email'],
          data: {
            ticketId: '{{trigger.ticketId}}',
            qcResult: '{{start-qc.result}}'
          }
        }
      },
      {
        id: 'generate-invoice',
        name: 'Generate Invoice',
        type: 'service_call',
        service: 'pricing',
        action: 'invoice',
        params: {
          ticketId: '{{trigger.ticketId}}'
        },
        onSuccess: 'notify-ready'
      },
      {
        id: 'notify-ready',
        name: 'Notify Customer - Ready',
        type: 'service_call',
        service: 'notifications',
        action: 'send',
        params: {
          userId: '{{trigger.customerId}}',
          type: 'repair_ready',
          channels: ['email', 'sms', 'push'],
          data: {
            ticketId: '{{trigger.ticketId}}',
            invoice: '{{generate-invoice.result}}'
          }
        },
        onSuccess: 'track-analytics'
      },
      {
        id: 'track-analytics',
        name: 'Track Analytics',
        type: 'service_call',
        service: 'analytics',
        action: 'track',
        params: {
          event: 'repair_completed',
          ticketId: '{{trigger.ticketId}}',
          metrics: {
            repairTime: '{{trigger.repairDuration}}',
            technicianId: '{{trigger.technicianId}}',
            qcScore: '{{start-qc.result.overallScore}}'
          }
        }
      }
    ]
  },
  {
    id: 'parts-hunt',
    name: 'Parts Hunting Workflow',
    description: 'Automated parts sourcing when inventory is low',
    triggerType: 'event',
    triggerConditions: [
      { field: 'eventType', operator: 'equals', value: 'part_needed' }
    ],
    enabled: true,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    errorHandling: { strategy: 'fallback', fallbackStepId: 'manual-order' },
    metadata: {
      version: '1.0.0',
      author: 'system',
      tags: ['inventory', 'ebay'],
      priority: 'normal'
    },
    steps: [
      {
        id: 'search-ebay',
        name: 'Search eBay for Parts',
        type: 'service_call',
        service: 'ebay_sniper',
        action: 'search',
        params: {
          query: '{{trigger.partName}}',
          partNumber: '{{trigger.partNumber}}',
          maxPrice: '{{trigger.maxBudget}}'
        },
        onSuccess: 'analyze-deals',
        onFailure: 'manual-order'
      },
      {
        id: 'analyze-deals',
        name: 'AI Analyze Deals',
        type: 'ai_decision',
        aiDecision: {
          prompt: 'Analyze these eBay listings and recommend the best deal considering price, seller rating, shipping time, and authenticity risk.',
          model: 'claude',
          outputSchema: {
            recommended: { type: 'object', properties: { listingId: { type: 'string' }, reason: { type: 'string' } } },
            alternatives: { type: 'array' },
            riskLevel: { type: 'string' }
          },
          contextFields: ['search-ebay.result.listings', 'trigger.urgency']
        },
        onSuccess: 'approve-purchase'
      },
      {
        id: 'approve-purchase',
        name: 'Approve Purchase',
        type: 'human_task',
        humanTask: {
          assignTo: 'role',
          role: 'inventory_manager',
          taskType: 'purchase_approval',
          instructions: 'Review and approve the recommended parts purchase',
          dueIn: 3600000 // 1 hour
        },
        onSuccess: 'place-order'
      },
      {
        id: 'place-order',
        name: 'Place eBay Order',
        type: 'service_call',
        service: 'ebay_sniper',
        action: 'buy-now',
        params: {
          listingId: '{{analyze-deals.result.recommended.listingId}}'
        },
        onSuccess: 'update-inventory'
      },
      {
        id: 'update-inventory',
        name: 'Update Inventory',
        type: 'service_call',
        service: 'inventory',
        action: 'add-incoming',
        params: {
          partNumber: '{{trigger.partNumber}}',
          orderId: '{{place-order.result.orderId}}',
          expectedArrival: '{{place-order.result.estimatedDelivery}}'
        }
      },
      {
        id: 'manual-order',
        name: 'Manual Order Required',
        type: 'human_task',
        humanTask: {
          assignTo: 'role',
          role: 'inventory_manager',
          taskType: 'manual_order',
          instructions: 'Automated sourcing failed. Please order part manually.'
        }
      }
    ]
  }
];

// ═══════════════════════════════════════════════════════════════════════════
// HONO APP
// ═══════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// Health check
app.get('/health', (c) => c.json({ 
  status: 'healthy', 
  service: 'workflow-orchestrator',
  version: '1.0.0'
}));

// ═══════════════════════════════════════════════════════════════════════════
// WORKFLOW MANAGEMENT
// ═══════════════════════════════════════════════════════════════════════════

app.get('/workflows', async (c) => {
  const { results } = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM workflows ORDER BY name'
  ).all();

  const workflows = [
    ...STANDARD_WORKFLOWS,
    ...results.map(r => JSON.parse(r.data as string))
  ];

  return c.json({ workflows });
});

app.get('/workflows/:id', async (c) => {
  const workflowId = c.req.param('id');

  // Check standard workflows
  const standard = STANDARD_WORKFLOWS.find(w => w.id === workflowId);
  if (standard) {
    return c.json({ workflow: standard });
  }

  // Check custom workflows
  const row = await c.env.NOIZYLAB_DB.prepare(
    'SELECT data FROM workflows WHERE id = ?'
  ).bind(workflowId).first();

  if (!row) {
    return c.json({ error: 'Workflow not found' }, 404);
  }

  return c.json({ workflow: JSON.parse(row.data as string) });
});

app.post('/workflows', async (c) => {
  const workflow = await c.req.json() as Workflow;

  workflow.id = workflow.id || `wf_${Date.now()}_${Math.random().toString(36).substring(7)}`;
  workflow.createdAt = new Date().toISOString();
  workflow.updatedAt = workflow.createdAt;

  await c.env.NOIZYLAB_DB.prepare(`
    INSERT INTO workflows (id, name, data, enabled, created_at)
    VALUES (?, ?, ?, ?, ?)
  `).bind(
    workflow.id,
    workflow.name,
    JSON.stringify(workflow),
    workflow.enabled ? 1 : 0,
    workflow.createdAt
  ).run();

  return c.json({ workflow }, 201);
});

// ═══════════════════════════════════════════════════════════════════════════
// WORKFLOW EXECUTION
// ═══════════════════════════════════════════════════════════════════════════

app.post('/workflows/:id/execute', async (c) => {
  const workflowId = c.req.param('id');
  const { triggerData, triggeredBy } = await c.req.json();

  // Find workflow
  let workflow = STANDARD_WORKFLOWS.find(w => w.id === workflowId);
  if (!workflow) {
    const row = await c.env.NOIZYLAB_DB.prepare(
      'SELECT data FROM workflows WHERE id = ?'
    ).bind(workflowId).first();

    if (!row) {
      return c.json({ error: 'Workflow not found' }, 404);
    }
    workflow = JSON.parse(row.data as string);
  }

  if (!workflow!.enabled) {
    return c.json({ error: 'Workflow is disabled' }, 400);
  }

  const engine = new WorkflowEngine(c.env);
  const execution = await engine.startWorkflow(workflow!, triggerData, triggeredBy || 'api');

  return c.json({ execution }, 202);
});

app.get('/executions', async (c) => {
  const workflowId = c.req.query('workflowId');
  const status = c.req.query('status');

  let query = 'SELECT * FROM workflow_executions WHERE 1=1';
  const params: any[] = [];

  if (workflowId) {
    query += ' AND workflow_id = ?';
    params.push(workflowId);
  }
  if (status) {
    query += ' AND status = ?';
    params.push(status);
  }

  query += ' ORDER BY started_at DESC LIMIT 100';

  const { results } = await c.env.NOIZYLAB_DB.prepare(query).bind(...params).all();

  return c.json({
    executions: results.map(r => JSON.parse(r.context as string))
  });
});

app.get('/executions/:id', async (c) => {
  const executionId = c.req.param('id');

  const cached = await c.env.NOIZYLAB_KV.get(`execution:${executionId}`);
  if (cached) {
    return c.json({ execution: JSON.parse(cached) });
  }

  const row = await c.env.NOIZYLAB_DB.prepare(
    'SELECT context FROM workflow_executions WHERE id = ?'
  ).bind(executionId).first();

  if (!row) {
    return c.json({ error: 'Execution not found' }, 404);
  }

  return c.json({ execution: JSON.parse(row.context as string) });
});

// Resume paused execution
app.post('/executions/:id/resume', async (c) => {
  const executionId = c.req.param('id');
  const { stepResult } = await c.req.json();

  const cached = await c.env.NOIZYLAB_KV.get(`execution:${executionId}`);
  if (!cached) {
    return c.json({ error: 'Execution not found' }, 404);
  }

  const execution: WorkflowExecution = JSON.parse(cached);
  
  if (execution.status !== 'paused' && execution.status !== 'waiting') {
    return c.json({ error: 'Execution is not paused' }, 400);
  }

  // Find workflow
  let workflow = STANDARD_WORKFLOWS.find(w => w.id === execution.workflowId);
  if (!workflow) {
    const row = await c.env.NOIZYLAB_DB.prepare(
      'SELECT data FROM workflows WHERE id = ?'
    ).bind(execution.workflowId).first();

    if (!row) {
      return c.json({ error: 'Workflow not found' }, 404);
    }
    workflow = JSON.parse(row.data as string);
  }

  // Update step result if provided
  if (stepResult && execution.currentStepId) {
    execution.stepResults[execution.currentStepId] = stepResult;
    execution.context[execution.currentStepId] = stepResult.result;
  }

  // Resume
  execution.status = 'running';
  const engine = new WorkflowEngine(c.env);
  
  // Find next step
  const currentStep = workflow!.steps.find(s => s.id === execution.currentStepId);
  if (currentStep?.onSuccess) {
    execution.currentStepId = currentStep.onSuccess;
  } else {
    const currentIndex = workflow!.steps.findIndex(s => s.id === execution.currentStepId);
    execution.currentStepId = workflow!.steps[currentIndex + 1]?.id;
  }

  // Continue processing would happen async
  await c.env.NOIZYLAB_QUEUE.send({
    type: 'continue_workflow',
    executionId,
    workflowId: workflow!.id
  });

  return c.json({ execution, status: 'resumed' });
});

// Cancel execution
app.post('/executions/:id/cancel', async (c) => {
  const executionId = c.req.param('id');

  const cached = await c.env.NOIZYLAB_KV.get(`execution:${executionId}`);
  if (!cached) {
    return c.json({ error: 'Execution not found' }, 404);
  }

  const execution: WorkflowExecution = JSON.parse(cached);
  execution.status = 'cancelled';
  execution.completedAt = new Date().toISOString();

  await c.env.NOIZYLAB_KV.put(`execution:${executionId}`, JSON.stringify(execution));
  await c.env.NOIZYLAB_DB.prepare(
    'UPDATE workflow_executions SET status = ?, completed_at = ? WHERE id = ?'
  ).bind('cancelled', execution.completedAt, executionId).run();

  return c.json({ execution });
});

// ═══════════════════════════════════════════════════════════════════════════
// EVENTS & TRIGGERS
// ═══════════════════════════════════════════════════════════════════════════

app.post('/events', async (c) => {
  const event = await c.req.json() as OrchestrationEvent;

  event.id = event.id || crypto.randomUUID();
  event.timestamp = new Date().toISOString();

  // Find workflows triggered by this event
  const allWorkflows = [
    ...STANDARD_WORKFLOWS,
    // Would also load custom workflows
  ];

  const triggeredWorkflows = allWorkflows.filter(w => {
    if (!w.enabled) return false;
    if (w.triggerType !== 'event') return false;

    return w.triggerConditions.every(condition => {
      const value = event.data[condition.field];
      switch (condition.operator) {
        case 'equals': return value === condition.value;
        case 'contains': return String(value).includes(condition.value);
        case 'in': return condition.value.includes(value);
        default: return false;
      }
    });
  });

  // Queue workflow executions
  const executions = [];
  for (const workflow of triggeredWorkflows) {
    await c.env.NOIZYLAB_QUEUE.send({
      type: 'execute_workflow',
      workflowId: workflow.id,
      triggerData: event.data,
      triggeredBy: event.source,
      correlationId: event.correlationId
    });
    executions.push({ workflowId: workflow.id, workflowName: workflow.name });
  }

  return c.json({
    event,
    triggeredWorkflows: executions
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// TASKS
// ═══════════════════════════════════════════════════════════════════════════

app.get('/tasks', async (c) => {
  const assignee = c.req.query('assignee');
  const role = c.req.query('role');
  const status = c.req.query('status') || 'pending';

  let query = 'SELECT * FROM workflow_tasks WHERE status = ?';
  const params: any[] = [status];

  if (assignee) {
    query += ' AND (assigned_to = ? OR assign_type = ?)';
    params.push(assignee, 'auto');
  }
  if (role) {
    query += ' AND assigned_to = ?';
    params.push(role);
  }

  query += ' ORDER BY created_at DESC';

  const { results } = await c.env.NOIZYLAB_DB.prepare(query).bind(...params).all();

  return c.json({ tasks: results });
});

app.post('/tasks/:id/complete', async (c) => {
  const taskId = c.req.param('id');
  const { result, completedBy } = await c.req.json();

  const task = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM workflow_tasks WHERE id = ?'
  ).bind(taskId).first();

  if (!task) {
    return c.json({ error: 'Task not found' }, 404);
  }

  await c.env.NOIZYLAB_DB.prepare(`
    UPDATE workflow_tasks 
    SET status = ?, completed_at = ?, completed_by = ?, result = ?
    WHERE id = ?
  `).bind(
    'completed',
    new Date().toISOString(),
    completedBy,
    JSON.stringify(result),
    taskId
  ).run();

  // Resume workflow
  await c.env.NOIZYLAB_QUEUE.send({
    type: 'task_completed',
    taskId,
    executionId: task.execution_id,
    stepId: task.step_id,
    result
  });

  return c.json({ message: 'Task completed' });
});

// ═══════════════════════════════════════════════════════════════════════════
// QUEUE CONSUMER
// ═══════════════════════════════════════════════════════════════════════════

export default {
  fetch: app.fetch,

  async queue(batch: MessageBatch<any>, env: Env): Promise<void> {
    const engine = new WorkflowEngine(env);

    for (const message of batch.messages) {
      const { type, ...data } = message.body;

      switch (type) {
        case 'execute_workflow': {
          let workflow = STANDARD_WORKFLOWS.find(w => w.id === data.workflowId);
          if (!workflow) {
            const row = await env.NOIZYLAB_DB.prepare(
              'SELECT data FROM workflows WHERE id = ?'
            ).bind(data.workflowId).first();
            if (row) {
              workflow = JSON.parse(row.data as string);
            }
          }
          if (workflow) {
            await engine.startWorkflow(workflow, data.triggerData, data.triggeredBy);
          }
          break;
        }

        case 'continue_workflow': {
          const cached = await env.NOIZYLAB_KV.get(`execution:${data.executionId}`);
          if (cached) {
            const execution = JSON.parse(cached) as WorkflowExecution;
            let workflow = STANDARD_WORKFLOWS.find(w => w.id === data.workflowId);
            if (!workflow) {
              const row = await env.NOIZYLAB_DB.prepare(
                'SELECT data FROM workflows WHERE id = ?'
              ).bind(data.workflowId).first();
              if (row) {
                workflow = JSON.parse(row.data as string);
              }
            }
            // Would continue processing
          }
          break;
        }

        case 'task_completed': {
          // Resume execution after task completion
          const cached = await env.NOIZYLAB_KV.get(`execution:${data.executionId}`);
          if (cached) {
            const execution = JSON.parse(cached) as WorkflowExecution;
            execution.stepResults[data.stepId] = {
              stepId: data.stepId,
              status: 'completed',
              startedAt: execution.stepResults[data.stepId]?.startedAt || new Date().toISOString(),
              completedAt: new Date().toISOString(),
              result: data.result
            };
            execution.context[data.stepId] = data.result;
            execution.status = 'running';

            await env.NOIZYLAB_KV.put(`execution:${data.executionId}`, JSON.stringify(execution));
          }
          break;
        }
      }

      message.ack();
    }
  }
};
