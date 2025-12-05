/**
 * 📡 EVENT BUS
 * Central nervous system for all NoizyOS events
 * Fish Music Inc - CB_01
 */

type EventHandler = (data: any) => void;

class EventBus {
  private listeners: Map<string, EventHandler[]> = new Map();
  private history: Array<{ event: string; data: any; timestamp: string }> = [];

  init() {
    console.log('📡 Event bus initialized');
  }

  on(event: string, handler: EventHandler) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    
    this.listeners.get(event)!.push(handler);
    console.log(`   📡 Listener registered: ${event}`);
  }

  emit(event: string, data: any) {
    // Log event
    this.history.push({
      event,
      data,
      timestamp: new Date().toISOString()
    });

    // Call listeners
    const handlers = this.listeners.get(event) || [];
    handlers.forEach(handler => {
      try {
        handler(data);
      } catch (err) {
        console.error(`❌ Event handler error for ${event}:`, err);
      }
    });

    console.log(`📢 Event emitted: ${event}`);
  }

  off(event: string, handler?: EventHandler) {
    if (!handler) {
      this.listeners.delete(event);
      return;
    }

    const handlers = this.listeners.get(event) || [];
    const filtered = handlers.filter(h => h !== handler);
    this.listeners.set(event, filtered);
  }

  getHistory(limit: number = 100) {
    return this.history.slice(-limit);
  }

  clearHistory() {
    this.history = [];
  }
}

export const NoizyBus = new EventBus();
