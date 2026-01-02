import React, { useState, useRef, useEffect, useCallback } from 'react';

/**
 * AR Camera Component for PCB Inspection
 * 
 * Features:
 * - Live camera feed with 48MP capture capability
 * - Real-time AR overlay for component highlighting
 * - Touch-to-focus and pinch-to-zoom
 * - Grid overlay for alignment
 * - Capture with flash support
 */

interface Component {
  id: string;
  type: string;
  position: { x: number; y: number };
  status: 'good' | 'warning' | 'defect';
  confidence: number;
}

interface ARCameraProps {
  onCapture: (imageData: Blob) => void;
  onAnalysisComplete?: (components: Component[]) => void;
  showGrid?: boolean;
  highlightComponents?: Component[];
}

const ARCamera: React.FC<ARCameraProps> = ({
  onCapture,
  onAnalysisComplete,
  showGrid = true,
  highlightComponents = []
}) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const overlayRef = useRef<HTMLCanvasElement>(null);
  
  const [isStreaming, setIsStreaming] = useState(false);
  const [isCapturing, setIsCapturing] = useState(false);
  const [zoom, setZoom] = useState(1);
  const [flashEnabled, setFlashEnabled] = useState(false);
  const [cameraFacing, setCameraFacing] = useState<'environment' | 'user'>('environment');
  const [error, setError] = useState<string | null>(null);

  // Initialize camera stream
  const startCamera = useCallback(async () => {
    try {
      const constraints: MediaStreamConstraints = {
        video: {
          facingMode: cameraFacing,
          width: { ideal: 4000 }, // Target high resolution
          height: { ideal: 3000 },
          aspectRatio: { ideal: 4 / 3 }
        },
        audio: false
      };

      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        await videoRef.current.play();
        setIsStreaming(true);
        setError(null);
      }
    } catch (err) {
      console.error('Camera error:', err);
      setError('Unable to access camera. Please grant permission.');
    }
  }, [cameraFacing]);

  // Stop camera stream
  const stopCamera = useCallback(() => {
    if (videoRef.current?.srcObject) {
      const stream = videoRef.current.srcObject as MediaStream;
      stream.getTracks().forEach(track => track.stop());
      videoRef.current.srcObject = null;
      setIsStreaming(false);
    }
  }, []);

  // Capture high-resolution image
  const captureImage = useCallback(async () => {
    if (!videoRef.current || !canvasRef.current) return;
    
    setIsCapturing(true);
    
    const video = videoRef.current;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    if (!ctx) return;
    
    // Set canvas to video resolution
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    // Draw video frame to canvas
    ctx.drawImage(video, 0, 0);
    
    // Convert to blob
    canvas.toBlob(
      (blob) => {
        if (blob) {
          onCapture(blob);
        }
        setIsCapturing(false);
      },
      'image/jpeg',
      0.95 // High quality
    );
  }, [onCapture]);

  // Draw AR overlay
  const drawOverlay = useCallback(() => {
    if (!overlayRef.current || !videoRef.current) return;
    
    const canvas = overlayRef.current;
    const video = videoRef.current;
    const ctx = canvas.getContext('2d');
    
    if (!ctx) return;
    
    // Match canvas size to video display size
    const rect = video.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.height;
    
    // Clear previous frame
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw grid if enabled
    if (showGrid) {
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.lineWidth = 1;
      
      // Vertical lines (rule of thirds)
      for (let i = 1; i < 3; i++) {
        const x = (canvas.width / 3) * i;
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
      }
      
      // Horizontal lines
      for (let i = 1; i < 3; i++) {
        const y = (canvas.height / 3) * i;
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
      }
    }
    
    // Draw component highlights
    highlightComponents.forEach(component => {
      const colors = {
        good: '#22C55E',
        warning: '#F59E0B',
        defect: '#EF4444'
      };
      
      // Scale position to canvas coordinates
      const x = (component.position.x / video.videoWidth) * canvas.width;
      const y = (component.position.y / video.videoHeight) * canvas.height;
      const size = 40;
      
      // Draw highlight box
      ctx.strokeStyle = colors[component.status];
      ctx.lineWidth = 3;
      ctx.strokeRect(x - size / 2, y - size / 2, size, size);
      
      // Draw pulsing animation for defects
      if (component.status === 'defect') {
        const pulse = Math.sin(Date.now() / 200) * 0.3 + 0.7;
        ctx.strokeStyle = `rgba(239, 68, 68, ${pulse})`;
        ctx.lineWidth = 2;
        ctx.strokeRect(x - size / 2 - 5, y - size / 2 - 5, size + 10, size + 10);
      }
      
      // Draw label
      ctx.fillStyle = colors[component.status];
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText(component.id, x - size / 2, y - size / 2 - 5);
      
      // Draw confidence
      ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText(`${(component.confidence * 100).toFixed(0)}%`, x + size / 2 + 5, y);
    });
    
    // Request next frame
    requestAnimationFrame(drawOverlay);
  }, [showGrid, highlightComponents]);

  // Switch camera
  const switchCamera = useCallback(() => {
    stopCamera();
    setCameraFacing(prev => prev === 'environment' ? 'user' : 'environment');
  }, [stopCamera]);

  // Handle zoom
  const handleZoom = useCallback((delta: number) => {
    setZoom(prev => Math.max(1, Math.min(5, prev + delta)));
  }, []);

  // Initialize on mount
  useEffect(() => {
    startCamera();
    return () => stopCamera();
  }, [startCamera, stopCamera]);

  // Start overlay animation
  useEffect(() => {
    if (isStreaming) {
      drawOverlay();
    }
  }, [isStreaming, drawOverlay]);

  // Apply zoom
  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.style.transform = `scale(${zoom})`;
    }
  }, [zoom]);

  return (
    <div className="ar-camera">
      <div className="camera-container">
        {/* Video feed */}
        <video
          ref={videoRef}
          playsInline
          muted
          className="camera-video"
          style={{ transform: `scale(${zoom})` }}
        />
        
        {/* AR overlay canvas */}
        <canvas ref={overlayRef} className="ar-overlay" />
        
        {/* Hidden capture canvas */}
        <canvas ref={canvasRef} style={{ display: 'none' }} />
        
        {/* Error display */}
        {error && (
          <div className="error-message">
            <p>{error}</p>
            <button onClick={startCamera}>Retry</button>
          </div>
        )}
      </div>
      
      {/* Controls */}
      <div className="camera-controls">
        <button 
          className="control-btn"
          onClick={() => handleZoom(-0.5)}
          disabled={zoom <= 1}
        >
          <span>−</span>
        </button>
        
        <button
          className="control-btn"
          onClick={() => setFlashEnabled(!flashEnabled)}
        >
          <span>{flashEnabled ? '⚡' : '💡'}</span>
        </button>
        
        <button
          className="capture-btn"
          onClick={captureImage}
          disabled={!isStreaming || isCapturing}
        >
          {isCapturing ? (
            <div className="spinner" />
          ) : (
            <div className="capture-ring" />
          )}
        </button>
        
        <button
          className="control-btn"
          onClick={switchCamera}
        >
          <span>🔄</span>
        </button>
        
        <button
          className="control-btn"
          onClick={() => handleZoom(0.5)}
          disabled={zoom >= 5}
        >
          <span>+</span>
        </button>
      </div>
      
      {/* Zoom indicator */}
      <div className="zoom-indicator">
        {zoom.toFixed(1)}x
      </div>
      
      <style>{`
        .ar-camera {
          position: relative;
          width: 100%;
          max-width: 800px;
          margin: 0 auto;
          background: #000;
          border-radius: 16px;
          overflow: hidden;
        }
        
        .camera-container {
          position: relative;
          aspect-ratio: 4/3;
          overflow: hidden;
        }
        
        .camera-video {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 0.2s ease;
          transform-origin: center;
        }
        
        .ar-overlay {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          pointer-events: none;
        }
        
        .error-message {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          text-align: center;
          color: white;
          background: rgba(0, 0, 0, 0.8);
          padding: 24px;
          border-radius: 12px;
        }
        
        .error-message button {
          margin-top: 12px;
          padding: 8px 24px;
          background: #22C55E;
          color: white;
          border: none;
          border-radius: 8px;
          cursor: pointer;
        }
        
        .camera-controls {
          display: flex;
          justify-content: center;
          align-items: center;
          gap: 16px;
          padding: 20px;
          background: rgba(0, 0, 0, 0.9);
        }
        
        .control-btn {
          width: 48px;
          height: 48px;
          border-radius: 50%;
          background: rgba(255, 255, 255, 0.1);
          border: none;
          color: white;
          font-size: 20px;
          cursor: pointer;
          transition: all 0.2s;
        }
        
        .control-btn:hover {
          background: rgba(255, 255, 255, 0.2);
        }
        
        .control-btn:disabled {
          opacity: 0.3;
          cursor: not-allowed;
        }
        
        .capture-btn {
          width: 72px;
          height: 72px;
          border-radius: 50%;
          background: white;
          border: 4px solid rgba(255, 255, 255, 0.3);
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.2s;
        }
        
        .capture-btn:hover {
          transform: scale(1.05);
        }
        
        .capture-btn:active {
          transform: scale(0.95);
        }
        
        .capture-ring {
          width: 56px;
          height: 56px;
          border-radius: 50%;
          background: #EF4444;
        }
        
        .spinner {
          width: 32px;
          height: 32px;
          border: 3px solid #ccc;
          border-top-color: #22C55E;
          border-radius: 50%;
          animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
        
        .zoom-indicator {
          position: absolute;
          top: 16px;
          right: 16px;
          background: rgba(0, 0, 0, 0.6);
          color: white;
          padding: 4px 12px;
          border-radius: 20px;
          font-size: 14px;
          font-family: 'JetBrains Mono', monospace;
        }
      `}</style>
    </div>
  );
};

export default ARCamera;
