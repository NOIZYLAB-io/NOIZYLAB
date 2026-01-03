import { Command } from "commander";
import dotenv from "dotenv";
dotenv.config();

import fs from "node:fs";
import path from "node:path";

import { http } from "./http.js";
import { wsListen, wsSend } from "./ws.js";
import { must, toInt, toUpperCode } from "./util.js";
import { doctor } from "./doctor.js";
import { PLAYBOOKS_SEED } from "./seed.js";
import { tailEvents } from "./sse.js";

const program = new Command();

program
  .name("nl")
  .description("NoizyLab OS CLI")
  .version("1.0.0");

//
// PUBLIC: Tickets
//
program
  .command("ticket:create")
  .description("Create a public ticket (Turnstile required)")
  .requiredOption("--subject <subject>")
  .option("--channel <channel>", "portal")
  .option("--turnstile <token>", process.env.TURNSTILE_TOKEN)
  .action(async (opt) => {
    const turnstileToken = must(opt.turnstile, "Missing --turnstile (or TURNSTILE_TOKEN env)");
    const out = await http({
      method: "POST",
      path: "/public/tickets",
      json: { subject: opt.subject, channel: opt.channel, turnstileToken }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("ticket:status")
  .description("Get ticket status + events (requires ticket secret)")
  .argument("<ticketPublicId>")
  .requiredOption("--secret <secret>")
  .action(async (ticketPublicId, opt) => {
    const out = await http({
      path: `/public/status/${ticketPublicId}?secret=${encodeURIComponent(opt.secret)}`
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// PUBLIC: Consent
//
program
  .command("consent:request")
  .description("Request consent for a scope (live_help|remote_control|uploads|recording)")
  .requiredOption("--ticket <ticketPublicId>")
  .requiredOption("--secret <secret>")
  .option("--scope <scope>", "live_help")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/public/consent/request",
      json: { ticketPublicId: opt.ticket, secret: opt.secret, scope: opt.scope }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("consent:grant")
  .description("Grant consent by consentId")
  .argument("<consentId>")
  .action(async (consentId) => {
    const out = await http({
      method: "POST",
      path: "/public/consent/grant",
      json: { consentId: toInt(consentId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("consent:revoke")
  .description("Revoke consent by consentId")
  .argument("<consentId>")
  .action(async (consentId) => {
    const out = await http({
      method: "POST",
      path: "/public/consent/revoke",
      json: { consentId: toInt(consentId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// PUBLIC: RealtimeKit join
//
program
  .command("rtk:join")
  .description("Join a RealtimeKit meeting by code (public)")
  .requiredOption("--code <code>")
  .option("--name <name>", "Client")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/public/rtk/join",
      json: { code: toUpperCode(opt.code), name: opt.name }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// STAFF: Tickets + status
//
program
  .command("staff:list")
  .description("List tickets by status (staff)")
  .option("--status <status>", "TRIAGE")
  .action(async (opt) => {
    const out = await http({
      path: `/staff/tickets?status=${encodeURIComponent(opt.status)}`
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("staff:status")
  .description("Set ticket status (staff)")
  .argument("<ticketId>")
  .requiredOption("--set <status>")
  .action(async (ticketId, opt) => {
    const out = await http({
      method: "PATCH",
      path: `/staff/tickets/${toInt(ticketId)}/status`,
      json: { status: opt.set }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// STAFF: RealtimeKit start
//
program
  .command("staff:rtk:start")
  .description("Start RealtimeKit meeting + staff token + join code (staff)")
  .option("--ticketId <id>")
  .option("--title <title>", "NoizyLab Live Help")
  .option("--staffName <name>", "NoizyLab Staff")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/rtk/start",
      json: {
        ticketId: opt.ticketId ? toInt(opt.ticketId) : undefined,
        title: opt.title,
        staffName: opt.staffName
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// STAFF: AI
//
program
  .command("staff:ai:triage")
  .description("AI triage (persona/tags/question/playbook) (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--text <text>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/ai/triage",
      json: { ticketId: toInt(opt.ticketId), text: opt.text }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("staff:ai:question")
  .description("AI next-best question (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--context <text>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/ai/next-question",
      json: { ticketId: toInt(opt.ticketId), context: opt.context }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("staff:ai:notes")
  .description("AI live notes (max 5 bullets) (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--transcript <text>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/ai/live-notes",
      json: { ticketId: toInt(opt.ticketId), transcript: opt.transcript }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// STAFF: Retention
//
program
  .command("staff:retention")
  .description("Set ticket retention (days) (staff)")
  .requiredOption("--ticketId <id>")
  .option("--days <n>", "90")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/retention/set",
      json: { ticketId: toInt(opt.ticketId), keepDays: toInt(opt.days) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("staff:note")
  .description("Add note to ticket (tracks first response for SLA)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--note <text>")
  .option("--public", "Make note visible to client")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/tickets/${opt.ticketId}/note`,
      json: { note: opt.note, isPublic: !!opt.public }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("estimate:send")
  .description("Create+send estimate and print approve/decline links (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--amountCents <n>")
  .requiredOption("--summary <text>")
  .option("--terms <text>", "")
  .option("--currency <cur>", "CAD")
  .option("--expiresMinutes <n>", "4320") // 72h
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/estimate/send",
      json: {
        ticketId: toInt(opt.ticketId),
        amount_cents: toInt(opt.amountCents),
        currency: opt.currency,
        summary: opt.summary,
        terms: opt.terms,
        expiresMinutes: toInt(opt.expiresMinutes)
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("status:send")
  .description("Send a 3-line status update NOW/NEXT/WHEN (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--now <text>")
  .requiredOption("--next <text>")
  .requiredOption("--when <text>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/status/send",
      json: {
        ticketId: toInt(opt.ticketId),
        now: opt.now,
        next: opt.next,
        when: opt.when
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("followups:run")
  .description("Run due followups (staff)")
  .option("--limit <n>", "50")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/followups/run",
      json: { limit: toInt(opt.limit) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("timeline:tail")
  .description("Live tail ticket events (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    await tailEvents(toInt(opt.ticketId));
  });

program
  .command("invoice:close")
  .description("Create invoice for ticket with line items (staff)")
  .requiredOption("--ticketId <id>")
  .option("--currency <cur>", "CAD")
  .option("--taxRate <n>", "0.13")
  .requiredOption("--item <label=...,qty=...,amountCents=...>", "Repeatable", (v, p: string[]) => (p.push(v), p), [])
  .action(async (opt) => {
    const items = (opt.item as string[]).map(s => {
      const m = Object.fromEntries(s.split(",").map(kv => kv.split("=").map(x => x.trim())));
      return {
        label: m["label"],
        qty: Number(m["qty"] ?? 1),
        amount_cents: Number(m["amountCents"] ?? 0)
      };
    });
    const out = await http({
      method: "POST",
      path: "/staff/invoice/close",
      json: { ticketId: toInt(opt.ticketId), currency: opt.currency, taxRate: Number(opt.taxRate), items }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("metrics:top")
  .description("Top event hotspots (staff)")
  .option("--days <n>", "30")
  .action(async (opt) => {
    const out = await http({ path: `/staff/metrics/top?days=${encodeURIComponent(opt.days)}` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("client:profile:set")
  .description("Set operational client traits (staff)")
  .requiredOption("--clientId <id>")
  .option("--comms <mode>", "calm")
  .option("--trait <TRAIT>", "Repeatable", (v, p: string[]) => (p.push(v), p), [])
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/client/profile/set",
      json: { clientId: toInt(opt.clientId), commsMode: opt.comms, traits: opt.trait }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("client:profile:get")
  .description("Get client profile (staff)")
  .requiredOption("--clientId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/client/profile/get?clientId=${encodeURIComponent(opt.clientId)}` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("device:register")
  .description("Register device fingerprint (staff)")
  .requiredOption("--label <text>")
  .requiredOption("--os <mac|win>")
  .requiredOption("--fingerprintInput <stableFields>")
  .option("--clientId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/device/register",
      json: {
        clientId: opt.clientId ? toInt(opt.clientId) : undefined,
        label: opt.label,
        os: opt.os,
        fingerprintInput: opt.fingerprintInput
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("export:case")
  .description("Export full case bundle (staff) and save to file")
  .requiredOption("--ticketId <id>")
  .option("--out <dir>", "./exports")
  .action(async (opt) => {
    const ticketId = toInt(opt.ticketId);
    const out = await http({ path: `/staff/export/case?ticketId=${encodeURIComponent(String(ticketId))}` });

    const dir = opt.out;
    fs.mkdirSync(dir, { recursive: true });

    const filename = `case_ticket_${ticketId}_${new Date().toISOString().replace(/[:.]/g, "-")}.json`;
    const fp = path.join(dir, filename);
    fs.writeFileSync(fp, JSON.stringify(out.bundle, null, 2), "utf8");

    console.log(JSON.stringify({ ok: true, file: fp }, null, 2));
  });

program
  .command("prevention:plan")
  .description("Create prevention plan + schedule D7/D30 followups (staff)")
  .requiredOption("--ticketId <id>")
  .option("--os <os>", "both")
  .option("--tag <TAG>", "Repeatable", (v, p: string[]) => (p.push(v), p), [])
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/prevention/plan",
      json: { ticketId: toInt(opt.ticketId), os: opt.os, tags: opt.tag }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("ops:cron")
  .description("Run retention purges + followups + daily metrics rollup (staff)")
  .option("--limit <n>", "100")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/ops/cron",
      json: { limit: toInt(opt.limit) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("ops:enqueue")
  .description("Enqueue ops jobs (staff)")
  .requiredOption("--type <retention_purge|followups_run|metrics_rollup>")
  .option("--limit <n>", "200")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/ops/enqueue",
      json: { type: opt.type, limit: toInt(opt.limit) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("ops:run")
  .description("Run a single ops job immediately (staff)")
  .requiredOption("--type <retention_purge|followups_run|metrics_rollup>")
  .option("--limit <n>", "200")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/ops/run",
      json: { type: opt.type, limit: toInt(opt.limit) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("dlq:list")
  .description("List DLQ quarantined jobs (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/dlq/list" });
    console.log(JSON.stringify(out, null, 2));
  });

//
// GENIUS UPGRADES
//

// Control lanes (session guardrails)
program
  .command("control:grant")
  .description("Grant remote control lane with 30m auto-revoke (staff)")
  .requiredOption("--ticketId <id>")
  .option("--minutes <n>", "30")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/control/grant",
      json: { ticketId: toInt(opt.ticketId), minutes: toInt(opt.minutes) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("control:revoke")
  .description("Revoke control lane (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/control/revoke",
      json: { ticketId: toInt(opt.ticketId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("control:expire")
  .description("Expire stale control lanes (staff)")
  .action(async () => {
    const out = await http({ method: "POST", path: "/staff/control/expire", json: {} });
    console.log(JSON.stringify(out, null, 2));
  });

// Tag discipline
program
  .command("tags:validate")
  .description("Validate tags against controlled enum (staff)")
  .requiredOption("--tag <TAG>", "Repeatable", (v, p: string[]) => (p.push(v), p), [])
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/tags/validate",
      json: { tags: opt.tag }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("tags:enum")
  .description("List allowed tag enum (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/tags/enum" });
    console.log(JSON.stringify(out, null, 2));
  });

// Playbook compiler
program
  .command("playbooks:compile")
  .description("Compile playbook to client + tech versions (staff)")
  .requiredOption("--code <PBx>")
  .option("--os <os>", "both")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/playbooks/compile",
      json: { code: toUpperCode(opt.code), os: opt.os }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Anti-repeat D3 nudge
program
  .command("followups:d3")
  .description("Schedule D3 micro-check-in (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/followups/d3",
      json: { ticketId: toInt(opt.ticketId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Triage autopilot
program
  .command("ai:autopilot")
  .description("Auto-suggest playbook based on tags (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/ai/autopilot",
      json: { ticketId: toInt(opt.ticketId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Fix receipts
program
  .command("receipt:get")
  .description("Get fix receipt for ticket (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/receipt/get?ticketId=${encodeURIComponent(opt.ticketId)}` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("receipt:generate")
  .description("Generate fix receipt manually (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--invoiceId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/receipt/generate",
      json: { ticketId: toInt(opt.ticketId), invoiceId: toInt(opt.invoiceId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// R2 Snapshot Exports
program
  .command("export:snapshot")
  .description("Create R2 snapshot + signed download URL (staff)")
  .requiredOption("--ticketId <id>")
  .option("--redact", "Redact PII from export", false)
  .option("--expiresMinutes <n>", "60")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/export/snapshot",
      json: {
        ticketId: toInt(opt.ticketId),
        redact: opt.redact,
        expiresMinutes: toInt(opt.expiresMinutes)
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Auto-close guard
program
  .command("autoclose:schedule")
  .description("Schedule auto-close for ticket (staff)")
  .requiredOption("--ticketId <id>")
  .option("--warnDays <n>", "5")
  .option("--closeDays <n>", "7")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/autoclose/schedule",
      json: {
        ticketId: toInt(opt.ticketId),
        warnDays: toInt(opt.warnDays),
        closeDays: toInt(opt.closeDays)
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("autoclose:cancel")
  .description("Cancel auto-close for ticket (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/autoclose/cancel",
      json: { ticketId: toInt(opt.ticketId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("autoclose:run")
  .description("Run auto-close processor (staff)")
  .option("--limit <n>", "50")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/autoclose/run",
      json: { limit: toInt(opt.limit) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// EXPORTS
//
program
  .command("export:snapshot")
  .description("Create R2 export snapshot with signed URL (staff)")
  .requiredOption("--ticketId <id>")
  .option("--redact", "Redact PII")
  .option("--expiresMinutes <n>", "60")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/export/snapshot",
      json: {
        ticketId: toInt(opt.ticketId),
        redacted: !!opt.redact,
        expiresMinutes: toInt(opt.expiresMinutes)
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("export:case")
  .description("Get case bundle JSON inline (staff)")
  .requiredOption("--ticketId <id>")
  .option("--redact", "Redact PII")
  .action(async (opt) => {
    const redact = opt.redact ? "1" : "0";
    const out = await http({
      path: `/staff/tickets/${opt.ticketId}/bundle?redact=${redact}`
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// WS: Chat
//
program
  .command("ws:listen")
  .description("Listen to a room websocket (prints messages)")
  .requiredOption("--url <wsUrl>")
  .action(async (opt) => {
    await wsListen(opt.url);
  });

program
  .command("ws:send")
  .description("Send a chat message over websocket")
  .requiredOption("--url <wsUrl>")
  .option("--who <who>", "staff")
  .requiredOption("--text <text>")
  .action(async (opt) => {
    await wsSend(opt.url, { who: opt.who, text: opt.text });
    console.log("sent");
  });

//
// PLAYBOOKS / ESTIMATES / PAYMENTS / CONTROL
// (Commands assume you implemented the routes previously; these are ready now.)
//
program
  .command("staff:playbook")
  .description("Apply a playbook run (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--code <playbookCode>")
  .option("--os <os>", "both")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/playbooks/apply",
      json: { ticketId: toInt(opt.ticketId), playbookCode: opt.code, os: opt.os }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("staff:estimate:create")
  .description("Create an estimate (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--amountCents <n>")
  .option("--currency <cur>", "CAD")
  .requiredOption("--summary <text>")
  .option("--terms <text>", "")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/estimate/create",
      json: {
        ticketId: toInt(opt.ticketId),
        amount_cents: toInt(opt.amountCents),
        currency: opt.currency,
        summary: opt.summary,
        terms: opt.terms
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("estimate:approve")
  .description("Public approve estimate (ticketPublicId + secret)")
  .requiredOption("--ticket <publicId>")
  .requiredOption("--secret <secret>")
  .requiredOption("--estimateId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/public/estimate/approve",
      json: { ticketPublicId: opt.ticket, secret: opt.secret, estimateId: toInt(opt.estimateId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("payment:link")
  .description("Create Stripe payment link (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--amountCents <n>")
  .option("--currency <cur>", "cad")
  .option("--description <text>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/payment/stripe/link",
      json: {
        ticketId: toInt(opt.ticketId),
        amount_cents: toInt(opt.amountCents),
        currency: opt.currency,
        description: opt.description
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("staff:control:request")
  .description("Request remote control lane (staff) (consent required)")
  .requiredOption("--ticketId <id>")
  .option("--minutes <n>", "30")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/control/request",
      json: { ticketId: toInt(opt.ticketId), minutes: toInt(opt.minutes) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// DOCTOR + SEED
//
program
  .command("doctor")
  .description("Smoke test (public + staff health). Use --deep for more.")
  .option("--deep", "Run deeper checks", false)
  .action(async (opt) => {
    const res = await doctor(!!opt.deep);
    const ok = res.every(r => r.ok);
    console.log(JSON.stringify({ ok, checks: res }, null, 2));
    process.exit(ok ? 0 : 1);
  });

program
  .command("playbooks:seed")
  .description("Seed PB1–PB12 into D1 via /staff/playbooks/seed (staff)")
  .action(async () => {
    const out = await http({
      method: "POST",
      path: "/staff/playbooks/seed",
      json: { playbooks: PLAYBOOKS_SEED }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// PLAYBOOKS: list, get, run
//
program
  .command("playbooks:list")
  .description("List all playbooks (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/playbooks/list" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("playbooks:get")
  .description("Get a playbook + steps (staff)")
  .requiredOption("--code <PBx>")
  .option("--os <os>", "both")
  .action(async (opt) => {
    const out = await http({
      path: `/staff/playbooks/get?code=${encodeURIComponent(opt.code)}&os=${encodeURIComponent(opt.os)}`
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("playbooks:run")
  .description("Start a playbook run for a ticket (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--code <playbookCode>")
  .option("--os <os>", "both")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/playbooks/apply",
      json: { ticketId: toInt(opt.ticketId), playbookCode: toUpperCode(opt.code), os: opt.os }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// SESSION: start (prints join code + wsUrl + auto-listens)
//
program
  .command("session:start")
  .description("Start RTK session (staff), print code + tokens + wsUrl, then auto-listen chat")
  .requiredOption("--ticketId <id>")
  .option("--title <title>", "NoizyLab Live Help")
  .option("--staffName <name>", "NoizyLab Staff")
  .option("--no-listen", "Do not auto-listen on websocket")
  .action(async (opt) => {
    // 1) Start RTK (creates meeting + join code + staff token)
    const started = await http({
      method: "POST",
      path: "/staff/rtk/start",
      json: { ticketId: toInt(opt.ticketId), title: opt.title, staffName: opt.staffName }
    });

    // started = { ok, roomId, code, expiresAt, meetingId, staffAuthToken }
    const roomId = must(started.roomId, "Missing roomId from /staff/rtk/start");

    // 2) Mint wsUrl for staff
    const ws = await http({
      method: "POST",
      path: "/staff/ws/url",
      json: { roomId }
    });

    const payload = {
      ok: true,
      ticketId: toInt(opt.ticketId),
      roomId,
      joinCode: started.code,
      codeExpiresAt: started.expiresAt,
      meetingId: started.meetingId,
      staffAuthToken: started.staffAuthToken,
      wsUrl: ws.wsUrl,
      wsExp: ws.exp
    };

    console.log(JSON.stringify(payload, null, 2));

    // 3) Auto-listen
    if (opt.listen !== false) {
      await wsListen(payload.wsUrl);
    }
  });

// ====================
// HOT ROD COMMANDS
// ====================

//
// SLA
//
program
  .command("sla:stats")
  .description("Get SLA dashboard stats (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/sla/stats" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("sla:targets")
  .description("List SLA targets (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/sla/targets" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("sla:set")
  .description("Set SLA target for ticket (staff)")
  .requiredOption("--ticketId <id>")
  .option("--slaTargetId <id>", "1")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/sla/set",
      json: { ticketId: toInt(opt.ticketId), slaTargetId: toInt(opt.slaTargetId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// CLIENT HEALTH
//
program
  .command("client:health")
  .description("Get client health score (staff)")
  .requiredOption("--clientId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/clients/${opt.clientId}/health` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("client:at-risk")
  .description("List at-risk clients (staff)")
  .option("--threshold <n>", "50")
  .action(async (opt) => {
    const out = await http({ path: `/staff/clients/at-risk?threshold=${opt.threshold}` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("sentiment:record")
  .description("Record client sentiment (staff)")
  .requiredOption("--clientId <id>")
  .option("--ticketId <id>")
  .requiredOption("--score <-2 to +2>")
  .option("--source <source>", "manual")
  .option("--notes <text>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/sentiment/record",
      json: {
        clientId: toInt(opt.clientId),
        ticketId: opt.ticketId ? toInt(opt.ticketId) : null,
        score: toInt(opt.score),
        source: opt.source,
        notes: opt.notes
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// HEATMAP
//
program
  .command("heatmap")
  .description("Get activity heatmap (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/heatmap" });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ESCALATIONS
//
program
  .command("escalations:run")
  .description("Run escalation check (staff)")
  .option("--limit <n>", "50")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/escalations/run",
      json: { limit: toInt(opt.limit) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("escalations:list")
  .description("List escalations for ticket (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/tickets/${opt.ticketId}/escalations` });
    console.log(JSON.stringify(out, null, 2));
  });

//
// BULK OPERATIONS
//
program
  .command("bulk:tag")
  .description("Bulk tag tickets (staff)")
  .requiredOption("--ticketIds <ids>", "Comma-separated ticket IDs")
  .requiredOption("--tags <tags>", "Comma-separated tags")
  .action(async (opt) => {
    const ticketIds = opt.ticketIds.split(",").map((s: string) => toInt(s.trim()));
    const tags = opt.tags.split(",").map((s: string) => s.trim().toUpperCase());
    const out = await http({
      method: "POST",
      path: "/staff/bulk/tag",
      json: { ticketIds, tags }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("bulk:close")
  .description("Bulk close tickets (staff)")
  .requiredOption("--ticketIds <ids>", "Comma-separated ticket IDs")
  .action(async (opt) => {
    const ticketIds = opt.ticketIds.split(",").map((s: string) => toInt(s.trim()));
    const out = await http({
      method: "POST",
      path: "/staff/bulk/close",
      json: { ticketIds }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("bulk:history")
  .description("List bulk operation history (staff)")
  .option("--limit <n>", "50")
  .action(async (opt) => {
    const out = await http({ path: `/staff/bulk/history?limit=${opt.limit}` });
    console.log(JSON.stringify(out, null, 2));
  });

//
// TEMPLATES
//
program
  .command("templates:list")
  .description("List ticket templates (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/templates" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("templates:create")
  .description("Create ticket template (staff)")
  .requiredOption("--code <code>")
  .requiredOption("--name <name>")
  .requiredOption("--subject <subject>")
  .option("--defaultTags <tags>", "Comma-separated tags")
  .option("--playbookCodes <codes>", "Comma-separated playbook codes")
  .option("--slaTargetId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/templates/create",
      json: {
        code: opt.code,
        name: opt.name,
        subject: opt.subject,
        defaultTags: opt.defaultTags?.split(",").map((s: string) => s.trim().toUpperCase()) ?? [],
        playbookCodes: opt.playbookCodes?.split(",").map((s: string) => s.trim()) ?? [],
        slaTargetId: opt.slaTargetId ? toInt(opt.slaTargetId) : null
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("templates:use")
  .description("Create ticket from template (staff)")
  .requiredOption("--templateCode <code>")
  .option("--clientId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/templates/create-ticket",
      json: {
        templateCode: opt.templateCode,
        clientId: opt.clientId ? toInt(opt.clientId) : null
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// DUPLICATES & LINKS
//
program
  .command("tickets:duplicates")
  .description("Find potential duplicate tickets (staff)")
  .requiredOption("--clientId <id>")
  .requiredOption("--subject <text>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/tickets/duplicates",
      json: { clientId: toInt(opt.clientId), subject: opt.subject }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("tickets:link")
  .description("Link two tickets (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--linkedTicketId <id>")
  .option("--linkType <type>", "duplicate|related|parent|child", "related")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/tickets/link",
      json: {
        ticketId: toInt(opt.ticketId),
        linkedTicketId: toInt(opt.linkedTicketId),
        linkType: opt.linkType
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// WEBHOOKS
//
program
  .command("webhooks:list")
  .description("List webhooks (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/webhooks" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("webhooks:create")
  .description("Create webhook (staff)")
  .requiredOption("--name <name>")
  .requiredOption("--url <url>")
  .option("--secret <secret>")
  .option("--events <events>", "Comma-separated event types (or * for all)", "*")
  .action(async (opt) => {
    const events = opt.events === "*" ? ["*"] : opt.events.split(",").map((s: string) => s.trim());
    const out = await http({
      method: "POST",
      path: "/staff/webhooks/create",
      json: { name: opt.name, url: opt.url, secret: opt.secret, events }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("webhooks:toggle")
  .description("Toggle webhook active status (staff)")
  .requiredOption("--id <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/webhooks/${opt.id}/toggle`
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("webhooks:test")
  .description("Test webhook delivery (staff)")
  .requiredOption("--id <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/webhooks/${opt.id}/test`
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// SAVED SEARCHES
//
program
  .command("searches:list")
  .description("List saved searches (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/searches" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("searches:save")
  .description("Save a search (staff)")
  .requiredOption("--name <name>")
  .requiredOption("--query <json>", "JSON query object")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/searches/save",
      json: { name: opt.name, query: JSON.parse(opt.query) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - KNOWLEDGE BASE
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("kb:list")
  .description("List knowledge base articles (public)")
  .option("--category <cat>", "Filter by category")
  .option("--limit <n>", "Max results", "20")
  .action(async (opt) => {
    let path = `/public/kb/articles?limit=${opt.limit}`;
    if (opt.category) path += `&category=${encodeURIComponent(opt.category)}`;
    const out = await http({ path });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("kb:get")
  .description("Get KB article by slug")
  .requiredOption("--slug <slug>")
  .action(async (opt) => {
    const out = await http({ path: `/public/kb/article/${opt.slug}` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("kb:search")
  .description("Search knowledge base")
  .requiredOption("--q <query>")
  .action(async (opt) => {
    const out = await http({ path: `/public/kb/search?q=${encodeURIComponent(opt.q)}` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("kb:create")
  .description("Create KB article (staff)")
  .requiredOption("--title <title>")
  .requiredOption("--slug <slug>")
  .requiredOption("--content <content>")
  .option("--category <cat>")
  .option("--tags <tags>", "Comma-separated tags")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/kb/articles",
      json: {
        title: opt.title,
        slug: opt.slug,
        content: opt.content,
        category: opt.category,
        tags: opt.tags ? opt.tags.split(",").map((t: string) => t.trim()) : []
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("kb:update")
  .description("Update KB article (staff)")
  .requiredOption("--id <id>")
  .option("--title <title>")
  .option("--content <content>")
  .option("--category <cat>")
  .option("--status <status>", "draft|published|archived")
  .action(async (opt) => {
    const out = await http({
      method: "PATCH",
      path: `/staff/kb/article/${opt.id}`,
      json: {
        title: opt.title,
        content: opt.content,
        category: opt.category,
        status: opt.status
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("kb:rate")
  .description("Rate a KB article")
  .requiredOption("--id <id>")
  .requiredOption("--helpful <bool>", "true or false")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/kb/article/${opt.id}/rate`,
      json: { helpful: opt.helpful === "true" }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("kb:suggest")
  .description("Get AI-suggested KB articles for query")
  .requiredOption("--q <query>")
  .action(async (opt) => {
    const out = await http({ path: `/public/kb/suggest?q=${encodeURIComponent(opt.q)}` });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - EMAIL
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("email:send")
  .description("Send email from ticket (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--to <email>")
  .requiredOption("--subject <subject>")
  .requiredOption("--body <body>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/email/send",
      json: {
        ticketId: toInt(opt.ticketId),
        to: opt.to,
        subject: opt.subject,
        body: opt.body
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("email:threads")
  .description("Get email threads for ticket (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/email/threads/${opt.ticketId}` });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - APPOINTMENTS
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("appointments:slots")
  .description("Get available appointment slots (public)")
  .option("--date <date>", "Date YYYY-MM-DD (default: today)")
  .option("--days <n>", "Number of days to fetch", "7")
  .action(async (opt) => {
    let path = `/public/appointments/slots?days=${opt.days}`;
    if (opt.date) path += `&date=${opt.date}`;
    const out = await http({ path });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("appointments:book")
  .description("Book an appointment (public)")
  .requiredOption("--slotId <id>")
  .requiredOption("--email <email>")
  .option("--name <name>")
  .option("--ticketId <id>")
  .option("--notes <notes>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/public/appointments/book",
      json: {
        slotId: toInt(opt.slotId),
        email: opt.email,
        name: opt.name,
        ticketId: opt.ticketId ? toInt(opt.ticketId) : undefined,
        notes: opt.notes
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("appointments:cancel")
  .description("Cancel an appointment")
  .requiredOption("--id <id>")
  .option("--reason <reason>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/public/appointments/${opt.id}/cancel`,
      json: { reason: opt.reason }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("appointments:list")
  .description("List appointments (staff)")
  .option("--date <date>", "Filter by date")
  .option("--status <status>", "Filter by status")
  .action(async (opt) => {
    let path = "/staff/appointments?limit=50";
    if (opt.date) path += `&date=${opt.date}`;
    if (opt.status) path += `&status=${opt.status}`;
    const out = await http({ path });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("appointments:confirm")
  .description("Confirm an appointment (staff)")
  .requiredOption("--id <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/appointments/${opt.id}/confirm`
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("availability:set")
  .description("Set staff availability (staff)")
  .requiredOption("--staffId <id>")
  .requiredOption("--dayOfWeek <n>", "0-6, Sunday=0")
  .requiredOption("--startTime <time>", "HH:MM")
  .requiredOption("--endTime <time>", "HH:MM")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/availability/set",
      json: {
        staffId: opt.staffId,
        dayOfWeek: toInt(opt.dayOfWeek),
        startTime: opt.startTime,
        endTime: opt.endTime
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("availability:generate")
  .description("Generate appointment slots (staff)")
  .requiredOption("--days <n>", "Days to generate")
  .option("--durationMins <n>", "Slot duration", "30")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/availability/generate-slots",
      json: {
        days: toInt(opt.days),
        durationMins: toInt(opt.durationMins)
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - NOTIFICATIONS
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("notifications:send")
  .description("Send notification (staff)")
  .requiredOption("--userId <id>")
  .requiredOption("--channel <chan>", "email|push|sms")
  .requiredOption("--title <title>")
  .requiredOption("--body <body>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/notifications/send",
      json: {
        userId: opt.userId,
        channel: opt.channel,
        title: opt.title,
        body: opt.body
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("notifications:prefs")
  .description("Get notification preferences")
  .requiredOption("--userId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/notifications/prefs/${opt.userId}` });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("notifications:prefs:set")
  .description("Set notification preferences")
  .requiredOption("--userId <id>")
  .requiredOption("--prefs <json>", "JSON preferences object")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/notifications/prefs/${opt.userId}`,
      json: JSON.parse(opt.prefs)
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - REPORTS
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("reports:generate")
  .description("Generate a report (staff)")
  .requiredOption("--type <type>", "ticket_volume|sla_compliance|staff_performance|client_satisfaction")
  .option("--startDate <date>")
  .option("--endDate <date>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/reports/generate",
      json: {
        type: opt.type,
        params: { startDate: opt.startDate, endDate: opt.endDate }
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("reports:schedule")
  .description("Schedule recurring report (staff)")
  .requiredOption("--name <name>")
  .requiredOption("--type <type>")
  .requiredOption("--schedule <cron>", "Cron expression or daily|weekly|monthly")
  .option("--recipients <emails>", "Comma-separated emails")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/reports/schedule",
      json: {
        name: opt.name,
        type: opt.type,
        schedule: opt.schedule,
        recipients: opt.recipients ? opt.recipients.split(",").map((e: string) => e.trim()) : []
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("reports:list")
  .description("List scheduled reports (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/reports/list" });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - WORKSPACES (MULTI-TENANT)
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("workspace:create")
  .description("Create a workspace (staff)")
  .requiredOption("--name <name>")
  .requiredOption("--slug <slug>")
  .option("--plan <plan>", "free|pro|enterprise", "free")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/workspaces/create",
      json: { name: opt.name, slug: opt.slug, plan: opt.plan }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("workspace:list")
  .description("List workspaces (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/workspaces" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("workspace:invite")
  .description("Invite user to workspace (staff)")
  .requiredOption("--workspaceId <id>")
  .requiredOption("--email <email>")
  .option("--role <role>", "owner|admin|member|viewer", "member")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/workspaces/${opt.workspaceId}/invite`,
      json: { email: opt.email, role: opt.role }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("workspace:members")
  .description("List workspace members (staff)")
  .requiredOption("--workspaceId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/workspaces/${opt.workspaceId}/members` });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - API KEYS
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("apikeys:create")
  .description("Create API key (staff)")
  .requiredOption("--name <name>")
  .option("--scopes <scopes>", "Comma-separated scopes (or * for all)", "*")
  .option("--expiresIn <days>", "Expire in N days")
  .action(async (opt) => {
    const scopes = opt.scopes === "*" ? ["*"] : opt.scopes.split(",").map((s: string) => s.trim());
    const json: any = { name: opt.name, scopes };
    if (opt.expiresIn) {
      json.expiresAt = new Date(Date.now() + toInt(opt.expiresIn) * 86400_000).toISOString();
    }
    const out = await http({
      method: "POST",
      path: "/staff/apikeys/create",
      json
    });
    console.log(JSON.stringify(out, null, 2));
    if (out.key) {
      console.log("\n⚠️  SAVE THIS KEY NOW - it won't be shown again!");
    }
  });

program
  .command("apikeys:list")
  .description("List API keys (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/apikeys" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("apikeys:revoke")
  .description("Revoke API key (staff)")
  .requiredOption("--id <id>")
  .action(async (opt) => {
    const out = await http({
      method: "DELETE",
      path: `/staff/apikeys/${opt.id}`
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - INTEGRATIONS
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("integrations:list")
  .description("List integrations (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/integrations" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("integrations:config")
  .description("Configure integration (staff)")
  .requiredOption("--provider <name>", "slack|discord|jira|zendesk|etc")
  .requiredOption("--config <json>", "JSON config object")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/integrations/config",
      json: {
        provider: opt.provider,
        config: JSON.parse(opt.config)
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("integrations:toggle")
  .description("Toggle integration active status (staff)")
  .requiredOption("--id <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: `/staff/integrations/${opt.id}/toggle`
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - AUDIT & COMPLIANCE
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("audit:log")
  .description("View audit log (staff)")
  .option("--resourceType <type>")
  .option("--resourceId <id>")
  .option("--actorId <id>")
  .option("--action <action>")
  .option("--limit <n>", "Max results", "100")
  .action(async (opt) => {
    let path = `/staff/audit/log?limit=${opt.limit}`;
    if (opt.resourceType) path += `&resourceType=${opt.resourceType}`;
    if (opt.resourceId) path += `&resourceId=${opt.resourceId}`;
    if (opt.actorId) path += `&actorId=${opt.actorId}`;
    if (opt.action) path += `&action=${opt.action}`;
    const out = await http({ path });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("gdpr:export")
  .description("Export user data (GDPR) (staff)")
  .requiredOption("--email <email>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/gdpr/export",
      json: { email: opt.email }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("gdpr:delete")
  .description("Delete user data (GDPR) (staff)")
  .requiredOption("--email <email>")
  .option("--confirm", "Confirm deletion")
  .action(async (opt) => {
    if (!opt.confirm) {
      console.log("⚠️  This action is IRREVERSIBLE. Add --confirm to proceed.");
      return;
    }
    const out = await http({
      method: "POST",
      path: "/staff/gdpr/delete",
      json: { email: opt.email }
    });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - TIME TRACKING
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("timer:start")
  .description("Start time tracker on ticket (staff)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--staffId <id>")
  .option("--description <desc>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/timer/start",
      json: {
        ticketId: toInt(opt.ticketId),
        staffId: opt.staffId,
        description: opt.description
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("timer:stop")
  .description("Stop time tracker (staff)")
  .requiredOption("--timerId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/timer/stop",
      json: { timerId: toInt(opt.timerId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("timer:summary")
  .description("Get time summary for ticket (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/tickets/${opt.ticketId}/time` });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - SURVEYS
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("survey:send")
  .description("Send satisfaction survey (staff)")
  .requiredOption("--ticketId <id>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/survey/send",
      json: { ticketId: toInt(opt.ticketId) }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("survey:stats")
  .description("Get survey statistics (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/survey/stats" });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// LEGENDARY UPGRADES - CANNED RESPONSES
// ═══════════════════════════════════════════════════════════════════
//
program
  .command("canned:list")
  .description("List canned responses (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/canned" });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("canned:create")
  .description("Create canned response (staff)")
  .requiredOption("--code <code>")
  .requiredOption("--title <title>")
  .requiredOption("--body <body>")
  .option("--category <cat>")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/canned/create",
      json: {
        code: opt.code,
        title: opt.title,
        body: opt.body,
        category: opt.category
      }
    });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("canned:use")
  .description("Get canned response by code (staff)")
  .requiredOption("--code <code>")
  .action(async (opt) => {
    const out = await http({ path: `/staff/canned/${opt.code}` });
    console.log(JSON.stringify(out, null, 2));
  });

//
// ═══════════════════════════════════════════════════════════════════
// ROUND 3: COMPUTING LEGENDS - Knowledge Workers
// ═══════════════════════════════════════════════════════════════════
//

// CPU Architecture
program
  .command("cpu:info")
  .description("Get CPU architecture information")
  .option("--arch <arch>", "x86|arm|risc-v|mips")
  .action(async (opt) => {
    const path = opt.arch ? `/cpu/${opt.arch}` : "/cpu/architectures";
    console.log(`🔧 Querying CPU Architecture Worker...`);
    const out = await http({ path, baseUrl: process.env.CPU_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("cpu:ask")
  .description("Ask AI about CPU architectures")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking CPU Architecture AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.CPU_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Operating Systems
program
  .command("os:history")
  .description("Get operating system history")
  .option("--family <family>", "unix|windows|macos|linux|mobile")
  .action(async (opt) => {
    const path = opt.family ? `/${opt.family}` : "/history";
    console.log(`💻 Querying Operating Systems Worker...`);
    const out = await http({ path, baseUrl: process.env.OS_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("os:ask")
  .description("Ask AI about operating systems")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Operating Systems AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.OS_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Programming Languages
program
  .command("lang:list")
  .description("Get programming language information")
  .option("--family <family>", "c|lisp|ml|scripting")
  .action(async (opt) => {
    const path = opt.family ? `/family/${opt.family}` : "/languages";
    console.log(`📝 Querying Programming Languages Worker...`);
    const out = await http({ path, baseUrl: process.env.LANG_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("lang:ask")
  .description("Ask AI about programming languages")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Programming Languages AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.LANG_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// GPU Computing
program
  .command("gpu:info")
  .description("Get GPU computing information")
  .option("--vendor <vendor>", "nvidia|amd|intel")
  .action(async (opt) => {
    const path = opt.vendor ? `/${opt.vendor}` : "/history";
    console.log(`🎮 Querying GPU Computing Worker...`);
    const out = await http({ path, baseUrl: process.env.GPU_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("gpu:ask")
  .description("Ask AI about GPUs and graphics computing")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking GPU Computing AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.GPU_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Network Protocols
program
  .command("net:protocols")
  .description("Get network protocol information")
  .option("--layer <layer>", "osi|tcp-ip|application")
  .action(async (opt) => {
    const path = opt.layer ? `/${opt.layer}` : "/osi";
    console.log(`🌐 Querying Network Protocols Worker...`);
    const out = await http({ path, baseUrl: process.env.NET_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("net:ask")
  .description("Ask AI about networking")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Network Protocols AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.NET_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Database Systems
program
  .command("db:info")
  .description("Get database systems information")
  .option("--type <type>", "relational|nosql|graph|timeseries")
  .action(async (opt) => {
    const path = opt.type ? `/${opt.type}` : "/history";
    console.log(`🗄️ Querying Database Systems Worker...`);
    const out = await http({ path, baseUrl: process.env.DB_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("db:ask")
  .description("Ask AI about databases")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Database Systems AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.DB_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// AI/ML History
program
  .command("ai:history")
  .description("Get AI/ML history")
  .option("--era <era>", "early|winters|deep-learning|transformers|llms")
  .action(async (opt) => {
    const path = opt.era ? `/${opt.era}` : "/timeline";
    console.log(`🤖 Querying AI/ML History Worker...`);
    const out = await http({ path, baseUrl: process.env.AIML_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("ai:ask")
  .description("Ask AI about AI/ML history")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking AI/ML History AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.AIML_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Security Systems
program
  .command("sec:info")
  .description("Get security systems information")
  .option("--topic <topic>", "encryption|authentication|malware|zero-trust")
  .action(async (opt) => {
    const path = opt.topic ? `/${opt.topic}` : "/history";
    console.log(`🔒 Querying Security Systems Worker...`);
    const out = await http({ path, baseUrl: process.env.SEC_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("sec:ask")
  .description("Ask AI about cybersecurity")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Security Systems AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.SEC_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Memory Systems
program
  .command("mem:info")
  .description("Get memory systems information")
  .option("--type <type>", "ddr|cache|hbm|emerging")
  .action(async (opt) => {
    const path = opt.type ? `/${opt.type}` : "/evolution";
    console.log(`🧩 Querying Memory Systems Worker...`);
    const out = await http({ path, baseUrl: process.env.MEM_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("mem:ask")
  .description("Ask AI about memory technology")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Memory Systems AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.MEM_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Storage Evolution
program
  .command("storage:info")
  .description("Get storage evolution information")
  .option("--type <type>", "hdd|ssd|nvme|filesystems|raid")
  .action(async (opt) => {
    const path = opt.type ? `/${opt.type}` : "/history";
    console.log(`💾 Querying Storage Evolution Worker...`);
    const out = await http({ path, baseUrl: process.env.STORAGE_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("storage:ask")
  .description("Ask AI about storage technology")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Storage Evolution AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.STORAGE_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Display Technology
program
  .command("display:info")
  .description("Get display technology information")
  .option("--type <type>", "lcd|oled|gaming|connectors")
  .action(async (opt) => {
    const path = opt.type ? `/${opt.type}` : "/history";
    console.log(`🖥️ Querying Display Technology Worker...`);
    const out = await http({ path, baseUrl: process.env.DISPLAY_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("display:ask")
  .description("Ask AI about display technology")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Display Technology AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.DISPLAY_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Motherboard Systems
program
  .command("mobo:info")
  .description("Get motherboard systems information")
  .option("--topic <topic>", "form-factors|buses|chipsets|sockets")
  .action(async (opt) => {
    const path = opt.topic ? `/${opt.topic}` : "/history";
    console.log(`🔌 Querying Motherboard Systems Worker...`);
    const out = await http({ path, baseUrl: process.env.MOBO_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("mobo:ask")
  .description("Ask AI about motherboards")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Motherboard Systems AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.MOBO_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Computing History
program
  .command("history:timeline")
  .description("Get computing history timeline")
  .option("--era <era>", "1940s|1950s|1960s|1970s|1980s|1990s|2000s|2010s|2020s")
  .action(async (opt) => {
    const path = opt.era ? `/era/${opt.era}` : "/timeline";
    console.log(`📜 Querying Computing History Worker...`);
    const out = await http({ path, baseUrl: process.env.HISTORY_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("history:ask")
  .description("Ask AI about computing history")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Computing History AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.HISTORY_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Quantum Computing
program
  .command("quantum:info")
  .description("Get quantum computing information")
  .option("--topic <topic>", "principles|algorithms|hardware|companies")
  .action(async (opt) => {
    const path = opt.topic ? `/${opt.topic}` : "/";
    console.log(`⚛️ Querying Quantum Computing Worker...`);
    const out = await http({ path, baseUrl: process.env.QUANTUM_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("quantum:ask")
  .description("Ask AI about quantum computing")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Quantum Computing AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.QUANTUM_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Compiler Technology
program
  .command("compiler:info")
  .description("Get compiler technology information")
  .option("--phase <phase>", "lexer|parser|optimizer|codegen")
  .action(async (opt) => {
    const path = opt.phase ? `/${opt.phase}` : "/";
    console.log(`⚙️ Querying Compiler Technology Worker...`);
    const out = await http({ path, baseUrl: process.env.COMPILER_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("compiler:ask")
  .description("Ask AI about compilers")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Compiler Technology AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.COMPILER_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Virtualization
program
  .command("virt:info")
  .description("Get virtualization information")
  .option("--type <type>", "hypervisors|containers|orchestration")
  .action(async (opt) => {
    const path = opt.type ? `/${opt.type}` : "/";
    console.log(`📦 Querying Virtualization Worker...`);
    const out = await http({ path, baseUrl: process.env.VIRT_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("virt:ask")
  .description("Ask AI about virtualization")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Virtualization AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.VIRT_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Embedded Systems
program
  .command("embedded:info")
  .description("Get embedded systems information")
  .option("--type <type>", "microcontrollers|rtos|iot|automotive")
  .action(async (opt) => {
    const path = opt.type ? `/${opt.type}` : "/";
    console.log(`🔧 Querying Embedded Systems Worker...`);
    const out = await http({ path, baseUrl: process.env.EMBEDDED_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("embedded:ask")
  .description("Ask AI about embedded systems")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Embedded Systems AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.EMBEDDED_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// HCI Evolution
program
  .command("hci:info")
  .description("Get HCI evolution information")
  .option("--type <type>", "input|displays|gui|vr-ar")
  .action(async (opt) => {
    const path = opt.type ? `/${opt.type}` : "/";
    console.log(`🖱️ Querying HCI Evolution Worker...`);
    const out = await http({ path, baseUrl: process.env.HCI_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("hci:ask")
  .description("Ask AI about human-computer interaction")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking HCI Evolution AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.HCI_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Xcode Genius
program
  .command("xcode:info")
  .description("Get Xcode information")
  .option("--topic <topic>", "build|signing|provisioning|swift")
  .action(async (opt) => {
    const path = opt.topic ? `/${opt.topic}` : "/";
    console.log(`🍎 Querying Xcode Genius Worker...`);
    const out = await http({ path, baseUrl: process.env.XCODE_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("xcode:ask")
  .description("Ask AI about Xcode development")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Xcode Genius AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.XCODE_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Automator Genius
program
  .command("automator:info")
  .description("Get macOS automation information")
  .option("--topic <topic>", "workflows|applescript|shortcuts")
  .action(async (opt) => {
    const path = opt.topic ? `/${opt.topic}` : "/";
    console.log(`⚡ Querying Automator Genius Worker...`);
    const out = await http({ path, baseUrl: process.env.AUTOMATOR_WORKER_URL });
    console.log(JSON.stringify(out, null, 2));
  });

program
  .command("automator:ask")
  .description("Ask AI about macOS automation")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🧠 Asking Automator Genius AI...`);
    const out = await http({
      method: "POST",
      path: "/ai/query",
      baseUrl: process.env.AUTOMATOR_WORKER_URL,
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Universal Knowledge Query - Ask any worker
program
  .command("ask")
  .description("Ask any computing question (routes to best worker)")
  .requiredOption("--question <q>")
  .action(async (opt) => {
    console.log(`🌌 Querying NoizyLab OS Universal Knowledge...`);
    const out = await http({
      method: "POST",
      path: "/ai/universal-query",
      json: { question: opt.question }
    });
    console.log(JSON.stringify(out, null, 2));
  });

// Worker Status
program
  .command("workers:status")
  .description("Get status of all 57 workers")
  .action(async () => {
    console.log(`📊 Checking NoizyLab OS Worker Status...`);
    const out = await http({ path: "/workers/status" });
    console.log(JSON.stringify(out, null, 2));
  });

await program.parseAsync(process.argv);
