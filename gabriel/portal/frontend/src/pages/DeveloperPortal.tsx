import React, { useState, useEffect } from 'react';

interface APIKey {
  id: string;
  name: string;
  prefix: string;
  permissions: string[];
  rateLimit: number;
  createdAt: string;
  lastUsed?: string;
  expiresAt?: string;
  active: boolean;
}

interface WebhookConfig {
  id: string;
  url: string;
  events: string[];
  active: boolean;
  createdAt: string;
  lastTriggered?: string;
  failureCount: number;
}

export default function DeveloperPortal() {
  const [activeTab, setActiveTab] = useState<'keys' | 'webhooks' | 'docs'>('keys');
  const [apiKeys, setApiKeys] = useState<APIKey[]>([]);
  const [webhooks, setWebhooks] = useState<WebhookConfig[]>([]);
  const [newKeyModal, setNewKeyModal] = useState(false);
  const [newWebhookModal, setNewWebhookModal] = useState(false);
  const [createdKey, setCreatedKey] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [keysRes, webhooksRes] = await Promise.all([
        fetch('/api/keys'),
        fetch('/api/webhooks'),
      ]);
      
      const keysData = await keysRes.json();
      const webhooksData = await webhooksRes.json();
      
      setApiKeys(keysData.keys || []);
      setWebhooks(webhooksData.webhooks || []);
    } catch (error) {
      console.error('Failed to fetch data:', error);
    } finally {
      setLoading(false);
    }
  };

  const createAPIKey = async (name: string, permissions: string[]) => {
    const response = await fetch('/api/keys', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, permissions }),
    });
    
    const data = await response.json();
    setCreatedKey(data.key);
    setApiKeys(prev => [...prev, data.apiKey]);
    setNewKeyModal(false);
  };

  const revokeKey = async (keyId: string) => {
    await fetch(`/api/keys/${keyId}`, { method: 'DELETE' });
    setApiKeys(prev => prev.filter(k => k.id !== keyId));
  };

  const createWebhook = async (url: string, events: string[]) => {
    const response = await fetch('/api/webhooks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url, events }),
    });
    
    const data = await response.json();
    setWebhooks(prev => [...prev, data.webhook]);
    setNewWebhookModal(false);
  };

  const deleteWebhook = async (webhookId: string) => {
    await fetch(`/api/webhooks/${webhookId}`, { method: 'DELETE' });
    setWebhooks(prev => prev.filter(w => w.id !== webhookId));
  };

  const testWebhook = async (webhookId: string) => {
    await fetch(`/api/webhooks/${webhookId}/test`, { method: 'POST' });
    alert('Test webhook sent!');
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-950">
        <div className="animate-spin w-8 h-8 border-2 border-green-500 border-t-transparent rounded-full" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-950 text-white">
      {/* Header */}
      <header className="border-b border-gray-800 p-6">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-2xl font-bold">Developer Portal</h1>
          <p className="text-gray-400 mt-1">API keys, webhooks, and documentation</p>
        </div>
      </header>

      {/* Tabs */}
      <div className="border-b border-gray-800">
        <div className="max-w-6xl mx-auto flex">
          {(['keys', 'webhooks', 'docs'] as const).map(tab => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-6 py-4 font-medium border-b-2 transition-colors ${
                activeTab === tab
                  ? 'border-green-500 text-green-500'
                  : 'border-transparent text-gray-400 hover:text-white'
              }`}
            >
              {tab === 'keys' && '🔑 API Keys'}
              {tab === 'webhooks' && '🔔 Webhooks'}
              {tab === 'docs' && '📚 Documentation'}
            </button>
          ))}
        </div>
      </div>

      {/* Content */}
      <div className="max-w-6xl mx-auto p-6">
        {/* API Keys Tab */}
        {activeTab === 'keys' && (
          <div>
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-xl font-semibold">API Keys</h2>
              <button
                onClick={() => setNewKeyModal(true)}
                className="px-4 py-2 bg-green-500 text-black rounded-lg font-medium"
              >
                + Create Key
              </button>
            </div>

            {/* Created key notice */}
            {createdKey && (
              <div className="mb-6 p-4 bg-green-500/10 border border-green-500 rounded-xl">
                <p className="font-medium text-green-400 mb-2">🔐 New API Key Created</p>
                <p className="text-sm text-gray-400 mb-2">
                  Copy this key now. It won't be shown again.
                </p>
                <code className="block p-3 bg-gray-900 rounded-lg text-sm font-mono break-all">
                  {createdKey}
                </code>
                <button
                  onClick={() => {
                    navigator.clipboard.writeText(createdKey);
                    alert('Copied!');
                  }}
                  className="mt-2 text-green-400 text-sm"
                >
                  📋 Copy to clipboard
                </button>
              </div>
            )}

            {/* Keys list */}
            <div className="space-y-4">
              {apiKeys.map(key => (
                <div
                  key={key.id}
                  className="p-4 bg-gray-900 rounded-xl border border-gray-800"
                >
                  <div className="flex justify-between items-start">
                    <div>
                      <div className="flex items-center gap-3">
                        <h3 className="font-semibold">{key.name}</h3>
                        <span className={`px-2 py-0.5 rounded text-xs ${
                          key.active ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'
                        }`}>
                          {key.active ? 'Active' : 'Revoked'}
                        </span>
                      </div>
                      <p className="text-gray-400 text-sm mt-1">
                        <code className="bg-gray-800 px-2 py-0.5 rounded">{key.prefix}...</code>
                      </p>
                    </div>
                    {key.active && (
                      <button
                        onClick={() => revokeKey(key.id)}
                        className="text-red-400 text-sm hover:text-red-300"
                      >
                        Revoke
                      </button>
                    )}
                  </div>
                  
                  <div className="mt-4 flex flex-wrap gap-2">
                    {key.permissions.map(perm => (
                      <span
                        key={perm}
                        className="px-2 py-1 bg-gray-800 rounded text-xs"
                      >
                        {perm}
                      </span>
                    ))}
                  </div>
                  
                  <div className="mt-4 text-xs text-gray-500 flex gap-4">
                    <span>Created: {new Date(key.createdAt).toLocaleDateString()}</span>
                    {key.lastUsed && (
                      <span>Last used: {new Date(key.lastUsed).toLocaleDateString()}</span>
                    )}
                    <span>Rate limit: {key.rateLimit}/min</span>
                  </div>
                </div>
              ))}
              
              {apiKeys.length === 0 && (
                <p className="text-gray-500 text-center py-12">
                  No API keys yet. Create one to get started.
                </p>
              )}
            </div>
          </div>
        )}

        {/* Webhooks Tab */}
        {activeTab === 'webhooks' && (
          <div>
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-xl font-semibold">Webhooks</h2>
              <button
                onClick={() => setNewWebhookModal(true)}
                className="px-4 py-2 bg-green-500 text-black rounded-lg font-medium"
              >
                + Add Webhook
              </button>
            </div>

            <div className="space-y-4">
              {webhooks.map(webhook => (
                <div
                  key={webhook.id}
                  className="p-4 bg-gray-900 rounded-xl border border-gray-800"
                >
                  <div className="flex justify-between items-start">
                    <div>
                      <p className="font-mono text-sm break-all">{webhook.url}</p>
                      <div className="mt-2 flex flex-wrap gap-2">
                        {webhook.events.map(event => (
                          <span
                            key={event}
                            className="px-2 py-1 bg-blue-500/20 text-blue-400 rounded text-xs"
                          >
                            {event}
                          </span>
                        ))}
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className={`w-2 h-2 rounded-full ${
                        webhook.active ? 'bg-green-500' : 'bg-red-500'
                      }`} />
                      <span className="text-xs text-gray-400">
                        {webhook.active ? 'Active' : 'Disabled'}
                      </span>
                    </div>
                  </div>
                  
                  <div className="mt-4 flex gap-4">
                    <button
                      onClick={() => testWebhook(webhook.id)}
                      className="text-sm text-blue-400 hover:text-blue-300"
                    >
                      Send Test
                    </button>
                    <button
                      onClick={() => deleteWebhook(webhook.id)}
                      className="text-sm text-red-400 hover:text-red-300"
                    >
                      Delete
                    </button>
                  </div>
                  
                  {webhook.failureCount > 0 && (
                    <p className="mt-2 text-xs text-yellow-400">
                      ⚠️ {webhook.failureCount} consecutive failures
                    </p>
                  )}
                </div>
              ))}
              
              {webhooks.length === 0 && (
                <p className="text-gray-500 text-center py-12">
                  No webhooks configured. Add one to receive notifications.
                </p>
              )}
            </div>
          </div>
        )}

        {/* Docs Tab */}
        {activeTab === 'docs' && (
          <div className="prose prose-invert max-w-none">
            <h2>API Documentation</h2>
            
            <h3>Authentication</h3>
            <p>All API requests require authentication using an API key.</p>
            <pre className="bg-gray-900 p-4 rounded-xl overflow-x-auto">
{`curl -X POST https://api.gabriel.noizylab.com/scan \\
  -H "Authorization: Bearer gab_live_xxxxx" \\
  -F "image=@board.jpg"`}
            </pre>

            <h3>Endpoints</h3>
            
            <h4>POST /api/scan</h4>
            <p>Analyze a circuit board image.</p>
            <pre className="bg-gray-900 p-4 rounded-xl overflow-x-auto">
{`{
  "scanId": "scan_123456",
  "status": "processing",
  "estimatedTime": "10-30 seconds"
}`}
            </pre>

            <h4>GET /api/scan/:id</h4>
            <p>Get scan results.</p>
            <pre className="bg-gray-900 p-4 rounded-xl overflow-x-auto">
{`{
  "scanId": "scan_123456",
  "status": "complete",
  "boardType": "iPhone 13 Pro Logic Board",
  "confidence": 94.5,
  "issues": [
    {
      "component": "U3100",
      "type": "damaged",
      "severity": "critical",
      "description": "IC shows signs of thermal damage",
      "location": { "x": 45.2, "y": 32.1, "width": 5, "height": 3 }
    }
  ]
}`}
            </pre>

            <h3>Webhooks</h3>
            <p>Receive real-time notifications for events:</p>
            <ul>
              <li><code>scan.started</code> - Scan processing began</li>
              <li><code>scan.completed</code> - Scan finished successfully</li>
              <li><code>scan.failed</code> - Scan processing failed</li>
              <li><code>issue.critical</code> - Critical issue detected</li>
              <li><code>credits.low</code> - Low credit balance</li>
            </ul>

            <h4>Webhook Payload</h4>
            <pre className="bg-gray-900 p-4 rounded-xl overflow-x-auto">
{`{
  "event": "scan.completed",
  "timestamp": "2026-01-02T12:00:00Z",
  "data": {
    "scanId": "scan_123456",
    "boardType": "iPhone 13 Pro Logic Board",
    "issuesCount": 3
  }
}`}
            </pre>

            <h4>Verifying Signatures</h4>
            <pre className="bg-gray-900 p-4 rounded-xl overflow-x-auto">
{`// Node.js example
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('base64');
  return signature === expected;
}`}
            </pre>

            <h3>Rate Limits</h3>
            <table className="w-full">
              <thead>
                <tr>
                  <th>Plan</th>
                  <th>Requests/min</th>
                  <th>Scans/month</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Free</td>
                  <td>10</td>
                  <td>5</td>
                </tr>
                <tr>
                  <td>Basic</td>
                  <td>60</td>
                  <td>100</td>
                </tr>
                <tr>
                  <td>Pro</td>
                  <td>300</td>
                  <td>Unlimited</td>
                </tr>
              </tbody>
            </table>

            <h3>SDKs</h3>
            <p>Official SDKs coming soon:</p>
            <ul>
              <li>JavaScript/TypeScript</li>
              <li>Python</li>
              <li>Go</li>
            </ul>
          </div>
        )}
      </div>

      {/* Create Key Modal */}
      {newKeyModal && (
        <CreateKeyModal
          onClose={() => setNewKeyModal(false)}
          onCreate={createAPIKey}
        />
      )}

      {/* Create Webhook Modal */}
      {newWebhookModal && (
        <CreateWebhookModal
          onClose={() => setNewWebhookModal(false)}
          onCreate={createWebhook}
        />
      )}
    </div>
  );
}

function CreateKeyModal({
  onClose,
  onCreate,
}: {
  onClose: () => void;
  onCreate: (name: string, permissions: string[]) => void;
}) {
  const [name, setName] = useState('');
  const [permissions, setPermissions] = useState<string[]>(['scan:read', 'scan:write']);

  const allPermissions = [
    { id: 'scan:read', label: 'Read Scans', description: 'View scan results' },
    { id: 'scan:write', label: 'Write Scans', description: 'Create new scans' },
    { id: 'reference:read', label: 'Read References', description: 'View golden references' },
    { id: 'reference:write', label: 'Write References', description: 'Upload references' },
    { id: 'webhook:manage', label: 'Manage Webhooks', description: 'Create/delete webhooks' },
    { id: 'analytics:read', label: 'Read Analytics', description: 'View usage analytics' },
  ];

  const togglePermission = (id: string) => {
    setPermissions(prev =>
      prev.includes(id)
        ? prev.filter(p => p !== id)
        : [...prev, id]
    );
  };

  return (
    <div className="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-50">
      <div className="bg-gray-900 rounded-2xl max-w-md w-full p-6">
        <h3 className="text-xl font-semibold mb-4">Create API Key</h3>
        
        <div className="space-y-4">
          <div>
            <label className="block text-sm text-gray-400 mb-1">Key Name</label>
            <input
              type="text"
              value={name}
              onChange={e => setName(e.target.value)}
              placeholder="e.g., Production Server"
              className="w-full px-4 py-2 bg-gray-800 border border-gray-700 rounded-lg"
            />
          </div>
          
          <div>
            <label className="block text-sm text-gray-400 mb-2">Permissions</label>
            <div className="space-y-2">
              {allPermissions.map(perm => (
                <label
                  key={perm.id}
                  className="flex items-start gap-3 p-3 bg-gray-800 rounded-lg cursor-pointer"
                >
                  <input
                    type="checkbox"
                    checked={permissions.includes(perm.id)}
                    onChange={() => togglePermission(perm.id)}
                    className="mt-1"
                  />
                  <div>
                    <p className="font-medium">{perm.label}</p>
                    <p className="text-sm text-gray-400">{perm.description}</p>
                  </div>
                </label>
              ))}
            </div>
          </div>
        </div>
        
        <div className="flex gap-3 mt-6">
          <button
            onClick={onClose}
            className="flex-1 py-2 bg-gray-800 rounded-lg"
          >
            Cancel
          </button>
          <button
            onClick={() => onCreate(name, permissions)}
            disabled={!name || permissions.length === 0}
            className="flex-1 py-2 bg-green-500 text-black rounded-lg font-medium disabled:opacity-50"
          >
            Create Key
          </button>
        </div>
      </div>
    </div>
  );
}

function CreateWebhookModal({
  onClose,
  onCreate,
}: {
  onClose: () => void;
  onCreate: (url: string, events: string[]) => void;
}) {
  const [url, setUrl] = useState('');
  const [events, setEvents] = useState<string[]>(['scan.completed']);

  const allEvents = [
    { id: 'scan.started', label: 'Scan Started' },
    { id: 'scan.completed', label: 'Scan Completed' },
    { id: 'scan.failed', label: 'Scan Failed' },
    { id: 'issue.critical', label: 'Critical Issue Detected' },
    { id: 'credits.low', label: 'Low Credits Warning' },
  ];

  const toggleEvent = (id: string) => {
    setEvents(prev =>
      prev.includes(id)
        ? prev.filter(e => e !== id)
        : [...prev, id]
    );
  };

  return (
    <div className="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-50">
      <div className="bg-gray-900 rounded-2xl max-w-md w-full p-6">
        <h3 className="text-xl font-semibold mb-4">Add Webhook</h3>
        
        <div className="space-y-4">
          <div>
            <label className="block text-sm text-gray-400 mb-1">Endpoint URL</label>
            <input
              type="url"
              value={url}
              onChange={e => setUrl(e.target.value)}
              placeholder="https://your-server.com/webhook"
              className="w-full px-4 py-2 bg-gray-800 border border-gray-700 rounded-lg"
            />
          </div>
          
          <div>
            <label className="block text-sm text-gray-400 mb-2">Events</label>
            <div className="space-y-2">
              {allEvents.map(event => (
                <label
                  key={event.id}
                  className="flex items-center gap-3 p-3 bg-gray-800 rounded-lg cursor-pointer"
                >
                  <input
                    type="checkbox"
                    checked={events.includes(event.id)}
                    onChange={() => toggleEvent(event.id)}
                  />
                  <span>{event.label}</span>
                </label>
              ))}
            </div>
          </div>
        </div>
        
        <div className="flex gap-3 mt-6">
          <button
            onClick={onClose}
            className="flex-1 py-2 bg-gray-800 rounded-lg"
          >
            Cancel
          </button>
          <button
            onClick={() => onCreate(url, events)}
            disabled={!url || events.length === 0}
            className="flex-1 py-2 bg-green-500 text-black rounded-lg font-medium disabled:opacity-50"
          >
            Add Webhook
          </button>
        </div>
      </div>
    </div>
  );
}
