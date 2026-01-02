import React, { useState, useEffect } from 'react';

interface DailyMetrics {
  date: string;
  scans: number;
  revenue: number;
  newUsers: number;
  activeUsers: number;
  issuesDetected: number;
}

interface RevenueBreakdown {
  goldenAudit: number;
  legacyKit: number;
  proSubscription: number;
  total: number;
}

interface DashboardData {
  summary: {
    totalScans: number;
    totalRevenue: number;
    avgConfidence: number;
    activeUsers: number;
  };
  daily: DailyMetrics[];
  revenueBreakdown: RevenueBreakdown;
  topBoards: { name: string; count: number }[];
  hourlyHeatmap: number[];
}

export default function AdminDashboard() {
  const [data, setData] = useState<DashboardData | null>(null);
  const [range, setRange] = useState<'today' | '7d' | '30d' | '90d'>('7d');
  const [loading, setLoading] = useState(true);
  const [realtime, setRealtime] = useState({
    scansLastHour: 0,
    activeNow: 0,
    revenueToday: 0
  });

  useEffect(() => {
    fetchDashboard();
    const interval = setInterval(fetchRealtime, 10000); // Update every 10s
    return () => clearInterval(interval);
  }, [range]);

  const fetchDashboard = async () => {
    setLoading(true);
    try {
      const response = await fetch(`/api/admin/metrics?range=${range}`);
      const data = await response.json();
      setData(data);
    } catch (error) {
      console.error('Failed to fetch metrics:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchRealtime = async () => {
    try {
      const response = await fetch('/api/admin/realtime');
      const data = await response.json();
      setRealtime(data);
    } catch (error) {
      console.error('Failed to fetch realtime:', error);
    }
  };

  if (loading || !data) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="spinner" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-950 text-white p-8">
      {/* Header */}
      <header className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold">Admin Dashboard</h1>
          <p className="text-gray-400">NoizyLab Analytics</p>
        </div>
        <div className="flex gap-2">
          {(['today', '7d', '30d', '90d'] as const).map((r) => (
            <button
              key={r}
              onClick={() => setRange(r)}
              className={`px-4 py-2 rounded-lg ${
                range === r ? 'bg-green-500 text-black' : 'bg-gray-800'
              }`}
            >
              {r === 'today' ? 'Today' : r}
            </button>
          ))}
        </div>
      </header>

      {/* Real-time Stats */}
      <div className="grid grid-cols-4 gap-4 mb-8">
        <RealtimeCard
          label="Scans/Hour"
          value={realtime.scansLastHour}
          trend={+5}
          icon="📊"
        />
        <RealtimeCard
          label="Active Now"
          value={realtime.activeNow}
          icon="👥"
          pulse
        />
        <RealtimeCard
          label="Revenue Today"
          value={`$${(realtime.revenueToday / 100).toFixed(2)}`}
          trend={+12}
          icon="💰"
        />
        <RealtimeCard
          label="Total Users"
          value={data.summary.activeUsers}
          icon="🌟"
        />
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-4 gap-4 mb-8">
        <MetricCard
          title="Total Scans"
          value={data.summary.totalScans.toLocaleString()}
          subtitle={`${range} period`}
        />
        <MetricCard
          title="Total Revenue"
          value={`$${(data.summary.totalRevenue / 100).toLocaleString()}`}
          subtitle={`${range} period`}
        />
        <MetricCard
          title="Issues Detected"
          value={data.daily.reduce((sum, d) => sum + d.issuesDetected, 0).toLocaleString()}
          subtitle="Components flagged"
        />
        <MetricCard
          title="Active Users"
          value={data.summary.activeUsers.toLocaleString()}
          subtitle="Unique users"
        />
      </div>

      <div className="grid grid-cols-3 gap-8 mb-8">
        {/* Revenue Breakdown */}
        <div className="bg-gray-900 rounded-xl p-6 border border-gray-800">
          <h3 className="text-lg font-semibold mb-4">Revenue Breakdown</h3>
          <div className="space-y-4">
            <RevenueBar
              label="Golden Audit ($4.99)"
              value={data.revenueBreakdown.goldenAudit}
              total={data.revenueBreakdown.total}
              color="green"
            />
            <RevenueBar
              label="Legacy Kit ($29)"
              value={data.revenueBreakdown.legacyKit}
              total={data.revenueBreakdown.total}
              color="blue"
            />
            <RevenueBar
              label="Pro Subscription ($99)"
              value={data.revenueBreakdown.proSubscription}
              total={data.revenueBreakdown.total}
              color="purple"
            />
          </div>
          <div className="mt-4 pt-4 border-t border-gray-800">
            <div className="flex justify-between">
              <span className="text-gray-400">Total</span>
              <span className="font-bold text-green-500">
                ${(data.revenueBreakdown.total / 100).toLocaleString()}
              </span>
            </div>
          </div>
        </div>

        {/* Top Boards */}
        <div className="bg-gray-900 rounded-xl p-6 border border-gray-800">
          <h3 className="text-lg font-semibold mb-4">Top Board Types</h3>
          <div className="space-y-3">
            {data.topBoards.slice(0, 8).map((board, i) => (
              <div key={board.name} className="flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <span className="text-gray-500 w-6">{i + 1}.</span>
                  <span className="truncate max-w-[150px]">{board.name}</span>
                </div>
                <span className="text-gray-400">{board.count}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Hourly Heatmap */}
        <div className="bg-gray-900 rounded-xl p-6 border border-gray-800">
          <h3 className="text-lg font-semibold mb-4">Activity Heatmap (Today)</h3>
          <div className="grid grid-cols-6 gap-2">
            {data.hourlyHeatmap.map((count, hour) => (
              <div
                key={hour}
                className="aspect-square rounded flex items-center justify-center text-xs"
                style={{
                  backgroundColor: `rgba(34, 197, 94, ${Math.min(count / 10, 1)})`,
                }}
                title={`${hour}:00 - ${count} scans`}
              >
                {hour}
              </div>
            ))}
          </div>
          <div className="mt-4 flex justify-between text-xs text-gray-500">
            <span>Low activity</span>
            <span>High activity</span>
          </div>
        </div>
      </div>

      {/* Daily Chart */}
      <div className="bg-gray-900 rounded-xl p-6 border border-gray-800">
        <h3 className="text-lg font-semibold mb-4">Daily Trends</h3>
        <div className="h-64 flex items-end gap-2">
          {data.daily.map((day) => {
            const maxScans = Math.max(...data.daily.map(d => d.scans));
            const height = maxScans > 0 ? (day.scans / maxScans) * 100 : 0;
            return (
              <div key={day.date} className="flex-1 flex flex-col items-center gap-2">
                <div
                  className="w-full bg-green-500/80 rounded-t transition-all hover:bg-green-500"
                  style={{ height: `${height}%` }}
                  title={`${day.date}: ${day.scans} scans, $${(day.revenue / 100).toFixed(2)}`}
                />
                <span className="text-xs text-gray-500 rotate-45 origin-left">
                  {day.date.slice(5)}
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

function RealtimeCard({ 
  label, 
  value, 
  trend, 
  icon, 
  pulse 
}: { 
  label: string; 
  value: number | string; 
  trend?: number; 
  icon: string;
  pulse?: boolean;
}) {
  return (
    <div className={`bg-gray-900 border border-gray-800 rounded-xl p-4 ${pulse ? 'animate-pulse' : ''}`}>
      <div className="flex justify-between items-start">
        <span className="text-2xl">{icon}</span>
        {trend !== undefined && (
          <span className={`text-xs ${trend >= 0 ? 'text-green-400' : 'text-red-400'}`}>
            {trend >= 0 ? '↑' : '↓'} {Math.abs(trend)}%
          </span>
        )}
      </div>
      <p className="text-2xl font-bold mt-2">{value}</p>
      <p className="text-gray-400 text-sm">{label}</p>
    </div>
  );
}

function MetricCard({ title, value, subtitle }: { title: string; value: string; subtitle: string }) {
  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <p className="text-gray-400 text-sm">{title}</p>
      <p className="text-3xl font-bold mt-1">{value}</p>
      <p className="text-gray-500 text-sm mt-1">{subtitle}</p>
    </div>
  );
}

function RevenueBar({ 
  label, 
  value, 
  total, 
  color 
}: { 
  label: string; 
  value: number; 
  total: number; 
  color: string;
}) {
  const percentage = total > 0 ? (value / total) * 100 : 0;
  const colors = {
    green: 'bg-green-500',
    blue: 'bg-blue-500',
    purple: 'bg-purple-500'
  };
  
  return (
    <div>
      <div className="flex justify-between text-sm mb-1">
        <span className="text-gray-400">{label}</span>
        <span>${(value / 100).toLocaleString()}</span>
      </div>
      <div className="h-2 bg-gray-800 rounded-full overflow-hidden">
        <div
          className={`h-full ${colors[color as keyof typeof colors]} transition-all`}
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
}
