/**
 * GABRIEL PIPELINE — Cloudflare Local Event Re-Simulation
 * 
 * Mirrors Cloudflare pipeline events locally for testing and development.
 * Simulates the complete event flow: INGEST → NORMALIZE → AI → MC96 → REWARD
 * 
 * @example
 * const pipeline = new GabrielPipeline({
 *   ingest: 'https://ingestion-worker.workers.dev',
 *   normalizer: 'https://normalizer-worker.workers.dev',
 *   ai: 'https://ai-worker.workers.dev',
 *   mc96: 'https://mc96-main.workers.dev',
 *   reward: 'https://reward-engine.workers.dev'
 * });
 * 
 * await pipeline.runEvent({ platform: 'kofi', payload: {...} });
 */
export class GabrielPipeline {
  constructor(endpoints = {}) {
    this.endpoints = endpoints;
    this.history = [];
    this.options = {
      timeout: 30000, // 30 second timeout per stage
      retries: 2,
      continueOnError: false
    };
  }

  /**
   * Run event through complete pipeline
   * @param {Object} event - Event to process
   * @param {Object} options - Pipeline options
   * @returns {Promise<Object>} Pipeline result
   */
  async runEvent(event, options = {}) {
    const opts = { ...this.options, ...options };
    const pipelineId = `pipe-${Date.now()}-${Math.random().toString(36).slice(2)}`;
    const startTime = Date.now();

    const result = {
      id: pipelineId,
      event,
      stages: {},
      success: false,
      error: null,
      duration: 0
    };

    try {
      // Stage 1: INGEST
      if (this.endpoints.ingest) {
        result.stages.ingest = await this._callStage(
          'ingest',
          this.endpoints.ingest,
          event,
          opts
        );

        if (!opts.continueOnError && result.stages.ingest.error) {
          throw new Error(`Ingest failed: ${result.stages.ingest.error}`);
        }
      }

      // Stage 2: NORMALIZE
      if (this.endpoints.normalizer) {
        const normalizedEvent = result.stages.ingest?.data || event;
        result.stages.normalizer = await this._callStage(
          'normalizer',
          this.endpoints.normalizer,
          normalizedEvent,
          opts
        );

        if (!opts.continueOnError && result.stages.normalizer.error) {
          throw new Error(`Normalizer failed: ${result.stages.normalizer.error}`);
        }
      }

      // Stage 3: AI ANALYSIS
      if (this.endpoints.ai) {
        const normalizedEvent = result.stages.normalizer?.data || event;
        result.stages.ai = await this._callStage(
          'ai',
          this.endpoints.ai,
          normalizedEvent,
          opts
        );

        if (!opts.continueOnError && result.stages.ai.error) {
          throw new Error(`AI analysis failed: ${result.stages.ai.error}`);
        }
      }

      // Stage 4: MC96 MAIN
      if (this.endpoints.mc96) {
        const enrichedEvent = result.stages.ai?.data || event;
        result.stages.mc96 = await this._callStage(
          'mc96',
          this.endpoints.mc96,
          enrichedEvent,
          opts
        );

        if (!opts.continueOnError && result.stages.mc96.error) {
          throw new Error(`MC96 processing failed: ${result.stages.mc96.error}`);
        }
      }

      // Stage 5: REWARD ENGINE
      if (this.endpoints.reward) {
        const processedEvent = result.stages.mc96?.data || event;
        result.stages.reward = await this._callStage(
          'reward',
          this.endpoints.reward,
          processedEvent,
          opts
        );

        if (!opts.continueOnError && result.stages.reward.error) {
          throw new Error(`Reward engine failed: ${result.stages.reward.error}`);
        }
      }

      result.success = true;
      result.duration = Date.now() - startTime;

      // Store in history
      this.history.push(result);
      if (this.history.length > 1000) {
        this.history.shift(); // Keep last 1000 events
      }

      return result;
    } catch (error) {
      result.error = error.message;
      result.duration = Date.now() - startTime;
      result.stages._error = {
        stage: 'pipeline',
        error: error.message,
        timestamp: Date.now()
      };

      this.history.push(result);
      throw error;
    }
  }

  /**
   * Run event through single stage
   * @param {string} stage - Stage name
   * @param {string} endpoint - Endpoint URL
   * @param {Object} data - Data to send
   * @param {Object} options - Options
   * @returns {Promise<Object>} Stage result
   */
  async _callStage(stage, endpoint, data, options) {
    const stageStart = Date.now();
    
    let lastError = null;
    
    for (let attempt = 0; attempt <= options.retries; attempt++) {
      try {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), options.timeout);

        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data),
          signal: controller.signal
        });

        clearTimeout(timeout);

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const result = await response.json();
        const duration = Date.now() - stageStart;

        return {
          stage,
          endpoint,
          success: true,
          status: response.status,
          data: result,
          duration,
          attempt: attempt + 1
        };
      } catch (error) {
        lastError = error;
        
        if (attempt < options.retries) {
          // Exponential backoff
          await this._delay(1000 * Math.pow(2, attempt));
        }
      }
    }

    const duration = Date.now() - stageStart;
    
    return {
      stage,
      endpoint,
      success: false,
      error: lastError?.message || 'Unknown error',
      duration,
      attempts: options.retries + 1
    };
  }

  /**
   * Run event through specific stage only
   * @param {string} stage - Stage name
   * @param {Object} event - Event data
   * @returns {Promise<Object>} Stage result
   */
  async runStage(stage, event) {
    const endpoint = this.endpoints[stage];
    
    if (!endpoint) {
      throw new Error(`Stage endpoint not configured: ${stage}`);
    }

    return await this._callStage(stage, endpoint, event, this.options);
  }

  /**
   * Get pipeline history
   * @param {number} limit - Number of recent events to return
   * @returns {Array} Recent pipeline runs
   */
  getHistory(limit = 100) {
    return this.history.slice(-limit);
  }

  /**
   * Get pipeline statistics
   * @returns {Object} Statistics
   */
  getStats() {
    const successful = this.history.filter(r => r.success).length;
    const failed = this.history.filter(r => !r.success).length;
    const avgDuration = this.history.length > 0
      ? this.history.reduce((sum, r) => sum + r.duration, 0) / this.history.length
      : 0;

    return {
      total: this.history.length,
      successful,
      failed,
      successRate: this.history.length > 0 ? successful / this.history.length : 0,
      avgDuration
    };
  }

  /**
   * Clear pipeline history
   */
  clearHistory() {
    this.history = [];
  }

  _delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

// Default export
export default GabrielPipeline;

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielPipeline;
  module.exports.default = GabrielPipeline;
}

