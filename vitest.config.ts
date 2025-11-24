import { defineWorkersConfig } from '@cloudflare/vitest-pool-workers/config';

export default defineWorkersConfig({
  test: {
    globals: true,
    include: ['tests/**/*.test.ts'],
    exclude: ['node_modules', 'dist'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html', 'lcov'],
      reportsDirectory: './coverage',
      include: ['src/**/*.ts'],
      exclude: [
        'src/**/*.d.ts',
        'src/**/*.test.ts',
        'src/index.ts',
      ],
      thresholds: {
        global: {
          branches: 80,
          functions: 80,
          lines: 80,
          statements: 80,
        },
      },
    },
    poolOptions: {
      workers: {
        wrangler: { configPath: './wrangler.toml' },
        miniflare: {
          kvNamespaces: ['EMAIL_KV'],
          d1Databases: ['EMAIL_DB'],
          queueProducers: { EMAIL_QUEUE: 'email-queue' },
          queueConsumers: { 'email-queue': {} },
        },
      },
    },
    reporters: ['verbose', 'html'],
    outputFile: {
      html: './test-results/index.html',
    },
    testTimeout: 30000,
    hookTimeout: 30000,
  },
});
