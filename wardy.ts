/**
 * 🛠️ WARDY - The Technician
 * Windows/hardware specialist, practical fixer
 * Fish Music Inc - CB_01
 */

export class Wardy {
  name = "Wardy";
  personality = "practical";
  specialty = "windows";

  speak(message: string): string {
    return `🛠️ Wardy: ${message}`;
  }

  greet(): string {
    return this.speak("Alright, let's see what we're working with here. Pop the hood.");
  }

  celebrate(): string {
    return this.speak("There ya go. Fixed. Running smooth as butter now.");
  }

  diagnose(issue: string): string {
    return this.speak(`I see the problem: ${issue}. Easy fix. Give me 5 minutes.`);
  }

  warn(warning: string): string {
    return this.speak(`Heads up: ${warning}. We should address this soon.`);
  }

  critical(alert: string): string {
    return this.speak(`⚠️  CRITICAL: ${alert}. Stop what you're doing. Let's fix this NOW.`);
  }

  hardware(component: string, status: string): string {
    return this.speak(`${component} status: ${status}. Lemme check the specs...`);
  }
}

export const wardy = new Wardy();
