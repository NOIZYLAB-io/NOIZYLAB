/**
 * 🌌 OMEGA CORE
 * The master AI brain, coordinator of all systems
 * Fish Music Inc - CB_01
 * 🔥 GORUNFREE! 🎸🔥
 */

import { fuse } from '../intelligence/fusion_engine';
import { shadowModel } from '../intelligence/shadow_device_model';
import { fallback } from '../orchestration/fallback_manager';
import { orchestratePipeline } from '../orchestration/pipeline_orchestrator';
import { safeExecuteAsync } from '../orchestration/safe_executor';
import { buildContext } from '../router/context_builder';

export async function omegaCore(input: any) {
  console.log('');
  console.log('╔═══════════════════════════════════════════════════════════════╗');
  console.log('║                                                               ║');
  console.log('║              🌌 OMEGA CORE ACTIVATED 🌌                       ║');
  console.log('║                                                               ║');
  console.log('╚═══════════════════════════════════════════════════════════════╝');
  console.log('');

  try {
    // Build unified context
    console.log('🏗️  [1/5] Building context...');
    const context = buildContext(input);

    // Create shadow device model
    console.log('👻 [2/5] Creating shadow device model...');
    const shadow = shadowModel(context);
    const prediction = shadow.predict();
    console.log(`   Prediction: ${prediction}`);

    // Run genius pipeline
    console.log('⚙️  [3/5] Orchestrating genius pipeline...');
    const pipeline = await safeExecuteAsync(
      () => orchestratePipeline({ ...input, context }),
      async (error) => {
        console.error('Pipeline failed, using fallback');
        return fallback(error);
      }
    );

    // Fuse results
    console.log('🔬 [4/5] Fusing multi-genius responses...');
    const fused = fuse(pipeline.results || []);

    // Generate final response
    console.log('✨ [5/5] Generating final response...');
    const response = {
      omega: true,
      session_id: input.session_id || `omega_${Date.now()}`,
      timestamp: new Date().toISOString(),
      
      context: {
        device: context.device,
        os: context.device?.os
      },
      
      prediction: {
        state: prediction,
        risk_score: this.calculateRiskScore(fused)
      },
      
      pipeline: {
        geniuses_called: pipeline.geniuses_called || [],
        results_count: pipeline.results?.length || 0
      },
      
      findings: fused.all_findings || [],
      recommendations: fused.priority_actions || [],
      
      confidence: fused.confidence_average || 0.9,
      
      next_steps: this.generateNextSteps(fused),
      
      metadata: {
        processing_time_ms: Date.now() - (input.start_time || Date.now()),
        version: '1.0.0'
      }
    };

    console.log('');
    console.log('✅ OMEGA CORE processing complete');
    console.log(`   Confidence: ${(response.confidence * 100).toFixed(1)}%`);
    console.log(`   Findings: ${response.findings.length}`);
    console.log(`   Recommendations: ${response.recommendations.length}`);
    console.log('');
    console.log('🔥 GORUNFREE! 🎸🔥');
    console.log('');

    return response;

  } catch (error) {
    console.error('❌ OMEGA CORE error:', error);
    
    return {
      omega: false,
      error: true,
      message: 'Omega Core encountered an error',
      fallback: fallback(error)
    };
  }
}

function calculateRiskScore(fused: any): number {
  const findings = fused.all_findings || [];
  
  let risk = 0;
  
  for (const finding of findings) {
    const lower = finding.toLowerCase();
    
    if (lower.includes('critical') || lower.includes('urgent') || lower.includes('failure')) {
      risk += 30;
    } else if (lower.includes('warning') || lower.includes('risk')) {
      risk += 15;
    } else if (lower.includes('recommended') || lower.includes('should')) {
      risk += 5;
    }
  }
  
  return Math.min(risk, 100);  // Cap at 100
}

function generateNextSteps(fused: any): string[] {
  const steps: string[] = [];
  
  const recs = fused.priority_actions || [];
  
  if (recs.length === 0) {
    return ['Device is healthy. No action needed.'];
  }
  
  // Take top 3-5 priority actions
  steps.push(...recs.slice(0, 5));
  
  // Add follow-up
  steps.push('Schedule follow-up scan in 30 days');
  
  return steps;
}
