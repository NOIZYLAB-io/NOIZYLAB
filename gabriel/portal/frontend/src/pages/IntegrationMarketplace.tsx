import React, { useState } from 'react';

interface Integration {
  id: string;
  name: string;
  slug: string;
  category: string;
  description: string;
  icon: string;
  status: 'stable' | 'beta' | 'coming_soon';
  pricing: 'free' | 'pro' | 'enterprise';
  connected?: boolean;
  lastSync?: string;
}

const CATEGORIES = [
  { id: 'all', label: 'All', icon: '🔌' },
  { id: 'parts', label: 'Parts Suppliers', icon: '🔧' },
  { id: 'inventory', label: 'Inventory', icon: '📦' },
  { id: 'communication', label: 'Communication', icon: '💬' },
  { id: 'storage', label: 'Cloud Storage', icon: '☁️' },
  { id: 'crm', label: 'CRM', icon: '👥' },
  { id: 'accounting', label: 'Accounting', icon: '💰' },
  { id: 'automation', label: 'Automation', icon: '⚡' },
];

const INTEGRATIONS: Integration[] = [
  // Parts
  { id: '1', name: 'Injured Gadgets', slug: 'injured-gadgets', category: 'parts', description: 'Auto-order replacement parts based on scan results', icon: '🔧', status: 'stable', pricing: 'pro' },
  { id: '2', name: 'iFixit Parts', slug: 'ifixit', category: 'parts', description: 'Search iFixit catalog for compatible parts', icon: '🛠️', status: 'stable', pricing: 'free', connected: true, lastSync: '2 hours ago' },
  { id: '3', name: 'Replacebase', slug: 'replacebase', category: 'parts', description: 'UK/EU parts supplier integration', icon: '📦', status: 'stable', pricing: 'pro' },
  { id: '4', name: 'MobileSentrix', slug: 'mobilesentrix', category: 'parts', description: 'Wholesale parts ordering', icon: '📱', status: 'beta', pricing: 'pro' },
  
  // Inventory
  { id: '5', name: 'RepairShopr', slug: 'repairshopr', category: 'inventory', description: 'Sync repairs, parts, and customers', icon: '🏪', status: 'stable', pricing: 'pro', connected: true, lastSync: '5 mins ago' },
  { id: '6', name: 'RepairDesk', slug: 'repairdesk', category: 'inventory', description: 'Complete POS and inventory sync', icon: '🖥️', status: 'stable', pricing: 'pro' },
  { id: '7', name: 'CellStore', slug: 'cellstore', category: 'inventory', description: 'Cell phone repair shop management', icon: '📊', status: 'beta', pricing: 'pro' },
  
  // Communication
  { id: '8', name: 'Slack', slug: 'slack', category: 'communication', description: 'Get scan notifications in Slack', icon: '💬', status: 'stable', pricing: 'free', connected: true, lastSync: '1 min ago' },
  { id: '9', name: 'Discord', slug: 'discord', category: 'communication', description: 'Send scan results to Discord', icon: '🎮', status: 'stable', pricing: 'free' },
  { id: '10', name: 'Twilio SMS', slug: 'twilio', category: 'communication', description: 'Send SMS updates to customers', icon: '📲', status: 'stable', pricing: 'pro' },
  
  // Storage
  { id: '11', name: 'Google Drive', slug: 'google-drive', category: 'storage', description: 'Backup reports to Drive', icon: '📁', status: 'stable', pricing: 'free' },
  { id: '12', name: 'Dropbox', slug: 'dropbox', category: 'storage', description: 'Sync reports and images', icon: '💧', status: 'stable', pricing: 'free' },
  
  // CRM
  { id: '13', name: 'HubSpot', slug: 'hubspot', category: 'crm', description: 'Sync customer data and history', icon: '🎯', status: 'beta', pricing: 'enterprise' },
  { id: '14', name: 'Salesforce', slug: 'salesforce', category: 'crm', description: 'Enterprise CRM integration', icon: '☁️', status: 'coming_soon', pricing: 'enterprise' },
  
  // Accounting
  { id: '15', name: 'QuickBooks', slug: 'quickbooks', category: 'accounting', description: 'Auto-create invoices', icon: '💰', status: 'stable', pricing: 'pro' },
  { id: '16', name: 'Xero', slug: 'xero', category: 'accounting', description: 'Accounting and invoicing', icon: '📈', status: 'beta', pricing: 'pro' },
  
  // Automation
  { id: '17', name: 'Zapier', slug: 'zapier', category: 'automation', description: 'Connect to 5000+ apps', icon: '⚡', status: 'stable', pricing: 'pro' },
  { id: '18', name: 'Make', slug: 'make', category: 'automation', description: 'Visual automation workflows', icon: '🔄', status: 'stable', pricing: 'pro' },
  { id: '19', name: 'n8n', slug: 'n8n', category: 'automation', description: 'Self-hosted automation', icon: '🔗', status: 'stable', pricing: 'free' },
];

