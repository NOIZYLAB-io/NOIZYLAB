#!/usr/bin/env python3
"""
🧞‍♂️ NOIZYGENIE'S GITLENS SUPERPOWERS GUIDE 🔮
==============================================
Your magical guide to GitLens awesomeness!
"""

def gitlens_superpowers():
    print("🌟 GITLENS MAGICAL FEATURES TO CLICK & EXPLORE:")
    print("=" * 60)
    
    features = {
        "🔍 File Annotations": {
            "what": "See who wrote each line of code",
            "why": "Instantly know who to ask about any code!",
            "action": "Click the 'Toggle File Annotations' in any file"
        },
        
        "📊 Git Graph": {
            "what": "Visual timeline of all commits",
            "why": "See your project's entire history like a movie!",
            "action": "Click 'Git Graph' in the Source Control panel"
        },
        
        "🔍 Blame Annotations": {
            "what": "Hover over any line to see commit details",
            "why": "Understand WHY code was written, not just WHO",
            "action": "Just hover over any line - magic happens!"
        },
        
        "🌳 Repository Explorer": {
            "what": "Navigate commits, branches, tags visually",
            "why": "Like a GPS for your Git repository!",
            "action": "Open GitLens sidebar (click GitLens icon)"
        },
        
        "⚡ Quick Actions": {
            "what": "Compare, checkout, cherry-pick with one click",
            "why": "Git commands become point-and-click simple!",
            "action": "Right-click any commit for magic menu"
        },
        
        "🔮 Line History": {
            "what": "See how any line evolved over time",
            "why": "Time travel through your code's evolution!",
            "action": "Right-click a line → 'Show Line History'"
        },
        
        "📈 Insights & Analytics": {
            "what": "See repository statistics and trends",
            "why": "Understand your team's coding patterns!",
            "action": "GitLens sidebar → Repositories → Your repo"
        },
        
        "🎯 Current Line Blame": {
            "what": "See commit info for current cursor line",
            "why": "Instant context without clicking anything!",
            "action": "Already enabled - just move your cursor!"
        }
    }
    
    for feature, details in features.items():
        print(f"\n{feature}")
        print(f"   💡 What: {details['what']}")
        print(f"   🎯 Why: {details['why']}")
        print(f"   🚀 Action: {details['action']}")
        print("   " + "─" * 50)
    
    print(f"\n🧞‍♂️ NOIZYGENIE'S COOLEST GITLENS TRICKS:")
    print("✨ Cmd/Ctrl + Shift + P → 'GitLens: Show Quick Commit Details'")
    print("🔥 Click any commit hash → See full commit details")
    print("⚡ Use GitLens Compare feature → See changes between any commits")
    print("🎨 GitLens Heat Map → See which files change most often")
    
    print(f"\n🎉 PRO TIP: GitLens turns Git from scary to MAGICAL! 🪄")

if __name__ == "__main__":
    print("🧞‍♂️ Welcome to GitLens Mastery Training!")
    gitlens_superpowers()
    print("\n💫 Now go click ALL the GitLens things! Your Git skills will level up instantly! 🚀")