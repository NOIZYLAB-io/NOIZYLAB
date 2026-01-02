import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { loadStripe } from '@stripe/stripe-js';
import { Elements } from '@stripe/react-stripe-js';
import ARCamera from './components/ARCamera';
import Dashboard from './pages/Dashboard';
import ScanResult from './pages/ScanResult';
import Pricing from './pages/Pricing';
import Success from './pages/Success';

// Initialize Stripe
const stripePromise = loadStripe(import.meta.env.VITE_STRIPE_PUBLIC_KEY || 'pk_test_placeholder');

function App() {
  return (
    <Elements stripe={stripePromise}>
      <BrowserRouter>
        <div className="min-h-screen bg-gray-950 text-white">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/scan" element={<ScanPage />} />
            <Route path="/result/:scanId" element={<ScanResult />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/pricing" element={<Pricing />} />
            <Route path="/success" element={<Success />} />
          </Routes>
        </div>
      </BrowserRouter>
    </Elements>
  );
}

// Home Page
function Home() {
  return (
    <div className="container mx-auto px-4 py-16">
      <header className="text-center mb-16">
        <h1 className="text-5xl font-bold mb-4">
          <span className="text-white">Noizy</span>
          <span className="text-green-500">Lab</span>
        </h1>
        <p className="text-xl text-gray-400 mb-8">
          AI-Powered Circuit Board Inspection
        </p>
        <div className="flex gap-4 justify-center">
          <a
            href="/scan"
            className="px-8 py-4 bg-green-500 text-black font-semibold rounded-lg hover:bg-green-400 transition"
          >
            Start Scanning — $4.99
          </a>
          <a
            href="/pricing"
            className="px-8 py-4 bg-gray-800 border border-gray-700 rounded-lg hover:bg-gray-700 transition"
          >
            View Pricing
          </a>
        </div>
      </header>

      <section className="grid md:grid-cols-3 gap-8 mb-16">
        <FeatureCard
          icon="🔍"
          title="AI Defect Detection"
          description="Gemini 3 Flash vision identifies cold solder joints, missing components, and counterfeits"
        />
        <FeatureCard
          icon="📊"
          title="Golden Reference"
          description="Compare against our database of known-good boards instantly"
        />
        <FeatureCard
          icon="🛠️"
          title="Repair Guidance"
          description="Claude AI generates step-by-step repair instructions"
        />
      </section>

      <section className="text-center">
        <h2 className="text-3xl font-bold mb-8">How It Works</h2>
        <div className="flex flex-col md:flex-row justify-center gap-8">
          <Step number={1} title="Take Photo" description="Capture your PCB with smartphone" />
          <Step number={2} title="AI Analysis" description="Compare to Golden References" />
          <Step number={3} title="Get Results" description="Detailed report with AR highlights" />
          <Step number={4} title="Follow Guide" description="Voice-guided repair instructions" />
        </div>
      </section>
    </div>
  );
}

// Scan Page
function ScanPage() {
  const [analyzing, setAnalyzing] = useState(false);
  const [result, setResult] = useState<any>(null);

  const handleCapture = async (imageBlob: Blob) => {
    setAnalyzing(true);
    
    try {
      const formData = new FormData();
      formData.append('image', imageBlob, 'pcb-scan.jpg');
      
      const response = await fetch('/api/scan', {
        method: 'POST',
        body: formData
      });
      
      const data = await response.json();
      setResult(data);
      
      // Navigate to results
      if (data.scanId) {
        window.location.href = `/result/${data.scanId}`;
      }
    } catch (error) {
      console.error('Scan failed:', error);
      alert('Scan failed. Please try again.');
    } finally {
      setAnalyzing(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold">Scan Your Board</h1>
        <p className="text-gray-400">Position your PCB in the camera frame</p>
      </header>

      <ARCamera
        onCapture={handleCapture}
        showGrid={true}
        highlightComponents={result?.analysis?.components || []}
      />

      {analyzing && (
        <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-50">
          <div className="text-center">
            <div className="w-16 h-16 border-4 border-green-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
            <p className="text-xl">Analyzing with AI...</p>
            <p className="text-gray-400">This may take a few seconds</p>
          </div>
        </div>
      )}
    </div>
  );
}

// Feature Card Component
function FeatureCard({ icon, title, description }: { icon: string; title: string; description: string }) {
  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <div className="text-4xl mb-4">{icon}</div>
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <p className="text-gray-400">{description}</p>
    </div>
  );
}

// Step Component
function Step({ number, title, description }: { number: number; title: string; description: string }) {
  return (
    <div className="text-center">
      <div className="w-16 h-16 bg-gray-900 border-2 border-green-500 rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
        {number}
      </div>
      <h4 className="font-semibold mb-1">{title}</h4>
      <p className="text-gray-400 text-sm">{description}</p>
    </div>
  );
}

export default App;
