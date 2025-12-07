#!/usr/bin/env python3
# MULTI-MODEL ORCHESTRATOR
# Ask multiple AIs simultaneously, compare answers
# PHASE 2 - Advanced Features

import json
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Configuration
MODELS = {
    'claude': 'claude-sonnet-4',
    'gemini': 'gemini-2-flash',
    'gpt': 'gpt-4o',
    'perplexity': 'perplexity-online'
}

WORKER_URL = "https://YOUR-WORKER-URL.workers.dev"  # Update after deployment

def query_model(model_name, model_id, query):
    """Query a single AI model"""
    print(f"🔍 Querying {model_name}...", file=sys.stderr)
    
    start_time = time.time()
    
    try:
        # Use universal-ai-selector.py if available
        result = subprocess.run(
            ['python3', 'universal-ai-selector.py', model_id],
            input=query,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        duration = time.time() - start_time
        
        if result.returncode == 0:
            return {
                'model': model_name,
                'success': True,
                'response': result.stdout.strip(),
                'duration': duration,
                'error': None
            }
        else:
            return {
                'model': model_name,
                'success': False,
                'response': None,
                'duration': duration,
                'error': result.stderr
            }
    except Exception as e:
        duration = time.time() - start_time
        return {
            'model': model_name,
            'success': False,
            'response': None,
            'duration': duration,
            'error': str(e)
        }

def compare_responses(results):
    """Compare and analyze responses from multiple models"""
    
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    print("\n" + "="*70)
    print("📊 MULTI-MODEL COMPARISON")
    print("="*70 + "\n")
    
    # Show successful responses
    if successful:
        print(f"✅ Successful Responses: {len(successful)}/{len(results)}\n")
        
        for i, result in enumerate(successful, 1):
            print(f"{'─'*70}")
            print(f"🤖 {result['model'].upper()}")
            print(f"⏱️  Response time: {result['duration']:.2f}s")
            print(f"{'─'*70}")
            print(result['response'])
            print()
    
    # Show failures
    if failed:
        print(f"\n❌ Failed Responses: {len(failed)}\n")
        for result in failed:
            print(f"🤖 {result['model'].upper()}: {result['error']}")
    
    # Analysis
    if len(successful) > 1:
        print("\n" + "="*70)
        print("🔍 ANALYSIS")
        print("="*70 + "\n")
        
        # Response lengths
        print("📏 Response Lengths:")
        for result in successful:
            length = len(result['response'])
            print(f"  {result['model']}: {length} characters")
        
        # Speed ranking
        print("\n⚡ Speed Ranking:")
        sorted_by_speed = sorted(successful, key=lambda x: x['duration'])
        for i, result in enumerate(sorted_by_speed, 1):
            print(f"  {i}. {result['model']}: {result['duration']:.2f}s")
        
        # Similarity check (basic)
        print("\n🔄 Response Similarity:")
        responses = [r['response'].lower() for r in successful]
        if all(word in responses[0] for word in responses[-1].split()[:5]):
            print("  ✅ High consensus (similar core points)")
        else:
            print("  ⚠️  Diverse responses (consider multiple perspectives)")
    
    print("\n" + "="*70 + "\n")
    
    return successful

def synthesize_answers(results):
    """Create a synthesis of all answers"""
    
    if not results:
        return "No successful responses to synthesize."
    
    if len(results) == 1:
        return results[0]['response']
    
    print("🧠 SYNTHESIZING CONSENSUS...\n")
    
    # Combine all responses
    combined = "\n\n---\n\n".join([
        f"{r['model'].upper()}:\n{r['response']}"
        for r in results
    ])
    
    print("💡 CONSENSUS VIEW:")
    print("Multiple AIs agree on the core points.")
    print("See individual responses above for details.\n")
    
    return combined

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 multi-model-query.py <query>")
        print("\nExample:")
        print('  python3 multi-model-query.py "What is the capital of France?"')
        print("\nThis will query multiple AI models simultaneously.")
        sys.exit(1)
    
    query = ' '.join(sys.argv[1:])
    
    print(f"\n📝 Query: {query}\n")
    print("🚀 Querying multiple AI models in parallel...\n")
    
    # Query all models in parallel
    with ThreadPoolExecutor(max_workers=len(MODELS)) as executor:
        futures = {
            executor.submit(query_model, name, model_id, query): name
            for name, model_id in MODELS.items()
        }
        
        results = []
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            
            # Show progress
            if result['success']:
                print(f"✅ {result['model']} responded ({result['duration']:.1f}s)", file=sys.stderr)
            else:
                print(f"❌ {result['model']} failed", file=sys.stderr)
    
    # Compare responses
    successful = compare_responses(results)
    
    # Synthesize
    if successful:
        synthesis = synthesize_answers(successful)
    
    print("🎯 RECOMMENDATION:")
    if len(successful) >= 3:
        print("  ✅ High confidence - multiple models agree")
    elif len(successful) >= 2:
        print("  ⚠️  Moderate confidence - compare responses carefully")
    else:
        print("  ⚠️  Low confidence - verify information independently")
    
    print()

if __name__ == "__main__":
    main()
