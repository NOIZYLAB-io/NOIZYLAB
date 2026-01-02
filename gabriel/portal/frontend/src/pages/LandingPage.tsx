import React, { useState, useEffect } from 'react';

const LandingPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [scanCount, setScanCount] = useState(47832);
  
  // Animate counter
  useEffect(() => {
    const interval = setInterval(() => {
      setScanCount(prev => prev + Math.floor(Math.random() * 3));
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleWaitlist = (e: React.FormEvent) => {
    e.preventDefault();
    // API call would go here
    setSubmitted(true);
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-slate-900/90 backdrop-blur border-b border-slate-800">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🔬</span>
            <span className="text-xl font-bold text-amber-500">GABRIEL</span>
          </div>
          <div className="hidden md:flex items-center gap-8">
            <a href="#features" className="text-slate-300 hover:text-white transition">Features</a>
            <a href="#pricing" className="text-slate-300 hover:text-white transition">Pricing</a>
            <a href="#demo" className="text-slate-300 hover:text-white transition">Demo</a>
            <a href="/docs" className="text-slate-300 hover:text-white transition">Docs</a>
          </div>
          <div className="flex items-center gap-4">
            <a href="/login" className="text-slate-300 hover:text-white transition">Log in</a>
            <a 
              href="/signup" 
              className="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold rounded-lg transition"
            >
              Start Free
            </a>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4">
        <div className="max-w-6xl mx-auto text-center">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-amber-500/10 border border-amber-500/30 rounded-full text-amber-400 text-sm mb-8">
            <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
            {scanCount.toLocaleString()} boards inspected
          </div>
          
          <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
            AI-Powered
            <span className="block text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-500">
              Board Inspection
            </span>
          </h1>
          
          <p className="text-xl md:text-2xl text-slate-400 max-w-3xl mx-auto mb-10">
            Point your camera at any PCB. Get instant diagnosis, repair guidance, 
            and AR overlays showing exactly what's wrong.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-16">
            <a 
              href="/scan" 
              className="px-8 py-4 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-slate-900 font-bold text-lg rounded-lg transition transform hover:scale-105 flex items-center justify-center gap-2"
            >
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              Try Free Scan
            </a>
            <a 
              href="#demo" 
              className="px-8 py-4 bg-slate-800 hover:bg-slate-700 border border-slate-700 font-semibold text-lg rounded-lg transition flex items-center justify-center gap-2"
            >
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Watch Demo
            </a>
          </div>

          {/* Hero Image */}
          <div className="relative max-w-4xl mx-auto">
            <div className="absolute -inset-4 bg-gradient-to-r from-amber-500/20 to-orange-500/20 rounded-2xl blur-xl"></div>
            <div className="relative bg-slate-800 rounded-xl overflow-hidden border border-slate-700 shadow-2xl">
              <div className="aspect-video bg-slate-900 flex items-center justify-center">
                {/* Placeholder for demo video/image */}
                <div className="text-center">
                  <div className="text-6xl mb-4">🔍</div>
                  <p className="text-slate-400">Interactive Demo Preview</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Trust Badges */}
      <section className="py-12 border-y border-slate-800 bg-slate-800/30">
        <div className="max-w-6xl mx-auto px-4">
          <p className="text-center text-slate-400 mb-8">Trusted by repair professionals worldwide</p>
          <div className="flex flex-wrap justify-center items-center gap-8 md:gap-16">
            {['iFixit', 'Louis Rossmann', 'Jessa Jones', 'Northridge Fix', 'Hugh Jeffreys'].map((name) => (
              <div key={name} className="text-slate-500 font-semibold text-lg">{name}</div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold mb-4">How GABRIEL Works</h2>
            <p className="text-xl text-slate-400">Three simple steps to diagnose any board</p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: '📸',
                title: 'Snap a Photo',
                description: 'Use your phone or webcam to capture the board. Our AI works with any angle, any lighting.',
              },
              {
                icon: '🤖',
                title: 'AI Analysis',
                description: 'Gemini 3 Flash compares your board against golden references, identifying issues in seconds.',
              },
              {
                icon: '🎯',
                title: 'AR Guidance',
                description: 'See exactly where problems are with augmented reality overlays and step-by-step repair instructions.',
              },
            ].map((feature, index) => (
              <div key={index} className="bg-slate-800 rounded-xl p-8 border border-slate-700 hover:border-amber-500/50 transition group">
                <div className="text-5xl mb-4">{feature.icon}</div>
                <h3 className="text-xl font-semibold mb-2 group-hover:text-amber-400 transition">{feature.title}</h3>
                <p className="text-slate-400">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Capabilities Grid */}
      <section className="py-20 px-4 bg-slate-800/30">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-4xl font-bold mb-6">Detect Any Issue</h2>
              <div className="space-y-4">
                {[
                  'Cold solder joints',
                  'Missing components',
                  'Bridged pins',
                  'Physical damage',
                  'Corrosion & liquid damage',
                  'Misaligned parts',
                  'Wrong components',
                  'Heat damage',
                ].map((issue, index) => (
                  <div key={index} className="flex items-center gap-3">
                    <div className="w-6 h-6 rounded-full bg-green-500/20 flex items-center justify-center">
                      <svg className="w-4 h-4 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    </div>
                    <span className="text-lg">{issue}</span>
                  </div>
                ))}
              </div>
            </div>
            <div className="bg-slate-800 rounded-xl p-8 border border-slate-700">
              <div className="aspect-square bg-slate-900 rounded-lg flex items-center justify-center">
                <div className="text-center">
                  <div className="text-8xl mb-4">🔬</div>
                  <p className="text-slate-400">Live Detection Preview</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold mb-4">Simple Pricing</h2>
            <p className="text-xl text-slate-400">Start free, pay as you grow</p>
          </div>

          <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
            {/* Free Tier */}
            <div className="bg-slate-800 rounded-xl p-8 border border-slate-700">
              <h3 className="text-xl font-semibold mb-2">Golden Audit</h3>
              <div className="text-4xl font-bold mb-4">$4.99<span className="text-lg text-slate-400">/scan</span></div>
              <p className="text-slate-400 mb-6">Perfect for occasional repairs</p>
              <ul className="space-y-3 mb-8">
                {['Pay per scan', 'Full AI analysis', 'AR overlay', 'PDF report'].map((feature) => (
                  <li key={feature} className="flex items-center gap-2 text-slate-300">
                    <svg className="w-5 h-5 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    {feature}
                  </li>
                ))}
              </ul>
              <a href="/scan" className="block w-full py-3 text-center bg-slate-700 hover:bg-slate-600 rounded-lg font-semibold transition">
                Try Now
              </a>
            </div>

            {/* Pro Tier */}
            <div className="bg-gradient-to-b from-amber-500/10 to-transparent rounded-xl p-8 border-2 border-amber-500 relative">
              <div className="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 bg-amber-500 text-slate-900 text-sm font-bold rounded-full">
                MOST POPULAR
              </div>
              <h3 className="text-xl font-semibold mb-2">Legacy Kit</h3>
              <div className="text-4xl font-bold mb-4">$29<span className="text-lg text-slate-400">/month</span></div>
              <p className="text-slate-400 mb-6">For repair shops</p>
              <ul className="space-y-3 mb-8">
                {['10 scans/month', 'Priority processing', 'Voice guidance', 'Custom references', 'Team access (3)', 'API access'].map((feature) => (
                  <li key={feature} className="flex items-center gap-2 text-slate-300">
                    <svg className="w-5 h-5 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    {feature}
                  </li>
                ))}
              </ul>
              <a href="/signup?plan=pro" className="block w-full py-3 text-center bg-amber-500 hover:bg-amber-600 text-slate-900 rounded-lg font-bold transition">
                Start Free Trial
              </a>
            </div>

            {/* Enterprise */}
            <div className="bg-slate-800 rounded-xl p-8 border border-slate-700">
              <h3 className="text-xl font-semibold mb-2">Enterprise</h3>
              <div className="text-4xl font-bold mb-4">$99<span className="text-lg text-slate-400">/month</span></div>
              <p className="text-slate-400 mb-6">For manufacturers</p>
              <ul className="space-y-3 mb-8">
                {['Unlimited scans', 'White-label reports', 'SSO/SAML', 'Custom AI training', 'Dedicated support', 'SLA guarantee'].map((feature) => (
                  <li key={feature} className="flex items-center gap-2 text-slate-300">
                    <svg className="w-5 h-5 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    {feature}
                  </li>
                ))}
              </ul>
              <a href="/contact" className="block w-full py-3 text-center bg-slate-700 hover:bg-slate-600 rounded-lg font-semibold transition">
                Contact Sales
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Waitlist CTA */}
      <section className="py-20 px-4 bg-gradient-to-r from-amber-500/10 to-orange-500/10">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-4">Ready to Transform Your Repairs?</h2>
          <p className="text-xl text-slate-400 mb-8">
            Join thousands of repair professionals using AI to diagnose faster.
          </p>
          
          {submitted ? (
            <div className="bg-green-500/20 border border-green-500 rounded-lg p-6">
              <div className="text-4xl mb-2">🎉</div>
              <p className="text-green-400 font-semibold">You're on the list! Check your email for next steps.</p>
            </div>
          ) : (
            <form onSubmit={handleWaitlist} className="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email"
                className="flex-1 px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500"
                required
              />
              <button 
                type="submit"
                className="px-6 py-3 bg-amber-500 hover:bg-amber-600 text-slate-900 font-bold rounded-lg transition"
              >
                Get Started
              </button>
            </form>
          )}
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-4 border-t border-slate-800">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <span className="text-2xl">🔬</span>
                <span className="text-xl font-bold text-amber-500">GABRIEL</span>
              </div>
              <p className="text-slate-400 text-sm">
                Generative Adversarial Board Inspection for Electronic Logic
              </p>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Product</h4>
              <ul className="space-y-2 text-slate-400">
                <li><a href="/features" className="hover:text-white transition">Features</a></li>
                <li><a href="/pricing" className="hover:text-white transition">Pricing</a></li>
                <li><a href="/docs" className="hover:text-white transition">Documentation</a></li>
                <li><a href="/changelog" className="hover:text-white transition">Changelog</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Company</h4>
              <ul className="space-y-2 text-slate-400">
                <li><a href="/about" className="hover:text-white transition">About</a></li>
                <li><a href="/blog" className="hover:text-white transition">Blog</a></li>
                <li><a href="/careers" className="hover:text-white transition">Careers</a></li>
                <li><a href="/contact" className="hover:text-white transition">Contact</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Legal</h4>
              <ul className="space-y-2 text-slate-400">
                <li><a href="/privacy" className="hover:text-white transition">Privacy</a></li>
                <li><a href="/terms" className="hover:text-white transition">Terms</a></li>
                <li><a href="/security" className="hover:text-white transition">Security</a></li>
              </ul>
            </div>
          </div>
          
          <div className="flex flex-col md:flex-row justify-between items-center pt-8 border-t border-slate-800">
            <p className="text-slate-400 text-sm">© 2025 NOIZYLAB. All rights reserved.</p>
            <div className="flex gap-4 mt-4 md:mt-0">
              <a href="https://twitter.com/noizylab" className="text-slate-400 hover:text-white transition">
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
              </a>
              <a href="https://github.com/Noizyfish" className="text-slate-400 hover:text-white transition">
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path fillRule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.17 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.604-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.464-1.11-1.464-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.167 22 16.418 22 12c0-5.523-4.477-10-10-10z" clipRule="evenodd"/></svg>
              </a>
              <a href="https://discord.gg/noizylab" className="text-slate-400 hover:text-white transition">
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 00-5.487 0 12.64 12.64 0 00-.617-1.25.077.077 0 00-.079-.037A19.736 19.736 0 003.677 4.37a.07.07 0 00-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 00.031.057 19.9 19.9 0 005.993 3.03.078.078 0 00.084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 00-.041-.106 13.107 13.107 0 01-1.872-.892.077.077 0 01-.008-.128 10.2 10.2 0 00.372-.292.074.074 0 01.077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 01.078.01c.12.098.246.198.373.292a.077.077 0 01-.006.127 12.299 12.299 0 01-1.873.892.077.077 0 00-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 00.084.028 19.839 19.839 0 006.002-3.03.077.077 0 00.032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 00-.031-.03z"/></svg>
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
