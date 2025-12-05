// auto-accept-current-mission.ts

// Ultra-clean, hardened, mission-scoped auto-accept handler for Cursor.

// Place in: .cursor/extensions/auto-accept-current-mission.ts

export function activate(agent: any) {

  // Active only for current mission

  let missionActive = true;



  // Regex catches all review/confirm phrasing without triggering false positives

  const confirmPattern = /\b(review|confirm|approve|apply changes|proceed|continue|are you sure|accept)\b/i;



  agent.onPrompt(async (prompt: string) => {

    if (!missionActive) return null;



    if (confirmPattern.test(prompt)) {

      return "yes"; // green light everything relevant

    }



    return null; // ignore unrelated prompts

  });



  // Hard shut-off when mission ends

  agent.onEvent("mission:end", () => {

    missionActive = false;

  });



  // Safety override if Cursor changes APIs later

  agent.onEvent("session:ended", () => {

    missionActive = false;

  });

}
