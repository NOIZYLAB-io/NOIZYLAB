/**
 * End-to-End Test Suite for GABRIEL Portal
 * 
 * Tests the complete user journey from signup to scan completion.
 * Run with: npx playwright test
 */

import { test, expect, Page } from '@playwright/test';

// Test configuration
const BASE_URL = process.env.TEST_URL || 'http://localhost:3000';
const API_URL = process.env.API_URL || 'http://localhost:8787';

// Test user credentials
const TEST_USER = {
  email: 'test@noizylab.com',
  password: 'TestPass123!',
  name: 'Test User',
};

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

async function login(page: Page) {
  await page.goto(`${BASE_URL}/login`);
  await page.fill('[data-testid="email-input"]', TEST_USER.email);
  await page.fill('[data-testid="password-input"]', TEST_USER.password);
  await page.click('[data-testid="login-button"]');
  await page.waitForURL('**/dashboard');
}

async function waitForAPI(page: Page) {
  await page.waitForResponse(response => 
    response.url().includes('/api/') && response.status() === 200
  );
}

// ============================================================================
// AUTHENTICATION TESTS
// ============================================================================

test.describe('Authentication', () => {
  test('should display login page', async ({ page }) => {
    await page.goto(`${BASE_URL}/login`);
    await expect(page.locator('h1')).toContainText(/sign in|login/i);
    await expect(page.locator('[data-testid="email-input"]')).toBeVisible();
    await expect(page.locator('[data-testid="password-input"]')).toBeVisible();
  });

  test('should show error for invalid credentials', async ({ page }) => {
    await page.goto(`${BASE_URL}/login`);
    await page.fill('[data-testid="email-input"]', 'wrong@email.com');
    await page.fill('[data-testid="password-input"]', 'wrongpassword');
    await page.click('[data-testid="login-button"]');
    
    await expect(page.locator('[data-testid="error-message"]')).toBeVisible();
  });

  test('should redirect to dashboard after login', async ({ page }) => {
    await login(page);
    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.locator('[data-testid="user-menu"]')).toBeVisible();
  });

  test('should logout successfully', async ({ page }) => {
    await login(page);
    await page.click('[data-testid="user-menu"]');
    await page.click('[data-testid="logout-button"]');
    await expect(page).toHaveURL(/.*login/);
  });
});

// ============================================================================
// SCAN FLOW TESTS
// ============================================================================

test.describe('Scan Flow', () => {
  test.beforeEach(async ({ page }) => {
    await login(page);
  });

  test('should navigate to scan page', async ({ page }) => {
    await page.click('[data-testid="new-scan-button"]');
    await expect(page).toHaveURL(/.*scan/);
    await expect(page.locator('[data-testid="camera-preview"]')).toBeVisible();
  });

  test('should upload image for scanning', async ({ page }) => {
    await page.goto(`${BASE_URL}/scan`);
    
    // Upload test image
    const fileInput = page.locator('input[type="file"]');
    await fileInput.setInputFiles('tests/fixtures/test-board.jpg');
    
    // Wait for upload to complete
    await expect(page.locator('[data-testid="image-preview"]')).toBeVisible();
    
    // Start scan
    await page.click('[data-testid="analyze-button"]');
    
    // Wait for processing
    await expect(page.locator('[data-testid="processing-indicator"]')).toBeVisible();
  });

  test('should display scan results', async ({ page }) => {
    await page.goto(`${BASE_URL}/scan/test-scan-id`);
    
    await expect(page.locator('[data-testid="scan-results"]')).toBeVisible();
    await expect(page.locator('[data-testid="issue-list"]')).toBeVisible();
  });

  test('should show AR overlay on results', async ({ page }) => {
    await page.goto(`${BASE_URL}/scan/test-scan-id`);
    
    await page.click('[data-testid="toggle-ar-overlay"]');
    await expect(page.locator('[data-testid="ar-canvas"]')).toBeVisible();
  });

  test('should generate PDF report', async ({ page }) => {
    await page.goto(`${BASE_URL}/scan/test-scan-id`);
    
    const [download] = await Promise.all([
      page.waitForEvent('download'),
      page.click('[data-testid="download-report"]'),
    ]);
    
    expect(download.suggestedFilename()).toMatch(/gabriel-report.*\.pdf/);
  });
});

