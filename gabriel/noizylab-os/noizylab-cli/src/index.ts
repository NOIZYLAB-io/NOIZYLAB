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
  .command("dlq:list")
  .description("List DLQ quarantined jobs (staff)")
  .action(async () => {
    const out = await http({ path: "/staff/dlq/list" });
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

await program.parseAsync(process.argv);
