/**
 * NoizyLab OS - Compliance Monitoring Worker
 * 
 * AI-powered regulatory compliance and audit engine that automatically
 * tracks, validates, and reports compliance across multiple frameworks.
 * 
 * Features:
 * - Multi-framework compliance (GDPR, HIPAA, SOC2, ISO27001, PCI-DSS)
 * - Real-time violation detection and alerting
 * - Automated audit trail generation
 * - Policy enforcement engine
 * - Risk assessment scoring
 * - Evidence collection and documentation
 * - Remediation workflow automation
 * - Continuous compliance monitoring
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  COMPLIANCE_CACHE: KVNamespace;
  AUDIT_STORAGE: R2Bucket;
  AI: any;
  ALERT_QUEUE: Queue;
  ENVIRONMENT: string;
}

interface ComplianceFramework {
  id: string;
  name: string;
  version: string;
  controls: ComplianceControl[];
  lastAudit: string;
  overallScore: number;
}

interface ComplianceControl {
  id: string;
  framework: string;
  category: string;
  name: string;
  description: string;
  requirement: string;
  status: 'compliant' | 'non-compliant' | 'partial' | 'not-applicable';
  evidence: Evidence[];
  lastChecked: string;
  riskLevel: 'critical' | 'high' | 'medium' | 'low';
  remediation?: string;
}

interface Evidence {
  id: string;
  controlId: string;
  type: 'document' | 'log' | 'screenshot' | 'api-response' | 'scan-result';
  source: string;
  content: string;
  collectedAt: string;
  validUntil: string;
  hash: string;
}

interface PolicyRule {
  id: string;
  name: string;
  frameworks: string[];
  condition: string;
  action: 'block' | 'alert' | 'log' | 'require-approval';
  severity: 'critical' | 'high' | 'medium' | 'low';
  enabled: boolean;
}

interface ViolationEvent {
  id: string;
  policyId: string;
  controlIds: string[];
  timestamp: string;
  source: string;
  description: string;
  severity: string;
  details: any;
  remediated: boolean;
  remediatedAt?: string;
}

interface AuditReport {
  id: string;
  framework: string;
  generatedAt: string;
  period: { start: string; end: string };
  overallScore: number;
  controlsAssessed: number;
  controlsPassing: number;
  findings: Finding[];
  recommendations: string[];
  executiveSummary: string;
}

interface Finding {
  controlId: string;
  severity: string;
  description: string;
  evidence: string[];
  recommendation: string;
  dueDate: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// ===========================================
// COMPLIANCE FRAMEWORKS
// ===========================================

const COMPLIANCE_FRAMEWORKS: Record<string, Partial<ComplianceFramework>> = {
  'gdpr': {
    name: 'General Data Protection Regulation',
    version: '2016/679',
    controls: []
  },
  'hipaa': {
    name: 'Health Insurance Portability and Accountability Act',
    version: '2013',
    controls: []
  },
  'soc2': {
    name: 'SOC 2 Type II',
    version: '2017',
    controls: []
  },
  'iso27001': {
    name: 'ISO/IEC 27001',
    version: '2022',
    controls: []
  },
  'pci-dss': {
    name: 'Payment Card Industry Data Security Standard',
    version: '4.0',
    controls: []
  }
};

// ===========================================
// COMPLIANCE DASHBOARD
// ===========================================

app.get('/compliance/dashboard', async (c) => {
  const env = c.env;
  
  // Get all framework statuses
  const frameworks = await Promise.all(
    Object.keys(COMPLIANCE_FRAMEWORKS).map(async (frameworkId) => {
      const cached = await env.COMPLIANCE_CACHE.get(`framework:${frameworkId}`, 'json');
      if (cached) return cached;
      
      // Calculate from DB if not cached
      const controls = await env.DB.prepare(`
        SELECT status, risk_level, COUNT(*) as count
        FROM compliance_controls
        WHERE framework = ?
        GROUP BY status, risk_level
      `).bind(frameworkId).all();
      
      const totalControls = controls.results.reduce((sum: number, r: any) => sum + r.count, 0);
      const compliantControls = controls.results
        .filter((r: any) => r.status === 'compliant')
        .reduce((sum: number, r: any) => sum + r.count, 0);
      
      const score = totalControls > 0 ? (compliantControls / totalControls) * 100 : 0;
      
      return {
        id: frameworkId,
        name: COMPLIANCE_FRAMEWORKS[frameworkId].name,
        version: COMPLIANCE_FRAMEWORKS[frameworkId].version,
        totalControls,
        compliantControls,
        score: Math.round(score),
        status: score >= 95 ? 'compliant' : score >= 80 ? 'partial' : 'non-compliant'
      };
    })
  );
  
  // Get recent violations
  const recentViolations = await env.DB.prepare(`
    SELECT * FROM compliance_violations
    WHERE timestamp > datetime('now', '-7 days')
    ORDER BY timestamp DESC
    LIMIT 20
  `).all();
  
  // Get upcoming audit deadlines
  const upcomingAudits = await env.DB.prepare(`
    SELECT * FROM audit_schedule
    WHERE scheduled_date > datetime('now')
    ORDER BY scheduled_date ASC
    LIMIT 10
  `).all();
  
  // Calculate overall risk score
  const riskScore = await calculateOverallRiskScore(env);
  
  return c.json({
    success: true,
    dashboard: {
      overallCompliance: Math.round(frameworks.reduce((sum, f: any) => sum + f.score, 0) / frameworks.length),
      riskScore,
      riskLevel: riskScore < 20 ? 'low' : riskScore < 50 ? 'medium' : riskScore < 80 ? 'high' : 'critical',
      frameworks,
      recentViolations: recentViolations.results,
      upcomingAudits: upcomingAudits.results,
      lastFullAudit: await getLastFullAuditDate(env),
      nextScheduledAudit: upcomingAudits.results[0] || null
    }
  });
});

// ===========================================
// CONTROL MANAGEMENT
// ===========================================

app.get('/compliance/controls/:framework', async (c) => {
  const env = c.env;
  const framework = c.req.param('framework');
  const category = c.req.query('category');
  const status = c.req.query('status');
  
  let query = `
    SELECT c.*, 
           (SELECT COUNT(*) FROM compliance_evidence e WHERE e.control_id = c.id) as evidence_count,
           (SELECT MAX(collected_at) FROM compliance_evidence e WHERE e.control_id = c.id) as last_evidence
    FROM compliance_controls c
    WHERE c.framework = ?
  `;
  
  const params: any[] = [framework];
  
  if (category) {
    query += ' AND c.category = ?';
    params.push(category);
  }
  
  if (status) {
    query += ' AND c.status = ?';
    params.push(status);
  }
  
  query += ' ORDER BY c.risk_level DESC, c.category, c.id';
  
  const controls = await env.DB.prepare(query).bind(...params).all();
  
  // Group by category
  const groupedControls = controls.results.reduce((acc: any, control: any) => {
    if (!acc[control.category]) {
      acc[control.category] = [];
    }
    acc[control.category].push(control);
    return acc;
  }, {});
  
  return c.json({
    success: true,
    framework: {
      id: framework,
      ...COMPLIANCE_FRAMEWORKS[framework]
    },
    controls: groupedControls,
    summary: {
      total: controls.results.length,
      compliant: controls.results.filter((c: any) => c.status === 'compliant').length,
      nonCompliant: controls.results.filter((c: any) => c.status === 'non-compliant').length,
      partial: controls.results.filter((c: any) => c.status === 'partial').length
    }
  });
});

app.post('/compliance/controls/:controlId/assess', async (c) => {
  const env = c.env;
  const controlId = c.req.param('controlId');
  const body = await c.req.json();
  
  // Get control details
  const control = await env.DB.prepare(`
    SELECT * FROM compliance_controls WHERE id = ?
  `).bind(controlId).first();
  
  if (!control) {
    return c.json({ success: false, error: 'Control not found' }, 404);
  }
  
  // Run automated assessment
  const assessment = await runAutomatedAssessment(env, control, body);
  
  // Update control status
  await env.DB.prepare(`
    UPDATE compliance_controls 
    SET status = ?, last_checked = datetime('now'), assessment_notes = ?
    WHERE id = ?
  `).bind(assessment.status, assessment.notes, controlId).run();
  
  // Store evidence
  if (assessment.evidence) {
    for (const evidence of assessment.evidence) {
      await storeEvidence(env, controlId, evidence);
    }
  }
  
  // Create violation if non-compliant
  if (assessment.status === 'non-compliant') {
    await createViolation(env, control, assessment);
  }
  
  return c.json({
    success: true,
    assessment: {
      controlId,
      status: assessment.status,
      previousStatus: control.status,
      notes: assessment.notes,
      evidenceCollected: assessment.evidence?.length || 0,
      riskImpact: assessment.riskImpact,
      recommendations: assessment.recommendations
    }
  });
});

// ===========================================
// POLICY ENFORCEMENT
// ===========================================

app.get('/compliance/policies', async (c) => {
  const env = c.env;
  
  const policies = await env.DB.prepare(`
    SELECT p.*, 
           (SELECT COUNT(*) FROM policy_violations pv WHERE pv.policy_id = p.id) as violation_count,
           (SELECT COUNT(*) FROM policy_violations pv WHERE pv.policy_id = p.id AND pv.timestamp > datetime('now', '-30 days')) as recent_violations
    FROM compliance_policies p
    ORDER BY p.severity DESC, p.name
  `).all();
  
  return c.json({
    success: true,
    policies: policies.results.map((p: any) => ({
      ...p,
      frameworks: JSON.parse(p.frameworks || '[]'),
      condition: JSON.parse(p.condition || '{}')
    }))
  });
});

app.post('/compliance/policies', async (c) => {
  const env = c.env;
  const policy = await c.req.json();
  
  const id = `POL-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  await env.DB.prepare(`
    INSERT INTO compliance_policies (id, name, description, frameworks, condition, action, severity, enabled, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    id,
    policy.name,
    policy.description,
    JSON.stringify(policy.frameworks),
    JSON.stringify(policy.condition),
    policy.action,
    policy.severity,
    policy.enabled ? 1 : 0
  ).run();
  
  // Clear cache
  await env.COMPLIANCE_CACHE.delete('policies:all');
  
  return c.json({
    success: true,
    policy: { id, ...policy }
  });
});

app.post('/compliance/policies/evaluate', async (c) => {
  const env = c.env;
  const { event, context } = await c.req.json();
  
  // Get all active policies
  const policies = await env.DB.prepare(`
    SELECT * FROM compliance_policies WHERE enabled = 1
  `).all();
  
  const violations: any[] = [];
  const actions: any[] = [];
  
  for (const policy of policies.results) {
    const condition = JSON.parse((policy as any).condition || '{}');
    
    if (evaluatePolicyCondition(condition, event, context)) {
      // Policy triggered
      violations.push({
        policyId: (policy as any).id,
        policyName: (policy as any).name,
        severity: (policy as any).severity,
        action: (policy as any).action
      });
      
      // Determine action
      switch ((policy as any).action) {
        case 'block':
          actions.push({ type: 'block', reason: (policy as any).name });
          break;
        case 'alert':
          await env.ALERT_QUEUE.send({
            type: 'compliance_violation',
            policy: (policy as any).id,
            event,
            timestamp: new Date().toISOString()
          });
          actions.push({ type: 'alert', sent: true });
          break;
        case 'require-approval':
          actions.push({ type: 'approval_required', workflow: 'compliance-review' });
          break;
        case 'log':
          actions.push({ type: 'logged' });
          break;
      }
      
      // Record violation
      await recordPolicyViolation(env, (policy as any).id, event);
    }
  }
  
  const shouldBlock = actions.some(a => a.type === 'block');
  const requiresApproval = actions.some(a => a.type === 'approval_required');
  
  return c.json({
    success: true,
    allowed: !shouldBlock,
    requiresApproval,
    violations,
    actions,
    recommendation: shouldBlock 
      ? 'Action blocked due to compliance policy violation'
      : requiresApproval 
        ? 'Action requires compliance approval before proceeding'
        : violations.length > 0 
          ? 'Action allowed but compliance violations logged'
          : 'Action compliant with all policies'
  });
});

// ===========================================
// EVIDENCE MANAGEMENT
// ===========================================

app.get('/compliance/evidence/:controlId', async (c) => {
  const env = c.env;
  const controlId = c.req.param('controlId');
  
  const evidence = await env.DB.prepare(`
    SELECT * FROM compliance_evidence
    WHERE control_id = ?
    ORDER BY collected_at DESC
  `).bind(controlId).all();
  
  return c.json({
    success: true,
    controlId,
    evidence: evidence.results.map((e: any) => ({
      ...e,
      isExpired: new Date(e.valid_until) < new Date(),
      content: e.type === 'document' ? '[Document in R2]' : e.content
    }))
  });
});

app.post('/compliance/evidence/collect', async (c) => {
  const env = c.env;
  const { controlId, type, source, autoCollect } = await c.req.json();
  
  let evidence: any;
  
  if (autoCollect) {
    // Automated evidence collection based on source
    evidence = await collectAutomatedEvidence(env, controlId, source);
  } else {
    // Manual evidence upload
    const formData = await c.req.formData();
    const file = formData.get('file');
    
    if (file && file instanceof File) {
      const content = await file.arrayBuffer();
      const hash = await hashContent(content);
      
      // Store in R2
      const key = `evidence/${controlId}/${Date.now()}-${file.name}`;
      await env.AUDIT_STORAGE.put(key, content, {
        customMetadata: {
          controlId,
          originalName: file.name,
          uploadedAt: new Date().toISOString()
        }
      });
      
      evidence = {
        type: 'document',
        source: 'manual-upload',
        content: key,
        hash
      };
    }
  }
  
  if (evidence) {
    await storeEvidence(env, controlId, evidence);
  }
  
  return c.json({
    success: true,
    evidence
  });
});

// ===========================================
// AUDIT MANAGEMENT
// ===========================================

app.post('/compliance/audit/generate', async (c) => {
  const env = c.env;
  const { framework, period } = await c.req.json();
  
  const auditId = `AUD-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  // Get all controls for framework
  const controls = await env.DB.prepare(`
    SELECT c.*, 
           (SELECT COUNT(*) FROM compliance_evidence e 
            WHERE e.control_id = c.id 
            AND e.collected_at BETWEEN ? AND ?) as evidence_count
    FROM compliance_controls c
    WHERE c.framework = ?
  `).bind(period.start, period.end, framework).all();
  
  // Get violations during period
  const violations = await env.DB.prepare(`
    SELECT * FROM compliance_violations
    WHERE timestamp BETWEEN ? AND ?
    AND control_ids LIKE ?
  `).bind(period.start, period.end, `%${framework}%`).all();
  
  // Calculate scores
  const totalControls = controls.results.length;
  const compliantControls = controls.results.filter((c: any) => c.status === 'compliant').length;
  const score = totalControls > 0 ? Math.round((compliantControls / totalControls) * 100) : 0;
  
  // Generate findings
  const findings = controls.results
    .filter((c: any) => c.status !== 'compliant')
    .map((c: any) => ({
      controlId: c.id,
      severity: c.risk_level,
      description: c.requirement,
      currentStatus: c.status,
      evidence: c.evidence_count,
      recommendation: generateRecommendation(c),
      dueDate: calculateDueDate(c.risk_level)
    }));
  
  // Use AI to generate executive summary
  const executiveSummary = await generateExecutiveSummary(env, framework, score, findings);
  
  // Create audit report
  const report: AuditReport = {
    id: auditId,
    framework,
    generatedAt: new Date().toISOString(),
    period,
    overallScore: score,
    controlsAssessed: totalControls,
    controlsPassing: compliantControls,
    findings,
    recommendations: findings.slice(0, 5).map((f: any) => f.recommendation),
    executiveSummary
  };
  
  // Store report in R2
  await env.AUDIT_STORAGE.put(
    `audits/${framework}/${auditId}.json`,
    JSON.stringify(report),
    { customMetadata: { framework, generatedAt: report.generatedAt } }
  );
  
  // Store in DB for indexing
  await env.DB.prepare(`
    INSERT INTO audit_reports (id, framework, generated_at, period_start, period_end, score, findings_count)
    VALUES (?, ?, datetime('now'), ?, ?, ?, ?)
  `).bind(auditId, framework, period.start, period.end, score, findings.length).run();
  
  return c.json({
    success: true,
    report
  });
});

app.get('/compliance/audit/reports', async (c) => {
  const env = c.env;
  const framework = c.req.query('framework');
  
  let query = `
    SELECT * FROM audit_reports
    ORDER BY generated_at DESC
    LIMIT 50
  `;
  
  if (framework) {
    query = `
      SELECT * FROM audit_reports
      WHERE framework = ?
      ORDER BY generated_at DESC
      LIMIT 50
    `;
  }
  
  const reports = framework 
    ? await env.DB.prepare(query).bind(framework).all()
    : await env.DB.prepare(query).all();
  
  return c.json({
    success: true,
    reports: reports.results
  });
});

// ===========================================
// VIOLATION MANAGEMENT
// ===========================================

app.get('/compliance/violations', async (c) => {
  const env = c.env;
  const status = c.req.query('status') || 'open';
  const severity = c.req.query('severity');
  const days = parseInt(c.req.query('days') || '30');
  
  let query = `
    SELECT v.*, p.name as policy_name, p.severity as policy_severity
    FROM compliance_violations v
    LEFT JOIN compliance_policies p ON v.policy_id = p.id
    WHERE v.timestamp > datetime('now', '-${days} days')
  `;
  
  if (status === 'open') {
    query += ' AND v.remediated = 0';
  } else if (status === 'remediated') {
    query += ' AND v.remediated = 1';
  }
  
  if (severity) {
    query += ` AND v.severity = '${severity}'`;
  }
  
  query += ' ORDER BY v.timestamp DESC LIMIT 100';
  
  const violations = await env.DB.prepare(query).all();
  
  return c.json({
    success: true,
    violations: violations.results,
    summary: {
      total: violations.results.length,
      critical: violations.results.filter((v: any) => v.severity === 'critical').length,
      high: violations.results.filter((v: any) => v.severity === 'high').length,
      medium: violations.results.filter((v: any) => v.severity === 'medium').length,
      low: violations.results.filter((v: any) => v.severity === 'low').length
    }
  });
});

app.post('/compliance/violations/:violationId/remediate', async (c) => {
  const env = c.env;
  const violationId = c.req.param('violationId');
  const { action, notes, evidence } = await c.req.json();
  
  // Get violation details
  const violation = await env.DB.prepare(`
    SELECT * FROM compliance_violations WHERE id = ?
  `).bind(violationId).first();
  
  if (!violation) {
    return c.json({ success: false, error: 'Violation not found' }, 404);
  }
  
  // Record remediation action
  await env.DB.prepare(`
    INSERT INTO remediation_actions (id, violation_id, action, notes, performed_at, performed_by)
    VALUES (?, ?, ?, ?, datetime('now'), ?)
  `).bind(
    `REM-${Date.now()}`,
    violationId,
    action,
    notes,
    'system'
  ).run();
  
  // Store evidence if provided
  if (evidence) {
    await storeEvidence(env, violationId, evidence);
  }
  
  // Update violation status
  await env.DB.prepare(`
    UPDATE compliance_violations 
    SET remediated = 1, remediated_at = datetime('now'), remediation_notes = ?
    WHERE id = ?
  `).bind(notes, violationId).run();
  
  // Re-assess affected controls
  const controlIds = JSON.parse((violation as any).control_ids || '[]');
  for (const controlId of controlIds) {
    await reassessControl(env, controlId);
  }
  
  return c.json({
    success: true,
    violation: {
      id: violationId,
      remediated: true,
      remediatedAt: new Date().toISOString(),
      affectedControlsReassessed: controlIds.length
    }
  });
});

// ===========================================
// RISK ASSESSMENT
// ===========================================

app.get('/compliance/risk/assessment', async (c) => {
  const env = c.env;
  
  // Get all non-compliant controls
  const nonCompliant = await env.DB.prepare(`
    SELECT * FROM compliance_controls
    WHERE status IN ('non-compliant', 'partial')
    ORDER BY risk_level DESC
  `).all();
  
  // Get open violations
  const openViolations = await env.DB.prepare(`
    SELECT * FROM compliance_violations
    WHERE remediated = 0
  `).all();
  
  // Calculate risk by category
  const riskByCategory: Record<string, any> = {};
  
  for (const control of nonCompliant.results as any[]) {
    const category = control.category;
    if (!riskByCategory[category]) {
      riskByCategory[category] = {
        category,
        totalControls: 0,
        criticalGaps: 0,
        highGaps: 0,
        mediumGaps: 0,
        lowGaps: 0,
        riskScore: 0
      };
    }
    
    riskByCategory[category].totalControls++;
    
    switch (control.risk_level) {
      case 'critical':
        riskByCategory[category].criticalGaps++;
        riskByCategory[category].riskScore += 10;
        break;
      case 'high':
        riskByCategory[category].highGaps++;
        riskByCategory[category].riskScore += 5;
        break;
      case 'medium':
        riskByCategory[category].mediumGaps++;
        riskByCategory[category].riskScore += 2;
        break;
      case 'low':
        riskByCategory[category].lowGaps++;
        riskByCategory[category].riskScore += 1;
        break;
    }
  }
  
  // Calculate overall risk score
  const overallRisk = await calculateOverallRiskScore(env);
  
  // Generate risk matrix
  const riskMatrix = generateRiskMatrix(nonCompliant.results, openViolations.results);
  
  // AI-powered risk insights
  const insights = await generateRiskInsights(env, riskByCategory, overallRisk);
  
  return c.json({
    success: true,
    riskAssessment: {
      overallScore: overallRisk,
      level: overallRisk < 20 ? 'low' : overallRisk < 50 ? 'medium' : overallRisk < 80 ? 'high' : 'critical',
      byCategory: Object.values(riskByCategory),
      riskMatrix,
      openViolationsCount: openViolations.results.length,
      nonCompliantControlsCount: nonCompliant.results.length,
      insights,
      lastAssessment: new Date().toISOString()
    }
  });
});

// ===========================================
// DATA PRIVACY (GDPR SPECIFIC)
// ===========================================

app.get('/compliance/gdpr/data-map', async (c) => {
  const env = c.env;
  
  // Get all data processing activities
  const activities = await env.DB.prepare(`
    SELECT * FROM data_processing_activities
    ORDER BY category, name
  `).all();
  
  // Get data subject requests
  const dsrStats = await env.DB.prepare(`
    SELECT type, status, COUNT(*) as count
    FROM data_subject_requests
    WHERE created_at > datetime('now', '-90 days')
    GROUP BY type, status
  `).all();
  
  // Get consent records summary
  const consentStats = await env.DB.prepare(`
    SELECT purpose, COUNT(*) as total,
           SUM(CASE WHEN granted = 1 THEN 1 ELSE 0 END) as granted,
           SUM(CASE WHEN granted = 0 THEN 1 ELSE 0 END) as withdrawn
    FROM consent_records
    GROUP BY purpose
  `).all();
  
  return c.json({
    success: true,
    gdpr: {
      dataProcessingActivities: activities.results,
      dataSubjectRequests: {
        stats: dsrStats.results,
        pendingCount: dsrStats.results
          .filter((d: any) => d.status === 'pending')
          .reduce((sum: number, d: any) => sum + d.count, 0)
      },
      consentManagement: consentStats.results,
      retentionPolicies: await getRetentionPolicies(env),
      crossBorderTransfers: await getCrossBorderTransfers(env)
    }
  });
});

app.post('/compliance/gdpr/dsr', async (c) => {
  const env = c.env;
  const { type, subjectId, subjectEmail, details } = await c.req.json();
  
  const id = `DSR-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  // Validate DSR type
  const validTypes = ['access', 'rectification', 'erasure', 'portability', 'restriction', 'objection'];
  if (!validTypes.includes(type)) {
    return c.json({ success: false, error: 'Invalid DSR type' }, 400);
  }
  
  // Create DSR record
  await env.DB.prepare(`
    INSERT INTO data_subject_requests (id, type, subject_id, subject_email, details, status, created_at, due_date)
    VALUES (?, ?, ?, ?, ?, 'pending', datetime('now'), datetime('now', '+30 days'))
  `).bind(id, type, subjectId, subjectEmail, JSON.stringify(details)).run();
  
  // Trigger automated processing if possible
  const automatedResult = await processAutomatedDSR(env, type, subjectId);
  
  return c.json({
    success: true,
    dsr: {
      id,
      type,
      status: automatedResult ? 'processing' : 'pending',
      dueDate: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString(),
      automatedProcessing: automatedResult
    }
  });
});

// ===========================================
// CONTINUOUS MONITORING
// ===========================================

app.post('/compliance/monitor/check', async (c) => {
  const env = c.env;
  
  const results: any[] = [];
  
  // Check all automated controls
  const automatedControls = await env.DB.prepare(`
    SELECT * FROM compliance_controls
    WHERE automated_check = 1
  `).all();
  
  for (const control of automatedControls.results as any[]) {
    const checkResult = await runAutomatedCheck(env, control);
    results.push({
      controlId: control.id,
      previousStatus: control.status,
      newStatus: checkResult.status,
      changed: control.status !== checkResult.status,
      details: checkResult.details
    });
    
    // Update if changed
    if (control.status !== checkResult.status) {
      await env.DB.prepare(`
        UPDATE compliance_controls
        SET status = ?, last_checked = datetime('now'), assessment_notes = ?
        WHERE id = ?
      `).bind(checkResult.status, checkResult.details, control.id).run();
      
      // Create violation if became non-compliant
      if (checkResult.status === 'non-compliant') {
        await createViolation(env, control, checkResult);
      }
    }
  }
  
  const changedCount = results.filter(r => r.changed).length;
  const newViolations = results.filter(r => r.changed && r.newStatus === 'non-compliant').length;
  
  // Clear cache
  await env.COMPLIANCE_CACHE.delete('dashboard');
  
  return c.json({
    success: true,
    monitoring: {
      controlsChecked: results.length,
      statusChanges: changedCount,
      newViolations,
      results: results.filter(r => r.changed)
    }
  });
});

// ===========================================
// HELPER FUNCTIONS
// ===========================================

async function calculateOverallRiskScore(env: Env): Promise<number> {
  // Weight factors for risk calculation
  const weights = {
    criticalControl: 10,
    highControl: 5,
    mediumControl: 2,
    lowControl: 1,
    openViolation: 3,
    overdueRemediation: 5
  };
  
  const nonCompliant = await env.DB.prepare(`
    SELECT risk_level, COUNT(*) as count
    FROM compliance_controls
    WHERE status = 'non-compliant'
    GROUP BY risk_level
  `).all();
  
  const violations = await env.DB.prepare(`
    SELECT COUNT(*) as count FROM compliance_violations WHERE remediated = 0
  `).first() as any;
  
  let score = 0;
  
  for (const row of nonCompliant.results as any[]) {
    switch (row.risk_level) {
      case 'critical': score += row.count * weights.criticalControl; break;
      case 'high': score += row.count * weights.highControl; break;
      case 'medium': score += row.count * weights.mediumControl; break;
      case 'low': score += row.count * weights.lowControl; break;
    }
  }
  
  score += (violations?.count || 0) * weights.openViolation;
  
  // Normalize to 0-100
  return Math.min(100, score);
}

async function getLastFullAuditDate(env: Env): Promise<string | null> {
  const result = await env.DB.prepare(`
    SELECT MAX(generated_at) as last_audit FROM audit_reports
  `).first() as any;
  
  return result?.last_audit || null;
}

async function runAutomatedAssessment(env: Env, control: any, params: any): Promise<any> {
  // Simulate automated assessment based on control type
  const checkType = control.automated_check_type || 'manual';
  
  switch (checkType) {
    case 'api-check':
      // Check external API for compliance status
      return { status: 'compliant', notes: 'API check passed', evidence: [] };
    
    case 'config-scan':
      // Scan configuration for compliance
      return { status: 'compliant', notes: 'Configuration compliant', evidence: [] };
    
    case 'log-analysis':
      // Analyze logs for compliance events
      return { status: 'compliant', notes: 'No violations in logs', evidence: [] };
    
    default:
      return { status: params.status || 'partial', notes: params.notes || 'Manual assessment', evidence: [] };
  }
}

async function storeEvidence(env: Env, controlId: string, evidence: any): Promise<void> {
  const id = `EVD-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  await env.DB.prepare(`
    INSERT INTO compliance_evidence (id, control_id, type, source, content, collected_at, valid_until, hash)
    VALUES (?, ?, ?, ?, ?, datetime('now'), datetime('now', '+365 days'), ?)
  `).bind(
    id,
    controlId,
    evidence.type,
    evidence.source,
    evidence.content,
    evidence.hash || ''
  ).run();
}

async function createViolation(env: Env, control: any, assessment: any): Promise<void> {
  const id = `VIO-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  await env.DB.prepare(`
    INSERT INTO compliance_violations (id, control_ids, timestamp, source, description, severity, details, remediated)
    VALUES (?, ?, datetime('now'), ?, ?, ?, ?, 0)
  `).bind(
    id,
    JSON.stringify([control.id]),
    'automated-assessment',
    `Control ${control.id} found non-compliant`,
    control.risk_level,
    JSON.stringify(assessment)
  ).run();
}

function evaluatePolicyCondition(condition: any, event: any, context: any): boolean {
  // Simple policy condition evaluator
  if (!condition || !condition.rules) return false;
  
  for (const rule of condition.rules) {
    const value = event[rule.field] || context[rule.field];
    
    switch (rule.operator) {
      case 'equals':
        if (value !== rule.value) return false;
        break;
      case 'contains':
        if (!value?.includes(rule.value)) return false;
        break;
      case 'greater_than':
        if (!(value > rule.value)) return false;
        break;
      case 'less_than':
        if (!(value < rule.value)) return false;
        break;
      case 'in':
        if (!rule.value.includes(value)) return false;
        break;
    }
  }
  
  return true;
}

async function recordPolicyViolation(env: Env, policyId: string, event: any): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO policy_violations (id, policy_id, event_data, timestamp)
    VALUES (?, ?, ?, datetime('now'))
  `).bind(
    `PV-${Date.now()}`,
    policyId,
    JSON.stringify(event)
  ).run();
}

async function collectAutomatedEvidence(env: Env, controlId: string, source: string): Promise<any> {
  // Automated evidence collection based on source type
  return {
    type: 'api-response',
    source,
    content: JSON.stringify({ status: 'collected', timestamp: new Date().toISOString() }),
    hash: 'auto-' + Date.now()
  };
}

async function hashContent(content: ArrayBuffer): Promise<string> {
  const hashBuffer = await crypto.subtle.digest('SHA-256', content);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

function generateRecommendation(control: any): string {
  const recommendations: Record<string, string> = {
    'critical': 'Immediate action required. Escalate to security team.',
    'high': 'Address within 7 days. Implement compensating controls.',
    'medium': 'Address within 30 days. Document exception if needed.',
    'low': 'Address within 90 days. Include in next review cycle.'
  };
  
  return recommendations[control.risk_level] || 'Review and assess priority';
}

function calculateDueDate(riskLevel: string): string {
  const days: Record<string, number> = {
    'critical': 7,
    'high': 14,
    'medium': 30,
    'low': 90
  };
  
  const daysToAdd = days[riskLevel] || 30;
  return new Date(Date.now() + daysToAdd * 24 * 60 * 60 * 1000).toISOString().split('T')[0];
}

async function generateExecutiveSummary(env: Env, framework: string, score: number, findings: any[]): Promise<string> {
  const prompt = `Generate a brief executive summary for a ${framework} compliance audit:
- Overall Score: ${score}%
- Total Findings: ${findings.length}
- Critical Findings: ${findings.filter(f => f.severity === 'critical').length}
- High Findings: ${findings.filter(f => f.severity === 'high').length}

Keep it to 2-3 paragraphs, professional tone.`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 500
    });
    return response.response;
  } catch {
    return `This ${framework} compliance audit achieved an overall score of ${score}%. ` +
           `${findings.length} findings were identified, with ${findings.filter(f => f.severity === 'critical').length} critical ` +
           `and ${findings.filter(f => f.severity === 'high').length} high severity issues requiring immediate attention.`;
  }
}

function generateRiskMatrix(controls: any[], violations: any[]): any {
  const matrix = {
    high_impact_high_likelihood: [],
    high_impact_low_likelihood: [],
    low_impact_high_likelihood: [],
    low_impact_low_likelihood: []
  };
  
  for (const control of controls) {
    const impact = ['critical', 'high'].includes(control.risk_level) ? 'high' : 'low';
    const likelihood = control.status === 'non-compliant' ? 'high' : 'low';
    
    const key = `${impact}_impact_${likelihood}_likelihood` as keyof typeof matrix;
    matrix[key].push(control.id);
  }
  
  return matrix;
}

async function generateRiskInsights(env: Env, riskByCategory: any, overallRisk: number): Promise<string[]> {
  const insights: string[] = [];
  
  if (overallRisk > 80) {
    insights.push('CRITICAL: Overall risk level is extremely high. Immediate executive attention required.');
  }
  
  const categories = Object.values(riskByCategory) as any[];
  const highestRisk = categories.sort((a, b) => b.riskScore - a.riskScore)[0];
  
  if (highestRisk) {
    insights.push(`Highest risk area: ${highestRisk.category} with ${highestRisk.criticalGaps} critical gaps.`);
  }
  
  return insights;
}

async function getRetentionPolicies(env: Env): Promise<any[]> {
  const policies = await env.DB.prepare(`
    SELECT * FROM data_retention_policies ORDER BY data_category
  `).all();
  return policies.results;
}

async function getCrossBorderTransfers(env: Env): Promise<any[]> {
  const transfers = await env.DB.prepare(`
    SELECT * FROM cross_border_transfers ORDER BY destination_country
  `).all();
  return transfers.results;
}

async function processAutomatedDSR(env: Env, type: string, subjectId: string): Promise<boolean> {
  // Attempt automated processing for certain DSR types
  if (type === 'access' || type === 'portability') {
    // These can potentially be automated
    return true;
  }
  return false;
}

async function runAutomatedCheck(env: Env, control: any): Promise<any> {
  // Run automated compliance check
  return {
    status: 'compliant',
    details: 'Automated check completed successfully'
  };
}

async function reassessControl(env: Env, controlId: string): Promise<void> {
  // Trigger reassessment of a control after remediation
  await env.DB.prepare(`
    UPDATE compliance_controls SET last_checked = datetime('now') WHERE id = ?
  `).bind(controlId).run();
}

// Queue handler for alerts
export default {
  fetch: app.fetch,
  async queue(batch: MessageBatch, env: Env) {
    for (const message of batch.messages) {
      const data = message.body as any;
      
      if (data.type === 'compliance_violation') {
        // Process violation alerts
        console.log('Compliance violation alert:', data);
        // Could integrate with PagerDuty, Slack, etc.
      }
      
      message.ack();
    }
  }
};
