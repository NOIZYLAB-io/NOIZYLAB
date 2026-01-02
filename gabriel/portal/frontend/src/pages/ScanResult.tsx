import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

interface Component {
  id: string;
  type: string;
  position: { x: number; y: number };
  solder_quality: number;
  anomalies: string[];
}

interface Issue {
  component: string;
  type: 'MISSING' | 'WRONG_VALUE' | 'SOLDER_DEFECT' | 'UNEXPECTED';
  severity: 'HIGH' | 'MEDIUM' | 'LOW';
  expected?: string;
  detected?: string;
  confidence?: number;
}

interface RepairStep {
  order: number;
  action: string;
  tools: string[];
  technique: string;
  warnings: string[];
}

interface ScanResult {
  scanId: string;
  timestamp: string;
  boardType: string;
  analysis: {
    components: Component[];
    confidence: number;
  };
  comparison: {
    issues: Issue[];
    matchedCount: number;
  } | null;
  repairPlan: {
    diagnosis: string;
    difficulty: string;
    estimated_time: string;
    steps: RepairStep[];
    confidence: number;
  } | null;
}

export default function ScanResult() {
  const { scanId } = useParams<{ scanId: string }>();
  const [result, setResult] = useState<ScanResult | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'overview' | 'issues' | 'repair'>('overview');

  useEffect(() => {
    const fetchResult = async () => {
      try {
        const response = await fetch(`/api/scan/${scanId}`);
        const data = await response.json();
        setResult(data);
      } catch (error) {
        console.error('Failed to fetch scan result:', error);
      } finally {
        setLoading(false);
      }
    };

    if (scanId) {
      fetchResult();
    }
  }, [scanId]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="spinner" />
      </div>
    );
  }

  if (!result) {
    return (
      <div className="container mx-auto px-4 py-16 text-center">
        <h1 className="text-2xl font-bold mb-4">Scan Not Found</h1>
        <p className="text-gray-400 mb-8">This scan may have expired or doesn't exist.</p>
        <a href="/scan" className="btn-primary">New Scan</a>
      </div>
    );
  }

  const issueCount = result.comparison?.issues.length || 0;
  const highSeverity = result.comparison?.issues.filter(i => i.severity === 'HIGH').length || 0;

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Header */}
      <header className="mb-8">
        <div className="flex justify-between items-start">
          <div>
            <h1 className="text-3xl font-bold">Scan Results</h1>
            <p className="text-gray-400">
              {result.boardType} • {new Date(result.timestamp).toLocaleString()}
            </p>
          </div>
          <div className="flex gap-4">
            <a href={`/api/report/${scanId}`} className="btn-secondary" target="_blank" rel="noopener noreferrer">
              Download PDF
            </a>
            <a href="/scan" className="btn-primary">New Scan</a>
          </div>
        </div>
      </header>

      {/* Summary Cards */}
      <div className="grid md:grid-cols-4 gap-4 mb-8">
        <SummaryCard
          title="Components"
          value={result.analysis.components.length.toString()}
          status="neutral"
        />
        <SummaryCard
          title="Issues Found"
          value={issueCount.toString()}
          status={issueCount === 0 ? 'good' : issueCount > 3 ? 'bad' : 'warning'}
        />
        <SummaryCard
          title="High Severity"
          value={highSeverity.toString()}
          status={highSeverity === 0 ? 'good' : 'bad'}
        />
        <SummaryCard
          title="Confidence"
          value={`${(result.analysis.confidence * 100).toFixed(0)}%`}
          status={result.analysis.confidence > 0.8 ? 'good' : 'warning'}
        />
      </div>

      {/* Tabs */}
      <div className="flex gap-4 mb-6 border-b border-gray-800">
        <TabButton active={activeTab === 'overview'} onClick={() => setActiveTab('overview')}>
          Overview
        </TabButton>
        <TabButton active={activeTab === 'issues'} onClick={() => setActiveTab('issues')}>
          Issues ({issueCount})
        </TabButton>
        <TabButton active={activeTab === 'repair'} onClick={() => setActiveTab('repair')}>
          Repair Plan
        </TabButton>
      </div>

      {/* Tab Content */}
      {activeTab === 'overview' && (
        <OverviewTab result={result} />
      )}

      {activeTab === 'issues' && (
        <IssuesTab issues={result.comparison?.issues || []} />
      )}

      {activeTab === 'repair' && (
        <RepairTab plan={result.repairPlan} />
      )}
    </div>
  );
}

function SummaryCard({ title, value, status }: { title: string; value: string; status: 'good' | 'warning' | 'bad' | 'neutral' }) {
  const colors = {
    good: 'text-green-500',
    warning: 'text-yellow-500',
    bad: 'text-red-500',
    neutral: 'text-blue-500'
  };

  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-4">
      <p className="text-gray-400 text-sm">{title}</p>
      <p className={`text-2xl font-bold ${colors[status]}`}>{value}</p>
    </div>
  );
}

