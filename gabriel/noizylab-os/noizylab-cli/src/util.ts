// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB CLI - Utilities
// ═══════════════════════════════════════════════════════════════════════════

export function must<T>(v: T | undefined | null, msg: string): T {
  if (v === undefined || v === null || (typeof v === "string" && v.trim() === "")) {
    throw new Error(msg);
  }
  return v;
}

export function toInt(v: any, fallback?: number): number {
  const n = Number(v);
  if (Number.isFinite(n)) return n;
  if (fallback !== undefined) return fallback;
  throw new Error(`Expected number, got: ${v}`);
}

export function toUpperCode(v: string) {
  return v.trim().toUpperCase();
}

export function log(msg: string) {
  console.log(msg);
}

export function info(msg: string) {
  console.log('ℹ', msg);
}

export function success(msg: string) {
  console.log('✓', msg);
}

export function warn(msg: string) {
  console.log('⚠', msg);
}

export function error(msg: string) {
  console.log('✗', msg);
}

export function header(title: string) {
  console.log();
  console.log(`═══ ${title} ═══`);
  console.log();
}

export function table(rows: Record<string, any>[]) {
  if (!rows.length) return log('(empty)');
  console.table(rows);
}

export function json(data: any) {
  console.log(JSON.stringify(data, null, 2));
}

export function nowISO() {
  return new Date().toISOString();
}

export function shortId(id: string) {
  return id.slice(0, 8);
}

export function formatDate(iso: string) {
  return new Date(iso).toLocaleString();
}

export function sleep(ms: number) {
  return new Promise(r => setTimeout(r, ms));
}

// 3-line comms format
export function threeLineComm(what: string, next: string, updateTime: string) {
  console.log();
  console.log('WHAT:', what);
  console.log('NEXT:', next);
  console.log('UPDATE:', updateTime);
  console.log();
}
