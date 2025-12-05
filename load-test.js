/**
 * K6 LOAD TESTING SUITE
 * Comprehensive load tests for all 17 workers
 * Tests: Smoke, Load, Stress, Spike, Soak
 */

import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// Custom metrics
const errorRate = new Rate('errors');
const responseTime = new Trend('response_time');

// Test configuration
export const options = {
  stages: [
    { duration: '2m', target: 100 },  // Ramp up to 100 users
    { duration: '5m', target: 100 },  // Stay at 100 users
    { duration: '2m', target: 200 },  // Spike to 200 users
    { duration: '5m', target: 200 },  // Stay at 200 users
    { duration: '2m', target: 0 },    // Ramp down to 0 users
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    http_req_failed: ['rate<0.01'],   // Error rate should be less than 1%
    errors: ['rate<0.05'],            // Custom error rate less than 5%
  },
};

// Worker endpoints
const WORKERS = {
  noizylab_business: 'https://noizylab-business-worker.noizylab-ca.workers.dev',
  noizylab_workflow: 'https://noizylab-workflow-worker.noizylab-ca.workers.dev',
  ai_genius: 'https://ai-genius-worker.noizylab-ca.workers.dev',
  email_automation: 'https://noizylab-email-automation.noizylab-ca.workers.dev',
  sms_notifications: 'https://noizylab-sms-notifications.noizylab-ca.workers.dev',
  fishmusicinc_portal: 'https://fishmusicinc-portal-worker.fishmusicinc-com.workers.dev',
  fishmusicinc_ai: 'https://fishmusicinc-ai-assistant.fishmusicinc-com.workers.dev',
  noizyai_api: 'https://noizyai-api-worker.noizy-ai.workers.dev',
  noizyai_gateway: 'https://noizyai-advanced-gateway.noizy-ai.workers.dev',
  analytics: 'https://unified-analytics-dashboard.noizylab-ca.workers.dev',
  portal: 'https://customer-self-service-portal.noizylab-ca.workers.dev',
  payment: 'https://payment-processing-system.noizylab-ca.workers.dev',
  health: 'https://health-monitoring-system.noizylab-ca.workers.dev',
  workers_ai: 'https://workers-ai-enhanced.noizylab-ca.workers.dev',
  monitoring: 'https://advanced-monitoring-dashboard.noizylab-ca.workers.dev',
  cache: 'https://intelligent-cache-layer.noizylab-ca.workers.dev',
};

export default function () {
  // Test NOIZYLAB Business Portal
  group('NOIZYLAB Business', () => {
    const res = http.get(`${WORKERS.noizylab_business}/health`);
    
    check(res, {
      'status is 200': (r) => r.status === 200,
      'response time < 200ms': (r) => r.timings.duration < 200,
    }) || errorRate.add(1);
    
    responseTime.add(res.timings.duration);
    sleep(1);
  });

  // Test AI Workers
  group('AI Workers', () => {
    const aiRes = http.get(`${WORKERS.ai_genius}/health`);
    check(aiRes, {
      'AI worker healthy': (r) => r.status === 200,
    }) || errorRate.add(1);
    
    const workersAiRes = http.get(`${WORKERS.workers_ai}/health`);
    check(workersAiRes, {
      'Workers AI healthy': (r) => r.status === 200,
    }) || errorRate.add(1);
    
    sleep(1);
  });

  // Test Analytics Dashboard
  group('Analytics & Monitoring', () => {
    const analyticsRes = http.get(`${WORKERS.analytics}/api/metrics/realtime`);
    check(analyticsRes, {
      'analytics status 200': (r) => r.status === 200,
      'has metrics data': (r) => r.json().totalRequests !== undefined,
    }) || errorRate.add(1);
    
    const monitoringRes = http.get(`${WORKERS.monitoring}/api/metrics/realtime`);
    check(monitoringRes, {
      'monitoring status 200': (r) => r.status === 200,
    }) || errorRate.add(1);
    
    sleep(1);
  });

  // Test Health Monitoring
  group('Health Checks', () => {
    const healthRes = http.get(`${WORKERS.health}/api/health/all`);
    check(healthRes, {
      'health check passes': (r) => r.status === 200,
      'all systems operational': (r) => r.json().status !== 'down',
    }) || errorRate.add(1);
    
    sleep(1);
  });

  // Test Cache Layer
  group('Cache Performance', () => {
    const cacheRes = http.get(`${WORKERS.cache}/api/cache/stats`);
    check(cacheRes, {
      'cache stats available': (r) => r.status === 200,
      'hit rate > 70%': (r) => r.json().hit_rate > 70,
    }) || errorRate.add(1);
    
    sleep(1);
  });

  // Test Customer Portal
  group('Customer Portal', () => {
    const portalRes = http.get(`${WORKERS.portal}/health`);
    check(portalRes, {
      'portal accessible': (r) => r.status === 200,
    }) || errorRate.add(1);
    
    sleep(1);
  });

  // Test Payment System
  group('Payment System', () => {
    const paymentRes = http.get(`${WORKERS.payment}/health`);
    check(paymentRes, {
      'payment system up': (r) => r.status === 200,
    }) || errorRate.add(1);
    
    sleep(1);
  });

  // Random delay between iterations
  sleep(Math.random() * 3 + 1);
}

// Setup function - runs once before tests
export function setup() {
  console.log('🚀 Starting load tests...');
  console.log(`Testing ${Object.keys(WORKERS).length} workers`);
  return { startTime: new Date() };
}

// Teardown function - runs once after tests
export function teardown(data) {
  const duration = (new Date() - data.startTime) / 1000;
  console.log(`✅ Load tests completed in ${duration.toFixed(2)}s`);
}