const IntegrationCard: React.FC<{
  integration: Integration;
  onConnect: (slug: string) => void;
  onDisconnect: (slug: string) => void;
}> = ({ integration, onConnect, onDisconnect }) => {
  const statusColors = {
    stable: 'bg-green-500/20 text-green-400',
    beta: 'bg-amber-500/20 text-amber-400',
    coming_soon: 'bg-slate-500/20 text-slate-400',
  };

  const pricingBadges = {
    free: { bg: 'bg-emerald-500/20', text: 'text-emerald-400', label: 'Free' },
    pro: { bg: 'bg-blue-500/20', text: 'text-blue-400', label: 'Pro' },
    enterprise: { bg: 'bg-purple-500/20', text: 'text-purple-400', label: 'Enterprise' },
  };

  const isComingSoon = integration.status === 'coming_soon';

  return (
    <div className={`bg-slate-800 rounded-xl p-6 border border-slate-700 hover:border-amber-500/50 transition ${isComingSoon ? 'opacity-60' : ''}`}>
      <div className="flex justify-between items-start mb-4">
        <div className="flex items-center gap-3">
          <div className="text-3xl">{integration.icon}</div>
          <div>
            <h3 className="font-semibold text-lg">{integration.name}</h3>
            <div className="flex gap-2 mt-1">
              <span className={`px-2 py-0.5 rounded text-xs ${statusColors[integration.status]}`}>
                {integration.status === 'coming_soon' ? 'Coming Soon' : integration.status.toUpperCase()}
              </span>
              <span className={`px-2 py-0.5 rounded text-xs ${pricingBadges[integration.pricing].bg} ${pricingBadges[integration.pricing].text}`}>
                {pricingBadges[integration.pricing].label}
              </span>
            </div>
          </div>
        </div>
        
        {integration.connected && (
          <div className="flex items-center gap-1 text-green-400 text-sm">
            <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
            Connected
          </div>
        )}
      </div>

      <p className="text-slate-400 text-sm mb-4">{integration.description}</p>

      {integration.connected && integration.lastSync && (
        <p className="text-slate-500 text-xs mb-4">Last sync: {integration.lastSync}</p>
      )}

      {isComingSoon ? (
        <button className="w-full py-2 bg-slate-700 text-slate-400 rounded-lg cursor-not-allowed">
          Coming Soon
        </button>
      ) : integration.connected ? (
        <div className="flex gap-2">
          <button className="flex-1 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg transition text-sm">
            Configure
          </button>
          <button 
            onClick={() => onDisconnect(integration.slug)}
            className="px-4 py-2 bg-red-500/20 text-red-400 hover:bg-red-500/30 rounded-lg transition text-sm"
          >
            Disconnect
          </button>
        </div>
      ) : (
        <button 
          onClick={() => onConnect(integration.slug)}
          className="w-full py-2 bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold rounded-lg transition"
        >
          Connect
        </button>
      )}
    </div>
  );
};

