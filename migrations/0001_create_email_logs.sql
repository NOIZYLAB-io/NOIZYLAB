-- NOIZYLAB Email System - Database Schema
-- Migration: Create email_logs table

-- Email logs table for tracking all sent emails
CREATE TABLE IF NOT EXISTS email_logs (
    id TEXT PRIMARY KEY,
    message_id TEXT UNIQUE NOT NULL,
    to_addresses TEXT NOT NULL, -- JSON array of email addresses
    from_address TEXT NOT NULL,
    subject TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('queued', 'sending', 'sent', 'delivered', 'bounced', 'failed', 'scheduled')),
    provider TEXT NOT NULL CHECK (provider IN ('mailchannels', 'resend', 'sendgrid', 'mock')),
    template_id TEXT,
    tags TEXT, -- JSON array
    metadata TEXT, -- JSON object
    error_message TEXT,
    sent_at TEXT,
    delivered_at TEXT,
    bounced_at TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_email_logs_message_id ON email_logs(message_id);
CREATE INDEX IF NOT EXISTS idx_email_logs_status ON email_logs(status);
CREATE INDEX IF NOT EXISTS idx_email_logs_from_address ON email_logs(from_address);
CREATE INDEX IF NOT EXISTS idx_email_logs_created_at ON email_logs(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_email_logs_template_id ON email_logs(template_id);

-- Webhook events table for tracking delivery events
CREATE TABLE IF NOT EXISTS webhook_events (
    id TEXT PRIMARY KEY,
    message_id TEXT NOT NULL,
    event_type TEXT NOT NULL CHECK (event_type IN ('email.sent', 'email.delivered', 'email.bounced', 'email.complained', 'email.failed')),
    provider TEXT NOT NULL,
    payload TEXT NOT NULL, -- JSON object
    processed_at TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (message_id) REFERENCES email_logs(message_id)
);

CREATE INDEX IF NOT EXISTS idx_webhook_events_message_id ON webhook_events(message_id);
CREATE INDEX IF NOT EXISTS idx_webhook_events_event_type ON webhook_events(event_type);
CREATE INDEX IF NOT EXISTS idx_webhook_events_created_at ON webhook_events(created_at DESC);

-- Suppression list for bounced/complained addresses
CREATE TABLE IF NOT EXISTS suppression_list (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    reason TEXT NOT NULL CHECK (reason IN ('bounce', 'complaint', 'manual')),
    source_message_id TEXT,
    notes TEXT,
    created_at TEXT NOT NULL,
    expires_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_suppression_list_email ON suppression_list(email);
CREATE INDEX IF NOT EXISTS idx_suppression_list_reason ON suppression_list(reason);
