import React, { useState, useCallback, useRef } from 'react';

interface Issue {
  id: string;
  component: string;
  type: 'damaged' | 'missing' | 'misaligned' | 'cold_solder' | 'bridged';
  severity: 'critical' | 'warning' | 'info';
  description: string;
  location: { x: number; y: number; width: number; height: number };
  confidence: number;
  repairGuide?: string;
}

interface AnnotationToolProps {
  imageUrl: string;
  issues: Issue[];
  onIssuesChange: (issues: Issue[]) => void;
  boardType?: string;
  readOnly?: boolean;
}

export default function AnnotationTool({
  imageUrl,
  issues,
  onIssuesChange,
  boardType,
  readOnly = false,
}: AnnotationToolProps) {
  const [selectedIssue, setSelectedIssue] = useState<string | null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [drawStart, setDrawStart] = useState<{ x: number; y: number } | null>(null);
  const [tool, setTool] = useState<'select' | 'draw' | 'pan'>('select');
  const [zoom, setZoom] = useState(1);
  const [pan, setPan] = useState({ x: 0, y: 0 });
  const [newIssue, setNewIssue] = useState<Partial<Issue> | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const getRelativePosition = useCallback((e: React.MouseEvent) => {
    const rect = containerRef.current?.getBoundingClientRect();
    if (!rect) return { x: 0, y: 0 };
    
    return {
      x: ((e.clientX - rect.left - pan.x) / zoom / rect.width) * 100,
      y: ((e.clientY - rect.top - pan.y) / zoom / rect.height) * 100,
    };
  }, [pan, zoom]);

  const handleMouseDown = (e: React.MouseEvent) => {
    if (readOnly || tool !== 'draw') return;
    
    const pos = getRelativePosition(e);
    setIsDrawing(true);
    setDrawStart(pos);
  };

  const handleMouseUp = (e: React.MouseEvent) => {
    if (!isDrawing || !drawStart) return;
    
    const pos = getRelativePosition(e);
    const width = Math.abs(pos.x - drawStart.x);
    const height = Math.abs(pos.y - drawStart.y);
    
    if (width > 2 && height > 2) {
      setNewIssue({
        location: {
          x: Math.min(pos.x, drawStart.x),
          y: Math.min(pos.y, drawStart.y),
          width,
          height,
        },
      });
    }
    
    setIsDrawing(false);
    setDrawStart(null);
  };

  const handleSaveNewIssue = () => {
    if (!newIssue?.location) return;
    
    const issue: Issue = {
      id: `issue_${Date.now()}`,
      component: newIssue.component || 'Unknown Component',
      type: newIssue.type || 'damaged',
      severity: newIssue.severity || 'warning',
      description: newIssue.description || '',
      location: newIssue.location,
      confidence: 100, // Manual annotation = 100% confidence
    };
    
    onIssuesChange([...issues, issue]);
    setNewIssue(null);
  };

  const handleDeleteIssue = (id: string) => {
    onIssuesChange(issues.filter(i => i.id !== id));
    setSelectedIssue(null);
  };

  const severityColors = {
    critical: { border: '#ef4444', bg: 'rgba(239, 68, 68, 0.3)' },
    warning: { border: '#f59e0b', bg: 'rgba(245, 158, 11, 0.3)' },
    info: { border: '#3b82f6', bg: 'rgba(59, 130, 246, 0.3)' },
  };

  return (
    <div className="flex flex-col h-full bg-gray-950">
      {/* Toolbar */}
      {!readOnly && (
        <div className="flex items-center gap-4 p-4 border-b border-gray-800">
          <div className="flex gap-2">
            <button
              onClick={() => setTool('select')}
              className={`px-4 py-2 rounded-lg flex items-center gap-2 ${
                tool === 'select' ? 'bg-green-500 text-black' : 'bg-gray-800'
              }`}
            >
              <span>🖱️</span> Select
            </button>
            <button
              onClick={() => setTool('draw')}
              className={`px-4 py-2 rounded-lg flex items-center gap-2 ${
                tool === 'draw' ? 'bg-green-500 text-black' : 'bg-gray-800'
              }`}
            >
              <span>✏️</span> Draw
            </button>
            <button
              onClick={() => setTool('pan')}
              className={`px-4 py-2 rounded-lg flex items-center gap-2 ${
                tool === 'pan' ? 'bg-green-500 text-black' : 'bg-gray-800'
              }`}
            >
              <span>🤚</span> Pan
            </button>
          </div>
          
          <div className="h-8 w-px bg-gray-700" />
          
          <div className="flex items-center gap-2">
            <button
              onClick={() => setZoom(z => Math.max(0.5, z - 0.25))}
              className="px-3 py-2 bg-gray-800 rounded-lg"
            >
              −
            </button>
            <span className="text-sm w-16 text-center">{Math.round(zoom * 100)}%</span>
            <button
              onClick={() => setZoom(z => Math.min(3, z + 0.25))}
              className="px-3 py-2 bg-gray-800 rounded-lg"
            >
              +
            </button>
            <button
              onClick={() => { setZoom(1); setPan({ x: 0, y: 0 }); }}
              className="px-3 py-2 bg-gray-800 rounded-lg text-sm"
            >
              Reset
            </button>
          </div>
          
          <div className="h-8 w-px bg-gray-700" />
          
          <div className="text-sm text-gray-400">
            {boardType && <span className="mr-4">📋 {boardType}</span>}
            <span>🎯 {issues.length} issues</span>
          </div>
        </div>
      )}

      {/* Main content */}
      <div className="flex flex-1 overflow-hidden">
        {/* Canvas area */}
        <div className="flex-1 overflow-hidden relative">
          <div
            ref={containerRef}
            className="absolute inset-0 overflow-hidden bg-gray-900 cursor-crosshair"
            onMouseDown={handleMouseDown}
            onMouseUp={handleMouseUp}
            style={{ cursor: tool === 'draw' ? 'crosshair' : tool === 'pan' ? 'grab' : 'default' }}
          >
            <div
              style={{
                transform: `translate(${pan.x}px, ${pan.y}px) scale(${zoom})`,
                transformOrigin: 'top left',
                transition: 'transform 0.1s ease-out',
              }}
              className="relative"
            >
              {/* Board image */}
              <img
                src={imageUrl}
                alt="Circuit board"
                className="max-w-none"
                draggable={false}
              />
              
              {/* Issue annotations */}
              {issues.map(issue => (
                <div
                  key={issue.id}
                  onClick={() => setSelectedIssue(issue.id)}
                  className={`absolute cursor-pointer transition-all ${
                    selectedIssue === issue.id ? 'ring-2 ring-white' : ''
                  }`}
                  style={{
                    left: `${issue.location.x}%`,
                    top: `${issue.location.y}%`,
                    width: `${issue.location.width}%`,
                    height: `${issue.location.height}%`,
                    border: `2px solid ${severityColors[issue.severity].border}`,
                    backgroundColor: severityColors[issue.severity].bg,
                  }}
                >
                  {/* Label */}
                  <div
                    className="absolute -top-6 left-0 px-2 py-0.5 rounded text-xs whitespace-nowrap"
                    style={{ backgroundColor: severityColors[issue.severity].border }}
                  >
                    {issue.component}
                  </div>
                  
                  {/* Confidence badge */}
                  <div className="absolute -bottom-5 right-0 px-1.5 py-0.5 bg-gray-900 rounded text-xs">
                    {issue.confidence}%
                  </div>
                </div>
              ))}
              
              {/* Drawing preview */}
              {isDrawing && drawStart && (
                <div
                  className="absolute border-2 border-dashed border-green-500 bg-green-500/20 pointer-events-none"
                  style={{
                    left: `${drawStart.x}%`,
                    top: `${drawStart.y}%`,
                  }}
                />
              )}
            </div>
          </div>
        </div>

        {/* Side panel */}
        <div className="w-80 bg-gray-900 border-l border-gray-800 flex flex-col">
          {/* Issue details */}
          {selectedIssue && (
            <div className="p-4 border-b border-gray-800">
              <div className="flex justify-between items-start mb-4">
                <h3 className="font-semibold">Issue Details</h3>
                {!readOnly && (
                  <button
                    onClick={() => handleDeleteIssue(selectedIssue)}
                    className="text-red-400 text-sm hover:text-red-300"
                  >
                    Delete
                  </button>
                )}
              </div>
              
              {(() => {
                const issue = issues.find(i => i.id === selectedIssue);
                if (!issue) return null;
                
                return (
                  <div className="space-y-3">
                    <div>
                      <label className="text-xs text-gray-500">Component</label>
                      <p className="font-medium">{issue.component}</p>
                    </div>
                    <div>
                      <label className="text-xs text-gray-500">Type</label>
                      <p className="capitalize">{issue.type.replace('_', ' ')}</p>
                    </div>
                    <div>
                      <label className="text-xs text-gray-500">Severity</label>
                      <span
                        className="px-2 py-0.5 rounded text-sm capitalize ml-2"
                        style={{ backgroundColor: severityColors[issue.severity].bg }}
                      >
                        {issue.severity}
                      </span>
                    </div>
                    <div>
                      <label className="text-xs text-gray-500">Description</label>
                      <p className="text-sm text-gray-300">{issue.description || 'No description'}</p>
                    </div>
                    <div>
                      <label className="text-xs text-gray-500">Confidence</label>
                      <div className="flex items-center gap-2 mt-1">
                        <div className="flex-1 h-2 bg-gray-800 rounded-full overflow-hidden">
                          <div
                            className="h-full bg-green-500"
                            style={{ width: `${issue.confidence}%` }}
                          />
                        </div>
                        <span className="text-sm">{issue.confidence}%</span>
                      </div>
                    </div>
                    {issue.repairGuide && (
                      <div>
                        <label className="text-xs text-gray-500">Repair Guide</label>
                        <p className="text-sm text-gray-300 mt-1">{issue.repairGuide}</p>
                      </div>
                    )}
                  </div>
                );
              })()}
            </div>
          )}

          {/* New issue form */}
          {newIssue && (
            <div className="p-4 border-b border-gray-800 bg-gray-800/50">
              <h3 className="font-semibold mb-4">New Annotation</h3>
              <div className="space-y-3">
                <div>
                  <label className="text-xs text-gray-500">Component</label>
                  <input
                    type="text"
                    value={newIssue.component || ''}
                    onChange={e => setNewIssue({ ...newIssue, component: e.target.value })}
                    className="w-full mt-1 px-3 py-2 bg-gray-900 border border-gray-700 rounded-lg"
                    placeholder="e.g., U1201"
                  />
                </div>
                <div>
                  <label className="text-xs text-gray-500">Type</label>
                  <select
                    value={newIssue.type || 'damaged'}
                    onChange={e => setNewIssue({ ...newIssue, type: e.target.value as Issue['type'] })}
                    className="w-full mt-1 px-3 py-2 bg-gray-900 border border-gray-700 rounded-lg"
                  >
                    <option value="damaged">Damaged</option>
                    <option value="missing">Missing</option>
                    <option value="misaligned">Misaligned</option>
                    <option value="cold_solder">Cold Solder</option>
                    <option value="bridged">Bridged</option>
                  </select>
                </div>
                <div>
                  <label className="text-xs text-gray-500">Severity</label>
                  <select
                    value={newIssue.severity || 'warning'}
                    onChange={e => setNewIssue({ ...newIssue, severity: e.target.value as Issue['severity'] })}
                    className="w-full mt-1 px-3 py-2 bg-gray-900 border border-gray-700 rounded-lg"
                  >
                    <option value="critical">Critical</option>
                    <option value="warning">Warning</option>
                    <option value="info">Info</option>
                  </select>
                </div>
                <div>
                  <label className="text-xs text-gray-500">Description</label>
                  <textarea
                    value={newIssue.description || ''}
                    onChange={e => setNewIssue({ ...newIssue, description: e.target.value })}
                    className="w-full mt-1 px-3 py-2 bg-gray-900 border border-gray-700 rounded-lg resize-none"
                    rows={2}
                    placeholder="Describe the issue..."
                  />
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={handleSaveNewIssue}
                    className="flex-1 py-2 bg-green-500 text-black rounded-lg font-medium"
                  >
                    Save
                  </button>
                  <button
                    onClick={() => setNewIssue(null)}
                    className="flex-1 py-2 bg-gray-700 rounded-lg"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Issue list */}
          <div className="flex-1 overflow-y-auto">
            <div className="p-4">
              <h3 className="font-semibold mb-3">All Issues ({issues.length})</h3>
              <div className="space-y-2">
                {issues.map(issue => (
                  <button
                    key={issue.id}
                    onClick={() => setSelectedIssue(issue.id)}
                    className={`w-full p-3 rounded-lg text-left transition-colors ${
                      selectedIssue === issue.id
                        ? 'bg-gray-800 ring-1 ring-green-500'
                        : 'bg-gray-800/50 hover:bg-gray-800'
                    }`}
                  >
                    <div className="flex items-start justify-between">
                      <div>
                        <p className="font-medium">{issue.component}</p>
                        <p className="text-sm text-gray-400 capitalize">
                          {issue.type.replace('_', ' ')}
                        </p>
                      </div>
                      <span
                        className="px-2 py-0.5 rounded text-xs"
                        style={{ backgroundColor: severityColors[issue.severity].bg }}
                      >
                        {issue.severity}
                      </span>
                    </div>
                  </button>
                ))}
                
                {issues.length === 0 && (
                  <p className="text-gray-500 text-center py-8">
                    No issues detected.
                    {!readOnly && ' Use the draw tool to annotate.'}
                  </p>
                )}
              </div>
            </div>
          </div>

          {/* Export button */}
          {!readOnly && issues.length > 0 && (
            <div className="p-4 border-t border-gray-800">
              <button
                onClick={() => {
                  const data = JSON.stringify({ boardType, issues }, null, 2);
                  const blob = new Blob([data], { type: 'application/json' });
                  const url = URL.createObjectURL(blob);
                  const a = document.createElement('a');
                  a.href = url;
                  a.download = `annotation-${Date.now()}.json`;
                  a.click();
                }}
                className="w-full py-3 bg-gray-800 rounded-lg font-medium hover:bg-gray-700"
              >
                📥 Export Annotations
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
