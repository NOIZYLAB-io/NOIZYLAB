import React, { useState, useEffect, useRef, useCallback } from 'react';

interface BatchScanProps {
  onComplete: (results: BatchResult[]) => void;
}

interface BatchResult {
  id: string;
  fileName: string;
  status: 'pending' | 'processing' | 'complete' | 'error';
  progress: number;
  result?: {
    boardType: string;
    issuesCount: number;
    confidence: number;
    issues: Array<{
      component: string;
      type: string;
      severity: string;
    }>;
  };
  error?: string;
}

export default function BatchScan({ onComplete }: BatchScanProps) {
  const [files, setFiles] = useState<File[]>([]);
  const [results, setResults] = useState<BatchResult[]>([]);
  const [isProcessing, setIsProcessing] = useState(false);
  const [dragActive, setDragActive] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const abortControllerRef = useRef<AbortController | null>(null);

  const handleDrag = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  }, []);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    const droppedFiles = Array.from(e.dataTransfer.files).filter(
      file => file.type.startsWith('image/')
    );

    if (droppedFiles.length > 0) {
      addFiles(droppedFiles);
    }
  }, []);

  const addFiles = (newFiles: File[]) => {
    setFiles(prev => [...prev, ...newFiles]);
    setResults(prev => [
      ...prev,
      ...newFiles.map(file => ({
        id: `${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
        fileName: file.name,
        status: 'pending' as const,
        progress: 0,
      })),
    ]);
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = Array.from(e.target.files || []);
    if (selectedFiles.length > 0) {
      addFiles(selectedFiles);
    }
  };

  const removeFile = (index: number) => {
    setFiles(prev => prev.filter((_, i) => i !== index));
    setResults(prev => prev.filter((_, i) => i !== index));
  };

  const processFiles = async () => {
    if (files.length === 0 || isProcessing) return;

    setIsProcessing(true);
    abortControllerRef.current = new AbortController();

    const updatedResults = [...results];

    for (let i = 0; i < files.length; i++) {
      if (abortControllerRef.current?.signal.aborted) break;

      const file = files[i];
      updatedResults[i] = { ...updatedResults[i], status: 'processing', progress: 0 };
      setResults([...updatedResults]);

      try {
        // Simulate progress updates
        for (let p = 0; p <= 80; p += 20) {
          await new Promise(r => setTimeout(r, 200));
          updatedResults[i] = { ...updatedResults[i], progress: p };
          setResults([...updatedResults]);
        }

        // Make actual API call
        const formData = new FormData();
        formData.append('image', file);
        formData.append('userId', 'batch_user');

        const response = await fetch('/api/scan', {
          method: 'POST',
          body: formData,
          signal: abortControllerRef.current?.signal,
        });

        if (!response.ok) throw new Error('Scan failed');

        const data = await response.json();

        // Poll for results
        let result = null;
        for (let attempt = 0; attempt < 30; attempt++) {
          await new Promise(r => setTimeout(r, 1000));
          
          const statusRes = await fetch(`/api/scan/${data.scanId}`);
          const statusData = await statusRes.json();
          
          if (statusData.status === 'complete') {
            result = statusData;
            break;
          }
          
          updatedResults[i] = { ...updatedResults[i], progress: 80 + (attempt / 30) * 20 };
          setResults([...updatedResults]);
        }

        if (result) {
          updatedResults[i] = {
            ...updatedResults[i],
            status: 'complete',
            progress: 100,
            result: {
              boardType: result.boardType || 'Unknown',
              issuesCount: result.issues?.length || 0,
              confidence: result.confidence || 0,
              issues: result.issues || [],
            },
          };
        } else {
          throw new Error('Timeout waiting for results');
        }
      } catch (error) {
        if ((error as Error).name === 'AbortError') break;
        
        updatedResults[i] = {
          ...updatedResults[i],
          status: 'error',
          progress: 0,
          error: (error as Error).message,
        };
      }

      setResults([...updatedResults]);
    }

    setIsProcessing(false);
    onComplete(updatedResults);
  };

  const cancelProcessing = () => {
    abortControllerRef.current?.abort();
    setIsProcessing(false);
  };

  const completedCount = results.filter(r => r.status === 'complete').length;
  const errorCount = results.filter(r => r.status === 'error').length;
  const totalIssues = results.reduce((sum, r) => sum + (r.result?.issuesCount || 0), 0);

  return (
    <div className="min-h-screen bg-gray-950 text-white p-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold">Batch Scan</h1>
          <p className="text-gray-400 mt-2">
            Upload multiple board images for automated analysis
          </p>
        </div>

        {/* Drop zone */}
        <div
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-xl p-12 text-center cursor-pointer transition-colors ${
            dragActive
              ? 'border-green-500 bg-green-500/10'
              : 'border-gray-700 hover:border-gray-600'
          }`}
        >
          <input
            ref={fileInputRef}
            type="file"
            multiple
            accept="image/*"
            onChange={handleFileSelect}
            className="hidden"
          />
          <div className="text-5xl mb-4">📸</div>
          <p className="text-lg font-medium">
            {dragActive ? 'Drop images here' : 'Drag & drop board images'}
          </p>
          <p className="text-gray-400 mt-2">
            or click to select files • PNG, JPG up to 10MB each
          </p>
        </div>

        {/* File list */}
        {results.length > 0 && (
          <div className="mt-8">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-xl font-semibold">
                Files ({results.length})
              </h2>
              {!isProcessing && (
                <button
                  onClick={() => {
                    setFiles([]);
                    setResults([]);
                  }}
                  className="text-gray-400 hover:text-white text-sm"
                >
                  Clear All
                </button>
              )}
            </div>

            <div className="space-y-3">
              {results.map((result, index) => (
                <div
                  key={result.id}
                  className="bg-gray-900 rounded-xl p-4 border border-gray-800"
                >
                  <div className="flex items-center gap-4">
                    {/* Thumbnail */}
                    <div className="w-16 h-16 bg-gray-800 rounded-lg overflow-hidden flex-shrink-0">
                      {files[index] && (
                        <img
                          src={URL.createObjectURL(files[index])}
                          alt={result.fileName}
                          className="w-full h-full object-cover"
                        />
                      )}
                    </div>

                    {/* Info */}
                    <div className="flex-1 min-w-0">
                      <p className="font-medium truncate">{result.fileName}</p>
                      
                      {result.status === 'pending' && (
                        <p className="text-gray-400 text-sm">Waiting...</p>
                      )}
                      
                      {result.status === 'processing' && (
                        <div className="mt-2">
                          <div className="h-2 bg-gray-800 rounded-full overflow-hidden">
                            <div
                              className="h-full bg-green-500 transition-all"
                              style={{ width: `${result.progress}%` }}
                            />
                          </div>
                          <p className="text-gray-400 text-sm mt-1">
                            Processing... {result.progress}%
                          </p>
                        </div>
                      )}
                      
                      {result.status === 'complete' && result.result && (
                        <div className="flex items-center gap-4 mt-1 text-sm">
                          <span className="text-green-400">✓ Complete</span>
                          <span className="text-gray-400">{result.result.boardType}</span>
                          <span className={result.result.issuesCount > 0 ? 'text-yellow-400' : 'text-green-400'}>
                            {result.result.issuesCount} issues
                          </span>
                          <span className="text-gray-400">{result.result.confidence}% confidence</span>
                        </div>
                      )}
                      
                      {result.status === 'error' && (
                        <p className="text-red-400 text-sm">❌ {result.error}</p>
                      )}
                    </div>

                    {/* Actions */}
                    {result.status === 'pending' && !isProcessing && (
                      <button
                        onClick={() => removeFile(index)}
                        className="text-gray-400 hover:text-red-400"
                      >
                        ✕
                      </button>
                    )}
                    
                    {result.status === 'complete' && (
                      <button className="px-4 py-2 bg-gray-800 rounded-lg text-sm hover:bg-gray-700">
                        View Details
                      </button>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Summary stats */}
        {(completedCount > 0 || errorCount > 0) && (
          <div className="mt-8 grid grid-cols-4 gap-4">
            <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
              <p className="text-gray-400 text-sm">Total Files</p>
              <p className="text-2xl font-bold">{results.length}</p>
            </div>
            <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
              <p className="text-gray-400 text-sm">Completed</p>
              <p className="text-2xl font-bold text-green-400">{completedCount}</p>
            </div>
            <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
              <p className="text-gray-400 text-sm">Errors</p>
              <p className="text-2xl font-bold text-red-400">{errorCount}</p>
            </div>
            <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
              <p className="text-gray-400 text-sm">Issues Found</p>
              <p className="text-2xl font-bold text-yellow-400">{totalIssues}</p>
            </div>
          </div>
        )}

        {/* Action buttons */}
        {results.length > 0 && (
          <div className="mt-8 flex gap-4">
            {!isProcessing ? (
              <>
                <button
                  onClick={processFiles}
                  disabled={results.every(r => r.status === 'complete' || r.status === 'error')}
                  className="flex-1 py-4 bg-green-500 text-black rounded-xl font-semibold text-lg disabled:opacity-50"
                >
                  🚀 Start Batch Analysis
                </button>
                {completedCount > 0 && (
                  <button
                    onClick={() => {
                      const csv = [
                        ['File', 'Board Type', 'Issues', 'Confidence', 'Status'].join(','),
                        ...results.map(r => [
                          r.fileName,
                          r.result?.boardType || '',
                          r.result?.issuesCount || 0,
                          r.result?.confidence || 0,
                          r.status,
                        ].join(','))
                      ].join('\n');
                      
                      const blob = new Blob([csv], { type: 'text/csv' });
                      const url = URL.createObjectURL(blob);
                      const a = document.createElement('a');
                      a.href = url;
                      a.download = `batch-scan-${Date.now()}.csv`;
                      a.click();
                    }}
                    className="px-8 py-4 bg-gray-800 rounded-xl font-semibold"
                  >
                    📥 Export CSV
                  </button>
                )}
              </>
            ) : (
              <button
                onClick={cancelProcessing}
                className="flex-1 py-4 bg-red-500 text-white rounded-xl font-semibold text-lg"
              >
                ⏹ Cancel
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
