/**
 * ⚡ NOIZYOS KERNEL
 * The heart, the electrical system, the core event bus
 * Fish Music Inc - CB_01
 * 🔥 GORUNFREE! 🎸🔥
 */

import { NoizyBus } from './event_bus';
import { hypervisor } from './hypervisor';

export class NoizyKernel {
  private static instance: NoizyKernel;
  private booted = false;
  private drivers: Map<string, any> = new Map();

  private constructor() {}

  static getInstance(): NoizyKernel {
    if (!NoizyKernel.instance) {
      NoizyKernel.instance = new NoizyKernel();
    }
    return NoizyKernel.instance;
  }

  async boot() {
    if (this.booted) {
      console.log('⚠️  Kernel already booted');
      return;
    }

    console.log('');
    console.log('╔═══════════════════════════════════════════════════════════════╗');
    console.log('║                                                               ║');
    console.log('║              ⚡ NOIZYOS KERNEL BOOTING ⚡                      ║');
    console.log('║                                                               ║');
    console.log('╚═══════════════════════════════════════════════════════════════╝');
    console.log('');

    // Initialize event bus
    console.log('[1/5] Initializing event bus...');
    NoizyBus.init();
    console.log('      ✅ Event bus online');

    // Load drivers
    console.log('[2/5] Loading kernel drivers...');
    await this.loadDrivers();
    console.log('      ✅ Drivers loaded');

    // Initialize hypervisor
    console.log('[3/5] Starting hypervisor...');
    hypervisor.init();
    console.log('      ✅ Hypervisor active');

    // Setup inter-process communication
    console.log('[4/5] Establishing IPC...');
    this.setupIPC();
    console.log('      ✅ IPC ready');

    // Kernel ready
    console.log('[5/5] Kernel initialization complete');
    
    this.booted = true;

    console.log('');
    console.log('✅ NOIZYOS KERNEL ONLINE');
    console.log('');

    // Emit boot event
    NoizyBus.emit('kernel:booted', {
      timestamp: new Date().toISOString(),
      version: '1.0.0'
    });
  }

  private async loadDrivers() {
    const driverList = [
      'voice_driver',
      'remote_driver',
      'mesh_driver',
      'update_driver',
      'vr_driver'
    ];

    for (const driver of driverList) {
      try {
        const module = await import(`./drivers/${driver}`);
        this.drivers.set(driver, module);
        console.log(`      ✅ ${driver}`);
      } catch (err) {
        console.log(`      ⚠️  ${driver} not available`);
      }
    }
  }

  private setupIPC() {
    // Inter-Process Communication setup
    NoizyBus.on('omega:complete', (data) => {
      console.log('🌌 Omega pipeline completed:', data.session_id);
    });

    NoizyBus.on('genius:called', (data) => {
      console.log(`🧠 Genius called: ${data.genius}`);
    });

    NoizyBus.on('autopilot:triggered', (data) => {
      console.log('🤖 Autopilot triggered:', data.reason);
    });
  }

  getDriver(name: string) {
    return this.drivers.get(name);
  }

  async shutdown() {
    console.log('⚡ Shutting down kernel...');
    
    // Emit shutdown event
    NoizyBus.emit('kernel:shutdown', {
      timestamp: new Date().toISOString()
    });

    this.booted = false;
    console.log('✅ Kernel stopped');
  }
}

export const kernel = NoizyKernel.getInstance();
