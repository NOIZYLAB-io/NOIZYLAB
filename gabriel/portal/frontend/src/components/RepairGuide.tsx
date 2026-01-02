import React, { useState, useEffect, useRef } from 'react';

interface RepairStep {
  id: string;
  title: string;
  description: string;
  duration: string;
  tools: string[];
  difficulty: 'easy' | 'medium' | 'hard' | 'expert';
  warnings?: string[];
  tips?: string[];
  videoUrl?: string;
  imageUrl?: string;
}

interface RepairGuideProps {
  boardType: string;
  issueType: string;
  component: string;
  onComplete?: () => void;
}

// Sample repair guides database
const REPAIR_GUIDES: Record<string, RepairStep[]> = {
  'cold_solder': [
    {
      id: '1',
      title: 'Identify Cold Solder Joints',
      description: 'Look for dull, grainy, or cracked solder joints. Cold solder joints often appear frosty rather than shiny.',
      duration: '2 min',
      tools: ['Magnifying glass', 'Good lighting'],
      difficulty: 'easy',
      tips: ['Use a 10x loupe for best results', 'Compare to known good joints nearby'],
    },
    {
      id: '2',
      title: 'Clean the Area',
      description: 'Apply flux to the affected joint. This helps the solder flow properly during reflow.',
      duration: '1 min',
      tools: ['Flux pen', 'IPA', 'Cotton swabs'],
      difficulty: 'easy',
      tips: ['Use no-clean flux for convenience'],
    },
    {
      id: '3',
      title: 'Reflow the Joint',
      description: 'Heat the joint with your soldering iron until the solder melts and flows. Add a tiny bit of fresh solder if needed.',
      duration: '30 sec',
      tools: ['Soldering iron (350°C)', 'Solder wire', 'Flux'],
      difficulty: 'medium',
      warnings: ['Don\'t overheat - keep iron contact under 3 seconds', 'Avoid nearby components'],
      tips: ['Touch iron to both pad and pin simultaneously', 'Watch for solder to "wet" and flow'],
    },
    {
      id: '4',
      title: 'Inspect the Repair',
      description: 'The joint should now appear shiny and have a smooth, concave fillet. Test functionality.',
      duration: '2 min',
      tools: ['Magnifying glass', 'Multimeter'],
      difficulty: 'easy',
      tips: ['Check for continuity', 'Verify no bridges to adjacent pins'],
    },
  ],
  'bridged': [
    {
      id: '1',
      title: 'Identify Solder Bridges',
      description: 'Look for unwanted solder connections between adjacent pins or pads.',
      duration: '2 min',
      tools: ['Magnifying glass', 'Good lighting'],
      difficulty: 'easy',
    },
    {
      id: '2',
      title: 'Apply Flux',
      description: 'Generously apply flux to the bridged area. Flux helps solder flow back to where it belongs.',
      duration: '30 sec',
      tools: ['Flux pen or paste'],
      difficulty: 'easy',
    },
    {
      id: '3',
      title: 'Use Solder Wick',
      description: 'Place solder wick over the bridge and heat with iron. The wick will absorb excess solder.',
      duration: '1 min',
      tools: ['Solder wick', 'Soldering iron'],
      difficulty: 'medium',
      warnings: ['Work quickly to avoid heat damage'],
      tips: ['Fresh wick works best', 'Cut off used sections as you go'],
    },
    {
      id: '4',
      title: 'Alternative: Drag Soldering',
      description: 'With a clean, tinned tip, drag across the pins. Surface tension pulls solder to individual pins.',
      duration: '30 sec',
      tools: ['Soldering iron with chisel tip', 'Flux'],
      difficulty: 'hard',
      tips: ['Practice on scrap boards first'],
    },
    {
      id: '5',
      title: 'Verify Repair',
      description: 'Inspect under magnification. Test continuity between pins that should be isolated.',
      duration: '2 min',
      tools: ['Magnifying glass', 'Multimeter'],
      difficulty: 'easy',
    },
  ],
  'missing': [
    {
      id: '1',
      title: 'Identify Component Value',
      description: 'Use board schematic, markings, or measurement to determine the correct replacement component.',
      duration: '5 min',
      tools: ['Schematic', 'Multimeter', 'Component database'],
      difficulty: 'medium',
      tips: ['Check nearby similar components', 'Search the board designation online'],
    },
    {
      id: '2',
      title: 'Source Replacement',
      description: 'Find a matching component from donor board, distributor, or component supplier.',
      duration: 'Varies',
      tools: ['Donor board', 'Component supplier'],
      difficulty: 'easy',
    },
    {
      id: '3',
      title: 'Prepare Pads',
      description: 'Clean the pads with flux and ensure they\'re tinned and ready for the new component.',
      duration: '2 min',
      tools: ['Flux', 'Soldering iron', 'Solder wick'],
      difficulty: 'easy',
    },
    {
      id: '4',
      title: 'Place Component',
      description: 'Position the component on the pads. Use tweezers for SMD, or pre-bend leads for through-hole.',
      duration: '1 min',
      tools: ['Tweezers', 'Magnification'],
      difficulty: 'medium',
    },
    {
      id: '5',
      title: 'Solder Component',
      description: 'Tack one corner/pin first, verify alignment, then solder remaining connections.',
      duration: '2 min',
      tools: ['Soldering iron', 'Solder', 'Flux'],
      difficulty: 'medium',
      warnings: ['Double-check orientation before soldering'],
    },
    {
      id: '6',
      title: 'Test Functionality',
      description: 'Power on and verify the repair restored functionality.',
      duration: '5 min',
      tools: ['Power supply', 'Multimeter', 'Test equipment'],
      difficulty: 'easy',
    },
  ],
  'damaged': [
    {
      id: '1',
      title: 'Assess Damage Extent',
      description: 'Determine if the component can be repaired in place or needs replacement.',
      duration: '3 min',
      tools: ['Magnifying glass', 'Multimeter'],
      difficulty: 'medium',
    },
    {
      id: '2',
      title: 'Remove Damaged Component',
      description: 'Use hot air or soldering iron to remove the damaged component.',
      duration: '3 min',
      tools: ['Hot air station', 'Soldering iron', 'Tweezers', 'Flux'],
      difficulty: 'hard',
      warnings: ['Protect nearby components with kapton tape', 'Use lowest effective temperature'],
    },
    {
      id: '3',
      title: 'Clean Site',
      description: 'Remove old solder and clean pads. Repair any lifted pads with jumper wires if needed.',
      duration: '5 min',
      tools: ['Solder wick', 'IPA', 'Jumper wire'],
      difficulty: 'medium',
    },
    {
      id: '4',
      title: 'Install Replacement',
      description: 'Place and solder the new component following proper technique for the package type.',
      duration: '5 min',
      tools: ['Soldering iron or hot air', 'Solder paste or wire', 'Flux'],
      difficulty: 'hard',
    },
    {
      id: '5',
      title: 'Verify Repair',
      description: 'Test all connections and functionality. Check for shorts and proper values.',
      duration: '5 min',
      tools: ['Multimeter', 'Oscilloscope', 'Power supply'],
      difficulty: 'medium',
    },
  ],
};

