import { http } from "./http.js";

type DoctorResult = { name: string; ok: boolean; detail?: any };

export async function doctor(deep: boolean): Promise<DoctorResult[]> {
  const results: DoctorResult[] = [];

  // Public root ping
  try {
    const r = await fetch(process.env.NOIZYLAB_BASE_URL!);
    results.push({ name: "public:root", ok: r.ok, detail: `${r.status} ${r.statusText}` });
  } catch (e: any) {
    results.push({ name: "public:root", ok: false, detail: String(e?.message ?? e) });
  }

  // Staff health (Access token headers must be present in env)
  try {
    const out = await http({ path: "/staff/health" });
    results.push({ name: "staff:health", ok: !!out?.ok, detail: out });
  } catch (e: any) {
    results.push({ name: "staff:health", ok: false, detail: String(e?.message ?? e) });
  }

  if (!deep) return results;

  // Deep checks (non-destructive)
  try {
    const list = await http({ path: "/staff/tickets?status=TRIAGE" });
    results.push({ name: "staff:list", ok: true, detail: { count: (list?.tickets?.length ?? 0) } });
  } catch (e: any) {
    results.push({ name: "staff:list", ok: false, detail: String(e?.message ?? e) });
  }

  return results;
}
