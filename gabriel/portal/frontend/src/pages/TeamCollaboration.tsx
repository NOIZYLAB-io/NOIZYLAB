import React, { useState } from 'react';

interface TeamMember {
  id: string;
  email: string;
  name: string;
  role: 'owner' | 'admin' | 'member' | 'viewer';
  joinedAt: string;
  lastActive?: string;
  avatar?: string;
}

interface Workspace {
  id: string;
  name: string;
  slug: string;
  plan: 'free' | 'pro' | 'enterprise';
  members: TeamMember[];
  createdAt: string;
  settings: {
    allowMemberInvites: boolean;
    defaultRole: TeamMember['role'];
    requireApproval: boolean;
  };
}

interface InvitationModalProps {
  isOpen: boolean;
  onClose: () => void;
  onInvite: (email: string, role: TeamMember['role']) => void;
}

const InvitationModal: React.FC<InvitationModalProps> = ({ isOpen, onClose, onInvite }) => {
  const [email, setEmail] = useState('');
  const [role, setRole] = useState<TeamMember['role']>('member');
  const [sending, setSending] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSending(true);
    await onInvite(email, role);
    setSending(false);
    setEmail('');
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div className="bg-slate-800 rounded-lg max-w-md w-full p-6">
        <div className="flex justify-between items-center mb-6">
          <h3 className="text-xl font-semibold">Invite Team Member</h3>
          <button onClick={onClose} className="text-slate-400 hover:text-white">
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Email Address
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="colleague@company.com"
              className="w-full px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500"
              required
            />
          </div>

          <div className="mb-6">
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Role
            </label>
            <select
              value={role}
              onChange={(e) => setRole(e.target.value as TeamMember['role'])}
              className="w-full px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500"
            >
              <option value="viewer">Viewer - Can view scans only</option>
              <option value="member">Member - Can create scans</option>
              <option value="admin">Admin - Full access</option>
            </select>
          </div>

          <div className="flex gap-3">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg transition"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={sending}
              className="flex-1 px-4 py-2 bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold rounded-lg transition disabled:opacity-50"
            >
              {sending ? 'Sending...' : 'Send Invite'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

const MemberCard: React.FC<{
  member: TeamMember;
  currentUserRole: TeamMember['role'];
  onRemove: (id: string) => void;
  onUpdateRole: (id: string, role: TeamMember['role']) => void;
}> = ({ member, currentUserRole, onRemove, onUpdateRole }) => {
  const canManage = currentUserRole === 'owner' || currentUserRole === 'admin';
  const isOwner = member.role === 'owner';

  const roleColors = {
    owner: 'bg-purple-500/20 text-purple-400',
    admin: 'bg-amber-500/20 text-amber-400',
    member: 'bg-blue-500/20 text-blue-400',
    viewer: 'bg-slate-500/20 text-slate-400',
  };

  return (
    <div className="flex items-center justify-between p-4 bg-slate-700/50 rounded-lg">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center font-semibold">
          {member.name.charAt(0).toUpperCase()}
        </div>
        <div>
          <h4 className="font-medium">{member.name}</h4>
          <p className="text-sm text-slate-400">{member.email}</p>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <span className={`px-2 py-1 rounded text-xs font-medium ${roleColors[member.role]}`}>
          {member.role.toUpperCase()}
        </span>

        {canManage && !isOwner && (
          <div className="flex gap-2">
            <select
              value={member.role}
              onChange={(e) => onUpdateRole(member.id, e.target.value as TeamMember['role'])}
              className="px-2 py-1 bg-slate-600 border border-slate-500 rounded text-sm focus:outline-none"
            >
              <option value="viewer">Viewer</option>
              <option value="member">Member</option>
              <option value="admin">Admin</option>
            </select>
            <button
              onClick={() => onRemove(member.id)}
              className="p-1 text-red-400 hover:text-red-300 hover:bg-red-500/20 rounded"
            >
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

const TeamCollaboration: React.FC = () => {
  const [workspace, setWorkspace] = useState<Workspace>({
    id: 'ws_001',
    name: 'NOIZYLAB Repairs',
    slug: 'noizylab-repairs',
    plan: 'pro',
    createdAt: '2025-01-01T00:00:00Z',
    members: [
      { id: '1', email: 'owner@noizylab.com', name: 'Marcus Chen', role: 'owner', joinedAt: '2025-01-01T00:00:00Z' },
      { id: '2', email: 'admin@noizylab.com', name: 'Sarah Kim', role: 'admin', joinedAt: '2025-01-05T00:00:00Z' },
      { id: '3', email: 'tech@noizylab.com', name: 'Alex Rivera', role: 'member', joinedAt: '2025-01-10T00:00:00Z' },
    ],
    settings: {
      allowMemberInvites: true,
      defaultRole: 'member',
      requireApproval: false,
    },
  });

  const [showInviteModal, setShowInviteModal] = useState(false);
  const [activeTab, setActiveTab] = useState<'members' | 'settings' | 'activity'>('members');

  const currentUserRole: TeamMember['role'] = 'owner'; // Would come from auth

  const handleInvite = async (email: string, role: TeamMember['role']) => {
    // API call would go here
    console.log('Inviting:', email, role);
    const newMember: TeamMember = {
      id: `${Date.now()}`,
      email,
      name: email.split('@')[0],
      role,
      joinedAt: new Date().toISOString(),
    };
    setWorkspace(prev => ({
      ...prev,
      members: [...prev.members, newMember],
    }));
  };

  const handleRemove = (memberId: string) => {
    if (!confirm('Are you sure you want to remove this team member?')) return;
    setWorkspace(prev => ({
      ...prev,
      members: prev.members.filter(m => m.id !== memberId),
    }));
  };

  const handleUpdateRole = (memberId: string, newRole: TeamMember['role']) => {
    setWorkspace(prev => ({
      ...prev,
      members: prev.members.map(m => 
        m.id === memberId ? { ...m, role: newRole } : m
      ),
    }));
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      {/* Header */}
      <header className="border-b border-slate-700 bg-slate-800/50 backdrop-blur">
        <div className="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
          <div>
            <h1 className="text-2xl font-bold text-amber-500">Team Management</h1>
            <p className="text-slate-400">{workspace.name}</p>
          </div>
          <button
            onClick={() => setShowInviteModal(true)}
            className="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold rounded-lg transition flex items-center gap-2"
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
            Invite Member
          </button>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8">
        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Team Members</p>
            <p className="text-3xl font-bold">{workspace.members.length}</p>
          </div>
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Admins</p>
            <p className="text-3xl font-bold">
              {workspace.members.filter(m => m.role === 'admin' || m.role === 'owner').length}
            </p>
          </div>
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Plan</p>
            <p className="text-3xl font-bold capitalize">{workspace.plan}</p>
          </div>
          <div className="bg-slate-800 rounded-lg p-4">
            <p className="text-slate-400 text-sm">Seat Limit</p>
            <p className="text-3xl font-bold">
              {workspace.plan === 'enterprise' ? '∞' : workspace.plan === 'pro' ? '10' : '3'}
            </p>
          </div>
        </div>

        {/* Tabs */}
        <div className="flex gap-4 border-b border-slate-700 mb-6">
          {(['members', 'settings', 'activity'] as const).map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-4 py-2 font-medium capitalize transition ${
                activeTab === tab
                  ? 'text-amber-500 border-b-2 border-amber-500'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Members Tab */}
        {activeTab === 'members' && (
          <div className="space-y-3">
            {workspace.members.map((member) => (
              <MemberCard
                key={member.id}
                member={member}
                currentUserRole={currentUserRole}
                onRemove={handleRemove}
                onUpdateRole={handleUpdateRole}
              />
            ))}
          </div>
        )}

        {/* Settings Tab */}
        {activeTab === 'settings' && (
          <div className="bg-slate-800 rounded-lg p-6 space-y-6">
            <h3 className="text-lg font-semibold mb-4">Workspace Settings</h3>
            
            <div>
              <label className="block text-sm font-medium text-slate-300 mb-2">
                Workspace Name
              </label>
              <input
                type="text"
                value={workspace.name}
                onChange={(e) => setWorkspace(prev => ({ ...prev, name: e.target.value }))}
                className="w-full max-w-md px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500"
              />
            </div>

            <div className="flex items-center justify-between max-w-md">
              <div>
                <h4 className="font-medium">Allow Member Invites</h4>
                <p className="text-sm text-slate-400">Let members invite others</p>
              </div>
              <button
                onClick={() => setWorkspace(prev => ({
                  ...prev,
                  settings: { ...prev.settings, allowMemberInvites: !prev.settings.allowMemberInvites }
                }))}
                className={`w-12 h-6 rounded-full transition ${
                  workspace.settings.allowMemberInvites ? 'bg-amber-500' : 'bg-slate-600'
                }`}
              >
                <div className={`w-5 h-5 bg-white rounded-full transform transition ${
                  workspace.settings.allowMemberInvites ? 'translate-x-6' : 'translate-x-0.5'
                }`} />
              </button>
            </div>

            <div className="flex items-center justify-between max-w-md">
              <div>
                <h4 className="font-medium">Require Approval</h4>
                <p className="text-sm text-slate-400">Admin must approve new members</p>
              </div>
              <button
                onClick={() => setWorkspace(prev => ({
                  ...prev,
                  settings: { ...prev.settings, requireApproval: !prev.settings.requireApproval }
                }))}
                className={`w-12 h-6 rounded-full transition ${
                  workspace.settings.requireApproval ? 'bg-amber-500' : 'bg-slate-600'
                }`}
              >
                <div className={`w-5 h-5 bg-white rounded-full transform transition ${
                  workspace.settings.requireApproval ? 'translate-x-6' : 'translate-x-0.5'
                }`} />
              </button>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-300 mb-2">
                Default Role for New Members
              </label>
              <select
                value={workspace.settings.defaultRole}
                onChange={(e) => setWorkspace(prev => ({
                  ...prev,
                  settings: { ...prev.settings, defaultRole: e.target.value as TeamMember['role'] }
                }))}
                className="px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500"
              >
                <option value="viewer">Viewer</option>
                <option value="member">Member</option>
              </select>
            </div>

            <div className="pt-4 border-t border-slate-700">
              <button className="px-4 py-2 bg-red-500/20 text-red-400 hover:bg-red-500/30 rounded-lg transition">
                Delete Workspace
              </button>
            </div>
          </div>
        )}

        {/* Activity Tab */}
        {activeTab === 'activity' && (
          <div className="bg-slate-800 rounded-lg p-6">
            <h3 className="text-lg font-semibold mb-4">Recent Activity</h3>
            <div className="space-y-4">
              {[
                { user: 'Marcus Chen', action: 'completed scan', target: 'iPhone 15 Logic Board', time: '2 hours ago' },
                { user: 'Sarah Kim', action: 'uploaded reference', target: 'MacBook Pro M3', time: '5 hours ago' },
                { user: 'Alex Rivera', action: 'generated report', target: 'Batch #45', time: '1 day ago' },
                { user: 'Marcus Chen', action: 'invited', target: 'tech@company.com', time: '3 days ago' },
              ].map((activity, index) => (
                <div key={index} className="flex items-center gap-4 py-2 border-b border-slate-700 last:border-0">
                  <div className="w-8 h-8 rounded-full bg-slate-600 flex items-center justify-center text-sm font-medium">
                    {activity.user.charAt(0)}
                  </div>
                  <div className="flex-1">
                    <p>
                      <span className="font-medium">{activity.user}</span>
                      {' '}{activity.action}{' '}
                      <span className="text-amber-400">{activity.target}</span>
                    </p>
                    <p className="text-sm text-slate-400">{activity.time}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      <InvitationModal
        isOpen={showInviteModal}
        onClose={() => setShowInviteModal(false)}
        onInvite={handleInvite}
      />
    </div>
  );
};

export default TeamCollaboration;
