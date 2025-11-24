/**
 * NOIZYLAB Email System - Providers Index
 * Export all email providers
 */

export { BaseEmailProvider, type SendOptions, type ProviderResponse } from './base';
export { MailChannelsProvider, createMailChannelsProvider } from './mailchannels';
export { ResendProvider, createResendProvider } from './resend';
export { SendGridProvider, createSendGridProvider } from './sendgrid';
export { MockProvider, createMockProvider, type MockSentEmail, type MockProviderConfig } from './mock';

import type { EmailProvider } from '../../types';
import { BaseEmailProvider } from './base';
import { MailChannelsProvider, createMailChannelsProvider } from './mailchannels';
import { ResendProvider, createResendProvider } from './resend';
import { SendGridProvider, createSendGridProvider } from './sendgrid';
import { MockProvider } from './mock';

/**
 * Provider registry type
 */
export type ProviderRegistry = {
  [K in EmailProvider]?: BaseEmailProvider;
};

/**
 * Create all available providers from environment
 */
export function createProviders(env: Env): ProviderRegistry {
  const providers: ProviderRegistry = {};

  // MailChannels is always available (free for Workers)
  providers.mailchannels = createMailChannelsProvider(env);

  // Resend (if API key provided)
  const resend = createResendProvider(env);
  if (resend !== null) {
    providers.resend = resend;
  }

  // SendGrid (if API key provided)
  const sendgrid = createSendGridProvider(env);
  if (sendgrid !== null) {
    providers.sendgrid = sendgrid;
  }

  return providers;
}

/**
 * Get default provider based on availability
 */
export function getDefaultProvider(providers: ProviderRegistry): BaseEmailProvider {
  // Priority: Resend > SendGrid > MailChannels
  if (providers.resend !== undefined) {
    return providers.resend;
  }
  if (providers.sendgrid !== undefined) {
    return providers.sendgrid;
  }
  if (providers.mailchannels !== undefined) {
    return providers.mailchannels;
  }

  throw new Error('No email provider available');
}

/**
 * Get provider by name
 */
export function getProvider(
  providers: ProviderRegistry,
  name: EmailProvider
): BaseEmailProvider | undefined {
  return providers[name];
}
