import React, { useState, useEffect } from 'react';

interface BoardDefinition {
  id: string;
  name: string;
  manufacturer: string;
  category: string;
  model?: string;
  year?: number;
  components: ComponentDefinition[];
  commonIssues: CommonIssue[];
  schematicAvailable: boolean;
  boardviewAvailable: boolean;
}

interface ComponentDefinition {
  designator: string;
  name: string;
  partNumber?: string;
  category: string;
  critical: boolean;
  replacementDifficulty: string;
}

interface CommonIssue {
  component: string;
  symptom: string;
  cause: string;
  solution: string;
  frequency: string;
  repairCost?: { min: number; max: number };
}

export default function BoardLibrary() {
  const [boards, setBoards] = useState<BoardDefinition[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [selectedBoard, setSelectedBoard] = useState<BoardDefinition | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchBoards();
  }, []);

  const fetchBoards = async () => {
    try {
      const response = await fetch('/api/boards');
      const data = await response.json();
      setBoards(data.boards || []);
    } catch (error) {
      console.error('Failed to fetch boards:', error);
    } finally {
      setLoading(false);
    }
  };

  const categories = [
    { id: 'phone', label: '📱 Phones', icon: '📱' },
    { id: 'laptop', label: '💻 Laptops', icon: '💻' },
    { id: 'tablet', label: '📱 Tablets', icon: '📱' },
    { id: 'console', label: '🎮 Consoles', icon: '🎮' },
    { id: 'pc', label: '🖥️ PCs', icon: '🖥️' },
    { id: 'other', label: '🔧 Other', icon: '🔧' },
  ];

  const filteredBoards = boards.filter(board => {
    const matchesSearch = !searchQuery ||
      board.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      board.manufacturer.toLowerCase().includes(searchQuery.toLowerCase()) ||
      board.model?.toLowerCase().includes(searchQuery.toLowerCase());
    
    const matchesCategory = !selectedCategory || board.category === selectedCategory;
    
    return matchesSearch && matchesCategory;
  });

  const frequencyColors = {
    rare: 'bg-gray-500',
    occasional: 'bg-yellow-500',
    common: 'bg-orange-500',
    very_common: 'bg-red-500',
  };

  const difficultyColors = {
    easy: 'text-green-400',
    medium: 'text-yellow-400',
    hard: 'text-orange-400',
    expert: 'text-red-400',
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
          <h1 className="text-2xl font-bold">Board Library</h1>
          <p className="text-gray-400 mt-1">
            Reference database of known PCB boards and components
          </p>
        </div>
      </header>

      <div className="max-w-6xl mx-auto p-6">
        {/* Search and filters */}
        <div className="flex gap-4 mb-6">
          <div className="flex-1">
            <input
              type="text"
              placeholder="Search boards..."
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              className="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl"
            />
          </div>
        </div>

        {/* Categories */}
        <div className="flex gap-2 overflow-x-auto pb-4 mb-6">
          <button
            onClick={() => setSelectedCategory(null)}
            className={`px-4 py-2 rounded-full whitespace-nowrap ${
              !selectedCategory ? 'bg-green-500 text-black' : 'bg-gray-800'
            }`}
          >
            All
          </button>
          {categories.map(cat => (
            <button
              key={cat.id}
              onClick={() => setSelectedCategory(cat.id)}
              className={`px-4 py-2 rounded-full whitespace-nowrap ${
                selectedCategory === cat.id ? 'bg-green-500 text-black' : 'bg-gray-800'
              }`}
            >
              {cat.icon} {cat.label}
            </button>
          ))}
        </div>

        {/* Board list or detail view */}
        {selectedBoard ? (
          <BoardDetail
            board={selectedBoard}
            onBack={() => setSelectedBoard(null)}
            frequencyColors={frequencyColors}
            difficultyColors={difficultyColors}
          />
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {filteredBoards.map(board => (
              <button
                key={board.id}
                onClick={() => setSelectedBoard(board)}
                className="p-4 bg-gray-900 rounded-xl border border-gray-800 text-left hover:border-green-500 transition-colors"
              >
                <div className="flex items-start justify-between">
                  <div>
                    <span className="text-xs text-gray-500 uppercase">
                      {board.manufacturer}
                    </span>
                    <h3 className="font-semibold mt-1">{board.name}</h3>
                    {board.model && (
                      <p className="text-sm text-gray-400">{board.model}</p>
                    )}
                  </div>
                  <span className="text-2xl">
                    {categories.find(c => c.id === board.category)?.icon || '📋'}
                  </span>
                </div>
                
                <div className="mt-4 flex items-center gap-4 text-sm text-gray-400">
                  <span>{board.components.length} components</span>
                  <span>{board.commonIssues.length} known issues</span>
                </div>
                
                <div className="mt-3 flex gap-2">
                  {board.schematicAvailable && (
                    <span className="px-2 py-0.5 bg-blue-500/20 text-blue-400 rounded text-xs">
                      Schematic
                    </span>
                  )}
                  {board.boardviewAvailable && (
                    <span className="px-2 py-0.5 bg-purple-500/20 text-purple-400 rounded text-xs">
                      Boardview
                    </span>
                  )}
                </div>
              </button>
            ))}
            
            {filteredBoards.length === 0 && (
              <div className="col-span-full text-center py-12 text-gray-500">
                No boards found matching your search.
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

function BoardDetail({
  board,
  onBack,
  frequencyColors,
  difficultyColors,
}: {
  board: BoardDefinition;
  onBack: () => void;
  frequencyColors: Record<string, string>;
  difficultyColors: Record<string, string>;
}) {
  const [activeTab, setActiveTab] = useState<'components' | 'issues'>('components');

  return (
    <div>
      {/* Back button and header */}
      <div className="mb-6">
        <button
          onClick={onBack}
          className="text-gray-400 hover:text-white mb-4"
        >
          ← Back to library
        </button>
        
        <div className="flex items-start justify-between">
          <div>
            <span className="text-sm text-gray-500">{board.manufacturer}</span>
            <h2 className="text-2xl font-bold mt-1">{board.name}</h2>
            <p className="text-gray-400 mt-1">
              {board.model} {board.year && `(${board.year})`}
            </p>
          </div>
          <div className="flex gap-2">
            {board.schematicAvailable && (
              <button className="px-4 py-2 bg-blue-500 text-white rounded-lg">
                📄 View Schematic
              </button>
            )}
            {board.boardviewAvailable && (
              <button className="px-4 py-2 bg-purple-500 text-white rounded-lg">
                🔍 Open Boardview
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-4 border-b border-gray-800 mb-6">
        <button
          onClick={() => setActiveTab('components')}
          className={`pb-4 px-2 border-b-2 ${
            activeTab === 'components'
              ? 'border-green-500 text-green-500'
              : 'border-transparent text-gray-400'
          }`}
        >
          Components ({board.components.length})
        </button>
        <button
          onClick={() => setActiveTab('issues')}
          className={`pb-4 px-2 border-b-2 ${
            activeTab === 'issues'
              ? 'border-green-500 text-green-500'
              : 'border-transparent text-gray-400'
          }`}
        >
          Common Issues ({board.commonIssues.length})
        </button>
      </div>

      {/* Components tab */}
      {activeTab === 'components' && (
        <div className="space-y-3">
          {board.components.map(component => (
            <div
              key={component.designator}
              className="p-4 bg-gray-900 rounded-xl border border-gray-800"
            >
              <div className="flex items-start justify-between">
                <div>
                  <div className="flex items-center gap-2">
                    <code className="px-2 py-0.5 bg-gray-800 rounded text-green-400">
                      {component.designator}
                    </code>
                    {component.critical && (
                      <span className="px-2 py-0.5 bg-red-500/20 text-red-400 rounded text-xs">
                        Critical
                      </span>
                    )}
                  </div>
                  <h4 className="font-semibold mt-2">{component.name}</h4>
                  {component.partNumber && (
                    <p className="text-sm text-gray-400">Part: {component.partNumber}</p>
                  )}
                </div>
                <div className="text-right">
                  <span className="text-xs text-gray-500">Difficulty</span>
                  <p className={`font-medium capitalize ${
                    difficultyColors[component.replacementDifficulty as keyof typeof difficultyColors] || ''
                  }`}>
                    {component.replacementDifficulty}
                  </p>
                </div>
              </div>
              <div className="mt-2 text-sm text-gray-500 capitalize">
                {component.category.replace('_', ' ')}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Issues tab */}
      {activeTab === 'issues' && (
        <div className="space-y-4">
          {board.commonIssues.map((issue, i) => (
            <div
              key={i}
              className="p-4 bg-gray-900 rounded-xl border border-gray-800"
            >
              <div className="flex items-start justify-between mb-3">
                <div className="flex items-center gap-2">
                  <code className="px-2 py-0.5 bg-gray-800 rounded">
                    {issue.component}
                  </code>
                  <span className={`px-2 py-0.5 rounded text-xs text-white ${
                    frequencyColors[issue.frequency as keyof typeof frequencyColors] || 'bg-gray-500'
                  }`}>
                    {issue.frequency.replace('_', ' ')}
                  </span>
                </div>
                {issue.repairCost && (
                  <span className="text-green-400">
                    ${issue.repairCost.min}-${issue.repairCost.max}
                  </span>
                )}
              </div>
              
              <h4 className="font-semibold text-yellow-400 mb-2">
                ⚠️ {issue.symptom}
              </h4>
              
              <div className="space-y-2 text-sm">
                <p>
                  <span className="text-gray-500">Cause:</span>{' '}
                  <span className="text-gray-300">{issue.cause}</span>
                </p>
                <p>
                  <span className="text-gray-500">Solution:</span>{' '}
                  <span className="text-green-400">{issue.solution}</span>
                </p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
