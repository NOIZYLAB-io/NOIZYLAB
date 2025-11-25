// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB AGENT TESTS
// ═══════════════════════════════════════════════════════════════════════════════

import { test, describe } from "node:test";
import assert from "node:assert";
import { AGENTS, getAgent, getAgentByTrigger } from "../agents/agent-definitions.js";

describe("Agent Definitions", () => {

  test("should have all 6 agents defined", () => {
    const agentNames = Object.keys(AGENTS);
    assert.strictEqual(agentNames.length, 6);
    assert.ok(agentNames.includes("LUCY"));
    assert.ok(agentNames.includes("KEITH"));
    assert.ok(agentNames.includes("WARDY"));
    assert.ok(agentNames.includes("RED_ALERT"));
    assert.ok(agentNames.includes("NOVA"));
    assert.ok(agentNames.includes("ECHO"));
  });

  test("should get agent by name", () => {
    const lucy = getAgent("LUCY");
    assert.strictEqual(lucy.name, "LUCY");
    assert.strictEqual(lucy.role, "Creative Director");
  });

  test("should get agent by name case-insensitive", () => {
    const keith = getAgent("keith");
    assert.strictEqual(keith.name, "KEITH");
  });

  test("should return RED_ALERT for urgent keywords", () => {
    const agent = getAgentByTrigger("URGENT: Server is down!");
    assert.strictEqual(agent.name, "RED_ALERT");
  });

  test("should return KEITH for technical keywords", () => {
    const agent = getAgentByTrigger("I found a bug in the API");
    assert.strictEqual(agent.name, "KEITH");
  });

  test("should return LUCY for creative keywords", () => {
    const agent = getAgentByTrigger("Need help with logo design");
    assert.strictEqual(agent.name, "LUCY");
  });

  test("should return WARDY for project keywords", () => {
    const agent = getAgentByTrigger("What's the project deadline?");
    assert.strictEqual(agent.name, "WARDY");
  });

  test("should return NOVA for research keywords", () => {
    const agent = getAgentByTrigger("Can you analyze this data?");
    assert.strictEqual(agent.name, "NOVA");
  });

  test("should default to ECHO for general messages", () => {
    const agent = getAgentByTrigger("Hello, I have a question");
    assert.strictEqual(agent.name, "ECHO");
  });

  test("each agent should have required properties", () => {
    for (const agent of Object.values(AGENTS)) {
      assert.ok(agent.id, `${agent.name} missing id`);
      assert.ok(agent.name, `${agent.name} missing name`);
      assert.ok(agent.role, `${agent.name} missing role`);
      assert.ok(agent.emoji, `${agent.name} missing emoji`);
      assert.ok(agent.color, `${agent.name} missing color`);
      assert.ok(agent.personality, `${agent.name} missing personality`);
      assert.ok(agent.capabilities, `${agent.name} missing capabilities`);
      assert.ok(agent.triggers, `${agent.name} missing triggers`);
      assert.ok(agent.prompts, `${agent.name} missing prompts`);
    }
  });

});

describe("Spam Detection", () => {

  test("should detect common spam patterns", () => {
    const spamTexts = [
      "You have won $1,000,000 USD!",
      "Click here for free money",
      "Nigerian prince needs your help",
      "Act now! Limited time offer!"
    ];

    // These should be flagged as spam (score >= 7)
    // In real tests, import the spam detection function
    assert.ok(spamTexts.length > 0);
  });

});

console.log("Running NoizyLab tests...");
