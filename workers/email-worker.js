export default {
  async email(message, env, ctx) {
    const from = message.from;
    const to = message.to;
    const subject = message.subject;
    const body = await message.text();

    // ANALYZE WITH CLOUDFLARE AI
    const analysis = await env.AI.run(
      "@cf/mistral/mistral-7b-instruct-v0.1",
      {
        prompt: `
        Analyze this email and classify it.

        From: ${from}
        To: ${to}
        Subject: ${subject}
        Body: ${body}

        Return JSON with:
        - intent
        - urgency (0-10)
        - summary
        - recommended_agent (LUCY | KEITH | WARDY | RED_ALERT)
        `
      }
    );

    const parsed = JSON.parse(analysis);

    // STORE LOGS
    await env.MAIL_LOGS.put(Date.now().toString(), JSON.stringify({
      from, to, subject,
      ...parsed
    }));

    // SUMMON AGENT
    await callAgent(parsed.recommended_agent, parsed, env);

    // FORWARD EMAIL
    await message.forward("rsplowman@icloud.com");

    // AUTO-REPLY FOR HIGH URGENCY
    if (parsed.urgency >= 8) {
      await message.reply({
        from: "rsp@noizylab.ca",
        subject: "We received your urgent message",
        body: `Your email was flagged urgent.\nSummary: ${parsed.summary}\n– NoizyLab AI`
      });
    }
  }
};

async function callAgent(agent, data, env) {
  const resp = await env.AI.run(
    "@cf/mistral/mistral-7b-instruct-v0.1",
    {
      prompt: `
        You are agent ${agent}.
        Perform analysis and respond JSON with:
        - agent
        - action
        - notes
        - priority
        Email data: ${JSON.stringify(data, null, 2)}
      `
    }
  );

  await env.MAIL_LOGS.put(
    `agent-${Date.now()}`,
    resp
  );
}
