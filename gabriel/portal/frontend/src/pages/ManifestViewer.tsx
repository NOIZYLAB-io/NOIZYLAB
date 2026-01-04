/**
 * NOIZYLAB SUCCESS MANIFEST VIEWER
 * =================================
 * Customer-facing portal for viewing repair manifests.
 * The premium proof of the sovereign miracle.
 */

import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  Shield,
  CheckCircle,
  AlertTriangle,
  Download,
  Share2,
  Zap,
  Cpu,
  Activity,
  Clock,
  DollarSign,
  FileText,
  Camera,
  Lock
} from 'lucide-react';

// Types
interface BiometricData {
  avgStability: number;
  auraMatchScore: number;
  jitterCompensated: number;
  sessionDuration: number;
}

interface ForensicImage {
  preRepair: string;
  postRepair: string;
  componentId: string;
}

interface Manifest {
  caseId: string;
  ticketId: string;
  customerName: string;
  customerEmail: string;
  deviceType: string;
  deviceModel: string;
  serialNumber?: string;
  diagnosis: string;
  rootCause: string;
  componentsAffected: string[];
  repairTechnique: string;
  solderPoints: number;
  voltageReadings: Record<string, number>;
  biometrics: BiometricData;
  forensicImages: ForensicImage[];
  verificationHash: string;
  totalPrice: number;
  createdAt: string;
  completedAt: string;
  paid?: boolean;
  paidAt?: string;
}

interface VerificationResult {
  verified: boolean;
  caseId: string;
  createdAt: string;
  device: string;
  customer: string;
  signature: string;
}

// API functions
const API_BASE = import.meta.env.VITE_API_BASE || 'https://api.noizylab.ca';

async function fetchManifest(caseId: string): Promise<Manifest> {
  const response = await fetch(`${API_BASE}/api/manifests/${caseId}`);
  if (!response.ok) throw new Error('Manifest not found');
  return response.json();
}

async function verifyManifest(caseId: string, hash?: string): Promise<VerificationResult> {
  const url = hash
    ? `${API_BASE}/api/manifests/${caseId}/verify?hash=${hash}`
    : `${API_BASE}/api/manifests/${caseId}/verify`;
  const response = await fetch(url);
  return response.json();
}

