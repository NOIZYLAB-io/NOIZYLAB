/**
 * 🎭 AVATAR ENGINE
 * Manages Lucy, Keith, and Wardy personalities
 * Fish Music Inc - CB_01
 */

import { Lucy, lucy } from './lucy';
import { Keith, keith } from './keith';
import { Wardy, wardy } from './wardy';

export type AvatarName = 'Lucy' | 'Keith' | 'Wardy';

export const Avatars = {
  Lucy: lucy,
  Keith: keith,
  Wardy: wardy
};

export function selectAvatar(context: any): Lucy | Keith | Wardy {
  const os = context.device?.os || '';
  const urgency = context.metrics?.urgency || 'normal';
  const preference = context.user?.preferred_avatar;

  // User preference overrides
  if (preference && Avatars[preference as AvatarName]) {
    return Avatars[preference as AvatarName];
  }

  // Auto-select based on context
  if (os.includes('mac') || os.includes('Mac')) {
    return Avatars.Lucy;  // Lucy for Mac
  }

  if (os.includes('Windows') || os.includes('windows')) {
    return Avatars.Wardy;  // Wardy for Windows
  }

  if (urgency === 'high' || urgency === 'emergency') {
    return Avatars.Keith;  // Keith for strategic situations
  }

  // Default: Lucy (most friendly)
  return Avatars.Lucy;
}

export function speakAsAvatar(context: any, message: string): string {
  const avatar = selectAvatar(context);
  return avatar.speak(message);
}

export function greetAsAvatar(context: any): string {
  const avatar = selectAvatar(context);
  return avatar.greet();
}

export const avatarEngine = {
  init: () => {
    console.log('🎭 Avatar Engine initialized');
    console.log('   Avatars: Lucy, Keith, Wardy');
  },
  select: selectAvatar,
  speak: speakAsAvatar,
  greet: greetAsAvatar,
  getAll: () => Avatars
};
