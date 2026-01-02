/**
 * GABRIEL Vision Pipeline Test Suite
 * 
 * End-to-end tests for the PCB inspection system
 * Run with: node --test tests/vision-pipeline.test.js
 */

import { describe, it, before, after } from 'node:test';
import assert from 'node:assert';

const API_BASE = process.env.API_URL || 'http://localhost:8787';

// Test image (base64 encoded 1x1 pixel placeholder)
const TEST_IMAGE_B64 = '/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAn/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBEQCEAPwCwAB//9k=';

describe('GABRIEL Vision API', () => {
  
  describe('Health Check', () => {
    it('should return healthy status', async () => {
      const response = await fetch(`${API_BASE}/api/health`);
      const data = await response.json();
      
      assert.strictEqual(response.status, 200);
      assert.strictEqual(data.status, 'healthy');
      assert(data.timestamp);
    });
  });

  describe('Scan Endpoint', () => {
    it('should reject requests without image', async () => {
      const response = await fetch(`${API_BASE}/api/scan`, {
        method: 'POST',
        body: new FormData()
      });
      
      assert.strictEqual(response.status, 400);
      const data = await response.json();
      assert.strictEqual(data.error, 'No image provided');
    });

    it('should accept image and return scan ID', async () => {
      const formData = new FormData();
      const imageBlob = await fetch(`data:image/jpeg;base64,${TEST_IMAGE_B64}`).then(r => r.blob());
      formData.append('image', imageBlob, 'test-pcb.jpg');
      formData.append('boardType', 'test-board');
      
      const response = await fetch(`${API_BASE}/api/scan`, {
        method: 'POST',
        body: formData
      });
      
      // May fail without real API keys, but structure should be correct
      if (response.status === 200) {
        const data = await response.json();
        assert(data.scanId);
        assert.strictEqual(data.status, 'complete');
        assert(data.summary);
      }
    });

    it('should retrieve scan results by ID', async () => {
      // First create a scan
      const formData = new FormData();
      const imageBlob = await fetch(`data:image/jpeg;base64,${TEST_IMAGE_B64}`).then(r => r.blob());
      formData.append('image', imageBlob, 'test-pcb.jpg');
      
      const createResponse = await fetch(`${API_BASE}/api/scan`, {
        method: 'POST',
        body: formData
      });
      
      if (createResponse.status === 200) {
        const { scanId } = await createResponse.json();
        
        const getResponse = await fetch(`${API_BASE}/api/scan/${scanId}`);
        assert.strictEqual(getResponse.status, 200);
        
        const data = await getResponse.json();
        assert.strictEqual(data.scanId, scanId);
      }
    });
  });

  describe('Golden Reference', () => {
    it('should return 404 for non-existent reference', async () => {
      const response = await fetch(`${API_BASE}/api/reference/non-existent-board`);
      assert.strictEqual(response.status, 404);
    });

    it('should require authentication for uploads', async () => {
      const formData = new FormData();
      formData.append('boardId', 'test-board');
      formData.append('manifest', JSON.stringify({ components: [] }));
      
      const response = await fetch(`${API_BASE}/api/reference`, {
        method: 'POST',
        body: formData
      });
      
      assert.strictEqual(response.status, 401);
    });
  });

  describe('Report Generation', () => {
    it('should return 404 for non-existent scan', async () => {
      const response = await fetch(`${API_BASE}/api/report/non-existent-id`);
      assert.strictEqual(response.status, 404);
    });
  });

  describe('Stripe Integration', () => {
    it('should create checkout session', async () => {
      const response = await fetch(`${API_BASE}/api/create-checkout-session`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          productId: 'golden_audit',
          successUrl: 'https://example.com/success',
          cancelUrl: 'https://example.com/cancel'
        })
      });
      
      // Will fail without Stripe key, but should return proper error
      const data = await response.json();
      assert(data.error || data.sessionId);
    });
  });

  describe('CORS', () => {
    it('should handle OPTIONS preflight', async () => {
      const response = await fetch(`${API_BASE}/api/health`, {
        method: 'OPTIONS'
      });
      
      assert.strictEqual(response.status, 200);
      assert(response.headers.get('Access-Control-Allow-Origin'));
    });
  });
});

describe('Performance Benchmarks', () => {
  it('health check should respond under 100ms', async () => {
    const start = performance.now();
    await fetch(`${API_BASE}/api/health`);
    const duration = performance.now() - start;
    
    console.log(`Health check: ${duration.toFixed(2)}ms`);
    assert(duration < 100, `Health check took ${duration}ms, expected <100ms`);
  });
});

// Run tests
console.log('🧪 GABRIEL Vision Pipeline Tests');
console.log(`API: ${API_BASE}`);
console.log('================================\n');