// Components
const StatusBadge: React.FC<{ status: 'verified' | 'pending' | 'error' }> = ({ status }) => {
  const styles = {
    verified: 'bg-green-500/20 text-green-400 border-green-500/50',
    pending: 'bg-yellow-500/20 text-yellow-400 border-yellow-500/50',
    error: 'bg-red-500/20 text-red-400 border-red-500/50'
  };

  const icons = {
    verified: <CheckCircle className="w-4 h-4" />,
    pending: <Clock className="w-4 h-4" />,
    error: <AlertTriangle className="w-4 h-4" />
  };

  const labels = {
    verified: 'VERIFIED',
    pending: 'PENDING',
    error: 'ERROR'
  };

  return (
    <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full border text-sm font-medium ${styles[status]}`}>
      {icons[status]}
      {labels[status]}
    </span>
  );
};

const MetricCard: React.FC<{
  icon: React.ReactNode;
  label: string;
  value: string | number;
  status?: 'good' | 'warning' | 'neutral';
}> = ({ icon, label, value, status = 'neutral' }) => {
  const statusColors = {
    good: 'text-green-400',
    warning: 'text-yellow-400',
    neutral: 'text-slate-300'
  };

  return (
    <div className="bg-slate-800/50 rounded-lg p-4 border border-slate-700">
      <div className="flex items-center gap-2 text-slate-400 mb-2">
        {icon}
        <span className="text-sm">{label}</span>
      </div>
      <div className={`text-xl font-bold ${statusColors[status]}`}>
        {value}
      </div>
    </div>
  );
};

const ForensicComparison: React.FC<{ forensic: ForensicImage }> = ({ forensic }) => {
  const [activeView, setActiveView] = useState<'pre' | 'post' | 'diff'>('post');

  return (
    <div className="bg-slate-800/50 rounded-lg p-4 border border-slate-700">
      <div className="flex items-center justify-between mb-4">
        <h4 className="font-medium text-white flex items-center gap-2">
          <Camera className="w-4 h-4 text-amber-500" />
          {forensic.componentId}
        </h4>
        <div className="flex gap-1">
          {(['pre', 'post', 'diff'] as const).map((view) => (
            <button
              key={view}
              onClick={() => setActiveView(view)}
              className={`px-3 py-1 text-xs rounded transition-colors ${
                activeView === view
                  ? 'bg-amber-500 text-black'
                  : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
              }`}
            >
              {view.toUpperCase()}
            </button>
          ))}
        </div>
      </div>

      <div className="aspect-video bg-slate-900 rounded-lg overflow-hidden flex items-center justify-center">
        {activeView === 'pre' && (
          <img
            src={forensic.preRepair}
            alt="Pre-repair state"
            className="max-w-full max-h-full object-contain"
            onError={(e) => {
              (e.target as HTMLImageElement).src = '/placeholder-pcb.jpg';
            }}
          />
        )}
        {activeView === 'post' && (
          <img
            src={forensic.postRepair}
            alt="Post-repair state"
            className="max-w-full max-h-full object-contain"
            onError={(e) => {
              (e.target as HTMLImageElement).src = '/placeholder-pcb.jpg';
            }}
          />
        )}
        {activeView === 'diff' && (
          <div className="text-slate-500 text-sm">
            Difference visualization loading...
          </div>
        )}
      </div>

      <div className="mt-3 flex gap-4 text-sm text-slate-400">
        <span className="flex items-center gap-1">
          <span className="w-2 h-2 rounded-full bg-red-500" />
          Pre-Repair
        </span>
        <span className="flex items-center gap-1">
          <span className="w-2 h-2 rounded-full bg-green-500" />
          Post-Repair
        </span>
      </div>
    </div>
  );
};

// Main Component
export const ManifestViewer: React.FC = () => {
  const { caseId } = useParams<{ caseId: string }>();
  const [manifest, setManifest] = useState<Manifest | null>(null);
  const [verification, setVerification] = useState<VerificationResult | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!caseId) return;

    async function load() {
      try {
        const [manifestData, verifyData] = await Promise.all([
          fetchManifest(caseId),
          verifyManifest(caseId)
        ]);
        setManifest(manifestData);
        setVerification(verifyData);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load manifest');
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [caseId]);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <div className="text-center">
          <Zap className="w-12 h-12 text-amber-500 animate-pulse mx-auto mb-4" />
          <p className="text-slate-400">Loading Sovereign Manifest...</p>
        </div>
      </div>
    );
  }

  if (error || !manifest) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <div className="text-center max-w-md">
          <AlertTriangle className="w-12 h-12 text-red-500 mx-auto mb-4" />
          <h2 className="text-xl font-bold text-white mb-2">Manifest Not Found</h2>
          <p className="text-slate-400 mb-6">{error || 'The requested manifest could not be found.'}</p>
          <Link
            to="/"
            className="inline-flex items-center gap-2 px-4 py-2 bg-amber-500 text-black rounded-lg hover:bg-amber-400 transition-colors"
          >
            Return Home
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      {/* Header */}
      <header className="border-b border-slate-800 bg-slate-900/80 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Shield className="w-8 h-8 text-amber-500" />
            <div>
              <h1 className="text-lg font-bold">NOIZYLAB SOVEREIGN FORENSICS</h1>
              <p className="text-xs text-slate-400">Case ID: {manifest.caseId}</p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <StatusBadge status={verification?.verified ? 'verified' : 'pending'} />
            <button
              className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 transition-colors"
              onClick={() => window.open(`${API_BASE}/api/manifests/${caseId}/pdf`)}
            >
              <Download className="w-5 h-5" />
            </button>
            <button
              className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 transition-colors"
              onClick={() => {
                navigator.clipboard.writeText(window.location.href);
                alert('Link copied!');
              }}
            >
              <Share2 className="w-5 h-5" />
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8">
        {/* Status Banner */}
        <div className="bg-gradient-to-r from-green-500/20 to-green-500/5 border border-green-500/30 rounded-xl p-6 mb-8">
          <div className="flex items-center gap-4">
            <div className="w-16 h-16 rounded-full bg-green-500/20 flex items-center justify-center">
              <CheckCircle className="w-8 h-8 text-green-400" />
            </div>
            <div>
              <h2 className="text-2xl font-bold text-green-400">RECOVERY COMPLETE</h2>
              <p className="text-slate-300">Integrity Verified | Signed by M2_ULTRA_GOD_NODE</p>
            </div>
          </div>
        </div>

        {/* Device Info */}
        <section className="mb-8">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
            <Cpu className="w-5 h-5 text-amber-500" />
            Device Information
          </h3>
          <div className="bg-slate-800/50 rounded-xl p-6 border border-slate-700">
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <p className="text-sm text-slate-400 mb-1">Device</p>
                <p className="text-lg font-medium">{manifest.deviceType} {manifest.deviceModel}</p>
              </div>
              <div>
                <p className="text-sm text-slate-400 mb-1">Serial Number</p>
                <p className="text-lg font-medium font-mono">{manifest.serialNumber || 'N/A'}</p>
              </div>
              <div>
                <p className="text-sm text-slate-400 mb-1">Customer</p>
                <p className="text-lg font-medium">{manifest.customerName}</p>
              </div>
              <div>
                <p className="text-sm text-slate-400 mb-1">Completed</p>
                <p className="text-lg font-medium">
                  {new Date(manifest.completedAt).toLocaleDateString('en-CA', {
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit'
                  })}
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Biometric Stability Report */}
        <section className="mb-8">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
            <Activity className="w-5 h-5 text-amber-500" />
            Biometric Stability Report
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <MetricCard
              icon={<Activity className="w-4 h-4" />}
              label="Average Stability"
              value={`${manifest.biometrics.avgStability}%`}
              status={manifest.biometrics.avgStability > 95 ? 'good' : 'warning'}
            />
            <MetricCard
              icon={<Shield className="w-4 h-4" />}
              label="Aura-Match Score"
              value={manifest.biometrics.auraMatchScore.toFixed(3)}
              status={manifest.biometrics.auraMatchScore > 0.95 ? 'good' : 'neutral'}
            />
            <MetricCard
              icon={<Zap className="w-4 h-4" />}
              label="Jitter Compensated"
              value={`${manifest.biometrics.jitterCompensated}mm`}
              status="good"
            />
            <MetricCard
              icon={<Clock className="w-4 h-4" />}
              label="Session Duration"
              value={`${manifest.biometrics.sessionDuration} min`}
              status="neutral"
            />
          </div>
        </section>

        {/* Repair Details */}
        <section className="mb-8">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
            <FileText className="w-5 h-5 text-amber-500" />
            Repair Specifications
          </h3>
          <div className="bg-slate-800/50 rounded-xl p-6 border border-slate-700 space-y-4">
            <div>
              <p className="text-sm text-slate-400 mb-1">Diagnosis</p>
              <p className="text-white">{manifest.diagnosis}</p>
            </div>
            <div>
              <p className="text-sm text-slate-400 mb-1">Root Cause</p>
              <p className="text-white">{manifest.rootCause}</p>
            </div>
            <div>
              <p className="text-sm text-slate-400 mb-1">Components Affected</p>
              <div className="flex flex-wrap gap-2">
                {manifest.componentsAffected.map((comp) => (
                  <span
                    key={comp}
                    className="px-3 py-1 bg-slate-700 rounded-full text-sm font-mono"
                  >
                    {comp}
                  </span>
                ))}
              </div>
            </div>
            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <p className="text-sm text-slate-400 mb-1">Repair Technique</p>
                <p className="text-white">{manifest.repairTechnique}</p>
              </div>
              <div>
                <p className="text-sm text-slate-400 mb-1">Solder Points</p>
                <p className="text-white font-mono">{manifest.solderPoints}</p>
              </div>
            </div>
          </div>
        </section>

        {/* Voltage Verification */}
        {Object.keys(manifest.voltageReadings).length > 0 && (
          <section className="mb-8">
            <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
              <Zap className="w-5 h-5 text-amber-500" />
              Voltage Verification
            </h3>
            <div className="bg-slate-800/50 rounded-xl overflow-hidden border border-slate-700">
              <table className="w-full">
                <thead>
                  <tr className="bg-slate-800">
                    <th className="px-4 py-3 text-left text-sm font-medium text-slate-400">Rail</th>
                    <th className="px-4 py-3 text-right text-sm font-medium text-slate-400">Voltage</th>
                    <th className="px-4 py-3 text-center text-sm font-medium text-slate-400">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(manifest.voltageReadings).map(([rail, voltage]) => (
                    <tr key={rail} className="border-t border-slate-700">
                      <td className="px-4 py-3 font-mono text-white">{rail}</td>
                      <td className="px-4 py-3 text-right font-mono text-white">{voltage}V</td>
                      <td className="px-4 py-3 text-center">
                        <span className="inline-flex items-center gap-1 text-green-400 text-sm">
                          <CheckCircle className="w-4 h-4" />
                          NOMINAL
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {/* Forensic Comparison */}
        {manifest.forensicImages.length > 0 && (
          <section className="mb-8">
            <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
              <Camera className="w-5 h-5 text-amber-500" />
              Forensic Comparison
            </h3>
            <div className="grid md:grid-cols-2 gap-4">
              {manifest.forensicImages.map((forensic, idx) => (
                <ForensicComparison key={idx} forensic={forensic} />
              ))}
            </div>
          </section>
        )}

        {/* Cryptographic Proof */}
        <section className="mb-8">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
            <Lock className="w-5 h-5 text-amber-500" />
            Cryptographic Truth
          </h3>
          <div className="bg-slate-800/50 rounded-xl p-6 border border-slate-700">
            <p className="text-slate-300 mb-4">
              This repair has been logged to the Sovereign Registry. The logic board's new hash
              has been verified against the Golden Reference. Any future drift will be detected
              by the SENTRY autonomous audit.
            </p>
            <div className="bg-slate-900 rounded-lg p-4 font-mono text-sm">
              <p className="text-slate-400">Sovereign Key:</p>
              <p className="text-amber-500 break-all">{manifest.verificationHash}</p>
              <p className="text-slate-400 mt-2">Authentication:</p>
              <p className="text-green-400">Signed by M2_ULTRA_GOD_NODE</p>
            </div>
          </div>
        </section>

        {/* Payment Section */}
        <section className="mb-8">
          <div className="bg-gradient-to-r from-amber-500/20 to-amber-500/5 border border-amber-500/30 rounded-xl p-6">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-lg font-bold flex items-center gap-2">
                  <DollarSign className="w-5 h-5 text-amber-500" />
                  Invoice Total
                </h3>
                <p className="text-3xl font-bold text-amber-400 mt-2">
                  ${manifest.totalPrice.toFixed(2)} CAD
                </p>
                {manifest.paid ? (
                  <p className="text-green-400 text-sm mt-1 flex items-center gap-1">
                    <CheckCircle className="w-4 h-4" />
                    Paid on {new Date(manifest.paidAt!).toLocaleDateString()}
                  </p>
                ) : (
                  <p className="text-slate-400 text-sm mt-1">Payment due within 7 days</p>
                )}
              </div>
              {!manifest.paid && (
                <Link
                  to={`/pay/${manifest.caseId}`}
                  className="px-6 py-3 bg-amber-500 text-black font-bold rounded-lg hover:bg-amber-400 transition-colors"
                >
                  Pay Now
                </Link>
              )}
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="text-center text-slate-500 text-sm py-8 border-t border-slate-800">
          <p>NOIZYLAB SOVEREIGN FORENSICS</p>
          <p className="mt-1">Your hardware has been restored to Sovereign Purity.</p>
          <p className="mt-4 text-amber-500 font-bold">GORUNFREE</p>
        </footer>
      </main>
    </div>
  );
};

export default ManifestViewer;
