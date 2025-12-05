/**
 * 👽 Agent Summoner
 * 
 * Agents now act like full cloud processes.
 * Cursor will extend these files automatically.
 */

import { Lucy } from "./lucy.js";
import { Keith } from "./keith.js";
import { Wardy } from "./wardy.js";

export async function summonAgent(agent, data, env) {
  switch (agent) {
    case "LUCY":
      return Lucy(data, env);
    
    case "KEITH":
      return Keith(data, env);
    
    case "WARDY":
      return Wardy(data, env);
    
    case "RED":
      return Lucy(data, env); // emergency routing
    
    default:
      console.log(`Unknown agent: ${agent}, ignoring.`);
      return null;
  }
}

