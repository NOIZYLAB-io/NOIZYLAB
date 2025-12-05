/**
 * 🧠 GENIUS BASE CLASS
 * Fish Music Inc - CB_01
 * All 25 NoizyGeniuses inherit from this
 */

export interface GeniusContext {
  device: any;
  logs?: any;
  metrics?: any;
  session_id?: string;
  user_id?: string;
}

export interface GeniusResponse {
  genius: string;
  findings: string[];
  recommendations: string[];
  confidence?: number;
  timestamp?: string;
}

export abstract class GeniusBase {
  abstract name: string;
  abstract squad: string;

  abstract analyze(context: GeniusContext): GeniusResponse;

  protected resp(findings: string[], recommendations: string[], confidence: number = 0.95): GeniusResponse {
    return {
      genius: this.name,
      findings,
      recommendations,
      confidence,
      timestamp: new Date().toISOString()
    };
  }
}