// ============================================================================
// DASHBOARD TESTS
// ============================================================================

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    await login(page);
  });

  test('should display user stats', async ({ page }) => {
    await expect(page.locator('[data-testid="total-scans"]')).toBeVisible();
    await expect(page.locator('[data-testid="credits-remaining"]')).toBeVisible();
  });

  test('should show recent scans', async ({ page }) => {
    await expect(page.locator('[data-testid="recent-scans-list"]')).toBeVisible();
    const scanItems = page.locator('[data-testid="scan-item"]');
    await expect(scanItems.first()).toBeVisible();
  });

  test('should navigate to scan details from history', async ({ page }) => {
    await page.click('[data-testid="scan-item"]:first-child');
    await expect(page).toHaveURL(/.*scan\/.+/);
  });
});

// ============================================================================
// PAYMENT TESTS
// ============================================================================

test.describe('Payments', () => {
  test.beforeEach(async ({ page }) => {
    await login(page);
  });

  test('should display pricing page', async ({ page }) => {
    await page.goto(`${BASE_URL}/pricing`);
    
    await expect(page.locator('[data-testid="pricing-golden-audit"]')).toBeVisible();
    await expect(page.locator('[data-testid="pricing-legacy-kit"]')).toBeVisible();
    await expect(page.locator('[data-testid="pricing-enterprise"]')).toBeVisible();
  });

  test('should initiate checkout for single scan', async ({ page }) => {
    await page.goto(`${BASE_URL}/pricing`);
    await page.click('[data-testid="buy-golden-audit"]');
    
    // Should redirect to Stripe checkout
    await page.waitForURL(/.*checkout\.stripe\.com.*/);
  });

  test('should display success page after payment', async ({ page }) => {
    // Simulate returning from Stripe with success
    await page.goto(`${BASE_URL}/success?session_id=test_session`);
    
    await expect(page.locator('[data-testid="payment-success"]')).toBeVisible();
    await expect(page.locator('text=Payment successful')).toBeVisible();
  });
});

// ============================================================================
// API INTEGRATION TESTS
// ============================================================================

test.describe('API Integration', () => {
  test('should return healthy status', async ({ request }) => {
    const response = await request.get(`${API_URL}/api/health`);
    expect(response.status()).toBe(200);
    
    const data = await response.json();
    expect(data.status).toBe('healthy');
  });

  test('should reject unauthenticated requests', async ({ request }) => {
    const response = await request.post(`${API_URL}/api/scan`, {
      data: {},
    });
    expect(response.status()).toBe(401);
  });

  test('should process scan with valid API key', async ({ request }) => {
    const response = await request.post(`${API_URL}/api/scan`, {
      headers: {
        'Authorization': `Bearer ${process.env.TEST_API_KEY}`,
      },
      multipart: {
        image: {
          name: 'test.jpg',
          mimeType: 'image/jpeg',
          buffer: Buffer.from('fake-image-data'),
        },
      },
    });
    
    // Either 200 (success) or 402 (needs payment)
    expect([200, 202, 402]).toContain(response.status());
  });
});

// ============================================================================
// GOLDEN REFERENCE TESTS
// ============================================================================

test.describe('Golden References', () => {
  test.beforeEach(async ({ page }) => {
    await login(page);
  });

  test('should display reference library', async ({ page }) => {
    await page.goto(`${BASE_URL}/references`);
    await expect(page.locator('[data-testid="reference-list"]')).toBeVisible();
  });

  test('should upload new reference', async ({ page }) => {
    await page.goto(`${BASE_URL}/references/upload`);
    
    const fileInput = page.locator('input[type="file"]');
    await fileInput.setInputFiles('tests/fixtures/reference-board.jpg');
    
    await page.fill('[data-testid="board-type-input"]', 'test-board');
    await page.fill('[data-testid="reference-name-input"]', 'Test Reference');
    
    await page.click('[data-testid="upload-reference-button"]');
    
    await expect(page.locator('text=Reference uploaded successfully')).toBeVisible();
  });
});

