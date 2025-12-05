/**
 * ⚙️ PIPELINE ORCHESTRATOR
 * Coordinates genius execution pipeline
 * Fish Music Inc - CB_01
 */

import { GeniusContext } from '../../geniuses/base/GeniusBase';
import { routeToGeniuses } from '../router/genius_router';

// Import all geniuses
import { PricingGenius } from '../../geniuses/business/PricingGenius';
import { HardwareGenius } from '../../geniuses/diagnosis/HardwareGenius';
import { MacRepairGenius } from '../../geniuses/diagnosis/MacRepairGenius';
import { MalwareGenius } from '../../geniuses/diagnosis/MalwareGenius';
import { WindowsRepairGenius } from '../../geniuses/diagnosis/WindowsRepairGenius';
import { CalmGenius } from '../../geniuses/experience/CalmGenius';
import { SupportGenius } from '../../geniuses/experience/SupportGenius';
import { AutomationGenius } from '../../geniuses/intelligence/AutomationGenius';
import { CrossSystemGenius } from '../../geniuses/intelligence/CrossSystemGenius';
import { ForesightGenius } from '../../geniuses/intelligence/ForesightGenius';
import { OmegaCoreGenius } from '../../geniuses/intelligence/OmegaCoreGenius';
import { PatternGenius } from '../../geniuses/intelligence/PatternGenius';
import { NetworkGenius } from '../../geniuses/optimization/NetworkGenius';
import { PerformanceGenius } from '../../geniuses/optimization/PerformanceGenius';
import { StorageGenius } from '../../geniuses/optimization/StorageGenius';
import { ThermalGenius } from '../../geniuses/optimization/ThermalGenius';

// Genius registry
const GENIUSES: Record<string, any> = {
  'MacRepairGenius': new MacRepairGenius(),
  'WindowsRepairGenius': new WindowsRepairGenius(),
  'HardwareGenius': new HardwareGenius(),
  'MalwareGenius': new MalwareGenius(),
  'PerformanceGenius': new PerformanceGenius(),
  'NetworkGenius': new NetworkGenius(),
  'StorageGenius': new StorageGenius(),
  'ThermalGenius': new ThermalGenius(),
  'CalmGenius': new CalmGenius(),
  'SupportGenius': new SupportGenius(),
  'PricingGenius': new PricingGenius(),
  'ForesightGenius': new ForesightGenius(),
  'PatternGenius': new PatternGenius(),
  'AutomationGenius': new AutomationGenius(),
  'CrossSystemGenius': new CrossSystemGenius(),
  'OmegaCoreGenius': new OmegaCoreGenius(),
};

export async function orchestratePipeline(payload: any) {
  const context: GeniusContext = payload.context;
  const targets = routeToGeniuses(payload);

  console.log('⚙️ Orchestrating pipeline...');
  console.log(`   Calling ${targets.length} geniuses:`, targets);

  const results = [];

  // Call each genius in sequence
  for (const geniusName of targets) {
    const genius = GENIUSES[geniusName];
    
    if (genius) {
      console.log(`   🧠 Calling ${geniusName}...`);
      const result = genius.analyze(context);
      results.push(result);
    } else {
      console.warn(`   ⚠️  Genius not found: ${geniusName}`);
    }
  }

  console.log('✅ Pipeline complete');

  return {
    summary: "Pipeline executed successfully",
    geniuses_called: targets,
    results,
    timestamp: new Date().toISOString()
  };
}
