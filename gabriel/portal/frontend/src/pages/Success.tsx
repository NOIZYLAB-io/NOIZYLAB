import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';

export default function Success() {
  const [searchParams] = useSearchParams();
  const [loading, setLoading] = useState(true);
  const [purchase, setPurchase] = useState<{
    product: string;
    scans: number;
  } | null>(null);

  useEffect(() => {
    const sessionId = searchParams.get('session_id');
    
    if (sessionId) {
      // Verify the session with backend
      fetch(`/api/verify-session?session_id=${sessionId}`)
        .then(res => res.json())
        .then(data => {
          setPurchase(data);
        })
        .catch(console.error)
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, [searchParams]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="spinner" />
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-16 text-center">
      <div className="max-w-md mx-auto">
        {/* Success Animation */}
        <div className="w-24 h-24 bg-green-500 rounded-full flex items-center justify-center mx-auto mb-8 animate-pulse-green">
          <svg className="w-12 h-12 text-black" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
          </svg>
        </div>

        <h1 className="text-3xl font-bold mb-4">Payment Successful!</h1>
        
        <p className="text-gray-400 mb-8">
          Thank you for your purchase. Your scan credits have been added to your account.
        </p>

        {purchase && (
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 mb-8">
            <p className="text-gray-400 text-sm">You purchased</p>
            <p className="text-2xl font-bold text-green-500">
              {purchase.scans === -1 ? 'Unlimited' : purchase.scans} Scan{purchase.scans !== 1 ? 's' : ''}
            </p>
            <p className="text-gray-400 text-sm mt-1">{purchase.product}</p>
          </div>
        )}

        <div className="flex flex-col gap-4">
          <a href="/scan" className="btn-primary">
            Start Scanning
          </a>
          <a href="/dashboard" className="btn-secondary">
            Go to Dashboard
          </a>
        </div>

        {/* Receipt notice */}
        <p className="text-gray-500 text-sm mt-8">
          A receipt has been sent to your email address.
        </p>
      </div>
    </div>
  );
}