export default function RepairGuide({
  boardType,
  issueType,
  component,
  onComplete,
}: RepairGuideProps) {
  const [currentStep, setCurrentStep] = useState(0);
  const [completedSteps, setCompletedSteps] = useState<Set<string>>(new Set());
  const [isPlaying, setIsPlaying] = useState(false);
  const [timer, setTimer] = useState(0);
  const timerRef = useRef<NodeJS.Timeout | null>(null);

  const steps = REPAIR_GUIDES[issueType] || REPAIR_GUIDES['damaged'];
  const step = steps[currentStep];

  useEffect(() => {
    if (isPlaying) {
      timerRef.current = setInterval(() => {
        setTimer(t => t + 1);
      }, 1000);
    }
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [isPlaying]);

  const toggleStep = (stepId: string) => {
    const newCompleted = new Set(completedSteps);
    if (newCompleted.has(stepId)) {
      newCompleted.delete(stepId);
    } else {
      newCompleted.add(stepId);
    }
    setCompletedSteps(newCompleted);
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const difficultyColors = {
    easy: 'bg-green-500/20 text-green-400',
    medium: 'bg-yellow-500/20 text-yellow-400',
    hard: 'bg-orange-500/20 text-orange-400',
    expert: 'bg-red-500/20 text-red-400',
  };

  const progress = (completedSteps.size / steps.length) * 100;

  return (
    <div className="flex flex-col h-full bg-gray-950 text-white">
      {/* Header */}
      <header className="p-6 border-b border-gray-800">
        <div className="flex justify-between items-start">
          <div>
            <p className="text-gray-400 text-sm">{boardType}</p>
            <h1 className="text-2xl font-bold mt-1">
              Repair: {issueType.replace('_', ' ')} - {component}
            </h1>
          </div>
          <div className="flex items-center gap-4">
            {/* Timer */}
            <div className="text-right">
              <p className="text-3xl font-mono">{formatTime(timer)}</p>
              <button
                onClick={() => setIsPlaying(!isPlaying)}
                className={`text-sm px-3 py-1 rounded ${
                  isPlaying ? 'bg-red-500/20 text-red-400' : 'bg-green-500/20 text-green-400'
                }`}
              >
                {isPlaying ? '⏸ Pause' : '▶ Start'} Timer
              </button>
            </div>
          </div>
        </div>
        
        {/* Progress bar */}
        <div className="mt-4">
          <div className="flex justify-between text-sm mb-1">
            <span className="text-gray-400">Progress</span>
            <span>{completedSteps.size}/{steps.length} steps</span>
          </div>
          <div className="h-2 bg-gray-800 rounded-full overflow-hidden">
            <div
              className="h-full bg-green-500 transition-all duration-300"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>
      </header>

      <div className="flex flex-1 overflow-hidden">
        {/* Steps sidebar */}
        <div className="w-80 border-r border-gray-800 overflow-y-auto">
          <div className="p-4">
            <h2 className="font-semibold mb-4">Repair Steps</h2>
            <div className="space-y-2">
              {steps.map((s, i) => (
                <button
                  key={s.id}
                  onClick={() => setCurrentStep(i)}
                  className={`w-full p-3 rounded-lg text-left transition-all ${
                    currentStep === i
                      ? 'bg-green-500/20 border border-green-500'
                      : 'bg-gray-900 hover:bg-gray-800'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <div
                      className={`w-6 h-6 rounded-full flex items-center justify-center text-sm ${
                        completedSteps.has(s.id)
                          ? 'bg-green-500 text-black'
                          : 'bg-gray-700'
                      }`}
                    >
                      {completedSteps.has(s.id) ? '✓' : i + 1}
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className={`font-medium truncate ${
                        completedSteps.has(s.id) ? 'text-gray-400 line-through' : ''
                      }`}>
                        {s.title}
                      </p>
                      <p className="text-xs text-gray-500">{s.duration}</p>
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Main content */}
        <div className="flex-1 overflow-y-auto">
          <div className="p-8 max-w-3xl mx-auto">
            {/* Step header */}
            <div className="flex items-start justify-between mb-6">
              <div>
                <p className="text-gray-400 text-sm">Step {currentStep + 1} of {steps.length}</p>
                <h2 className="text-2xl font-bold mt-1">{step.title}</h2>
              </div>
              <div className="flex items-center gap-2">
                <span className={`px-3 py-1 rounded text-sm ${difficultyColors[step.difficulty]}`}>
                  {step.difficulty}
                </span>
                <span className="text-gray-400">{step.duration}</span>
              </div>
            </div>

            {/* Description */}
            <p className="text-lg text-gray-300 mb-8">{step.description}</p>

            {/* Tools needed */}
            <div className="bg-gray-900 rounded-xl p-6 mb-6">
              <h3 className="font-semibold mb-3 flex items-center gap-2">
                🔧 Tools Needed
              </h3>
              <div className="flex flex-wrap gap-2">
                {step.tools.map((tool) => (
                  <span
                    key={tool}
                    className="px-3 py-1 bg-gray-800 rounded-full text-sm"
                  >
                    {tool}
                  </span>
                ))}
              </div>
            </div>

            {/* Warnings */}
            {step.warnings && step.warnings.length > 0 && (
              <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-6 mb-6">
                <h3 className="font-semibold mb-3 flex items-center gap-2 text-red-400">
                  ⚠️ Warnings
                </h3>
                <ul className="space-y-2">
                  {step.warnings.map((warning, i) => (
                    <li key={i} className="text-red-300 flex items-start gap-2">
                      <span className="text-red-500">•</span>
                      {warning}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Tips */}
            {step.tips && step.tips.length > 0 && (
              <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-6 mb-6">
                <h3 className="font-semibold mb-3 flex items-center gap-2 text-blue-400">
                  💡 Pro Tips
                </h3>
                <ul className="space-y-2">
                  {step.tips.map((tip, i) => (
                    <li key={i} className="text-blue-300 flex items-start gap-2">
                      <span className="text-blue-500">•</span>
                      {tip}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Navigation */}
            <div className="flex items-center gap-4 mt-8">
              <button
                onClick={() => setCurrentStep(Math.max(0, currentStep - 1))}
                disabled={currentStep === 0}
                className="px-6 py-3 bg-gray-800 rounded-lg disabled:opacity-50"
              >
                ← Previous
              </button>
              
              <button
                onClick={() => toggleStep(step.id)}
                className={`flex-1 py-3 rounded-lg font-semibold transition-colors ${
                  completedSteps.has(step.id)
                    ? 'bg-gray-700 text-gray-300'
                    : 'bg-green-500 text-black'
                }`}
              >
                {completedSteps.has(step.id) ? '↩ Mark Incomplete' : '✓ Mark Complete'}
              </button>
              
              {currentStep < steps.length - 1 ? (
                <button
                  onClick={() => setCurrentStep(currentStep + 1)}
                  className="px-6 py-3 bg-gray-800 rounded-lg"
                >
                  Next →
                </button>
              ) : (
                <button
                  onClick={() => {
                    if (completedSteps.size === steps.length) {
                      onComplete?.();
                    }
                  }}
                  disabled={completedSteps.size !== steps.length}
                  className="px-6 py-3 bg-green-500 text-black rounded-lg disabled:opacity-50"
                >
                  🎉 Finish
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
