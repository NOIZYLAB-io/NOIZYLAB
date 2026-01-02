import React, { useState, useEffect } from 'react';

interface ScanHistory {
  scanId: string;
  timestamp: string;
  boardType: string;
  issuesFound: number;
  status: 'complete' | 'processing' | 'failed';
}

interface UserStats {
  scansRemaining: number;
  totalScans: number;
  subscription: {
    status: string;
    plan: string;
  } | null;
}

export default function Dashboard() {
  const [scans, setScans] = useState<ScanHistory[]>([]);
  const [stats, setStats] = useState<UserStats | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch user data
    const fetchData = async () => {
      try {
        // Mock data for now
        setStats({
          scansRemaining: 7,
          totalScans: 23,
          subscription: null
        });
        
        setScans([
          {
            scanId: 'scan_123',
            timestamp: '2026-01-02T10:30:00Z',
            boardType: 'iPhone 15 Pro MLB',
            issuesFound: 3,
            status: 'complete'
          },
          {
            scanId: 'scan_122',
            timestamp: '2026-01-01T14:20:00Z',
            boardType: 'MacBook M2 Logic',
            issuesFound: 0,
            status: 'complete'
          },
          {
            scanId: 'scan_121',
            timestamp: '2025-12-30T09:15:00Z',
            boardType: 'Unknown',
            issuesFound: 5,
            status: 'complete'
          }
        ]);
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="spinner" />
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <p className="text-gray-400">Manage your scans and subscription</p>
      </header>

      {/* Stats Cards */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <StatCard
          title="Scans Remaining"
          value={stats?.scansRemaining === -1 ? '∞' : stats?.scansRemaining.toString() || '0'}
          subtitle={stats?.scansRemaining === -1 ? 'Unlimited (Pro)' : 'Purchase more in Pricing'}
        />
        <StatCard
          title="Total Scans"
          value={stats?.totalScans.toString() || '0'}
          subtitle="All time"
        />
        <StatCard
          title="Subscription"
          value={stats?.subscription?.plan || 'None'}
          subtitle={stats?.subscription?.status || 'Upgrade to Pro'}
        />
      </div>

      {/* Recent Scans */}
      <section>
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">Recent Scans</h2>
          <a href="/scan" className="btn-primary">
            New Scan
          </a>
        </div>

        <div className="space-y-4">
          {scans.map(scan => (
            <ScanCard key={scan.scanId} scan={scan} />
          ))}
        </div>

        {scans.length === 0 && (
          <div className="text-center py-12 text-gray-400">
            <p>No scans yet. Start your first scan!</p>
          </div>
        )}
      </section>
    </div>
  );
}

function StatCard({ title, value, subtitle }: { title: string; value: string; subtitle: string }) {
  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <p className="text-gray-400 text-sm mb-1">{title}</p>
      <p className="text-3xl font-bold text-green-500">{value}</p>
      <p className="text-gray-500 text-sm mt-1">{subtitle}</p>
    </div>
  );
}

function ScanCard({ scan }: { scan: ScanHistory }) {
  const statusColors = {
    complete: 'bg-green-500/20 text-green-400',
    processing: 'bg-yellow-500/20 text-yellow-400',
    failed: 'bg-red-500/20 text-red-400'
  };

  return (
    <a
      href={`/result/${scan.scanId}`}
      className="block bg-gray-900 border border-gray-800 rounded-xl p-4 hover:border-gray-700 transition-colors"
    >
      <div className="flex justify-between items-start">
        <div>
          <h3 className="font-semibold">{scan.boardType}</h3>
          <p className="text-gray-400 text-sm">
            {new Date(scan.timestamp).toLocaleDateString('en-US', {
              month: 'short',
              day: 'numeric',
              year: 'numeric',
              hour: '2-digit',
              minute: '2-digit'
            })}
          </p>
        </div>
        <div className="text-right">
          <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${statusColors[scan.status]}`}>
            {scan.status}
          </span>
          <p className="text-gray-400 text-sm mt-1">
            {scan.issuesFound} {scan.issuesFound === 1 ? 'issue' : 'issues'}
          </p>
        </div>
      </div>
    </a>
  );
}
