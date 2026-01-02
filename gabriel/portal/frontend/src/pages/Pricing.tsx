import React from 'react';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe(import.meta.env.VITE_STRIPE_PUBLIC_KEY || 'pk_test_placeholder');

interface PricingTier {
  id: string;
  name: string;
  price: string;
  period: string;
  description: string;
  features: string[];
  featured?: boolean;
  buttonText: string;
}

const tiers: PricingTier[] = [
  {
    id: 'golden_audit',
    name: 'Golden Audit',
    price: '$4.99',
    period: '/scan',
    description: 'Perfect for DIY repair enthusiasts',
    features: [
      'Single board analysis',
      'AI defect detection',
      'Basic repair guidance',
      'PDF report download',
    ],
    buttonText: 'Buy Single Scan'
  },
  {
    id: 'legacy_kit',
    name: 'Legacy Kit',
    price: '$29',
    period: '/bundle',
    description: 'Vintage electronics restoration',
    features: [
      '10 board scans',
      'Priority processing',
      'AR overlay access',
      'Voice guidance',
      'Component sourcing tips',
    ],
    featured: true,
    buttonText: 'Get Legacy Kit'
  },
  {
    id: 'pro_monthly',
    name: 'Pro',
    price: '$99',
    period: '/month',
    description: 'For repair shops & professionals',
    features: [
      'Unlimited scans',
      'Custom Golden References',
      'Full API access',
      'White-label reports',
      'Priority support',
      'Team management',
    ],
    buttonText: 'Start Free Trial'
  }
];

export default function Pricing() {
  const handlePurchase = async (productId: string) => {
    try {
      const response = await fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          productId,
          successUrl: window.location.origin + '/success?session_id={CHECKOUT_SESSION_ID}',
          cancelUrl: window.location.origin + '/pricing'
        })
      });

      const { url, error } = await response.json();
      
      if (error) {
        alert(error);
        return;
      }

      // Redirect to Stripe Checkout
      window.location.href = url;
    } catch (error) {
      console.error('Payment error:', error);
      alert('Payment system is loading. Please try again.');
    }
  };

  return (
    <div className="container mx-auto px-4 py-16">
      <header className="text-center mb-16">
        <h1 className="text-4xl font-bold mb-4">Simple Pricing</h1>
        <p className="text-gray-400 text-lg">
          Start scanning for $4.99, or go unlimited with Pro
        </p>
      </header>

      <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        {tiers.map((tier) => (
          <PricingCard
            key={tier.id}
            tier={tier}
            onPurchase={() => handlePurchase(tier.id)}
          />
        ))}
      </div>

      {/* FAQ Section */}
      <section className="mt-24 max-w-3xl mx-auto">
        <h2 className="text-2xl font-bold text-center mb-8">Frequently Asked Questions</h2>
        
        <div className="space-y-4">
          <FAQ
            question="How does the scan credit system work?"
            answer="Each scan uses one credit. Golden Audit gives you 1 credit, Legacy Kit gives you 10. Pro subscribers have unlimited scans."
          />
          <FAQ
            question="Do scan credits expire?"
            answer="No, scan credits never expire. Use them whenever you need."
          />
          <FAQ
            question="Can I upgrade to Pro later?"
            answer="Yes! Any unused scan credits will be converted to bonus credits on your Pro account."
          />
          <FAQ
            question="What payment methods do you accept?"
            answer="We accept all major credit cards, Apple Pay, and Google Pay through Stripe."
          />
          <FAQ
            question="Is there a refund policy?"
            answer="Yes, we offer a 30-day money-back guarantee on all purchases."
          />
        </div>
      </section>

      {/* Enterprise CTA */}
      <section className="mt-24 text-center">
        <div className="bg-gradient-to-r from-green-500/10 to-blue-500/10 border border-gray-800 rounded-2xl p-12">
          <h2 className="text-2xl font-bold mb-4">Need Enterprise Features?</h2>
          <p className="text-gray-400 mb-8 max-w-xl mx-auto">
            Custom Golden Reference libraries, on-premise deployment, dedicated support, and more.
          </p>
          <a
            href="mailto:enterprise@noizylab.ai"
            className="btn-secondary inline-block"
          >
            Contact Sales
          </a>
        </div>
      </section>
    </div>
  );
}

function PricingCard({ tier, onPurchase }: { tier: PricingTier; onPurchase: () => void }) {
  return (
    <div
      className={`relative bg-gray-900 border rounded-2xl p-8 ${
        tier.featured
          ? 'border-green-500 scale-105'
          : 'border-gray-800'
      }`}
    >
      {tier.featured && (
        <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-green-500 text-black text-xs font-semibold px-3 py-1 rounded-full">
          Most Popular
        </div>
      )}

      <h3 className="text-2xl font-bold">{tier.name}</h3>
      <div className="mt-4 mb-2">
        <span className="text-4xl font-bold">{tier.price}</span>
        <span className="text-gray-400">{tier.period}</span>
      </div>
      <p className="text-gray-400 text-sm mb-6">{tier.description}</p>

      <ul className="space-y-3 mb-8">
        {tier.features.map((feature, index) => (
          <li key={index} className="flex items-center gap-3 text-sm">
            <span className="text-green-500">✓</span>
            <span className="text-gray-300">{feature}</span>
          </li>
        ))}
      </ul>

      <button
        onClick={onPurchase}
        className={`w-full py-3 rounded-lg font-semibold transition-all ${
          tier.featured
            ? 'bg-green-500 text-black hover:bg-green-400'
            : 'bg-gray-800 text-white hover:bg-gray-700 border border-gray-700'
        }`}
      >
        {tier.buttonText}
      </button>
    </div>
  );
}

function FAQ({ question, answer }: { question: string; answer: string }) {
  const [open, setOpen] = React.useState(false);

  return (
    <div className="border border-gray-800 rounded-xl">
      <button
        onClick={() => setOpen(!open)}
        className="w-full px-6 py-4 flex justify-between items-center text-left"
      >
        <span className="font-medium">{question}</span>
        <span className="text-gray-400">{open ? '−' : '+'}</span>
      </button>
      {open && (
        <div className="px-6 pb-4 text-gray-400">
          {answer}
        </div>
      )}
    </div>
  );
}