function TabButton({ active, onClick, children }: { active: boolean; onClick: () => void; children: React.ReactNode }) {
  return (
    <button
      onClick={onClick}
      className={`px-4 py-2 font-medium transition-colors ${
        active
          ? 'text-green-500 border-b-2 border-green-500'
          : 'text-gray-400 hover:text-white'
      }`}
    >
      {children}
    </button>
  );
}

function OverviewTab({ result }: { result: ScanResult }) {
  return (
    <div className="space-y-6">
      <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <h3 className="font-semibold mb-4">Component Summary</h3>
        <div className="grid md:grid-cols-3 gap-4">
          {Object.entries(
            result.analysis.components.reduce((acc, c) => {
              acc[c.type] = (acc[c.type] || 0) + 1;
              return acc;
            }, {} as Record<string, number>)
          ).map(([type, count]) => (
            <div key={type} className="flex justify-between">
              <span className="text-gray-400 capitalize">{type}</span>
              <span className="font-mono">{count}</span>
            </div>
          ))}
        </div>
      </div>

      {result.repairPlan && (
        <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
          <h3 className="font-semibold mb-4">Quick Diagnosis</h3>
          <p className="text-gray-300">{result.repairPlan.diagnosis}</p>
          <div className="flex gap-4 mt-4">
            <span className="text-gray-400">
              Difficulty: <span className="text-white capitalize">{result.repairPlan.difficulty}</span>
            </span>
            <span className="text-gray-400">
              Est. Time: <span className="text-white">{result.repairPlan.estimated_time}</span>
            </span>
          </div>
        </div>
      )}
    </div>
  );
}

function IssuesTab({ issues }: { issues: Issue[] }) {
  if (issues.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-6xl mb-4">✅</div>
        <h3 className="text-xl font-semibold mb-2">No Issues Found</h3>
        <p className="text-gray-400">Your board looks good!</p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {issues.map((issue, index) => (
        <IssueCard key={index} issue={issue} />
      ))}
    </div>
  );
}

function IssueCard({ issue }: { issue: Issue }) {
  const severityColors = {
    HIGH: 'bg-red-500/20 text-red-400 border-red-500/30',
    MEDIUM: 'bg-yellow-500/20 text-yellow-400 border-yellow-500/30',
    LOW: 'bg-blue-500/20 text-blue-400 border-blue-500/30'
  };

  const typeLabels = {
    MISSING: 'Missing Component',
    WRONG_VALUE: 'Wrong Value',
    SOLDER_DEFECT: 'Solder Defect',
    UNEXPECTED: 'Unexpected Component'
  };

  return (
    <div className={`border rounded-xl p-4 ${severityColors[issue.severity]}`}>
      <div className="flex justify-between items-start">
        <div>
          <h4 className="font-semibold">{issue.component}</h4>
          <p className="text-sm opacity-80">{typeLabels[issue.type]}</p>
        </div>
        <span className="text-xs font-medium px-2 py-1 rounded bg-black/20">
          {issue.severity}
        </span>
      </div>
      {issue.expected && (
        <p className="text-sm mt-2">
          Expected: <span className="font-mono">{issue.expected}</span>
        </p>
      )}
      {issue.detected && (
        <p className="text-sm">
          Detected: <span className="font-mono">{issue.detected}</span>
        </p>
      )}
    </div>
  );
}

function RepairTab({ plan }: { plan: ScanResult['repairPlan'] }) {
  if (!plan || plan.steps.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-6xl mb-4">🛠️</div>
        <h3 className="text-xl font-semibold mb-2">No Repairs Needed</h3>
        <p className="text-gray-400">Your board is in good condition.</p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {plan.steps.map((step, index) => (
        <div key={index} className="bg-gray-900 border border-gray-800 rounded-xl p-4">
          <div className="flex gap-4">
            <div className="w-8 h-8 bg-green-500 text-black rounded-full flex items-center justify-center font-bold flex-shrink-0">
              {step.order}
            </div>
            <div className="flex-1">
              <h4 className="font-semibold">{step.action}</h4>
              <p className="text-gray-400 text-sm mt-1">{step.technique}</p>
              
              {step.tools.length > 0 && (
                <div className="flex gap-2 mt-2 flex-wrap">
                  {step.tools.map((tool, i) => (
                    <span key={i} className="text-xs bg-gray-800 px-2 py-1 rounded">
                      {tool}
                    </span>
                  ))}
                </div>
              )}
              
              {step.warnings.length > 0 && (
                <div className="mt-2 text-yellow-400 text-sm">
                  ⚠️ {step.warnings.join(', ')}
                </div>
              )}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
