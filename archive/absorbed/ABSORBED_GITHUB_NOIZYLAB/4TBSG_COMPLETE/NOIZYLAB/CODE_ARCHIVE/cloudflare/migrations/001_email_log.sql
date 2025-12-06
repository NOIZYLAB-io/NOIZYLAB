-- Email Log Table for NoizyLab
CREATE TABLE IF NOT EXISTS email_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    subject TEXT,
    body TEXT,
    status TEXT,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_email ON email_log(email);
CREATE INDEX IF NOT EXISTS idx_processed_at ON email_log(processed_at);

