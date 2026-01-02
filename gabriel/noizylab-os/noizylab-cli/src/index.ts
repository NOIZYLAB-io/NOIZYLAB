import { Command } from "commander";
import dotenv from "dotenv";
dotenv.config();

import { http } from "./http.js";
import { wsListen, wsSend } from "./ws.js";
import { must, toInt, toUpperCode } from "./util.js";

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
  .command("staff:payment:link")
  .description("Create payment link (staff) (provider-agnostic stub)")
  .requiredOption("--ticketId <id>")
  .requiredOption("--amountCents <n>")
  .option("--currency <cur>", "CAD")
  .option("--provider <p>", "stripe")
  .action(async (opt) => {
    const out = await http({
      method: "POST",
      path: "/staff/payment/link",
      json: {
        ticketId: toInt(opt.ticketId),
        amount_cents: toInt(opt.amountCents),
        currency: opt.currency,
        provider: opt.provider
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

await program.parseAsync(process.argv);