const IntegrationMarketplace: React.FC = () => {
  const [activeCategory, setActiveCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [connecting, setConnecting] = useState<string | null>(null);

  const filteredIntegrations = INTEGRATIONS.filter(int => {
    const matchesCategory = activeCategory === 'all' || int.category === activeCategory;
    const matchesSearch = int.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         int.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const connectedCount = INTEGRATIONS.filter(i => i.connected).length;

  const handleConnect = async (slug: string) => {
    setConnecting(slug);
    // API call would redirect to OAuth
    try {
      const response = await fetch(`/api/integrations/${slug}/connect`, {
        method: 'POST',
      });
      const data = await response.json();
      if (data.authUrl) {
        window.location.href = data.authUrl;
      }
    } catch (error) {
      console.error('Connect failed:', error);
    }
    setConnecting(null);
  };

  const handleDisconnect = async (slug: string) => {
    if (!confirm('Are you sure you want to disconnect this integration?')) return;
    try {
      await fetch(`/api/integrations/${slug}`, {
        method: 'DELETE',
      });
      // Would refresh list in real app
    } catch (error) {
      console.error('Disconnect failed:', error);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      {/* Header */}
      <header className="border-b border-slate-700 bg-slate-800/50 backdrop-blur sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div>
            <h1 className="text-2xl font-bold text-amber-500">Integrations</h1>
            <p className="text-slate-400">{connectedCount} of {INTEGRATIONS.length} connected</p>
          </div>
          <div className="relative">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search integrations..."
              className="w-64 px-4 py-2 pl-10 bg-slate-700 border border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500"
            />
            <svg className="w-5 h-5 absolute left-3 top-2.5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        {/* Categories */}
        <div className="flex gap-2 overflow-x-auto pb-4 mb-8 scrollbar-hide">
          {CATEGORIES.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setActiveCategory(cat.id)}
              className={`px-4 py-2 rounded-lg flex items-center gap-2 whitespace-nowrap transition ${
                activeCategory === cat.id
                  ? 'bg-amber-500 text-slate-900 font-semibold'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <span>{cat.icon}</span>
              {cat.label}
            </button>
          ))}
        </div>

        {/* Stats Bar */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Available</p>
            <p className="text-2xl font-bold">{INTEGRATIONS.length}</p>
          </div>
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Connected</p>
            <p className="text-2xl font-bold text-green-400">{connectedCount}</p>
          </div>
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Free</p>
            <p className="text-2xl font-bold">{INTEGRATIONS.filter(i => i.pricing === 'free').length}</p>
          </div>
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Coming Soon</p>
            <p className="text-2xl font-bold text-slate-400">{INTEGRATIONS.filter(i => i.status === 'coming_soon').length}</p>
          </div>
        </div>

        {/* Integration Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredIntegrations.map((integration) => (
            <IntegrationCard
              key={integration.id}
              integration={integration}
              onConnect={handleConnect}
              onDisconnect={handleDisconnect}
            />
          ))}
        </div>

        {filteredIntegrations.length === 0 && (
          <div className="text-center py-16">
            <div className="text-6xl mb-4">🔍</div>
            <h3 className="text-xl font-semibold mb-2">No integrations found</h3>
            <p className="text-slate-400">Try a different search term or category</p>
          </div>
        )}

        {/* Request Integration CTA */}
        <div className="mt-12 bg-gradient-to-r from-amber-500/10 to-orange-500/10 rounded-xl p-8 text-center">
          <h3 className="text-2xl font-bold mb-2">Missing an integration?</h3>
          <p className="text-slate-400 mb-4">
            Let us know what tools you use and we'll add them to our roadmap.
          </p>
          <button className="px-6 py-3 bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold rounded-lg transition">
            Request Integration
          </button>
        </div>
      </main>
    </div>
  );
};

export default IntegrationMarketplace;
