/**
 * NOIZYLAB Dashboard Routes
 * Beautiful web dashboard for API token management
 */

import { Hono } from 'hono';
import { html } from 'hono/html';
import type { Env, Variables } from '../types';

const dashboard = new Hono<{ Bindings: Env; Variables: Variables }>();

// Dashboard HTML Template
const dashboardHTML = () => html`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOIZYLAB - API Token Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a0a0f;
            --bg-secondary: #12121a;
            --bg-tertiary: #1a1a25;
            --bg-card: #16161f;
            --accent-primary: #6366f1;
            --accent-secondary: #8b5cf6;
            --accent-gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
            --text-primary: #ffffff;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --border-color: #2a2a3a;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --info: #3b82f6;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            line-height: 1.6;
        }

        /* Animated background */
        .bg-gradient {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background:
                radial-gradient(ellipse at 20% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(168, 85, 247, 0.05) 0%, transparent 70%);
            pointer-events: none;
            z-index: 0;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
            position: relative;
            z-index: 1;
        }

        /* Header */
        header {
            padding: 1.5rem 0;
            border-bottom: 1px solid var(--border-color);
            background: rgba(10, 10, 15, 0.8);
            backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .logo-icon {
            width: 48px;
            height: 48px;
            background: var(--accent-gradient);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.25rem;
        }

        .logo-text h1 {
            font-size: 1.5rem;
            font-weight: 700;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .logo-text span {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        .header-actions {
            display: flex;
            gap: 1rem;
            align-items: center;
        }

        /* Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            font-weight: 500;
            font-size: 0.875rem;
            cursor: pointer;
            transition: all 0.2s ease;
            border: none;
            text-decoration: none;
        }

        .btn-primary {
            background: var(--accent-gradient);
            color: white;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
        }

        .btn-secondary {
            background: var(--bg-tertiary);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
        }

        .btn-secondary:hover {
            background: var(--bg-card);
            border-color: var(--accent-primary);
        }

        .btn-danger {
            background: rgba(239, 68, 68, 0.1);
            color: var(--danger);
            border: 1px solid rgba(239, 68, 68, 0.3);
        }

        .btn-danger:hover {
            background: rgba(239, 68, 68, 0.2);
        }

        .btn-sm {
            padding: 0.5rem 1rem;
            font-size: 0.8125rem;
        }

        /* Main content */
        main {
            padding: 2rem 0 4rem;
        }

        /* Stats Cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .stat-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            border-color: var(--accent-primary);
            transform: translateY(-2px);
        }

        .stat-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
        }

        .stat-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .stat-icon.blue { background: rgba(59, 130, 246, 0.1); }
        .stat-icon.green { background: rgba(16, 185, 129, 0.1); }
        .stat-icon.purple { background: rgba(139, 92, 246, 0.1); }
        .stat-icon.orange { background: rgba(245, 158, 11, 0.1); }

        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .stat-label {
            color: var(--text-muted);
            font-size: 0.875rem;
        }

        .stat-change {
            font-size: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }

        .stat-change.positive { color: var(--success); }
        .stat-change.negative { color: var(--danger); }

        /* Section */
        .section {
            margin-bottom: 2rem;
        }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
        }

        .section-title {
            font-size: 1.25rem;
            font-weight: 600;
        }

        /* Token Table */
        .table-container {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            overflow: hidden;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            text-align: left;
            padding: 1rem 1.5rem;
            background: var(--bg-tertiary);
            color: var(--text-secondary);
            font-weight: 500;
            font-size: 0.8125rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            border-bottom: 1px solid var(--border-color);
        }

        td {
            padding: 1rem 1.5rem;
            border-bottom: 1px solid var(--border-color);
            vertical-align: middle;
        }

        tr:last-child td {
            border-bottom: none;
        }

        tr:hover {
            background: rgba(99, 102, 241, 0.03);
        }

        .token-name {
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .token-icon {
            width: 36px;
            height: 36px;
            background: var(--accent-gradient);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .token-key {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8125rem;
            color: var(--text-muted);
            background: var(--bg-tertiary);
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 500;
        }

        .badge-active {
            background: rgba(16, 185, 129, 0.1);
            color: var(--success);
        }

        .badge-inactive {
            background: rgba(239, 68, 68, 0.1);
            color: var(--danger);
        }

        .badge-scope {
            background: rgba(99, 102, 241, 0.1);
            color: var(--accent-primary);
            margin-right: 0.25rem;
            margin-bottom: 0.25rem;
        }

        .scopes-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.25rem;
        }

        .actions {
            display: flex;
            gap: 0.5rem;
        }

        .action-btn {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background: var(--bg-tertiary);
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }

        .action-btn:hover {
            border-color: var(--accent-primary);
            color: var(--accent-primary);
        }

        .action-btn.danger:hover {
            border-color: var(--danger);
            color: var(--danger);
        }

        /* Modal */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(8px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 1000;
        }

        .modal-overlay.active {
            display: flex;
        }

        .modal {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            width: 100%;
            max-width: 600px;
            max-height: 90vh;
            overflow-y: auto;
            animation: modalSlide 0.3s ease;
        }

        @keyframes modalSlide {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .modal-header {
            padding: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .modal-title {
            font-size: 1.25rem;
            font-weight: 600;
        }

        .modal-close {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            border: 1px solid var(--border-color);
            background: transparent;
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }

        .modal-close:hover {
            border-color: var(--danger);
            color: var(--danger);
        }

        .modal-body {
            padding: 1.5rem;
        }

        .modal-footer {
            padding: 1.5rem;
            border-top: 1px solid var(--border-color);
            display: flex;
            gap: 1rem;
            justify-content: flex-end;
        }

        /* Form */
        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            font-size: 0.875rem;
        }

        .form-input {
            width: 100%;
            padding: 0.75rem 1rem;
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            color: var(--text-primary);
            font-size: 0.9375rem;
            transition: all 0.2s ease;
        }

        .form-input:focus {
            outline: none;
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        }

        .form-hint {
            margin-top: 0.5rem;
            font-size: 0.8125rem;
            color: var(--text-muted);
        }

        .checkbox-group {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.75rem;
        }

        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem;
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .checkbox-item:hover {
            border-color: var(--accent-primary);
        }

        .checkbox-item input {
            width: 18px;
            height: 18px;
            accent-color: var(--accent-primary);
        }

        .checkbox-item label {
            font-size: 0.875rem;
            cursor: pointer;
        }

        /* Token Display */
        .token-display {
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
        }

        .token-display-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.75rem;
        }

        .token-display-value {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9375rem;
            word-break: break-all;
            padding: 1rem;
            background: var(--bg-primary);
            border-radius: 8px;
        }

        .token-warning {
            background: rgba(245, 158, 11, 0.1);
            border: 1px solid rgba(245, 158, 11, 0.3);
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            display: flex;
            gap: 0.75rem;
            align-items: flex-start;
        }

        .token-warning-icon {
            color: var(--warning);
            font-size: 1.25rem;
        }

        .token-warning-text {
            font-size: 0.875rem;
            color: var(--warning);
        }

        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 4rem 2rem;
        }

        .empty-state-icon {
            width: 80px;
            height: 80px;
            background: var(--bg-tertiary);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            font-size: 2rem;
        }

        .empty-state-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .empty-state-text {
            color: var(--text-muted);
            margin-bottom: 1.5rem;
        }

        /* Loading */
        .loading {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid var(--border-color);
            border-top-color: var(--accent-primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Toast */
        .toast-container {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 2000;
        }

        .toast {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1rem 1.5rem;
            margin-top: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            animation: toastSlide 0.3s ease;
        }

        @keyframes toastSlide {
            from {
                opacity: 0;
                transform: translateX(100%);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .toast-success { border-left: 3px solid var(--success); }
        .toast-error { border-left: 3px solid var(--danger); }
        .toast-warning { border-left: 3px solid var(--warning); }

        /* Responsive */
        @media (max-width: 768px) {
            .container {
                padding: 0 1rem;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }

            .table-container {
                overflow-x: auto;
            }

            table {
                min-width: 800px;
            }

            .checkbox-group {
                grid-template-columns: 1fr;
            }

            .modal {
                margin: 1rem;
                max-height: calc(100vh - 2rem);
            }
        }
    </style>
</head>
<body>
    <div class="bg-gradient"></div>

    <header>
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <div class="logo-icon">NZ</div>
                    <div class="logo-text">
                        <h1>NOIZYLAB</h1>
                        <span>API Token Dashboard</span>
                    </div>
                </div>
                <div class="header-actions">
                    <a href="/health" class="btn btn-secondary">
                        <span>🔍</span> Health
                    </a>
                    <a href="/docs" class="btn btn-secondary">
                        <span>📚</span> Docs
                    </a>
                    <button class="btn btn-primary" onclick="openCreateModal()">
                        <span>✨</span> Create Token
                    </button>
                </div>
            </div>
        </div>
    </header>

    <main>
        <div class="container">
            <!-- Stats -->
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon blue">🔑</div>
                        <span class="stat-change positive">↑ 12%</span>
                    </div>
                    <div class="stat-value" id="stat-total">--</div>
                    <div class="stat-label">Total Tokens</div>
                </div>
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon green">✅</div>
                        <span class="stat-change positive">Active</span>
                    </div>
                    <div class="stat-value" id="stat-active">--</div>
                    <div class="stat-label">Active Tokens</div>
                </div>
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon purple">📊</div>
                        <span class="stat-change positive">↑ 24%</span>
                    </div>
                    <div class="stat-value" id="stat-requests">--</div>
                    <div class="stat-label">API Requests (24h)</div>
                </div>
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon orange">⚡</div>
                        <span class="stat-change">Avg</span>
                    </div>
                    <div class="stat-value" id="stat-latency">--</div>
                    <div class="stat-label">Avg Response (ms)</div>
                </div>
            </div>

            <!-- Tokens Section -->
            <div class="section">
                <div class="section-header">
                    <h2 class="section-title">API Tokens</h2>
                    <div class="header-actions">
                        <button class="btn btn-secondary btn-sm" onclick="refreshTokens()">
                            <span>🔄</span> Refresh
                        </button>
                    </div>
                </div>

                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Token</th>
                                <th>Scopes</th>
                                <th>Status</th>
                                <th>Last Used</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="tokens-table">
                            <tr>
                                <td colspan="6">
                                    <div class="loading">
                                        <div class="spinner"></div>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </main>

    <!-- Create Token Modal -->
    <div class="modal-overlay" id="create-modal">
        <div class="modal">
            <div class="modal-header">
                <h3 class="modal-title">Create New Token</h3>
                <button class="modal-close" onclick="closeCreateModal()">✕</button>
            </div>
            <div class="modal-body">
                <form id="create-token-form">
                    <div class="form-group">
                        <label class="form-label">Token Name</label>
                        <input type="text" class="form-input" id="token-name" placeholder="My Application" required>
                        <p class="form-hint">A friendly name to identify this token</p>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Expiration (Days)</label>
                        <input type="number" class="form-input" id="token-expiry" placeholder="90" min="1" max="365">
                        <p class="form-hint">Leave empty for no expiration</p>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Rate Limit (requests/hour)</label>
                        <input type="number" class="form-input" id="token-ratelimit" placeholder="1000" min="1" max="100000">
                        <p class="form-hint">Maximum API requests per hour</p>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Scopes (Permissions)</label>
                        <div class="checkbox-group">
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-email-send" value="email:send" checked>
                                <label for="scope-email-send">Send Emails</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-email-read" value="email:read">
                                <label for="scope-email-read">Read Emails</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-templates-read" value="templates:read">
                                <label for="scope-templates-read">Read Templates</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-templates-write" value="templates:write">
                                <label for="scope-templates-write">Write Templates</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-analytics-read" value="analytics:read">
                                <label for="scope-analytics-read">View Analytics</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-webhooks-manage" value="webhooks:manage">
                                <label for="scope-webhooks-manage">Manage Webhooks</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-batch-send" value="batch:send">
                                <label for="scope-batch-send">Batch Send</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="scope-api-keys-manage" value="api-keys:manage">
                                <label for="scope-api-keys-manage">Manage API Keys</label>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeCreateModal()">Cancel</button>
                <button class="btn btn-primary" onclick="createToken()">
                    <span>✨</span> Create Token
                </button>
            </div>
        </div>
    </div>

    <!-- Token Created Modal -->
    <div class="modal-overlay" id="token-created-modal">
        <div class="modal">
            <div class="modal-header">
                <h3 class="modal-title">🎉 Token Created Successfully!</h3>
                <button class="modal-close" onclick="closeTokenCreatedModal()">✕</button>
            </div>
            <div class="modal-body">
                <div class="token-display">
                    <div class="token-display-header">
                        <span>Your API Token</span>
                        <button class="btn btn-secondary btn-sm" onclick="copyToken()">
                            <span>📋</span> Copy
                        </button>
                    </div>
                    <div class="token-display-value" id="new-token-value">
                        <!-- Token will be inserted here -->
                    </div>
                </div>

                <div class="token-warning">
                    <span class="token-warning-icon">⚠️</span>
                    <div class="token-warning-text">
                        <strong>Important:</strong> Copy this token now! It will only be shown once and cannot be retrieved later.
                        Store it securely.
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-primary" onclick="closeTokenCreatedModal()">
                    I've Saved My Token
                </button>
            </div>
        </div>
    </div>

    <!-- Confirm Delete Modal -->
    <div class="modal-overlay" id="delete-modal">
        <div class="modal">
            <div class="modal-header">
                <h3 class="modal-title">⚠️ Revoke Token</h3>
                <button class="modal-close" onclick="closeDeleteModal()">✕</button>
            </div>
            <div class="modal-body">
                <p>Are you sure you want to revoke this token?</p>
                <p style="margin-top: 1rem; color: var(--text-muted);">
                    Token: <strong id="delete-token-name"></strong>
                </p>
                <p style="margin-top: 0.5rem; color: var(--danger); font-size: 0.875rem;">
                    This action will immediately stop all API access using this token.
                </p>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeDeleteModal()">Cancel</button>
                <button class="btn btn-danger" onclick="confirmDelete()">
                    <span>🗑️</span> Revoke Token
                </button>
            </div>
        </div>
    </div>

    <!-- Toast Container -->
    <div class="toast-container" id="toast-container"></div>

    <script>
        // State
        let tokens = [];
        let deleteTokenId = null;
        let newTokenValue = null;

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            loadTokens();
            loadStats();
        });

        // API Functions
        async function loadTokens() {
            try {
                const response = await fetch('/tokens');
                const data = await response.json();

                if (data.success) {
                    tokens = data.data.tokens;
                    renderTokens();
                }
            } catch (error) {
                showToast('Failed to load tokens', 'error');
            }
        }

        async function loadStats() {
            // Simulate stats for now
            document.getElementById('stat-total').textContent = '--';
            document.getElementById('stat-active').textContent = '--';
            document.getElementById('stat-requests').textContent = '--';
            document.getElementById('stat-latency').textContent = '--';

            // Update stats after loading tokens
            setTimeout(() => {
                document.getElementById('stat-total').textContent = tokens.length;
                document.getElementById('stat-active').textContent = tokens.filter(t => t.isActive).length;
                document.getElementById('stat-requests').textContent = '1.2K';
                document.getElementById('stat-latency').textContent = '45';
            }, 500);
        }

        function renderTokens() {
            const tbody = document.getElementById('tokens-table');

            if (tokens.length === 0) {
                tbody.innerHTML = \`
                    <tr>
                        <td colspan="6">
                            <div class="empty-state">
                                <div class="empty-state-icon">🔑</div>
                                <h3 class="empty-state-title">No API Tokens</h3>
                                <p class="empty-state-text">Create your first API token to get started</p>
                                <button class="btn btn-primary" onclick="openCreateModal()">
                                    <span>✨</span> Create Token
                                </button>
                            </div>
                        </td>
                    </tr>
                \`;
                return;
            }

            tbody.innerHTML = tokens.map(token => \`
                <tr>
                    <td>
                        <div class="token-name">
                            <div class="token-icon">🔑</div>
                            <span>\${escapeHtml(token.name)}</span>
                        </div>
                    </td>
                    <td>
                        <code class="token-key">\${token.keyPrefix}</code>
                    </td>
                    <td>
                        <div class="scopes-list">
                            \${token.scopes.slice(0, 3).map(s => \`<span class="badge badge-scope">\${s.split(':')[0]}</span>\`).join('')}
                            \${token.scopes.length > 3 ? \`<span class="badge badge-scope">+\${token.scopes.length - 3}</span>\` : ''}
                        </div>
                    </td>
                    <td>
                        <span class="badge \${token.isActive ? 'badge-active' : 'badge-inactive'}">
                            \${token.isActive ? '● Active' : '○ Inactive'}
                        </span>
                    </td>
                    <td>
                        \${token.lastUsedAt ? formatDate(token.lastUsedAt) : 'Never'}
                    </td>
                    <td>
                        <div class="actions">
                            <button class="action-btn" title="View Details" onclick="viewToken('\${token.id}')">
                                👁️
                            </button>
                            <button class="action-btn" title="Rotate Token" onclick="rotateToken('\${token.id}')">
                                🔄
                            </button>
                            <button class="action-btn danger" title="Revoke Token" onclick="openDeleteModal('\${token.id}', '\${escapeHtml(token.name)}')">
                                🗑️
                            </button>
                        </div>
                    </td>
                </tr>
            \`).join('');
        }

        async function createToken() {
            const name = document.getElementById('token-name').value;
            const expiresInDays = document.getElementById('token-expiry').value;
            const rateLimit = document.getElementById('token-ratelimit').value;

            const scopes = Array.from(document.querySelectorAll('.checkbox-item input:checked'))
                .map(el => el.value);

            if (!name) {
                showToast('Please enter a token name', 'warning');
                return;
            }

            if (scopes.length === 0) {
                showToast('Please select at least one scope', 'warning');
                return;
            }

            try {
                const response = await fetch('/tokens', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name,
                        scopes,
                        expiresInDays: expiresInDays ? parseInt(expiresInDays) : undefined,
                        rateLimit: rateLimit ? parseInt(rateLimit) : undefined,
                    }),
                });

                const data = await response.json();

                if (data.success) {
                    newTokenValue = data.data.rawKey;
                    document.getElementById('new-token-value').textContent = newTokenValue;
                    closeCreateModal();
                    document.getElementById('token-created-modal').classList.add('active');
                    loadTokens();
                    loadStats();
                    showToast('Token created successfully!', 'success');
                } else {
                    showToast(data.error?.message || 'Failed to create token', 'error');
                }
            } catch (error) {
                showToast('Failed to create token', 'error');
            }
        }

        async function rotateToken(id) {
            if (!confirm('This will create a new token and deactivate the old one. Continue?')) {
                return;
            }

            try {
                const response = await fetch(\`/tokens/\${id}/rotate\`, {
                    method: 'POST',
                });

                const data = await response.json();

                if (data.success) {
                    newTokenValue = data.data.rawKey;
                    document.getElementById('new-token-value').textContent = newTokenValue;
                    document.getElementById('token-created-modal').classList.add('active');
                    loadTokens();
                    showToast('Token rotated successfully!', 'success');
                } else {
                    showToast(data.error?.message || 'Failed to rotate token', 'error');
                }
            } catch (error) {
                showToast('Failed to rotate token', 'error');
            }
        }

        async function confirmDelete() {
            if (!deleteTokenId) return;

            try {
                const response = await fetch(\`/tokens/\${deleteTokenId}/revoke\`, {
                    method: 'POST',
                });

                const data = await response.json();

                if (data.success) {
                    closeDeleteModal();
                    loadTokens();
                    loadStats();
                    showToast('Token revoked successfully', 'success');
                } else {
                    showToast(data.error?.message || 'Failed to revoke token', 'error');
                }
            } catch (error) {
                showToast('Failed to revoke token', 'error');
            }
        }

        function viewToken(id) {
            window.location.href = \`/dashboard/tokens/\${id}\`;
        }

        // Modal Functions
        function openCreateModal() {
            document.getElementById('create-modal').classList.add('active');
            document.getElementById('token-name').focus();
        }

        function closeCreateModal() {
            document.getElementById('create-modal').classList.remove('active');
            document.getElementById('create-token-form').reset();
        }

        function closeTokenCreatedModal() {
            document.getElementById('token-created-modal').classList.remove('active');
            newTokenValue = null;
        }

        function openDeleteModal(id, name) {
            deleteTokenId = id;
            document.getElementById('delete-token-name').textContent = name;
            document.getElementById('delete-modal').classList.add('active');
        }

        function closeDeleteModal() {
            document.getElementById('delete-modal').classList.remove('active');
            deleteTokenId = null;
        }

        // Utility Functions
        function copyToken() {
            if (newTokenValue) {
                navigator.clipboard.writeText(newTokenValue);
                showToast('Token copied to clipboard!', 'success');
            }
        }

        function refreshTokens() {
            loadTokens();
            loadStats();
            showToast('Refreshed!', 'success');
        }

        function escapeHtml(str) {
            const div = document.createElement('div');
            div.textContent = str;
            return div.innerHTML;
        }

        function formatDate(dateStr) {
            const date = new Date(dateStr);
            const now = new Date();
            const diff = now - date;

            if (diff < 60000) return 'Just now';
            if (diff < 3600000) return \`\${Math.floor(diff / 60000)}m ago\`;
            if (diff < 86400000) return \`\${Math.floor(diff / 3600000)}h ago\`;
            if (diff < 604800000) return \`\${Math.floor(diff / 86400000)}d ago\`;

            return date.toLocaleDateString();
        }

        function showToast(message, type = 'success') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = \`toast toast-\${type}\`;
            toast.innerHTML = \`
                <span>\${type === 'success' ? '✓' : type === 'error' ? '✕' : '!'}</span>
                <span>\${message}</span>
            \`;
            container.appendChild(toast);

            setTimeout(() => {
                toast.style.animation = 'toastSlide 0.3s ease reverse';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeCreateModal();
                closeTokenCreatedModal();
                closeDeleteModal();
            }
        });
    </script>
</body>
</html>
`;

/**
 * GET /dashboard
 * Main dashboard page
 */
dashboard.get('/', async (c) => {
  return c.html(dashboardHTML());
});

/**
 * GET /dashboard/tokens/:id
 * Token detail page
 */
dashboard.get('/tokens/:id', async (c) => {
  const { id } = c.req.param();
  // Return token detail page (simplified for now)
  return c.redirect('/dashboard');
});

export default dashboard;