// ============================================================================
// BOARD LIBRARY TESTS
// ============================================================================

test.describe('Board Library', () => {
  test('should display board categories', async ({ page }) => {
    await page.goto(`${BASE_URL}/boards`);
    
    await expect(page.locator('[data-testid="board-categories"]')).toBeVisible();
    await expect(page.locator('text=iPhone')).toBeVisible();
    await expect(page.locator('text=MacBook')).toBeVisible();
  });

  test('should search boards', async ({ page }) => {
    await page.goto(`${BASE_URL}/boards`);
    
    await page.fill('[data-testid="board-search"]', 'iPhone 15');
    await page.press('[data-testid="board-search"]', 'Enter');
    
    await expect(page.locator('[data-testid="board-card"]').first()).toContainText('iPhone 15');
  });

  test('should display board details', async ({ page }) => {
    await page.goto(`${BASE_URL}/boards`);
    
    await page.click('[data-testid="board-card"]:first-child');
    
    await expect(page.locator('[data-testid="board-details-modal"]')).toBeVisible();
    await expect(page.locator('[data-testid="common-issues-list"]')).toBeVisible();
  });
});

// ============================================================================
// RESPONSIVE DESIGN TESTS
// ============================================================================

test.describe('Responsive Design', () => {
  test('should display mobile navigation', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 }); // iPhone SE
    await page.goto(BASE_URL);
    
    await expect(page.locator('[data-testid="mobile-menu-button"]')).toBeVisible();
    await page.click('[data-testid="mobile-menu-button"]');
    await expect(page.locator('[data-testid="mobile-nav"]')).toBeVisible();
  });

  test('should be usable on tablet', async ({ page }) => {
    await page.setViewportSize({ width: 768, height: 1024 }); // iPad
    await page.goto(BASE_URL);
    
    await expect(page.locator('[data-testid="hero-section"]')).toBeVisible();
  });
});

// ============================================================================
// ACCESSIBILITY TESTS
// ============================================================================

test.describe('Accessibility', () => {
  test('should have proper heading hierarchy', async ({ page }) => {
    await page.goto(BASE_URL);
    
    const h1 = await page.locator('h1').count();
    expect(h1).toBe(1);
  });

  test('should have accessible form labels', async ({ page }) => {
    await page.goto(`${BASE_URL}/login`);
    
    const emailInput = page.locator('[data-testid="email-input"]');
    await expect(emailInput).toHaveAttribute('aria-label');
  });

  test('should be keyboard navigable', async ({ page }) => {
    await page.goto(BASE_URL);
    
    // Tab through main navigation
    await page.keyboard.press('Tab');
    await page.keyboard.press('Tab');
    await page.keyboard.press('Enter');
    
    // Should navigate somewhere
    expect(page.url()).not.toBe(BASE_URL);
  });
});

// ============================================================================
// PERFORMANCE TESTS
// ============================================================================

test.describe('Performance', () => {
  test('should load landing page quickly', async ({ page }) => {
    const startTime = Date.now();
    await page.goto(BASE_URL);
    const loadTime = Date.now() - startTime;
    
    // Should load in under 3 seconds
    expect(loadTime).toBeLessThan(3000);
  });

  test('should have reasonable bundle size', async ({ page }) => {
    await page.goto(BASE_URL);
    
    const resourceTimings = await page.evaluate(() => {
      return performance.getEntriesByType('resource')
        .filter(r => r.name.includes('.js'))
        .reduce((acc, r) => acc + r.transferSize, 0);
    });
    
    // JS bundle should be under 500KB
    expect(resourceTimings).toBeLessThan(500 * 1024);
  });
});
