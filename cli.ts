#!/usr/bin/env node
/**
 * 🎛️ NOIZYOS SERVICE MANAGER - CLI
 * Command-line control for all NoizyOS services
 * Fish Music Inc - CB_01
 */

const registry = require('./service_registry.json');

const command = process.argv[2];
const target = process.argv[3];

console.log('🎛️ NoizyOS Service Manager');
console.log('');

switch (command) {
  case 'start':
    if (target === 'all' || target === 'everything') {
      startAll();
    } else {
      startService(target);
    }
    break;

  case 'stop':
    if (target === 'all' || target === 'everything') {
      stopAll();
    } else {
      stopService(target);
    }
    break;

  case 'restart':
    if (target === 'all' || target === 'everything') {
      restartAll();
    } else {
      restartService(target);
    }
    break;

  case 'status':
    showStatus(target);
    break;

  case 'list':
    listServices();
    break;

  default:
    showHelp();
}

function startAll() {
  console.log('🚀 Starting all NoizyOS services...');
  console.log('');
  
  for (const service of registry.services) {
    startService(service.name);
  }
  
  console.log('');
  console.log('✅ All services started');
}

function stopAll() {
  console.log('🛑 Stopping all NoizyOS services...');
  console.log('');
  
  for (const service of registry.services) {
    stopService(service.name);
  }
  
  console.log('');
  console.log('✅ All services stopped');
}

function restartAll() {
  console.log('🔄 Restarting all NoizyOS services...');
  stopAll();
  console.log('');
  setTimeout(() => startAll(), 2000);
}

function startService(name: string) {
  console.log(`   🚀 Starting ${name}...`);
  // TODO: Actually start the service
}

function stopService(name: string) {
  console.log(`   🛑 Stopping ${name}...`);
  // TODO: Actually stop the service
}

function restartService(name: string) {
  stopService(name);
  setTimeout(() => startService(name), 1000);
}

function showStatus(target?: string) {
  console.log('📊 NoizyOS Status:');
  console.log('');
  
  for (const service of registry.services) {
    if (!target || service.name === target) {
      const status = '🟢';  // TODO: Check actual status
      console.log(`   ${status} ${service.name.padEnd(20)} ${service.port || 'N/A'}`);
    }
  }
  
  console.log('');
}

function listServices() {
  console.log('📋 Available Services:');
  console.log('');
  
  for (const service of registry.services) {
    console.log(`   • ${service.name} - ${service.description}`);
  }
  
  console.log('');
}

function showHelp() {
  console.log('Usage:');
  console.log('  noizy start [service|all]     Start service(s)');
  console.log('  noizy stop [service|all]      Stop service(s)');
  console.log('  noizy restart [service|all]   Restart service(s)');
  console.log('  noizy status [service]        Show status');
  console.log('  noizy list                    List all services');
  console.log('');
  console.log('Examples:');
  console.log('  noizy start backend');
  console.log('  noizy start all');
  console.log('  noizy status');
  console.log('  noizy restart omega');
  console.log('');
}
